const observer=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting)e.target.classList.add('visible')}),{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>observer.observe(el));
const glow=document.querySelector('.cursor-glow');
window.addEventListener('pointermove',e=>{glow.style.left=e.clientX+'px';glow.style.top=e.clientY+'px'});
document.querySelectorAll('.card').forEach(card=>card.addEventListener('pointermove',e=>{const r=card.getBoundingClientRect();card.style.background=`radial-gradient(circle at ${e.clientX-r.left}px ${e.clientY-r.top}px,rgba(210,172,85,.12),#0a1018 55%)`}));

function documentCard(doc){
  const ready=doc.status==="reviewed"&&doc.visibility==="public";
  const status=ready?"Opublikowany":"W przygotowaniu";
  const actions=ready
    ? `<div class="document-actions"><a href="${doc.html}" class="document-link">Czytaj <span>↗</span></a>${doc.pdf?`<a href="${doc.pdf}" class="document-download">PDF ↓</a>`:""}</div>`
    : `<div class="document-actions"><span class="document-pending">Publikacja po weryfikacji</span></div>`;
  return `<article class="document-card ${ready?"is-ready":"is-pending"}"><div class="document-meta"><span>${String(doc.order).padStart(2,"0")}</span><b>${doc.category}</b></div><h3>${doc.title}</h3><p>${doc.summary}</p><div class="document-state"><i></i>${status}${ready&&doc.updated?` · ${doc.updated}`:""}</div>${actions}</article>`;
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
      const selected=container.dataset.mode==="featured"?docs.filter(d=>d.featured).slice(0,3):docs;
      container.innerHTML=selected.map(documentCard).join("");
    });
  }catch(error){
    containers.forEach(container=>container.innerHTML='<p class="documents-error">Katalog dokumentów jest chwilowo niedostępny.</p>');
  }
}
loadDocuments();
