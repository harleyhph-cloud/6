import streamlit as st
import streamlit.components.v1 as components

# Configuración básica de la página
st.set_page_config(page_title="Para Mi Novia ❤️", layout="wide")

# Eliminar espacios en blanco por defecto de Streamlit
st.markdown("""
    <style>
    .block-container { padding: 0px !important; }
    iframe { display: block; }
    </style>
""", unsafe_allow_html=True)

# Código HTML/CSS/JS de tu página
html = """
<!DOCTYPE html>
<html>
<head>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#000; overflow:hidden; }
#pantalla {
  height: 100vh; width: 100vw;
  background: #000;
  display: flex; justify-content: center; align-items: center;
  position: relative; overflow: hidden;
  cursor: pointer; user-select: none;
}
#fondo-corazon {
  position: absolute; width: 100%; height: 100%;
  display: flex; justify-content: center; align-items: center;
  font-size: 140vmin; opacity: 0.45; line-height: 1;
  transform: scale(1.1) translateY(12%);
  z-index: 1; pointer-events: none;
}
#titulo {
  position: absolute;
  color: #ffffff;
  font-family: 'Arial Rounded MT Bold', Arial, sans-serif;
  font-size: 8vw; font-weight: bold; text-align: center;
  z-index: 10;
  text-shadow: 0px 4px 15px rgba(0,0,0,0.9);
  max-width: 90%; letter-spacing: 2px;
  pointer-events: none;
}
#hint {
  position: absolute; bottom: 40px;
  color: rgba(255,255,255,0.75);
  font-family: Arial, sans-serif;
  font-size: 1.4vw; letter-spacing: 3px;
  text-transform: uppercase; z-index: 10;
  animation: parpadeo 2s ease-in-out infinite;
  pointer-events: none;
}
@keyframes aparecerFoto {
  0% { transform: scale(0) rotate(-10deg); opacity: 0; }
  70% { transform: scale(1.1) rotate(5deg); opacity: 1; }
  100% { transform: scale(1) rotate(0deg); opacity: 1; }
}
.contenedor-fotos { display: flex; justify-content: center; gap: 15px; margin-top: 20px; }
.foto-animada { width: 120px; height: 120px; object-fit: cover; border-radius: 10px; border: 3px solid #ff4d6d; animation: aparecerFoto 0.8s cubic-bezier(0.17, 0.67, 0.83, 0.67) forwards; opacity: 0; }
.foto-1 { animation-delay: 0.3s; }
.foto-2 { animation-delay: 0.6s; }
.foto-3 { animation-delay: 0.9s; }
@keyframes parpadeo { 0%,100% { opacity: 0.35; } 50% { opacity: 1; } }
.globo { position: absolute; pointer-events: none; z-index: 20; display: flex; flex-direction: column; align-items: center; animation: flotar linear forwards; }
.hilo { width: 1.5px; height: 38px; background: rgba(255,255,255,0.45); }
@keyframes flotar { 0%{transform:translateY(0) translateX(0); opacity:1;} 100%{transform:translateY(-110vh) translateX(0); opacity:0;} }
#btn-carta { position: absolute; top: 75%; z-index: 25; padding: 12px 25px; background: rgba(255, 255, 255, 0.1); border: 1px solid white; border-radius: 30px; color: white; font-family: sans-serif; cursor: pointer; font-weight: bold; font-size: 1.2vw; }
#modal-carta { display: none; position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 100; justify-content: center; align-items: center; }
#contenido-modal { background: white; padding: 40px; border-radius: 20px; text-align: center; color: #333; max-width: 70%; font-family: Arial, sans-serif; position: relative; }
#btn-cerrar { position: absolute; top: 10px; right: 15px; font-size: 24px; cursor: pointer; color: #888; font-weight: bold; }
</style>
</head>
<body>
<div id="pantalla" onclick="lanzarGlobos(event)">
  <div id="fondo-corazon">💗</div>
  <h1 id="titulo">feliz 6 meses amoor</h1>
  <div id="btn-carta" onclick="event.stopPropagation(); document.getElementById('modal-carta').style.display='flex'">💌 CARTA</div>
  <span id="hint">✨ dale clic a la pantalla ✨</span>
</div>

<div id="modal-carta" onclick="this.style.display='none'">
  <div id="contenido-modal" onclick="event.stopPropagation()">
    <div id="btn-cerrar" onclick="document.getElementById('modal-carta').style.display='none'">×</div>
    <h2>Para el amor de mi vida ❤️</h2>
    <p><br>Seis meses contigo, mi niña linda.<br>
    Gracias por estar a mi lado y hacerme tan feliz.<br>
    Eres todo para mí, Arlianys.<br>
    ¡Te amo mucho!<br><br></p>
    <div class="contenedor-fotos">
      <img src="https://raw.githubusercontent.com/harleyhph-cloud/nv/main/aa.jpeg" class="foto-animada foto-1">
      <img src="https://raw.githubusercontent.com/harleyhph-cloud/nv/main/an.jpeg" class="foto-animada foto-2">
      <img src="https://raw.githubusercontent.com/harleyhph-cloud/nv/main/ani.jpeg" class="foto-animada foto-3">
    </div>
  </div>
</div>

<script>
const paleta = [['#ff0054','#aa0033'],['#ff4d6d','#cc2244'],['#ff85a1','#cc3366'],['#c9184a','#880022'],['#ffb3c1','#dd4477'],['#e5383b','#991122'],['#ff6b6b','#bb2222'],['#ffc8dd','#ff3388']];
function corazonSVG(size, c2) {
  const id = 'g' + Math.random().toString(36).slice(2,8);
  return `<svg width="${size}" height="${size}" viewBox="0 0 100 92"><defs><radialGradient id="${id}" cx="38%" cy="32%" r="58%"><stop offset="0%" stop-color="rgba(255,255,255,0.4)"/><stop offset="100%" stop-color="${c2}"/></radialGradient></defs><path d="M50 85 C50 85 5 55 5 28 C5 12 17 2 30 2 C38 2 45 7 50 13 C55 7 62 2 70 2 C83 2 95 12 95 28 C95 55 50 85 50 85 Z" fill="url(#${id})" stroke="${c2}" stroke-width="1.5"/></svg>`;
}
function crearGlobo(x) {
  const pantalla = document.getElementById('pantalla');
  const el = document.createElement('div');
  el.classList.add('globo');
  el.style.left = x + (Math.random()-0.5)*130 + 'px';
  el.style.bottom = '-160px';
  el.style.animationDuration = (4 + Math.random()*3.5) + 's';
  const par = paleta[Math.floor(Math.random()*paleta.length)];
  el.innerHTML = corazonSVG(100, par[1]) + '<div class="hilo"></div>';
  pantalla.appendChild(el);
  el.addEventListener('animationend', () => el.remove());
}
function lanzarGlobos(e) {
  const rect = e.currentTarget.getBoundingClientRect();
  const relX = e.clientX - rect.left;
  for(let i=0; i<8; i++) setTimeout(() => crearGlobo(relX), i*90);
}
</script>
</body>
</html>
"""

components.html(html, height=900, scrolling=False)