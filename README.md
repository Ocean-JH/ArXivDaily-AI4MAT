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

*Last updated: 2026-02-18 06:29:22 (SGT)*

### 1. GenPANIS: A Latent-Variable Generative Framework for Forward and Inverse PDE Problems in Multiphase Media

**Authors:** Matthaios Chatzopoulos, Phaedon-Stelios Koutsourelakis

**Published:** 2026-02-16

**Category:** stat.ML

**ID:** 2602.14642v1

**Link:** [http://arxiv.org/abs/2602.14642v1](http://arxiv.org/abs/2602.14642v1)

**Summary:** Inverse problems and inverse design in multiphase media, i.e., recovering or engineering microstructures to achieve target macroscopic responses, require operating on discrete-valued material fields, rendering the problem non-differentiable and incompatible with gradient-based methods. Existing approaches either relax to continuous approximations, compromising physical fidelity, or employ separate heavyweight models for forward and inverse tasks. We propose GenPANIS, a unified generative framework that preserves exact discrete microstructures while enabling gradient-based inference through continuous latent embeddings. The model learns a joint distribution over microstructures and PDE solutions, supporting bidirectional inference (forward prediction and inverse recovery) within a single architecture. The generative formulation enables training with unlabeled data, physics residuals, and minimal labeled pairs. A physics-aware decoder incorporating a differentiable coarse-grained PDE solver preserves governing equation structure, enabling extrapolation to varying boundary conditions and microstructural statistics. A learnable normalizing flow prior captures complex posterior structure for inverse problems. Demonstrated on Darcy flow and Helmholtz equations, GenPANIS maintains accuracy on challenging extrapolative scenarios - including unseen boundary conditions, volume fractions, and microstructural morphologies, with sparse, noisy observations. It outperforms state-of-the-art methods while using 10 - 100 times fewer parameters and providing principled uncertainty quantification....

---

### 2. PeroMAS: A Multi-agent System of Perovskite Material Discovery

**Authors:** Yishu Wang, Wei Liu, Yifan Li, Shengxiang Xu, Xujie Yuan, Ran Li, Yuyu Luo, Jia Zhu, Shimin Di, Min-Ling Zhang, Guixiang Li

**Published:** 2026-02-10

**Category:** cs.MA

**ID:** 2602.13312v1

**Link:** [http://arxiv.org/abs/2602.13312v1](http://arxiv.org/abs/2602.13312v1)

**Summary:** As a pioneer of the third-generation photovoltaic revolution, Perovskite Solar Cells (PSCs) are renowned for their superior optoelectronic performance and cost potential. The development process of PSCs is precise and complex, involving a series of closed-loop workflows such as literature retrieval, data integration, experimental design, and synthesis. However, existing AI perovskite approaches focus predominantly on discrete models, including material design, process optimization,and property prediction. These models fail to propagate physical constraints across the workflow, hindering end-to-end optimization. In this paper, we propose a multi-agent system for perovskite material discovery, named PeroMAS. We first encapsulated a series of perovskite-specific tools into Model Context Protocols (MCPs). By planning and invoking these tools, PeroMAS can design perovskite materials under multi-objective constraints, covering the entire process from literature retrieval and data extraction to property prediction and mechanism analysis. Furthermore, we construct an evaluation benchmark by perovskite human experts to assess this multi-agent system. Results demonstrate that, compared to single Large Language Model (LLM) or traditional search strategies, our system significantly enhances discovery efficiency. It successfully identified candidate materials satisfying multi-objective constraints. Notably, we verify PeroMAS's effectiveness in the physical world through real synthesis experiments....

---

### 3. Judging the Judges: Human Validation of Multi-LLM Evaluation for High-Quality K--12 Science Instructional Materials

**Authors:** Peng He, Zhaohui Li, Zeyuan Wang, Jinjun Xiong, Tingting Li

**Published:** 2026-01-31

**Category:** cs.CY

**ID:** 2602.13243v1

**Link:** [http://arxiv.org/abs/2602.13243v1](http://arxiv.org/abs/2602.13243v1)

**Summary:** Designing high-quality, standards-aligned instructional materials for K--12 science is time-consuming and expertise-intensive. This study examines what human experts notice when reviewing AI-generated evaluations of such materials, aiming to translate their insights into design principles for a future GenAI-based instructional material design agent. We intentionally selected 12 high-quality curriculum units across life, physical, and earth sciences from validated programs such as OpenSciEd and Multiple Literacies in Project-based Learning. Using the EQuIP rubric with 9 evaluation items, we prompted GPT-4o, Claude, and Gemini to produce numerical ratings and written rationales for each unit, generating 648 evaluation outputs. Two science education experts independently reviewed all outputs, marking agreement (1) or disagreement (0) for both scores and rationales, and offering qualitative reflections on AI reasoning. This process surfaces patterns in where LLM judgments align with or diverge from expert perspectives, revealing reasoning strengths, gaps, and contextual nuances. These insights will directly inform the development of a domain-specific GenAI agent to support the design of high-quality instructional materials in K--12 science education....

---


<!-- ARXIV_PAPERS_END -->