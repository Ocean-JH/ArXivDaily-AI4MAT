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

*Last updated: 2026-04-08 06:36:31 (SGT)*

### 1. Generative AI for material design: A mechanics perspective from burgers to matter

**Authors:** Vahidullah Tac, Ellen Kuhl

**Published:** 2026-04-03

**Category:** cs.CE

**ID:** 2604.03409v1

**Link:** [http://arxiv.org/abs/2604.03409v1](http://arxiv.org/abs/2604.03409v1)

**Summary:** Generative artificial intelligence offers a new paradigm to design matter in high-dimensional spaces. However, its underlying mechanisms remain difficult to interpret and limit adoption in computational mechanics. This gap is striking because its core tools-diffusion, stochastic differential equations, and inverse problems-are fundamental to the mechanics of materials. Here we show that diffusion-based generative AI and computational mechanics are rooted in the same principles. We illustrate this connection using a three-ingredient burger as a minimal benchmark for material design in a low-dimensional space, where both forward and reverse diffusion admit analytical solutions: Markov chains with Bayesian inversion in the discrete case and the Ornstein-Uhlenbeck process with score-based reversal in the continuous case. We extend this framework to a high-dimensional design space with 146 ingredients and 8.9x10^43 possible configurations, where analytical solutions become intractable. We therefore learn the discrete and continuous reverse processes using neural network models that infer inverse dynamics from data. We train the models on only 2,260 recipes and generate one million samples that capture the statistical structure of the data, including ingredient prevalence and quantitative composition. We further generate five new burgers and validate them in a restaurant-based sensory study with 100 participants, where three of the AI-designed burgers outperform the classical Big Mac in overall liking, flavor, and texture. These results establish diffusion-based generative modeling as a physically grounded approach to design in high-dimensional spaces. They position generative AI as a natural extension of computational mechanics, with applications from burgers to matter, and establish a path toward data-driven, physics-informed generative design....

---

### 2. Generative Chemical Language Models for Energetic Materials Discovery

**Authors:** Andrew Salij, R. Seaton Ullberg, Megan C. Davis, Marc J. Cawkwell, Christopher J. Snyder, Cristina Garcia Cardona, Ivana Matanovic, Wilton J. M. Kort-Kamp

**Published:** 2026-03-30

**Category:** physics.chem-ph

**ID:** 2604.03304v1

**Link:** [http://arxiv.org/abs/2604.03304v1](http://arxiv.org/abs/2604.03304v1)

**Summary:** The discovery of new energetic materials remains a pressing challenge hindered by limited availability of high-quality data. To address this, we have developed generative molecular language models that have been pretrained on extensive chemical data and then fine-tuned with curated energetic materials datasets. This transfer-learning strategy extends the chemical language model capabilities beyond the pharmacological space in which they have been predominantly developed, offering a framework applicable to other data-spare discovery problems. Furthermore, we discuss the benefits of fragment-based molecular encodings for chemical language models, in particular in constructing synthetically accessible structures. Together, these advances provide a foundation for accelerating the design of next-generation energetic materials with demanding performance requirements....

---

### 3. Scaling atom-by-atom inverse design with nano-topology optimization and diffusion models

**Authors:** Chun-Teh Chen, Denvid Lau

**Published:** 2026-03-24

**Category:** physics.app-ph

**ID:** 2604.03276v1

**Link:** [http://arxiv.org/abs/2604.03276v1](http://arxiv.org/abs/2604.03276v1)

**Summary:** The mechanical properties of metallic nanostructures are governed not only by topology but also by crystal symmetry and face-specific surface physics, which are typically absent from continuum topology optimization. We develop an atom-by-atom inverse design framework that combines Nano-Topology Optimization (Nano-TO) with conditional denoising diffusion probabilistic models. Nano-TO treats each atom as a discrete design variable and evaluates stiffness from the symmetric curvature of the total energy, removing residual surface-stress bias. A crystallography-aligned multi-shell sensitivity filter stabilizes the optimization and enables designs containing more than 6.5 x 10^5 atoms. Using aluminum nanocantilevers, we identify a surface-physics-driven topology selection rule: thickness-periodic beams favor brace-dominated trusses, whereas finite-thickness beams favor nearly closed walls that provide efficient shear paths and reduce surface penalties. At sufficiently small scales, these walls become mechanically unstable, and truss-like layouts reappear. In nanopillar studies, atomistic optimization outperforms continuum topology-optimized designs. Finally, conditional diffusion models trained on Nano-TO data generate diverse high-performance candidates near the optimization frontier. These results establish nanoscale inverse design as a coupled problem of topology and surface physics....

---


<!-- ARXIV_PAPERS_END -->