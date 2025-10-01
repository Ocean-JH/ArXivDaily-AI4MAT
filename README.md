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

*Last updated: 2025-10-02 06:15:40 (SGT)*

### 1. Fine-Tuning Bulk-oriented Universal Interatomic Potentials for Surfaces: Accuracy, Efficiency, and Forgetting Control

**Authors:** Jaekyun Hwang, Taehun Lee, Yonghyuk Lee, Su-Hyun Yoo

**Published:** 2025-09-30

**Category:** cond-mat.mtrl-sci

**ID:** 2509.25807v1

**Link:** [http://arxiv.org/abs/2509.25807v1](http://arxiv.org/abs/2509.25807v1)

**Summary:** Accurate prediction of surface energies and stabilities is essential for
materials design, yet first-principles calculations remain computationally
expensive and most existing interatomic potentials are trained only on bulk
systems. Here, we demonstrate that fine-tuning foundation machine learning
potentials (MLPs) significantly improves both computational efficiency and
predictive accuracy for surface modeling. While existing universal interatomic
potentials (UIPs) have been solely trained and validated on bulk datasets, we
extend their applicability to complex and scientifically significant unary,
binary, and ternary surface systems. We systematically compare models trained
from scratch, zero-shot inference, conventional fine-tuning, and multi-head
fine-tuning approach that enhances transferability and mitigates catastrophic
forgetting. Fine-tuning consistently reduces prediction errors with
orders-of-magnitude fewer training configurations, and multi-head fine-tuning
delivers robust and generalizable predictions even for materials beyond the
initial training domain. These findings offer practical guidance for leveraging
pre-trained MLPs to accelerate surface modeling and highlight a scalable path
toward data-efficient, next-generation atomic-scale simulations in
computational materials science....

---

### 2. Steering an Active Learning Workflow Towards Novel Materials Discovery via Queue Prioritization

**Authors:** Marcus Schwarting, Logan Ward, Nathaniel Hudson, Xiaoli Yan, Ben Blaiszik, Santanu Chaudhuri, Eliu Huerta, Ian Foster

**Published:** 2025-09-29

**Category:** cs.LG

**ID:** 2509.25538v1

**Link:** [http://arxiv.org/abs/2509.25538v1](http://arxiv.org/abs/2509.25538v1)

**Summary:** Generative AI poses both opportunities and risks for solving inverse design
problems in the sciences. Generative tools provide the ability to expand and
refine a search space autonomously, but do so at the cost of exploring
low-quality regions until sufficiently fine tuned. Here, we propose a queue
prioritization algorithm that combines generative modeling and active learning
in the context of a distributed workflow for exploring complex design spaces.
We find that incorporating an active learning model to prioritize top design
candidates can prevent a generative AI workflow from expending resources on
nonsensical candidates and halt potential generative model decay. For an
existing generative AI workflow for discovering novel molecular structure
candidates for carbon capture, our active learning approach significantly
increases the number of high-quality candidates identified by the generative
model. We find that, out of 1000 novel candidates, our workflow without active
learning can generate an average of 281 high-performing candidates, while our
proposed prioritization with active learning can generate an average 604
high-performing candidates....

---

### 3. Guided Diffusion for the Discovery of New Superconductors

**Authors:** Pawan Prakash, Jason B. Gibson, Zhongwei Li, Gabriele Di Gianluca, Juan Esquivel, Eric Fuemmeler, Benjamin Geisler, Jung Soo Kim, Adrian Roitberg, Ellad B. Tadmor, Mingjie Liu, Stefano Martiniani, Gregory R. Stewart, James J. Hamlin, Peter J. Hirschfeld, Richard G. Hennig

**Published:** 2025-09-29

**Category:** cond-mat.supr-con

**ID:** 2509.25186v1

**Link:** [http://arxiv.org/abs/2509.25186v1](http://arxiv.org/abs/2509.25186v1)

**Summary:** The inverse design of materials with specific desired properties, such as
high-temperature superconductivity, represents a formidable challenge in
materials science due to the vastness of chemical and structural space. We
present a guided diffusion framework to accelerate the discovery of novel
superconductors. A DiffCSP foundation model is pretrained on the Alexandria
Database and fine-tuned on 7,183 superconductors with first principles derived
labels. Employing classifier-free guidance, we sample 200,000 structures, which
lead to 34,027 unique candidates. A multistage screening process that combines
machine learning and density functional theory (DFT) calculations to assess
stability and electronic properties, identifies 773 candidates with
DFT-calculated $T_\mathrm{c}>5$ K. Notably, our generative model demonstrates
effective property-driven design. Our computational findings were validated
against experimental synthesis and characterization performed as part of this
work, which highlighted challenges in sparsely charted chemistries. This
end-to-end workflow accelerates superconductor discovery while underscoring the
challenge of predicting and synthesizing experimentally realizable materials....

---


<!-- ARXIV_PAPERS_END -->