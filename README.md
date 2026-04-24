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

## New Papers (9)

*Last updated: 2026-04-25 06:37:01 (SGT)*

### 1. GFlowState: Visualizing the Training of Generative Flow Networks Beyond the Reward

**Authors:** Florian Holeczek, Andreas Hinterreiter, Alex Hernandez-Garcia, Marc Streit, Christina Humer

**Published:** 2026-04-23

**Category:** cs.LG

**ID:** 2604.21830v1

**Link:** [http://arxiv.org/abs/2604.21830v1](http://arxiv.org/abs/2604.21830v1)

**Summary:** We present GFlowState, a visual analytics system designed to illuminate the training process of Generative Flow Networks (GFlowNets or GFNs). GFlowNets are a probabilistic framework for generating samples proportionally to a reward function. While GFlowNets have proved to be powerful tools in applications such as molecule and material discovery, their training dynamics remain difficult to interpret. Standard machine learning tools allow metric tracking but do not reveal how models explore the sample space, construct sample trajectories, or shift sampling probabilities during training. Our solution, GFlowState, allows users to analyze sampling trajectories, compare the sample space relative to reference datasets, and analyze the training dynamics. To this end, we introduce multiple views, including a chart of candidate rankings, a state projection, a node-link diagram of the trajectory network, and a transition heatmap. These visualizations enable GFlowNet developers and users to investigate sampling behavior and policy evolution, and to identify underexplored regions and sources of training failure. Case studies demonstrate how the system supports debugging and assessing the quality of GFlowNets across application domains. By making the structural dynamics of GFlowNets observable, our work enhances their interpretability and can accelerate GFlowNet development in practice....

---

### 2. Algebraic Language Models for Inverse Design of Metamaterials via Diffusion Transformers

**Authors:** Li Zheng, Siddhant Kumar, Dennis M. Kochmann

**Published:** 2025-07-21

**Category:** cs.CE

**ID:** 2507.15753v2

**Link:** [http://arxiv.org/abs/2507.15753v2](http://arxiv.org/abs/2507.15753v2)

**Summary:** Generative machine learning models have revolutionized material discovery by capturing complex structure-property relationships, yet extending these approaches to the inverse design of three-dimensional metamaterials remains limited by computational complexity and underexplored design spaces due to the lack of expressive representations. Here we present DiffuMeta, a generative framework integrating diffusion transformers with an algebraic language representation, encoding three-dimensional geometries as mathematical sentences. This compact, unified parameterization spans diverse topologies, enabling the direct application of transformers to structural design. DiffuMeta leverages diffusion models to generate new shell structures with precisely targeted stress-strain responses under large deformations, accounting for buckling and contact while addressing the inherent one-to-many mapping by producing diverse solutions. Uniquely, our approach enables simultaneous control over multiple mechanical objectives, including linear and nonlinear responses beyond training domains. Experimental validation of fabricated structures further confirms the efficacy of our approach for accelerated design of metamaterials and structures with tailored properties....

---

### 3. Accurate predictive model of band gap with selected important features based on explainable machine learning

**Authors:** Joohwi Lee, Kaito Miyamoto

**Published:** 2025-03-06

**Category:** cond-mat.mtrl-sci

**ID:** 2503.04492v3

**Link:** [http://arxiv.org/abs/2503.04492v3](http://arxiv.org/abs/2503.04492v3)

**Summary:** In the rapidly advancing field of materials informatics, nonlinear machine learning models have demonstrated exceptional predictive capabilities for material properties. However, their black-box nature limits interpretability, and they may incorporate features that do not contribute to -- or even deteriorate -- model performance. This study employs explainable ML (XML) techniques, including permutation feature importance and the SHapley Additive exPlanation, applied to a pristine support vector regression model designed to predict band gaps at the GW level using 18 input features. Guided by XML-derived individual feature importance, a simple framework is proposed to construct reduced-feature predictive models. Model evaluations indicate that an XML-guided compact model, consisting of the top five features, achieves comparable accuracy to the pristine model on in-domain datasets (0.254 vs. 0.247 eV) while showing improved generalization with lower prediction errors on out-of-domain data (0.348 vs. 0.460 eV). Additionally, the study underscores the necessity for eliminating strongly correlated features (correlation coefficient greater than 0.8) to prevent misinterpretation and overestimation of feature importance before applying XML. This study highlights XML's effectiveness in developing simplified yet highly accurate machine learning models by clarifying feature roles, thereby reducing computational costs for feature acquisition and enhancing model trustworthiness for materials discovery....

---

### 4. GEWUM: General Exploration Workflow for the Utopia of Materials: A Unified Platform for Automated Structure Generation, Selection, and Validation

**Authors:** Jiexi Song, Aixian She, Changpeng Song, Diwei Shi, Fengyuan Xuan, Chongde Cao

**Published:** 2026-04-23

**Category:** cond-mat.mtrl-sci

**ID:** 2604.21401v1

**Link:** [http://arxiv.org/abs/2604.21401v1](http://arxiv.org/abs/2604.21401v1)

**Summary:** The discovery of materials with tailored properties is increasingly reliant on computational methods. However, the fragmented landscape of existing software often hinders the seamless integration of large-scale structure prediction with rigorous stability validation, particularly in high-performance computing (HPC) environments. To address this gap, we present GEWUM (General Exploration Workflow for the Utopia of Materials), a unified, open-source platform designed to automate and accelerate materials discovery. GEWUM integrates the Selective Random Structure Search (SRSS) strategy with universal Machine Learning Interatomic Potentials (uMLIPs), enabling efficient exploration of vast chemical spaces. Its core architecture features a modular design with native support for SLURM-based HPC clusters. The platform unifies the entire workflow, from random structure generation and diversity-preserving selection to thermodynamic and dynamic stability assessments, as well as advanced property calculations (e.g., elastic constants, thermal conductivity, and quasi-harmonic approximations). We demonstrate GEWUM's capabilities through three distinct case studies: (1) the prediction of low-energy polymorphs in the complex Al-Sc-N nitride system; (2) the identification of a P-62c phase of U3Si5, distinct from the known AlB2 type; and (3) the high-pressure structure prediction of ThH10 at 150 GPa. Furthermore, benchmark tests show reasonable agreement in predicting thermophysical properties. By bridging the gap between uMLIPs and automated high-throughput workflows, GEWUM serves as a valuable framework to facilitate efficient and scalable materials exploration....

---

### 5. Navigating Order-(Dis)Order Family Trees via Group-Subgroup Transitions

**Authors:** Shuya Yamazaki, Yuyao Huang, Martin Hoffmann Petersen, Wei Nong, Kedar Hippalgaonkar

**Published:** 2026-04-23

**Category:** cond-mat.mtrl-sci

**ID:** 2604.21386v1

**Link:** [http://arxiv.org/abs/2604.21386v1](http://arxiv.org/abs/2604.21386v1)

**Summary:** As closed-loop materials discovery systems scale to produce millions of candidate compounds, the credibility of the novelty they reward becomes a critical concern. Novelty is commonly assessed against databases of ordered crystal structures, in which atomic sites are fully occupied. Yet, a predicted ordered structure may simply correspond to a particular ordering of a known disordered phase, whose sites are occupied by multiple species in the statistical average structure; we refer to such a structure as an ordered child of a disordered parent. Here, we introduce order-(dis)order family trees, a symmetry-based framework that organizes ordered and disordered structures through group-subgroup relations and enables novelty to be explicitly evaluated. We develop a high-throughput family matching procedure, to identify possible disordered parents and symmetry-related ordered relatives for a given ordered structure. As validation, we test our framework on synthesis-facing case studies (A-Lab), where it correctly recovers existing disordered parents for the targeted ordered structures. Extending this family-tree-based benchmark to experimental structure databases (ICSD), computational datasets (MP-20, Alex-MP-20, and GNoME), and crystal generative models further reveals that many ordered structures that appear novel as individual entries are, in fact, better understood as members of experimentally known order-(dis)order family trees. We also show that this is particularly evident in symmetry-agnostic all-atom generative models, which more frequently produce ordered structures derived from known disordered parents, whereas symmetry-constrained models are 2-4x less prone to this behavior. Our results establish order-(dis)order family trees as a key requirement for achieving genuine novelty in data-driven materials discovery....

---

### 6. Analytic Inverse Design of Temporal Metamaterials via Space-Time Duality

**Authors:** Giuseppe Castaldi, Marino Coppolaro, Massimo Moccia, Carlo Rizza, Nader Engheta, Vincenzo Galdi

**Published:** 2026-04-23

**Category:** physics.optics

**ID:** 2604.21383v1

**Link:** [http://arxiv.org/abs/2604.21383v1](http://arxiv.org/abs/2604.21383v1)

**Summary:** Temporal metamaterials, created by modulating the refractive index in time, offer powerful means of controlling wave propagation but still lack a systematic design methodology. Here, we develop an analytic inverse-design framework rooted in space-time duality and the established theory of one-dimensional spatial inverse scattering. By prescribing reflection (backward-wave) and transmission (forward-wave) responses in rational-function form, we obtain closed-form refractive-index modulations that are guaranteed to be physically admissible. This approach avoids iterative optimization and provides direct analytic control of the modulation. We illustrate the method with syntheses of mathematical operators, such as derivatives and integrals, as well as Chebyshev- and Butterworth-type filters, and validate the results through finite-difference time-domain simulations. Our findings establish a general route to temporal media with tailored functional and spectral responses, enabling applications in wave-based information processing, programmable filtering, and amplification schemes inspired by photonic time crystals....

---

### 7. Generative Discovery of Magnetic Insulators under Competing Physical Constraints

**Authors:** Qiulin Zeng, Tahiya Chowdhury, Md Shafayat Hossain

**Published:** 2026-04-22

**Category:** cond-mat.mtrl-sci

**ID:** 2604.21073v1

**Link:** [http://arxiv.org/abs/2604.21073v1](http://arxiv.org/abs/2604.21073v1)

**Summary:** Discovering materials that must simultaneously satisfy multiple competing constraints remains a central challenge in computational materials design, particularly in data-scarce regimes where conventional data-driven approaches are least effective. Magnetic insulators represent a stringent example: the electronic conditions that favor magnetic order often also promote metallicity, while insulating behavior suppresses the interactions that stabilize magnetism. As a result, experimentally viable magnetic insulators are rare and difficult to identify through conventional screening. Here, we introduce MagMatLLM, a constraint-guided generative discovery framework that integrates language-model-based crystal generation with evolutionary selection, surrogate screening, and first-principles validation to target simultaneous stability, magnetism, and insulating behavior. Unlike stability-first approaches, the framework enforces functional constraints during generation and selection, steering the search toward sparsely populated regions of materials space defined by competing physical requirements. Using this workflow, we identify twelve previously unreported candidate magnetic insulators, including Tm$_4$Co$_2$Cr$_2$O$_{12}$ and Cr$_4$Nb$_2$O$_{12}$. Of these, ten are dynamically stable by phonon analysis and exhibit finite band gaps and nonzero magnetic moments in spin-polarized density functional theory calculations. Beyond the specific compounds identified here, this work establishes a general constraint-guided paradigm for multi-objective materials discovery in sparse chemical spaces and provides a transferable strategy for the design of quantum materials under competing physical constraints....

---

### 8. Expanding the extreme-k dielectric materials space through physics-validated generative reasoning

**Authors:** Hossain Hridoy, Tahiya Chowdhury, Md Shafayat Hossain

**Published:** 2026-04-22

**Category:** cond-mat.mtrl-sci

**ID:** 2604.21068v1

**Link:** [http://arxiv.org/abs/2604.21068v1](http://arxiv.org/abs/2604.21068v1)

**Summary:** The most technologically consequential materials are often the rarest: they occupy narrow regions of chemical space, obey competing physical constraints, and appear only sparsely in existing databases. High-kappa dielectrics, high-Tc superconductors, and ferromagnetic insulators are to name a few. This scarcity fundamentally limits today's data-driven materials discovery, where machine-learning models excel at interpolation but struggle to generate genuinely new candidates. Here, we introduce DielecMIND, an artificial intelligence framework that reframes materials discovery as a reasoning-driven exploration instead of a database-screening problem. Using high-kappa dielectrics as a data-scarce and technologically stringent test case, DielecMIND combines large-language-model hypothesis generation for the first time with physics validated first-principles calculation to navigate chemical space beyond known compounds. Prior to our work, only 14 experimentally or computationally validated materials with kappa > 150 were known. Our framework discovers and validates 5 new such compounds, expanding this rare-materials class by a remarkable = 35% in a single study. Among them, we find that Ba2TiHfO6 exhibits a dielectric constant of 637, minimal loss at low optical frequencies, and stability up to 800 K. Beyond dielectrics, this work demonstrates a new paradigm for artificial-intelligence-guided discovery: one that generates a small number of physically grounded, experimentally plausible candidates yet measurably expands sparsely populated functional materials spaces. Thus, DielecMIND points toward a general strategy for discovering rare, high-impact functional materials where data scarcity has long constrained progress....

---

### 9. Symmetry Classification of Magnetic Orders using Oriented Spin Space Groups

**Authors:** Yuntian Liu, Xiaobing Chen, Yutong Yu, Jesús Etxebarria, J. Manuel Perez-Mato, Qihang Liu

**Published:** 2025-06-25

**Category:** cond-mat.mtrl-sci

**ID:** 2506.20739v3

**Link:** [http://arxiv.org/abs/2506.20739v3](http://arxiv.org/abs/2506.20739v3)

**Summary:** Magnetism has witnessed remarkable progress in recent decades, largely driven by its potential for next-generation storage devices. However, the classification of magnetic orders, even for fundamental concepts such as ferromagnetism and antiferromagnetism, remains a topic of active evolution, particularly with the discovery of unconventional magnetic materials and advances in antiferromagnetic spintronics. Here, we present a unified classification of magnetic order utilizing the state-of-the-art spin space group (SSG) theory. Based on whether the net spin magnetization is constrained to zero by SSG, we systematically categorize magnetic orders into ferromagnetism (including ferrimagnetism) and antiferromagnetism. We further introduce an oriented SSG description, i.e., an SSG with a fixed magnetic orientation, thereby unifying the SSG and magnetic space group frameworks. This approach clearly reveals the symmetry-breaking pathway induced by spin-orbit coupling. The proposed group framework completes the intrinsic logic of magnetic symmetry and identifies a distinct magnetic phase, termed spin-orbit magnetism, in which the net spin magnetization is induced by spin-orbit coupling. Our work provides a comprehensive symmetry-based perspective for classifying magnetic order, offering fresh insights into unconventional magnets and broad applicability in spintronics and quantum material design....

---


<!-- ARXIV_PAPERS_END -->