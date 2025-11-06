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

## New Papers (8)

*Last updated: 2025-11-07 06:17:03 (SGT)*

### 1. Are diffusion models ready for materials discovery in unexplored chemical space?

**Authors:** Sanghyun Kim, Gihyeon Jeon, Seungwoo Hwang, Jiho Lee, Jisu Jung, Seungwu Han, Sungwoo Kang

**Published:** 2025-10-10

**Category:** cond-mat.mtrl-sci

**ID:** 2510.09406v2

**Link:** [http://arxiv.org/abs/2510.09406v2](http://arxiv.org/abs/2510.09406v2)

**Summary:** While diffusion models are attracting increasing attention for the design of
novel materials, their ability to generate low-energy structures in unexplored
chemical spaces has not been systematically assessed. Here, we evaluate the
performance of two diffusion models, MatterGen and DiffCSP, against three
databases: a ternary oxide set (constructed by a genetic algorithm), a ternary
nitride set (constructed by template informatics), and the GNoME database
(constructed by a combination of both). We find that diffusion models generally
perform stably in well-sampled chemical spaces (oxides and nitrides), but are
less effective in uncommon ones (GNoME), which contains many compositions
involving rare-earth elements and unconventional stoichiometry. Finally, we
assess their size-extrapolation capability and observe a significant drop in
performance when the number of atoms exceeds the trained range. This is
attributed to the limitations imposed by periodic boundary conditions, which we
refer to as the curse of periodicity. This study paves the way for future
developments in materials design by highlighting both the strength and the
limitations of diffusion models....

---

### 2. EGMOF: Efficient Generation of Metal-Organic Frameworks Using a Hybrid Diffusion-Transformer Architecture

**Authors:** Seunghee Han, Yeonghun Kang, Taeun Bae, Varinia Bernales, Alan Aspuru-Guzik, Jihan Kim

**Published:** 2025-11-05

**Category:** cond-mat.mtrl-sci

**ID:** 2511.03122v1

**Link:** [http://arxiv.org/abs/2511.03122v1](http://arxiv.org/abs/2511.03122v1)

**Summary:** Designing materials with targeted properties remains challenging due to the
vastness of chemical space and the scarcity of property-labeled data. While
recent advances in generative models offer a promising way for inverse design,
most approaches require large datasets and must be retrained for every new
target property. Here, we introduce the EGMOF (Efficient Generation of MOFs), a
hybrid diffusion-transformer framework that overcomes these limitations through
a modular, descriptor-mediated workflow. EGMOF decomposes inverse design into
two steps: (1) a one-dimensional diffusion model (Prop2Desc) that maps desired
properties to chemically meaningful descriptors followed by (2) a transformer
model (Desc2MOF) that generates structures from these descriptors. This modular
hybrid design enables minimal retraining and maintains high accuracy even under
small-data conditions. On a hydrogen uptake dataset, EGMOF achieved over 95%
validity and 84% hit rate, representing significant improvements of up to 57%
in validity and 14% in hit rate compared to existing methods, while remaining
effective with only 1,000 training samples. Moreover, our model successfully
performed conditional generation across 29 diverse property datasets, including
CoREMOF, QMOF, and text-mined experimental datasets, whereas previous models
have not. This work presents a data-efficient, generalizable approach to the
inverse design of diverse MOFs and highlights the potential of modular inverse
design workflows for broader materials discovery....

---

### 3. A Normalized Descriptor for Unbiased Screening of Second-Order Nonlinear Optical Materials

**Authors:** Aubrey G. J. Nyiri, Michael J. Waters, James M. Rondinelli

**Published:** 2025-11-04

**Category:** cond-mat.mtrl-sci

**ID:** 2511.03038v1

**Link:** [http://arxiv.org/abs/2511.03038v1](http://arxiv.org/abs/2511.03038v1)

**Summary:** Second-order nonlinear optical materials enable frequency doubling of light
(second-harmonic generation, SHG), which is essential for optoelectronic
applications ranging from materials characterization to quantum technologies.
However, comparing SHG performance across materials remains challenging as the
second-order nonlinear susceptibility $\chi^{(2)}$ spans several orders of
magnitude and strongly depends on the band gap $E_g$. To address this, we
empirically validate a theoretical upper bound on $\chi^{(2)}$ using new
databases of \textit{ab initio}-computed nonlinear optical (NLO) properties. We
then formulate a normalized descriptor, $\hat{d}$, which expresses the NLO
response of a material relative to the band gap-dependent physical limit. We
show that $\hat{d}$ exhibits a similar distribution across a wide range of band
gap energies. This universality supports the use of $\hat{d}$ as a robust,
generalizable descriptor for data-driven and chemistry-informed machine
learning models of NLO response, enabling accelerated materials discovery and
optimization across broad application frequencies....

---

### 4. A Synthesizability-Guided Pipeline for Materials Discovery

**Authors:** Thorben Prein, Willis O'Leary, Aikaterini Flessa Savvidou, Elchaïma Bourneix, Joonatan E. M. Laulainen

**Published:** 2025-11-03

**Category:** cs.CE

**ID:** 2511.01790v1

**Link:** [http://arxiv.org/abs/2511.01790v1](http://arxiv.org/abs/2511.01790v1)

**Summary:** Computational materials discovery relies on the generation of plausible
crystal structures. The plausibility is typically judged through density
functional theory methods which, while typically accurate at zero Kelvin, often
favor low-energy structures that are not experimentally accessible. We develop
a combined compositional and structural synthesizability score which provides
an accurate way of predicting which compounds can actually be synthesized in a
laboratory. We use it to evaluate non-synthesized structures from the Materials
Project, GNoME, and Alexandria, and identified several hundred highly
synthesizable candidates. We then predict synthesis pathways, conduct
corresponding experiments, and characterize the products across 16 targets,
successfully synthesizing 7 of 16. The entire experimental process was
completed in only three days. Our results highlight omissions in lists of known
synthesized structures, deliver insights into the practical utility of current
materials databases, and showcase the central role synthesizability prediction
can play in materials discovery....

---

### 5. AI-Guided Molecular Simulations in VR: Exploring Strategies for Imitation Learning in Hyperdimensional Molecular Systems

**Authors:** Mohamed Dhouioui, Jonathan Barnoud, Rhoslyn Roebuck Williams, Harry J. Stroud, Phil Bates, David R. Glowacki

**Published:** 2024-09-11

**Category:** cs.LG

**ID:** 2409.07189v2

**Link:** [http://arxiv.org/abs/2409.07189v2](http://arxiv.org/abs/2409.07189v2)

**Summary:** Molecular dynamics (MD) simulations are a crucial computational tool for
researchers to understand and engineer molecular structure and function in
areas such as drug discovery, protein engineering, and material design. Despite
their utility, MD simulations are expensive, owing to the high dimensionality
of molecular systems. Interactive molecular dynamics in virtual reality
(iMD-VR) has recently emerged as a "human-in-the-loop" strategy for efficiently
navigating hyper-dimensional molecular systems. By providing an immersive 3D
environment that enables visualization and manipulation of real-time molecular
simulations running on high-performance computing architectures, iMD-VR enables
researchers to reach out and guide molecular conformational dynamics, in order
to efficiently explore complex, high-dimensional molecular systems. Moreover,
iMD-VR simulations generate rich datasets that capture human experts' spatial
insight regarding molecular structure and function. This paper explores the use
of researcher-generated iMD-VR datasets to train AI agents via imitation
learning (IL). IL enables agents to mimic complex behaviours from expert
demonstrations, circumventing the need for explicit programming or intricate
reward design. In this article, we review IL across robotics and Multi-agents
systems domains which are comparable to iMD-VR, and discuss how iMD-VR
recordings could be used to train IL models to interact with MD simulations. We
then illustrate the applications of these ideas through a proof-of-principle
study where iMD-VR data was used to train a CNN network on a simple molecular
manipulation task; namely, threading a small molecule through a nanotube pore.
Finally, we outline future research directions and potential challenges of
using AI agents to augment human expertise in navigating vast molecular
conformational spaces....

---

### 6. MaterialsGalaxy: A Platform Fusing Experimental and Theoretical Data in Condensed Matter Physics

**Authors:** Tiannian Zhu, Zhong Fang, Quansheng Wu, Hongming Weng

**Published:** 2025-10-30

**Category:** cond-mat.mtrl-sci

**ID:** 2510.26886v1

**Link:** [http://arxiv.org/abs/2510.26886v1](http://arxiv.org/abs/2510.26886v1)

**Summary:** Modern materials science generates vast and diverse datasets from both
experiments and computations, yet these multi-source, heterogeneous data often
remain disconnected in isolated "silos". Here, we introduce MaterialsGalaxy, a
comprehensive platform that deeply fuses experimental and theoretical data in
condensed matter physics. Its core innovation is a structure similarity-driven
data fusion mechanism that quantitatively links cross-modal records - spanning
diffraction, crystal growth, computations, and literature - based on their
underlying atomic structures. The platform integrates artificial intelligence
(AI) tools, including large language models (LLMs) for knowledge extraction,
generative models for crystal structure prediction, and machine learning
property predictors, to enhance data interpretation and accelerate materials
discovery. We demonstrate that MaterialsGalaxy effectively integrates these
disparate data sources, uncovering hidden correlations and guiding the design
of novel materials. By bridging the long-standing gap between experiment and
theory, MaterialsGalaxy provides a new paradigm for data-driven materials
research and accelerates the discovery of advanced materials....

---

### 7. Higher-dimensional Fermiology in bulk moiré metals

**Authors:** Kevin P. Nuckolls, Nisarga Paul, Alan Chen, Filippo Gaggioli, Joshua P. Wakefield, Avi Auslender, Jules Gardener, Austin J. Akey, David Graf, Takehito Suzuki, David C. Bell, Liang Fu, Joseph G. Checkelsky

**Published:** 2025-10-30

**Category:** cond-mat.mtrl-sci

**ID:** 2510.26880v1

**Link:** [http://arxiv.org/abs/2510.26880v1](http://arxiv.org/abs/2510.26880v1)

**Summary:** In the past decade, moir\'e materials have revolutionized how we engineer and
control quantum phases of matter. Among incommensurate materials, moir\'e
materials are aperiodic composite crystals whose long-wavelength moir\'e
superlattices enable tunable properties without chemically modifying their
layers. To date, nearly all reports of moir\'e materials have investigated van
der Waals heterostructures assembled far from thermodynamic equilibrium. Here
we introduce a conceptually new approach to synthesizing high-mobility moir\'e
materials in thermodynamic equilibrium. We report a new family of foliated
superlattice materials (Sr$_6$TaS$_8$)$_{1+\delta}$(TaS$_2$)$_8$ that are
exfoliatable van der Waals crystals with atomically incommensurate lattices.
Lattice mismatches between alternating layers generate moir\'e superlattices,
analogous to those of 2D moir\'e heterobilayers, that are coherent throughout
these crystals and are tunable through their synthesis conditions without
altering their chemical composition. High-field quantum oscillation
measurements map the complex Fermiology of these moir\'e metals, which can be
tuned via the moir\'e superlattice structure. We find that the Fermi surface of
the structurally simplest moir\'e metal is comprised of over 40 distinct
cross-sectional areas, the most observed in any material to our knowledge. This
can be naturally understood by postulating that bulk moir\'e materials can
encode electronic properties of higher-dimensional superspace crystals in ways
that parallel well-established crystallographic methods used for incommensurate
lattices. More broadly, our work demonstrates a scalable synthesis approach
potentially capable of producing moir\'e materials for electronics applications
and evidences a novel material design concept for accessing a broad range of
physical phenomena proposed in higher dimensions....

---

### 8. Benchmarking Generative AI Against Bayesian Optimization for Constrained Multi-Objective Inverse Design

**Authors:** Muhammad Bilal Awan, Abdul Razzaq, Abdul Shahid

**Published:** 2025-10-29

**Category:** cs.LG

**ID:** 2511.00070v1

**Link:** [http://arxiv.org/abs/2511.00070v1](http://arxiv.org/abs/2511.00070v1)

**Summary:** This paper investigates the performance of Large Language Models (LLMs) as
generative optimizers for solving constrained multi-objective regression tasks,
specifically within the challenging domain of inverse design
(property-to-structure mapping). This problem, critical to materials
informatics, demands finding complex, feasible input vectors that lie on the
Pareto optimal front. While LLMs have demonstrated universal effectiveness
across generative and reasoning tasks, their utility in constrained,
continuous, high-dimensional numerical spaces tasks they weren't explicitly
architected for remains an open research question. We conducted a rigorous
comparative study between established Bayesian Optimization (BO) frameworks and
a suite of fine-tuned LLMs and BERT models. For BO, we benchmarked the
foundational BoTorch Ax implementation against the state-of-the-art q-Expected
Hypervolume Improvement (qEHVI, BoTorchM). The generative approach involved
fine-tuning models via Parameter-Efficient Fine-Tuning (PEFT), framing the
challenge as a regression problem with a custom output head. Our results show
that BoTorch qEHVI achieved perfect convergence (GD=0.0), setting the
performance ceiling. Crucially, the best-performing LLM (WizardMath-7B)
achieved a Generational Distance (GD) of 1.21, significantly outperforming the
traditional BoTorch Ax baseline (GD=15.03). We conclude that specialized BO
frameworks remain the performance leader for guaranteed convergence, but
fine-tuned LLMs are validated as a promising, computationally fast alternative,
contributing essential comparative metrics to the field of AI-driven
optimization. The findings have direct industrial applications in optimizing
formulation design for resins, polymers, and paints, where multi-objective
trade-offs between mechanical, rheological, and chemical properties are
critical to innovation and production efficiency....

---


<!-- ARXIV_PAPERS_END -->