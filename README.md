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

*Last updated: 2026-04-01 06:33:13 (SGT)*

### 1. Electrospinning-Data.org: A FAIR, Structured Knowledge Resource for Nanofiber Fabrication

**Authors:** Mehrab Mahdian, Ferenc Ender, Tamas Pardy

**Published:** 2026-03-29

**Category:** cs.DB

**ID:** 2603.27841v1

**Link:** [http://arxiv.org/abs/2603.27841v1](http://arxiv.org/abs/2603.27841v1)

**Summary:** Electrospinning is a versatile nanofabrication technique whose outcomes emerge from a complex, high-dimensional interplay between solution properties, processing parameters, and environmental conditions. Optimizing this parameter space for targeted fiber morphology is inherently challenging, often driving extensive trial-and-error experimentation and generating vast experimental data across laboratories worldwide. Yet this knowledge remains fragmented and underutilized due to inconsistent reporting and a pervasive bias toward successful outcomes, limiting reproducibility and hindering data-driven research. Here we introduce Electrospinning-Data.org, a FAIR-aligned data aggregation infrastructure that organizes dispersed electrospinning experiments into structured, reusable, and failure-aware scientific records. The platform is built around a unified process-structure-property data model linking experimental inputs, environmental conditions, and nanofiber morphology, annotated through a controlled vocabulary, within a consistent, machine-readable schema. A two-stage moderation pipeline combining automated validation with expert review supports data quality and long-term interoperability. The resulting structured, failure-inclusive corpus provides a framework for data-driven research, including predictive modelling, inverse design of target morphologies, and systematic mapping of instability regimes that would otherwise require extensive trial-and-error experimentation....

---

### 2. Offline Materials Optimization with CliqueFlowmer

**Authors:** Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine, Pieter Abbeel

**Published:** 2026-03-06

**Category:** cs.AI

**ID:** 2603.06082v3

**Link:** [http://arxiv.org/abs/2603.06082v3](http://arxiv.org/abs/2603.06082v3)

**Summary:** Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable its use in specialized materials discovery problems and support interdisciplinary research, we open-source our code and provide additional project information at https://github.com/znowu/CliqueFlowmer....

---

### 3. AutoMS: Multi-Agent Evolutionary Search for Cross-Physics Inverse Microstructure Design

**Authors:** Zhenyuan Zhao, Yu Xing, Tianyang Xue, Lingxin Cao, Xin Yan, Lin Lu

**Published:** 2026-03-28

**Category:** cs.AI

**ID:** 2603.27195v1

**Link:** [http://arxiv.org/abs/2603.27195v1](http://arxiv.org/abs/2603.27195v1)

**Summary:** Designing microstructures that satisfy coupled cross-physics objectives is a fundamental challenge in material science. This inverse design problem involves a vast, discontinuous search space where traditional topology optimization is computationally prohibitive, and deep generative models often suffer from "physical hallucinations," lacking the capability to ensure rigorous validity. To address this limitation, we introduce AutoMS, a multi-agent neuro-symbolic framework that reformulates inverse design as an LLM-driven evolutionary search. Unlike methods that treat LLMs merely as interfaces, AutoMS integrates them as "semantic navigators" to initialize search spaces and break local optima, while our novel Simulation-Aware Evolutionary Search (SAES) addresses the "blindness" of traditional evolutionary strategies. Specifically, SAES utilizes simulation feedback to perform local gradient approximation and directed parameter updates, effectively guiding the search toward physically valid Pareto frontiers. Orchestrating specialized agents (Manager, Parser, Generator, and Simulator), AutoMS achieves a state-of-the-art 83.8\% success rate on 17 diverse cross-physics tasks, nearly doubling the performance of traditional NSGA-II (43.7\%) and significantly outperforming ReAct-based LLM baselines (53.3\%). Furthermore, our hierarchical architecture reduces total execution time by 23.3\%. AutoMS demonstrates that autonomous agent systems can effectively navigate complex physical landscapes, bridging the gap between semantic design intent and rigorous physical validity....

---

### 4. Property-Guided Molecular Generation and Optimization via Latent Flows

**Authors:** Alexander Arjun Lobo, Urvi Awasthi, Leonid Zhukov

**Published:** 2026-03-27

**Category:** cs.LG

**ID:** 2603.26889v1

**Link:** [http://arxiv.org/abs/2603.26889v1](http://arxiv.org/abs/2603.26889v1)

**Summary:** Molecular discovery is increasingly framed as an inverse design problem: identifying molecular structures that satisfy desired property profiles under feasibility constraints. While recent generative models provide continuous latent representations of chemical space, targeted optimization within these representations often leads to degraded validity, loss of structural fidelity, or unstable behavior. We introduce MoltenFlow, a modular framework that combines property-organized latent representations with flow-matching generative priors and gradient-based guidance. This formulation supports both conditioned generation and local optimization within a single latent-space framework. We show that guided latent flows enable efficient multi-objective molecular optimization under fixed oracle budgets with controllable trade-offs, while a learned flow prior improves unconditional generation quality....

---


<!-- ARXIV_PAPERS_END -->