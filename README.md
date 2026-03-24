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

## New Papers (6)

*Last updated: 2026-03-25 06:28:45 (SGT)*

### 1. Exploring self-driving labs for optoelectronic materials

**Authors:** Jonathan Staaf Scragg

**Published:** 2026-03-23

**Category:** cond-mat.mtrl-sci

**ID:** 2603.21704v1

**Link:** [http://arxiv.org/abs/2603.21704v1](http://arxiv.org/abs/2603.21704v1)

**Summary:** Self-driving laboratories (SDLs), by combining automation with machine learning-guided experiment selection, have the potential to transform experimental materials science. To date, most SDLs have been optimisation-driven, designed to rapidly converge on performance metrics, by embedding multiple mechanistic layers within platform-specific surrogate models. Such approaches excel at process tuning yet offer limited insight into the underlying physics governing synthesis-property relationships. Here we articulate a complementary paradigm: the exploration-driven, or scientific, SDL, whose primary purpose is the generation of data for data-driven science. We exemplify this concept for the case of inorganic optoelectronic materials, arguing that defect physics, which forms the central mechanistic link between synthesis conditions and functional properties, provides the foundation for designing a suitable SDL. Because defect populations and their spatial organisation cannot generally be resolved directly - nor fully predicted from first principles - the task of the SDL is to generate datasets in which thermodynamic and kinetic synthesis variables are systematically perturbed and defect-sensitive observables measured in parallel. From this basis, we propose a set of design principles for scientific SDLs that will enable them to operate close to the physics of optoelectronic materials, thereby generating transferrable and reusable datasets offering radical insight. We use Cu2ZnSn(S,Se)4 as a case study, both to show the scale of the task of defect-aware materials exploration as well to highlight as the deficiencies in the current paradigm. We propose that properly designed SDLs can generate the structured datasets necessary to enable mechanistic inference and advance synthesis-aware materials design....

---

### 2. Inverse design of heterodeformations for strain soliton networks in bilayer 2D materials

**Authors:** Md Tusher Ahmed, Nikhil Chandra Admal

**Published:** 2026-03-22

**Category:** cond-mat.mtrl-sci

**ID:** 2603.21446v1

**Link:** [http://arxiv.org/abs/2603.21446v1](http://arxiv.org/abs/2603.21446v1)

**Summary:** Strain soliton networks strongly influence the structural and electronic properties of heterodeformed bilayer systems, yet their design remains challenging due to the high dimensionality of heterodeformation space and the absence of a direct map between deformation and network geometry. In this work, we introduce a geometric framework that establishes a one-to-one mapping between heterodeformations and the geometry of the strain soliton network expressed as line vector-Burgers vector pairs. The admissible networks are constrained by topology dictated by the generalized stacking fault energy landscape. We show that the moiré Bravais lattice, corresponding to a uniform heterodeformation, alone is insufficient to characterize the interface: distinct heterodeformations can share identical moiré Bravais lattices while producing different soliton networks, reflecting an inherent many-to-one mapping when only translational symmetry is considered. In contrast, the soliton network encodes the full multilattice geometry of the interface, including topology and connectivity, which are not captured by the moiré Bravais lattice alone. The proposed framework enables the direct construction of heterodeformations from target networks, providing a systematic route for inverse design of moiré interfaces beyond conventional twist-based approaches....

---

### 3. AutoMOOSE: An Agentic AI for Autonomous Phase-Field Simulation

**Authors:** Sukriti Manna, Henry Chan, Subramanian K. R. S. Sankaranarayanan

**Published:** 2026-03-22

**Category:** cs.AI

**ID:** 2603.20986v1

**Link:** [http://arxiv.org/abs/2603.20986v1](http://arxiv.org/abs/2603.20986v1)

**Summary:** Multiphysics simulation frameworks such as MOOSE provide rigorous engines for phase-field materials modeling, yet adoption is constrained by the expertise required to construct valid input files, coordinate parameter sweeps, diagnose failures, and extract quantitative results. We introduce AutoMOOSE, an open-source agentic framework that orchestrates the full simulation lifecycle from a single natural-language prompt. AutoMOOSE deploys a five-agent pipeline in which the Input Writer coordinates six sub-agents and the Reviewer autonomously corrects runtime failures without user intervention. A modular plugin architecture enables new phase-field formulations without modifying the core framework, and a Model Context Protocol (MCP) server exposes the workflow as ten structured tools for interoperability with any MCP-compatible client. Validated on a four-temperature copper grain growth benchmark, AutoMOOSE generates MOOSE input files with 6 of 12 structural blocks matching a human expert reference exactly and 4 functionally equivalent, executes all runs in parallel with a 1.8x speedup, and performs an end-to-end physical consistency check spanning intent, finite-element execution, and Arrhenius kinetics with no human verification. Grain coarsening kinetics are recovered with R^2 = 0.90-0.95 at T >= 600 K; the recovered activation energy Q_fit = 0.296 eV is consistent with a human-written reference (Q_fit = 0.267 eV) under identical parameters. Three runtime failure classes were diagnosed and resolved autonomously within a single correction cycle, and every run produces a provenance record satisfying FAIR data principles. These results show that the gap between knowing the physics and executing a validated simulation campaign can be bridged by a lightweight multi-agent orchestration layer, providing a pathway toward AI-driven materials discovery and self-driving laboratories....

---

### 4. Physics Enhanced Deep Surrogates for the Phonon Boltzmann Transport Equation

**Authors:** Antonio Varagnolo, Giuseppe Romano, Raphaël Pestourie

**Published:** 2025-11-25

**Category:** physics.comp-ph

**ID:** 2512.05976v2

**Link:** [http://arxiv.org/abs/2512.05976v2](http://arxiv.org/abs/2512.05976v2)

**Summary:** Designing materials with controlled heat flow at the nano-scale is central to advances in microelectronics, thermoelectrics, and energy-conversion technologies. At these scales, phonon transport follows the Boltzmann Transport Equation (BTE), which captures non-diffusive (ballistic) effects but is too costly to solve repeatedly in inverse-design loops. Existing surrogate approaches trade speed for accuracy: fast macroscopic solvers can overestimate conductivities by hundreds of percent, while recent data-driven operator learners often require thousands of high-fidelity simulations. This creates a need for a fast, data-efficient surrogate that remains reliable across ballistic and diffusive regimes. We introduce a Physics-Enhanced Deep Surrogate (PEDS) that combines a differentiable Fourier solver with a neural generator and couples it with uncertainty-driven active learning. The Fourier solver acts as a physical inductive bias, while the network learns geometry-dependent corrections and a mixing coefficient that interpolates between macroscopic and nano-scale behavior. PEDS reduces training-data requirements by up to 70% compared with purely data-driven baselines, achieves roughly 5% fractional error with only 300 high-fidelity BTE simulations, and enables efficient design of porous geometries spanning 12-85 W m$^{-1}$ K$^{-1}$ with average design errors of 4%. The learned mixing parameter recovers the ballistic-diffusive transition and improves out of distribution robustness. These results show that embedding simple, differentiable low-fidelity physics can dramatically increase surrogate data-efficiency and interpretability, making repeated PDE-constrained optimization practical for nano-scale thermal-materials design....

---

### 5. Active learning for photonic crystals

**Authors:** Ryan Lopez, Charlotte Loh, Rumen Dangovski, Marin Soljačić

**Published:** 2026-01-22

**Category:** physics.optics

**ID:** 2601.16287v2

**Link:** [http://arxiv.org/abs/2601.16287v2](http://arxiv.org/abs/2601.16287v2)

**Summary:** Active learning for photonic crystals explores the integration of analytic approximate Bayesian last layer neural networks (LL-BNNs) with uncertainty-driven sample selection to accelerate photonic band gap prediction. We employ an analytic LL-BNN formulation, corresponding to the infinite Monte Carlo sample limit, to obtain uncertainty estimates that are strongly correlated with the true predictive error on unlabeled candidate structures. These uncertainty scores drive an active learning strategy that prioritizes the most informative simulations during training. Applied to the task of predicting band gap sizes in two-dimensional, two-tone photonic crystals, our approach achieves up to a 2.6x reduction in required training data compared to a random sampling baseline while maintaining predictive accuracy. The efficiency gains arise from concentrating computational resources on high uncertainty regions of the design space rather than sampling uniformly. Given the substantial cost of full band structure simulations, especially in three dimensions, this data efficiency enables rapid and scalable surrogate modeling. Our results suggest that analytic LL-BNN based active learning can substantially accelerate topological optimization and inverse design workflows for photonic crystals, and more broadly, offers a general framework for data efficient regression across scientific machine learning domains....

---

### 6. A chemical language model for reticular materials design

**Authors:** Dhruv Menon, Vivek Singh, Xu Chen, Mohammad Reza Alizadeh Kiapi, Ivan Zyuzin, Hamish W. Macleod, Nakul Rampal, William Shepard, Omar M. Yaghi, David Fairen-Jimenez

**Published:** 2026-03-20

**Category:** cond-mat.mtrl-sci

**ID:** 2603.20389v1

**Link:** [http://arxiv.org/abs/2603.20389v1](http://arxiv.org/abs/2603.20389v1)

**Summary:** Reticular chemistry has enabled the synthesis of tens of thousands of metal-organic frameworks (MOFs), yet the discovery of new materials still relies largely on intuition-driven linker design and iterative experimentation. As a result, researchers explore only a small fraction of the vast chemical space accessible to reticular materials, limiting the systematic discovery of frameworks with targeted properties. Here, we introduce Nexerra-R1, a building-block chemical language model that enables inverse design in reticular chemistry through the targeted generation of organic linkers. Rather than generating complete frameworks directly, Nexerra-R1 operates at the level of molecular building blocks, preserving the modular logic that underpins reticular synthesis. The model supports both unconstrained generation of low-connectivity linkers and scaffold-constrained design of symmetric multidentate motifs compatible with predefined nodes and topologies. We further combine linker generation with flow-guided distributional targeting to steer the generative process toward application-relevant objectives while maintaining chemical validity and assembly feasibility. The generated linkers are subsequently assembled into three-dimensional frameworks and are structurally optimized to produce candidate materials compatible with experimental synthesis. Using Nexerra-R1, we validate this strategy by rediscovering known MOFs and by proposing the experimental synthesis of a previously unreported framework, CU-525, generated entirely in silico. Together, these results establish a general inverse-design paradigm for reticular materials in which controllable chemical language modelling enables the direct translation from computational design to synthesizable frameworks....

---


<!-- ARXIV_PAPERS_END -->