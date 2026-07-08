from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Edbin Motors — Built For What's Next</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --charcoal: #14170f;
    --panel: #1d221a;
    --panel-line: #2c3327;
    --rust: #c2601f;
    --rust-bright: #e17a2e;
    --olive: #7c8a6b;
    --sand: #e9e4d4;
    --sand-dim: #9a9a86;
  }

  *{ box-sizing:border-box; }
  html{ scroll-behavior:smooth; }

  body{
    margin:0;
    background:var(--charcoal);
    color:var(--sand);
    font-family:'Inter', sans-serif;
    overflow-x:hidden;
  }

  ::selection{ background:var(--rust); color:var(--charcoal); }

  a{ color:inherit; }

  /* --- Topographic contour texture, used as the recurring signature motif --- */
  .topo-bg{
    position:absolute;
    inset:0;
    background-image:
      repeating-radial-gradient(circle at 20% 30%, transparent 0, transparent 38px, rgba(124,138,107,0.14) 39px, transparent 40px, transparent 78px, rgba(124,138,107,0.10) 79px, transparent 80px),
      repeating-radial-gradient(circle at 80% 70%, transparent 0, transparent 46px, rgba(194,96,31,0.10) 47px, transparent 48px, transparent 92px, rgba(194,96,31,0.07) 93px, transparent 94px);
    opacity:0.9;
    pointer-events:none;
  }

  /* --- Header --- */
  .site-header{
    position:sticky;
    top:0;
    z-index:50;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:20px 6vw;
    background:rgba(20,23,15,0.88);
    backdrop-filter:blur(8px);
    border-bottom:1px solid var(--panel-line);
  }
  .logo{
    display:flex;
    align-items:center;
    gap:12px;
    font-family:'Oswald', sans-serif;
    font-size:20px;
    font-weight:600;
    letter-spacing:1.5px;
    text-transform:uppercase;
  }
  .logo .coord{
    font-family:'JetBrains Mono', monospace;
    font-size:11px;
    color:var(--rust-bright);
    letter-spacing:0.5px;
  }
  .logo-mark{
    width:34px; height:34px;
    border:1.5px solid var(--rust-bright);
    border-radius:50%;
    display:flex; align-items:center; justify-content:center;
  }
  .logo-mark svg{ width:20px; height:20px; }

  nav a{
    margin-left:32px;
    text-decoration:none;
    font-size:13px;
    letter-spacing:1.2px;
    text-transform:uppercase;
    color:var(--sand-dim);
    transition:color .2s ease;
  }
  nav a:hover{ color:var(--rust-bright); }

  /* --- Hero --- */
  .hero{
    position:relative;
    padding:120px 6vw 100px;
    text-align:left;
    max-width:1100px;
  }
  .eyebrow{
    font-family:'JetBrains Mono', monospace;
    font-size:12px;
    letter-spacing:2px;
    color:var(--rust-bright);
    text-transform:uppercase;
    display:flex;
    align-items:center;
    gap:10px;
    margin-bottom:22px;
  }
  .eyebrow::before{
    content:"";
    width:28px; height:1px;
    background:var(--rust-bright);
    display:inline-block;
  }
  h1{
    font-family:'Oswald', sans-serif;
    font-weight:700;
    font-size:clamp(42px, 7vw, 84px);
    line-height:0.98;
    letter-spacing:-0.5px;
    text-transform:uppercase;
    margin:0 0 28px;
  }
  h1 span{ color:var(--rust-bright); }
  .hero p.lede{
    font-size:18px;
    line-height:1.7;
    color:var(--sand-dim);
    max-width:520px;
    margin:0 0 40px;
  }
  .hero-ctas{ display:flex; gap:16px; flex-wrap:wrap; }
  .btn{
    font-family:'Inter', sans-serif;
    font-weight:600;
    font-size:14px;
    letter-spacing:0.4px;
    text-decoration:none;
    padding:15px 30px;
    border-radius:2px;
    display:inline-block;
    transition:transform .18s ease, background .18s ease;
  }
  .btn-primary{ background:var(--rust); color:var(--charcoal); }
  .btn-primary:hover{ background:var(--rust-bright); transform:translateY(-2px); }
  .btn-ghost{ border:1px solid var(--panel-line); color:var(--sand); }
  .btn-ghost:hover{ border-color:var(--olive); transform:translateY(-2px); }

  /* --- Section label --- */
  .section-head{
    padding:0 6vw;
    display:flex;
    align-items:baseline;
    justify-content:space-between;
    gap:24px;
    margin-bottom:44px;
    flex-wrap:wrap;
  }
  .section-head h2{
    font-family:'Oswald', sans-serif;
    text-transform:uppercase;
    font-size:32px;
    font-weight:600;
    letter-spacing:0.5px;
    margin:0;
  }
  .section-head .tag{
    font-family:'JetBrains Mono', monospace;
    font-size:12px;
    color:var(--sand-dim);
    letter-spacing:1px;
  }

  /* --- Fleet / spec-sheet cards --- */
  .fleet{ padding:70px 6vw 100px; position:relative; }
  .grid{
    display:grid;
    grid-template-columns:repeat(auto-fit, minmax(280px, 1fr));
    gap:24px;
  }
  .card{
    background:var(--panel);
    border:1px solid var(--panel-line);
    border-radius:4px;
    padding:0;
    overflow:hidden;
    transition:border-color .25s ease, transform .25s ease;
  }
  .card:hover{ border-color:var(--rust); transform:translateY(-4px); }
  .card-plate{
    display:flex;
    justify-content:space-between;
    align-items:center;
    padding:16px 22px;
    border-bottom:1px solid var(--panel-line);
    font-family:'JetBrains Mono', monospace;
    font-size:11px;
    color:var(--sand-dim);
    letter-spacing:1px;
  }
  .card-plate .status{ color:var(--olive); }
  .card-body{ padding:26px 22px 28px; }
  .card-body h3{
    font-family:'Oswald', sans-serif;
    font-size:24px;
    text-transform:uppercase;
    margin:0 0 4px;
    letter-spacing:0.3px;
  }
  .card-body .class-tag{
    font-size:12px;
    color:var(--rust-bright);
    text-transform:uppercase;
    letter-spacing:1px;
    margin-bottom:20px;
    display:block;
  }
  .specs{ list-style:none; margin:0; padding:0; }
  .specs li{
    display:flex;
    justify-content:space-between;
    padding:9px 0;
    border-bottom:1px dashed var(--panel-line);
    font-size:13px;
  }
  .specs li:last-child{ border-bottom:none; }
  .specs li span:first-child{ color:var(--sand-dim); }
  .specs li span:last-child{
    font-family:'JetBrains Mono', monospace;
    color:var(--sand);
  }

  /* --- Strip stat bar --- */
  .stat-strip{
    display:flex;
    flex-wrap:wrap;
    gap:0;
    border-top:1px solid var(--panel-line);
    border-bottom:1px solid var(--panel-line);
    margin:0 6vw 90px;
  }
  .stat{
    flex:1 1 160px;
    padding:28px 6px;
    text-align:center;
    border-right:1px solid var(--panel-line);
  }
  .stat:last-child{ border-right:none; }
  .stat .num{
    font-family:'Oswald', sans-serif;
    font-size:34px;
    color:var(--rust-bright);
    display:block;
  }
  .stat .label{
    font-family:'JetBrains Mono', monospace;
    font-size:11px;
    color:var(--sand-dim);
    letter-spacing:1px;
    text-transform:uppercase;
  }

  /* --- Footer / deploy stamp --- */
  .footer{
    padding:50px 6vw 40px;
    border-top:1px solid var(--panel-line);
    display:flex;
    justify-content:space-between;
    align-items:center;
    flex-wrap:wrap;
    gap:20px;
  }
  .footer .brand-mini{
    font-family:'Oswald', sans-serif;
    text-transform:uppercase;
    letter-spacing:1px;
    color:var(--sand-dim);
    font-size:13px;
  }
  .stamp{
    font-family:'JetBrains Mono', monospace;
    font-size:11px;
    letter-spacing:1px;
    color:var(--olive);
    border:1px solid var(--olive);
    padding:8px 16px;
    border-radius:2px;
    text-transform:uppercase;
  }

  @media (max-width:640px){
    .site-header{ padding:16px 5vw; }
    nav{ display:none; }
    .hero{ padding:80px 5vw 70px; }
    .fleet{ padding:50px 5vw 70px; }
    .section-head{ padding:0 5vw; }
    .stat-strip{ margin:0 5vw 70px; }
    .footer{ padding:40px 5vw 30px; }
  }
