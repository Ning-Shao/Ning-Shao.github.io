---
layout: default
title: Home
---

<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
  <a href="/projects">Projects</a>
  <a href="/contact">Contact</a>
</nav>

# Welcome to Ning's personal website. 
<div class="soft-intro">
  Hi! I’m Ning Shao — a philosopher turned technologist. I explore the ethics of artificial intelligence and design technologies grounded in humanity.

</div>

<!-- ===== PDF Modal Window ===== -->
<div id="pdfModal" style="
  display:none;
  position:fixed;
  top:0;
  left:0;
  width:100%;
  height:100%;
  background:rgba(0,0,0,0.7);
  justify-content:center;
  align-items:center;
  z-index:999;
">
  <div style="
    position:relative;
    width:85%;
    height:85%;
    background:white;
    border-radius:12px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
  ">

    <!-- Close Button -->
    <span onclick="document.getElementById('pdfModal').style.display='none'" 
      style="
        position:absolute;
        top:10px;
        right:20px;
        font-size:2rem;
        color:#333;
        cursor:pointer;
        z-index:1000;
      ">&times;</span>

    <!-- Download Button -->
    <a href="{{ '/design/cvsample1.pdf' | relative_url }}" download style="
      position:absolute;
      top:12px;
      right:70px;
      background: linear-gradient(135deg, #2e503d, #5b8c63);
      color: #f9f9f7;
      padding: 0.4rem 1rem;
      border-radius: 8px;
      font-weight: 600;
      font-size: 0.9rem;
      box-shadow: 0 4px 10px rgba(46,80,61,0.25);
      text-decoration:none;
      transition: background 0.3s ease, transform 0.2s ease;
      z-index:1000;
    " 
    onmouseover="this.style.background='linear-gradient(135deg,#3f6b4e,#6fa47b)'; this.style.transform='translateY(-1px)'"
    onmouseout="this.style.background='linear-gradient(135deg,#2e503d,#5b8c63)'; this.style.transform='translateY(0)'">
      ⬇ Download CV
    </a>

    <!-- PDF Viewer -->
    <iframe src="{{ '/design/cvsample1.pdf' | relative_url }}" 
      style="width:100%;height:100%;border:none;"></iframe>
  </div>
</div>

<section id="studio" style="
  margin: 4rem auto;
  max-width: 1100px;
  padding: 2.5rem;
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.25);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  text-align: center;
  font-family: 'Nunito Sans', sans-serif;
  opacity: 1;
  transform: none; 
  transition: all 1s ease;
" class="fade-in">

<h2 style="color:#2e503d;font-size:2rem;font-weight:700;">Jojo's Design Studio</h2>
<p style="margin-top:1rem;color:#333;font-size:1.1rem;">
  Build your stylish personal brand.<br>
  Provide <strong>personal website</strong> and <strong>resume developmeny</strong> service, with your personal traits
</p>

<!-- sample display -->
<div style="
    margin-top:2rem;
    display:flex;
    overflow-x:auto;
    gap:1.5rem;
    padding-bottom:1rem;
    scroll-snap-type:x mandatory;
  ">

  <!-- CV Sample Card -->
 <div style="
  flex:0 0 320px;
  scroll-snap-align:start;
  border-radius:16px;
  overflow:hidden;
  background: rgba(255,255,255,0.65);
  backdrop-filter: blur(6px);
  box-shadow:0 4px 15px rgba(0,0,0,0.08);
  transition:transform 0.3s;
  cursor:pointer;
" 
onmouseover="this.style.transform='scale(1.03)'" 
onmouseout="this.style.transform='scale(1)'"
onclick="document.getElementById('pdfModal').style.display='flex'">

  <img src="https://via.placeholder.com/320x210.png?text=CV+Sample" alt="Resume Sample" style="width:100%;height:210px;object-fit:cover;">
  <div style="padding:1rem;">
    <h3 style="color:#2e503d;">CV Sample (Click to View)</h3>
    <p style="font-size:0.9rem;">A professional LaTeX-designed resume sample.</p>
  </div>
</div>

    <div style="
      flex:0 0 320px;
      scroll-snap-align:start;
      border-radius:16px;
      overflow:hidden;
      background: rgba(255,255,255,0.65);
      backdrop-filter: blur(6px);
      box-shadow:0 4px 15px rgba(0,0,0,0.08);
      transition:transform 0.3s;
    " onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
      <img src="images/portfolio1.jpg" alt="Website Design" style="width:100%;height:210px;object-fit:cover;">
      <div style="padding:1rem;">
        <h3 style="color:#2e503d;">Website development: Personal website</h3>
        <p style="font-size:0.9rem;">descriptions tbd</p>
      </div>
    </div>

    <div style="
      flex:0 0 320px;
      scroll-snap-align:start;
      border-radius:16px;
      overflow:hidden;
      background: rgba(255,255,255,0.65);
      backdrop-filter: blur(6px);
      box-shadow:0 4px 15px rgba(0,0,0,0.08);
      transition:transform 0.3s;
    " onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
      <img src="images/resume2.jpg" alt="Creative Resume" style="width:100%;height:210px;object-fit:cover;">
      <div style="padding:1rem;">
        <h3 style="color:#2e503d;">CV Design: innovative traits</h3>
        <p style="font-size:0.9rem;">emphasize on visual design and personal expression</p>
      </div>
    </div>

  </div>

  <!-- button -->
  <div style="margin-top:2rem;">
    <a href="/contact" style="
      text-decoration:none;
    background: linear-gradient(135deg, #2e503d, #5b8c63);
    color: #f9f9f7;
    padding: 0.9rem 2rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 1rem;
    box-shadow: 0 6px 16px rgba(46,80,61,0.25);
    transition: background 0.4s ease, transform 0.3s ease;
  " onmouseover="this.style.background='linear-gradient(135deg,#3f6b4e,#6fa47b)'; this.style.transform='translateY(-2px)'"
    onmouseout="this.style.background='linear-gradient(135deg,#2e503d,#5b8c63)'; this.style.transform='translateY(0)'">
    Get Your Quote
    </a>
  </div>
</section>



  

