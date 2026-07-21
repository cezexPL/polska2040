const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
const glow=document.querySelector('.cursor-glow');
if(glow)window.addEventListener('pointermove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'});
document.querySelectorAll('.card').forEach(card=>card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();card.style.background=`radial-gradient(circle at ${e.clientX-r.left}px ${e.clientY-r.top}px,rgba(210,172,85,.12),#0a1018 55%)`}));

function escapeHtml(value){
  return String(value??"").replace(/[&<>"']/g,char=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#039;"})[char]);
}
function documentCard(doc){
  const ready=doc.status==="reviewed"&&doc.visibility==="public";
  const status=ready?"Ekspercki draft v0.1":"W przygotowaniu";
  const measure=doc.pages?`${doc.pages} str.`:doc.slides?`${doc.slides} slajdów`:"Plik danych";
  const actions=ready
    ? `<div class="document-actions">${doc.html?`<button type="button" class="document-link" data-reader-url="${escapeHtml(doc.html)}" data-reader-title="${escapeHtml(doc.title)}">Czytaj online <span>↗</span></button>`:""}<span class="document-files">${doc.pdf?`<a href="${escapeHtml(doc.pdf)}" class="document-download">PDF ↓</a>`:""}${doc.download?`<a href="${escapeHtml(doc.download)}" class="document-download">${escapeHtml(doc.downloadLabel||"Plik")} ↓</a>`:""}</span></div>`
    : `<div class="document-actions"><span class="document-pending">Publikacja po weryfikacji</span></div>`;
  return `<article class="document-card ${ready?"is-ready":"is-pending"}" data-search="${escapeHtml(`${doc.title} ${doc.summary} ${doc.category}`.toLowerCase())}"><div class="document-meta"><span>${String(doc.order).padStart(2,"0")}</span><b>${escapeHtml(doc.category)}</b></div><h3>${escapeHtml(doc.title)}</h3><p>${escapeHtml(doc.summary)}</p><div class="document-state"><i></i>${status} · ${measure}${ready&&doc.updated?` · ${escapeHtml(doc.updated)}`:""}</div>${actions}</article>`;
}
function openReader(url,title){
  let reader=document.querySelector(".document-reader");
  if(!reader){
    reader=document.createElement("div");
    reader.className="document-reader";
    reader.innerHTML='<div class="reader-bar"><strong></strong><span><a target="_blank" rel="noopener">Otwórz w nowej karcie ↗</a><button type="button" aria-label="Zamknij czytnik">×</button></span></div><iframe title="Czytnik dokumentu"></iframe>';
    document.body.appendChild(reader);
    reader.querySelector("button").addEventListener("click",()=>{reader.classList.remove("is-open");reader.querySelector("iframe").src="about:blank";document.body.classList.remove("reader-open")});
    reader.addEventListener("click",event=>{if(event.target===reader)reader.querySelector("button").click()});
    document.addEventListener("keydown",event=>{if(event.key==="Escape"&&reader.classList.contains("is-open"))reader.querySelector("button").click()});
  }
  reader.querySelector("strong").textContent=title;
  reader.querySelector("a").href=url;
  reader.querySelector("iframe").src=url;
  reader.classList.add("is-open");
  document.body.classList.add("reader-open");
}
async function loadDocuments(){
  const containers=document.querySelectorAll("[data-documents-list]");
  if(!containers.length)return;
  try{
    const response=await fetch("/documents.json",{cache:"no-store"});
    if(!response.ok)throw new Error("manifest");
    const data=await response.json();
    containers.forEach(container=>{
      const docs=[...data.documents].sort((a,b)=>a.order-b.order);
      const selected=container.dataset.mode==="featured"?docs.filter(d=>d.featured).slice(0,5):docs;
      container.innerHTML=selected.map(documentCard).join("");
      container.addEventListener("click",event=>{const trigger=event.target.closest("[data-reader-url]");if(trigger)openReader(trigger.dataset.readerUrl,trigger.dataset.readerTitle)});
      const count=document.querySelector("[data-documents-count]");
      if(count)count.textContent=`${selected.length} pozycji w wydaniu ${data.version}`;
    });
    const search=document.querySelector("#document-search");
    if(search)search.addEventListener("input",()=>{const query=search.value.trim().toLowerCase();document.querySelectorAll(".documents-page .document-card").forEach(card=>card.hidden=query&&!card.dataset.search.includes(query))});
  }catch(error){
    containers.forEach(container=>container.innerHTML='<p class="documents-error">Katalog dokumentów jest chwilowo niedostępny.</p>');
  }
}
loadDocuments();
