---
layout: default
title: AI Art Review Desk
---

{% include nav.html %}

# AI Art Review Desk

<p class="project-detail-kicker">AI-powered Art Competition Review Demo</p>

<div class="project-detail-hero">
  <img src="{{ '/assets/images/painting_brushes.jpg' | relative_url }}" alt="Paint brushes and artwork materials">
  <div>
    <p>AI-powered pre-review workspace for art and design competition submissions.</p>
    <dl class="project-meta project-meta-detail">
      <div>
        <dt>Role</dt>
        <dd>AI Product Builder / Prototype Lead</dd>
      </div>
      <div>
        <dt>Tools</dt>
        <dd>Figma, HTML/CSS/JavaScript, Vite, Codex, GitHub, Netlify, Cloudflare</dd>
      </div>
      <div>
        <dt>Status</dt>
        <dd>Static MVP / Mock AI Demo</dd>
      </div>
    </dl>
    <a class="project-demo-link" href="https://jojoslab.com" target="_blank" rel="noopener">Open Demo</a>
  </div>
</div>

## Project Overview

AI Art Review Desk is a static MVP for an AI-powered pre-review workspace designed for art and design competition submissions. The demo helps students, teachers, and competition organizers preview how an AI-assisted review flow could support work evaluation, feedback generation, and revision planning before formal submission.

## Problem

In art and design competitions, students often lack structured feedback before submission, while teachers spend significant time giving repetitive comments on theme alignment, visual expression, originality, completeness, and competition fit. The goal of this project was to turn a vague "AI review assistant" idea into a concrete, clickable, and deployable product demo.

## Target Users

Primary users:

- Art and design students preparing competition submissions
- Teachers providing pre-submission feedback
- Competition organizers exploring AI-assisted review workflows

## My Role

I worked on product framing, interaction flow, prototype iteration, front-end demo implementation support, mock AI review logic, deployment, and technical boundary planning. I used Codex-assisted development to turn the product concept into a static web demo and deployed it through Netlify with a custom domain.

## Product Scope

The project focuses on validating the core pre-review workflow before adding production infrastructure, authentication, or real model calls.

## Key Features

- Multi-image work upload and preview
- Competition/category navigation structure
- Mock AI pre-review report generation
- Structured scoring dimensions
- Review history persistence
- Static deployment with custom domain
- Future API proxy architecture planning

## Design & Technical Decisions

The first version intentionally avoids direct integration with a real model API. Instead, it uses a mock AI review flow to validate the user journey, report structure, and product positioning before introducing backend complexity.

For future real-model integration, the system would require a backend proxy layer:

```text
static frontend -> /api/reviews -> backend/serverless proxy -> model provider API
```

This prevents API keys from being exposed in the browser and allows future support for authentication, file handling, model routing, logging, and evaluation metrics.

## Demo & Deployment

The public static MVP is available at [jojoslab.com](https://jojoslab.com).

## Limitations

Current limitations:

- The AI review is mocked and does not call a real model API.
- Image understanding is not yet implemented.
- The review criteria are static and not yet connected to a competition-specific knowledge base.
- The demo is optimized for product validation rather than production-scale deployment.

## Next Steps

Next steps include integrating a backend proxy, connecting a real multimodal model API, building a competition criteria knowledge base, improving report quality, adding teacher-editable review rubrics, and collecting feedback from students and teachers.

## What I Learned

This project clarified how to move from a broad AI product idea into a scoped, deployable prototype. I learned to separate product validation from production infrastructure, make mock AI behavior explicit, and plan a safer future architecture before introducing real model APIs.

[← Return to Projects]({{ '/projects/' | relative_url }}){: .btn-outline}
