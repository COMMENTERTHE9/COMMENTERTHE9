<div align="center">

```
 ██████╗██╗  ██╗
██╔════╝╚██╗██╔╝
██║      ╚███╔╝ 
██║      ██╔██╗ 
╚██████╗██╔╝ ██╗
 ╚═════╝╚═╝  ╚═╝
```

### COMMENTERTHE9

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=15&duration=2800&pause=1200&color=0A84FF&center=true&vCenter=true&multiline=true&width=620&height=70&lines=Compiler+engineer.+Language+designer.+Systems+builder.;No+GC.+No+pauses.+No+abstractions+you+didn%27t+ask+for.;Turning+ideas+that+don%27t+exist+yet+into+things+that+compile." alt="Typing SVG" />

<br/>

[![Cx Language](https://img.shields.io/badge/Cx-Systems%20Language-0a84ff?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/COMMENTERTHE9/Cx_lang)
[![Blaze](https://img.shields.io/badge/Blaze-Compiler-ff6b35?style=for-the-badge&logo=llvm&logoColor=white)](#)
[![Cogito](https://img.shields.io/badge/Cogito-LeetCode%20for%20AI-00c896?style=for-the-badge&logo=rust&logoColor=white)](#)
[![Status](https://img.shields.io/badge/Status-Shipping-1aff6e?style=for-the-badge)](#)

</div>

---

<table>
<tr>
<td width="55%" valign="top">

## What I Build

I write compilers, design languages, and build the infrastructure that other software runs on.

My primary work is **Cx** — a compiled systems language targeting game engine developers and performance-critical software. No garbage collector. No runtime pauses. No abstractions you didn't ask for. The control you want, the clarity you deserve.

Alongside that: **Blaze**, a governed world-change language with a locked spec. **Cogito**, a deterministic AI evaluation platform. And further back — a space MMO with universe-physics, not game-mechanics.

I don't prototype. I ship compilers.

</td>
<td width="45%" valign="top">

## Stack

```
Language Implementation  →  Rust
Cx Compiler Backend      →  Custom IR + LLVM
Blaze Compiler           →  C (WSL)
Web Platform (Cogito)    →  Leptos + Axum
Database                 →  PostgreSQL / SeaORM
Build & CI               →  GitHub Actions
Infra                    →  DigitalOcean / Cloudflare
```

</td>
</tr>
</table>

---

## Active Projects

<table>
<tr>

<td width="33%" valign="top">

### 🔵 [Cx Language](https://github.com/COMMENTERTHE9/Cx_lang)

A compiled systems language for engine developers and performance-first software.

```
v4.5 — 10 of 19 hard blockers done
Test matrix: 78/78 green
```

**Shipped:**
- Multi-file imports (`#![imports]`)
- String interpolation
- Generic structs
- Full if/else/while pipeline
- SSA backedges for loop lowering
- ABI & data layout locked
- Custom IR with pretty printer
- JIT build + CI matrix

**Philosophy:** *Python for adults.*
Control without the mess.
Performance without the lies.

</td>

<td width="33%" valign="top">

### 🟠 Blaze Compiler

A governed world-change language with a locked spec. Companion to Cx, designed for a different kind of correctness.

**Recent work:**
- Dead file purge + god-file splits
- Debug print gating
- Header architecture redesign
- AST complete overhaul
- GGGX algorithm integration
- Solid Arithmetic Theory in type system

**Design principle:** The spec is locked. The compiler follows the language — not the other way around.

</td>

<td width="33%" valign="top">

### 🟢 Cogito

*LeetCode for AI.*

A deterministic evaluation platform for assessing AI model capability — built on real scoring, not vibes.

**Stack:** Leptos · Axum · PostgreSQL · SeaORM · Stripe
**Evaluator:** Deterministic Rust engine (no LLM scoring)
**Design language:** Industrial. Dark. Monospace. No purple.

> If you can't measure it deterministically, you don't know it.

</td>

</tr>
</table>

---

## The Cx Philosophy

<div align="center">

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   No GC.          You don't pay for what you don't use.                 │
│   No pauses.      Latency is a feature, not a footnote.                 │
│   No abstractions you didn't ask for.                                   │
│                                                                         │
│   Memory you control. Performance you can reason about.                 │
│   Built for engines, tools, and software with a point of view.          │
│                                                                         │
│   Cx is not trying to be the next Rust or the next C.                   │
│   It's trying to be the first Cx.                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

</div>

---

## Compiler Architecture (Cx)

```
Source (.cx)
    │
    ▼
┌──────────────┐    ┌──────────────────┐    ┌───────────────────┐
│   Frontend   │───▶│   Semantic /     │───▶│   IR Lowering     │
│              │    │   Type Checker   │    │   (SSA form)      │
│  Lexer       │    │                  │    │                   │
│  Parser      │    │  Generic structs │    │  Function calls   │
│  Multi-file  │    │  Type inference  │    │  While loops      │
│  imports     │    │  Const / pub     │    │  Backedges        │
└──────────────┘    └──────────────────┘    └─────────┬─────────┘
                                                      │
                                                      ▼
                                           ┌───────────────────┐
                                           │   Backend (WIP)   │
                                           │                   │
                                           │  ABI locked       │
                                           │  Data layout      │
                                           │  Scalar types     │
                                           │  Code emission    │
                                           └───────────────────┘
```

---

## What I Think About

- Language design as a philosophical act — compilers have opinions whether you admit it or not
- What it means for a type system to tell the truth
- ABI decisions and their downstream consequences across years of code
- IR design that stays readable under transformation
- Deterministic evaluation over probabilistic guessing
- Systems that are correct by construction, not by convention
- Why performance and clarity are not a tradeoff

---

## GitHub Stats

<div align="center">

<img height="175" src="https://github-readme-stats.vercel.app/api?username=COMMENTERTHE9&show_icons=true&theme=dark&hide_border=true&cache_seconds=86400" alt="GitHub stats" />
<img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=COMMENTERTHE9&layout=compact&theme=dark&hide_border=true&cache_seconds=86400" alt="Top languages" />

<br/>

<img src="https://streak-stats.demolab.com?user=COMMENTERTHE9&theme=github-dark-blue&hide_border=true&cache_seconds=86400" alt="GitHub streak" />

</div>
---

## Contribution Activity

## Contribution Activity

<div align="center">

![Starry Contributions](https://raw.githubusercontent.com/COMMENTERTHE9/COMMENTERTHE9/main/starry-contributions.svg)

</div>

<details>
<summary>✨ Enable the contribution snake animation (one-time setup)</summary>

Create `.github/workflows/snake.yml` in your profile repo:

```yaml
name: Generate Snake

on:
  schedule:
    - cron: "0 */12 * * *"
  workflow_dispatch:

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: Platane/snk@v3
        with:
          github_user_name: ${{ github.repository_owner }}
          outputs: |
            dist/github-contribution-grid-snake-dark.svg?palette=github-dark
      - uses: crazy-max/ghaction-github-pages@v3.1.0
        with:
          target_branch: output
          build_dir: dist
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

Then swap the activity graph image above for:

```
![snake](https://raw.githubusercontent.com/COMMENTERTHE9/COMMENTERTHE9/output/github-contribution-grid-snake-dark.svg)
```

</details>

---

<div align="center">

**COMMENTERTHE9** · Compiler Engineer · Language Designer · Systems Builder

*The goal isn't to make another language. The goal is to make the right one.*

[![GitHub](https://img.shields.io/badge/GitHub-COMMENTERTHE9-0a84ff?style=flat-square&logo=github)](https://github.com/COMMENTERTHE9)

</div>
<div align="center">

**COMMENTERTHE9** · Compiler Engineer · Language Designer · Systems Builder

*The goal isn't to make another language. The goal is to make the right one.*

[![GitHub](https://img.shields.io/badge/GitHub-COMMENTERTHE9-0a84ff?style=flat-square&logo=github)](https://github.com/COMMENTERTHE9)

</div>
