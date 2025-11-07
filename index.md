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

<!-- ===== PDF Modal Window (Reusable) ===== -->
<div id="pdfModal">
  <div class="modal-content">
    <span class="close-btn" onclick="document.getElementById('pdfModal').style.display='none'">&times;</span>
    <a id="downloadLink" class="download-btn" href="#" download>⬇ Download File</a>
    <iframe id="pdfFrame" src=""></iframe>
  </div>
</div>

<section id="studio" class="fade-in">
  <h2>Jojo's Design Studio</h2>
  <p>
    Build your stylish personal brand.<br>
    Provide <strong>personal website</strong> and <strong>resume development</strong> service, with your personal traits.
  </p>

  <div class="card-container">
    <!-- Card 1 -->
    <div class="card" data-pdf="{{ '/design/cvsample1.pdf' | relative_url }}">
      <iframe src="https://docs.google.com/gview?embedded=true&url=https://ning-shao.github.io/design/cvsample1.pdf"></iframe>
      <div class="card-content">
        <h3>CV Sample (Click to View)</h3>
        <p>A professional LaTeX-designed resume sample.</p>
      </div>
    </div>

    <!-- Card 2 -->
    <div class="card" data-pdf="{{ '/design/cvsample2.pdf' | relative_url }}">
      <img src="/images/portfolio1.jpg" alt="Website Design">
      <div class="card-content">
        <h3>Website Portfolio</h3>
        <p>Showcase of personal website designs.</p>
      </div>
    </div>

    <!-- Card 3 -->
    <div class="card" data-pdf="{{ '/design/cvsample3.pdf' | relative_url }}">
      <img src="/images/resume2.jpg" alt="Creative Resume">
      <div class="card-content">
        <h3>Creative CV</h3>
        <p>Emphasize on visual design and personality expression.</p>
      </div>
    </div>
  </div>

  <div style="margin-top:2rem;">
    <a href="/contact" class="btn-green">Get Your Quote</a>
  </div>
</section>

<script>
  // PDF Modal Control
  const modal = document.getElementById('pdfModal');
  const pdfFrame = document.getElementById('pdfFrame');
  const downloadLink = document.getElementById('downloadLink');

  document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
      const pdfPath = card.getAttribute('data-pdf');
      pdfFrame.src = pdfPath;
      downloadLink.href = pdfPath;
      modal.style.display = 'flex';
    });
  });

  // click background to close Modal
  modal.addEventListener('click', e => {
    if (e.target === modal) modal.style.display = 'none';
  });
</script>
