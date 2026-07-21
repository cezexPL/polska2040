#!/usr/bin/env python3
"""Create a reviewable, versioned snapshot from the generated dist tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
RELEASES = ROOT / "release"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_text_copy(path: Path) -> None:
    """Normalize copied review text without mutating canonical workspace files."""
    text = path.read_text(encoding="utf-8")
    lines = []
    for line in text.splitlines():
        if path.suffix.lower() == ".md" and line.endswith("  "):
            line = line.rstrip() + "<br>"
        else:
            line = line.rstrip()
        lines.append(line)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--version", default="v0.1")
    args = parser.parse_args()
    if not args.version or any(part in args.version for part in ("/", "\\", "..")):
        raise SystemExit("Unsafe release version")
    if not (DIST / "build-manifest.json").exists() or not (DIST / "output-qa.json").exists():
        raise SystemExit("Run make build && make qa before packaging")
    qa = json.loads((DIST / "output-qa.json").read_text(encoding="utf-8"))
    if qa.get("status") != "passed":
        raise SystemExit("Output QA has not passed")

    target = (RELEASES / args.version).resolve()
    if RELEASES.resolve() not in target.parents:
        raise SystemExit("Release target escaped release/")
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(DIST, target)

    # Keep the review snapshot self-contained: independent reports retain their
    # relative links to canonical documents and evidence registries.
    source_ignore = shutil.ignore_patterns("cache", "downloads", "__pycache__", "*.pyc")
    for directory_name in ("documents", "research", "inputs", "orchestration", "tooling"):
        source = ROOT / directory_name
        if source.exists():
            shutil.copytree(source, target / directory_name, ignore=source_ignore)
    for file_name in (
        "AGENTS.md",
        "GOAL.md",
        "METHODOLOGY.md",
        "SECURITY.md",
        "DATA_POLICY.md",
        "Makefile",
        "requirements.txt",
    ):
        source = ROOT / file_name
        if source.exists():
            shutil.copy2(source, target / file_name)
    if (ROOT / "README.md").exists():
        project_readme = (ROOT / "README.md").read_text(encoding="utf-8")
        project_readme = project_readme.replace("](release/README.md)", "](README.md)")
        (target / "PROJECT-README.md").write_text(project_readme, encoding="utf-8")

    # Source Markdown uses project-root asset references understood by the
    # builder. Rewrite only the packaged snapshot to standard file-relative
    # paths so the review bundle remains navigable outside the repository.
    packaged_documents = target / "documents"
    if packaged_documents.exists():
        for markdown_path in packaged_documents.rglob("*.md"):
            asset_prefix = Path(
                os.path.relpath(target / "assets", markdown_path.parent)
            ).as_posix()
            markdown_text = markdown_path.read_text(encoding="utf-8")
            markdown_text = markdown_text.replace("](assets/", f"]({asset_prefix}/")
            markdown_text = markdown_text.replace(
                'src="assets/', f'src="{asset_prefix}/'
            )
            markdown_path.write_text(markdown_text, encoding="utf-8")

    copied_text_roots = [
        target / "documents",
        target / "research",
        target / "inputs",
        target / "orchestration",
        target / "tooling",
        target / "reports",
    ]
    text_suffixes = {".md", ".yaml", ".yml", ".json", ".py", ".txt"}
    for copied_root in copied_text_roots:
        if not copied_root.exists():
            continue
        for text_path in copied_root.rglob("*"):
            if text_path.is_file() and text_path.suffix.lower() in text_suffixes:
                normalize_text_copy(text_path)
    for root_text_name in (
        "PROJECT-README.md",
        "README.md",
        "AGENTS.md",
        "GOAL.md",
        "METHODOLOGY.md",
        "SECURITY.md",
        "DATA_POLICY.md",
        "Makefile",
        "requirements.txt",
    ):
        root_text = target / root_text_name
        if root_text.exists():
            normalize_text_copy(root_text)
    for svg_path in (target / "assets" / "generated").glob("*.svg"):
        normalize_text_copy(svg_path)
    if (RELEASES / "README.md").exists():
        shutil.copy2(RELEASES / "README.md", target / "README.md")
        normalize_text_copy(target / "README.md")
    reports_dir = ROOT / "reports"
    if reports_dir.exists():
        release_reports = target / "reports"
        release_reports.mkdir(parents=True, exist_ok=True)
        for report_path in sorted(reports_dir.glob("*.md")):
            report_text = report_path.read_text(encoding="utf-8")
            # In the workspace reports sit beside dist/; in a versioned package
            # the generated artifacts are already at the package root.
            report_text = report_text.replace("](../dist/", "](../")
            (release_reports / report_path.name).write_text(
                report_text, encoding="utf-8"
            )
            normalize_text_copy(release_reports / report_path.name)

    copied_files = sorted(path for path in target.rglob("*") if path.is_file())
    release_metadata = {
        "version": args.version,
        "status": "independent expert draft for review",
        "evidence_cutoff": date.today().isoformat(),
        "artifact_count": qa["artifact_count"],
        "file_count_excluding_checksums": len(copied_files) + 1,
        "qa_status": qa["status"],
        "canonical_sources": "documents and research (snapshot); live workspace ../../documents and ../../research",
        "publication_requires_human_approval": True,
        "formal_government_submission_ready": False,
        "formal_blocker": "GAP-0011: owner, legal process and strategy hierarchy require competent-authority determination",
    }
    (target / "release-metadata.json").write_text(
        json.dumps(release_metadata, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    files = sorted(
        path for path in target.rglob("*") if path.is_file() and path.name != "SHA256SUMS"
    )
    lines = [f"{sha256(path)}  {path.relative_to(target)}" for path in files]
    (target / "SHA256SUMS").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Packaged {len(files)} files in {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
