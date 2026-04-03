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
As an AI Product Builder, I build AI-powered tools to improve learning and decision-making efficiency. As a philosopher turned technologist, I explore the ethics of artificial intelligence and design technologies grounded in humanity.

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
  <h2>Google Store User Data Dashboard</h2>
  <p>
问题：
比较谷歌商店的应用
<br>
解决方案：
构建可视化dashboard，提供交互式数据分析
<br>
我的贡献：
- 使用AI辅助开发
- 设计交互逻辑
- 优化信息结构
<br>
结果：
提升数据理解效率
  </p>

  <div class="card-container">
    <!-- Card 1 -->
    <div class="card" data-pdf="{{ '/projects/streamlit_app.py' | relative_url }}">
      <img src="/project/google_user_data_dashboard.jpg" alt="Google Store User Data Dashboard">
      <div class="card-content">
        <h3>Google Store User Data Dashboard</h3>
      </div>
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
