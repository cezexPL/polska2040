import {readFileSync, writeFileSync} from "node:fs";

const path=new URL("./index.html",import.meta.url);
let html=readFileSync(path,"utf8");

function replaceExact(before,after,label){
  if(!html.includes(before))throw new Error(`Nie znaleziono fragmentu: ${label}`);
  html=html.replaceAll(before,after);
}

replaceExact(
  "Niezależny program strategiczny 2026–2040: bezpieczeństwo, przemysł, AI, kadry oraz odporność inteligencji i energii.",
  "Niezależny ekspercki program strategiczny 2026–2040: bezpieczeństwo, przemysł, systemy autonomiczne, AI, kadry, partnerstwa i rozwój regionów.",
  "opis SEO"
);
replaceExact(
  "Bezpieczeństwo. Przemysł. AI. Kadry.<br/>Jeden plan działania dla silnej i odpornej Polski.",
  "Zamówienia. Przemysł. AI. Kadry. Partnerstwa. Regiony.<br/>Sześć filarów jednego systemu bezpieczeństwa i rozwoju.",
  "lead hero"
);

const strip='<div class="pillar-strip shell" id="filary"><a class="pillar-tab" href="#pillar-01"><span>01</span><b>Potrzeby i testy</b></a><a class="pillar-tab" href="#pillar-02"><span>02</span><b>Przemysł</b></a><a class="pillar-tab" href="#pillar-03"><span>03</span><b>Autonomia i AI</b></a><a class="pillar-tab" href="#pillar-04"><span>04</span><b>Kadry</b></a><a class="pillar-tab" href="#pillar-05"><span>05</span><b>Partnerstwa</b></a><a class="pillar-tab" href="#pillar-06"><span>06</span><b>Regiony i eksport</b></a></div>';
const stripPattern=/<div class="pillar-strip shell" id="filary">.*?<\/div><\/section><section class="manifesto/s;
if(!stripPattern.test(html))throw new Error("Nie znaleziono paska filarów");
html=html.replace(stripPattern,`${strip}</section><section class="manifesto`);

const signals='<div class="card-signal" aria-hidden="true"><b></b><b></b><b></b><b></b></div>';
const pillars=[
  ["01","Potrzeby, testy i zamówienia","Proces problem → prototyp → test → mała partia → skalowanie, oparty na mierzalnych bramkach."],
  ["02","Przemysł i łańcuchy dostaw","Polskie moce produkcyjne, serwis, odporność komponentowa i eksport technologii podwójnego zastosowania."],
  ["03","Autonomia, AI, dane i cyber","Systemy autonomiczne, bezpieczna przestrzeń danych, ocena modeli i suwerenne zasoby obliczeniowe."],
  ["04","Kadry i inżynieria","Inżynierowie, technicy i operatorzy oraz sieć edukacji odpowiadająca na zweryfikowany popyt kompetencyjny."],
  ["05","Ukraina, UE, NATO i partnerstwa","Partnerstwa z kontrolą IP, due diligence, bezpieczeństwem dostaw i zgodnością z interesem Polski."],
  ["06","Regiony, zastosowania cywilne i eksport","Produktywność MŚP, usługi publiczne, pilotaże regionalne i skalowanie rozwiązań na rynki zagraniczne."]
];
const cards=pillars.map(([number,title,copy])=>`<article class="pillar-card" id="pillar-${number}"><div class="card-top"><span>${number}</span><i aria-hidden="true"></i></div><h3>${title}</h3><p>${copy}</p>${signals}</article>`).join("");
const section=`<section class="pillars-section section shell" aria-labelledby="pillars-title"><div class="section-head"><div class="section-kicker"><span>02</span> Sześć współzależnych filarów</div><h2 id="pillars-title">Nie sześć osobnych polityk.<br/>Jeden system rozwoju.</h2></div><div class="pillar-cards">${cards}</div></section>`;
const sectionPattern=/<section class="pillars-section section shell".*?<\/section><section class="roadmap/s;
if(!sectionPattern.test(html))throw new Error("Nie znaleziono sekcji filarów");
html=html.replace(sectionPattern,`${section}<section class="roadmap`);

replaceExact(
  "Ramy etapów są propozycją do walidacji. Budżety i KPI zostaną opublikowane po audycie danych.",
  "Roadmapa, KPI i trzy scenariusze finansowe są dostępne w wydaniu v0.1. Wartości pozostają hipotezami do walidacji, a nie przyjętym budżetem państwa.",
  "nota roadmapy"
);
replaceExact(
  "Materiały pojawiają się sukcesywnie po zakończeniu prac, weryfikacji źródeł i dopuszczeniu do publikacji.",
  "Pięć głównych dokumentów wydania v0.1 jest dostępnych do konsultacji: strategia, roadmapa, finansowanie oraz noty dla Premiera/RM i Prezydenta/BBN. Otwórz materiał w czytniku lub pobierz format źródłowy.",
  "opis biblioteki"
);
replaceExact(
  "Materiał konferencyjny i ekspercki draft programu będą rozwijane wraz z księgą dowodową, modelem finansowym i planem wdrożenia.",
  "Pełny ekspercki pakiet v0.1 — strategia, księga dowodowa, model finansowy, roadmapa i materiały decyzyjne — jest dostępny do krytycznej konsultacji.",
  "opis końcowy"
);

// The original export appended a stale React Server Components payload after
// the complete static DOM. It duplicated old copy and referenced absent bundles.
html=html.replace(/<script id="_R_">[\s\S]*$/,`<script src="app.js?v=docs3" defer></script></body></html>`);
html=html.replace(/<link rel="modulepreload"[^>]*>/g,"");
html=html.replace(/<script>self\.__VINEXT_[\s\S]*?<\/script>/g,"");
html=html.replace(/<link[^>]+href="\/assets\/[^"]+"[^>]*>/g,"");
html=html.replace(/<style data-vinext-fonts>[\s\S]*?<\/style>/g,"");
html=html.replace(/<meta name="codex-preview"[^>]*>/g,"");
html=html.replace(/ data-rsc-css-href="[^"]+"| data-precedence="[^"]+"/g,"");

writeFileSync(path,html);