</style>
</head>
<body>

<header class="site-header">
  <div class="logo">
    <div class="logo-mark">
      <svg viewBox="0 0 24 24" fill="none" stroke="#e17a2e" stroke-width="1.6"><path d="M2 12c2-4 4-4 6 0s4 4 6 0 4-4 6 0"/></svg>
    </div>
    <div>
      EDBIN MOTORS
      <div class="coord">09.9312° N, 76.2673° E</div>
    </div>
  </div>
  <nav>
    <a href="#fleet">Fleet</a>
    <a href="#specs">Numbers</a>
    <a href="#contact">Contact</a>
  </nav>
</header>

<section class="hero">
  <div class="topo-bg"></div>
  <div class="eyebrow">Est. Kerala &nbsp;/&nbsp; Off-Road Division</div>
  <h1>Terrain has<br>never been<br><span>optional.</span></h1>
  <p class="lede">Three 4x4 platforms selected for one job: getting through ground that stops everything else. No trims for show — every spec below is one you'll actually use.</p>
  <div class="hero-ctas">
    <a href="#fleet" class="btn btn-primary">View the fleet</a>
    <a href="#contact" class="btn btn-ghost">Book a test drive</a>
  </div>
</section>

<div class="stat-strip">
  <div class="stat"><span class="num">4WD</span><span class="label">On every model</span></div>
  <div class="stat"><span class="num">3</span><span class="label">Platforms in stock</span></div>
  <div class="stat"><span class="num">V8</span><span class="label">Flagship engine</span></div>
  <div class="stat"><span class="num">24/7</span><span class="label">Recovery support</span></div>
