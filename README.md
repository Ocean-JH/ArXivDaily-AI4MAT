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

*Last updated: 2025-09-16 06:14:41 (SGT)*

### 1. OpenCSP: A Deep Learning Framework for Crystal Structure Prediction from Ambient to High Pressure

**Authors:** Yinan Wang, Xiaoyang Wang, Zhenyu Wang, Jing Wu, Jian Lv, Han Wang

**Published:** 2025-09-12

**Category:** cond-mat.mtrl-sci

**ID:** 2509.10293v1

**Link:** [http://arxiv.org/abs/2509.10293v1](http://arxiv.org/abs/2509.10293v1)

**Summary:** High-pressure crystal structure prediction (CSP) underpins advances in
condensed matter physics, planetary science, and materials discovery. Yet, most
large atomistic models are trained on near-ambient, equilibrium data, leading
to degraded stress accuracy at tens to hundreds of gigapascals and sparse
coverage of pressure-stabilized stoichiometries and dense coordination motifs.
Here, we introduce OpenCSP, a machine learning framework for CSP tasks spanning
ambient to high-pressure conditions. This framework comprises an open-source
pressure-resolved dataset alongside a suite of publicly available atomistic
models that are jointly optimized for accuracy in energy, force, and stress
predictions. The dataset is constructed via randomized high-pressure sampling
and iteratively refined through an uncertainty-guided concurrent learning
strategy, which enriches underrepresented compression regimes while suppressing
redundant DFT labeling. Despite employing a training corpus one to two orders
of magnitude smaller than those of leading large models, OpenCSP achieves
comparable or superior performance in high-pressure enthalpy ranking and
stability prediction. Across benchmark CSP tasks spanning a wide pressure
window, our models match or surpass MACE-MPA-0, MatterSim v1 5M, and
GRACE-2L-OAM, with the largest gains observed at elevated pressures. These
results demonstrate that targeted, pressure-aware data acquisition coupled with
scalable architectures enables data-efficient, high-fidelity CSP, paving the
way for autonomous materials discovery under ambient and extreme conditions....

---

### 2. Space Group Informed Transformer for Crystalline Materials Generation

**Authors:** Zhendong Cao, Xiaoshan Luo, Jian Lv, Lei Wang

**Published:** 2024-03-23

**Category:** cond-mat.mtrl-sci

**ID:** 2403.15734v3

**Link:** [http://arxiv.org/abs/2403.15734v3](http://arxiv.org/abs/2403.15734v3)

**Summary:** We introduce CrystalFormer, a transformer-based autoregressive model
specifically designed for space group-controlled generation of crystalline
materials. By explicitly incorporating space group symmetry, CrystalFormer
greatly reduces the effective complexity of crystal space, which is essential
for data-and compute-efficient generative modeling of crystalline materials.
Leveraging the prominent discrete and sequential nature of the Wyckoff
positions, CrystalFormer learns to generate crystals by directly predicting the
species and coordinates of symmetry-inequivalent atoms in the unit cell. We
demonstrate the advantages of CrystalFormer in standard tasks such as symmetric
structure initialization and element substitution over widely used conventional
approaches. Furthermore, we showcase its plug-and-play application to
property-guided materials design, highlighting its flexibility. Our analysis
reveals that CrystalFormer ingests sensible solid-state chemistry knowledge and
heuristics by compressing the material dataset, thus enabling systematic
exploration of crystalline materials space. The simplicity, generality, and
adaptability of CrystalFormer position it as a promising architecture to be the
foundational model of the entire crystalline materials space, heralding a new
era in materials discovery and design....

---

### 3. Unveiling the Role of Solvents in DBTTF:HATCN Ternary Cocrystals

**Authors:** Ana M. Valencia, Lisa Schraut-May, Marie Siegert, Sebastian Hammer, Beatrice Cula, Alexandra Friedrich, Holger Helten, Jens Pflaum, Caterina Cocchi, Andreas Opitz

**Published:** 2025-09-12

**Category:** cond-mat.mtrl-sci

**ID:** 2509.09998v1

**Link:** [http://arxiv.org/abs/2509.09998v1](http://arxiv.org/abs/2509.09998v1)

**Summary:** Donor-acceptor (D:A) cocrystals offer a promising platform for
next-generation optoelectronic applications, but the impact of residual solvent
molecules on their properties remains an open question. We investigate six
novel D:A cocrystals of dibenzotetrathiafulvalene (DBTTF) and
1,4,5,8,9,11-hexaazatriphenylenehexacarbo-nitrile (HATCN), prepared via solvent
evaporation, yielding 1:1 molar ratios, and horizontal vapor deposition,
resulting in solvent-free 3:2 cocrystals. Combining spectroscopy and
density-functional theory (DFT) calculations, we find that, while the
electronic and optical properties of the cocrystals are largely unaffected by
solvent inclusion, the charge transfer mechanism is surprisingly complex. Raman
spectroscopy reveals a consistent charge transfer of 0.11 $e$ across all
considered structures, corroborated by DFT calculations on solvent-free
systems. Partial charge analysis reveals that in solvated cocrystals, solvent
molecules actively participate in the charge transfer process as primary
electron acceptors. This involvement can perturb the expected D:A behavior,
revealing a faceted charge-transfer mechanism in HATCN even beyond the
established involvement of its cyano group. Overall, our study demonstrates
that while solution-based methods preserve the intrinsic D:A characteristics,
solvents can be leveraged as active electronic components, opening new avenues
for material design....

---

### 4. Self-Optimizing Machine Learning Potential Assisted Automated Workflow for Highly Efficient Complex Systems Material Design

**Authors:** Jiaxiang Li, Junwei Feng, Jie Luo, Bowen Jiang, Xiangyu Zheng, Qigang Song, Jian Lv, Keith Butler, Hanyu Liu, Congwei Xie, Yu Xie, Yanming Ma

**Published:** 2025-05-13

**Category:** cond-mat.mtrl-sci

**ID:** 2505.08159v3

**Link:** [http://arxiv.org/abs/2505.08159v3](http://arxiv.org/abs/2505.08159v3)

**Summary:** Machine learning interatomic potentials have revolutionized complex materials
design by enabling rapid exploration of material configurational spaces via
crystal structure prediction with ab initio accuracy. However, critical
challenges persist in ensuring robust generalization to unknown structures and
minimizing the requirement for substantial expert knowledge and time-consuming
manual interventions. Here, we propose an automated crystal structure
prediction framework built upon the attention-coupled neural networks potential
to address these limitations. The generalizability of the potential is achieved
by sampling regions across the local minima of the potential energy surface,
where the self-evolving pipeline autonomously refines the potential iteratively
while minimizing human intervention. The workflow is validated on Mg-Ca-H
ternary and Be-P-N-O quaternary systems by exploring nearly 10 million
configurations, demonstrating substantial speedup compared to first-principles
calculations. These results underscore the effectiveness of our approach in
accelerating the exploration and discovery of complex multi-component
functional materials....

---


<!-- ARXIV_PAPERS_END -->