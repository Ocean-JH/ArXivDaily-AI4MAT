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

*Last updated: 2025-07-09 06:17:47 (SGT)*

### 1. TopoMAS: Large Language Model Driven Topological Materials Multiagent System

**Authors:** Baohua Zhang, Xin Li, Huangchao Xu, Zhong Jin, Quansheng Wu, Ce Li

**Published:** 2025-07-05

**Category:** cond-mat.mtrl-sci

**ID:** 2507.04053v1

**Link:** [http://arxiv.org/abs/2507.04053v1](http://arxiv.org/abs/2507.04053v1)

**Summary:** Topological materials occupy a frontier in condensed-matter physics thanks to
their remarkable electronic and quantum properties, yet their cross-scale
design remains bottlenecked by inefficient discovery workflows. Here, we
introduce TopoMAS (Topological materials Multi-Agent System), an interactive
human-AI framework that seamlessly orchestrates the entire materials-discovery
pipeline: from user-defined queries and multi-source data retrieval, through
theoretical inference and crystal-structure generation, to first-principles
validation. Crucially, TopoMAS closes the loop by autonomously integrating
computational outcomes into a dynamic knowledge graph, enabling continuous
knowledge refinement. In collaboration with human experts, it has already
guided the identification of novel topological phases SrSbO3, confirmed by
first-principles calculations. Comprehensive benchmarks demonstrate robust
adaptability across base Large Language Model, with the lightweight Qwen2.5-72B
model achieving 94.55% accuracy while consuming only 74.3-78.4% of tokens
required by Qwen3-235B and 83.0% of DeepSeek-V3's usage--delivering responses
twice as fast as Qwen3-235B. This efficiency establishes TopoMAS as an
accelerator for computation-driven discovery pipelines. By harmonizing rational
agent orchestration with a self-evolving knowledge graph, our framework not
only delivers immediate advances in topological materials but also establishes
a transferable, extensible paradigm for materials-science domain....

---

### 2. Kinetic Langevin Diffusion for Crystalline Materials Generation

**Authors:** François Cornet, Federico Bergamin, Arghya Bhowmik, Juan Maria Garcia Lastra, Jes Frellsen, Mikkel N. Schmidt

**Published:** 2025-07-04

**Category:** cs.LG

**ID:** 2507.03602v1

**Link:** [http://arxiv.org/abs/2507.03602v1](http://arxiv.org/abs/2507.03602v1)

**Summary:** Generative modeling of crystalline materials using diffusion models presents
a series of challenges: the data distribution is characterized by inherent
symmetries and involves multiple modalities, with some defined on specific
manifolds. Notably, the treatment of fractional coordinates representing atomic
positions in the unit cell requires careful consideration, as they lie on a
hypertorus. In this work, we introduce Kinetic Langevin Diffusion for Materials
(KLDM), a novel diffusion model for crystalline materials generation, where the
key innovation resides in the modeling of the coordinates. Instead of resorting
to Riemannian diffusion on the hypertorus directly, we generalize Trivialized
Diffusion Model (TDM) to account for the symmetries inherent to crystals. By
coupling coordinates with auxiliary Euclidean variables representing
velocities, the diffusion process is now offset to a flat space. This allows us
to effectively perform diffusion on the hypertorus while providing a training
objective that accounts for the periodic translation symmetry of the true data
distribution. We evaluate KLDM on both Crystal Structure Prediction (CSP) and
De-novo Generation (DNG) tasks, demonstrating its competitive performance with
current state-of-the-art models....

---


<!-- ARXIV_PAPERS_END -->