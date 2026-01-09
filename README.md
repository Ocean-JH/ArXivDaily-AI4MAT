# ArXiv Daily - AI4MAT

**Daily automatic updates of the latest arXiv papers on AI for Materials Science (AI4MatSci).** 

Stay informed with cutting-edge research at the intersection of artificial intelligence and materials science — automatically!

## :bookmark: Related Fields

- (Computational) Materials Science
- Machine Learning
- Materials Design
- Crystal Structure Prediction
- Generative AI for Materials Discovery

## :star: Customize Yours

Let's start with a star :star:!

And then, feel free to adjust the `query` field in the file `config.json` to match your own research interests(see [arXiv API User's Manual](https://info.arxiv.org/help/api/user-manual.html#51-details-of-query-construction) for more information)!

## :handshake: Contributions

Contributions are welcome!
 Feel free to open an Issue or a Pull Request if you have ideas for improvement, new features, or better queries.

## :blue_heart: ​Acknowledge

Thank you to [arXiv](https://arxiv.org/) for use of its open access interoperability.

---

## :scroll: Paper List


<!-- ARXIV_PAPERS_START -->

## New Papers (1)

*Last updated: 2026-01-10 06:19:30 (SGT)*

### 1. LinkD: AutoRegressive Diffusion Model for Mechanical Linkage Synthesis

**Authors:** Yayati Jadhav, Amir Barati Farimani

**Published:** 2026-01-07

**Category:** cs.LG

**ID:** 2601.04054v1

**Link:** [http://arxiv.org/abs/2601.04054v1](http://arxiv.org/abs/2601.04054v1)

**Summary:** Designing mechanical linkages to achieve target end-effector trajectories presents a fundamental challenge due to the intricate coupling between continuous node placements, discrete topological configurations, and nonlinear kinematic constraints. The highly nonlinear motion-to-configuration relationship means small perturbations in joint positions drastically alter trajectories, while the combinatorially expanding design space renders conventional optimization and heuristic methods computationally intractable. We introduce an autoregressive diffusion framework that exploits the dyadic nature of linkage assembly by representing mechanisms as sequentially constructed graphs, where nodes correspond to joints and edges to rigid links. Our approach combines a causal transformer with a Denoising Diffusion Probabilistic Model (DDPM), both conditioned on target trajectories encoded via a transformer encoder. The causal transformer autoregressively predicts discrete topology node-by-node, while the DDPM refines each node's spatial coordinates and edge connectivity to previously generated nodes. This sequential generation enables adaptive trial-and-error synthesis where problematic nodes exhibiting kinematic locking or collisions can be selectively regenerated, allowing autonomous correction of degenerate configurations during design. Our graph-based, data-driven methodology surpasses traditional optimization approaches, enabling scalable inverse design that generalizes to mechanisms with arbitrary node counts. We demonstrate successful synthesis of linkage systems containing up to 20 nodes with extensibility to N-node architectures. This work advances autoregressive graph generation methodologies and computational kinematic synthesis, establishing new paradigms for scalable inverse design of complex mechanical systems....

---


<!-- ARXIV_PAPERS_END -->