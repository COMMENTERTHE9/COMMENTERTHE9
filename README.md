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

**Compiler engineer. Language designer. Systems builder.**

*Turning ideas that don't exist yet into things that compile.*

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
- Solid Arithmetic Theory embedded in type system

**Design principle:** The spec is locked. The compiler follows the language — not the other way around.

</td>

<td width="33%" valign="top">

### 🟢 Cogito

*LeetCode for AI.*

A deterministic evaluation platform for assessing AI model capability — built on real scoring, not vibes.

**Stack:** Leptos · Axum · PostgreSQL · SeaORM · Stripe  
**Evaluator:** Deterministic Rust engine (no LLM-based scoring)  
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

<table>
<tr>
<td width="50%">

**Technical**
- Language design as a philosophical act
- What it means for a compiler to have a point of view  
- ABI decisions and their downstream consequences
- IR design that stays readable under transformation
- Deterministic evaluation over probabilistic guessing
- Systems that are correct by construction, not by convention

</td>
<td width="50%">



</td>
</tr>
</table>

---

## GitHub Stats

<div align="center">
  <img height="175" src="https://github-readme-stats.vercel.app/api?username=COMMENTERTHE9&show_icons=true&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=0a84ff&icon_color=0a84ff&text_color=c9d1d9" />
  <img height="175" src="https://github-readme-stats.vercel.app/api/top-langs/?username=COMMENTERTHE9&layout=compact&theme=github_dark&hide_border=true&bg_color=0d1117&title_color=0a84ff&text_color=c9d1d9" />
</div>

<div align="center">
  <img src="https://streak-stats.demolab.com?user=COMMENTERTHE9&theme=github-dark-blue&hide_border=true&background=0d1117&ring=0a84ff&fire=ff6b35&currStreakLabel=0a84ff" />
</div>

---

<div align="center">

**COMMENTERTHE9** · Compiler Engineer · Language Designer · Systems Builder

*The goal isn't to make another language. The goal is to make the right one.*

[![GitHub](https://img.shields.io/badge/GitHub-COMMENTERTHE9-0a84ff?style=flat-square&logo=github)](https://github.com/COMMENTERTHE9)

</div>
