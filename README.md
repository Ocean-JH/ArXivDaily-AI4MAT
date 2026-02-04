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

## New Papers (3)

*Last updated: 2026-02-05 06:26:18 (SGT)*

### 1. Optimization and Generation in Aerodynamics Inverse Design

**Authors:** Huaguan Chen, Ning Lin, Luxi Chen, Rui Zhang, Wenbing Huang, Chongxuan Li, Hao Sun

**Published:** 2026-02-03

**Category:** cs.LG

**ID:** 2602.03582v1

**Link:** [http://arxiv.org/abs/2602.03582v1](http://arxiv.org/abs/2602.03582v1)

**Summary:** Inverse design with physics-based objectives is challenging because it couples high-dimensional geometry with expensive simulations, as exemplified by aerodynamic shape optimization for drag reduction. We revisit inverse design through two canonical solutions, the optimal design point and the optimal design distribution, and relate them to optimization and guided generation. Building on this view, we propose a new training loss for cost predictors and a density-gradient optimization method that improves objectives while preserving plausible shapes. We further unify existing training-free guided generation methods. To address their inability to approximate conditional covariance in high dimensions, we develop a time- and memory-efficient algorithm for approximate covariance estimation. Experiments on a controlled 2D study and high-fidelity 3D aerodynamic benchmarks (car and aircraft), validated by OpenFOAM simulations and miniature wind-tunnel tests with 3D-printed prototypes, demonstrate consistent gains in both optimization and guided generation. Additional offline RL results further support the generality of our approach....

---

### 2. Accelerating Complex Materials Discovery with Universal Machine-Learning Potential-Driven Structure Prediction

**Authors:** Yuqi An, Zhenbin Wang

**Published:** 2026-02-03

**Category:** cond-mat.mtrl-sci

**ID:** 2602.03369v1

**Link:** [http://arxiv.org/abs/2602.03369v1](http://arxiv.org/abs/2602.03369v1)

**Summary:** Universal machine-learning interatomic potentials (uMLIPs) have become powerful tools for accelerating computational materials discovery by replacing expensive first-principles calculations in crystal structure prediction (CSP). However, their effectiveness in identifying new, complex materials remains uncertain. Here, we systematically assess the capability of a uMLIP (i.e.,M3GNet) to accelerate CSP in quaternary oxides. Through extensive exploration of the Sr-Li-Al-O and Ba-Y-Al-O systems, we show that uMLIP can rediscover experimentally known materials absent from its training set and identify seven new thermodynamically and dynamically stable compounds. These include a new polymorph of Sr2LiAlO4 (P3221) and a new disordered phase, Sr2Li4Al2O7 (P1_bar). Furthermore, our results show stability predictions based on the semilocal PBE functional require cross-validation with higher-level methods, such as SCAN and RPA, to ensure reliability. While uMLIPs substantially reduce the computational cost of CSP, the primary bottleneck has shifted to the efficiency of search algorithms in navigating complex structural spaces. This work highlights both the promise and current limitations of uMLIP-driven CSP in the discovery of new materials....

---

### 3. Learning ORDER-Aware Multimodal Representations for Composite Materials Design

**Authors:** Xinyao Li, Hangwei Qian, Jingjing Li, Ivor Tsang

**Published:** 2026-01-23

**Category:** cs.LG

**ID:** 2602.02513v1

**Link:** [http://arxiv.org/abs/2602.02513v1](http://arxiv.org/abs/2602.02513v1)

**Summary:** Artificial intelligence (AI) has shown remarkable success in materials discovery and property prediction, particularly for crystalline and polymer systems where material properties and structures are dominated by discrete graph representations. Such graph-central paradigm breaks down on composite materials, which possess continuous and nonlinear design spaces that lack well-defined graph structures. General composite descriptors, e.g., fiber volume and misalignment angle, cannot fully capture the fiber distributions that fundamentally determine microstructural characteristics, necessitating the integration of heterogeneous data sources through multimodal learning. Existing alignment-oriented multimodal frameworks have proven effective on abundant crystal or polymer data under discrete, unique graph-property mapping assumptions, but fail to address the highly continuous composite design space under extreme data scarcity. In this work, we introduce ORDinal-aware imagE-tabulaR alignment (ORDER), a multimodal pretraining framework that establishes ordinality as a core principle for composite material representations. ORDER ensures that materials with similar target properties occupy nearby regions in the latent space, which effectively preserves the continuous nature of composite properties and enables meaningful interpolation between sparsely observed designs. We evaluate ORDER on a public Nanofiber-enforced composite dataset and an internally curated dataset that simulates the construction of carbon fiber T700 with diverse fiber distributions. ORDER achieves consistent improvements over state-of-the-art multimodal baselines across property prediction, cross-modal retrieval, and microstructure generation tasks....

---


<!-- ARXIV_PAPERS_END -->