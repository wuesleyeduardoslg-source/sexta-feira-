const host = "http://localhost:5000"; // ou IP do dispositivo corpo

function modulo(cmd){
  fetch(`${host}/modulo?cmd=${cmd}`)
    .then(r=>r.json())
    .then(d=>document.getElementById("status").innerText=d.resposta);
}

function voz(){
  fetch(`${host}/voz`)
    .then(r=>r.json())
    .then(d=>document.getElementById("status").innerText="Você disse: "+d.resposta);
}

function scrape(){
  const url=document.getElementById("urlInput").value;
  fetch(`${host}/web/scrape?url=${encodeURIComponent(url)}`)
    .then(r=>r.json())
    .then(d=>document.getElementById("status").innerText=`Título: ${d.title}\nLinks: ${d.links.length}`);
}

function download(){
  const url=document.getElementById("urlInput").value;
  fetch(`${host}/web/download?url=${encodeURIComponent(url)}`)
    .then(r=>r.json())
    .then(d=>document.getElementById("status").innerText=`Arquivo salvo em: ${d.download_path}`);
}

function search(){
  const q=document.getElementById("queryInput").value;
  fetch(`${host}/web/search?q=${encodeURIComponent(q)}`)
    .then(r=>r.json())
    .then(d=>document.getElementById("status").innerText=`Resultados:\n${JSON.stringify(d).slice(0,500)}...`);
                              }
  
