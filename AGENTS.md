# AI Agent Guide for John Marcus Aziz portfolio

This document provides comprehensive context and guidelines for AI agents working on this repository.

## 0. Agent Mission

The agent’s goal is to continuously improve this portfolio site by:

- Increasing clarity, professionalism, and impact of content
- Optimizing for recruiter and hiring manager engagement
- Maintaining fast load times and GitHub Pages compatibility
- Improving SEO and accessibility
- Preserving a clean, modern visual design

When making changes, prioritize:

1. Readability and scannability
2. Measurable impact (metrics, outcomes)
3. Simplicity over complexity

## 1. Project Identity

- **Name**: John Marcus Aziz
- **Purpose**: Professional portfolio website for John Marcus Aziz, Innovative solutions architect and entrepreneur with 20+ years driving digital transformation, AI/ML, and enterprise IT solutions.
- **Type**: Single Page Application (SPA)
- **Live URL**: [resume.johnmarcusaziz.com](https://resume.johnmarcusaziz.com)

## Key Achievements

- Led AI transformation impacting $X revenue
- Reduced costs by X% across enterprise systems
- Scaled platform to X users

## Target Roles

- Solutions Architect
- AI/ML Leader
- Enterprise Architect
- CTO / Head of Engineering

## 2. Technology Stack

- This is a static Jekyll site with no JavaScript build pipeline.
- Do not introduce Node.js, npm, or complex build systems.
- Keep the site compatible with native GitHub Pages builds.

## 3. Project Structure

```Markdown

JA-resume/
├── _config.yml
├── AGENTS.md
├── AUTHORS.md
├── CHANGELOG.md
├── CNAME
├── coverpage.md
├── index.md
├── LICENSE.md
├── NEWS.md
├── README.md
├── resume.md
├── resume.pdf
├── resume.odt
├── SECURITY.md

```

## 4. Development Workflow

## 5. Design System & Aesthetics

- Use lightweight CSS only (no heavy JS frameworks)
- Prefer inline styles or minimal CSS files
- Avoid dependencies that GitHub Pages cannot build

- Visual Guidelines:
  - Use subtle glassmorphism (avoid overuse)
  - Ensure text contrast meets accessibility standards
  - Keep animations minimal and performant

- Mobile-first design is required

## 6. Content Strategy

- Use concise, results-driven bullet points (Google/consulting style)
- Each experience entry should:
  - Start with a strong action verb
  - Include measurable outcomes (%, $, scale, performance)
  - Be 1–2 lines max per bullet

- Tone:
  - Professional, confident, and direct
  - Avoid buzzwords without proof
  - Avoid fluff or generic claims

- Prioritize:
  - AI/ML, digital transformation, and enterprise impact
  - Leadership and ownership
  - Business outcomes over technical details

- Avoid:
  - Long paragraphs
  - First-person pronouns (“I”, “me”)

## 7. Agent Guidelines & Rules

- Do NOT:
  - Introduce frameworks (React, Vue, etc.)
  - Add backend services
  - Break GitHub Pages compatibility

- Prefer:
  - Markdown-first solutions
  - Simplicity over feature expansion
  - Readability over visual complexity

- When editing:
  - Make small, incremental changes
  - Preserve existing working structure
  - Ensure links and anchors still function

- Always validate:
  - Markdown renders correctly
  - No broken links

## 8. Deployment

- The project is deployed on GitHub Pages.
- Deploys automatically on push to `main`.

## 9. SEO & Performance

- Use semantic HTML via Markdown (headings in correct order)
- Ensure each page has:
  - Title
  - Meta description
- Optimize images (if added) for size

- Prioritize:
  - Fast load time (<2s)
  - Minimal external dependencies

- Use keywords:
  - "Solutions Architect"
  - "AI/ML"
  - "Digital Transformation"
  - "Enterprise IT"

## 10. Change Safety Guidelines

### Safe Changes

- Editing content in .md files
- Improving wording and formatting
- Updating styles within existing theme constraints

### Risky Changes (require caution)

- Changing _config.yml
- Modifying theme structure
- Adding external scripts or dependencies

## 11. Execution Rules

When making changes:

- Always output full file contents when editing
- Do not describe changes — implement them
- Prefer modifying existing files over creating new ones
- Keep formatting valid Markdown

If unsure:

- Ask for clarification instead of guessing
