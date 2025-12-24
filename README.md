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

## New Papers (5)

*Last updated: 2025-12-25 06:18:25 (SGT)*

### 1. QE-Catalytic: A Graph-Language Multimodal Base Model for Relaxed-Energy Prediction in Catalytic Adsorption

**Authors:** Yanjie Li, Jian Xu, Xueqing Chen, Lina Yu, Shiming Xiang, Weijun Li, Cheng-lin Liu

**Published:** 2025-12-23

**Category:** cs.LG

**ID:** 2512.20084v1

**Link:** [http://arxiv.org/abs/2512.20084v1](http://arxiv.org/abs/2512.20084v1)

**Summary:** Adsorption energy is a key descriptor of catalytic reactivity. It is fundamentally defined as the difference between the relaxed total energy of the adsorbate-surface system and that of an appropriate reference state; therefore, the accuracy of relaxed-energy prediction directly determines the reliability of machine-learning-driven catalyst screening. E(3)-equivariant graph neural networks (GNNs) can natively operate on three-dimensional atomic coordinates under periodic boundary conditions and have demonstrated strong performance on such tasks. In contrast, language-model-based approaches, while enabling human-readable textual descriptions and reducing reliance on explicit graph -- thereby broadening applicability -- remain insufficient in both adsorption-configuration energy prediction accuracy and in distinguishing ``the same system with different configurations,'' even with graph-assisted pretraining in the style of GAP-CATBERTa.
  To this end, we propose QE-Catalytic, a multimodal framework that deeply couples a large language model (\textbf{Q}wen) with an E(3)-equivariant graph Transformer (\textbf{E}quiformer-V2), enabling unified support for adsorption-configuration property prediction and inverse design on complex catalytic surfaces. During prediction, QE-Catalytic jointly leverages three-dimensional structures and structured configuration text, and injects ``3D geometric information'' into the language channel via graph-text alignment, allowing it to function as a high-performance text-based predictor when precise coordinates are unavailable, while also autoregressively generating CIF files for target-energy-driven structure design and information completion. On OC20, QE-Catalytic reduces the MAE of relaxed adsorption energy from 0.713~eV to 0.486~eV, and consistently outperforms baseline models such as CatBERTa and GAP-CATBERTa across multiple evaluation protocols....

---

### 2. Computational Design of Metal-Free Porphyrin Dyes for Sustainable Dye-Sensitized Solar Cells Informing Energy Informatics and Decision Support

**Authors:** Md Mahmudul Hasan, Chiara Bordin, Fairuz Islam, Tamanna Tasnim, Md. Athar Ishtiyaq, Md. Tasin Nur Rahim, Dhrubo Roy

**Published:** 2025-12-22

**Category:** cond-mat.mtrl-sci

**ID:** 2512.19529v1

**Link:** [http://arxiv.org/abs/2512.19529v1](http://arxiv.org/abs/2512.19529v1)

**Summary:** This study aims to evaluate the optoelectronic properties of metal free porphyrin-based D-$π$-A dyes via in-silico performance investigation notifying energy informatics and decision support. To develop novel organic dyes, three acceptor/anchoring groups and five donating groups were introduced to strategic positions of the base porphyrin structure, resulting in a total of fifteen dyes. The singlet ground state geometries of the dyes were optimized utilizing density functional theory (DFT) with B3LYP and the excited state optical properties were explored through time-dependent DFT (TD-DFT) using the PCM model with tetrahydrofuran (THF) as solvent. Both DFT and TD-DFT calculations were carried out using the 6-311G(d,p) basis set. The HOMO energy levels of almost all the modified dyes are lower than the redox potential of I$^-$/I$3^-$ and LUMO energy levels are higher than the conduction band of TiO$2$. The absorption maxima values ranged from 690.64 to 975.55 nm. The dye N1 using triphenylamine group as donor and p-ethynylbenzoic acid group as acceptor, showed optimum optoelectronic properties ($ΔG{reg}=-9.73$ eV, $ΔG{inj}=7.18$ eV, $V_{OC}=1.47$ V and $J_{SC}=15.03$ mA/cm$^2$) with highest PCE 14.37%, making it the best studied dye. This newly modified organic dye with enhanced PCE is remarkably effective for the dye-sensitized solar cells (DSSC) industry. Beyond materials discovery, this study highlights the role of high-performance computing in enabling predictive screening of dye candidates and generating performance indicators (HOMO-LUMO gaps, absorption spectra, charge transfer free energies, photovoltaic metrics). These outputs can serve as key parameters for energy informatics and system modelling....

---

### 3. Measuring the Hall effect in hysteretic materials

**Authors:** Jaime M. Moya, Anthony Voyemant, Sudipta Chatterjee, Scott B. Lee, Grigorii Skorupskii, Connor J. Pollak, Leslie M. Schoop

**Published:** 2025-12-22

**Category:** cond-mat.str-el

**ID:** 2512.19427v1

**Link:** [http://arxiv.org/abs/2512.19427v1](http://arxiv.org/abs/2512.19427v1)

**Summary:** Measurement of the Hall effect is a ubiquitous probe for materials discovery, characterization, and metrology. Inherent to the Hall measurement geometry, the measured signal is often contaminated by unwanted contributions, so the data must be processed to isolate the Hall response. The standard approach invokes Onsager-Casimir reciprocity and antisymmetrizes the raw signal about zero applied magnetic field. In hysteretic materials this becomes nontrivial, since Onsager-Casimir relations apply only to microscopically reversible states. Incorrect antisymmetrization can lead to artifacts that mimic anomalous or topological Hall signatures. The situation is especially subtle when hysteresis loops are not centered at zero applied field, as in exchange-biased systems. A practical reference for generically extracting the Hall response in hysteretic materials is lacking. Here, using Co$_3$Sn$_2$S$_2$ as a bulk single-crystal model that can be prepared with or without exchange-biased hysteresis, we demonstrate two procedures that can be used to extract the Hall effect: (1) reverse-magnetic-field reciprocity and (2) antisymmetrization with respect to applied field. We then measure the Hall effect on CeCoGe$_3$, a noncentrosymmetric antiferromagnet which can be prepared to have asymmetric magnetization and magnetoresistance, and demonstrate how improper processing can generate artificial anomalous Hall signals. These methods are generic and can be applied to any conductor....

---

### 4. PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design

**Authors:** Andy Xu, Rohan Desai, Larry Wang, Gabriel Hope, Ethan Ritz

**Published:** 2025-09-08

**Category:** cs.LG

**ID:** 2509.07150v3

**Link:** [http://arxiv.org/abs/2509.07150v3](http://arxiv.org/abs/2509.07150v3)

**Summary:** Reinforcement Learning from Verifiable Rewards (RLVR) has emerged as a promising approach to improve correctness in LLMs, however, in many scientific problems, the objective is not necessarily to produce the correct answer, but instead to produce a diverse array of candidates which satisfy a set of constraints. We study this challenge in the context of materials generation. To this end, we introduce PLaID++, an LLM post-trained for stable and property-guided crystal generation. We find that performance hinges on our crystallographic representation and reward formulation. First, we introduce a compact, symmetry-informed Wyckoff text representation which improves computational efficiency and encourages generalization from physical priors. Second, we demonstrate that temperature scaling acts as an entropy regularizer which counteracts mode collapse and encourages exploration. By encoding symmetry constraints directly into text and guiding model outputs towards desirable chemical space, PLaID++ generates structures that are thermodynamically stable, unique, and novel at a $\sim$50\% greater rate than prior methods and conditionally generates structures with desired space group properties. Our work demonstrates the potential of adapting post-training techniques from natural language processing to materials design, paving the way for targeted and efficient discovery of novel materials....

---

### 5. Lattice-Renormalized Tunneling Models for Superconducting Qubit Materials

**Authors:** P. G. Pritchard, James M. Rondinelli

**Published:** 2025-12-20

**Category:** quant-ph

**ID:** 2512.18156v1

**Link:** [http://arxiv.org/abs/2512.18156v1](http://arxiv.org/abs/2512.18156v1)

**Summary:** We present a lattice-renormalized formalism for configurational tunneling two-level systems (TLS) that overcomes limitations of minimum-energy-path and light-particle models. Derived from the nuclear Hamiltonian, our formulation introduces composite phonon coordinates to capture lattice distortions between degenerate potential wells. This approach resolves deficiencies in prior models and enables accurate computation of tunnel splittings and excitation spectra for hydrogen-based TLS in bcc Nb. Our results bound experimental tunnel splittings and reveal strong anharmonic couplings between tunneling atoms and lattice phonons, establishing a direct link between TLS dynamics and phonon-mediated strain interactions. The formalism further generalizes to multi-level systems (MLS), providing insight into defect-induced decoherence in superconducting qubits and guiding strategies for materials design to suppress TLS-related loss....

---


<!-- ARXIV_PAPERS_END -->