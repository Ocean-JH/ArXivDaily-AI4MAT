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

## New Papers (7)

*Last updated: 2025-11-18 06:17:38 (SGT)*

### 1. Human-AI collaborative autonomous synthesis with pulsed laser deposition for remote epitaxy

**Authors:** Asraful Haque, Daniel T. Yimam, Jawad Chowdhury, Ralph Bulanadi, Ivan Vlassiouk, John Lasseter, Sujoy Ghosh, Christopher M. Rouleau, Kai Xiao, Yongtao Liu, Eva Zarkadoula, Rama K. Vasudevan, Sumner B. Harris

**Published:** 2025-11-14

**Category:** cond-mat.mtrl-sci

**ID:** 2511.11558v1

**Link:** [http://arxiv.org/abs/2511.11558v1](http://arxiv.org/abs/2511.11558v1)

**Summary:** Autonomous laboratories typically rely on data-driven decision-making, occasionally with human-in-the-loop oversight to inject domain expertise. Fully leveraging AI agents, however, requires tightly coupled, collaborative workflows spanning hypothesis generation, experimental planning, execution, and interpretation. To address this, we develop and deploy a human-AI collaborative (HAIC) workflow that integrates large language models for hypothesis generation and analysis, with collaborative policy updates driving autonomous pulsed laser deposition (PLD) experiments for remote epitaxy of BaTiO$_3$/graphene. HAIC accelerated the hypothesis formation and experimental design and efficiently mapped the growth space to graphene-damage. In situ Raman spectroscopy reveals that chemistry drives degradation while the highest energy plume components seed defects, identifying a low-O$_2$ pressure low-temperature synthesis window that preserves graphene but is incompatible with optimal BaTiO$_3$ growth. Thus, we show a two-step Ar/O$_2$ deposition is required to exfoliate ferroelectric BaTiO$_3$ while maintaining a monolayer graphene interlayer. HAIC stages human insight with AI reasoning between autonomous batches to drive rapid scientific progress, providing an evolution to many existing human-in-the-loop autonomous workflows....

---

### 2. The Interoperability Challenge in DFT Workflows Across Implementations

**Authors:** S. K. Steensen, T. S. Thakur, M. Dillenz, J. M. Carlsson, C. R. C. Rego, E. Flores, H. Hajiyani, F. Hanke, J. M. G. Lastra, W. Wenzel, N. Marzari, T. Vegge, G. Pizzi, I. E. Castelli

**Published:** 2025-11-14

**Category:** cond-mat.mtrl-sci

**ID:** 2511.11524v1

**Link:** [http://arxiv.org/abs/2511.11524v1](http://arxiv.org/abs/2511.11524v1)

**Summary:** Interoperability and cross-validation remains a significant challenge in the computational materials discovery community. In this context, we introduce a common input/output standard designed for internal translation by various workflow managers (AiiDA, PerQueue, Pipeline Pilot, and SimStack) to produce results in a unified schema. This standard aims to enable engine-agnostic workflow execution across multiple density functional theory (DFT) codes, including CASTEP, GPAW, Quantum ESPRESSO, and VASP. As a demonstration, we have implemented a workflow to calculate the open-circuit voltage across several battery cathode materials using the proposed universal input/output schema. We analyze and resolve the challenges of reconciling energetics computed by different DFT engines and document the code-specific idiosyncrasies that make straightforward comparisons difficult. Motivated by these challenges, we outline general design principles for robust automated DFT workflows. This work represents a practical step towards more reproducible and interoperable workflows for high-throughput materials screening, while highlighting challenges of aligning electronic properties, especially for non-pristine structures....

---

### 3. Data-efficient U-Net for Segmentation of Carbide Microstructures in SEM Images of Steel Alloys

**Authors:** Alinda Ezgi Gerçek, Till Korten, Paul Chekhonin, Maleeha Hassan, Peter Steinbach

**Published:** 2025-11-14

**Category:** cs.LG

**ID:** 2511.11485v1

**Link:** [http://arxiv.org/abs/2511.11485v1](http://arxiv.org/abs/2511.11485v1)

**Summary:** Understanding reactor-pressure-vessel steel microstructure is crucial for predicting mechanical properties, as carbide precipitates both strengthen the alloy and can initiate cracks. In scanning electron microscopy images, gray-value overlap between carbides and matrix makes simple thresholding ineffective. We present a data-efficient segmentation pipeline using a lightweight U-Net (30.7~M parameters) trained on just \textbf{10 annotated scanning electron microscopy images}. Despite limited data, our model achieves a \textbf{Dice-Sørensen coefficient of 0.98}, significantly outperforming the state-of-the-art in the field of metallurgy (classical image analysis: 0.85), while reducing annotation effort by one order of magnitude compared to the state-of-the-art data efficient segmentation model. This approach enables rapid, automated carbide quantification for alloy design and generalizes to other steel types, demonstrating the potential of data-efficient deep learning in reactor-pressure-vessel steel analysis....

---

### 4. Metavalent Bonding-Induced Phonon Hardening and Giant Anharmonicity in BeO

**Authors:** Xuejie Li, Yuzhou Hao, Yujie Liu, Shengying Yue, Xiaolong Yang, Turab Lookman, Xiangdong Ding, Jun Sun, Zhibin Gao

**Published:** 2025-11-14

**Category:** cond-mat.mtrl-sci

**ID:** 2511.11443v1

**Link:** [http://arxiv.org/abs/2511.11443v1](http://arxiv.org/abs/2511.11443v1)

**Summary:** The search for materials with intrinsically low thermal conductivity ($κ_L$) is critical for energy applications, yet conventional descriptors often fail to capture the complex interplay between bonding and lattice dynamics. Here, first-principles calculations are used to contrast the thermal transport in covalent zincblende (zb) and metavalent rocksalt (rs) BeO. We find that the metavalent bonding in rs-BeO enhances lattice anharmonicity, activating multi-phonon scattering channels and suppressing phonon transport. This results in an ultralow $κ_L$ of 24 W m$^{-1}$ K$^{-1}$ at 300 K, starkly contrasting with the zb phase (357 W m$^{-1}$ K$^{-1}$). Accurately modeling such strongly anharmonic systems requires explicit inclusion of temperature-dependent phonon renormalization and four-phonon scattering. These contributions, negligible in zb-BeO, are essential for high-precision calculations of the severely suppressed $κ_L$ in rs-BeO. Finally, we identify three key indicators to guide the discovery of metavalently bonded, incipient-metallic materials: (i) an NaCl-type crystal structure, (ii) large Grüneisen parameters ($\textgreater$2), and (iii) a breakdown of the Lyddane-Sachs-Teller relation. These findings provide microscopic insight into thermal transport suppression by metavalent bonding and offer a predictive framework for identifying promising thermoelectrics and phase-change materials....

---

### 5. Robust inverse material design with physical guarantees using the Voigt-Reuss Net

**Authors:** Sanath Keshav, Felix Fritzen

**Published:** 2025-11-14

**Category:** cs.LG

**ID:** 2511.11388v1

**Link:** [http://arxiv.org/abs/2511.11388v1](http://arxiv.org/abs/2511.11388v1)

**Summary:** We propose a spectrally normalized surrogate for forward and inverse mechanical homogenization with hard physical guarantees. Leveraging the Voigt-Reuss bounds, we factor their difference via a Cholesky-like operator and learn a dimensionless, symmetric positive semi-definite representation with eigenvalues in $[0,1]$; the inverse map returns symmetric positive-definite predictions that lie between the bounds in the Löwner sense. In 3D linear elasticity on an open dataset of stochastic biphasic microstructures, a fully connected Voigt-Reuss net trained on $>\!7.5\times 10^{5}$ FFT-based labels with 236 isotropy-invariant descriptors and three contrast parameters recovers the isotropic projection with near-perfect fidelity (isotropy-related entries: $R^2 \ge 0.998$), while anisotropy-revealing couplings are unidentifiable from $SO(3)$-invariant inputs. Tensor-level relative Frobenius errors have median $\approx 1.7\%$ and mean $\approx 3.4\%$ across splits. For 2D plane strain on thresholded trigonometric microstructures, coupling spectral normalization with a differentiable renderer and a CNN yields $R^2>0.99$ on all components, subpercent normalized losses, accurate tracking of percolation-induced eigenvalue jumps, and robust generalization to out-of-distribution images. Treating the parametric microstructure as design variables, batched first-order optimization with a single surrogate matches target tensors within a few percent and returns diverse near-optimal designs. Overall, the Voigt-Reuss net unifies accurate, physically admissible forward prediction with large-batch, constraint-consistent inverse design, and is generic to elliptic operators and coupled-physics settings....

---

### 6. Sparse Methods for Vector Embeddings of TPC Data

**Authors:** Tyler Wheeler, Michelle P. Kuchera, Raghuram Ramanujan, Ryan Krupp, Chris Wrede, Saiprasad Ravishankar, Connor L. Cross, Hoi Yan Ian Heung, Andrew J. Jones, Benjamin Votaw

**Published:** 2025-11-14

**Category:** cs.LG

**ID:** 2511.11221v1

**Link:** [http://arxiv.org/abs/2511.11221v1](http://arxiv.org/abs/2511.11221v1)

**Summary:** Time Projection Chambers (TPCs) are versatile detectors that reconstruct charged-particle tracks in an ionizing medium, enabling sensitive measurements across a wide range of nuclear physics experiments. We explore sparse convolutional networks for representation learning on TPC data, finding that a sparse ResNet architecture, even with randomly set weights, provides useful structured vector embeddings of events. Pre-training this architecture on a simple physics-motivated binary classification task further improves the embedding quality. Using data from the GAseous Detector with GErmanium Tagging (GADGET) II TPC, a detector optimized for measuring low-energy $β$-delayed particle decays, we represent raw pad-level signals as sparse tensors, train Minkowski Engine ResNet models, and probe the resulting event-level embeddings which reveal rich event structure. As a cross-detector test, we embed data from the Active-Target TPC (AT-TPC) -- a detector designed for nuclear reaction studies in inverse kinematics -- using the same encoder. We find that even an untrained sparse ResNet model provides useful embeddings of AT-TPC data, and we observe improvements when the model is trained on GADGET data. Together, these results highlight the potential of sparse convolutional techniques as a general tool for representation learning in diverse TPC experiments....

---

### 7. Sliding Ferroelectric Metal with Ferrimagnetism

**Authors:** Zhenzhou Guo, Shifeng Qian, Xiaodong Zhou, Wenhong Wang, Zhenxiang Cheng, Xiaotian Wang

**Published:** 2025-08-11

**Category:** cond-mat.mtrl-sci

**ID:** 2508.07947v2

**Link:** [http://arxiv.org/abs/2508.07947v2](http://arxiv.org/abs/2508.07947v2)

**Summary:** Two-dimensional (2D) sliding ferroelectric (FE) metals with ferrimagnetism represent a previously unexplored class of spintronic materials, featuring out-of-plane FE polarization, metallic conductivity, and a finite net magnetization, which together enable electrically tunable spintronic functionalities via FE switching. Here, based on antiferromagnetic (AFM) metallic bilayers, we propose a general strategy for constructing 2D sliding FE ferrimagnetic (FiM) metals that can achieve triply-coupled switching, in which the FE polarization, spin splitting, and net magnetization are reversed simultaneously through FE switching. As a prototypical realization, we design a bilayer sliding FE metal with FiM order, derived from monolayer Fe$_5$GeTe$_2$ -- a van der Waals metal with intrinsic ferromagnetic order close to room temperature. The system exhibits a FE transition from a nonpolar (NP) AFM phase to a FE FiM phase via interlayer sliding. The in-plane mirror symmetry breaking in FE metallic states lifts the nonrelativistic spin degeneracy that exists in the NP phase, leading to a sizable net magnetic moment. Furthermore, the interplay between metallicity, ferroelectricity, and ferrimagnetism gives rise to pronounced sign-reversible transport responses near the Fermi level, all of which can be electrically controlled by FE switching. Our results establish sliding FE metals with FiM as a promising platform for electrically reconfigurable, high-speed, and low-dissipation spintronic devices....

---


<!-- ARXIV_PAPERS_END -->