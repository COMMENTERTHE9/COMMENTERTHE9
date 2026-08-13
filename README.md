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

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&size=14&duration=2800&pause=1200&color=0A84FF&center=true&vCenter=true&multiline=true&width=620&height=60&lines=Compiler+engineer.+Language+designer.+Systems+builder.;Cx+%7C+Blaze+%7C+building+in+public." alt="Typing SVG" />

<br/>

[![Cx Language](https://img.shields.io/badge/Cx-Systems_Language-0a84ff?style=for-the-badge&logo=rust&logoColor=white)](https://github.com/COMMENTERTHE9/Cx_lang)
![Blaze](https://img.shields.io/badge/Blaze-Compiler-ff6b35?style=for-the-badge)

</div>

---

## What I work on

I build compilers, design languages, and write the infrastructure that other software runs on. Two active projects right now.

---

## Active Projects

<table>
<tr>

<td width="50%" valign="top">

### [Cx Language](https://github.com/COMMENTERTHE9/Cx_lang)

Compiled systems language. No GC. Targets game engine developers and performance-critical software.

**Recently landed**
- Multi-file imports (`#![imports]`)
- String interpolation
- Generic structs
- Full if / else / while pipeline
- SSA backedges for loop lowering
- ABI + data layout locked
- Custom IR pretty printer
- JIT build + CI matrix

**Currently working on**
- Backend expansion
- More lowering coverage
- Compiler cleanup
- Docs and language structure

</td>

<td width="50%" valign="top">

### Blaze Compiler

Companion compiler project. Different design goal from Cx — governed world-change language with a locked spec.

**Recently landed**
- Dead file purge
- Header split from god-header
- Debug print gating
- AST complete redesign
- GGGX algorithm integration
- Solid Arithmetic Theory in type system

**Currently working on**
- Syntax audit
- Cleanup roadmap
- Codegen consolidation
- Compiler structure before deeper redesign

</td>

</tr>
</table>

---

## Stack

```
Language implementation  →  Rust
Blaze compiler           →  C (WSL)
CI / automation          →  GitHub Actions
Infra                    →  DigitalOcean / Cloudflare
```

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

## GitHub Stats

<div align="center">

<img src="https://streak-stats.demolab.com?user=COMMENTERTHE9&theme=github-dark-blue&hide_border=true&cache_seconds=86400" alt="GitHub streak" />

</div>

---

## Contributions

<div align="center">

![Starry Contributions](https://raw.githubusercontent.com/COMMENTERTHE9/COMMENTERTHE9/main/starry-contributions.svg?v=fd7aabc2)

</div>

---

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-COMMENTERTHE9-0a84ff?style=flat-square&logo=github)](https://github.com/COMMENTERTHE9)

</div>
