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

*Last updated: 2025-10-18 06:15:49 (SGT)*

### 1. Learning Inter-Atomic Potentials without Explicit Equivariance

**Authors:** Ahmed A. Elhag, Arun Raja, Alex Morehead, Samuel M. Blau, Garrett M. Morris, Michael M. Bronstein

**Published:** 2025-09-25

**Category:** cs.LG

**ID:** 2510.00027v2

**Link:** [http://arxiv.org/abs/2510.00027v2](http://arxiv.org/abs/2510.00027v2)

**Summary:** Accurate and scalable machine-learned inter-atomic potentials (MLIPs) are
essential for molecular simulations ranging from drug discovery to new material
design. Current state-of-the-art models enforce roto-translational symmetries
through equivariant neural network architectures, a hard-wired inductive bias
that can often lead to reduced flexibility, computational efficiency, and
scalability. In this work, we introduce TransIP: Transformer-based Inter-Atomic
Potentials, a novel training paradigm for interatomic potentials achieving
symmetry compliance without explicit architectural constraints. Our approach
guides a generic non-equivariant Transformer-based model to learn
SO(3)-equivariance by optimizing its representations in the embedding space.
Trained on the recent Open Molecules (OMol25) collection, a large and diverse
molecular dataset built specifically for MLIPs and covering different types of
molecules (including small organics, biomolecular fragments, and
electrolyte-like species), TransIP effectively learns symmetry in its latent
space, providing low equivariance error. Further, compared to a data
augmentation baseline, TransIP achieves 40% to 60% improvement in performance
across varying OMol25 dataset sizes. More broadly, our work shows that learned
equivariance can be a powerful and efficient alternative to augmentation-based
MLIP models....

---

### 2. Strain-induced Moiré Reconstruction and Memorization in Two-Dimensional Materials without Twist

**Authors:** Nazmul Hasan, Tara Peña, Aditya Dey, Dongyoung Yoon, Zakaria Islam, Yue Zhang, Maria Vitoria Guimaraes Leal, Arend M. van der Zande, Hesam Askari, Stephen M. Wu

**Published:** 2025-10-15

**Category:** cond-mat.mtrl-sci

**ID:** 2510.13699v1

**Link:** [http://arxiv.org/abs/2510.13699v1](http://arxiv.org/abs/2510.13699v1)

**Summary:** Two-dimensional (2D) materials with a twist between layers exhibit a moir\'e
interference pattern with larger periodicity than any of the constituent layer
unit cells. In these systems, a wealth of exotic phases appear that result from
moir\'e-dependent many-body electron correlation effects or non-trivial band
topology. One problem with using twist to generate moir\'e interference has
been the difficulty in creating high-quality, uniform, and repeatable samples
due to fabrication through mechanical stacking with viscoelastic stamps. Here
we show, a new method to generate moir\'e interference through the controlled
application of layer-by-layer strain (heterostrain) on non-twisted 2D
materials, where moir\'e interference results from strain-induced lattice
mismatch without twisting or stacking. Heterostrain generation is achieved by
depositing stressed thin films onto 2D materials to apply large strains to the
top layers while leaving layers further down less strained. We achieve
deterministic control of moir\'e periodicity and symmetry in non-twisted 2D
multilayers and bilayers, with 97% yield, through varying stressor film force
(film thickness X film stress) and geometry. Moir\'e reconstruction effects are
memorized after the removal of the stressor layers. Control over the strain
degree-of-freedom opens the door to a completely unexplored set of unrealized
tunable moir\'e geometric symmetries, which may now be achieved in a high-yield
and user-skill independent process taking only hours. This technique solves a
long-standing throughput bottleneck in new moir\'e quantum materials discovery
and opens the door to industrially-compatible manufacturing for 2D
moir\'e-based electronic or optical devices....

---

### 3. Deep Generative Prior for First Order Inverse Optimization

**Authors:** Haoyu Yang, Kamyar Azizzadenesheli, Haoxing Ren

**Published:** 2025-04-28

**Category:** cs.AI

**ID:** 2504.20278v2

**Link:** [http://arxiv.org/abs/2504.20278v2](http://arxiv.org/abs/2504.20278v2)

**Summary:** Inverse design optimization aims to infer system parameters from observed
solutions, posing critical challenges across domains such as semiconductor
manufacturing, structural engineering, materials science, and fluid dynamics.
The lack of explicit mathematical representations in many systems complicates
this process and makes the first order optimization impossible. Mainstream
approaches, including generative AI and Bayesian optimization, address these
challenges but have limitations. Generative AI is computationally expensive,
while Bayesian optimization, relying on surrogate models, suffers from
scalability, sensitivity to priors, and noise issues, often leading to
suboptimal solutions. This paper introduces Deep Physics Prior (DPP), a novel
method enabling first-order gradient-based inverse optimization with surrogate
machine learning models. By leveraging pretrained auxiliary Neural Operators,
DPP enforces prior distribution constraints to ensure robust and meaningful
solutions. This approach is particularly effective when prior data and
observation distributions are unknown....

---


<!-- ARXIV_PAPERS_END -->