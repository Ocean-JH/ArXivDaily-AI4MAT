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

## New Papers (2)

*Last updated: 2025-10-15 06:16:24 (SGT)*

### 1. Machine Learning-Driven Insights into Excitonic Effects in 2D Materials

**Authors:** Ahsan Javed, Sajid Ali

**Published:** 2025-01-02

**Category:** cond-mat.mtrl-sci

**ID:** 2501.01092v3

**Link:** [http://arxiv.org/abs/2501.01092v3](http://arxiv.org/abs/2501.01092v3)

**Summary:** Understanding excitonic effects in two-dimensional (2D) materials is critical
for advancing their potential in next-generation electronic and photonic
devices. In this study, we introduce a machine learning (ML)-based framework to
predict exciton binding energies in 2D materials, offering a computationally
efficient alternative to traditional methods such as many-body perturbation
theory (GW) and the Bethe-Salpeter equation. Leveraging data from the
Computational 2D Materials Database (C2DB), our ML models establish connections
between cheaply available material descriptors and complex excitonic
properties, significantly accelerating the screening process for materials with
pronounced excitonic effects. Additionally, Bayesian optimization with Gaussian
process regression was employed to efficiently filter materials with largest
exciton binding energies, further enhancing the discovery process. Although
developed for 2D systems, this approach is versatile and can be extended to
three-dimensional materials, broadening its applicability in materials
discovery....

---

### 2. Controllable Graph Generation with Diffusion Models via Inference-Time Tree Search Guidance

**Authors:** Jiachi Zhao, Zehong Wang, Yamei Liao, Chuxu Zhang, Yanfang Ye

**Published:** 2025-10-12

**Category:** cs.LG

**ID:** 2510.10402v1

**Link:** [http://arxiv.org/abs/2510.10402v1](http://arxiv.org/abs/2510.10402v1)

**Summary:** Graph generation is a fundamental problem in graph learning with broad
applications across Web-scale systems, knowledge graphs, and scientific domains
such as drug and material discovery. Recent approaches leverage diffusion
models for step-by-step generation, yet unconditional diffusion offers little
control over desired properties, often leading to unstable quality and
difficulty in incorporating new objectives. Inference-time guidance methods
mitigate these issues by adjusting the sampling process without retraining, but
they remain inherently local, heuristic, and limited in controllability. To
overcome these limitations, we propose TreeDiff, a Monte Carlo Tree Search
(MCTS) guided dual-space diffusion framework for controllable graph generation.
TreeDiff is a plug-and-play inference-time method that expands the search space
while keeping computation tractable. Specifically, TreeDiff introduces three
key designs to make it practical and scalable: (1) a macro-step expansion
strategy that groups multiple denoising updates into a single transition,
reducing tree depth and enabling long-horizon exploration; (2) a dual-space
denoising mechanism that couples efficient latent-space denoising with
lightweight discrete correction in graph space, ensuring both scalability and
structural fidelity; and (3) a dual-space verifier that predicts long-term
rewards from partially denoised graphs, enabling early value estimation and
removing the need for full rollouts. Extensive experiments on 2D and 3D
molecular generation benchmarks, under both unconditional and conditional
settings, demonstrate that TreeDiff achieves state-of-the-art performance.
Notably, TreeDiff exhibits favorable inference-time scaling: it continues to
improve with additional computation, while existing inference-time methods
plateau early under limited resources....

---


<!-- ARXIV_PAPERS_END -->