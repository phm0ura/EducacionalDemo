from flask import Flask, render_template_string, jsonify
from datetime import datetime

app = Flask(__name__)

# ============================================================
# CHAMADA EDUCAÇÃO
# Plataforma demonstrativa de ensino com vídeos do YouTube
# ============================================================

PLAYLIST_ID = "PLzISi0jWP8c3FjwO53b6_dgZ64gCnov6O"

# O YouTube entrega automaticamente os vídeos da playlist
# através do player incorporado. Assim, não precisamos
# cadastrar manualmente cada vídeo.
COURSE = {
    "title": "EducAÇÃO",
    "subtitle": "Aprenda no seu ritmo. Conhecimento que chama para a ação.",
    "description": (
        "Uma plataforma educacional demonstrativa, com identidade visual construída em tons de azul, criada com Python + Flask, "
        "com aulas em vídeo, acompanhamento de progresso e uma experiência "
        "de aprendizagem simples e moderna."
    ),
    "category": "Formação",
    "level": "Todos os níveis",
    "playlist_id": PLAYLIST_ID,
}


HTML = r"""
<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{ course.title }} — Plataforma Educacional</title>

<style>
:root{
    --navy:#0B1F3A;
    --navy2:#12315B;
    --blue:#1769E0;
    --blue2:#4D8DFF;
    --cyan:#6EC8FF;
    --cream:#F3F7FC;
    --white:#FFFFFF;
    --text:#132238;
    --muted:#6B7A90;
    --line:#DCE6F2;
    --green:#2878D7;
    --yellow:#5EA2FF;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
    margin:0;
    font-family:Inter,Segoe UI,system-ui,-apple-system,sans-serif;
    color:var(--text);
    background:var(--cream);
}
button,input{font:inherit}
button{cursor:pointer}
a{text-decoration:none;color:inherit}


/* PALETA EDUCACIONAL — AZUL */
:root{
    --blue-deep:#0B1F3A;
    --blue-dark:#12315B;
    --blue-main:#1769E0;
    --blue-soft:#4D8DFF;
    --blue-light:#6EC8FF;
    --blue-pale:#EEF5FF;
}

/* HEADER */
.top{
    height:70px;
    background:#fff;
    border-bottom:1px solid var(--line);
    display:flex;
    align-items:center;
    position:sticky;
    top:0;
    z-index:30;
}
.nav{
    width:min(1250px,94%);
    margin:auto;
    display:flex;
    align-items:center;
    gap:30px;
}
.logo{
    font-weight:950;
    font-size:21px;
    letter-spacing:-1px;
    white-space:nowrap;
}
.logo span{color:var(--blue)}
.nav-links{
    display:flex;
    gap:23px;
    color:#657187;
    font-size:14px;
    flex:1;
}
.nav-links a:hover{color:var(--blue)}
.search{
    width:220px;
    border:1px solid var(--line);
    border-radius:10px;
    padding:10px 12px;
    outline:none;
}
.avatar{
    width:38px;height:38px;border-radius:50%;
    background:linear-gradient(135deg,var(--blue),var(--cyan));
    color:#fff;display:grid;place-items:center;font-weight:900;
}

/* HERO */
.hero{
    background:
        radial-gradient(circle at 85% 20%,#315dd455,transparent 32%),
        linear-gradient(120deg,var(--navy),#20345c);
    color:#fff;
}
.hero-inner{
    width:min(1250px,94%);
    margin:auto;
    padding:55px 0 58px;
    display:grid;
    grid-template-columns:1.15fr .85fr;
    gap:55px;
    align-items:center;
}
.eyebrow{
    color:#9DCCFF;
    text-transform:uppercase;
    letter-spacing:1.6px;
    font-weight:900;
    font-size:11px;
}
.hero h1{
    font-size:clamp(42px,5vw,67px);
    line-height:1;
    letter-spacing:-3px;
    margin:14px 0 17px;
}
.hero h1 span{color:var(--cyan)}
.hero p{
    max-width:650px;
    color:#D2E2F5;
    font-size:17px;
    line-height:1.65;
}
.hero-actions{display:flex;gap:10px;margin-top:25px;flex-wrap:wrap}
.btn{
    border:0;border-radius:10px;padding:13px 17px;font-weight:850;
}
.primary{background:var(--cyan);color:#102235}
.secondary{background:#4D8DFF18;color:#fff;border:1px solid #ffffff2a}
.course-card{
    background:#fff;
    color:var(--text);
    border-radius:18px;
    padding:24px;
    box-shadow:0 25px 60px #0003;
}
.course-cover{
    height:170px;
    border-radius:13px;
    background:
      linear-gradient(135deg,#223e77cc,#4778ff88),
      url("https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&w=1000&q=85") center/cover;
    display:flex;align-items:flex-end;padding:18px;color:#fff;
}
.course-cover strong{font-size:21px}
.course-meta{display:flex;gap:15px;color:var(--muted);font-size:12px;margin-top:15px}
.progress-label{display:flex;justify-content:space-between;margin-top:18px;font-size:12px}
.progress{height:8px;background:#edf0f5;border-radius:99px;overflow:hidden;margin-top:7px}
.progress div{height:100%;background:linear-gradient(90deg,var(--blue),var(--blue2),var(--cyan));width:35%}

/* LAYOUT */
.page{
    width:min(1250px,94%);
    margin:auto;
    display:grid;
    grid-template-columns:1fr 330px;
    gap:24px;
    padding:35px 0 60px;
}
.main,.sidebar-card{
    background:#fff;
    border:1px solid var(--line);
    border-radius:17px;
}
.main{overflow:hidden}
.section-head{padding:24px 25px 10px}
.section-head h2{margin:0;font-size:25px;letter-spacing:-.7px}
.section-head p{color:var(--muted);margin:7px 0 0;font-size:14px}

/* PLAYER */
.player{
    background:#081A2F;
    aspect-ratio:16/9;
    width:100%;
}
.player iframe{width:100%;height:100%;border:0}
.player-note{
    padding:13px 18px;
    background:#f8faff;
    color:#6d7890;
    font-size:12px;
    border-bottom:1px solid var(--line);
}

/* LESSON LIST */
.lessons{padding:12px 16px 20px}
.lesson{
    display:flex;
    align-items:center;
    gap:13px;
    padding:14px 11px;
    border-radius:11px;
    border:1px solid transparent;
    transition:.15s;
}
.lesson:hover{background:#f7f9fd}
.lesson.active{
    background:#EEF5FF;
    border-color:#CFE0FA;
}
.play{
    width:38px;height:38px;min-width:38px;
    border-radius:10px;
    background:#EAF2FF;
    color:var(--blue);
    display:grid;place-items:center;
    font-size:13px;
}
.lesson.done .play{background:#E8F2FF;color:var(--blue)}
.lesson-info{flex:1}
.lesson-title{font-weight:750;font-size:14px}
.lesson-meta{font-size:11px;color:var(--muted);margin-top:4px}
.check{color:var(--blue);font-weight:900}

/* SIDEBAR */
.sidebar{display:flex;flex-direction:column;gap:18px}
.sidebar-card{padding:21px}
.sidebar-card h3{margin:0 0 15px;font-size:17px}
.stat-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.stat{
    background:#f7f9fc;border-radius:11px;padding:14px;
}
.stat strong{font-size:23px;display:block}
.stat span{font-size:11px;color:var(--muted)}
.tip{
    border-left:3px solid var(--blue2);
    background:#EEF6FF;
    padding:13px 14px;
    color:#536A83;
    font-size:12px;
    line-height:1.6;
}

/* API */
.api-section{
    width:min(1250px,94%);
    margin:0 auto 60px;
}
.api-box{
    background:var(--navy);
    color:#dce8fa;
    border-radius:17px;
    padding:25px;
}
.api-box h2{margin-top:0}
.endpoint{
    display:flex;gap:12px;align-items:center;
    font-family:Consolas,monospace;font-size:13px;
}
.method{color:var(--cyan);font-weight:900}
.api-result{
    margin-top:15px;
    padding:15px;
    background:#071A30;
    border-radius:10px;
    color:#A9BFDA;
    font:12px/1.65 Consolas,monospace;
    white-space:pre-wrap;
}
footer{
    background:#fff;
    border-top:1px solid var(--line);
    padding:35px;
    text-align:center;
    color:var(--muted);
    font-size:12px;
}

/* TOAST */
.toast{
    position:fixed;
    right:22px;
    bottom:22px;
    background:var(--navy);
    color:#fff;
    padding:14px 18px;
    border-radius:11px;
    box-shadow:0 15px 40px #0003;
    display:none;
    z-index:99;
}

@media(max-width:900px){
    .search{display:none}
    .hero-inner{grid-template-columns:1fr}
    .page{grid-template-columns:1fr}
}
@media(max-width:600px){
    .nav-links{display:none}
    .hero-inner{padding:40px 0}
    .hero h1{letter-spacing:-2px}
    .course-card{max-width:100%}
}
</style>
</head>

<body>

<header class="top">
<nav class="nav">
    <div class="logo"> Educ<span>AÇÃO📚</span></div>

    <div class="nav-links">
        <a href="#curso">Meu curso</a>
        <a href="#aulas">Aulas</a>
        <a href="#recursos">Recursos</a>
        <a href="#tecnologia">Tecnologia</a>
    </div>

    <input class="search" placeholder="🔎  Buscar uma aula..." oninput="searchLessons(this.value)">
    <div class="avatar">EA</div>
</nav>
</header>

<section class="hero">
<div class="hero-inner">

    <div>
        <div class="eyebrow">Plataforma de aprendizagem</div>
        <h1>Conhecimento que<br><span>chama para a ação.</span></h1>
        <p>{{ course.description }}</p>

        <div class="hero-actions">
            <a href="#aulas" class="btn primary">▶ Continuar estudando</a>
            <button class="btn secondary" onclick="showToast('Certificado: recurso demonstrativo')">🏆 Meu certificado</button>
        </div>
    </div>

    <div class="course-card">
        <div class="course-cover">
            <strong>{{ course.title }}</strong>
        </div>
        <div class="course-meta">
            <span>🎓 {{ course.category }}</span>
            <span>📚 {{ course.level }}</span>
            <span>▶ Vídeos</span>
        </div>
        <div class="progress-label">
            <span>Seu progresso</span>
            <strong id="progressText">35%</strong>
        </div>
        <div class="progress"><div id="progressBar"></div></div>
    </div>

</div>
</section>


<main class="page" id="curso">

<div class="main">

    <div class="section-head" id="aulas">
        <h2>Conteúdo do curso</h2>
        <p>Selecione uma aula na playlist para começar a assistir.</p>
    </div>

    <!--
      O player utiliza diretamente a playlist do YouTube.
      O usuário pode trocar de vídeo usando os controles/playlist
      fornecidos pelo próprio YouTube.
    -->
    <div class="player">
        <iframe
            src="https://www.youtube.com/embed/videoseries?list={{ course.playlist_id }}&rel=0"
            title="EducAÇÃO — aulas"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
        </iframe>
    </div>

    <div class="player-note">
        ▶ As aulas são reproduzidas diretamente do YouTube. A playlist é a fonte oficial do conteúdo.
    </div>

    <div class="lessons" id="lessonList">
        {% for i in range(1, 9) %}
        <div class="lesson {% if i == 1 %}active{% endif %}" data-title="Aula {{ i }}" onclick="selectLesson(this, {{ i }})">
            <div class="play">▶</div>
            <div class="lesson-info">
                <div class="lesson-title">Aula {{ i }}</div>
                <div class="lesson-meta">Vídeo da playlist · EducAÇÃO</div>
            </div>
            <div class="check" style="display:none">✓</div>
        </div>
        {% endfor %}
    </div>

</div>


<aside class="sidebar">

    <div class="sidebar-card">
        <h3>Seu aprendizado</h3>

        <div class="stat-grid">
            <div class="stat">
                <strong id="watched">0</strong>
                <span>Aulas concluídas</span>
            </div>
            <div class="stat">
                <strong>8</strong>
                <span>Aulas demonstrativas</span>
            </div>
            <div class="stat">
                <strong>⚡ 4</strong>
                <span>Dias de sequência</span>
            </div>
            <div class="stat">
                <strong>⭐ 240</strong>
                <span>Pontos</span>
            </div>
        </div>
    </div>

    <div class="sidebar-card" id="recursos">
        <h3>Recursos</h3>

        <button class="btn secondary" style="width:100%;color:var(--text);background:#fff;border:1px solid var(--line)"
                onclick="showToast('Material complementar — demonstração')">
            📄 Material complementar
        </button>

        <button class="btn secondary" style="width:100%;margin-top:9px;color:var(--text);background:#fff;border:1px solid var(--line)"
                onclick="showToast('Questionário — demonstração')">
            📝 Fazer questionário
        </button>

        <button class="btn secondary" style="width:100%;margin-top:9px;color:var(--text);background:#fff;border:1px solid var(--line)"
                onclick="showToast('Certificado disponível após conclusão')">
            🏆 Certificado
        </button>
    </div>

    <div class="sidebar-card">
        <h3>💡 Dica de estudo</h3>
        <div class="tip">
            Reserve alguns minutos por dia para assistir às aulas e anote os principais pontos.
            Constância é mais importante do que velocidade.
        </div>
    </div>

</aside>

</main>


<section class="api-section" id="tecnologia">
    <div class="api-box">
        <h2>Flask por trás da plataforma</h2>
        <p style="color:#9db2cc">
            O frontend conversa com uma API Python. Em um projeto real,
            ela poderia buscar cursos, usuários, progresso, certificados e
            permissões diretamente de um banco de dados.
        </p>

        <div class="endpoint">
            <span class="method">GET</span>
            <span>/api/course</span>
        </div>

        <div class="api-result" id="apiResult">
Clique em "Testar API" para consultar o backend.
        </div>

        <button class="btn primary" onclick="testApi()" style="margin-top:12px">
            ⚡ Testar API
        </button>
    </div>
</section>


<footer>
    <strong>EducAÇÃO</strong> · Plataforma demonstrativa criada com Python + Flask + Jinja<br>
    Conteúdo em vídeo fornecido através da playlist pública do YouTube.
</footer>

<div id="toast" class="toast"></div>

<script>
let completed = JSON.parse(localStorage.getItem('educacao_completed') || '[]');

function updateProgress(){
    const total = 8;
    const percentage = Math.round((completed.length / total) * 100);

    document.getElementById('watched').textContent = completed.length;
    document.getElementById('progressText').textContent = percentage + '%';
    document.getElementById('progressBar').style.width = percentage + '%';

    document.querySelectorAll('.lesson').forEach((lesson, index)=>{
        const number = index + 1;
        const check = lesson.querySelector('.check');

        if(completed.includes(number)){
            lesson.classList.add('done');
            check.style.display = 'block';
        }
    });
}

function selectLesson(element, number){
    document.querySelectorAll('.lesson').forEach(x=>x.classList.remove('active'));
    element.classList.add('active');

    if(!completed.includes(number)){
        completed.push(number);
        localStorage.setItem('educacao_completed', JSON.stringify(completed));
        updateProgress();
        showToast('Aula '+number+' marcada como concluída');
    }
}

function searchLessons(value){
    value = value.toLowerCase();

    document.querySelectorAll('.lesson').forEach(lesson=>{
        const title = lesson.dataset.title.toLowerCase();
        lesson.style.display = title.includes(value) ? 'flex' : 'none';
    });
}

async function testApi(){
    const box = document.getElementById('apiResult');
    box.textContent = 'Consultando backend Flask...';

    const response = await fetch('/api/course');
    const data = await response.json();

    box.textContent = JSON.stringify(data, null, 2);
}

function showToast(message){
    const toast = document.getElementById('toast');
    toast.textContent = '✓ ' + message;
    toast.style.display = 'block';

    setTimeout(()=>{
        toast.style.display = 'none';
    },2200);
}

updateProgress();
</script>

</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML, course=COURSE)


@app.route("/api/course")
def api_course():
    return jsonify({
        "success": True,
        "course": COURSE,
        "platform": "Chamada EducAÇÃO",
        "framework": "Flask",
        "video_provider": "YouTube",
        "generated_at": datetime.now().isoformat(timespec="seconds")
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "chamada-educacao",
        "framework": "Flask"
    })


if __name__ == "__main__":
    app.run(debug=True)
