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

## New Papers (4)

*Last updated: 2026-04-15 06:42:43 (SGT)*

### 1. deCIFer: Crystal Structure Prediction from Powder Diffraction Data using Autoregressive Language Models

**Authors:** Frederik Lizak Johansen, Ulrik Friis-Jensen, Erik Bjørnager Dam, Kirsten Marie Ørnsbjerg Jensen, Rocío Mercado, Raghavendra Selvan

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.02189v4

**Link:** [http://arxiv.org/abs/2502.02189v4](http://arxiv.org/abs/2502.02189v4)

**Summary:** Novel materials drive advancements in fields ranging from energy storage to electronics, with crystal structure characterization forming a crucial yet challenging step in materials discovery. In this work, we introduce \emph{deCIFer}, an autoregressive language model designed for powder X-ray diffraction (PXRD)-conditioned crystal structure prediction (PXRD-CSP). Unlike traditional CSP methods that rely primarily on composition or symmetry constraints, deCIFer explicitly incorporates PXRD data, directly generating crystal structures in the widely adopted Crystallographic Information File (CIF) format. The model is trained on nearly 2.3 million crystal structures, with PXRD conditioning augmented by basic forms of synthetic experimental artifacts, specifically Gaussian noise and instrumental peak broadening, to reflect fundamental real-world conditions. Validated across diverse synthetic datasets representative of challenging inorganic materials, deCIFer achieves a 94\% structural match rate. The evaluation is based on metrics such as the residual weighted profile ($R_{wp}$) and structural match rate (MR), chosen explicitly for their practical relevance in this inherently underdetermined problem. deCIFer establishes a robust baseline for future expansion toward more complex experimental scenarios, bridging the gap between computational predictions and experimental crystal structure determination....

---

### 2. AutoMS: Multi-Agent Evolutionary Search for Cross-Physics Inverse Microstructure Design

**Authors:** Zhenyuan Zhao, Yu Xing, Tianyang Xue, Lingxin Cao, Xin Yan, Lin Lu

**Published:** 2026-03-28

**Category:** cs.AI

**ID:** 2603.27195v2

**Link:** [http://arxiv.org/abs/2603.27195v2](http://arxiv.org/abs/2603.27195v2)

**Summary:** Designing microstructures with coupled cross-physics objectives is a fundamental challenge where traditional topology optimization is often computationally prohibitive and deep generative models frequently suffer from physical hallucinations. We introduce AutoMS, a multi-agent neuro-symbolic framework that reformulates inverse design as an LLM-driven evolutionary search. AutoMS leverages LLMs as semantic navigators to decompose complex requirements and coordinate agent workflows, while a novel Simulation-Aware Evolutionary Search (SAES) mechanism handles low-level numerical optimization via local gradient approximation and directed parameter updates. This architecture achieves a state-of-the-art 83.8% success rate on 17 diverse cross-physics tasks, significantly outperforming both traditional evolutionary algorithms and existing agentic baselines. By decoupling open-ended semantic orchestration from simulation-grounded numerical search, AutoMS provides a robust pathway for navigating complex physical landscapes that remain intractable for standard generative or purely linguistic approaches....

---

### 3. PyAPX: Python toolkit for atomic configuration pattern exploration

**Authors:** Akira Kusaba, Tetsuji Kuboyama, Karol Kawka, Pawel Kempisty, Yoshihiro Kangawa

**Published:** 2025-11-22

**Category:** cond-mat.mtrl-sci

**ID:** 2511.17972v2

**Link:** [http://arxiv.org/abs/2511.17972v2](http://arxiv.org/abs/2511.17972v2)

**Summary:** In materials discovery, the integration of first-principles calculations with machine learning techniques has been actively studied for two key tasks: crystal structure prediction, which searches for stable structures given a chemical composition, and elemental substitution, which explores chemical compositions that yield desirable properties in a given crystal structure. However, even when both the crystal structure and chemical composition are fixed, material properties can still vary depending on the atomic arrangements (configurations) at crystallographic sites. To support detailed material design, we present PyAPX, a Python toolkit that performs Bayesian searches of stable atomic configurations. A distinctive feature of this initial release is the introduction of encoding methods suitable for configuration search, and we evaluate their performance using the h-BCN system. As a result, they were confirmed to yield superior convergence compared to commonly used one-hot encoding. PyAPX is broadly applicable to crystalline materials and is expected to further advance materials discovery....

---

### 4. Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery

**Authors:** Yiwen Wang, Gregory Sinenka, Xhuliano Brace

**Published:** 2026-04-08

**Category:** cs.AI

**ID:** 2604.07512v2

**Link:** [http://arxiv.org/abs/2604.07512v2](http://arxiv.org/abs/2604.07512v2)

**Summary:** We present Rhizome OS-1, a semi-autonomous operating system for small molecule drug discovery in which multi-modal AI agents operate as a full multidisciplinary discovery team. These agents function as computational chemists, medicinal chemists, and patent agents: they write and execute analysis code (fingerprint clustering, R-group decomposition, substructure search), visually triage molecular grids using vision capabilities, formulate explicit medicinal chemistry hypotheses across three strategy tiers, assess patent freedom-to-operate, and dynamically adapt generation strategies based on empirical screening feedback. Powered by r1 - a 246M-parameter graph diffusion model trained on 800 million molecular graphs - the system generates novel chemical matter directly on molecular graphs using fragment masking, scaffold decoration, linker design, and graph editing primitives. In two oncology campaigns (BCL6 BTB domain and EZH2 SET domain), the agent team executed 26 seeds and produced 5,231 novel molecules. Across both targets, 91.9% of generated Murcko scaffolds are absent from ChEMBL, with median Tanimoto similarity of 0.56-0.69 to the nearest known active. Boltz-2 binding affinity predictions, calibrated against ChEMBL data, achieved Spearman correlations of -0.53 to -0.64 and ROC AUC values of 0.88-0.93. These results demonstrate that semi-autonomous agent systems, equipped with graph-native generative tools and physics-informed scoring, enable a new paradigm for early-stage drug discovery: scaled, rapid, and adaptive inverse design with embedded medicinal chemistry reasoning....

---


<!-- ARXIV_PAPERS_END -->