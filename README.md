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

*Last updated: 2026-02-11 06:37:52 (SGT)*

### 1. Refining the Information Bottleneck via Adversarial Information Separation

**Authors:** Shuai Ning, Zhenpeng Wang, Lin Wang, Bing Chen, Shuangrong Liu, Xu Wu, Jin Zhou, Bo Yang

**Published:** 2026-02-06

**Category:** cs.LG

**ID:** 2602.06549v2

**Link:** [http://arxiv.org/abs/2602.06549v2](http://arxiv.org/abs/2602.06549v2)

**Summary:** Generalizing from limited data is particularly critical for models in domains such as material science, where task-relevant features in experimental datasets are often heavily confounded by measurement noise and experimental artifacts. Standard regularization techniques fail to precisely separate meaningful features from noise, while existing adversarial adaptation methods are limited by their reliance on explicit separation labels. To address this challenge, we propose the Adversarial Information Separation Framework (AdverISF), which isolates task-relevant features from noise without requiring explicit supervision. AdverISF introduces a self-supervised adversarial mechanism to enforce statistical independence between task-relevant features and noise representations. It further employs a multi-layer separation architecture that progressively recycles noise information across feature hierarchies to recover features inadvertently discarded as noise, thereby enabling finer-grained feature extraction. Extensive experiments demonstrate that AdverISF outperforms state-of-the-art methods in data-scarce scenarios. In addition, evaluations on real-world material design tasks show that it achieves superior generalization performance....

---

### 2. Sequential versus Manifold Bayesian Optimization under Realistic Experimental Time Constraints

**Authors:** Boris Slautin, Sergei Kalinin

**Published:** 2026-02-08

**Category:** cond-mat.mtrl-sci

**ID:** 2602.07753v1

**Link:** [http://arxiv.org/abs/2602.07753v1](http://arxiv.org/abs/2602.07753v1)

**Summary:** Bayesian optimization (BO) is widely used for autonomous materials discovery, yet its classical sequential formulation is insufficient for design of experimental workflows that often combine parallel or batch synthesis with inherently serial characterization. Methods such as combinatorial spread libraries and printed libraries sample a defined low-D manifold in the chemical space of the system. Here, we introduce a time-aware framework for comparing sequential and manifold BO under experimentally realistic constraints. By explicitly modeling synthesis and characterization times, we define an effective experimental time metric that enables fair, time-normalized benchmarking of optimization strategies. Using numerical experiments in ternary and quaternary compositional spaces, we show that sequential BO remains optimal for short-term experiments or when batching provides no effective time advantage, whereas manifold BO becomes favorable once multiplexed synthesis enables faster accumulation of measurements. We identify a small set of physically interpretable parameters that govern the transition between these regimes. These results establish a general, experimentally grounded framework for selecting optimization strategies in self-driving laboratories and autonomous materials discovery workflows. The accompanying analysis code is publicly available at https://github.com/Slautin/2025_GP_BO_Manifolds....

---

### 3. GraphAgents: Knowledge Graph-Guided Agentic AI for Cross-Domain Materials Design

**Authors:** Isabella A. Stewart, Tarjei Paule Hage, Yu-Chuan Hsu, Markus J. Buehler

**Published:** 2026-02-07

**Category:** cs.AI

**ID:** 2602.07491v1

**Link:** [http://arxiv.org/abs/2602.07491v1](http://arxiv.org/abs/2602.07491v1)

**Summary:** Large Language Models (LLMs) promise to accelerate discovery by reasoning across the expanding scientific landscape. Yet, the challenge is no longer access to information but connecting it in meaningful, domain-spanning ways. In materials science, where innovation demands integrating concepts from molecular chemistry to mechanical performance, this is especially acute. Neither humans nor single-agent LLMs can fully contend with this torrent of information, with the latter often prone to hallucinations. To address this bottleneck, we introduce a multi-agent framework guided by large-scale knowledge graphs to find sustainable substitutes for per- and polyfluoroalkyl substances (PFAS)-chemicals currently under intense regulatory scrutiny. Agents in the framework specialize in problem decomposition, evidence retrieval, design parameter extraction, and graph traversal, uncovering latent connections across distinct knowledge pockets to support hypothesis generation. Ablation studies show that the full multi-agent pipeline outperforms single-shot prompting, underscoring the value of distributed specialization and relational reasoning. We demonstrate that by tailoring graph traversal strategies, the system alternates between exploitative searches focusing on domain-critical outcomes and exploratory searches surfacing emergent cross-connections. Illustrated through the exemplar of biomedical tubing, the framework generates sustainable PFAS-free alternatives that balance tribological performance, thermal stability, chemical resistance, and biocompatibility. This work establishes a framework combining knowledge graphs with multi-agent reasoning to expand the materials design space, showcasing several initial design candidates to demonstrate the approach....

---


<!-- ARXIV_PAPERS_END -->