</div>

<section class="fleet" id="fleet">
  <div class="section-head">
    <h2>The Fleet</h2>
    <span class="tag">INVENTORY // 3 UNITS ACTIVE</span>
  </div>
  <div class="grid">

    <div class="card">
      <div class="card-plate"><span>UNIT / LC-100</span><span class="status">● IN STOCK</span></div>
      <div class="card-body">
        <h3>Land Cruiser</h3>
        <span class="class-tag">Premium SUV</span>
        <ul class="specs">
          <li><span>Engine</span><span>4.7L V8</span></li>
          <li><span>Drivetrain</span><span>Full-Time 4WD</span></li>
          <li><span>Terrain Modes</span><span>6-Mode Crawl</span></li>
          <li><span>Ground Clearance</span><span>225 mm</span></li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-plate"><span>UNIT / FE-3.2</span><span class="status">● IN STOCK</span></div>
      <div class="card-body">
        <h3>Ford Endeavour</h3>
        <span class="class-tag">Adventure SUV</span>
        <ul class="specs">
          <li><span>Engine</span><span>3.2L Diesel</span></li>
          <li><span>Drivetrain</span><span>4x4 Shift-on-Fly</span></li>
          <li><span>Terrain Modes</span><span>Terrain Management</span></li>
          <li><span>Ground Clearance</span><span>228 mm</span></li>
        </ul>
      </div>
    </div>

    <div class="card">
      <div class="card-plate"><span>UNIT / HX-4D</span><span class="status">● IN STOCK</span></div>
      <div class="card-body">
        <h3>Toyota Hilux</h3>
        <span class="class-tag">Pickup Truck</span>
        <ul class="specs">
          <li><span>Engine</span><span>2.8L Turbo-D</span></li>
          <li><span>Drivetrain</span><span>Part-Time 4WD</span></li>
          <li><span>Payload Rating</span><span>Extreme Duty</span></li>
          <li><span>Ground Clearance</span><span>216 mm</span></li>
        </ul>
      </div>
    </div>

  </div>
</section>

<footer class="footer" id="contact">
  <span class="brand-mini">Edbin Motors © 2026</span>
  <span class="stamp">Deployed via Jenkins + Docker + AWS</span>
</footer>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
