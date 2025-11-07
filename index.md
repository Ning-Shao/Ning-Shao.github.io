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

<!-- sale window -->

<section id="studio" style="
  margin: 4rem auto;
  max-width: 1100px;
  padding: 2.5rem;
  border-radius: 22px;
  background: rgba(255, 255, 255, 0.55);
  box-shadow: 0 8px 25px rgba(0,0,0,0.1);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  text-align: center;
  font-family: 'Nunito Sans', sans-serif;
  opacity: 0;
  transform: translateY(30px);
  transition: all 1s ease;
" class="fade-in">

<h2 style="color:#2e503d;font-size:2rem;font-weight:700;">Design & Resume Studio</h2>
<p style="margin-top:1rem;color:#333;font-size:1.1rem;">
  Build your stylish personal brand.<br>
  Provide <strong>personal website</strong> and <strong>resume developmeny</strong> service, with your personal traits/ 

<!-- sample display -->
<div style="
    margin-top:2rem;
    display:flex;
    overflow-x:auto;
    gap:1.5rem;
    padding-bottom:1rem;
    scroll-snap-type:x mandatory;
  ">

    <div style="
      flex:0 0 320px;
      scroll-snap-align:start;
      border-radius:16px;
      overflow:hidden;
      background:white;
      box-shadow:0 4px 15px rgba(0,0,0,0.08);
      transition:transform 0.3s;
    " onmouseover="this.style.transform='scale(1.03)'" onmouseout="this.style.transform='scale(1)'">
      <img src="images/resume1.jpg" alt="Resume Design" style="width:100%;height:210px;object-fit:cover;">
      <div style="padding:1rem;">
        <h3 style="color:#2e503d;">sample design according to your position applied</h3>
        <p style="font-size:0.9rem;">descriptions tbd</p>
      </div>
    </div>

    <div style="
      flex:0 0 320px;
      scroll-snap-align:start;
      border-radius:16px;
      overflow:hidden;
      background:white;
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
      background:white;
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
    <a href="https://formspree.io/f/mldopkjb" style="
      text-decoration:none;
      background-color:#3367D6;
      color:white;
      padding:0.9rem 2rem;
      border-radius:10px;
      font-weight:600;
      font-size:1rem;
      transition:0.3s;
    " onmouseover="this.style.background='#244eb0'" onmouseout="this.style.background='#3367D6'">Get Your Quote</a>
  </div>
</section>

<script>
  window.addEventListener('scroll', () => {
    document.querySelectorAll('.fade-in').forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 100) {
        el.style.opacity = 1;
        el.style.transform = 'translateY(0)';
      }
    });
  });
</script>
  

