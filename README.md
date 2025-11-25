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

## New Papers (18)

*Last updated: 2025-11-26 06:19:20 (SGT)*

### 1. Artificial Intelligence Driven Workflow for Accelerating Design of Novel Photosensitizers

**Authors:** Hongyi Wang, Xiuli Zheng, Weimin Liu, Zitian Tang, Sheng Gong

**Published:** 2025-11-24

**Category:** cond-mat.mtrl-sci

**ID:** 2511.19347v1

**Link:** [http://arxiv.org/abs/2511.19347v1](http://arxiv.org/abs/2511.19347v1)

**Summary:** The discovery of high-performance photosensitizers has long been hindered by the time-consuming and resource-intensive nature of traditional trial-and-error approaches. Here, we present \textbf{A}I-\textbf{A}ccelerated \textbf{P}hoto\textbf{S}ensitizer \textbf{I}nnovation (AAPSI), a closed-loop workflow that integrates expert knowledge, scaffold-based molecule generation, and Bayesian optimization to accelerate the design of novel photosensitizers. The scaffold-driven generation in AAPSI ensures structural novelty and synthetic feasibility, while the iterative AI-experiment loop accelerates the discovery of novel photosensitizers. AAPSI leverages a curated database of 102,534 photosensitizer-solvent pairs and generate 6,148 synthetically accessible candidates. These candidates are screened via graph transformers trained to predict singlet oxygen quantum yield ($φ_Δ$) and absorption maxima ($λ_{max}$), following experimental validation. This work generates several novel candidates for photodynamic therapy (PDT), among which the hypocrellin-based candidate HB4Ph exhibits exceptional performance at the Pareto frontier of high quantum yield of singlet oxygen and long absorption maxima among current photosensitizers ($φ_Δ$=0.85, $λ_{max}$=650nm)....

---

### 2. High-throughput validation of phase formability and simulation accuracy of Cantor alloys

**Authors:** Changjun Cheng, Daniel Persaud, Kangming Li, Michael J. Moorehead, Natalie Page, Christian Lavoie, Beatriz Diaz Moreno, Adrien Couet, Samuel E Lofland, Jason Hattrick-Simpers

**Published:** 2025-11-24

**Category:** cond-mat.mtrl-sci

**ID:** 2511.19335v1

**Link:** [http://arxiv.org/abs/2511.19335v1](http://arxiv.org/abs/2511.19335v1)

**Summary:** High-throughput methods enable accelerated discovery of novel materials in complex systems such as high-entropy alloys, which exhibit intricate phase stability across vast compositional spaces. Computational approaches, including Density Functional Theory (DFT) and calculation of phase diagrams (CALPHAD), facilitate screening of phase formability as a function of composition and temperature. However, the integration of computational predictions with experimental validation remains challenging in high-throughput studies. In this work, we introduce a quantitative confidence metric to assess the agreement between predictions and experimental observations, providing a quantitative measure of the confidence of machine learning models trained on either DFT or CALPHAD input in accounting for experimental evidence. The experimental dataset was generated via high-throughput in-situ synchrotron X-ray diffraction on compositionally varied FeNiMnCr alloy libraries, heated from room temperature to ~1000 °C. Agreement between the observed and predicted phases was evaluated using either temperature-independent phase classification or a model that incorporates a temperature-dependent probability of phase formation. This integrated approach demonstrates where strong overall agreement between computation and experiment exists, while also identifying key discrepancies, particularly in FCC/BCC predictions at Mn-rich regions to inform future model refinement....

---

### 3. Interpreting GFlowNets for Drug Discovery: Extracting Actionable Insights for Medicinal Chemistry

**Authors:** Amirtha Varshini A S, Duminda S. Ranasinghe, Hok Hei Tam

**Published:** 2025-11-24

**Category:** cs.LG

**ID:** 2511.19264v1

**Link:** [http://arxiv.org/abs/2511.19264v1](http://arxiv.org/abs/2511.19264v1)

**Summary:** Generative Flow Networks, or GFlowNets, offer a promising framework for molecular design, but their internal decision policies remain opaque. This limits adoption in drug discovery, where chemists require clear and interpretable rationales for proposed structures. We present an interpretability framework for SynFlowNet, a GFlowNet trained on documented chemical reactions and purchasable starting materials that generates both molecules and the synthetic routes that produce them. Our approach integrates three complementary components. Gradient based saliency combined with counterfactual perturbations identifies which atomic environments influence reward and how structural edits change molecular outcomes. Sparse autoencoders reveal axis aligned latent factors that correspond to physicochemical properties such as polarity, lipophilicity, and molecular size. Motif probes show that functional groups including aromatic rings and halogens are explicitly encoded and linearly decodable from the internal embeddings. Together, these results expose the chemical logic inside SynFlowNet and provide actionable and mechanistic insight that supports transparent and controllable molecular design....

---

### 4. Solar-GECO: Perovskite Solar Cell Property Prediction with Geometric-Aware Co-Attention

**Authors:** Lucas Li, Jean-Baptiste Puel, Florence Carton, Dounya Barrit, Jhony H. Giraldo

**Published:** 2025-11-24

**Category:** cs.LG

**ID:** 2511.19263v1

**Link:** [http://arxiv.org/abs/2511.19263v1](http://arxiv.org/abs/2511.19263v1)

**Summary:** Perovskite solar cells are promising candidates for next-generation photovoltaics. However, their performance as multi-scale devices is determined by complex interactions between their constituent layers. This creates a vast combinatorial space of possible materials and device architectures, making the conventional experimental-based screening process slow and expensive. Machine learning models try to address this problem, but they only focus on individual material properties or neglect the important geometric information of the perovskite crystal. To address this problem, we propose to predict perovskite solar cell power conversion efficiency with a geometric-aware co-attention (Solar-GECO) model. Solar-GECO combines a geometric graph neural network (GNN) - that directly encodes the atomic structure of the perovskite absorber - with language model embeddings that process the textual strings representing the chemical compounds of the transport layers and other device components. Solar-GECO also integrates a co-attention module to capture intra-layer dependencies and inter-layer interactions, while a probabilistic regression head predicts both power conversion efficiency (PCE) and its associated uncertainty. Solar-GECO achieves state-of-the-art performance, significantly outperforming several baselines, reducing the mean absolute error (MAE) for PCE prediction from 3.066 to 2.936 compared to semantic GNN (the previous state-of-the-art model). Solar-GECO demonstrates that integrating geometric and textual information provides a more powerful and accurate framework for PCE prediction....

---

### 5. High-Throughput Quantification of Altermagnetic Band Splitting

**Authors:** Ali Sufyan, Brahim Marfoua, J. Andreas Larsson, Erik van Loon, Rickard Armiento

**Published:** 2025-09-18

**Category:** cond-mat.mtrl-sci

**ID:** 2509.14729v2

**Link:** [http://arxiv.org/abs/2509.14729v2](http://arxiv.org/abs/2509.14729v2)

**Summary:** Altermagnetism represents a recently established class of collinear magnetism that combines zero net magnetization with momentum-dependent spin polarization, enabled by symmetry constraints rather than spin-orbit coupling. This distinctive behavior gives rise to sizable spin splitting even in materials composed of light, earth-abundant elements, offering promising prospects for next-generation spintronics applications. Despite growing theoretical and experimental interest, the discovery of altermagnetic materials remains limited due to the complexity of magnetic symmetry and the inefficiency of conventional approaches. Here, we present a comprehensive high-throughput screening of the entire MAGNDATA database, integrating symmetry analysis with spin-polarized density functional theory (DFT) calculations to identify and characterize altermagnetic candidates. Our workflow uncovers 173 materials exhibiting significant spin splitting ($\geq 50$ meV within $\pm 3$ eV of the Fermi level), spanning both metallic and semiconducting systems. Crucially, our momentum-resolved analysis reveals that the spin splitting varies strongly across the Brillouin zone, and that the maximal splitting tends to occur away from the high-symmetry paths, a result that directly informs and guides future photoemission experiments. By expanding the catalog of known altermagnets and elucidating the symmetry-protected origins of spin splitting, this work lays a robust foundation for future experimental and theoretical advances in spintronics and quantum materials discovery....

---

### 6. Feature Ranking in Credit-Risk with Qudit-Based Networks

**Authors:** Georgios Maragkopoulos, Lazaros Chavatzoglou, Aikaterini Mandilara, Dimitris Syvridis

**Published:** 2025-11-24

**Category:** quant-ph

**ID:** 2511.19150v1

**Link:** [http://arxiv.org/abs/2511.19150v1](http://arxiv.org/abs/2511.19150v1)

**Summary:** In finance, predictive models must balance accuracy and interpretability, particularly in credit risk assessment, where model decisions carry material consequences. We present a quantum neural network (QNN) based on a single qudit, in which both data features and trainable parameters are co-encoded within a unified unitary evolution generated by the full Lie algebra. This design explores the entire Hilbert space while enabling interpretability through the magnitudes of the learned coefficients. We benchmark our model on a real-world, imbalanced credit-risk dataset from Taiwan. The proposed QNN consistently outperforms LR and reaches the results of random forest models in macro-F1 score while preserving a transparent correspondence between learned parameters and input feature importance. To quantify the interpretability of the proposed model, we introduce two complementary metrics: (i) the edit distance between the model's feature ranking and that of LR, and (ii) a feature-poisoning test where selected features are replaced with noise. Results indicate that the proposed quantum model achieves competitive performance while offering a tractable path toward interpretable quantum learning....

---

### 7. MOCLIP: A Foundation Model for Large-Scale Nanophotonic Inverse Design

**Authors:** S. Rodionov, A. Burguete-Lopez, M. Makarenko, Q. Wang, F. Getman, A. Fratalocchi

**Published:** 2025-11-24

**Category:** physics.optics

**ID:** 2511.18980v1

**Link:** [http://arxiv.org/abs/2511.18980v1](http://arxiv.org/abs/2511.18980v1)

**Summary:** Foundation models (FM) are transforming artificial intelligence by enabling generalizable, data-efficient solutions across different domains for a broad range of applications. However, the lack of large and diverse datasets limits the development of FM in nanophotonics. This work presents MOCLIP (Metasurface Optics Contrastive Learning Pretrained), a nanophotonic foundation model that integrates metasurface geometry and spectra within a shared latent space. MOCLIP employs contrastive learning to align geometry and spectral representations using an experimentally acquired dataset with a sample density comparable to ImageNet-1K. The study demonstrates MOCLIP inverse design capabilities for high-throughput zero-shot prediction at a rate of 0.2 million samples per second, enabling the design of a full 4-inch wafer populated with high-density metasurfaces in minutes. It also shows generative latent-space optimization reaching 97 percent accuracy. Finally, we introduce an optical information storage concept that uses MOCLIP to achieve a density of 0.1 Gbit per square millimeter at the resolution limit, exceeding commercial optical media by a factor of six. These results position MOCLIP as a scalable and versatile platform for next-generation photonic design and data-driven applications....

---

### 8. Quantized Polarization Redefines Polar Interfaces

**Authors:** Hongsheng Pang, Lixin He

**Published:** 2025-11-24

**Category:** cond-mat.mtrl-sci

**ID:** 2511.18697v1

**Link:** [http://arxiv.org/abs/2511.18697v1](http://arxiv.org/abs/2511.18697v1)

**Summary:** In crystalline solids, the electronic polarization follows the \emph{generalized Neumann's principle}, under which all crystallographic point groups can, in principle, support ferroelectric polarization. However, in high-symmetry structures, polarization is constrained by symmetry operations and becomes quantized into discrete values. We demonstrate that this quantized polarization (QP) is not a mathematical artifact but a \emph{symmetry-protected invariant} that encodes intrinsic information about a material's symmetry and electronic structure. Because of its discrete and non-continuous nature, when two materials with different QPs form an interface, their bulk polarization states cannot be connected adiabatically, compelling the system to develop pronounced interfacial responses: such as metallic states, bound charges, or strong lattice distortions. This theoretical framework provides a unified reinterpretation of classical systems such as the LaAlO$_3$/SrTiO$_3$ interface, revealing it as a prototypical case of QP mismatch. By establishing QP as a fundamental bulk invariant, our work uncovers a universal mechanism governing interfacial electronic phenomena and opens new pathways for the design of functional quantum materials through engineered polarization mismatch....

---

### 9. High-throughput computation of electric polarization in solids via Berry flux diagonalization

**Authors:** Abigail N. Poteshman, Francesco Ricci, Jeffrey B. Neaton

**Published:** 2025-11-23

**Category:** cond-mat.mtrl-sci

**ID:** 2511.18586v1

**Link:** [http://arxiv.org/abs/2511.18586v1](http://arxiv.org/abs/2511.18586v1)

**Summary:** Electric polarization in the absence of an externally applied electric field is a key property of polar materials, but the standard interpolation-based ab initio approach to compute polarization differences within the modern theory of polarization presents challenges for automated high-throughput calculations. Berry flux diagonalization [J. Bonini et. al, Phys. Rev. B 102, 045141 (2020)] has been proposed as an efficient and reliable alternative, though it has yet to be widely deployed. Here, we assess Berry flux diagonalization using ab initio calculations of a large set of materials, introducing and validating heuristics that ensure branch alignment with a minimal number of intermediate interpolated structures. Our automated implementation of Berry flux diagonalization succeeds in cases where prior interpolation-based workflows fail due to band-gap closures or branch ambiguities. Benchmarking with ab initio calculations of 176 candidate ferroelectrics, we demonstrate the efficacy of the approach on a broad range of insulating materials and obtain accurate effective polarization values with fewer interpolated structures than prior automated interpolation-based workflows. Our real-space heuristics that can predict gauge stability a priori from ionic displacements enable a general automated framework for reliable polarization calculations and efficient high-throughput screening of chemically and structurally diverse polar insulators. These results establish Berry flux diagonalization as a robust and efficient method to compute the effective polarization of solids and to accelerate the data-driven discovery of functional polar materials....

---

### 10. Curvature-Dependent Polarity of Interfacial Energy Flow in Functionalized CNT Polymer Nanocomposites: A Reactive Molecular Dynamics Perspective

**Authors:** Mehedi Hasan, Khayrul Islam, Michael T. Kio, AKM Masud

**Published:** 2025-11-23

**Category:** physics.atm-clus

**ID:** 2511.18560v1

**Link:** [http://arxiv.org/abs/2511.18560v1](http://arxiv.org/abs/2511.18560v1)

**Summary:** Carbon nanotube (CNT)-polymer composites are widely engineered using surface coatings and chemical treatments to improve interfacial bonding and load transfer. It has been suggested in the nanocomposite literature that nanotube curvature, in conjunction with surface functionalization such as polydopamine (PDA) coating, could serve as an additional control knob for tuning interfacial bonding and energy dissipation in polymer-CNT systems. While experimental and simulation studies have demonstrated the benefits of PDA functionalization, the fundamental mechanism by which nanotube curvature modulates interfacial energy flow and mechanical polarity remains unresolved. This gap is sharpened by a persistent paradox: identical PDA functionalization strengthens some CNT-polymer systems while weakening others, a curvature-dependent inconsistency that has remained unexplained. Here, we employ reactive molecular dynamics (ReaxFF) simulations to resolve how curvature and PDA functionalization jointly govern interfacial energy evolution in CNT-polyvinyl alcohol (PVA) nanocomposites. Our investigation reveals that curvature and PDA functionalization jointly produce opposite regimes of interfacial energy flow: high-curvature CNTs generate dissipative, frictional interphases, whereas low-curvature CNTs confine energy in rigid, cohesive shells. This polarity inversion originates from a curvature-induced transition in PDA adsorption geometry that transforms the interphase from an energy-releasing to an energy-storing configuration. These results establish curvature as a fundamental design parameter for engineering polymer-nanotube interfaces, offering a predictive route to tune interfacial energy flow, mechanical resilience, and transport properties beyond the limits of conventional chemical functionalization....

---

### 11. Thermal Analog Computing: Application to Matrix-vector Multiplication with Inverse-designed Metastructures

**Authors:** Caio Silva, Giuseppe Romano

**Published:** 2025-03-28

**Category:** cond-mat.mes-hall

**ID:** 2503.22603v2

**Link:** [http://arxiv.org/abs/2503.22603v2](http://arxiv.org/abs/2503.22603v2)

**Summary:** The rising computational demand of modern workloads has renewed interest in energy-efficient paradigms such as neuromorphic and analog computing. A fundamental operation in these systems is matrix-vector multiplication (MVM), ubiquitous in signal processing and machine learning. Here, we demonstrate MVM using inverse-designed metastructures that exploit heat conduction as the signal carrier. The proposed approach is based on a generalization of effective thermal conductivity to systems with multiple input and output ports: The input signal is encoded as a set of applied temperatures, while the output is represented by the power collected at designated terminals. The metastructures are obtained via density-based topology optimization, enabled by a differentiable thermal transport solver and automatic differentiation, achieving an accuracy $> 99\%$ in most cases across pool of matrices with dimensions $2 \times 2$ and $3 \times 3$. We apply this methodology--termed thermal analog computing--to realize matrices relevant to practical tasks, including the discrete Fourier transform and convolutional filters. These results suggest new opportunities for analog information processing in environments where temperature gradients naturally arise, such as device hotspots and thermal controllers...

---

### 12. DeepRWCap: Neural-Guided Random-Walk Capacitance Solver for IC Design

**Authors:** Hector R. Rodriguez, Jiechen Huang, Wenjian Yu

**Published:** 2025-11-10

**Category:** cs.LG

**ID:** 2511.06831v2

**Link:** [http://arxiv.org/abs/2511.06831v2](http://arxiv.org/abs/2511.06831v2)

**Summary:** Monte Carlo random walk methods are widely used in capacitance extraction for their mesh free formulation and inherent parallelism. However, modern semiconductor technologies with densely packed structures present significant challenges in unbiasedly sampling transition domains in walk steps with multiple high contrast dielectric materials. We present DeepRWCap, a machine learning guided random walk solver that predicts the transition quantities required to guide each step of the walk. These include Poisson kernels, gradient kernels, and the signs and magnitudes of weights. DeepRWCap employs a two stage neural architecture that decomposes structured outputs into face wise distributions and spatial kernels on cube faces. It uses 3D convolutional networks to capture volumetric dielectric interactions and 2D depthwise separable convolutions to model localized kernel behavior. The design incorporates grid based positional encodings and structural design choices informed by cube symmetries to reduce learning redundancy and improve generalization. Trained on 100000 procedurally generated dielectric configurations, DeepRWCap achieves a mean relative error of 1.24 +/- 0.53% when benchmarked against the commercial Raphael solver on the self capacitance estimation of 10 industrial designs spanning 12 to 55 nm nodes. Compared to the state of the art stochastic difference method Microwalk, DeepRWCap achieves an average speedup of 23%. On complex designs with runtimes over 10 seconds, it reaches an average acceleration of 49%....

---

### 13. Hierarchical Deep Research with Local-Web RAG: Toward Automated System-Level Materials Discovery

**Authors:** Rui Ding, Rodrigo Pires Ferreira, Yuxin Chen, Junhong Chen

**Published:** 2025-11-23

**Category:** cs.LG

**ID:** 2511.18303v1

**Link:** [http://arxiv.org/abs/2511.18303v1](http://arxiv.org/abs/2511.18303v1)

**Summary:** We present a long-horizon, hierarchical deep research (DR) agent designed for complex materials and device discovery problems that exceed the scope of existing Machine Learning (ML) surrogates and closed-source commercial agents. Our framework instantiates a locally deployable DR instance that integrates local retrieval-augmented generation with large language model reasoners, enhanced by a Deep Tree of Research (DToR) mechanism that adaptively expands and prunes research branches to maximize coverage, depth, and coherence. We systematically evaluate across 27 nanomaterials/device topics using a large language model (LLM)-as-judge rubric with five web-enabled state-of-the-art models as jurors. In addition, we conduct dry-lab validations on five representative tasks, where human experts use domain simulations (e.g., density functional theory, DFT) to verify whether DR-agent proposals are actionable. Results show that our DR agent produces reports with quality comparable to--and often exceeding--those of commercial systems (ChatGPT-5-thinking/o3/o4-mini-high Deep Research) at a substantially lower cost, while enabling on-prem integration with local data and tools....

---

### 14. SynTwins: A Retrosynthesis-Guided Framework for Synthesizable Molecular Analog Generation

**Authors:** Shuan Chen, Gunwook Nam, Alan Aspuru-Guzik, Yousung Jung

**Published:** 2025-07-03

**Category:** physics.chem-ph

**ID:** 2507.02752v2

**Link:** [http://arxiv.org/abs/2507.02752v2](http://arxiv.org/abs/2507.02752v2)

**Summary:** The disconnect between AI-generated molecules with desirable properties and their synthetic feasibility remains a critical bottleneck in computational discovery of drugs and materials. While generative AI has accelerated the proposal of candidate molecules, many of these structures prove challenging or impossible to synthesize using established chemical reactions. Here, we introduce SynTwins, a novel retrosynthesis-guided molecule design framework that finds synthetically accessible molecular analogs by emulating expert chemists' strategies in three steps: retrosynthesis, searching similar building blocks, and virtual synthesis. Using a search algorithm instead of a stochastic data-driven generator, SynTwins outperforms state-of-the-art machine learning models at exploring synthetically accessible analogs while maintaining high structural similarity to original target molecules. Furthermore, when integrated into existing molecular property-optimization frameworks, our hybrid approach produces synthetically feasible analogs with minimal loss in property scores. Our comprehensive benchmarking across diverse molecular datasets demonstrates that SynTwins effectively bridges the gap between computational design and experimental synthesis, providing a practical solution for accelerating the discovery of synthesizable molecules with desired properties for a wide range of applications....

---

### 15. PyAPX: Python toolkit for atomic configuration pattern exploration

**Authors:** Akira Kusaba, Tetsuji Kuboyama, Karol Kawka, Pawel Kempisty, Yoshihiro Kangawa

**Published:** 2025-11-22

**Category:** cond-mat.mtrl-sci

**ID:** 2511.17972v1

**Link:** [http://arxiv.org/abs/2511.17972v1](http://arxiv.org/abs/2511.17972v1)

**Summary:** In materials discovery, the integration of first-principles calculations with machine learning techniques has been actively studied for two key tasks: crystal structure prediction, which searches for stable structures given a chemical composition, and elemental substitution, which explores chemical compositions that yield desirable properties in a given crystal structure. However, even when both the crystal structure and chemical composition are fixed, material properties can still vary depending on the atomic arrangements (configurations) at crystallographic sites. To support detailed material design, we present PyAPX, a Python toolkit that performs Bayesian searches of stable atomic configurations. A distinctive feature of this initial release is the introduction of encoding methods suitable for configuration search, and we evaluate their performance using the h-BCN system. As a result, they were confirmed to yield superior convergence compared to commonly used one-hot encoding. PyAPX is broadly applicable to crystalline materials and is expected to further advance materials discovery....

---

### 16. Hyperbolic Dispersion and Low-Frequency Plasmons in Electrides

**Authors:** Qi-Dong Hao, Hao Wang, Hong-Xing Song, Xiang-Rong Chen, Hua Y. Geng

**Published:** 2025-11-22

**Category:** physics.optics

**ID:** 2511.17859v1

**Link:** [http://arxiv.org/abs/2511.17859v1](http://arxiv.org/abs/2511.17859v1)

**Summary:** Natural hyperbolic materials have attracted significant interest in the field of photonics due to their unique optical properties. Based on the initial successful explorations on layered crystalline materials, hyperbolic dispersion was associated with extreme structural anisotropy, despite the rarity of natural materials exhibiting this property. Here we show that non cubic electrides are generally promising natural hyperbolic materials owing to charge localization in interstitial sites. This includes elemental and binary electrides, as well as some two-dimensional materials that show prominent in-plane hyperbolic dispersion. They exhibit low plasma frequencies and a broad hyperbolic window spanning the infrared to the ultraviolet. In semiconductor electrides, anisotropic interband transitions provide an additional mechanism for hyperbolic behaviour. These findings remove the previously held prerequisite of structural anisotropy for natural hyperbolic materials, and open up new opportunities, which might change the current strategy for searching and design photonic materials....

---

### 17. Towards a deeper fundamental understanding of (Al,Sc)N ferroelectric nitrides

**Authors:** Peng Chen, Dawei Wang, Alejandro Mercado Tejerina, Keisuke Yazawa, Andriy Zakutayev, Charles Paillard, Laurent Bellaiche

**Published:** 2025-09-18

**Category:** cond-mat.mtrl-sci

**ID:** 2509.15050v3

**Link:** [http://arxiv.org/abs/2509.15050v3](http://arxiv.org/abs/2509.15050v3)

**Summary:** Density Functional Theory (DFT) calculations, within the virtual crystal alloy approximation, are performed, along with the development of a Landau-type model employing a symmetry-allowed analytical expression of the internal energy and having parameters being determined from first principles, to investigate properties and energetics of Al1-xScxN ferroelectric nitrides in their hexagonal forms. These DFT computations and this model predict the existence of two different types of minima, namely the 4-fold-coordinated wurtzite (WZ) polar structure and a 5-times paraelectric hexagonal phase (to be denoted as H5), for any Sc composition up to 40%. The H5 minimum progressively becomes the lowest energy state within hexagonal symmetry as the Sc concentration increases from 0 to 40%. Furthermore, the model points out to several key findings. Examples include the crucial role of the coupling between polarization and strains to create the WZ minimum, in addition to polar and elastic energies, and that the origin of the H5 state overcoming the WZ phase as the global minimum within hexagonal symmetry when increasing the Sc composition mostly lies in the compositional dependency of only two parameters, one linked to the polarization and another one being purely elastic in nature. Other examples are that forcing Al1-xScxN systems to have no or a weak change in lattice parameters when heating them allows to reproduce well their finite-temperature polar properties, and that a value of the axial ratio close to that of the ideal WZ structure does imply a large polarization at low temperatures but not necessarily at high temperatures because of the ordered-disordered character of the temperature-induced formation of the WZ state. Such findings should allow for a better fundamental understanding of (Al,Sc)N ferroelectric nitrides, which may be used to design efficient devices operating at low voltages....

---

### 18. When Active Learning Fails, Uncalibrated Out of Distribution Uncertainty Quantification Might Be the Problem

**Authors:** Ashley S. Dale, Kangming Li, Brian DeCost, Hao Wan, Yuchen Han, Yao Fehlis, Jason Hattrick-Simpers

**Published:** 2025-11-21

**Category:** cond-mat.mtrl-sci

**ID:** 2511.17760v1

**Link:** [http://arxiv.org/abs/2511.17760v1](http://arxiv.org/abs/2511.17760v1)

**Summary:** Efficiently and meaningfully estimating prediction uncertainty is important for exploration in active learning campaigns in materials discovery, where samples with high uncertainty are interpreted as containing information missing from the model. In this work, the effect of different uncertainty estimation and calibration methods are evaluated for active learning when using ensembles of ALIGNN, eXtreme Gradient Boost, Random Forest, and Neural Network model architectures. We compare uncertainty estimates from ALIGNN deep ensembles to loss landscape uncertainty estimates obtained for solubility, bandgap, and formation energy prediction tasks. We then evaluate how the quality of the uncertainty estimate impacts an active learning campaign that seeks model generalization to out-of-distribution data. Uncertainty calibration methods were found to variably generalize from in-domain data to out-of-domain data. Furthermore, calibrated uncertainties were generally unsuccessful in reducing the amount of data required by a model to improve during an active learning campaign on out-of-distribution data when compared to random sampling and uncalibrated uncertainties. The impact of poor-quality uncertainty persists for random forest and eXtreme Gradient Boosting models trained on the same data for the same tasks, indicating that this is at least partially intrinsic to the data and not due to model capacity alone. Analysis of the target, in-distribution uncertainty, out-of-distribution uncertainty, and training residual distributions suggest that future work focus on understanding empirical uncertainties in the feature input space for cases where ensemble prediction variances do not accurately capture the missing information required for the model to generalize....

---


<!-- ARXIV_PAPERS_END -->