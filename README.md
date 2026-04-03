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

*Last updated: 2026-04-04 06:31:19 (SGT)*

### 1. Loop-level surrogate modeling of dopant-distribution effects in Ba(Zr,Ti)O$_3$

**Authors:** Heiko Röthl, Elke Kraker, Julien Magnien, Manfred Mücke, Florian Mayer

**Published:** 2026-04-02

**Category:** cond-mat.mtrl-sci

**ID:** 2604.02325v1

**Link:** [http://arxiv.org/abs/2604.02325v1](http://arxiv.org/abs/2604.02325v1)

**Summary:** Barium titanate-based perovskites are important candidates for lead-free dielectric and electromechanical technologies. In Zr-substituted BaTiO$_3$ (BZT), functional behavior is usually discussed in terms of the average Zr concentration, while the influence of dopant spatial distribution beyond average concentration is less understood and difficult to explore systematically. Here we present an accelerated materials-design workflow that links controlled dopant distributions to full field-driven response curves. We generate a broad set of Zr distributions spanning a continuum of nanoscale arrangements, with layers, rods, dots, and lamellae serving as representative end-member motifs, and encode each configuration using a compact, parametrized descriptor model. Effective-Hamiltonian molecular dynamics is used to compute polarization-electric-field and strain-field hysteresis loops, and we train a conditional autoencoder surrogate to predict complete loops directly from the distribution parameters. This surrogate enables rapid screening and dense, property-selective design maps at scales that are not feasible with direct simulations alone, and it supports targeted follow-up simulations in regions of interest. Using the predicted loop database, we screen the distribution space for multiple functional targets, including energy-storage performance, electromechanical response, and switching behavior, and identify the corresponding dopant distribution motif families. The resulting design maps show that dopant distribution is an independent tuning parameter that can strongly affect hysteresis behavior and loop-derived figures of merit: layer-like motifs, vertical lamellae, and nanoplate-like inclusions emerge in different performance regimes. More generally, predicting full response curves enables screening of other loop-derived targets and multi-objective design in substituted ferroelectrics....

---

### 2. AlloyVAE: A generative model for complex probabilistic field-to-field relationships in alloys

**Authors:** Ningyu Yan, Zhuocheng Xie, Kai Guo, Yejun Gu, Huajian Gao, Yang Xiang

**Published:** 2026-04-02

**Category:** cond-mat.mtrl-sci

**ID:** 2604.02281v1

**Link:** [http://arxiv.org/abs/2604.02281v1](http://arxiv.org/abs/2604.02281v1)

**Summary:** The inherent compositional heterogeneity of multi-principal element alloys (MPEAs) gives rise to complex, spatially varying mechanical fields that cannot be uniquely determined from coarse-grained composition descriptors. This non-uniqueness introduces intrinsically probabilistic structure-property relationships, posing a fundamental challenge to conventional deterministic modeling and machine learning approaches that collapse such mappings into average predictions. Here, we present AlloyVAE, a physics-informed generative framework that learns the full conditional distribution of mechanical fields from microstructural inputs. Built upon a conditional variational autoencoder architecture, the model incorporates learned smoothing operators to enhance functional regularity and a self-consistency mechanism to enforce physical plausibility. Trained on atomistic simulation data, AlloyVAE accurately predicts distributions of residual stress fields from composition and short-range order, and enables the generation of multiple physically consistent realizations under identical input conditions. Beyond forward prediction, the framework supports inverse design by optimizing composition fields to achieve targeted mechanical responses, and is extensible to coupled mappings involving eigenstrain. By capturing one-to-many structure-property relationships in heterogeneous materials, this work establishes a probabilistic paradigm for materials modeling and design, providing a scalable alternative to conventional simulations for navigating high-dimensional compositional spaces....

---


<!-- ARXIV_PAPERS_END -->