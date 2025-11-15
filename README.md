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

## New Papers (377)

*Last updated: 2025-11-16 06:13:46 (SGT)*

### 1. Probing the Liquid Solid Interfaces of 2D SnSe MXene Battery Anodes at the Nanoscale

**Authors:** Lukas Worch, Kavin Arunasalam, Neil Mulcahy, Syeda Ramin Jannat, James Douglas, Baptiste Gault, Valeria Nicolosi, Michele Shelly Conroy

**Published:** 2025-11-13

**Category:** cond-mat.mtrl-sci

**ID:** 2511.10278v1

**Link:** [http://arxiv.org/abs/2511.10278v1](http://arxiv.org/abs/2511.10278v1)

**Summary:** Understanding degradation processes in lithium ion batteries is essential for improving long term performance and advancing sustainable energy technologies. Tin selenide (SnSe) has emerged as a promising anode material due to the high theoretical capacity of tin. Unlike conventional intercalation based electrodes, SnSe undergoes conversion and alloying reactions with lithium to form Li4.4Sn, Sn, and Li2Se, enabling high lithium storage but inducing large volume changes that cause mechanical instability and capacity fading. Embedding SnSe nanoparticles within a Ti3C2Tx MXene framework offers a strategy to mitigate these effects by enhancing conductivity and structural resilience. Here, cryogenic focused ion beam (cryo FIB) slice and view revealed progressive material redistribution and morphological transformation during cycling, underscoring the need for site specific chemical analysis. Cryogenic atom probe tomography (cryo APT) of selected regions provided high spatial and chemical resolution while preserving beam sensitive phases, uncovering nanoscale degradation mechanisms including phase transformations, partial dissolution of active material, and, importantly, the first direct evidence of copper corrosion and copper ion migration from the current collector into the electrode. The observation of copper redistribution demonstrates that current collector degradation contributes directly to chemical contamination and capacity fading in composite electrodes. Together, cryo FIB and cryo APT provide a powerful workflow for elucidating electrode degradation in reactive, beam sensitive systems, offering critical insights for designing more durable and stable next generation battery materials....

---

### 2. Energy Underprediction from Symmetry in Machine-Learning Interatomic Potentials

**Authors:** Wei Nong, Ruiming Zhu, Zekun Ren, Martin Hoffmann Petersen, Shuya Yamazaki, Nikita Kazeev, Andrey Ustyuzhanin, Gang Wu, Shuo-Wang Yang, Kedar Hippalgaonkar

**Published:** 2025-07-21

**Category:** cond-mat.mtrl-sci

**ID:** 2507.15190v2

**Link:** [http://arxiv.org/abs/2507.15190v2](http://arxiv.org/abs/2507.15190v2)

**Summary:** Machine learning interatomic potentials (MLIAPs) have emerged as powerful tools for accelerating materials simulations with near-density functional theory (DFT) accuracy. However, despite significant advances, we identify a critical yet overlooked issue undermining their reliability: a systematic energy underprediction. This problem becomes starkly evident in large-scale thermodynamic stability assessments. By performing over 12 million calculations using nine MLIAPs for over 150,000 inorganic crystals in the Materials Project, we demonstrate that most frontier models consistently underpredict energy above hull (Ehull), a key metric for thermodynamic stability, total energy, and formation energy, despite the fact that over 90\% of test structures (DFT-relaxed) are in the training data. The mean absolute errors (MAE) for Ehull exceed ~30 meV/atom even by the best model, directly challenging claims of achieving ``DFT accuracy'' for property predictions central to materials discovery, especially related to (meta-)stability. Crucially, we trace this underprediction to insufficient handling of symmetry degrees of freedom (DOF), constituting both lattice symmetry and Wyckoff site symmetries for the space group. MLIAPs exhibit pronounced errors (MAE for Ehull $>$ ~40 meV/atom) in structures with high symmetry DOF, where subtle atomic displacements significantly impact energy landscapes. Further analysis also indicates that the MLIAPs show severe energy underprediction for a large proportion of near-hull materials. We argue for improvements on symmetry-aware models such as explicit DOF encoding or symmetry-regularized loss functions, and more robust MLIAPs for predicting crystal properties where the preservation and breaking of symmetry are pivotal....

---

### 3. MicroLad: 2D-to-3D Microstructure Reconstruction and Generation via Latent Diffusion and Score Distillation

**Authors:** Kang-Hyun Lee, Faez Ahmed

**Published:** 2025-08-27

**Category:** cond-mat.mtrl-sci

**ID:** 2508.20138v4

**Link:** [http://arxiv.org/abs/2508.20138v4](http://arxiv.org/abs/2508.20138v4)

**Summary:** A major obstacle to establishing reliable structure-property (SP) linkages in materials engineering is the scarcity of diverse 3D microstructure datasets. Limited dataset availability and insufficient control over the analysis and design space restrict the variety of achievable microstructure morphologies, hindering progress in solving the inverse (property-to-structure) design problem. To address these challenges, we introduce MicroLad, a latent diffusion framework specifically designed for reconstructing 3D microstructures from 2D data. Trained on 2D images and employing multi-plane denoising diffusion sampling in the latent space, the framework reliably generates stable and coherent 3D volumes that remain statistically consistent with the original data. While this reconstruction capability enables dimensionality expansion (2D-to-3D) for generating statistically equivalent 3D samples from 2D data, effective exploration of microstructure design requires methods to guide the generation process toward specific objectives. To achieve this, MicroLad integrates score distillation sampling (SDS), which combines a differentiable score loss with microstructural descriptor-matching and property-alignment terms. This approach updates encoded 2D slices of the 3D volume in the latent space, enabling robust inverse-controlled 2D-to-3D microstructure generation. Consequently, the method facilitates exploration of an expanded 3D microstructure analysis and design space in terms of both microstructural descriptors and material properties....

---

### 4. Engineering stacking-induced topological phase transitions in bilayer heterostructures

**Authors:** Arjyama Bordoloi, Daniel Kaplan, Sobhit Singh

**Published:** 2025-04-29

**Category:** cond-mat.mes-hall

**ID:** 2504.21126v2

**Link:** [http://arxiv.org/abs/2504.21126v2](http://arxiv.org/abs/2504.21126v2)

**Summary:** Nonmagnetic topological insulators (TIs) are known for their robust metallic surface/edge states that are protected by time-reversal symmetry, making them promising candidates for next-generation spintronic and nanoelectronic devices. Traditional approaches to realizing TIs have focused on inducing band inversion via strong spin-orbit coupling (SOC), yet many materials with substantial SOC often remain topologically trivial. In this work, we present a materials-design strategy for engineering topologically non-trivial phases, e.g., quantum spin Hall phases, by vertically stacking topologically trivial Rashba monolayers in an inverted fashion. Using BiSb as a prototype system, we demonstrate that while the BiSb monolayer is topologically trivial (despite having significant SOC), an inverted BiSb-SbBi bilayer configuration realizes a non-trivial topological phase with enhanced spin Hall conductivity. We further reveal a delicate interplay between the SOC strength and the interlayer electron tunneling that governs the emergence of a nontrivial topological phase in the bilayer heterostructure. This phase can be systematically tuned using an external electric field, providing an experimentally accessible means of controlling the system's topology. Our magnetotransport studies further validate this interplay, by revealing $g$-factor suppression and the emergence a zeroth Landau level. Notably, the inverted bilayer heterostructure exhibits a robust and tunable spin Hall effect, with performance comparable to that of state-of-the-art materials. Thus, our findings unveil an alternative pathway for designing and engineering functional properties in 2D topological systems using topologically trivial constituent monolayers....

---

### 5. Beyond empirical models: Discovering new constitutive laws in solids with graph-based equation discovery

**Authors:** Hao Xu, Yuntian Chen, Dongxiao Zhang

**Published:** 2025-11-13

**Category:** cond-mat.mtrl-sci

**ID:** 2511.09906v1

**Link:** [http://arxiv.org/abs/2511.09906v1](http://arxiv.org/abs/2511.09906v1)

**Summary:** Constitutive models are fundamental to solid mechanics and materials science, underpinning the quantitative description and prediction of material responses under diverse loading conditions. Traditional phenomenological models, which are derived through empirical fitting, often lack generalizability and rely heavily on expert intuition and predefined functional forms. In this work, we propose a graph-based equation discovery framework for the automated discovery of constitutive laws directly from multisource experimental data. This framework expresses equations as directed graphs, where nodes represent operators and variables, edges denote computational relations, and edge features encode parametric dependencies. This enables the generation and optimization of free-form symbolic expressions with undetermined material-specific parameters. Through the proposed framework, we have discovered new constitutive models for strain-rate effects in alloy steel materials and the deformation behavior of lithium metal. Compared with conventional empirical models, these new models exhibit compact analytical structures and achieve higher accuracy. The proposed graph-based equation discovery framework provides a generalizable and interpretable approach for data-driven scientific modelling, particularly in contexts where traditional empirical formulations are inadequate for representing complex physical phenomena....

---

### 6. Structure of Antiphase boundaries in Ni-M-Ga: multiscale modelling

**Authors:** Jan Zemen, František Máca, Václav Drchal, Martin Veis, Oleg Heczko

**Published:** 2025-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2511.09751v1

**Link:** [http://arxiv.org/abs/2511.09751v1](http://arxiv.org/abs/2511.09751v1)

**Summary:** Antiphase boundaries (APBs) are ubiquitous in ordered Heusler alloys and strongly influence magnetic coercivity in Ni-Mn-Ga, yet the link between their atomic-scale exchange interactions and micrometer-scale magnetic contrast measured by magnetic force microscopy (MFM) remains unclear. We combine density functional theory (DFT) and finite-element magnetostatics to bridge these scales in Ni-Mn-Ga. DFT calculations on supercells containing planar APBs show that the lowest-energy configuration comprises a pair of parallel APBs enclosing a nanoscale region - only three Mn-Ga atomic layers thick - whose magnetization is antiparallel to the surrounding matrix due to strong antiferromagnetic exchange across each APB (in contrast to ferromagnetic coupling in bulk martensite). According to our magnetostatic finite element model, this thin region with antiparallel magnetization generates the characteristic MFM contrast extending approx. 100 nm from the APB pair. When the APBs are further apart than 50 nm, dipole-dipole penalties outweigh exchange gains, preventing formation of an extended antiparallel domain, in agreement with experimental evidence. These results identify APB pairs as the origin of the observed MFM contrast and offer an interpretation of the modest strengths of domain-wall pinning by APBs, informing the design of magnetic shape-memory alloys with tailored coercivity....

---

### 7. A Fourier-Based Global Denoising Model for Smart Artifacts Removing of Microscopy Images

**Authors:** Huanhuan Zhao, Connor Vernachio, Laxmi Bhurtel, Wooin Yang, Ruben Millan-Solsona, Spenser R. Brown, Marti Checa, Komal Sharma Agrawal, Adam M. Guss, Liam Collins, Wonhee Ko, Arpan Biswas

**Published:** 2025-11-12

**Category:** eess.IV

**ID:** 2511.09734v1

**Link:** [http://arxiv.org/abs/2511.09734v1](http://arxiv.org/abs/2511.09734v1)

**Summary:** Microscopy such as Scanning Tunneling Microscopy (STM), Atomic Force Microscopy (AFM) and Scanning Electron Microscopy (SEM) are essential tools in material imaging at micro- and nanoscale resolutions to extract physical knowledge and materials structure-property relationships. However, tuning microscopy controls (e.g. scanning speed, current setpoint, tip bias etc.) to obtain a high-quality of images is a non-trivial and time-consuming effort. On the other hand, with sub-standard images, the key features are not accurately discovered due to noise and artifacts, leading to erroneous analysis. Existing denoising models mostly build on generalizing the weak signals as noises while the strong signals are enhanced as key features, which is not always the case in microscopy images, thus can completely erase a significant amount of hidden physical information. To address these limitations, we propose a global denoising model (GDM) to smartly remove artifacts of microscopy images while preserving weaker but physically important features. The proposed model is developed based on 1) first designing a two-imaging input channel of non-pair and goal specific pre-processed images with user-defined trade-off information between two channels and 2) then integrating a loss function of pixel- and fast Fourier-transformed (FFT) based on training the U-net model. We compared the proposed GDM with the non-FFT denoising model over STM-generated images of Copper(Cu) and Silicon(Si) materials, AFM-generated Pantoea sp.YR343 bio-film images and SEM-generated plastic degradation images. We believe this proposed workflow can be extended to improve other microscopy image quality and will benefit the experimentalists with the proposed design flexibility to smartly tune via domain-experts preferences....

---

### 8. pH Regulates Ion Dynamics in Carboxylated Mixed Conductors

**Authors:** Zeyuan Sun, Mengting Sun, Rajiv Giridharagopal, Robert C. Hamburger, Siyu Qin, Haoxuan Li, Mitchell C. Hausback, Yulong Zheng, Bohyeon Kim, Heng Tan, Thomas E. Gartner, Elizabeth R. Young, Christopher J Takacs, David S. Ginger, Elsa Reichmanis

**Published:** 2025-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2511.09671v1

**Link:** [http://arxiv.org/abs/2511.09671v1](http://arxiv.org/abs/2511.09671v1)

**Summary:** Coupled ionic and electronic transport underpins processes as diverse as electrochemical energy conversion, biological signaling, and soft adaptive electronics. Yet, how chemical environments such as pH modulate this coupling at the molecular scale remains poorly understood. Here, we show that the protonation state of carboxylated polythiophenes provides precise chemical control over ion dynamics, doping efficiency, solvent uptake and mechanical response. The findings establish molecular acidity as a general strategy to program ionic preference and mechanical stability, offering design principles for pH-responsive mixed conductors and soft electronic materials that couple ionic, electronic, and mechanical functionality....

---

### 9. DensiCrafter: Physically-Constrained Generation and Fabrication of Self-Supporting Hollow Structures

**Authors:** Shengqi Dang, Fu Chai, Jiaxin Li, Chao Yuan, Wei Ye, Nan Cao

**Published:** 2025-11-12

**Category:** cs.CV

**ID:** 2511.09298v1

**Link:** [http://arxiv.org/abs/2511.09298v1](http://arxiv.org/abs/2511.09298v1)

**Summary:** The rise of 3D generative models has enabled automatic 3D geometry and texture synthesis from multimodal inputs (e.g., text or images). However, these methods often ignore physical constraints and manufacturability considerations. In this work, we address the challenge of producing 3D designs that are both lightweight and self-supporting. We present DensiCrafter, a framework for generating lightweight, self-supporting 3D hollow structures by optimizing the density field. Starting from coarse voxel grids produced by Trellis, we interpret these as continuous density fields to optimize and introduce three differentiable, physically constrained, and simulation-free loss terms. Additionally, a mass regularization penalizes unnecessary material, while a restricted optimization domain preserves the outer surface. Our method seamlessly integrates with pretrained Trellis-based models (e.g., Trellis, DSO) without any architectural changes. In extensive evaluations, we achieve up to 43% reduction in material mass on the text-to-3D task. Compared to state-of-the-art baselines, our method could improve the stability and maintain high geometric fidelity. Real-world 3D-printing experiments confirm that our hollow designs can be reliably fabricated and could be self-supporting....

---

### 10. Hydrogen permeability prediction in palladium alloys and virtual screening of B2-phase stabilized Pd(100-x-y)CuxMy ternary alloys using machine learning

**Authors:** Eric Kolor, Edoardo Magnone, Muhammad Harussani Moklis, Md. Rubel, Sasipa Boonyubol, Koichi Mikami, Jeffrey S. Cross

**Published:** 2025-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2511.09245v1

**Link:** [http://arxiv.org/abs/2511.09245v1](http://arxiv.org/abs/2511.09245v1)

**Summary:** We present a forward prediction material screening framework designed to discover Pd-Cu alloys with improved B2 phase stability, thereby unlocking simultaneous $H_2$ generation and utilization. First, we trained CatBoost models with literature-derived Pd alloy data to predict $H_2$ permeability from composition and testing conditions. We evaluated fractional, composition-based, and physics-informed descriptors, individually and in combination, and showed that sequential Pearson filtering and fold-wise SHAP-based recursive feature elimination with cross-fold aggregation reduced errors while controlling complexity. Guided by the one-SE rule, a narrower domain-informed set of 13 features provided the best accuracy parsimony trade-off ($R^2=0.81$), only 0.01 below the max. $R^2$ achievable with 3x the number of features. SHAP analysis indicated that high permeability is promoted by elevated temperature, lattice expansion relative to Pd, atomic size mismatch, and favorable mixing tendencies. Second, the selected model was applied to screen $Pd_{(100-x-y)}Cu_{x}M_{y}$ spanning 16 co-dopants M for B2 stabilization. For each M system, we obtained the Pareto set of compositions that minimize Pd content and Miedema heat of formation and maximize the permeability, then picked three compounds, including that with the highest predicted permeability, the lowest Miedema heat of formation, and the lowest Pd content. With a final filter considering M concentration for single-phase Pd-M solution formation, we recommend Pd48.48Cu43.00Y8.52, Pd49.08Cu42.45Sc8.47, Pd56.09Cu33.70La10.21, and Pd52.68Cu40.44Mg6.88 for experimental validation. We predict those alloys to exhibit permeabilities 1.7 to 1.9 higher than B2 Pd60Cu40. Our framework provides plausible experimental targets and a scalable pathway for designing stable, high-temperature, H2-selective Pd-alloy membranes....

---

### 11. Assessing Band Gap Stability of Organic Semiconductor Thin Films for Flexible Electronic Applications

**Authors:** Mahya Ghorab, Ayush K. Ranga, Arnulf Materny, Veit Wagner, Mojtaba Joodaki

**Published:** 2025-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2511.09226v1

**Link:** [http://arxiv.org/abs/2511.09226v1](http://arxiv.org/abs/2511.09226v1)

**Summary:** Integration of organic semiconductors into flexible electronics requires that their optoelectronic properties remain stable under mechanical deformation. Among these, the optical band gap governs exciton generation and limits photovoltaic voltage, making it a key parameter for strain-resilient design. In this work, we investigate band gap shifts in poly(3-hexylthiophene-2,5-diyl) (P3HT) and poly(3,4-ethylenedioxythiophene):poly(styrenesulfonate) (PEDOT:PSS)/P3HT thin films deposited on flexible poly(ethylene terephthalate) (PET) substrates under uniaxial tensile strain ranging from 1\% to 10\%. Samples were subjected to mechanical deformation and then characterized by ultraviolet--visible (UV--Vis) absorption spectroscopy. The optical band gaps extracted using a standardized Tauc analysis and statistically validated through equivalence testing and robust regression models. We find that up to 7\% strain, the band gap shift ($ΔE_g$) remains effectively invariant, independent of annealing condition or stack configuration, demonstrating electronic stability. However, at 10\% strain, all groups exhibit a reproducible widening of $\sim$4--5~meV. This threshold-like behavior marks a transition from mechanical accommodation to electronic perturbation. These findings confirm that the optical band gap in semicrystalline P3HT-based thin films is robust under practical deformation, which provides clear strain thresholds to inform mechanical modeling and device-level simulation of flexible organic optoelectronic systems....

---

### 12. CrystalFormer-RL: Reinforcement Fine-Tuning for Materials Design

**Authors:** Zhendong Cao, Lei Wang

**Published:** 2025-04-03

**Category:** cond-mat.mtrl-sci

**ID:** 2504.02367v2

**Link:** [http://arxiv.org/abs/2504.02367v2](http://arxiv.org/abs/2504.02367v2)

**Summary:** Reinforcement fine-tuning played an instrumental role in enhancing the instruction-following and reasoning abilities of large language models. In this work, we employ reinforcement fine-tuning for materials design, in which discriminative machine learning models are used to provide rewards to the autoregressive transformer-based materials generative model CrystalFormer. By optimizing the reward signals-such as energy above the convex hull and material properties figures of merit-reinforcement fine-tuning infuses knowledge from discriminative models into generative models. The resulting model, CrystalFormer-RL, shows enhanced stability in generated crystals and successfully discovers crystals with desirable yet conflicting material properties, such as substantial dielectric constant and band gap simultaneously. Notably, we observe that reinforcement fine-tuning not only enables the property-guided material design but also unlocks property-based material retrieval behavior of pretrained generative model. The present framework opens an exciting gateway to the synergies of the machine learning ecosystem for materials design....

---

### 13. Phonon-Dominated Thermal Transport and Large Violation of the Wiedemann-Franz Law in Topological Semimetal CoSi

**Authors:** Luyao Zhong, Xin Jin, Mingquan He, Rui Wang, Xiaoyuan Zhou, Tianqi Deng, Xiaolong Yang

**Published:** 2025-11-09

**Category:** cond-mat.mtrl-sci

**ID:** 2511.06290v2

**Link:** [http://arxiv.org/abs/2511.06290v2](http://arxiv.org/abs/2511.06290v2)

**Summary:** The Wiedemann-Franz (WF) law, relating the electronic thermal conductivity ($κ_{\rm e}$) to the electrical conductivity, is vital in numerous applications such as in the design of thermoelectric materials and in the experimental determination of the lattice thermal conductivity ($κ_{\rm L}$). While the WF law is generally robust, violations are frequently observed, typically manifesting in a reduced Lorenz number ($L$) relative to the Sommerfeld value ($L_0$) due to inelastic scattering. Here, we report a pronounced departure from the WF law in the topological semimetal CoSi, where the electronic Lorenz number ($L_{\rm e}$) instead rises up to $\sim40\%$ above $L_0$. We demonstrate that this anomaly arises from strong bipolar diffusive transport, enabled by topological band-induced electron-hole compensation, which allows electrons and holes to flow cooperatively and additively enhance the heat current. Concurrently, we unveil that the lattice contribution to thermal conductivity is anomalously large and becomes the dominant component below room temperature. As a result, if $κ_{\rm L}$ is assumed negligible -- as conventional in metals, the resulting $L$ from the total thermal conductivity ($κ_{\rm tot}=κ_{\rm L}+κ_{\rm e}$) deviates from $L_0$ by more than a factor of three. Our work provides deeper insight into the unconventional thermal transport physics in topological semimetals....

---

### 14. MicroEvoEval: A Systematic Evaluation Framework for Image-Based Microstructure Evolution Prediction

**Authors:** Qinyi Zhang, Duanyu Feng, Ronghui Han, Yangshuai Wang, Hao Wang

**Published:** 2025-11-12

**Category:** cond-mat.mtrl-sci

**ID:** 2511.08955v1

**Link:** [http://arxiv.org/abs/2511.08955v1](http://arxiv.org/abs/2511.08955v1)

**Summary:** Simulating microstructure evolution (MicroEvo) is vital for materials design but demands high numerical accuracy, efficiency, and physical fidelity. Although recent studies on deep learning (DL) offer a promising alternative to traditional solvers, the field lacks standardized benchmarks. Existing studies are flawed due to a lack of comparing specialized MicroEvo DL models with state-of-the-art spatio-temporal architectures, an overemphasis on numerical accuracy over physical fidelity, and a failure to analyze error propagation over time. To address these gaps, we introduce MicroEvoEval, the first comprehensive benchmark for image-based microstructure evolution prediction. We evaluate 14 models, encompassing both domain-specific and general-purpose architectures, across four representative MicroEvo tasks with datasets specifically structured for both short- and long-term assessment. Our multi-faceted evaluation framework goes beyond numerical accuracy and computational cost, incorporating a curated set of structure-preserving metrics to assess physical fidelity. Our extensive evaluations yield several key insights. Notably, we find that modern architectures (e.g., VMamba), not only achieve superior long-term stability and physical fidelity but also operate with an order-of-magnitude greater computational efficiency. The results highlight the necessity of holistic evaluation and identify these modern architectures as a highly promising direction for developing efficient and reliable surrogate models in data-driven materials science....

---

### 15. Material-Based Intelligence: Self-organizing, Autonomous and Adaptive Cognition Embodied in Physical Substrates

**Authors:** Vladimir A. Baulin, Rudolf M. Füchslin, Achille Giacometti, Helmut Hauser, Marco Werner

**Published:** 2025-11-11

**Category:** cond-mat.soft

**ID:** 2511.08838v1

**Link:** [http://arxiv.org/abs/2511.08838v1](http://arxiv.org/abs/2511.08838v1)

**Summary:** The design of intelligent materials often draws parallels with the complex adaptive behaviors of biological organisms, where robust functionality stems from sophisticated hierarchical organization and emergent long-distance coordination among a myriad local components. Current synthetic materials, despite integrating advanced sensors and actuators, predominantly demonstrate only simple, pre-programmed stimulus-response functionalities, falling short of robustly autonomous intelligent behavior. These systems typically execute tasks determined by rigid design or external control, fundamentally lacking the intricate internal feedback loops, dynamic adaptation, self-generated learning, and genuine self-determination characteristic of biological agents. This perspective proposes a fundamentally different approach focusing on architectures where material-based intelligence is not pre-designed, but arises spontaneously from self-organization harnessing far-from-equilibrium dynamics. This work explores interdisciplinary concepts from material physics, chemistry, biology, and computation, identifying concrete pathways toward developing materials that not only react, but actively perceive, adapt, learn, self-correct, and potentially self-construct, moving beyond biomimicry to cultivate fully synthetic, self-evolving systems without external control. This framework outlines the fundamental requirements for, and constraints upon, future architectures where complex, goal-directed functionalities emerge synergistically from integrated local processes, distinguishing material-based intelligence from traditional hardware-software divisions. This demands that concepts of high-level goals and robust, replicable memory mechanisms are encoded and enacted through the material's inherent dynamics, inherently blurring the distinction between system output and process....

---

### 16. Generative AI Meets 6G and Beyond: Diffusion Models for Semantic Communications

**Authors:** Hai-Long Qin, Jincheng Dai, Guo Lu, Shuo Shao, Sixian Wang, Tongda Xu, Wenjun Zhang, Ping Zhang, Khaled B. Letaief

**Published:** 2025-11-11

**Category:** eess.SP

**ID:** 2511.08416v1

**Link:** [http://arxiv.org/abs/2511.08416v1](http://arxiv.org/abs/2511.08416v1)

**Summary:** Semantic communications mark a paradigm shift from bit-accurate transmission toward meaning-centric communication, essential as wireless systems approach theoretical capacity limits. The emergence of generative AI has catalyzed generative semantic communications, where receivers reconstruct content from minimal semantic cues by leveraging learned priors. Among generative approaches, diffusion models stand out for their superior generation quality, stable training dynamics, and rigorous theoretical foundations. However, the field currently lacks systematic guidance connecting diffusion techniques to communication system design, forcing researchers to navigate disparate literatures. This article provides the first comprehensive tutorial on diffusion models for generative semantic communications. We present score-based diffusion foundations and systematically review three technical pillars: conditional diffusion for controllable generation, efficient diffusion for accelerated inference, and generalized diffusion for cross-domain adaptation. In addition, we introduce an inverse problem perspective that reformulates semantic decoding as posterior inference, bridging semantic communications with computational imaging. Through analysis of human-centric, machine-centric, and agent-centric scenarios, we illustrate how diffusion models enable extreme compression while maintaining semantic fidelity and robustness. By bridging generative AI innovations with communication system design, this article aims to establish diffusion models as foundational components of next-generation wireless networks and beyond....

---

### 17. Revealing the Hidden Third Dimension of Point Defects in Two-Dimensional MXenes

**Authors:** Grace Guinan, Michelle A. Smeaton, Brian C. Wyatt, Steven Goldy, Hilary Egan, Andrew Glaws, Garritt J. Tucker, Babak Anasori, Steven R. Spurgeon

**Published:** 2025-11-11

**Category:** cond-mat.mtrl-sci

**ID:** 2511.08350v1

**Link:** [http://arxiv.org/abs/2511.08350v1](http://arxiv.org/abs/2511.08350v1)

**Summary:** Point defects govern many important functional properties of two-dimensional (2D) materials. However, resolving the three-dimensional (3D) arrangement of these defects in multi-layer 2D materials remains a fundamental challenge, hindering rational defect engineering. Here, we overcome this limitation using an artificial intelligence-guided electron microscopy workflow to map the 3D topology and clustering of atomic vacancies in Ti$_3$C$_2$T$_X$ MXene. Our approach reconstructs the 3D coordinates of vacancies across hundreds of thousands of lattice sites, generating robust statistical insight into their distribution that can be correlated with specific synthesis pathways. This large-scale data enables us to classify a hierarchy of defect structures--from isolated vacancies to nanopores--revealing their preferred formation and interaction mechanisms, as corroborated by molecular dynamics simulations. This work provides a generalizable framework for understanding and ultimately controlling point defects across large volumes, paving the way for the rational design of defect-engineered functional 2D materials....

---

### 18. Beyond Distributions: Geometric Action Control for Continuous Reinforcement Learning

**Authors:** Zhihao Lin

**Published:** 2025-11-11

**Category:** cs.AI

**ID:** 2511.08234v1

**Link:** [http://arxiv.org/abs/2511.08234v1](http://arxiv.org/abs/2511.08234v1)

**Summary:** Gaussian policies have dominated continuous control in deep reinforcement learning (RL), yet they suffer from a fundamental mismatch: their unbounded support requires ad-hoc squashing functions that distort the geometry of bounded action spaces. While von Mises-Fisher (vMF) distributions offer a theoretically grounded alternative on the sphere, their reliance on Bessel functions and rejection sampling hinders practical adoption. We propose \textbf{Geometric Action Control (GAC)}, a novel action generation paradigm that preserves the geometric benefits of spherical distributions while \textit{simplifying computation}. GAC decomposes action generation into a direction vector and a learnable concentration parameter, enabling efficient interpolation between deterministic actions and uniform spherical noise. This design reduces parameter count from \(2d\) to \(d+1\), and avoids the \(O(dk)\) complexity of vMF rejection sampling, achieving simple \(O(d)\) operations. Empirically, GAC consistently matches or exceeds state-of-the-art methods across six MuJoCo benchmarks, achieving 37.6\% improvement over SAC on Ant-v4 and the best results on 4 out of 6 tasks. Our ablation studies reveal that both \textbf{spherical normalization} and \textbf{adaptive concentration control} are essential to GAC's success. These findings suggest that robust and efficient continuous control does not require complex distributions, but a principled respect for the geometry of action spaces. Code and pretrained models are available in supplementary materials....

---

### 19. Radar-APLANC: Unsupervised Radar-based Heartbeat Sensing via Augmented Pseudo-Label and Noise Contrast

**Authors:** Ying Wang, Zhaodong Sun, Xu Cheng, Zuxian He, Xiaobai Li

**Published:** 2025-11-11

**Category:** cs.CV

**ID:** 2511.08071v1

**Link:** [http://arxiv.org/abs/2511.08071v1](http://arxiv.org/abs/2511.08071v1)

**Summary:** Frequency Modulated Continuous Wave (FMCW) radars can measure subtle chest wall oscillations to enable non-contact heartbeat sensing. However, traditional radar-based heartbeat sensing methods face performance degradation due to noise. Learning-based radar methods achieve better noise robustness but require costly labeled signals for supervised training. To overcome these limitations, we propose the first unsupervised framework for radar-based heartbeat sensing via Augmented Pseudo-Label and Noise Contrast (Radar-APLANC). We propose to use both the heartbeat range and noise range within the radar range matrix to construct the positive and negative samples, respectively, for improved noise robustness. Our Noise-Contrastive Triplet (NCT) loss only utilizes positive samples, negative samples, and pseudo-label signals generated by the traditional radar method, thereby avoiding dependence on expensive ground-truth physiological signals. We further design a pseudo-label augmentation approach featuring adaptive noise-aware label selection to improve pseudo-label signal quality. Extensive experiments on the Equipleth dataset and our collected radar dataset demonstrate that our unsupervised method achieves performance comparable to state-of-the-art supervised methods. Our code, dataset, and supplementary materials can be accessed from https://github.com/RadarHRSensing/Radar-APLANC....

---

### 20. ElastoGen: 4D Generative Elastodynamics

**Authors:** Yutao Feng, Yintong Shang, Xiang Feng, Lei Lan, Shandian Zhe, Tianjia Shao, Hongzhi Wu, Kun Zhou, Chenfanfu Jiang, Yin Yang

**Published:** 2024-05-23

**Category:** cs.LG

**ID:** 2405.15056v3

**Link:** [http://arxiv.org/abs/2405.15056v3](http://arxiv.org/abs/2405.15056v3)

**Summary:** We present ElastoGen, a knowledge-driven AI model that generates physically accurate 4D elastodynamics. Unlike deep models that learn from video- or image-based observations, ElastoGen leverages the principles of physics and learns from established mathematical and optimization procedures. The core idea of ElastoGen is converting the differential equation, corresponding to the nonlinear force equilibrium, into a series of iterative local convolution-like operations, which naturally fit deep architectures. We carefully build our network module following this overarching design philosophy. ElastoGen is much more lightweight in terms of both training requirements and network scale than deep generative models. Because of its alignment with actual physical procedures, ElastoGen efficiently generates accurate dynamics for a wide range of hyperelastic materials and can be easily integrated with upstream and downstream deep modules to enable end-to-end 4D generation....

---

### 21. Guiding Generative Models to Uncover Diverse and Novel Crystals via Reinforcement Learning

**Authors:** Hyunsoo Park, Aron Walsh

**Published:** 2025-11-10

**Category:** cs.LG

**ID:** 2511.07158v1

**Link:** [http://arxiv.org/abs/2511.07158v1](http://arxiv.org/abs/2511.07158v1)

**Summary:** Discovering functional crystalline materials entails navigating an immense combinatorial design space. While recent advances in generative artificial intelligence have enabled the sampling of chemically plausible compositions and structures, a fundamental challenge remains: the objective misalignment between likelihood-based sampling in generative modelling and targeted focus on underexplored regions where novel compounds reside. Here, we introduce a reinforcement learning framework that guides latent denoising diffusion models toward diverse and novel, yet thermodynamically viable crystalline compounds. Our approach integrates group relative policy optimisation with verifiable, multi-objective rewards that jointly balance creativity, stability, and diversity. Beyond de novo generation, we demonstrate enhanced property-guided design that preserves chemical validity, while targeting desired functional properties. This approach establishes a modular foundation for controllable AI-driven inverse design that addresses the novelty-validity trade-off across scientific discovery applications of generative models....

---

### 22. Rethinking Crystal Symmetry Prediction: A Decoupled Perspective

**Authors:** Liheng Yu, Zhe Zhao, Xucong Wang, Di Wu, Pengkun Wang

**Published:** 2025-11-10

**Category:** cs.LG

**ID:** 2511.06976v1

**Link:** [http://arxiv.org/abs/2511.06976v1](http://arxiv.org/abs/2511.06976v1)

**Summary:** Efficiently and accurately determining the symmetry is a crucial step in the structural analysis of crystalline materials. Existing methods usually mindlessly apply deep learning models while ignoring the underlying chemical rules. More importantly, experiments show that they face a serious sub-property confusion SPC problem. To address the above challenges, from a decoupled perspective, we introduce the XRDecoupler framework, a problem-solving arsenal specifically designed to tackle the SPC problem. Imitating the thinking process of chemists, we innovatively incorporate multidimensional crystal symmetry information as superclass guidance to ensure that the model's prediction process aligns with chemical intuition. We further design a hierarchical PXRD pattern learning model and a multi-objective optimization approach to achieve high-quality representation and balanced optimization. Comprehensive evaluations on three mainstream databases (e.g., CCDC, CoREMOF, and InorganicData) demonstrate that XRDecoupler excels in performance, interpretability, and generalization....

---

### 23. DeepRWCap: Neural-Guided Random-Walk Capacitance Solver for IC Design

**Authors:** Hector R. Rodriguez, Jiechen Huang, Wenjian Yu

**Published:** 2025-11-10

**Category:** cs.LG

**ID:** 2511.06831v1

**Link:** [http://arxiv.org/abs/2511.06831v1](http://arxiv.org/abs/2511.06831v1)

**Summary:** Monte Carlo random walk methods are widely used in capacitance extraction for their mesh-free formulation and inherent parallelism. However, modern semiconductor technologies with densely packed structures present significant challenges in unbiasedly sampling transition domains in walk steps with multiple high-contrast dielectric materials. We present DeepRWCap, a machine learning-guided random walk solver that predicts the transition quantities required to guide each step of the walk. These include Poisson kernels, gradient kernels, signs and magnitudes of weights. DeepRWCap employs a two-stage neural architecture that decomposes structured outputs into face-wise distributions and spatial kernels on cube faces. It uses 3D convolutional networks to capture volumetric dielectric interactions and 2D depthwise separable convolutions to model localized kernel behavior. The design incorporates grid-based positional encodings and structural design choices informed by cube symmetries to reduce learning redundancy and improve generalization. Trained on 100,000 procedurally generated dielectric configurations, DeepRWCap achieves a mean relative error of $1.24\pm0.53$\% when benchmarked against the commercial Raphael solver on the self-capacitance estimation of 10 industrial designs spanning 12 to 55 nm nodes. Compared to the state-of-the-art stochastic difference method Microwalk, DeepRWCap achieves an average 23\% speedup. On complex designs with runtimes over 10 s, it reaches an average 49\% acceleration....

---

### 24. Taming Multi-Domain, -Fidelity Data: Towards Foundation Models for Atomistic Scale Simulations

**Authors:** Tomoya Shiota, Kenji Ishihara, Tuan Minh Do, Toshio Mori, Wataru Mizukami

**Published:** 2024-12-17

**Category:** physics.chem-ph

**ID:** 2412.13088v2

**Link:** [http://arxiv.org/abs/2412.13088v2](http://arxiv.org/abs/2412.13088v2)

**Summary:** Machine learning interatomic potentials (MLIPs) are changing atomistic simulations in the field of chemistry and materials science. However, constructing a single universal MLIP that can accurately model molecular and crystalline systems remains challenging. A central obstacle is the integration of diverse datasets generated under different computational conditions. We present Total Energy Alignment (TEA), which is an approach that enables the seamless integration of heterogeneous quantum chemical datasets without redundant calculations. Using TEA, we trained MACE-Osaka24, the first open-source MLIP model based on a unified dataset covering molecular and crystalline systems. This universal model displays strong performances across diverse chemical systems, exhibiting similar or improved accuracies in predicting organic reaction barriers compared to those of specialized models, while effectively maintaining state-of-the-art accuracies for inorganic systems. These advancements pave the way for accelerated discoveries in the fields of chemistry and materials science via genuine foundation models for chemistry....

---

### 25. Explainable Probabilistic Machine Learning for Predicting Drilling Fluid Loss of Circulation in Marun Oil Field

**Authors:** Seshu Kumar Damarla, Xiuli Zhu

**Published:** 2025-11-10

**Category:** cs.LG

**ID:** 2511.06607v1

**Link:** [http://arxiv.org/abs/2511.06607v1](http://arxiv.org/abs/2511.06607v1)

**Summary:** Lost circulation remains a major and costly challenge in drilling operations, often resulting in wellbore instability, stuck pipe, and extended non-productive time. Accurate prediction of fluid loss is therefore essential for improving drilling safety and efficiency. This study presents a probabilistic machine learning framework based on Gaussian Process Regression (GPR) for predicting drilling fluid loss in complex formations. The GPR model captures nonlinear dependencies among drilling parameters while quantifying predictive uncertainty, offering enhanced reliability for high-risk decision-making. Model hyperparameters are optimized using the Limited memory Broyden Fletcher Goldfarb Shanno (LBFGS) algorithm to ensure numerical stability and robust generalization. To improve interpretability, Local Interpretable Model agnostic Explanations (LIME) are employed to elucidate how individual features influence model predictions. The results highlight the potential of explainable probabilistic learning for proactive identification of lost-circulation risks, optimized design of lost circulation materials (LCM), and reduction of operational uncertainties in drilling applications....

---

### 26. Scalable Machine Learning Models for Predicting Quantum Transport in Disordered 2D Hexagonal Materials

**Authors:** Seyed Mahdi Mastoor, Amirhossein Ahmadkhan Kordbacheh

**Published:** 2025-06-09

**Category:** cond-mat.mes-hall

**ID:** 2506.07983v2

**Link:** [http://arxiv.org/abs/2506.07983v2](http://arxiv.org/abs/2506.07983v2)

**Summary:** We introduce scalable machine learning models to accurately predict two key quantum transport properties, the transmission coefficient T(E) and average local density of states (Average-LDOS) in two-dimensional (2D) hexagonal materials with magnetic disorder. Using a tight binding Hamiltonian combined with the Non-Equilibrium Green's Function (NEGF) formalism, we generate a large dataset of over 400,000 unique configurations across graphene, germanene, silicene, and stanene nanoribbons with varying geometries, impurity concentrations, and energy levels. A central contribution of this work is the development of a geometrydriven, physically interpretable feature space that enables the models to generalize across material types and device sizes. Random Forest regression and classification models are evaluated in terms of accuracy, stability, and extrapolation ability. Regression consistently outperforms classification in capturing continuous transport behavior on in-domain data. However, extrapolation performance degrades significantly, revealing the limitations of tree-based models in unseen regimes. This study highlights both the potential and constraints of scalable ML models for quantum transport prediction and motivates future research into physics-informed or graph-based learning architectures for improved generalization in spintronic and nanoelectronic device design....

---

### 27. Language Model Distillation: A Temporal Difference Imitation Learning Perspective

**Authors:** Zishun Yu, Shangzhe Li, Xinhua Zhang

**Published:** 2025-05-24

**Category:** cs.CL

**ID:** 2505.20335v2

**Link:** [http://arxiv.org/abs/2505.20335v2](http://arxiv.org/abs/2505.20335v2)

**Summary:** Large language models have led to significant progress across many NLP tasks, although their massive sizes often incur substantial computational costs. Distillation has become a common practice to compress these large and highly capable models into smaller, more efficient ones. Many existing language model distillation methods can be viewed as behavior cloning from the perspective of imitation learning or inverse reinforcement learning. This viewpoint has inspired subsequent studies that leverage (inverse) reinforcement learning techniques, including variations of behavior cloning and temporal difference learning methods. Rather than proposing yet another specific temporal difference method, we introduce a general framework for temporal difference-based distillation by exploiting the distributional sparsity of the teacher model. Specifically, it is often observed that language models assign most probability mass to a small subset of tokens. Motivated by this observation, we design a temporal difference learning framework that operates on a reduced action space (a subset of vocabulary), and demonstrate how practical algorithms can be derived and the resulting performance improvements....

---

### 28. Fuzzy Neural Network Performance and Interpretability of Quantum Wavefunction Probability Predictions

**Authors:** Pedro H. M. Zanineli, Matheus Zaia Monteiro, Vinicius Francisco Wasques, Francielle Santo Pedro Simões, Gabriel R. Schleder

**Published:** 2025-11-07

**Category:** physics.chem-ph

**ID:** 2511.05261v1

**Link:** [http://arxiv.org/abs/2511.05261v1](http://arxiv.org/abs/2511.05261v1)

**Summary:** Predicting quantum wavefunction probability distributions is crucial for computational chemistry and materials science, yet machine learning (ML) models often face a trade-off between accuracy and interpretability. This study compares Artificial Neural Networks (ANNs) and Adaptive Neuro-Fuzzy Inference Systems (ANFIS) in modeling quantum probability distributions for the H$_{2}^+$ ion, leveraging data generated via Physics-Informed Neural Networks (PINNs). While ANN achieved superior accuracy (R$^2$ = 0.99 vs ANFIS's 0.95 with Gaussian membership functions), it required over 50x more parameters (2,305 vs 39-45). ANFIS, however, provided unique interpretability: its Gaussian membership functions encoded spatial electron localization near proton positions ($μ= 1.2 A$), mirroring Born probability densities, while fuzzy rules reflected quantum superposition principles. Rules prioritizing the internuclear direction revealed the system's 1D symmetry, aligning with Linear Combination of Atomic Orbitals theory--a novel data-driven perspective on orbital hybridization. Membership function variances ($σ$) further quantified electron delocalization trends, and peak prediction errors highlighted unresolved quantum cusps. The choice of functions critically impacted performance: Gaussian/Generalized Bell outperformed Sigmoid, with errors improving as training data increased, showing scalability. This study underscores the context-dependent value of ML: ANN for precision and ANFIS for interpretable, parameter-efficient approximations that link inputs to physical behavior. These findings advocate hybrid approaches in quantum simulations, balancing accuracy with explainability to accelerate discovery. Future work should extend ANFIS to multi-electron systems and integrate domain-specific constraints (e.g., kinetic energy terms), bridging data-driven models and fundamental physics....

---

### 29. Optimizing Cross-Domain Transfer for Universal Machine Learning Interatomic Potentials

**Authors:** Jaesun Kim, Jinmu You, Yutack Park, Yunsung Lim, Yujin Kang, Jisu Kim, Haekwan Jeon, Suyeon Ju, Deokgi Hong, Seung Yul Lee, Saerom Choi, Yongdeok Kim, Jae W. Lee, Seungwu Han

**Published:** 2025-10-13

**Category:** cond-mat.mtrl-sci

**ID:** 2510.11241v3

**Link:** [http://arxiv.org/abs/2510.11241v3](http://arxiv.org/abs/2510.11241v3)

**Summary:** Accurate yet transferable machine-learning interatomic potentials (MLIPs) are essential for accelerating materials and chemical discovery. However, most universal MLIPs overfit to narrow datasets or computational protocols, limiting their reliability across chemical and functional domains. We introduce a transferable multi-domain training strategy that jointly optimizes universal and task-specific parameters through selective regularization, coupled with a domain-bridging set (DBS) that aligns potential-energy surfaces across datasets. Systematic ablation experiments show that small DBS fractions (0.1%) and targeted regularization synergistically enhance out-of-distribution generalization while preserving in-domain fidelity. Trained on fifteen open databases spanning molecules, crystals, and surfaces, our model, SevenNet-Omni, achieves state-of-the-art cross-domain accuracy, including adsorption-energy errors below 0.06 eV on metallic surfaces and 0.1 eV on metal-organic frameworks. Despite containing only 0.5% r$^2$SCAN data, SevenNet-Omni reproduces high-fidelity r$^2$SCAN energetics, demonstrating effective cross-functional transfer from large PBE datasets. This framework offers a scalable route toward universal, transferable MLIPs that bridge quantum-mechanical fidelities and chemical domains....

---

### 30. Retrieval Augmented Diffusion Model for Structure-informed Antibody Design and Optimization

**Authors:** Zichen Wang, Yaokun Ji, Jianing Tian, Shuangjia Zheng

**Published:** 2024-10-19

**Category:** cs.AI

**ID:** 2410.15040v2

**Link:** [http://arxiv.org/abs/2410.15040v2](http://arxiv.org/abs/2410.15040v2)

**Summary:** Antibodies are essential proteins responsible for immune responses in organisms, capable of specifically recognizing antigen molecules of pathogens. Recent advances in generative models have significantly enhanced rational antibody design. However, existing methods mainly create antibodies from scratch without template constraints, leading to model optimization challenges and unnatural sequences. To address these issues, we propose a retrieval-augmented diffusion framework, termed RADAb, for efficient antibody design. Our method leverages a set of structural homologous motifs that align with query structural constraints to guide the generative model in inversely optimizing antibodies according to desired design criteria. Specifically, we introduce a structure-informed retrieval mechanism that integrates these exemplar motifs with the input backbone through a novel dual-branch denoising module, utilizing both structural and evolutionary information. Additionally, we develop a conditional diffusion model that iteratively refines the optimization process by incorporating both global context and local evolutionary conditions. Our approach is agnostic to the choice of generative models. Empirical experiments demonstrate that our method achieves state-of-the-art performance in multiple antibody inverse folding and optimization tasks, offering a new perspective on biomolecular generative models....

---

### 31. Intrinsic Fracture Nonreciprocity at the Nanoscale

**Authors:** Siwei Zhao, Penghua Ying, Guoqiang Zhang, Ke Zhou, Shengying Yue, Yan Chen, Yilun Liu

**Published:** 2025-11-07

**Category:** cond-mat.mtrl-sci

**ID:** 2511.04936v1

**Link:** [http://arxiv.org/abs/2511.04936v1](http://arxiv.org/abs/2511.04936v1)

**Summary:** We reveal intrinsic fracture nonreciprocity, manifesting as directional asymmetry in crack resistance, in two-dimensional heterostructures engineered through lattice-mismatched interfaces. Density-functional theory combined with machine-learning molecular dynamics show that intrinsic lattice mismatch between bonded component crystals imprints asymmetric prestrain states at crack tips, governing bond-breaking thresholds through charge redistribution. The failure criterion obeys a universal exponential scaling law between normalized charge density and bond strain, insensitive to bonding chemistry and local atomic environment. The magnitude of nonreciprocity scales systematically with lattice mismatch, reaching 49% at 10% mismatch. Validation across hexagonal, square, rectangular, and oblique two-dimensional lattices confirms universality, establishing interface strain engineering as a general design principle that bridges electronic structure to nanoscale failure, enabling rational design of damage-tolerant nanostructures....

---

### 32. GENIAL: Generative Design Space Exploration via Network Inversion for Low Power Algorithmic Logic Units

**Authors:** Maxence Bouvier, Ryan Amaudruz, Felix Arnold, Renzo Andri, Lukas Cavigelli

**Published:** 2025-07-25

**Category:** cs.LG

**ID:** 2507.18989v2

**Link:** [http://arxiv.org/abs/2507.18989v2](http://arxiv.org/abs/2507.18989v2)

**Summary:** As AI workloads proliferate, optimizing arithmetic units is becoming increasingly important for reducing the footprint of digital systems. Conventional design flows, which often rely on manual or heuristic-based optimization, are limited in their ability to thoroughly explore the vast design space. In this paper, we introduce GENIAL, a machine learning-based framework for the automatic generation and optimization of arithmetic units, with a focus on multipliers.
  At the core of GENIAL is a Transformer-based surrogate model trained in two stages, involving self-supervised pretraining followed by supervised finetuning, to robustly forecast key hardware metrics such as power and area from abstracted design representations. By inverting the surrogate model, GENIAL efficiently searches for new operand encodings that directly minimize power consumption in arithmetic units for specific input data distributions. Extensive experiments on large datasets demonstrate that GENIAL is consistently more sample efficient than other methods, and converges faster towards optimized designs. This enables deployment of a high-effort logic synthesis optimization flow in the loop, improving the accuracy of the surrogate model. Notably, GENIAL automatically discovers encodings that achieve up to 18% switching activity savings within multipliers on representative AI workloads compared with the conventional two's complement. We also demonstrate the versatility of our approach by achieving significant improvements on Finite State Machines, highlighting GENIAL's applicability for a wide spectrum of logic functions. Together, these advances mark a significant step toward automated Quality-of-Results-optimized combinational circuit generation for digital systems....

---

### 33. KAN-Enhanced Contrastive Learning Accelerating Crystal Structure Identification from XRD Patterns

**Authors:** Chenlei Xu, Tianhao Su, Jie Xiong, Yue Wu, Shuya Dong, Tian Jiang, Mengwei He, Shuai Chen, Tong-Yi Zhang

**Published:** 2025-11-06

**Category:** cond-mat.mtrl-sci

**ID:** 2511.04055v1

**Link:** [http://arxiv.org/abs/2511.04055v1](http://arxiv.org/abs/2511.04055v1)

**Summary:** Accurate determination of crystal structures is central to materials science, underpinning the understanding of composition-structure-property relationships and the discovery of new materials. Powder X-ray diffraction is a key technique in this pursuit due to its versatility and reliability. However, current analysis pipelines still rely heavily on expert knowledge and slow iterative fitting, limiting their scalability in high-throughput and autonomous settings. Here, we introduce a physics-guided contrastive learning framework termed as XCCP. It aligns powder diffraction patterns with candidate crystal structures in a shared embedding space to enable efficient structure retrieval and symmetry recognition. The XRD encoder employs a dual-expert design with a Kolmogorov-Arnold Network projection head, one branch emphasizes low angle reflections reflecting long-range order, while the other captures dense high angle peaks shaped by symmetry. Coupled with a crystal graph encoder, contrastive pretraining yields physically grounded representations. XCCP demonstrates strong performance across tasks, with structure retrieval reaching 0.89 and space group identification attains 0.93 accuracy. The framework further generalizes to compositionally similar multi principal element alloys and demonstrates zero-shot transfer to experimental patterns. These results establish XCCP as a robust, interpretable, and scalable approach that offers a new paradigm for X-ray diffraction analysis. XCCP facilitates high-throughput screening, rapid structural validation and integration into autonomous laboratories....

---

### 34. A data-driven quest for room-temperature bulk plastically deformable ceramics

**Authors:** Iwo Słodczyk, Alexander Frisch, Xufei Fang, Inna Gitman, Fengxian Liu

**Published:** 2025-11-05

**Category:** cond-mat.mtrl-sci

**ID:** 2511.03815v1

**Link:** [http://arxiv.org/abs/2511.03815v1](http://arxiv.org/abs/2511.03815v1)

**Summary:** The growing number of ceramics exhibiting bulk plasticity at room temperature has renewed interest in revisiting plastic deformation and dislocation-mediated mechanical and functional properties in these materials. In this work, a data-driven approach is employed to identify the key parameters governing room-temperature bulk plasticity in ceramics. The model integrates an existing dataset of 55 ceramic materials, 38 plastically deformable and 17 brittle, and achieves accurate classification of bulk plasticity. The analysis reveals several key parameters essential for predicting bulk plasticity: i) Poisson's ratio and Pugh's ratio as macroscopic indicators reflecting the balance between shear and volumetric deformation resistance, and ii) Burgers vector, crystal structure and melting temperature as crystallographic descriptors associated with lattice geometry, slip resistance and thermal stability, and iii) Bader charge as a microscopic measure of bonding character. Together, these parameters define a multiscale descriptor space linking intrinsic materials properties to bulk room-temperature plasticity in ceramics, bridging the gap between empirical ductility criteria and atomistic mechanisms of dislocation-mediated plasticity. While preliminary, this study provides the first systematic, data-driven mapping of the governing factors of ceramic plasticity. The resulting framework establishes a foundation for unifying experimental and computational studies through shared datasets and descriptors, fostering collective progress toward understanding and designing intrinsically ductile ceramics....

---

### 35. Kosmos: An AI Scientist for Autonomous Discovery

**Authors:** Ludovico Mitchener, Angela Yiu, Benjamin Chang, Mathieu Bourdenx, Tyler Nadolski, Arvis Sulovari, Eric C. Landsness, Daniel L. Barabasi, Siddharth Narayanan, Nicky Evans, Shriya Reddy, Martha Foiani, Aizad Kamal, Leah P. Shriver, Fang Cao, Asmamaw T. Wassie, Jon M. Laurent, Edwin Melville-Green, Mayk Caldas, Albert Bou, Kaleigh F. Roberts, Sladjana Zagorac, Timothy C. Orr, Miranda E. Orr, Kevin J. Zwezdaryk, Ali E. Ghareeb, Laurie McCoy, Bruna Gomes, Euan A. Ashley, Karen E. Duff, Tonio Buonassisi, Tom Rainforth, Randall J. Bateman, Michael Skarlinski, Samuel G. Rodriques, Michaela M. Hinks, Andrew D. White

**Published:** 2025-11-04

**Category:** cs.AI

**ID:** 2511.02824v2

**Link:** [http://arxiv.org/abs/2511.02824v2](http://arxiv.org/abs/2511.02824v2)

**Summary:** Data-driven scientific discovery requires iterative cycles of literature search, hypothesis generation, and data analysis. Substantial progress has been made towards AI agents that can automate scientific research, but all such agents remain limited in the number of actions they can take before losing coherence, thus limiting the depth of their findings. Here we present Kosmos, an AI scientist that automates data-driven discovery. Given an open-ended objective and a dataset, Kosmos runs for up to 12 hours performing cycles of parallel data analysis, literature search, and hypothesis generation before synthesizing discoveries into scientific reports. Unlike prior systems, Kosmos uses a structured world model to share information between a data analysis agent and a literature search agent. The world model enables Kosmos to coherently pursue the specified objective over 200 agent rollouts, collectively executing an average of 42,000 lines of code and reading 1,500 papers per run. Kosmos cites all statements in its reports with code or primary literature, ensuring its reasoning is traceable. Independent scientists found 79.4% of statements in Kosmos reports to be accurate, and collaborators reported that a single 20-cycle Kosmos run performed the equivalent of 6 months of their own research time on average. Furthermore, collaborators reported that the number of valuable scientific findings generated scales linearly with Kosmos cycles (tested up to 20 cycles). We highlight seven discoveries made by Kosmos that span metabolomics, materials science, neuroscience, and statistical genetics. Three discoveries independently reproduce findings from preprinted or unpublished manuscripts that were not accessed by Kosmos at runtime, while four make novel contributions to the scientific literature....

---

### 36. Coherent Phonon Negative Refraction via Interfacial Momentum Compensation

**Authors:** Hao Chen, Zhong-Ke Ding, Nannan Luo, Jiang Zeng, Li-Ming Tang, Ke-Qiu Chen

**Published:** 2025-11-05

**Category:** cond-mat.mes-hall

**ID:** 2511.03599v1

**Link:** [http://arxiv.org/abs/2511.03599v1](http://arxiv.org/abs/2511.03599v1)

**Summary:** Negative refraction of coherent phonons is crucial for thermal management and quantum information processing, but it remains unrealized because achieving the suitable dispersion for negative refraction simultaneously with long-range coherence is challenging. In this letter, we overcome this limitation by introducing a momentum compensation mechanism mediated by discrete translational symmetry. Interfacial reciprocal lattice vectors provide momentum compensation during phonon tunneling and induce asymmetric mode matching, resulting in negative refraction without requiring strong dispersion anisotropy or a negative-curvature band. Using non-equilibrium Green's function formalism, we demonstrate coherent negative refraction of isotropic acoustic phonons in graphene/hexagonal boron nitride heterostructures. This general mechanism enables active control of phonon flow via interfacial design, paving the way for applications in atomic-scale phonon lenses and directional thermal transport....

---

### 37. The Mirror Loop: Recursive Non-Convergence in Generative Reasoning Systems

**Authors:** Bentley DeVilling

**Published:** 2025-10-23

**Category:** cs.LG

**ID:** 2510.21861v2

**Link:** [http://arxiv.org/abs/2510.21861v2](http://arxiv.org/abs/2510.21861v2)

**Summary:** Large language models are often described as capable of reflective reasoning, yet recursive self-evaluation without external feedback frequently yields reformulation rather than progress. We test this prediction in a cross-provider study of 144 reasoning sequences across three models (OpenAI GPT-4o-mini, Anthropic Claude 3 Haiku, and Google Gemini 2.0 Flash) and four task families (arithmetic, code, explanation, reflection), each iterated ten times under two conditions: ungrounded self-critique and a minimal grounding intervention (a single verification step at iteration three). Mean informational change (delta I, measured via normalized edit distance) declined by 55% from early (0.193) to late (0.087) iterations in ungrounded runs, with consistent patterns across all three providers. Grounded runs showed a +28% rebound in informational change immediately after the intervention and sustained non-zero variance thereafter. Complementary measures-n-gram novelty, embedding drift, and character-level entropy-converged on the same pattern: reflection without contact tends toward informational closure. We interpret this as evidence for a structural limit on self-correction in generative reasoning: without an exchange of information with an independent verifier or environment, recursive inference approaches an attractor state of epistemic stasis. Minimal grounding functions as dissipative coupling, reintroducing informational flux. The cross-architecture consistency suggests the mirror loop arises from shared autoregressive training objectives rather than provider-specific alignment schemes. The results delineate when reflection is performative rather than epistemic and motivate design principles for grounded, cooperative reasoning. Materials and code are publicly available....

---

### 38. Lorentz Skew Scattering Nonreciprocal Magneto-Transport

**Authors:** Xiu Fang Lu, Xue-Jin Zhang, Naizhou Wang, Jin Cao, Dan Zhao, Hui Wang, Tao Wu, Xian Hui Chen, Shen Lai, Cong Xiao, Shengyuan A. Yang, Weibo Gao

**Published:** 2025-11-05

**Category:** cond-mat.mes-hall

**ID:** 2511.03273v1

**Link:** [http://arxiv.org/abs/2511.03273v1](http://arxiv.org/abs/2511.03273v1)

**Summary:** In materials with broken inversion symmetry, nonreciprocal magneto-transport (NRMT) manifests as a bilinear dependence of charge conductivity on applied electric (E) and magnetic (B) fields. This phenomenon is deeply rooted in symmetry and electronic quantum geometry, holding promise for novel rectification and detector technologies. Existing experimental studies generally attribute NRMT to Zeeman-driven mechanisms and exhibit quadratic scaling with conductivity. Here, we report a previously unknown NRMT microscopic mechanism - Lorentz skew scattering (LSK) - revealed through the discovery of an unprecedented quartic scaling law of NRMT as well as quantitative agreement between theory and experiment in BiTeBr. LSK emerges from the interplay of Lorentz force and skew scattering, bridging classical field effect to quantum scattering effect on the Fermi surface. We demonstrate that the LSK dominates NRMT in BiTeBr, and elucidate that this dominance over other possible contributions stems from high mobility and strong Rashba splitting. The finding of LSK mechanism is of unique importance because it unveils the leading NRMT effect in high-mobility systems and suggests a universal principle towards strong NRMT by enhancing electronic relaxation time in topological materials, rendering a new designing idea for low-dissipation rectifiers and high-performance quantum electronics....

---

### 39. Cooperative Ion Conduction Enabled by Site Percolation in Random Substitutional Crystals

**Authors:** Rikuya Ishikawa, Kyohei Takae, Rei Kurita

**Published:** 2025-05-01

**Category:** cond-mat.mtrl-sci

**ID:** 2505.00362v2

**Link:** [http://arxiv.org/abs/2505.00362v2](http://arxiv.org/abs/2505.00362v2)

**Summary:** Efficient and safe energy storage technologies are essential for realizing a sustainable and electrified society. Among the key challenges, the design of superionic conductors for all-solid-state batteries often faces a fundamental trade-off between stability and ionic conductivity. Random substitutional crystals, where atomic species are randomly distributed throughout a crystal lattice, present a promising route to overcome this trade-off. Although the importance of cooperative motion in ion conduction has been pointed out, there is a lack of understanding of the relationship between mesoscale structural organization and macroscopic conductivity, limiting the rational design of optimal compositions. Here, we systematically investigate the ionic conductivity of rock salt random substitutional ionic crystals Li$_x$Pb$_{1-2x}$Bi$_x$Te as a function of Li concentration $x$ using molecular dynamics simulations. We find that ionic conductivity increases sharply once the $x$ exceeds a critical threshold, without disrupting the underlying crystal structure. Strikingly, this threshold aligns with the site-percolation threshold predicted by percolation theory. Our findings establish ion percolation as a universal design principle that reconciles the trade-off between conductivity and stability, offering a simple and broadly applicable strategy for the development of robust, high-performance solid electrolytes....

---

### 40. Fine-Tuning Vision-Language Models for Multimodal Polymer Property Prediction

**Authors:** An Vuong, Minh-Hao Van, Prateek Verma, Chen Zhao, Xintao Wu

**Published:** 2025-11-04

**Category:** cs.LG

**ID:** 2511.05577v1

**Link:** [http://arxiv.org/abs/2511.05577v1](http://arxiv.org/abs/2511.05577v1)

**Summary:** Vision-Language Models (VLMs) have shown strong performance in tasks like visual question answering and multimodal text generation, but their effectiveness in scientific domains such as materials science remains limited. While some machine learning methods have addressed specific challenges in this field, there is still a lack of foundation models designed for broad tasks like polymer property prediction using multimodal data. In this work, we present a multimodal polymer dataset to fine-tune VLMs through instruction-tuning pairs and assess the impact of multimodality on prediction performance. Our fine-tuned models, using LoRA, outperform unimodal and baseline approaches, demonstrating the benefits of multimodal learning. Additionally, this approach reduces the need to train separate models for different properties, lowering deployment and maintenance costs....

---

### 41. Leveraging Discrete Function Decomposability for Scientific Design

**Authors:** James C. Bowden, Sergey Levine, Jennifer Listgarten

**Published:** 2025-11-04

**Category:** cs.LG

**ID:** 2511.03032v1

**Link:** [http://arxiv.org/abs/2511.03032v1](http://arxiv.org/abs/2511.03032v1)

**Summary:** In the era of AI-driven science and engineering, we often want to design discrete objects in silico according to user-specified properties. For example, we may wish to design a protein to bind its target, arrange components within a circuit to minimize latency, or find materials with certain properties. Given a property predictive model, in silico design typically involves training a generative model over the design space (e.g., protein sequence space) to concentrate on designs with the desired properties. Distributional optimization -- which can be formalized as an estimation of distribution algorithm or as reinforcement learning policy optimization -- finds the generative model that maximizes an objective function in expectation. Optimizing a distribution over discrete-valued designs is in general challenging because of the combinatorial nature of the design space. However, many property predictors in scientific applications are decomposable in the sense that they can be factorized over design variables in a way that could in principle enable more effective optimization. For example, amino acids at a catalytic site of a protein may only loosely interact with amino acids of the rest of the protein to achieve maximal catalytic activity. Current distributional optimization algorithms are unable to make use of such decomposability structure. Herein, we propose and demonstrate use of a new distributional optimization algorithm, Decomposition-Aware Distributional Optimization (DADO), that can leverage any decomposability defined by a junction tree on the design variables, to make optimization more efficient. At its core, DADO employs a soft-factorized "search distribution" -- a learned generative model -- for efficient navigation of the search space, invoking graph message-passing to coordinate optimization across linked factors....

---

### 42. Suppression of auxetic behavior in black phosphorus with sulfur substitution

**Authors:** Hayden Groeschel, Arjyama Bordoloi, Sobhit Singh

**Published:** 2025-11-04

**Category:** cond-mat.mtrl-sci

**ID:** 2511.02609v1

**Link:** [http://arxiv.org/abs/2511.02609v1](http://arxiv.org/abs/2511.02609v1)

**Summary:** Sulfur-doped black phosphorus (b-P) has recently emerged as a promising candidate for next-generation electronic and optoelectronic technologies owing to its enhanced environmental stability and tunable electronic properties. In this work, we systematically investigate the effects of sulfur substitution on the elastic, mechanical, and electronic properties of b-P, with a particular focus on its auxetic behavior (that is, negative Poisson's ratio), using first-principles density functional theory calculations. Our results unveil the fundamental origin of the intrinsic auxetic response in pristine b-P and elucidate how sulfur incorporation alters this behavior. We find that sulfur atoms distort the characteristic bow-tie structural motif responsible for the negative Poisson's ratio in b-P, thereby suppressing the in-plane auxeticity. Moreover, the resulting charge redistribution also effectively quenches the out-of-plane auxetic response of b-P. With increasing sulfur content, the bulk modulus and Poisson's ratio increase, whereas the Young's modulus, shear modulus, and Debye temperature decrease. Additionally, sulfur substitution suppresses the semiconducting properties of b-P, giving rise to metallicity. These findings highlight that although sulfur substitution enhances the environmental stability of b-P, it also substantially modifies its elastic and mechanical properties, particularly the auxetic behavior, which is an important consideration in the design of nanoscale electronic devices....

---

### 43. Adhesive strength of bio-inspired fibrillar arrays in the presence of contact defects

**Authors:** Agostinelli Daniele, Shojaeifard Mohammad, Bacca Mattia

**Published:** 2025-11-04

**Category:** cond-mat.soft

**ID:** 2511.02477v1

**Link:** [http://arxiv.org/abs/2511.02477v1](http://arxiv.org/abs/2511.02477v1)

**Summary:** The performance of bio-inspired fibrillar adhesives can be compromised by surface roughness, manufacturing imperfections or impurities. Previous studies investigated the cases of distributed defects on the array, and defects at the level of single fibrils. However, the influence of localized, macroscopic defects remains largely unexplored. Using numerical simulations of a discrete mechanical model for a fibrillar adhesive with a thick backing layer, we investigate how the size and location of a single circular defect affect the established scaling law between the adhesion force ($F$) and the effective compliance of the system ($β$), \ie, $F \propto β^{-1/2}$. We find that edge defects are generally more detrimental than central ones, as they act as pre-cracks that amplify stress concentrations at the adhesive's edge, accelerating a crack-like failure. Consequently, the established adhesion scaling law is preserved, with the defect only reducing the effective contact area. In contrast, a central defect fundamentally alters the mechanics of detachment. By transforming the contact geometry into an annulus, it promotes more uniform load sharing across the remaining fibrils and mitigates the edge-dominated failure mechanism. This change makes the adhesive strength less sensitive to the compliance of the system, as reflected by a less negative scaling exponent. The transition between these two regimes appears to occur for defects whose boundary merges with the one of the adhesive. These results provide practical guidance for the design, engineering and quality control of bio-inspired fibrillar adhesives....

---

### 44. Dual-Polarization SHG Interferometry for Imaging Antiparallel Domains and Stacking Angles of 2D Heterocrystals

**Authors:** Juseung Oh, Wontaek Kim, Gyouil Jeong, Yeri Lee, Jihun Kim, Hyeongjoon Kim, Hyeon Suk Shin, Sunmin Ryu

**Published:** 2025-05-28

**Category:** physics.optics

**ID:** 2505.21922v2

**Link:** [http://arxiv.org/abs/2505.21922v2](http://arxiv.org/abs/2505.21922v2)

**Summary:** Optical second-harmonic generation (SHG) enables orientational polarimetry for crystallographic analysis and domain imaging of various materials. However, conventional intensity polarimetry, which neglects phase information, fails to resolve antiparallel domains and to describe two-dimensional heterostructures, which represent a new class of van der Waals-bound composite crystals. In this work, we report dual-polarization spectral phase interferometry (DP-SPI) and establish a generalized SHG superposition model that incorporates the observables of DP-SPI. Antiparallel domains of monolayer transition metal dichalcogenides (TMDs) were successfully imaged with distinction, validating the interferometric polarimetry. From DP interferograms of TMD heterobilayers, the orientation of each layer could be determined, enabling layer-resolved probing. By employing the superposition model, we also demonstrate the photonic design and fabrication of ternary TMD heterostructures for circularly polarized SHG. These methods, providing comprehensive SHG measurements and theoretical description, can be extended to heterostructures consisting of more than two constituent layers and are not limited to TMDs or 2D materials....

---

### 45. AI-assisted design of chemically recyclable polymers for food packaging

**Authors:** Brandon K. Phan, Chiho Kim, Janhavi Nistane, Wei Xiong, Haoyu Chen, Woo Jin Jang, Farzad Gholami, Yongliang Su, Jerry Qi, Ryan Lively, Will Gutekunst, Rampi Ramprasad

**Published:** 2025-11-03

**Category:** cond-mat.soft

**ID:** 2511.04704v1

**Link:** [http://arxiv.org/abs/2511.04704v1](http://arxiv.org/abs/2511.04704v1)

**Summary:** Polymer packaging plays a crucial role in food preservation but poses major challenges in recycling and environmental persistence. To address the need for sustainable, high-performance alternatives, we employed a polymer informatics workflow to identify single- and multi-layer drop-in replacements for polymer-based packaging materials. Machine learning (ML) models, trained on carefully curated polymer datasets, predicted eight key properties across a library of approximately 7.4 million ring-opening polymerization (ROP) polymers generated by virtual forward synthesis (VFS). Candidates were prioritized by the enthalpy of polymerization, a critical metric for chemical recyclability. This screening yielded thousands of promising candidates, demonstrating the feasibility of replacing diverse packaging architectures. We then experimentally validated poly(p-dioxanone) (poly-PDO), an existing ROP polymer whose barrier performance had not been previously reported. Validation showed that poly-PDO exhibits strong water barrier performance, mechanical and thermal properties consistent with predictions, and excellent chemical recyclability (95% monomer recovery), thereby meeting the design targets and underscoring its potential for sustainable packaging. These findings highlight the power of informatics-driven approaches to accelerate the discovery of sustainable polymers by uncovering opportunities in both existing and novel chemistries....

---

### 46. Machine learning descriptors for predicting the high temperature oxidation of refractory complex concentrated alloys

**Authors:** Akhil Bejjipurapu, Alejandro Strachan, Kenneth H. Sandhage, Michael S. Titus

**Published:** 2025-11-02

**Category:** cond-mat.mtrl-sci

**ID:** 2511.01095v1

**Link:** [http://arxiv.org/abs/2511.01095v1](http://arxiv.org/abs/2511.01095v1)

**Summary:** Refractory Complex Concentrated Alloys (RCCAs) can exhibit exceptional high-temperature strength, making such alloys promising candidates for high-temperature structural applications. However, current RCCAs do not possess the high-temperature oxidation resistance required to survive in oxidizing environments for more than a few hours at or above 1000$^\circ$C, without relying primarily on an environmental barrier coating. Here, we present a machine-learning framework designed to predict the oxidation-induced specific mass changes of RCCAs exposed for 24 h at 1000$^\circ$C in air, in order to support the search for oxidation-resistant alloys over a wide range of compositions. A database was constructed of experimental specific mass change data, upon oxidation at 900-1000$^\circ$C for 24 h in air, for 77 compositions comprised of simple elements, binary alloys, and higher-order elemental systems. We then developed a Gaussian Process Regression (GPR) model with physics-informed descriptors based on oxidation products, capturing the fundamental chemistry of oxide formation and stability. Application of this GPR model to the database yielded a MAE (mean absolute error) test score of 5.78 mg/cm$^2$, which was a significant improvement in accuracy relative to models only utilizing traditional alloy-based descriptors. Our model was used to screen over 5,100 quaternary RCCAs, revealing compositions with significantly lower predicted specific mass changes compared to existing literature sources. Overall, this work establishes a versatile and efficient strategy to accelerate the discovery of next-generation RCCAs with enhanced resistance to extreme environments....

---

### 47. Validation of Semi-Empirical xTB Methods for High-Throughput Screening of TADF Emitters: A 747-Molecule Benchmark Study

**Authors:** Jean-Pierre Tchapet Njafa, Elvira Vanelle Kameni Tcheuffa, Aissatou Maghame, Serge Guy Nana Engo

**Published:** 2025-11-02

**Category:** cond-mat.mtrl-sci

**ID:** 2511.00922v1

**Link:** [http://arxiv.org/abs/2511.00922v1](http://arxiv.org/abs/2511.00922v1)

**Summary:** Thermally activated delayed fluorescence (TADF) emitters are essential for next-generation, high-efficiency organic light-emitting diodes (OLEDs), yet their rational design is hampered by the high computational cost of accurate excited-state predictions. Here, we present a comprehensive benchmark study validating semi-empirical extended tight-binding (xTB) methods -- specifically sTDA-xTB and sTD-DFT-xTB -- for the high-throughput screening of TADF materials. Using an unprecedentedly large dataset of \num{747} experimentally characterized emitters, our framework demonstrates a computational cost reduction of over \qty{99}{\percent} compared to conventional TD-DFT, while maintaining strong internal consistency between methods (Pearson $r \approx \num{0.82}$ for \deltaest), validating their utility for relative molecular ranking. Validation against \num{312} experimental \deltaest values reveals a mean absolute error of approximately \qty{0.17}{\electronvolt}, a discrepancy attributed to the vertical approximation inherent to the HTS protocol, underscoring the methods' role in screening rather than quantitative prediction. Through large-scale data analysis, we statistically validate key design principles, confirming the superior performance of Donor-Acceptor-Donor (D-A-D) architectures and identifying an optimal D-A torsional angle range of \qtyrange{50}{90}{\degree} for efficient TADF. Principal Component Analysis reveals that the complex property space is fundamentally low-dimensional, with three components capturing nearly \qty{90}{\percent} of the variance. This work establishes these semi-empirical methods as powerful, cost-effective tools for accelerating TADF discovery and provides a robust set of data-driven design rules and methodological guidelines for the computational materials science community....

---

### 48. Language Native Lightly Structured Databases for Large Language Model Driven Composite Materials Research

**Authors:** Yuze Liu, Zhaoyuan Zhang, Xiangsheng Zeng, Yihe Zhang, Leping Yu, Lejia Wang, Xi Yu

**Published:** 2025-09-07

**Category:** cs.DB

**ID:** 2509.06093v2

**Link:** [http://arxiv.org/abs/2509.06093v2](http://arxiv.org/abs/2509.06093v2)

**Summary:** The preparation procedures of materials are often embedded narratively in experimental protocols, research articles, patents, and laboratory notes, and are structured around procedural sequences, causal relationships, and conditional logic. The synthesis of boron nitride nanosheet (BNNS) polymer composites exemplifies this linguistically encoded decision-making system, where the practical experiments involve interdependent multistage and path-dependent processes such as exfoliation, functionalization, and dispersion, each governed by heterogeneous parameters and contextual contingencies, challenging conventional numerical optimization paradigms for experiment design. We reformulate this challenge into a text-reasoning problem through a framework centered on a text-first, lightly structured materials database and large language models (LLMs) as text reasoning engines. We constructed a database that captures evidence-linked narrative excerpts from the literature while normalizing only the minimum necessary entities, attributes, and relations to enable composite retrieval that unifies semantic matching, lexical cues, and explicit value filters. Building on this language-native, provenance-preserving foundation, the LLM operates in two complementary modes: retrieval-augmented generation (RAG), grounding outputs in retrieved evidence modules from the database, and experience-augmented reasoning (EAR), which leverages iteratively trained text guides derived from multi-source literature-based narrative data as external references to inform reasoning and decision-making. Applying this integration-and-reasoning framework, we demonstrate rapid, laboratory-scale optimization of BNNS preparation, highlighting how language-native data combined with LLM-based reasoning can significantly accelerate practical material preparation....

---

### 49. Split Gibbs Discrete Diffusion Posterior Sampling

**Authors:** Wenda Chu, Zihui Wu, Yifan Chen, Yang Song, Yisong Yue

**Published:** 2025-03-03

**Category:** cs.LG

**ID:** 2503.01161v3

**Link:** [http://arxiv.org/abs/2503.01161v3](http://arxiv.org/abs/2503.01161v3)

**Summary:** We study the problem of posterior sampling in discrete-state spaces using discrete diffusion models. While posterior sampling methods for continuous diffusion models have achieved remarkable progress, analogous methods for discrete diffusion models remain challenging. In this work, we introduce a principled plug-and-play discrete diffusion posterior sampling algorithm based on split Gibbs sampling, which we call SGDD. Our algorithm enables reward-guided generation and solving inverse problems in discrete-state spaces. We demonstrate the convergence of SGDD to the target posterior distribution and verify this through controlled experiments on synthetic benchmarks. Our method enjoys state-of-the-art posterior sampling performance on a range of benchmarks for discrete data, including DNA sequence design, discrete image inverse problems, and music infilling, achieving more than 30% improved performance compared to existing baselines. Our code is available at https://github.com/chuwd19/Split-Gibbs-Discrete-Diffusion-Posterior-Sampling....

---

### 50. Persistent Homology for Structural Characterization in Disordered Systems

**Authors:** An Wang, Li Zou

**Published:** 2024-11-21

**Category:** cond-mat.dis-nn

**ID:** 2411.14390v9

**Link:** [http://arxiv.org/abs/2411.14390v9](http://arxiv.org/abs/2411.14390v9)

**Summary:** We propose a unified framework based on persistent homology (PH) to characterize both local and global structures in disordered systems. It can simultaneously generate local and global descriptors using the same algorithm and data structure, and has shown to be highly effective and interpretable in predicting particle rearrangements and classifying global phases. We also demonstrated that using a single variable enables a linear SVM to achieve nearly perfect three-phase classification. Inspired by this discovery, we define a non-parametric metric, the Separation Index (SI), which not only achieves this classification without sacrificing significant performance but also establishes a connection between particle environments and the global phase structure. Our methods provide an effective framework for understanding and analyzing the properties of disordered materials, with broad potential applications in materials science and even wider studies of complex systems....

---

### 51. AI-Driven Design of poly(ethylene terephthalate)-replacement copolymers

**Authors:** Chiho Kim, Wei Xiong, Akhlak Mahmood, Rampi Ramprasad, Huan Tran

**Published:** 2025-10-31

**Category:** cond-mat.soft

**ID:** 2511.04695v1

**Link:** [http://arxiv.org/abs/2511.04695v1](http://arxiv.org/abs/2511.04695v1)

**Summary:** Poly(ethylene terephthalate) (PET), a widely used thermoplastic in packaging, textiles, and engineering applications, is valued for its strength, clarity, and chemical resistance. Increasing environmental impact concerns and regulatory pressures drive the search for alternatives with comparable or superior performance. We present an AI-driven polymer design pipeline employing virtual forward synthesis (VFS) to generate PET-replacement copolymers. Inspired by the esterification route of PET synthesis, we systematically combined a down-selected set of Toxic Substances Control Act (TSCA)-listed monomers to create 12,100 PET-like polymers. Machine learning models predicted glass transition temperature (Tg), band gap, and tendency to crystallize, for all designs. Multi-objective screening identified 1,108 candidates predicted to match or exceed PET in $T_{\rm g}$ and band gap, including the ``rediscovery'' of other known commercial PET-alternate polymers (e.g., PETG, Tritan, Ecozen) that provide retrospective validation of our design pipeline, demonstrating a capability to rapidly design experimentally feasible polymers at a scale. Furthermore, selected, entirely new (previously unknown) candidates designed here have been synthesized and characterized, providing a definitive validation of the design framework....

---

### 52. Learning Sparse Approximate Inverse Preconditioners for Conjugate Gradient Solvers on GPUs

**Authors:** Zherui Yang, Zhehao Li, Kangbo Lyu, Yixuan Li, Tao Du, Ligang Liu

**Published:** 2025-10-31

**Category:** cs.LG

**ID:** 2510.27517v1

**Link:** [http://arxiv.org/abs/2510.27517v1](http://arxiv.org/abs/2510.27517v1)

**Summary:** The conjugate gradient solver (CG) is a prevalent method for solving symmetric and positive definite linear systems Ax=b, where effective preconditioners are crucial for fast convergence. Traditional preconditioners rely on prescribed algorithms to offer rigorous theoretical guarantees, while limiting their ability to exploit optimization from data. Existing learning-based methods often utilize Graph Neural Networks (GNNs) to improve the performance and speed up the construction. However, their reliance on incomplete factorization leads to significant challenges: the associated triangular solve hinders GPU parallelization in practice, and introduces long-range dependencies which are difficult for GNNs to model. To address these issues, we propose a learning-based method to generate GPU-friendly preconditioners, particularly using GNNs to construct Sparse Approximate Inverse (SPAI) preconditioners, which avoids triangular solves and requires only two matrix-vector products at each CG step. The locality of matrix-vector product is compatible with the local propagation mechanism of GNNs. The flexibility of GNNs also allows our approach to be applied in a wide range of scenarios. Furthermore, we introduce a statistics-based scale-invariant loss function. Its design matches CG's property that the convergence rate depends on the condition number, rather than the absolute scale of A, leading to improved performance of the learned preconditioner. Evaluations on three PDE-derived datasets and one synthetic dataset demonstrate that our method outperforms standard preconditioners (Diagonal, IC, and traditional SPAI) and previous learning-based preconditioners on GPUs. We reduce solution time on GPUs by 40%-53% (68%-113% faster), along with better condition numbers and superior generalization performance. Source code available at https://github.com/Adversarr/LearningSparsePreconditioner4GPU...

---

### 53. Crossover between intrinsic and temperature-assisted regimes in spin-orbit torque switching of antiferromagnetic order

**Authors:** Takumi Matsuo, Tomoya Higo, Daisuke Nishio-Hamane, Takuya Matsuda, Ryota Uesugi, Hanshen Tsai, Kouta Kondou, Shinji Miwa, Yoshichika Otani, Satoru Nakatsuji

**Published:** 2025-10-31

**Category:** cond-mat.mtrl-sci

**ID:** 2510.27138v1

**Link:** [http://arxiv.org/abs/2510.27138v1](http://arxiv.org/abs/2510.27138v1)

**Summary:** Intensive studies have been made on antiferromagnets as candidate materials for next generation memory bits due to their ultrafast dynamics reaching picosecond time scales. Recent demonstrations of electrical bidirectional switching of antiferromagnetic states have attracted significant attention. However, under the presence of significant Joule heating that destabilizes the magnetic order, the timescales associated with the switching can be limited to nanoseconds or longer. Here, we present the observation of a crossover in the switching behavior of the chiral antiferromagnet Mn3Sn by tuning the magnetic layer thickness. While Joule heating interferes with switching in thicker devices, we find clear signatures of an intrinsic spin-orbit torque mechanism as the thickness is reduced, avoiding the heating effect. The suppression of heating enables switching without significant attenuation of the readout signal using pulses shorter than those required by temperature-assisted mechanisms. The crossover into the spin-orbit torque switching behavior clarifies the potential for achieving ultrafast switching as expected from the picosecond spin dynamics of antiferromagnets. Our results lay the groundwork for designing antiferromagnetic memory devices that can operate at ultrafast timescales....

---

### 54. CDFlow: Building Invertible Layers with Circulant and Diagonal Matrices

**Authors:** Xuchen Feng, Siyu Liao

**Published:** 2025-10-29

**Category:** cs.LG

**ID:** 2510.25323v2

**Link:** [http://arxiv.org/abs/2510.25323v2](http://arxiv.org/abs/2510.25323v2)

**Summary:** Normalizing flows are deep generative models that enable efficient likelihood estimation and sampling through invertible transformations. A key challenge is to design linear layers that enhance expressiveness while maintaining efficient computation of the Jacobian determinant and inverse. We introduce a novel invertible linear layer based on the product of circulant and diagonal matrices. This decomposition reduces parameter complexity from $\mathcal{O}(n^2)$ to $\mathcal{O}(mn)$ using $m$ diagonal matrices and $m-1$ circulant matrices while still approximating general linear transformations. By leveraging the Fast Fourier Transform, our approach reduces the time complexity of matrix inversion from $\mathcal{O}(n^3)$ to $\mathcal{O}(mn\log n)$ and that of computing the log-determinant from $\mathcal{O}(n^3)$ to $\mathcal{O}(mn)$, where $n$ is the input dimension. We build upon this layer to develop Circulant-Diagonal Flow (CDFlow), which achieves strong density estimation on natural image datasets and effectively models data with inherent periodic structure. Furthermore, CDFlow significantly accelerates key operations in normalizing flows, providing practical benefits for scalable generative modeling....

---

### 55. The Denario project: Deep knowledge AI agents for scientific discovery

**Authors:** Francisco Villaescusa-Navarro, Boris Bolliet, Pablo Villanueva-Domingo, Adrian E. Bayer, Aidan Acquah, Chetana Amancharla, Almog Barzilay-Siegal, Pablo Bermejo, Camille Bilodeau, Pablo Cárdenas Ramírez, Miles Cranmer, Urbano L. França, ChangHoon Hahn, Yan-Fei Jiang, Raul Jimenez, Jun-Young Lee, Antonio Lerario, Osman Mamun, Thomas Meier, Anupam A. Ojha, Pavlos Protopapas, Shimanto Roy, David N. Spergel, Pedro Tarancón-Álvarez, Ujjwal Tiwari, Matteo Viel, Digvijay Wadekar, Chi Wang, Bonny Y. Wang, Licong Xu, Yossi Yovel, Shuwen Yue, Wen-Han Zhou, Qiyao Zhu, Jiajun Zou, Íñigo Zubeldia

**Published:** 2025-10-30

**Category:** cs.AI

**ID:** 2510.26887v1

**Link:** [http://arxiv.org/abs/2510.26887v1](http://arxiv.org/abs/2510.26887v1)

**Summary:** We present Denario, an AI multi-agent system designed to serve as a scientific research assistant. Denario can perform many different tasks, such as generating ideas, checking the literature, developing research plans, writing and executing code, making plots, and drafting and reviewing a scientific paper. The system has a modular architecture, allowing it to handle specific tasks, such as generating an idea, or carrying out end-to-end scientific analysis using Cmbagent as a deep-research backend. In this work, we describe in detail Denario and its modules, and illustrate its capabilities by presenting multiple AI-generated papers generated by it in many different scientific disciplines such as astrophysics, biology, biophysics, biomedical informatics, chemistry, material science, mathematical physics, medicine, neuroscience and planetary science. Denario also excels at combining ideas from different disciplines, and we illustrate this by showing a paper that applies methods from quantum physics and machine learning to astrophysical data. We report the evaluations performed on these papers by domain experts, who provided both numerical scores and review-like feedback. We then highlight the strengths, weaknesses, and limitations of the current system. Finally, we discuss the ethical implications of AI-driven research and reflect on how such technology relates to the philosophy of science. We publicly release the code at https://github.com/AstroPilot-AI/Denario. A Denario demo can also be run directly on the web at https://huggingface.co/spaces/astropilot-ai/Denario, and the full app will be deployed on the cloud....

---

### 56. Adversarial generalization of unfolding (model-based) networks

**Authors:** Vicky Kouni

**Published:** 2025-09-18

**Category:** cs.LG

**ID:** 2509.15370v3

**Link:** [http://arxiv.org/abs/2509.15370v3](http://arxiv.org/abs/2509.15370v3)

**Summary:** Unfolding networks are interpretable networks emerging from iterative algorithms, incorporate prior knowledge of data structure, and are designed to solve inverse problems like compressed sensing, which deals with recovering data from noisy, missing observations. Compressed sensing finds applications in critical domains, from medical imaging to cryptography, where adversarial robustness is crucial to prevent catastrophic failures. However, a solid theoretical understanding of the performance of unfolding networks in the presence of adversarial attacks is still in its infancy. In this paper, we study the adversarial generalization of unfolding networks when perturbed with $l_2$-norm constrained attacks, generated by the fast gradient sign method. Particularly, we choose a family of state-of-the-art overaparameterized unfolding networks and deploy a new framework to estimate their adversarial Rademacher complexity. Given this estimate, we provide adversarial generalization error bounds for the networks under study, which are tight with respect to the attack level. To our knowledge, this is the first theoretical analysis on the adversarial generalization of unfolding networks. We further present a series of experiments on real-world data, with results corroborating our derived theory, consistently for all data. Finally, we observe that the family's overparameterization can be exploited to promote adversarial robustness, shedding light on how to efficiently robustify neural networks....

---

### 57. Impact of hydrogenation on the structure, chemistry, and electrical properties of flame-synthesized carbon nanoparticle films

**Authors:** Luca Basta, Francesca Picca, Pegah Darvehi, Vincenzo Pagliara, Alberto Aloisio, Mario Commodo, Patrizia Minutolo, Vito Mennella, Stefan Heun, Stefano Veronesi, Andrea D'Anna

**Published:** 2025-10-30

**Category:** cond-mat.mes-hall

**ID:** 2510.26733v1

**Link:** [http://arxiv.org/abs/2510.26733v1](http://arxiv.org/abs/2510.26733v1)

**Summary:** The interaction between hydrogen atoms and carbon nanoparticles is a fundamental process governing the properties of carbonaceous materials in environments ranging from combustion systems to the interstellar medium. This study investigates the effects of controlled atomic hydrogen exposure on young and mature soot nanoparticles, generated in premixed ethylene-air flames, and deposited on substrates. We employed a multi-technique approach to characterize the chemical, mechanical, and electrical evolution of the films. In-situ infrared spectroscopy revealed non-monotonic behavior: an initial increase in aliphatic CH bonds was observed, followed by a decrease at higher hydrogen fluences. This was accompanied by a continuous decrease in the aromatic C=C signal. Atomic force microscopy showed a significant increase in the Young's modulus of the film for both sample types after hydrogenation. This mechanical change was correlated with an increase in the I(D)/I(G) ratio from Raman spectroscopy. Furthermore, both macroscopic current vs. voltage and local scanning tunneling spectroscopy measurements demonstrated a notable increase in electrical conductivity. For single just-formed soot particles, moreover, a hydrogen-induced transformation from a semiconductive to a semi-metallic nature was observed. The collective evidence points towards an H-induced CC cross-linking mechanism within the nanoparticle films. We propose that atomic hydrogen facilitates the formation of radical sites, which promotes covalent bond formation between adjacent particles or molecular units, creating a more interconnected and rigid network, with smaller interlayer distance. These findings provide crucial insights into the structural evolution of carbonaceous materials in hydrogen-rich environments, with direct implications for understanding soot formation and for the tailored design of carbon-based materials....

---

### 58. PoseDiff: A Unified Diffusion Model Bridging Robot Pose Estimation and Video-to-Action Control

**Authors:** Haozhuo Zhang, Michele Caprio, Jing Shao, Qiang Zhang, Jian Tang, Shanghang Zhang, Wei Pan

**Published:** 2025-09-29

**Category:** cs.RO

**ID:** 2509.24591v2

**Link:** [http://arxiv.org/abs/2509.24591v2](http://arxiv.org/abs/2509.24591v2)

**Summary:** We present PoseDiff, a conditional diffusion model that unifies robot state estimation and control within a single framework. At its core, PoseDiff maps raw visual observations into structured robot states-such as 3D keypoints or joint angles-from a single RGB image, eliminating the need for multi-stage pipelines or auxiliary modalities. Building upon this foundation, PoseDiff extends naturally to video-to-action inverse dynamics: by conditioning on sparse video keyframes generated by world models, it produces smooth and continuous long-horizon action sequences through an overlap-averaging strategy. This unified design enables scalable and efficient integration of perception and control. On the DREAM dataset, PoseDiff achieves state-of-the-art accuracy and real-time performance for pose estimation. On Libero-Object manipulation tasks, it substantially improves success rates over existing inverse dynamics modules, even under strict offline settings. Together, these results show that PoseDiff provides a scalable, accurate, and efficient bridge between perception, planning, and control in embodied AI. The video visualization results can be found on the project page: https://haozhuo-zhang.github.io/PoseDiff-project-page/....

---

### 59. StyleGuard: Preventing Text-to-Image-Model-based Style Mimicry Attacks by Style Perturbations

**Authors:** Yanjie Li, Wenxuan Zhang, Xinqi Lyu, Yihao Liu, Bin Xiao

**Published:** 2025-05-24

**Category:** cs.CV

**ID:** 2505.18766v2

**Link:** [http://arxiv.org/abs/2505.18766v2](http://arxiv.org/abs/2505.18766v2)

**Summary:** Recently, text-to-image diffusion models have been widely used for style mimicry and personalized customization through methods such as DreamBooth and Textual Inversion. This has raised concerns about intellectual property protection and the generation of deceptive content. Recent studies, such as Glaze and Anti-DreamBooth, have proposed using adversarial noise to protect images from these attacks. However, recent purification-based methods, such as DiffPure and Noise Upscaling, have successfully attacked these latest defenses, showing the vulnerabilities of these methods. Moreover, present methods show limited transferability across models, making them less effective against unknown text-to-image models. To address these issues, we propose a novel anti-mimicry method, StyleGuard. We propose a novel style loss that optimizes the style-related features in the latent space to make it deviate from the original image, which improves model-agnostic transferability. Additionally, to enhance the perturbation's ability to bypass diffusion-based purification, we designed a novel upscale loss that involves ensemble purifiers and upscalers during training. Extensive experiments on the WikiArt and CelebA datasets demonstrate that StyleGuard outperforms existing methods in robustness against various transformations and purifications, effectively countering style mimicry in various models. Moreover, StyleGuard is effective on different style mimicry methods, including DreamBooth and Textual Inversion. The code is available at https://github.com/PolyLiYJ/StyleGuard....

---

### 60. QuantumBench: A Benchmark for Quantum Problem Solving

**Authors:** Shunya Minami, Tatsuya Ishigaki, Ikko Hamamura, Taku Mikuriya, Youmi Ma, Naoaki Okazaki, Hiroya Takamura, Yohichi Suzuki, Tadashi Kadowaki

**Published:** 2025-10-30

**Category:** cs.AI

**ID:** 2511.00092v1

**Link:** [http://arxiv.org/abs/2511.00092v1](http://arxiv.org/abs/2511.00092v1)

**Summary:** Large language models are now integrated into many scientific workflows, accelerating data analysis, hypothesis generation, and design space exploration. In parallel with this growth, there is a growing need to carefully evaluate whether models accurately capture domain-specific knowledge and notation, since general-purpose benchmarks rarely reflect these requirements. This gap is especially clear in quantum science, which features non-intuitive phenomena and requires advanced mathematics. In this study, we introduce QuantumBench, a benchmark for the quantum domain that systematically examine how well LLMs understand and can be applied to this non-intuitive field. Using publicly available materials, we compiled approximately 800 questions with their answers spanning nine areas related to quantum science and organized them into an eight-option multiple-choice dataset. With this benchmark, we evaluate several existing LLMs and analyze their performance in the quantum domain, including sensitivity to changes in question format. QuantumBench is the first LLM evaluation dataset built for the quantum domain, and it is intended to guide the effective use of LLMs in quantum research....

---

### 61. Theoretical design of the large topological magnetoelectric effect in the Co-intercalated NbS$_2$ structure

**Authors:** Hyowon Park, Ivar Martin

**Published:** 2025-10-30

**Category:** cond-mat.mtrl-sci

**ID:** 2510.26054v1

**Link:** [http://arxiv.org/abs/2510.26054v1](http://arxiv.org/abs/2510.26054v1)

**Summary:** A triangular Co-ion lattice intercalated between 1-H NbS$_2$ layers can exhibit a large anomalous Hall effect (AHE) due to the finite scalar spin chirality originating from the non-coplanar $3q$ ordering of Co spins. This large AHE occurs when the scalar spin chirality is uniform in all Co layers, as indeed found in the Co$_{1/3}$NbS$_2$ case [Phys. Rev. Mater. 6, 024201 (2022)]. However, if the spin chirality were staggered with the opposite signs in the adjacent Co layers, the net AHE would disappear, yielding instead the topological magneto-electric effect. Here, we theoretically verify that a transverse electric field generates a finite orbital magnetization under such conditions, consistent with the axion-like coupling. Using first-principles calculations, we show that the resulting magneto-electric coupling, $α^{zz}$ can be as large as 0.9 $e^2/2h$. We also demonstrate that the inter-layer magnetic coupling in these materials can be tuned by strain, enabling the switching between the AHE and the axionic states....

---

### 62. A General and Streamlined Differentiable Optimization Framework

**Authors:** Andrew W. Rosemberg, Joaquim Dias Garcia, François Pacaud, Robert B. Parker, Benoît Legat, Kaarthik Sundar, Russell Bent, Pascal Van Hentenryck

**Published:** 2025-10-29

**Category:** cs.LG

**ID:** 2510.25986v1

**Link:** [http://arxiv.org/abs/2510.25986v1](http://arxiv.org/abs/2510.25986v1)

**Summary:** Differentiating through constrained optimization problems is increasingly central to learning, control, and large-scale decision-making systems, yet practical integration remains challenging due to solver specialization and interface mismatches. This paper presents a general and streamlined framework-an updated DiffOpt.jl-that unifies modeling and differentiation within the Julia optimization stack. The framework computes forward - and reverse-mode solution and objective sensitivities for smooth, potentially nonconvex programs by differentiating the KKT system under standard regularity assumptions. A first-class, JuMP-native parameter-centric API allows users to declare named parameters and obtain derivatives directly with respect to them - even when a parameter appears in multiple constraints and objectives - eliminating brittle bookkeeping from coefficient-level interfaces. We illustrate these capabilities on convex and nonconvex models, including economic dispatch, mean-variance portfolio selection with conic risk constraints, and nonlinear robot inverse kinematics. Two companion studies further demonstrate impact at scale: gradient-based iterative methods for strategic bidding in energy markets and Sobolev-style training of end-to-end optimization proxies using solver-accurate sensitivities. Together, these results demonstrate that differentiable optimization can be deployed as a routine tool for experimentation, learning, calibration, and design-without deviating from standard JuMP modeling practices and while retaining access to a broad ecosystem of solvers....

---

### 63. A Geometric Pathway for Tuning Ferroelectric Properties via Polar State Reconfiguration

**Authors:** Hao-Cheng Thong, Bo Wu, Fan Hu, Pedro B. Groszewicz, Chen-Bo-Wen Li, Jun Chen, Mao-Hua Zhang, Dragan Damjanovic, Ben Xu, Ke Wang

**Published:** 2025-10-29

**Category:** cond-mat.mtrl-sci

**ID:** 2510.25142v1

**Link:** [http://arxiv.org/abs/2510.25142v1](http://arxiv.org/abs/2510.25142v1)

**Summary:** We report the discovery of a geometric pathway for tuning ferroelectric properties through thermally driven reconfiguration between coexisting polar states in Li-substituted NaNbO3. Using first-principles density functional theory calculation and 7Li solid-state nuclear magnetic resonance spectroscopy measurement, we reveal that Li substitution creates two distinct polar configurations whose transformation under annealing enhances the Curie temperature and induces piezoelectric hardening. Our findings establish a geometrically-driven polar state reconfiguration mechanism, providing a general design principle for ferroics whereby macroscopic functional properties can be engineered via lattice geometry....

---

### 64. Kolmogorov-Arnold Energy Models: Fast and Interpretable Generative Modeling

**Authors:** Prithvi Raj

**Published:** 2025-06-17

**Category:** cs.LG

**ID:** 2506.14167v6

**Link:** [http://arxiv.org/abs/2506.14167v6](http://arxiv.org/abs/2506.14167v6)

**Summary:** Learning an energy-based model (EBM) in the latent space of a top-down generative model offers a powerful framework for generation across many data modalities. However, it remains unclear how its interpretability can be used to guide model design, improve generative quality, and reduce training time. Moreover, the reliance on Langevin Monte Carlo (LMC) sampling presents challenges in efficiency and sampling multimodal latent distributions. We propose a novel adaptation of the Kolmogorov-Arnold representation theorem for generative modeling and introduce the Kolmogorov-Arnold Energy Model (KAEM) to take advantage of structural and inductive biases. By constraining the prior to univariate relationships, KAEM enables fast and exact inference via the inverse transform method. With the low dimensionality of the latent space and suitable inductive biases encoded, we demonstrate that importance sampling (IS) becomes a viable, unbiased, and highly efficient posterior sampler. For domains where IS fails, we introduce a strategy based on population-based LMC, decomposing the posterior into a sequence of annealed distributions to improve LMC mixing. KAEM balances common generative modeling trade-offs, offering fast inference, interpretability, and stable training, while being naturally suited to Zettascale Computing hardware....

---

### 65. Stabilisation of hBN/SiC Heterostructures with Vacancies and Transition-Metal Atoms

**Authors:** Arsalan Hashemi, Nima Ghafari Cherati, Sadegh Ghaderzadeh, Yanzhou Wang, Mahdi Ghorbani-Asl, Tapio Ala-Nissila

**Published:** 2025-10-28

**Category:** cond-mat.mtrl-sci

**ID:** 2510.24952v1

**Link:** [http://arxiv.org/abs/2510.24952v1](http://arxiv.org/abs/2510.24952v1)

**Summary:** When two-dimensional atomic layers of different materials are brought into close proximity to form van der Waals (vdW) heterostructures, interactions between adjacent layers significantly influence their physicochemical properties. These effects seem particularly pronounced when the interface exhibits local order and near-perfect structural alignment, leading to the emergence of Moiré patterns. Using quantum mechanical density functional theory calculations, we propose a prototypical bilayer heterostructure composed of hexagonal boron nitride (hBN) and silicon carbide (SiC), characterized by a lattice mismatch of 18.77\% between their primitive unit cells. We find that the removal of boron atoms from specific lattice sites can convert the interlayer interaction from weak vdW coupling to robust localized silicon-nitrogen covalent bonding. Motivated by this, we study the binding of transition-metal adatoms and formulate design guidelines to enhance surface reactivity, thereby enabling the controlled isolation of single-metal atoms. Our machine-learning-assisted molecular dynamics simulations confirm both dynamical stability and metal anchoring feasibility at finite temperatures. Our results suggest the hBN/SiC heterostructure as a versatile platform for atomically precise transition-metal functionalization, having potential for next-generation catalytic energy-conversion technologies....

---

### 66. SHA-256 Infused Embedding-Driven Generative Modeling of High-Energy Molecules in Low-Data Regimes

**Authors:** Siddharth Verma, Alankar Alankar

**Published:** 2025-10-28

**Category:** cs.LG

**ID:** 2510.25788v1

**Link:** [http://arxiv.org/abs/2510.25788v1](http://arxiv.org/abs/2510.25788v1)

**Summary:** High-energy materials (HEMs) are critical for propulsion and defense domains, yet their discovery remains constrained by experimental data and restricted access to testing facilities. This work presents a novel approach toward high-energy molecules by combining Long Short-Term Memory (LSTM) networks for molecular generation and Attentive Graph Neural Networks (GNN) for property predictions. We propose a transformative embedding space construction strategy that integrates fixed SHA-256 embeddings with partially trainable representations. Unlike conventional regularization techniques, this changes the representational basis itself, reshaping the molecular input space before learning begins. Without recourse to pretraining, the generator achieves 67.5% validity and 37.5% novelty. The generated library exhibits a mean Tanimoto coefficient of 0.214 relative to training set signifying the ability of framework to generate a diverse chemical space. We identified 37 new super explosives higher than 9 km/s predicted detonation velocity....

---

### 67. Molecular simulations of Perovskites CsXI3 (X = Pb,Sn) Using Machine-Learning Interatomic Potentials

**Authors:** Atefe Ebrahimi, Franco Pellegrini, Stefano De Gironcoli

**Published:** 2025-10-28

**Category:** cond-mat.mtrl-sci

**ID:** 2510.24874v1

**Link:** [http://arxiv.org/abs/2510.24874v1](http://arxiv.org/abs/2510.24874v1)

**Summary:** Cesium based halide perovskites, such as CsPbI3 and CsSnI3, have emerged as exceptional candidates for next generation photovoltaic and optoelectronic technologies, but their practical application is limited by temperature dependent phase transitions and structural instabilities. Here, we develop machine learning interatomic potentials within the LATTE framework to simulate these materials with near experimental accuracy at a fraction of the computational cost compared to previous computational studies. Our molecular dynamics simulations based on the trained MLIPs reproduce energies and forces across multiple phases, enabling large scale simulations that capture cubic tetragonal orthorhombic transitions, lattice parameters, and octahedral tilting with unprecedented resolution. We find that Pb based perovskites exhibit larger octahedral tilts and higher phase transition temperatures than Sn based analogues, reflecting stronger bonding and enhanced structural stability, whereas Sn based perovskites display reduced tilts and lower barriers, suggesting tunability through compositional or interface engineering. Beyond these systems, our work demonstrates that MLIPs can bridge first principles accuracy with simulation efficiency, providing a robust framework for exploring phase stability, anharmonicity, and rational design in next generation halide perovskites....

---

### 68. Deep-Learning-Empowered Programmable Topolectrical Circuits

**Authors:** Hao Jia, Shanglin Yang, Jiajun He, Shuo Liu, Haoxiang Chen, Ce Shang, Shaojie Ma, Peng Han, Ching Hua Lee, Zhen Gao, Yun Lai, Tie Jun Cui

**Published:** 2025-10-28

**Category:** cond-mat.dis-nn

**ID:** 2510.24463v1

**Link:** [http://arxiv.org/abs/2510.24463v1](http://arxiv.org/abs/2510.24463v1)

**Summary:** Topolectrical circuits provide a versatile platform for exploring and simulating modern physical models. However, existing approaches suffer from incomplete programmability and ineffective feature prediction and control mechanisms, hindering the investigation of physical phenomena on an integrated platform and limiting their translation into practical applications. Here, we present a deep learning empowered programmable topolectrical circuits (DLPTCs) platform for physical modeling and analysis. By integrating fully independent, continuous tuning of both on site and off site terms of the lattice Hamiltonian, physics graph informed inverse state design, and immediate hardware verification, our system bridges the gap between theoretical modeling and practical realization. Through flexible control and adiabatic path engineering, we experimentally observe the boundary states without global symmetry in higher order topological systems, their adiabatic phase transitions, and the flat band like characteristic corresponding to Landau levels in the circuit. Incorporating a physics graph informed mechanism with a generative AI model for physics exploration, we realize arbitrary, position controllable on board Anderson localization, surpassing conventional random localization. Utilizing this unique capability with high fidelity hardware implementation, we further demonstrate a compelling cryptographic application: hash based probabilistic information encryption by leveraging Anderson localization with extensive disorder configurations, enabling secure delivery of full ASCII messages....

---

### 69. Tunable hyperbolic Landau-level polaritons in charge-neutral graphene nanoribbon metasurfaces

**Authors:** Kateryna Domina, Tetiana Slipchenko, D. -H. -Minh Nguyen, Alexey B. Kuzmenko, Luis Martin-Moreno, Dario Bercioux, Alexey Y. Nikitin

**Published:** 2025-06-30

**Category:** cond-mat.mes-hall

**ID:** 2506.23786v3

**Link:** [http://arxiv.org/abs/2506.23786v3](http://arxiv.org/abs/2506.23786v3)

**Summary:** Magnetized charge-neutral graphene supports collective hybrid electronic excitations - polaritons - which have quantum origin. In contrast to polaritons in doped graphene, which arise from intraband electronic transitions, those in charge-neutral graphene originate from interband transitions between Landau levels, enabled by the applied magnetic field. Control of such quantum polaritons and shaping their wavefronts remains totally unexplored. Here we design an artificial two-dimensional quantum material formed by charge-neutral graphene nanoribbons exposed to an external magnetic field. In such metasurface, quantum polaritons acquire a hyperbolic dispersion. We find that the topology of the isofrequency curves of quantum hyperbolic magnetoexciton polaritons excited in this quantum material can change, so that the shape of isofrequency curves transforms from a closed to open one by tuning the external magnetic field strength. At the topological transition, we observe canalization phenomena, consisting of the propagation of all the polaritonic plane waves in the continuum along the same direction when excited by a point source. From a general perspective, our fundamental findings introduce a novel type of actively-tunable quantum polaritons with hyperbolic dispersion and can be further generalized to other types of quantum materials and polaritons in them. In practice, quantum hyperbolic polaritons can be used for applications related to quantum sensing and computing....

---

### 70. Geometric Mixture Models for Electrolyte Conductivity Prediction

**Authors:** Anyi Li, Jiacheng Cen, Songyou Li, Mingze Li, Yang Yu, Wenbing Huang

**Published:** 2025-10-17

**Category:** cs.LG

**ID:** 2510.15403v2

**Link:** [http://arxiv.org/abs/2510.15403v2](http://arxiv.org/abs/2510.15403v2)

**Summary:** Accurate prediction of ionic conductivity in electrolyte systems is crucial for advancing numerous scientific and technological applications. While significant progress has been made, current research faces two fundamental challenges: (1) the lack of high-quality standardized benchmarks, and (2) inadequate modeling of geometric structure and intermolecular interactions in mixture systems. To address these limitations, we first reorganize and enhance the CALiSol and DiffMix electrolyte datasets by incorporating geometric graph representations of molecules. We then propose GeoMix, a novel geometry-aware framework that preserves Set-SE(3) equivariance-an essential but challenging property for mixture systems. At the heart of GeoMix lies the Geometric Interaction Network (GIN), an equivariant module specifically designed for intermolecular geometric message passing. Comprehensive experiments demonstrate that GeoMix consistently outperforms diverse baselines (including MLPs, GNNs, and geometric GNNs) across both datasets, validating the importance of cross-molecular geometric interactions and equivariant message passing for accurate property prediction. This work not only establishes new benchmarks for electrolyte research but also provides a general geometric learning framework that advances modeling of mixture systems in energy materials, pharmaceutical development, and beyond....

---

### 71. Strong Intra- and Interchain Orbital Coupling Leads to Multiband and High Thermoelectric Performance in Na$_2$Au$X$ ($X$ = P, As, Sb, and Bi)

**Authors:** Zhonghao Xia, Zhilong Yang, Yali Yang, Kaile Ren, Jiangang He

**Published:** 2025-10-28

**Category:** cond-mat.mtrl-sci

**ID:** 2510.23983v1

**Link:** [http://arxiv.org/abs/2510.23983v1](http://arxiv.org/abs/2510.23983v1)

**Summary:** The intrinsic coupling among electrical conductivity ($σ$), Seebeck coefficient ($S$), and lattice thermal conductivity ($κ_{\mathrm{L}}$) imposes a fundamental limit on the dimensionless figure of merit $ZT$ in thermoelectric (TE) materials. Increasing band degeneracy can effectively balance $σ$ and $S$, enabling a high power factor (PF, $S^{2}σ$). However, compounds with intrinsically large band degeneracy are scarce. Here, we present an unconventional strategy to realize elevated band degeneracy in zigzag-chain Na$_2$Au$X$ ($X$ = P, As, Sb, Bi) compounds by harnessing strong intra- and interchain orbital coupling. Pronounced hybridization between Au-$d_{z^{2}}$ and $X$-$p_{z}$ orbitals along the Au--$X$ zigzag chains, together with unexpectedly strong interchain $X$-$p_{x}/p_{y}$ coupling, produces a highly dispersive, multivalley valence band structure that supports an exceptional PF. Concurrently, the intrinsically weak interchain interactions arising from the quasi-one-dimensional framework, together with the weakened Au--$X$ and Au--Au bonds within the chains due to filling of $p$-$d^{*}$ antibonding states, result in an ultralow $κ_{\mathrm{L}}$. First-principles calculations combined with Boltzmann transport theory predict that $p$-type Na$_2$AuBi achieves a PF of $63.9\,μ\mathrm{W}\,\mathrm{cm}^{-1}\,\mathrm{K}^{-2}$, an ultralow $κ_{\mathrm{L}}$ of $0.49\,\mathrm{W}\,\mathrm{m}^{-1}\,\mathrm{K}^{-1}$, and a maximum $ZT$ of $4.7$ along the zigzag-chain direction at $800\,\mathrm{K}$. This work establishes a new design paradigm for high-efficiency TE materials by exploiting substantial orbital overlap in structurally weakly bonded, quasi-one-dimensional systems, opening promising avenues for the discovery and engineering of next-generation high-performance TE materials....

---

### 72. DeFecT-FF: Accelerated Modeling of Defects in Cd-Zn--Te-Se-S Compounds Combining High-Throughput DFT and Machine Learning Force Fields

**Authors:** Md Habibur Rahman, Arun Mannodi-Kanakkithodi

**Published:** 2025-10-27

**Category:** cond-mat.mtrl-sci

**ID:** 2510.23514v1

**Link:** [http://arxiv.org/abs/2510.23514v1](http://arxiv.org/abs/2510.23514v1)

**Summary:** We developed DeFecT-FF, a framework for predicting the energies and ground-state configurations of native point defects, extrinsic dopants, impurities, and defect complexes in zincblende-phase Cd/Zn-Te/Se/S compounds relevant to CdTe-based solar cells. The framework combines high-throughput DFT data with crystal graph-based machine learning force fields (MLFFs) trained to reproduce DFT energies and forces. Alloying at Cd or Te sites offers a route to tune the electronic and defect properties of CdTe absorbers for improved solar efficiency. Given the vast number of possible defect types, charge states, and symmetry-breaking configurations, traditional DFT approaches are computationally prohibitive. Our dataset includes GGA-PBE and HSE06-optimized structures for bulk, alloyed, interface, and grain-boundary systems. Using active learning, we expanded the dataset and trained MLFFs to accurately predict energies across charge states. The model enabled rapid screening and discovery of new low-energy defect configurations, validated through HSE06 calculations with spin-orbit coupling. The DeFecT-FF framework is publicly available as a nanoHUB tool, allowing users to upload crystallographic files, automatically generate defects, and compute defect formation energies versus Fermi level and chemical potentials, greatly reducing the need for expensive DFT simulations....

---

### 73. Design principles for amorphous solid-state electrolytes

**Authors:** Qifan Yang, Xiao Fu, Xuhe Gong, Jingchen Lian, Liqi Wang, Ruijuan Xiao, Yong-Sheng Hu, Hong Li

**Published:** 2025-10-27

**Category:** cond-mat.mtrl-sci

**ID:** 2510.23251v1

**Link:** [http://arxiv.org/abs/2510.23251v1](http://arxiv.org/abs/2510.23251v1)

**Summary:** Amorphous solid-state electrolytes (SSEs) offer unique advantages for next-generation batteries, but their rational design is hindered by an unclear structure-property relationship. This study establishes universal design principles through atomistic simulations of 32 amorphous Li-M-X systems (M = B, Al, Si, P; X = F, Cl, Br, I, O, S, Se, N). We identify four structure types governed by a rule that saturated M-X groups with more negative charges preferentially form M-X-M chains, identify paddle-wheel and cooperative migration as two favorable transport mechanisms that are significantly enhanced in amorphous structures. We also pinpoint Oxides and fluorides as optimal for electrochemical and hydrolytic stability, and reveal bulk modulus as a simple predictor for $Li^+$ mobility. These insights are integrated into a practical design diagram, providing a novel and valuable framework for advancing high-performance amorphous SSEs....

---

### 74. P-orbital spin generator with large spin Hall angle and long spin diffusion length

**Authors:** Gen Li, Ying Zhang, Xiaoguang Xu, Lei Shen, Zheng Feng, Kangkang Meng, Ang Li, Lu Cheng, Kang He, Wei Tan, Yong Wu, Yihong Wu, Yong Jiang

**Published:** 2025-03-27

**Category:** cond-mat.mtrl-sci

**ID:** 2503.21129v2

**Link:** [http://arxiv.org/abs/2503.21129v2](http://arxiv.org/abs/2503.21129v2)

**Summary:** High density data storage and spin-logic devices require highly efficient all-electric control of spin moments. So far, charge-to-spin conversion through the spin Hall effect (SHE) highly limits to d-orbital materials associated with strong spin-orbit coupling (SOC), especially heavy metals. However, d-orbital heavy metals with strong SOC results in a short spin diffusion length, which restricts the spin transport and accumulation in spintronic devices. Therefore, it is urgent to discovery new SHE materials with both large spin Hall conductivity and high spin transport ability beyond d-orbital materials. Here, we experimentally report a large charge to spin conversion in a p-orbital In2Bi alloy, exhibiting the coexistence of a large spin Hall angle and a long spin diffusion length (4 times that of Pt). Our first-principles calculations reveal that small gap openings near the Fermi level lead to large Berry curvature-related spin Hall conductivity. Due to the delocalized nature of p-orbitals of In2Bi, its spin current can overcome the physical barriers between spin Hall angle and spin diffusion length in d-orbital metals, thereby advancing the development of high performance spintronic devices....

---

### 75. Mastering energy landscapes via liquid liquid phase separation to program active supramolecular coassembly from the nano to macro scale

**Authors:** Yuanhao Wu, Alexander van Teijlingen, Julie Watts, Zhiquan Yu, Shanshan Su, Jose Carlos RodriguezCabello, Lihi Abramovich, Tell Tuttle, Alvaro Mata

**Published:** 2025-10-27

**Category:** cond-mat.soft

**ID:** 2510.23017v1

**Link:** [http://arxiv.org/abs/2510.23017v1](http://arxiv.org/abs/2510.23017v1)

**Summary:** The energy landscape dictates pathways and outcomes in supramolecular selfassembly, yet harnessing it from the nano to the macro scales remains a major challenge. Here, we demonstrate liquid liquid phase separation (LLPS) as a powerful tool to navigate and engineer the energy landscapes of coassembly systems comprising disordered proteins and peptides. We quantitatively map the energy barriers and transition states governing structural transitions, enabling predictive on off control of assembly and hierarchical order from nano to macro scales. By integrating supramolecular biofabrication, we achieve spatially organized architectures with life like non equilibrium behaviour. Crucially, assembly stability and scalable selfsorting are shown to depend on accessing minimum energy states, regardless of whether the co assembled structures are disordered or ordered. This work establishes energy landscape mediation via LLPS as a general framework for designing lifelike, hierarchically structured materials....

---

### 76. Multi-Agent Conditional Diffusion Model with Mean Field Communication as Wireless Resource Allocation Planner

**Authors:** Kechen Meng, Sinuo Zhang, Rongpeng Li, Xiangming Meng, Chan Wang, Ming Lei, Zhifeng Zhao

**Published:** 2025-10-27

**Category:** cs.AI

**ID:** 2510.22969v1

**Link:** [http://arxiv.org/abs/2510.22969v1](http://arxiv.org/abs/2510.22969v1)

**Summary:** In wireless communication systems, efficient and adaptive resource allocation plays a crucial role in enhancing overall Quality of Service (QoS). While centralized Multi-Agent Reinforcement Learning (MARL) frameworks rely on a central coordinator for policy training and resource scheduling, they suffer from scalability issues and privacy risks. In contrast, the Distributed Training with Decentralized Execution (DTDE) paradigm enables distributed learning and decision-making, but it struggles with non-stationarity and limited inter-agent cooperation, which can severely degrade system performance. To overcome these challenges, we propose the Multi-Agent Conditional Diffusion Model Planner (MA-CDMP) for decentralized communication resource management. Built upon the Model-Based Reinforcement Learning (MBRL) paradigm, MA-CDMP employs Diffusion Models (DMs) to capture environment dynamics and plan future trajectories, while an inverse dynamics model guides action generation, thereby alleviating the sample inefficiency and slow convergence of conventional DTDE methods. Moreover, to approximate large-scale agent interactions, a Mean-Field (MF) mechanism is introduced as an assistance to the classifier in DMs. This design mitigates inter-agent non-stationarity and enhances cooperation with minimal communication overhead in distributed settings. We further theoretically establish an upper bound on the distributional approximation error introduced by the MF-based diffusion generation, guaranteeing convergence stability and reliable modeling of multi-agent stochastic dynamics. Extensive experiments demonstrate that MA-CDMP consistently outperforms existing MARL baselines in terms of average reward and QoS metrics, showcasing its scalability and practicality for real-world wireless network optimization....

---

### 77. Numerical and data-driven modeling of spall failure in polycrystalline ductile materials

**Authors:** Indrashish Saha, Lori Graham-Brady

**Published:** 2025-07-04

**Category:** cond-mat.mtrl-sci

**ID:** 2507.03706v3

**Link:** [http://arxiv.org/abs/2507.03706v3](http://arxiv.org/abs/2507.03706v3)

**Summary:** Developing materials with tailored mechanical performance requires iteration over a large number of proposed designs. When considering dynamic fracture, experiments at every iteration are usually infeasible. While high-fidelity, physics-based simulations can potentially reduce experimental efforts, they remain computationally expensive. As a faster alternative, key dynamic properties can be predicted directly from microstructural images using deep-learning surrogate models. In this work, the spallation of ductile polycrystals under plate-impact loading at strain rates of O(10^6 s^-1) is considered. A physics-based numerical model that couples crystal plasticity and a cohesive zone model is used to generate data for the surrogate models. Three architectures - 3D U-Net, 3D Fourier Neural Operator (FNO-3D), and U-FNO were trained on the particle-velocity field data from the numerical model. The generalization of the models was evaluated using microstructures with varying grain sizes and aspect ratios. U-FNO and 3D U-Net performed significantly better than FNO-3D across all datasets. Furthermore, U-FNO and 3D U-Net exhibited comparable accuracy for every metric considered in this study. However, training the U-FNO requires almost twice the computational effort compared to the 3D U-Net, making it a desirable option for a surrogate model....

---

### 78. Multiscale Modeling of Abnormal Grain Growth: Role of Solute Segregation and Grain Boundary Character

**Authors:** Albert Linda, Rajdip Mukherjee, Somnath Bhowmick

**Published:** 2025-10-17

**Category:** cond-mat.mtrl-sci

**ID:** 2510.15840v2

**Link:** [http://arxiv.org/abs/2510.15840v2](http://arxiv.org/abs/2510.15840v2)

**Summary:** Abnormal grain growth (AGG) influences the properties of polycrystalline materials; however, the underlying mechanisms, particularly the role of solute segregation at the grain boundary (GB), are difficult to quantify precisely. This study demonstrates a multiscale framework that integrates atomic-scale segregation energetics (using density functional theory) with mesoscale grain growth dynamics (using phase-field model) to investigate AGG, using $α$-Fe as an example system. Multisite segregation energies are calculated for symmetric tilt grain boundaries (STGBs) along the $\langle 110 \rangle$ axis for nine different solutes (Co, Cr, Mn, Mo, Nb, Ni, Ti, W, and V), encompassing three different types of coincident site lattice (CSL) boundaries: $\sum 3 (11\bar{2})$, $\sum 9 (\bar{2}21)$, and $\sum 3 (\bar{1}11)$. The model takes into account the effect of solute drag on GB mobility, estimated using a bulk solute concentration of 0.1 at\%. The results demonstrate that AGG originates due to GB anisotropy, the extent of which largely depends on the type of solute atom present. Such a complex dependence necessitates using a multiscale model to understand AGG comprehensively. In general, low-energy $Σ3$ boundaries are found to have higher mobility and show preferential growth for most of the solutes, other than Co. The study reveals how the distribution of GB types significantly influences AGG. When 10-30\% of the GBs are high-mobility type, crown-like morphologies are observed, leading to AGG. These findings underscore the critical role of GB chemistry and crystallography in governing AGG, and the model can be generalized to provide a predictive framework for controlling grain growth through strategic solute design in advanced alloys....

---

### 79. An Analytic Theory of Quantum Imaginary Time Evolution

**Authors:** Min Chen, Bingzhi Zhang, Quntao Zhuang, Junyu Liu

**Published:** 2025-10-26

**Category:** quant-ph

**ID:** 2510.22481v1

**Link:** [http://arxiv.org/abs/2510.22481v1](http://arxiv.org/abs/2510.22481v1)

**Summary:** Quantum imaginary time evolution (QITE) algorithm is one of the most promising variational quantum algorithms (VQAs), bridging the current era of Noisy Intermediate-Scale Quantum devices and the future of fully fault-tolerant quantum computing. Although practical demonstrations of QITE and its potential advantages over the general VQA trained with vanilla gradient descent (GD) in certain tasks have been reported, a first-principle, theoretical understanding of QITE remains limited. Here, we aim to develop an analytic theory for the dynamics of QITE. First, we show that QITE can be interpreted as a form of a general VQA trained with Quantum Natural Gradient Descent (QNGD), where the inverse quantum Fisher information matrix serves as the learning-rate tensor. This equivalence is established not only at the level of gradient update rules, but also through the action principle: the variational principle can be directly connected to the geometric geodesic distance in the quantum Fisher information metric, up to an integration constant. Second, for wide quantum neural networks, we employ the quantum neural tangent kernel framework to construct an analytic model for QITE. We prove that QITE always converges faster than GD-based VQA, though this advantage is suppressed by the exponential growth of Hilbert space dimension. This helps explain certain experimental results in quantum computational chemistry. Our theory encompasses linear, quadratic, and more general loss functions. We validate the analytic results through numerical simulations. Our findings establish a theoretical foundation for QITE dynamics and provide analytic insights for the first-principle design of variational quantum algorithms....

---

### 80. You Don't Need Prompt Engineering Anymore: The Prompting Inversion

**Authors:** Imran Khan

**Published:** 2025-10-25

**Category:** cs.CL

**ID:** 2510.22251v1

**Link:** [http://arxiv.org/abs/2510.22251v1](http://arxiv.org/abs/2510.22251v1)

**Summary:** Prompt engineering, particularly Chain-of-Thought (CoT) prompting, significantly enhances LLM reasoning capabilities. We introduce "Sculpting," a constrained, rule-based prompting method designed to improve upon standard CoT by reducing errors from semantic ambiguity and flawed common sense.
  We evaluate three prompting strategies (Zero Shot, standard CoT, and Sculpting) across three OpenAI model generations (gpt-4o-mini, gpt-4o, gpt-5) using the GSM8K mathematical reasoning benchmark (1,317 problems).
  Our findings reveal a "Prompting Inversion": Sculpting provides advantages on gpt-4o (97% vs. 93% for standard CoT), but becomes detrimental on gpt-5 (94.00% vs. 96.36% for CoT on full benchmark). We trace this to a "Guardrail-to-Handcuff" transition where constraints preventing common-sense errors in mid-tier models induce hyper-literalism in advanced models. Our detailed error analysis demonstrates that optimal prompting strategies must co-evolve with model capabilities, suggesting simpler prompts for more capable models....

---

### 81. Electric-Field-Tunable Luttinger compensated antiferromagnetism in double CrCl2 chains

**Authors:** Deping Guo, Weihan Zhang, Canbo Zong, Cong Wang, Wei Ji

**Published:** 2025-10-25

**Category:** cond-mat.mtrl-sci

**ID:** 2510.22153v1

**Link:** [http://arxiv.org/abs/2510.22153v1](http://arxiv.org/abs/2510.22153v1)

**Summary:** Luttinger compensated antiferromagnets (LcAFMs), combining spin polarization with vanishing net magnetization, offering distinct advantages for next-generation spintronic applications. Using first-principles calculations, we demonstrate that conventional antiferromagnetic CrCl2 double chains can be transformed into one-dimensional LcAFMs under an external electric field, exhibiting pronounced isotropic spin splitting. The magnitude of the splitting, as well as the band gap, can be effectively tuned by both in-plane and out-of-plane fields, thereby providing greater controllability than in two-dimensional counterparts. To further enhance the tunability, we design a nearly lattice-matched CrCl2/MoTe2 heterostructure and uncover that interfacial charge transfer generates a built-in electric field, inducing spin splitting comparable to that driven by external fields. These results establish interfacial engineering as a highly efficient route to realize and manipulate LcAFM states in low-dimensional magnets, expanding the design principles for spintronic functionalities at the nanoscale....

---

### 82. Tailoring dispersion and evanescent modes in multimodal nonlocal lattices using positive-only interactions

**Authors:** Lucas Rouhi, Christophe Droz

**Published:** 2025-10-24

**Category:** cond-mat.mtrl-sci

**ID:** 2510.21629v1

**Link:** [http://arxiv.org/abs/2510.21629v1](http://arxiv.org/abs/2510.21629v1)

**Summary:** Metamaterials derive their unconventional properties from engineered microstructures, with periodic lattices providing a versatile framework for modeling wave propagation. Dispersion relations, obtained from Bloch-Floquet theory, govern how waves propagate, attenuate, or localize within such systems. Extending interactions beyond nearest neighbors, through nonlocality, substantially enriches the design space of band diagrams, enabling phenomena such as negative or zero group velocities, roton-like extrema, and band-gap localization. However, existing approaches to dispersion tailoring often rely on analytical formulations or Fourier-based identifications, which become impractical for complex coupling mechanisms and offer limited control over physical constraints such as stiffness positivity. This work introduces a general interpolation-based framework for customizing dispersion relations in uniform nonlocal lattices. Rather than reconstructing full dispersion curves, the method enforces prescribed frequency-wavenumber points as interpolation constraints, enabling localized and tunable control of wave behavior. The formulation is applied to both spring- and beam-interaction lattices, and demonstrated on an Euler-Bernoulli beam model with adjustable nonlocal couplings. Through systematic parameter tuning, the framework enables the creation of rotons, the adjustment of group-velocity dispersion, and the design of evanescent waves with controlled exponential decay within band gaps, all while ensuring real, positive-only stiffness parameters and passive mechanical behavior. Altogether, this parametric interpolation strategy provides a physically consistent and computationally efficient route for engineering advanced phononic functionalities in periodic nonlocal systems....

---

### 83. Learning Neural Control Barrier Functions from Expert Demonstrations using Inverse Constraint Learning

**Authors:** Yuxuan Yang, Hussein Sibai

**Published:** 2025-10-24

**Category:** cs.AI

**ID:** 2510.21560v1

**Link:** [http://arxiv.org/abs/2510.21560v1](http://arxiv.org/abs/2510.21560v1)

**Summary:** Safety is a fundamental requirement for autonomous systems operating in critical domains. Control barrier functions (CBFs) have been used to design safety filters that minimally alter nominal controls for such systems to maintain their safety. Learning neural CBFs has been proposed as a data-driven alternative for their computationally expensive optimization-based synthesis. However, it is often the case that the failure set of states that should be avoided is non-obvious or hard to specify formally, e.g., tailgating in autonomous driving, while a set of expert demonstrations that achieve the task and avoid the failure set is easier to generate. We use ICL to train a constraint function that classifies the states of the system under consideration to safe, i.e., belong to a controlled forward invariant set that is disjoint from the unspecified failure set, and unsafe ones, i.e., belong to the complement of that set. We then use that function to label a new set of simulated trajectories to train our neural CBF. We empirically evaluate our approach in four different environments, demonstrating that it outperforms existing baselines and achieves comparable performance to a neural CBF trained with the same data but annotated with ground-truth safety labels....

---

### 84. Race and Gender in LLM-Generated Personas: A Large-Scale Audit of 41 Occupations

**Authors:** Ilona van der Linden, Sahana Kumar, Arnav Dixit, Aadi Sudan, Smruthi Danda, David C. Anastasiu, Kai Lukoff

**Published:** 2025-10-23

**Category:** cs.HC

**ID:** 2510.21011v1

**Link:** [http://arxiv.org/abs/2510.21011v1](http://arxiv.org/abs/2510.21011v1)

**Summary:** Generative AI tools are increasingly used to create portrayals of people in occupations, raising concerns about how race and gender are represented. We conducted a large-scale audit of over 1.5 million occupational personas across 41 U.S. occupations, generated by four large language models with different AI safety commitments and countries of origin (U.S., China, France). Compared with Bureau of Labor Statistics data, we find two recurring patterns: systematic shifts, where some groups are consistently under- or overrepresented, and stereotype exaggeration, where existing demographic skews are amplified. On average, White (--31pp) and Black (--9pp) workers are underrepresented, while Hispanic (+17pp) and Asian (+12pp) workers are overrepresented. These distortions can be extreme: for example, across all four models, Housekeepers are portrayed as nearly 100\% Hispanic, while Black workers are erased from many occupations. For HCI, these findings show provider choice materially changes who is visible, motivating model-specific audits and accountable design practices....

---

### 85. Frequency-Dynamic Attention Modulation for Dense Prediction

**Authors:** Linwei Chen, Lin Gu, Ying Fu

**Published:** 2025-07-16

**Category:** cs.CV

**ID:** 2507.12006v4

**Link:** [http://arxiv.org/abs/2507.12006v4](http://arxiv.org/abs/2507.12006v4)

**Summary:** Vision Transformers (ViTs) have significantly advanced computer vision, demonstrating strong performance across various tasks. However, the attention mechanism in ViTs makes each layer function as a low-pass filter, and the stacked-layer architecture in existing transformers suffers from frequency vanishing. This leads to the loss of critical details and textures. We propose a novel, circuit-theory-inspired strategy called Frequency-Dynamic Attention Modulation (FDAM), which can be easily plugged into ViTs. FDAM directly modulates the overall frequency response of ViTs and consists of two techniques: Attention Inversion (AttInv) and Frequency Dynamic Scaling (FreqScale). Since circuit theory uses low-pass filters as fundamental elements, we introduce AttInv, a method that generates complementary high-pass filtering by inverting the low-pass filter in the attention matrix, and dynamically combining the two. We further design FreqScale to weight different frequency components for fine-grained adjustments to the target response function. Through feature similarity analysis and effective rank evaluation, we demonstrate that our approach avoids representation collapse, leading to consistent performance improvements across various models, including SegFormer, DeiT, and MaskDINO. These improvements are evident in tasks such as semantic segmentation, object detection, and instance segmentation. Additionally, we apply our method to remote sensing detection, achieving state-of-the-art results in single-scale settings. The code is available at https://github.com/Linwei-Chen/FDAM....

---

### 86. Microfluidic Study of Evaporation-Driven Crystallization of Saline and Ammonia Brines under Hydrogen Flow

**Authors:** Karol M. Dąbrowski, Mohammad Nooraiepour, Mohammad Masoudi

**Published:** 2025-10-23

**Category:** physics.flu-dyn

**ID:** 2510.20321v1

**Link:** [http://arxiv.org/abs/2510.20321v1](http://arxiv.org/abs/2510.20321v1)

**Summary:** Underground storage of hydrogen and ammonia in geological formations is essential for renewable energy integration, but salt precipitation during gas injection may threaten storage performance. While extensively studied for CO2 systems, precipitation mechanisms in hydrogen-brine and ammonia-brine systems remain poorly understood. This study presents a comprehensive microfluidic investigation of salt crystallization during hydrogen injection into saline and ammonia-containing brines using high-pressure microfluidics. We conducted 81 high-pressure experiments systematically varying brine composition (1-5 mol/kg NaCl), chemical additives (surfactants, alcohols, ammonia), and hydrogen flow rates (200-1300 mL/min). Quantitative image analysis reveals that hydrogen-induced precipitation differs fundamentally from CO2 systems. Hydrogen drives physical precipitation via evaporation and capillary trapping, producing discrete, localized deposits. In contrast, CO2-ammonia systems generate extensive reactive precipitation of ammonium bicarbonate with interconnected crystal networks. Interfacial tension (IFT) controls both residual brine distribution and final crystal coverage: high-IFT fluids form large, interconnected brine pools promoting extensive crystallization, while low-IFT fluids create isolated pools reducing crystal coverage by 50\%. Alcohol and surfactant additives suppress precipitation by enhancing brine mobility, whereas ammonia paradoxically increases crystal fractions despite lower IFT. Higher flow rates accelerate crystallization across all compositions, enabling operational mitigation strategies. and demonstrate that gas-specific, rather than CO2-analog, risk assessments are essential for underground hydrogen storage design. The effectiveness of chemical additives offers promising pathways for near-wellbore protection in underground hydrogen storage operations....

---

### 87. Domain wall induced topological Hall effect in the chiral-lattice ferromagnet Fe$_x$TaS$_2$

**Authors:** Sk Jamaluddin, Warit Nisaiyok, Yu Zhang, Hari Bhandari, Brian A. Francisco, Peter E. Siegfried, Fehmi Sami Yasin, Tianyi Wang, Abhijeet Nayak, Mohamed El Gazzah, Resham Babu Regmi, June Ho Yeo, Liuyan Zhao, J. F. Mitchell, Yong-Tao Cui, Nirmal J. Ghimire

**Published:** 2025-10-23

**Category:** cond-mat.mtrl-sci

**ID:** 2510.20181v1

**Link:** [http://arxiv.org/abs/2510.20181v1](http://arxiv.org/abs/2510.20181v1)

**Summary:** Magnetic topology and its associated emergent phenomena are central to realizing intriguing quantum states and spintronics functionalities. Designing spin textures to achieve strong and distinct electrical responses remains a significant challenge. Layered transition metal dichalcogenides offer a versatile platform for tailoring structural and magnetic properties, enabling access to a wide spectrum of topological magnetic states. Here, we report a domain-wall-driven, large, and tunable topological Hall effect (THE) in a non-centrosymmetric intercalated transition metal dichalcogenides series Fe$_x$TaS$_2$. By systematically varying the Fe intercalation level, we exert precise control over the magnetic ground states, allowing manipulation of the topological Hall effect. Real-space magnetic force microscopy (MFM) provides direct evidence of periodic magnetic stripe domain formation, confirming the microscopic origin of the observed topological transport phenomena. Our findings establish a promising way for tuning the topology of domains to generate substantial electromagnetic responses in layered magnetic materials....

---

### 88. To Use or to Refuse? Re-Centering Student Agency with Generative AI in Engineering Design Education

**Authors:** Thijs Willems, Sumbul Khan, Qian Huang, Bradley Camburn, Nachamma Sockalingam, King Wang Poon

**Published:** 2025-10-22

**Category:** cs.CY

**ID:** 2510.19342v1

**Link:** [http://arxiv.org/abs/2510.19342v1](http://arxiv.org/abs/2510.19342v1)

**Summary:** This pilot study traces students' reflections on the use of AI in a 13-week foundational design course enrolling over 500 first-year engineering and architecture students at the Singapore University of Technology and Design. The course was an AI-enhanced design course, with several interventions to equip students with AI based design skills. Students were required to reflect on whether the technology was used as a tool (instrumental assistant), a teammate (collaborative partner), or neither (deliberate non-use). By foregrounding this three-way lens, students learned to use AI for innovation rather than just automation and to reflect on agency, ethics, and context rather than on prompt crafting alone. Evidence stems from coursework artefacts: thirteen structured reflection spreadsheets and eight illustrated briefs submitted, combined with notes of teachers and researchers. Qualitative coding of these materials reveals shared practices brought about through the inclusion of Gen-AI, including accelerated prototyping, rapid skill acquisition, iterative prompt refinement, purposeful "switch-offs" during user research, and emergent routines for recognizing hallucinations. Unexpectedly, students not only harnessed Gen-AI for speed but (enabled by the tool-teammate-neither triage) also learned to reject its outputs, invent their own hallucination fire-drills, and divert the reclaimed hours into deeper user research, thereby transforming efficiency into innovation. The implications of the approach we explore shows that: we can transform AI uptake into an assessable design habit; that rewarding selective non-use cultivates hallucination-aware workflows; and, practically, that a coordinated bundle of tool access, reflection, role tagging, and public recognition through competition awards allows AI based innovation in education to scale without compromising accountability....

---

### 89. An Encoder-Decoder Foundation Chemical Language Model for Generative Polymer Design

**Authors:** Harikrishna Sahu, Wei Xiong, Anagha Savit, Shivank S Shukla, Rampi Ramprasad

**Published:** 2025-10-21

**Category:** cond-mat.mtrl-sci

**ID:** 2510.18860v1

**Link:** [http://arxiv.org/abs/2510.18860v1](http://arxiv.org/abs/2510.18860v1)

**Summary:** Traditional machine learning has advanced polymer discovery, yet direct generation of chemically valid and synthesizable polymers without exhaustive enumeration remains a challenge. Here we present polyT5, an encoder-decoder chemical language model based on the T5 architecture, trained to understand and generate polymer structures. polyT5 enables both property prediction and the targeted generation of polymers conditioned on desired property values. We demonstrate its utility for dielectric polymer design, seeking candidates with dielectric constant >3, bandgap >4 eV, and glass transition temperature >400 K, alongside melt-processability and solubility requirements. From over 20,000 generated promising candidates, one was experimentally synthesized and validated, showing strong agreement with predictions. To further enhance usability, we integrated polyT5 within an agentic AI framework that couples it with a general-purpose LLM, allowing natural language interaction for property prediction and generative design. Together, these advances establish a versatile and accessible framework for accelerated polymer discovery....

---

### 90. Design and theory of switchable linear magnetoelectricity by ferroelectricity in Type-I multiferroics

**Authors:** Hui-Min Zhang, Cheng-Ao Ji, Tong Zhu, Hongjun Xiang, Hiroshi Kageyama, Shuai Dong, James M. Rondinelli, Xue-Zeng Lu

**Published:** 2025-10-20

**Category:** cond-mat.mtrl-sci

**ID:** 2510.17627v1

**Link:** [http://arxiv.org/abs/2510.17627v1](http://arxiv.org/abs/2510.17627v1)

**Summary:** We present a comprehensive theoretical investigation of magnetoelectric (ME) coupling mechanisms in 19 altermagnetic and 4 ferrimagnetic Type-I multiferroics using electronic band structure calculations with spin-orbit coupling, a first-principles ME response framework, and spin-space-group theory analysis. We formulate a universal scheme for realizing nonvolatile ME coupling in Type-I multiferroics, where two distinct pathways emerge, each dictated by spin-space symmetry. The first pathway is associated with switching of the spin splitting or the now familiar spin-momentum locking in reciprocal space, characteristic of some altermagnetic mul-tiferroics that exhibit coexisting antiferromagnetism and ferroelectricity. The second pathway involves real-space magnetization switching via electric polarization reversal, characterized by switchable components of the linear ME tensor, despite the traditionally weak coupling in Type-I systems due to the independent origins of magnetism and ferroelectricity. We demonstrate that these two intrinsic ME coupling mechanisms are mutually exclusive and propose thermodynami-cally stable compounds for experimentation. Our findings establish general design principles for controlling robust nonvolatile ME effects in multiferroic materials....

---

### 91. Micro-crystal GaAs array sub-cells for Si tandem solar cells

**Authors:** James P. Connolly, Ahmed Nejim, Alexandre Jaffré, J Alvarez, Kleider J. P., Denis Mencaraglia, Laurie Dentz, Geraldine Hallais, Frédéric Hamouda, Laetitia Vincent, Daniel Bouchier, Charles Renard

**Published:** 2025-10-20

**Category:** cond-mat.mtrl-sci

**ID:** 2510.17254v1

**Link:** [http://arxiv.org/abs/2510.17254v1](http://arxiv.org/abs/2510.17254v1)

**Summary:** This work reports optical and electronic numerical modelling of a novel emerging structure which is the GaAs nanocrystal on Si tandem solar cell by epitaxial lateral overgrowth, a technique which allows defect free material growth. The techniqueconsists of creating nucleation sites in a silicon surface SiO2 layer and initiating growth of nanoscalescale seeds, whereby strain energy remains below the Matthews-Blakeslee strain relaxation limit. This leads to AlxGaAs growth in micro-crystals without generation of material defects. The focus of this presentation is optical and electrical modelling of nanocrystals for applications in the very active field of silicon based multijunction solar cells, and design of a AlxGaAs/Si two terminal tandem, for compositions ranging from x=0 to x=30% in absorber layers. We present a model of the complete structure in two dimensions, consisting of a Al xGaAs high bandgap subcell connected with a tunnel junction to the low bandgap Si junction. The elaboration of models is described, with an emphasis on the AlxGaAs crystal featuring a non-planar pn-junction, and a focus on the optical properties of this lattice of micrometric AlGaAs crystals and in particular their light trapping properties from the resulting surface texture. The question of AlxGaAs surface coverage is addressed, given that neighbouring AlxGaAs crystals have different crystal orientations on a (111) Si surface, such that any coalescence of neighbour AlxGaAs crystals leads to crippling defects at their interface. The result is that some high energy incident light above the AlxGaAs bandgap is nevertheless transmitted directly to the Si cell, such that the resulting photogenerated carriers thermalise to the Silicon bandgap, and result in a loss of efficiency. The interface between AlxGaAs and Si subcells is addressed, with an emphasis on current transport efficiency through the nanoseeds and tunnelling currents through appropriately designed SiO2 buffer layers. This work therefore presents a theoretical framework for evaluating the potential of AlxGaAs nanocrystal growth on Si for light trapping, for GaAs silicon two terminal tandem cell performance including tunnel junctions, and provides models and design rules for efficient AlxGaAs microcrystal arrays as high bandgap subcells for tandem solar cells on silicon....

---

### 92. From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery

**Authors:** Jiaqi Wei, Yuejin Yang, Xiang Zhang, Yuhan Chen, Xiang Zhuang, Zhangyang Gao, Dongzhan Zhou, Guangshuai Wang, Zhiqiang Gao, Juntai Cao, Zijie Qiu, Ming Hu, Chenglong Ma, Shixiang Tang, Junjun He, Chunfeng Song, Xuming He, Qiang Zhang, Chenyu You, Shuangjia Zheng, Ning Ding, Wanli Ouyang, Nanqing Dong, Yu Cheng, Siqi Sun, Lei Bai, Bowen Zhou

**Published:** 2025-08-18

**Category:** cs.LG

**ID:** 2508.14111v2

**Link:** [http://arxiv.org/abs/2508.14111v2](http://arxiv.org/abs/2508.14111v2)

**Summary:** Artificial intelligence (AI) is reshaping scientific discovery, evolving from specialized computational tools into autonomous research partners. We position Agentic Science as a pivotal stage within the broader AI for Science paradigm, where AI systems progress from partial assistance to full scientific agency. Enabled by large language models (LLMs), multimodal systems, and integrated research platforms, agentic AI shows capabilities in hypothesis generation, experimental design, execution, analysis, and iterative refinement -- behaviors once regarded as uniquely human. This survey provides a domain-oriented review of autonomous scientific discovery across life sciences, chemistry, materials science, and physics. We unify three previously fragmented perspectives -- process-oriented, autonomy-oriented, and mechanism-oriented -- through a comprehensive framework that connects foundational capabilities, core processes, and domain-specific realizations. Building on this framework, we (i) trace the evolution of AI for Science, (ii) identify five core capabilities underpinning scientific agency, (iii) model discovery as a dynamic four-stage workflow, (iv) review applications across the above domains, and (v) synthesize key challenges and future opportunities. This work establishes a domain-oriented synthesis of autonomous scientific discovery and positions Agentic Science as a structured paradigm for advancing AI-driven research....

---

### 93. Consistent Zero-Shot Imitation with Contrastive Goal Inference

**Authors:** Kathryn Wantlin, Chongyi Zheng, Benjamin Eysenbach

**Published:** 2025-10-20

**Category:** cs.LG

**ID:** 2510.17059v1

**Link:** [http://arxiv.org/abs/2510.17059v1](http://arxiv.org/abs/2510.17059v1)

**Summary:** In the same way that generative models today conduct most of their training in a self-supervised fashion, how can agentic models conduct their training in a self-supervised fashion, interactively exploring, learning, and preparing to quickly adapt to new tasks? A prerequisite for embodied agents deployed in real world interactions ought to be training with interaction, yet today's most successful AI models (e.g., VLMs, LLMs) are trained without an explicit notion of action. The problem of pure exploration (which assumes no data as input) is well studied in the reinforcement learning literature and provides agents with a wide array of experiences, yet it fails to prepare them for rapid adaptation to new tasks. Today's language and vision models are trained on data provided by humans, which provides a strong inductive bias for the sorts of tasks that the model will have to solve (e.g., modeling chords in a song, phrases in a sonnet, sentences in a medical record). However, when they are prompted to solve a new task, there is a faulty tacit assumption that humans spend most of their time in the most rewarding states. The key contribution of our paper is a method for pre-training interactive agents in a self-supervised fashion, so that they can instantly mimic human demonstrations. Our method treats goals (i.e., observations) as the atomic construct. During training, our method automatically proposes goals and practices reaching them, building off prior work in reinforcement learning exploration. During evaluation, our method solves an (amortized) inverse reinforcement learning problem to explain demonstrations as optimal goal-reaching behavior. Experiments on standard benchmarks (not designed for goal-reaching) show that our approach outperforms prior methods for zero-shot imitation....

---

### 94. Intermediate-Band Formation in Tm3+-doped Ca2SnO4: A Wide-Gap Oxide Host for Visible-Light Absorption and Energy Applications

**Authors:** Shah Hussain, Sikander Azam, Umme Habiba, Qaiser Rafiq, Amin Ur Rahman, Hamada H. Amer, Yasir Saeed

**Published:** 2025-10-19

**Category:** cond-mat.mtrl-sci

**ID:** 2510.16957v1

**Link:** [http://arxiv.org/abs/2510.16957v1](http://arxiv.org/abs/2510.16957v1)

**Summary:** Rare earth doping is an effective way to convert chemically stable oxides into multifunctional materials with coupled electronic, optical, and magnetic properties. We present first principles calculations of pristine and Tm3+ doped Ca2SnO4 to understand how localized 4f states change the structural, electronic, magnetic, and optical behavior of the host. Pristine Ca2SnO4 is a mechanically stable, wide band gap insulator with mostly ionic covalent bonding and diamagnetic character. Replacing Ca2+ with Tm3+ introduces several key changes: (i) localized Tm 4f states create intermediate levels inside the wide gap, reducing the optical band gap; (ii) exchange and spin orbit interactions generate strong local magnetic moments and spin asymmetry near the conduction band; (iii) electron localization function analysis shows enhanced covalency and electron pockets that stabilize luminescent centers; and (iv) the optical response shows visible range absorption, refractive index features, and low energy plasmon peaks while maintaining high energy dielectric stability. These effects make Tm doped Ca2SnO4 a mechanically robust, optically tunable, and magnetically active oxide phosphor suitable for red emission, intermediate band photovoltaics, and spin photon coupling. More broadly, our results show how targeted rare earth substitution can enable multifunctionality in wide gap stannates and guide the design of next generation spintronic photonic oxides....

---

### 95. Sparse Transformer Architectures via Regularized Wasserstein Proximal Operator with $L_1$ Prior

**Authors:** Fuqun Han, Stanley Osher, Wuchen Li

**Published:** 2025-10-18

**Category:** cs.LG

**ID:** 2510.16356v1

**Link:** [http://arxiv.org/abs/2510.16356v1](http://arxiv.org/abs/2510.16356v1)

**Summary:** In this work, we propose a sparse transformer architecture that incorporates prior information about the underlying data distribution directly into the transformer structure of the neural network. The design of the model is motivated by a special optimal transport problem, namely the regularized Wasserstein proximal operator, which admits a closed-form solution and turns out to be a special representation of transformer architectures. Compared with classical flow-based models, the proposed approach improves the convexity properties of the optimization problem and promotes sparsity in the generated samples. Through both theoretical analysis and numerical experiments, including applications in generative modeling and Bayesian inverse problems, we demonstrate that the sparse transformer achieves higher accuracy and faster convergence to the target distribution than classical neural ODE-based methods....

---

### 96. Engineering phase-frustration induced flat bands in an aza-triangulene covalent Kagome lattice

**Authors:** Yuyi Yan, Fujia Liu, Weichen Tang, Han Xuan Wong, Boyu Qie, Steven G. Louie, Felix R. Fischer

**Published:** 2025-10-17

**Category:** cond-mat.mtrl-sci

**ID:** 2510.16126v1

**Link:** [http://arxiv.org/abs/2510.16126v1](http://arxiv.org/abs/2510.16126v1)

**Summary:** Pi-conjugated covalent organic frameworks (COFs) provide a versatile platform for the realization of designer quantum nanomaterials. Strong electron-electron correlation within these artificial lattices can give rise to exotic phases of matter. Their experimental realization however requires precise control over orbital symmetry, charge localization, and band dispersion all arising from the effective hybridization between molecular linkers and nodes. Here, we present a modular strategy for constructing diatomic Kagome lattices from aza-[3]triangulene (A[3]T) nodes, in which a D3h symmetric ground state is stabilized through resonance contributions from a cumulenenic linker. First-principles density-functional theory and scanning tunnelling spectroscopy reveal that the hybridization of a sixfold degenerate set of edge-localized Wannier functions in the unit cell gives rise to orbital-phase frustration-induced non-trivial flat bands. These results establish a general design principle for engineering orbital interactions in organic lattices and open a pathway toward programmable COF-based quantum materials with correlated electronic ground states....

---

### 97. LeMat-Traj: A Scalable and Unified Dataset of Materials Trajectories for Atomistic Modeling

**Authors:** Ali Ramlaoui, Martin Siron, Inel Djafar, Joseph Musielewicz, Amandine Rossello, Victor Schmidt, Alexandre Duval

**Published:** 2025-08-28

**Category:** cs.LG

**ID:** 2508.20875v2

**Link:** [http://arxiv.org/abs/2508.20875v2](http://arxiv.org/abs/2508.20875v2)

**Summary:** The development of accurate machine learning interatomic potentials (MLIPs) is limited by the fragmented availability and inconsistent formatting of quantum mechanical trajectory datasets derived from Density Functional Theory (DFT). These datasets are expensive to generate yet difficult to combine due to variations in format, metadata, and accessibility. To address this, we introduce LeMat-Traj, a curated dataset comprising over 120 million atomic configurations aggregated from large-scale repositories, including the Materials Project, Alexandria, and OQMD. LeMat-Traj standardizes data representation, harmonizes results and filters for high-quality configurations across widely used DFT functionals (PBE, PBESol, SCAN, r2SCAN). It significantly lowers the barrier for training transferrable and accurate MLIPs. LeMat-Traj spans both relaxed low-energy states and high-energy, high-force structures, complementing molecular dynamics and active learning datasets. By fine-tuning models pre-trained on high-force data with LeMat-Traj, we achieve a significant reduction in force prediction errors on relaxation tasks. We also present LeMaterial-Fetcher, a modular and extensible open-source library developed for this work, designed to provide a reproducible framework for the community to easily incorporate new data sources and ensure the continued evolution of large-scale materials datasets. LeMat-Traj and LeMaterial-Fetcher are publicly available at https://huggingface.co/datasets/LeMaterial/LeMat-Traj and https://github.com/LeMaterial/lematerial-fetcher....

---

### 98. Reasoning-Enhanced Large Language Models for Molecular Property Prediction

**Authors:** Jiaxi Zhuang, Yaorui Shi, Jue Hou, Yunong He, Mingwei Ye, Mingjun Xu, Yuming Su, Linfeng Zhang, Ying Qian, Linfeng Zhang, Guolin Ke, Hengxing Cai

**Published:** 2025-10-11

**Category:** cs.LG

**ID:** 2510.10248v2

**Link:** [http://arxiv.org/abs/2510.10248v2](http://arxiv.org/abs/2510.10248v2)

**Summary:** Molecular property prediction is crucial for drug discovery and materials science, yet existing approaches suffer from limited interpretability, poor cross-task generalization, and lack of chemical reasoning capabilities. Traditional machine learning models struggle with task transferability, while specialized molecular language models provide little insight into their decision-making processes. To address these limitations, we propose \textbf{MPPReasoner}, a multimodal large language model that incorporates chemical reasoning for molecular property prediction. Our approach, built upon Qwen2.5-VL-7B-Instruct, integrates molecular images with SMILES strings to enable comprehensive molecular understanding. We develop a two-stage training strategy: supervised fine-tuning (SFT) using 16,000 high-quality reasoning trajectories generated through expert knowledge and multiple teacher models, followed by Reinforcement Learning from Principle-Guided Rewards (RLPGR). RLPGR employs verifiable, rule-based rewards that systematically evaluate chemical principle application, molecular structure analysis, and logical consistency through computational verification. Extensive experiments across 8 datasets demonstrate significant performance improvements, with MPPReasoner outperforming the best baselines by 7.91\% and 4.53\% on in-distribution and out-of-distribution tasks respectively. MPPReasoner exhibits exceptional cross-task generalization and generates chemically sound reasoning paths that provide valuable insights into molecular property analysis, substantially enhancing both interpretability and practical utility for chemists. Code is available at https://anonymous.4open.science/r/MPPReasoner-12687....

---

### 99. Unravelling the Catalytic Activity of Dual-Metal Doped N6-Graphene for Sulfur Reduction via Machine Learning-Accelerated First-Principles Calculations

**Authors:** Sahil Kumar, Adithya Maurya K R, Mudit Dixit

**Published:** 2025-10-17

**Category:** cond-mat.mtrl-sci

**ID:** 2510.15397v1

**Link:** [http://arxiv.org/abs/2510.15397v1](http://arxiv.org/abs/2510.15397v1)

**Summary:** Understanding and optimizing polysulfide adsorption and conversion processes are critical to mitigating shuttle effects and sluggish redox kinetics in lithium-sulfur batteries (LSBs). Here, we introduce a machine-learning-accelerated framework, Precise and Accurate Configuration Evaluation (PACE), that integrates Machine Learning Interatomic Potentials (MLIPs) with Density Functional Theory (DFT) to systematically explore adsorption configurations and energetics of a series of N6-coordinated dual-atom catalysts (DACs). Our results demonstrate that, compared with single-atom catalysts, DACs exhibit improved LiPS adsorption and redox conversion through cooperative metal-sulfur interactions and electronic coupling between adjacent metal centers. Among all DACs, Fe-Ni and Fe-Pt show optimal catalytic performance, due to their optimal adsorption energies (-1.0 to -2.3 eV), low free-energy barriers (<=0.4 eV) for the Li2S2 to Li2S conversion, and facile Li2S decomposition barriers (<=1.0 eV). To accelerate catalyst screening, we further developed a machine learning (ML) regression model trained on DFT-calculated data to predict the Gibbs free energy (ΔG) of Li2Sn adsorption using physically interpretable descriptors. The Gradient Boosting Regression (GBR) model yields an R^2 of 0.85 and an MAE of 0.26 eV, enabling the rapid prediction of ΔG for unexplored DACs. Electronic-structure analyses reveal that the superior performance originates from the optimal d-band alignment and S-S bond polarization induced by the cooperative effect of dual metal centres. This dual ML-DFT framework demonstrates a generalizable, data-driven design strategy for the rational discovery of efficient catalysts for next-generation LSBs....

---

### 100. Spin-Selective Second-Order Topological Insulators Enabling Cornertronics in 2D Altermagnets

**Authors:** Ning-Jing Yang, Zhigao Huang, Jian-Min Zhang

**Published:** 2025-10-15

**Category:** cond-mat.mes-hall

**ID:** 2510.13319v2

**Link:** [http://arxiv.org/abs/2510.13319v2](http://arxiv.org/abs/2510.13319v2)

**Summary:** Recent progress in spintronics within the paradigm of altermagnets (AMs) opens new avenues for next-generation electronic device design. Here, we establish a spin-corner locking mechanism that generates second-order topological states in two-dimensional (2D) altermagnetic systems, through effective model analysis. Remarkably, the breaking of Mxy symmetry under uniaxial strain creates spin-resolved corner modes, driving the system into a corner-polarized second-order topological insulator (CPSOTI). Beyond critical strain, a topological phase transition to quantum anomalous Hall insulator occurs with quantized conductance. Through first-principles calculations, we identify two experimentally viable candidates for 2D intrinsic AM CrO and Cr$_2$Se$_2$O -- which host robust CPSOTI. Moreover, we construct the topological phase diagram of CrO and predict the existence of an altermagnetic Weyl semimetal phase. Our findings open technological avenues in altermagnetism and higher-order topology, while providing opportunities for coupling topological spintronics with cornertronics....

---

### 101. High-entropy perovskites as new photocatalysts for cocatalyst-free water splitting

**Authors:** Ho Truong Nam Hai, Makoto Arita, Kaveh Edalati

**Published:** 2025-10-17

**Category:** physics.chem-ph

**ID:** 2510.15225v1

**Link:** [http://arxiv.org/abs/2510.15225v1](http://arxiv.org/abs/2510.15225v1)

**Summary:** The photocatalytic water-splitting process is thermodynamically challenging and requires catalysts with suitable band structures, as well as the presence of supporting cocatalysts. By considering the unique charge carrier mobility in perovskites, this study introduces three new ABO3-type high-entropy perovskites (Ba1/2Sr1/2)(Ti1/3Zr1/3Hf1/3)O3, (Ba1/2Sr1/2)(Ga1/3In1/3Sn1/3)O3 and (Ba1/2Sr1/2)(Ti1/3Zr1/3Sn1/3)O3 for cocatalyst-free photocatalysis. The three catalysts, having a single-phase cubic structure, are designed by considering configurational entropy, tolerance factor, octahedral factor, ionic radius deviation and valence deviation of >1.5R (R: gas constant), 0.9-1.0, 0.4-0.8, >0.3 and >0.3, respectively. The perovskites exhibit similar valence band tops, while their bandgaps vary slightly depending on the composition at the B-site (slightly lower bandgap by including d10 cations). Additionally, all three materials demonstrate effective hydrogen generation without the need for added cocatalysts. This investigation confirms that high-entropy oxide perovskites can offer significant potential for cocatalyst-free photocatalytic reactions....

---

### 102. Camera Movement Classification in Historical Footage: A Comparative Study of Deep Video Models

**Authors:** Tingyu Lin, Armin Dadras, Florian Kleber, Robert Sablatnig

**Published:** 2025-10-16

**Category:** cs.CV

**ID:** 2510.14713v1

**Link:** [http://arxiv.org/abs/2510.14713v1](http://arxiv.org/abs/2510.14713v1)

**Summary:** Camera movement conveys spatial and narrative information essential for understanding video content. While recent camera movement classification (CMC) methods perform well on modern datasets, their generalization to historical footage remains unexplored. This paper presents the first systematic evaluation of deep video CMC models on archival film material. We summarize representative methods and datasets, highlighting differences in model design and label definitions. Five standard video classification models are assessed on the HISTORIAN dataset, which includes expert-annotated World War II footage. The best-performing model, Video Swin Transformer, achieves 80.25% accuracy, showing strong convergence despite limited training data. Our findings highlight the challenges and potential of adapting existing models to low-quality video and motivate future work combining diverse input modalities and temporal architectures....

---

### 103. Odd elasticity in disordered chiral active materials

**Authors:** Cheng-Tai Lee, Tom C. Lubensky, Tomer Markovich

**Published:** 2025-08-06

**Category:** cond-mat.soft

**ID:** 2508.04468v3

**Link:** [http://arxiv.org/abs/2508.04468v3](http://arxiv.org/abs/2508.04468v3)

**Summary:** Chiral active materials are abundant in nature, including the cytoskeleton with attached motor proteins, rotary clusters of bacteria flagella, and self-spinning starfish embryos. These materials break both time reversal and mirror-image (parity) symmetries due to injection of torques at the microscale. Recently, it was found that chiral active materials may show a new type of elastic response termed `odd' elasticity. Currently, odd elasticity is understood microscopically only in ordered structures, e.g., lattice designs of metamaterials. It still remains to explore how odd elasticity can emerge in natural or biological systems, which are usually disordered. To address this, we propose a minimal generic model for disordered `odd solids', using micropolar (Cosserat) elasticity in the presence of local active torques. We find that odd elasticity naturally emerges as a nonlinear effect of internal particle rotations. Exploring the viscoelasticity of this solid, when immersed in active self-spinning solvent (`odd fluid'), we discover both dynamically unstable regions and regions in which bulk waves can propagate even in an overdamped solid....

---

### 104. Discovery of Hyperelastic Constitutive Laws from Experimental Data with EUCLID

**Authors:** Arefeh Abbasi, Maurizio Ricci, Pietro Carrara, Moritz Flaschel, Siddhant Kumar, Sonia Marfia, Laura De Lorenzis

**Published:** 2025-10-16

**Category:** physics.comp-ph

**ID:** 2510.24747v1

**Link:** [http://arxiv.org/abs/2510.24747v1](http://arxiv.org/abs/2510.24747v1)

**Summary:** We assess the performance of EUCLID, Efficient Unsupervised Constitutive Law Identification and Discovery, a recently proposed framework for automated discovery of constitutive laws, on experimental data. Mechanical tests are performed on natural rubber specimens spanning simple to complex geometries, from which we collect both global, force elongation, and local, full-field displacement, measurements. Using these data, we obtain constitutive laws via two routes, the conventional identification of unknown parameters in a priori selected material models, and EUCLID, which automates model selection and parameter identification within a unified model-discovery pipeline. We compare the two methodologies using global versus local data, analyze predictive accuracy, and examine generalization to unseen geometries. Moreover, we quantify the experimental noise, investigate the coverage of the material state space achieved by each approach and discuss the relative performance of different datasets and different a priori chosen models versus EUCLID....

---

### 105. Unifying Polymer Modeling and Design via a Conformation-Centric Generative Foundation Model

**Authors:** Fanmeng Wang, Shan Mei, Wentao Guo, Hongshuai Wang, Qi Ou, Zhifeng Gao, Hongteng Xu

**Published:** 2025-10-15

**Category:** cs.LG

**ID:** 2510.16023v1

**Link:** [http://arxiv.org/abs/2510.16023v1](http://arxiv.org/abs/2510.16023v1)

**Summary:** Polymers, macromolecules formed from covalently bonded monomers, underpin countless technologies and are indispensable to modern life. While deep learning is advancing polymer science, existing methods typically represent the whole polymer solely through monomer-level descriptors, overlooking the global structural information inherent in polymer conformations, which ultimately limits their practical performance. Moreover, this field still lacks a universal foundation model that can effectively support diverse downstream tasks, thereby severely constraining progress. To address these challenges, we introduce PolyConFM, the first polymer foundation model that unifies polymer modeling and design through conformation-centric generative pretraining. Recognizing that each polymer conformation can be decomposed into a sequence of local conformations (i.e., those of its repeating units), we pretrain PolyConFM under the conditional generation paradigm, reconstructing these local conformations via masked autoregressive (MAR) modeling and further generating their orientation transformations to recover the corresponding polymer conformation. Besides, we construct the first high-quality polymer conformation dataset via molecular dynamics simulations to mitigate data sparsity, thereby enabling conformation-centric pretraining. Experiments demonstrate that PolyConFM consistently outperforms representative task-specific methods on diverse downstream tasks, equipping polymer science with a universal and powerful tool....

---

### 106. Conditional Flow Matching for Bayesian Posterior Inference

**Authors:** So Won Jeong, Percy S. Zhai, Veronika Ročková

**Published:** 2025-10-10

**Category:** stat.ML

**ID:** 2510.09534v2

**Link:** [http://arxiv.org/abs/2510.09534v2](http://arxiv.org/abs/2510.09534v2)

**Summary:** We propose a generative multivariate posterior sampler via flow matching. It offers a simple training objective, and does not require access to likelihood evaluation. The method learns a dynamic, block-triangular velocity field in the joint space of data and parameters, which results in a deterministic transport map from a source distribution to the desired posterior. The inverse map, named vector rank, is accessible by reversibly integrating the velocity over time. It is advantageous to leverage the dynamic design: proper constraints on the velocity yield a monotone map, which leads to a conditional Brenier map, enabling a fast and simultaneous generation of Bayesian credible sets whose contours correspond to level sets of Monge-Kantorovich data depth. Our approach is computationally lighter compared to GAN-based and diffusion-based counterparts, and is capable of capturing complex posterior structures. Finally, frequentist theoretical guarantee on the consistency of the recovered posterior distribution, and of the corresponding Bayesian credible sets, is provided....

---

### 107. Selective Adversarial Attacks on LLM Benchmarks

**Authors:** Ivan Dubrovsky, Anastasia Orlova, Illarion Iov, Nina Gubina, Irena Gureeva, Alexey Zaytsev

**Published:** 2025-10-15

**Category:** cs.LG

**ID:** 2510.13570v1

**Link:** [http://arxiv.org/abs/2510.13570v1](http://arxiv.org/abs/2510.13570v1)

**Summary:** Benchmarking outcomes increasingly govern trust, selection, and deployment of LLMs, yet these evaluations remain vulnerable to semantically equivalent adversarial perturbations. Prior work on adversarial robustness in NLP has emphasized text attacks that affect many models equally, leaving open the question of whether it is possible to selectively degrade or enhance performance while minimally affecting other models. We formalize this problem and study selective adversarial attacks on MMLU - a widely used benchmark designed to measure a language model's broad general knowledge and reasoning ability across different subjects. Using canonical attacks integrated into TextAttack framework, we introduce a protocol for selectivity assessment, develop a custom constraint to increase selectivity of attacks and propose a surrogate-LLM pipeline that generates selective perturbations. Empirically, we find that selective adversarial attacks exist and can materially alter relative rankings, challenging the fairness, reproducibility, and transparency of leaderboard-driven evaluation. Our results motivate perturbation-aware reporting and robustness diagnostics for LLM evaluation and demonstrate that even subtle edits can shift comparative judgments....

---

### 108. Ultrafast exciton polaron dynamics in 2D Ruddlesden Popper lead halide perovskites

**Authors:** Anirban Mondal, Kwang Jin Lee, Seungmin Lee, Oui Jin Oh, Myeongsam Jen, Jun Hong Noh, Jong Min Lim, Minhaeng Cho

**Published:** 2025-10-15

**Category:** cond-mat.mtrl-sci

**ID:** 2510.13547v1

**Link:** [http://arxiv.org/abs/2510.13547v1](http://arxiv.org/abs/2510.13547v1)

**Summary:** Two dimensional Ruddlesden Popper (2D) RP hybrid perovskites exhibit substantially higher chemical and structural stability than their three dimensional (3D) counterparts, positioning them as promising candidates for next generation optoelectronics. While quasiparticle dynamics in 3D perovskites are well studied, their 2D analogues remain comparatively underexplored. Here we systematically investigate the branching, dynamics, and interactions of free excitons (FEs) and exciton polarons EPs in monolayer 2D RP perovskites using visible range femtosecond transient absorption TA spectroscopy. We prepared monolayer 2D RP perovskite thin films with varied organic spacers and distinct fabrication routes for comparative analysis. We find that the EP binding energy is 50 65 meV in (BA)2PbI4 and 37 39 meV in (PEA)2PbI4, consistent with spacer layer dependent coupling as corroborated by FTIR. We reveal a dynamic equilibrium between FEs and EPs that persists for tens of picoseconds. Notably, the TA signatures differ by fabrication route films from the newly developed process show weaker Auger annihilation and a reduced hot phonon bottleneck than those from the conventional route trends consistent with fewer traps and impurities in the former. Coupled rate equation modeling reproduces the transients and quantifies the processes of hot carrier relaxation, exciton exciton annihilation, exciton phonon coupling, and FE EP interconversion. These results demonstrate that the chemical synthetic process (fabrication route) and spacer choice significantly influence EP stability and population balance, offering practical levers for engineering ultrafast photophysics in 2D perovskites and guiding the design of advanced optoelectronic devices....

---

### 109. Multi-state Protein Design with DynamicMPNN

**Authors:** Alex Abrudan, Sebastian Pujalte Ojeda, Chaitanya K. Joshi, Matthew Greenig, Felipe Engelberger, Alena Khmelinskaia, Jens Meiler, Michele Vendruscolo, Tuomas P. J. Knowles

**Published:** 2025-07-29

**Category:** cs.LG

**ID:** 2507.21938v2

**Link:** [http://arxiv.org/abs/2507.21938v2](http://arxiv.org/abs/2507.21938v2)

**Summary:** Structural biology has long been dominated by the one sequence, one structure, one function paradigm, yet many critical biological processes - from enzyme catalysis to membrane transport - depend on proteins that adopt multiple conformational states. Existing multi-state design approaches rely on post-hoc aggregation of single-state predictions, achieving poor experimental success rates compared to single-state design. We introduce DynamicMPNN, an inverse folding model explicitly trained to generate sequences compatible with multiple conformations through joint learning across conformational ensembles. Trained on 46,033 conformational pairs covering 75% of CATH superfamilies and evaluated using Alphafold 3, DynamicMPNN outperforms ProteinMPNN by up to 25% on decoy-normalized RMSD and by 12% on sequence recovery across our challenging multi-state protein benchmark....

---

### 110. Magnetically controllable nonlinear valley Hall effect in centrosymmetric ferromagnets

**Authors:** Ruijing Fang, Jie Zhang, Zhichao Zhou, Xiao Li

**Published:** 2025-10-15

**Category:** cond-mat.mes-hall

**ID:** 2510.13457v1

**Link:** [http://arxiv.org/abs/2510.13457v1](http://arxiv.org/abs/2510.13457v1)

**Summary:** Valley Hall effect is fundamental to valleytronics and provides a promising avenue for advancing information technology. While conventional valley Hall effect requires the inversion symmetry breaking, the recently proposed nonlinear valley Hall (NVH) effect removes the symmetry constraint, and broaden material choices. However, existing studies are limited to nonmagnetic materials without spin involvement and rely on external strain to break rotational symmetry. Here, to address these limitations, we design a magnetically controllable NVH effect in centrosymmetric ferromagnets, by the tight-binding model and first-principles calculations. The model calculations demonstrate nonvanishing NVH conductivities can emerge in pristine hexagonal lattice without external strain, with the magnitude, sign, and spin polarization of the conductivities being all dependent on the magnetization orientation. The effect thus generates various spin-polarized valley Hall currents, characterized by distinct combinations of current direction and spin polarization. First-principle results on a ferromagnetic VSi$_2$N$_4$ bilayer confirm considerable NVH conductivities and their dependence on the magnetization. The magnetically controllable NVH effect unlocks the potential of centrosymmetric magnets for valleytronics, and offer opportunities for novel spintronic and valleytronic devices....

---

### 111. Computational Insights into Defect Induced Modulation in Electronic Properties of 2D Nitride Monolayers

**Authors:** Shreya G. Sarkar, Kuneh Parag Shah, Brahmananda Chakraborty

**Published:** 2025-10-15

**Category:** cond-mat.mtrl-sci

**ID:** 2510.13440v1

**Link:** [http://arxiv.org/abs/2510.13440v1](http://arxiv.org/abs/2510.13440v1)

**Summary:** Two-dimensional (2D) nitride materials such as hexagonal boron nitride (h-BN), graphitic carbon nitride (g-C$_3$N$_4$), and beryllonitrene (BeN$_4$) have emerged as promising candidates for next generation electronic, optoelectronic, and energy applications due to their unique structural and electronic properties. This study presents a systematic investigation of the effects of vacancy defect, specifically the role of nitrogen and constituent atom vacancies on the electronic properties of these materials. Our findings reveal that the introduction of nitrogen vacancies significantly alters the electronic characteristics of these materials. In h-BN, the presence of a nitrogen monovacancy significantly lowers the work function from 5.97 eV to 3.45 eV, one of the lowest values reported for any 2D material. Additionally, this defect reduces the band gap from 4.6 eV to 0.64 eV, driving the material toward half-metallic behavior. This is accompanied by the emergence of flat bands near the Fermi level, indicative of strong electron-electron interactions. In g-C$_3$N$_4$, nitrogen vacancies lead to a decrease in work function and band gap, with double nitrogen vacancies rendering the material nearly metallic. In BeN$_4$, nitrogen vacancies result in minimal charge redistribution and a slight increase in work function, highlighting the material's unique electronic behavior. These results underscore the potential of vacancy engineering in tuning the electronic properties of 2D nitride materials, offering avenues for the design of materials with tailored work functions and band gaps for applications in optoelectronics, spintronics, and catalysis....

---

### 112. First-Principles Exploration of Pentagonal TiN$_8$ and MoN$_8$ Monolayers as New Magnetic Topological Insulator

**Authors:** Zheng Wang, Beichen Ruan, Zhuoheng Li, Shu-Shen Lyu, Kaixuan Chen

**Published:** 2025-10-15

**Category:** cond-mat.mtrl-sci

**ID:** 2510.13107v1

**Link:** [http://arxiv.org/abs/2510.13107v1](http://arxiv.org/abs/2510.13107v1)

**Summary:** The quest for robust, intrinsically magnetic topological materials exhibiting the quantum anomalous Hall (QAH) effect is a central challenge in condensed matter physics and the application of revolutionary electronics. However, progress has been hampered by the limited number of candidate materials, which often suffer from poor stability and complex synthesis. Here, we introduce a new paradigm by exploring the emergent magnetism and nontrivial band topology in the largely overlooked family of two-dimensional (2D) pentagonal MN$_8$ monolayers. Employing first-principles calculations, we reveal that these systems host out-of-plane ferromagnetic ground states, a key feature that unlocks nontrivial topological properties driven by the localized $d$-orbitals of the embedded transition metals. Remarkably, we identify TiN$_8$ as a QAH insulator characterized by a Chern number of $C=-1$. Even more strikingly, MoN$_8$ is predicted to be a rare high-Chern-number QAH insulator, boasting a Chern number of $C=2$. Our findings establish the penta-MN$_8$ family as a fertile and versatile platform for realizing exotic topological quantum states. This work not only significantly expands the material landscape for magnetic topological insulators but also provides a solid theoretical foundation for designing next-generation spintronic and quantum computing devices....

---

### 113. Magnon-phonon interactions from first principles

**Authors:** Khoa B. Le, Ali Esquembre-Kucukalic, Hsiao-Yi Chen, Ivan Maliyov, Yao Luo, Jin-Jian Zhou, Davide Sangalli, Alejandro Molina-Sanchez, Marco Bernardi

**Published:** 2025-02-07

**Category:** cond-mat.mtrl-sci

**ID:** 2502.05385v2

**Link:** [http://arxiv.org/abs/2502.05385v2](http://arxiv.org/abs/2502.05385v2)

**Summary:** Modeling spin-wave (magnon) dynamics in novel materials is important to advance spintronics and spin-based quantum technologies. The interactions between magnons and lattice vibrations (phonons) limit the length scale for magnon transport. However, quantifying these interactions remains challenging. Here we show many-body calculations of magnon-phonon (mag-ph) coupling based on the ab initio Bethe-Salpeter equation. We derive expressions for mag-ph coupling matrices and compute them in 2D ferromagnets, focusing on hydrogenated graphene and monolayer CrI3. Our analysis shows that electron-phonon (e-ph) and mag-ph interactions differ significantly, where modes with weak e-ph coupling can exhibit strong mag-ph coupling (and vice versa), and reveals which phonon modes couple more strongly with magnons. In both materials studied here, the inelastic magnon relaxation time is found to decrease abruptly above the threshold for emission of strongly coupled phonons, thereby defining a low-energy window for efficient magnon transport. By averaging in this window, we compute the temperature-dependent magnon mean-free path, a key figure of merit for spintronics, entirely from first principles. The theory and computational tools shown in this work enable studies of magnon interactions, scattering, and dynamics in generic materials, advancing the design of magnetic systems and magnon- and spin-based devices....

---

### 114. Large Language Models Inference Engines based on Spiking Neural Networks

**Authors:** Adarsha Balaji, Sandeep Madireddy, Prasanna Balaprakash

**Published:** 2025-09-30

**Category:** cs.LG

**ID:** 2510.00133v3

**Link:** [http://arxiv.org/abs/2510.00133v3](http://arxiv.org/abs/2510.00133v3)

**Summary:** Foundational models based on the transformer architecture are currently the state-of-the-art in general language modeling, as well as in scientific areas such as material science and climate. However, training and deploying these models is computationally challenging as the time and space complexity has a quadratic relation to the input sequence length. Several efforts exploring efficient computational paradigms and model architectures to address these limitations have been made. In this work, we explore spiking neural networks (SNNs) to design transformer models. A challenge in training large-scale SNNs, using existing surrogate learning methods is inefficient and time-consuming. On the other hand, techniques to convert existing transformer-based models to their SNN equivalent are not scalable, as achieving optimal performance comes at the cost of a large number of spike time-steps, i.e. increased latency. To address this, we propose NeurTransformer, a methodology for designing transformer-based SNN for inference using a supervised fine-tuning approach with existing conversion methods. The proposed methodology works by: (1) replacing the self-attention mechanism with a spike-based self-attention (SSA), (2) converting the feed-forward block of the trained transformer model to its equivalent SNN, and (3) fine-tuning the SSA block using SNN-based surrogate learning algorithms. We benchmark the proposed methodology and demonstrate its accuracy and scalability using three variants of the GPT-2 model of increasing model size. We observe that the converted GPT-2 small models demonstrate a 5-12% loss in cosine similarity and a 9.7% reduction in perplexity. Finally, we demonstrate the energy efficiency of the SSA block compared to the ASA block and show between 64.71% and 85.28% reductions in estimated energy consumption when implementing the self-attention mechanism on a digital hardware....

---

### 115. Defect Passivation and Förster-Type Energy Exchange in H2Pc-TMD Organic-Inorganic Heterostructures

**Authors:** Šimun Mandić, Ana Senkić, Nataša Vujičić

**Published:** 2025-10-14

**Category:** cond-mat.mtrl-sci

**ID:** 2510.12437v1

**Link:** [http://arxiv.org/abs/2510.12437v1](http://arxiv.org/abs/2510.12437v1)

**Summary:** Organic - inorganic heterostructures (HS) combine the strong light absorption and exciton generation capabilities of organic molecules with the unique excitonic properties of layered transition metal dichalcogenides (TMDs), where the interfacial band alignment dictates the optical response. In this work, we investigate the influence of H2Pc molecules on CVD-grown MoS2 and WS2 monolayers using correlative microscopy techniques - Kelvin probe force microscopy (KPFM), photoluminescence (PL), and Raman spectroscopy. Comprehensive analysis of both electronic and optical properties provides detailed insights into the energy band alignment in these two HS. Despite their similar band alignments, the heterostructures exhibit strikingly different optical signatures. In the case of H2Pc/MoS2 HS, the effect of defect healing is more pronounced, while for the H2Pc/WS2 HS, strong indications of Förster energy transfer are observed. These findings highlight the critical role of transition dipole moment in addition to spectral overlap between donor emission and acceptor absorption in the design of optoelectronic devices....

---

### 116. Spectroscopic Determination of Site-Selective Ligand Binding on Single Anisotropic Nanocrystals

**Authors:** Dong Le, Wade Shipley, Alexandria Do, Liya Bi, Yufei Wang, Krista P. Balto, Rourav Basak, Hans A. Bechtel, Stephanie N. Gilbert Corder, Ilya Mazalov, Tesa Manto, Reno Sammons, Yutong She, Fiona Liang, Ganesh Raghavendran, Joshua S. Figueroa, Shaowei Li, Tod A. Pascal, Andrea R. Tao, Alex Frano

**Published:** 2025-10-14

**Category:** cond-mat.mtrl-sci

**ID:** 2510.12199v1

**Link:** [http://arxiv.org/abs/2510.12199v1](http://arxiv.org/abs/2510.12199v1)

**Summary:** Organic surface ligands are integral components of nanocrystals and nanoparticles that have a strong influence on their physicochemical properties, their interaction with the environment, and their ability to self-assemble and order into higher-order structures. These hybrid nanomaterials are tunable with applications in catalysis, directed self-assembly, next-generation optoelectronics, and chemical and quantum sensing. Critically, future advances depend on our ability to rationally engineer their surface chemistry. However, fundamental knowledge of ligand-nanoparticle behavior is limited by uncertainty in where and how these ligands bind to surfaces. For nanoparticles, in particular, few characterization techniques offer both the high spatial resolution and the precise chemical mapping needed to identify specific ligand binding sites. In this study, we utilized synchrotron infrared nanospectroscopy (SINS), atomic force microscopy (AFM), and scanning tunneling microscopy (STM) together with first-principles computer simulations to validate the site-selective adsorption of organic ligands on a shaped nanocrystal surface. Specifically, we demonstrate that the sterically encumbered isocyanide ligands (CNAr^{Mes2}) preferentially bind to the high curvature features of Ag nanocubes (NCs), where low-coordinate Ag atoms are present. In contrast, isocyanide ligands that do not exhibit these steric properties show no surface selectivity. SINS serves as an effective tool to validate these surface binding interactions at the near-single molecule level. These results indicate that steric effects can be successfully harnessed to design bespoke organic ligands for fine-tuning nanocrystal surface chemistry and the properties of the nanocrystal ligand shell....

---

### 117. Microscopic Intricacies of Self-Healing in Halide Perovskite-Charge Transport Layer Heterostructures

**Authors:** Tejmani Behera, Boris Louis, Lukas Paesen, Roel Vanden Brande, Koki Asano, Martin Vacha, Maarten Roeffaers, Elke Debroye, Johan Hofkens, Sudipta Setha

**Published:** 2025-10-13

**Category:** cond-mat.mtrl-sci

**ID:** 2510.11948v1

**Link:** [http://arxiv.org/abs/2510.11948v1](http://arxiv.org/abs/2510.11948v1)

**Summary:** The stability and performance of halide perovskite photovoltaic devices are critically limited by progressive defect generation and associated local non-radiative losses during operation. Self-healing of defects provides a promising pathway to prolong device functionality, yet the underlying microscopic mechanisms remain poorly understood, particularly the role of interfacial chemistry on trap dynamics and healing kinetics. Here, we elucidate self-healing and defect evolution in triple-cation mixed halide (TCMH) perovskite films and their device-relevant charge transport layer heterostructures subjected to photo-induced damage. Using correlation clustering imaging (CLIM), our recently developed local functional imaging tool, we map spatiotemporal photoluminescence heterogeneity to track defect dynamics in pristine and heterostructure films. The defect healing follows bi-phasic kinetics, with an initial electronic relaxation (tens of minutes) and a subsequent slower phase (~ hours) associated to ionic and lattice rearrangement. Most importantly, our results demonstrate that the chemical nature of charge-transport layers modulates trap activity, healing kinetics, and halide redistribution, with heterostructures exhibiting faster recovery than pristine films, a boon for device resilience. These findings provide new insights into the dynamic interaction between defects, interfaces, and ion migration, and establish a framework for rational design of durable, next-generation perovskite optoelectronic devices....

---

### 118. Strain-induced multiferroicity in Cr1/3NbS2

**Authors:** Y. Sun, Y. Ahn, D. Sapkota, H. S. Arachchige, R. Xue, S. Mozaffari, D. G. Mandrus, L. Zhao, J. Orenstein, V. Sunko

**Published:** 2025-10-13

**Category:** cond-mat.mtrl-sci

**ID:** 2510.11619v1

**Link:** [http://arxiv.org/abs/2510.11619v1](http://arxiv.org/abs/2510.11619v1)

**Summary:** Multiferroic materials, in which electric polarization and magnetic order coexist and couple, offer rich opportunities for both fundamental discovery and technology. However, multiferroicity remains rare due to conflicting electronic requirements for ferroelectricity and magnetism. One route to circumvent this challenge is to exploit the noncollinear ordering of spin cycloids, whose symmetry permits the emergence of polar order. In this work, we introduce another pathway to multiferroic order in which strain generates polarization in materials that host nonpolar spin spirals. To demonstrate this phenomenon, we chose the spin spiral in the well-studied helimagnet Cr1/3NbS2. To detect the induced polarization, we introduce the technique of magnetoelectric birefringence (MEB), an optical probe that enables spatially-resolved and unambiguous detection of polar order. By combining MEB imaging with strain engineering, we confirm the onset of a polar vector at the magnetic transition, establishing strained Cr1/3NbS2 as a type-II multiferroic....

---

### 119. Towards Unified and Lossless Latent Space for 3D Molecular Latent Diffusion Modeling

**Authors:** Yanchen Luo, Zhiyuan Liu, Yi Zhao, Sihang Li, Hengxing Cai, Kenji Kawaguchi, Tat-Seng Chua, Yang Zhang, Xiang Wang

**Published:** 2025-03-19

**Category:** cs.LG

**ID:** 2503.15567v4

**Link:** [http://arxiv.org/abs/2503.15567v4](http://arxiv.org/abs/2503.15567v4)

**Summary:** 3D molecule generation is crucial for drug discovery and material science, requiring models to process complex multi-modalities, including atom types, chemical bonds, and 3D coordinates. A key challenge is integrating these modalities of different shapes while maintaining SE(3) equivariance for 3D coordinates. To achieve this, existing approaches typically maintain separate latent spaces for invariant and equivariant modalities, reducing efficiency in both training and sampling. In this work, we propose \textbf{U}nified Variational \textbf{A}uto-\textbf{E}ncoder for \textbf{3D} Molecular Latent Diffusion Modeling (\textbf{UAE-3D}), a multi-modal VAE that compresses 3D molecules into latent sequences from a unified latent space, while maintaining near-zero reconstruction error. This unified latent space eliminates the complexities of handling multi-modality and equivariance when performing latent diffusion modeling. We demonstrate this by employing the Diffusion Transformer--a general-purpose diffusion model without any molecular inductive bias--for latent generation. Extensive experiments on GEOM-Drugs and QM9 datasets demonstrate that our method significantly establishes new benchmarks in both \textit{de novo} and conditional 3D molecule generation, achieving leading efficiency and quality. On GEOM-Drugs, it reduces FCD by 72.6\% over the previous best result, while achieving over 70\% relative average improvements in geometric fidelity. Our code is released at https://github.com/lyc0930/UAE-3D/....

---

### 120. In-plane polar domains enhanced energy storage

**Authors:** Yu Lei, Xiaoming Shi, Sihan Yan, Qinghua Zhang, Jiecheng Liu, Sixu Wang, Yu Chen, Jiaou Wang, He Qi, Qian Li, Ting Lin, Jingfen Li, Qing Zhu, Haoyu Wang, Jing Chen, Lincong Shu, Linkun Wang, Han Wu, Xianran Xing

**Published:** 2025-10-13

**Category:** cond-mat.mtrl-sci

**ID:** 2510.11126v1

**Link:** [http://arxiv.org/abs/2510.11126v1](http://arxiv.org/abs/2510.11126v1)

**Summary:** Relaxor ferroelectric thin films are recognized for their ultrahigh power density, rendering them highly promising for energy storage applications in electrical and electronic systems. However, achieving high energy storage performance with chemically homogeneous, environmentally friendly and compositionally stable materials remains challenging. In this work, we present a design of dielectrics with high energy storage performance via an in-plane polar domains incorporating polar nanoregions mechanism. Guided by phase-field simulations, we synthesized La/Si co-doping BaTiO3 solid-solution thin films with high chemical homogeneity to realize high energy storage performance. Given that, we achieve a high energy density of 203.7J/cm3 and an energy efficiency of approximately 80% at an electric field of 6.15MV/cm. This mechanism holds significant promise for the design of next-generation high-performance dielectric materials for energy storage and other advanced functional materials....

---

### 121. Generalized quantum limits of electrical contact resistance and thermal boundary resistance

**Authors:** Alice Ho, Jashan Singhal, Deji Akinwande, Huili Grace Xing, Debdeep Jena

**Published:** 2025-10-13

**Category:** cond-mat.mtrl-sci

**ID:** 2510.10919v1

**Link:** [http://arxiv.org/abs/2510.10919v1](http://arxiv.org/abs/2510.10919v1)

**Summary:** The importance of electrical contact resistance and thermal boundary resistance has increased dramatically as devices are scaled to atomic limits. The use of a rich range of materials with various bandstructures (e.g. parabolic, conical), and in geometries exploiting various dimensionalities (e.g. 1D wires, 2D sheets, and 3D bulk) will increase in the future. Here we derive a single general expression for the quantum limit of electrical contact resistivity for various bandstructures and all dimensions. A corresponding result for the quantum limit of thermal boundary resistance is also derived. These results will be useful to quantitatively co-design, benchmark, and guide the lowering of electrical and thermal boundary resistances for energy efficient devices....

---

### 122. Two-dimensional flat-bands in Moire-diamonds

**Authors:** Yalan Wei, Shifang Li, Yuke Song, Chaoyu He

**Published:** 2025-10-13

**Category:** cond-mat.mes-hall

**ID:** 2510.10908v1

**Link:** [http://arxiv.org/abs/2510.10908v1](http://arxiv.org/abs/2510.10908v1)

**Summary:** The discovery of flat-bands in magic-angle twisted bilayer graphene has underscored the potential of moire engineering for correlated states, but such phases are notoriously difficult to realize and highly fragile against perturbations. Here, we propose an alternative route to flat-bands by introducing sp3 hybridization in twisted graphite. Instead of relying on fine-tuned magic angles, our approach identifies flat-band states at relatively large twist angles with short moire periods. In this regime, sp3-induced reconstructions generate electronic states that, once formed, are locked by substantial energy barriers, rendering them robust against external perturbations. Using twisted graphite as a prototype, we uncover a series moire-diamond that host two-dimensional flat conduction of valence bands, where carriers are localized within specific momentum planes but remain dispersive along orthogonal directions. The emergence of dimensional flat-bands opens a new platform for flat-band-driven correlated physics and suggests opportunities for designing quantum materials with highly directional electronic functionalities....

---

### 123. FRIREN: Beyond Trajectories -- A Spectral Lens on Time

**Authors:** Qilin Wang

**Published:** 2025-05-23

**Category:** cs.LG

**ID:** 2505.17370v4

**Link:** [http://arxiv.org/abs/2505.17370v4](http://arxiv.org/abs/2505.17370v4)

**Summary:** Long-term time-series forecasting (LTSF) models are often presented as general-purpose solutions that can be applied across domains, implicitly assuming that all data is pointwise predictable. Using chaotic systems such as Lorenz-63 as a case study, we argue that geometric structure - not pointwise prediction - is the right abstraction for a dynamic-agnostic foundational model. Minimizing the Wasserstein-2 distance (W2), which captures geometric changes, and providing a spectral view of dynamics are essential for long-horizon forecasting. Our model, FRIREN (Flow-inspired Representations via Interpretable Eigen-networks), implements an augmented normalizing-flow block that embeds data into a normally distributed latent representation. It then generates a W2-efficient optimal path that can be decomposed into rotation, scaling, inverse rotation, and translation. This architecture yields locally generated, geometry-preserving predictions that are independent of the underlying dynamics, and a global spectral representation that functions as a finite Koopman operator with a small modification. This enables practitioners to identify which modes grow, decay, or oscillate, both locally and system-wide. FRIREN achieves an MSE of 11.4, MAE of 1.6, and SWD of 0.96 on Lorenz-63 in a 336-in, 336-out, dt=0.01 setting, surpassing TimeMixer (MSE 27.3, MAE 2.8, SWD 2.1). The model maintains effective prediction for 274 out of 336 steps, approximately 2.5 Lyapunov times. On Rossler (96-in, 336-out), FRIREN achieves an MSE of 0.0349, MAE of 0.0953, and SWD of 0.0170, outperforming TimeMixer's MSE of 4.3988, MAE of 0.886, and SWD of 3.2065. FRIREN is also competitive on standard LTSF datasets such as ETT and Weather. By connecting modern generative flows with classical spectral analysis, FRIREN makes long-term forecasting both accurate and interpretable, setting a new benchmark for LTSF model design....

---

### 124. PRISM: Enhancing Protein Inverse Folding through Fine-Grained Retrieval on Structure-Sequence Multimodal Representations

**Authors:** Sazan Mahbub, Souvik Kundu, Eric P. Xing

**Published:** 2025-10-12

**Category:** q-bio.QM

**ID:** 2510.11750v1

**Link:** [http://arxiv.org/abs/2510.11750v1](http://arxiv.org/abs/2510.11750v1)

**Summary:** Designing protein sequences that fold into a target three-dimensional structure, known as the inverse folding problem, is central to protein engineering but remains challenging due to the vast sequence space and the importance of local structural constraints. Existing deep learning approaches achieve strong recovery rates, yet they lack explicit mechanisms to reuse fine-grained structure-sequence patterns that are conserved across natural proteins. We present PRISM, a multimodal retrieval-augmented generation framework for inverse folding that retrieves fine-grained representations of potential motifs from known proteins and integrates them with a hybrid self-cross attention decoder. PRISM is formulated as a latent-variable probabilistic model and implemented with an efficient approximation, combining theoretical grounding with practical scalability. Across five benchmarks (CATH-4.2, TS50, TS500, CAMEO 2022, and the PDB date split), PRISM establishes new state of the art in both perplexity and amino acid recovery, while also improving foldability metrics (RMSD, TM-score, pLDDT), demonstrating that fine-grained multimodal retrieval is a powerful and efficient paradigm for protein sequence design....

---

### 125. Progressive Scale Convolutional Network for Spatio-Temporal Downscaling of Soil Moisture: A Case Study Over the Tibetan Plateau

**Authors:** Ziyu Zhou, Keyan Hu, Ling Zhang, Zhaohui Xue, Yutian Fang, Yusha Zheng

**Published:** 2025-10-11

**Category:** cs.LG

**ID:** 2510.10244v1

**Link:** [http://arxiv.org/abs/2510.10244v1](http://arxiv.org/abs/2510.10244v1)

**Summary:** Soil moisture (SM) plays a critical role in hydrological and meteorological processes. High-resolution SM can be obtained by combining coarse passive microwave data with fine-scale auxiliary variables. However, the inversion of SM at the temporal scale is hindered by the incompleteness of surface auxiliary factors. To address this issue, first, we introduce validated high temporal resolution ERA5-Land variables into the downscaling process of the low-resolution SMAP SM product. Subsequently, we design a progressive scale convolutional network (PSCNet), at the core of which are two innovative components: a multi-frequency temporal fusion module (MFTF) for capturing temporal dynamics, and a bespoke squeeze-and-excitation (SE) block designed to preserve fine-grained spatial details. Using this approach, we obtained seamless SM products for the Tibetan Plateau (TP) from 2016 to 2018 at 10-km spatial and 3-hour temporal resolution. The experimental results on the TP demonstrated the following: 1) In the satellite product validation, the PSCNet exhibited comparable accuracy and lower error, with a mean R value of 0.881, outperforming other methods. 2) In the in-situ site validation, PSCNet consistently ranked among the top three models for the R metric across all sites, while also showing superior performance in overall error reduction. 3) In the temporal generalization validation, the feasibility of using high-temporal resolution ERA5-Land variables for downscaling was confirmed, as all methods maintained an average relative error within 6\% for the R metric and 2\% for the ubRMSE metric. 4) In the temporal dynamics and visualization validation, PSCNet demonstrated excellent temporal sensitivity and vivid spatial details. Overall, PSCNet provides a promising solution for spatio-temporal downscaling by effectively modeling the intricate spatio-temporal relationships in SM data....

---

### 126. Doc2SAR: A Synergistic Framework for High-Fidelity Extraction of Structure-Activity Relationships from Scientific Documents

**Authors:** Jiaxi Zhuang, Kangning Li, Jue Hou, Mingjun Xu, Zhifeng Gao, Hengxing Cai

**Published:** 2025-06-24

**Category:** cs.CL

**ID:** 2506.21625v2

**Link:** [http://arxiv.org/abs/2506.21625v2](http://arxiv.org/abs/2506.21625v2)

**Summary:** Extracting molecular structure-activity relationships (SARs) from scientific literature and patents is essential for drug discovery and materials research. However, this task remains challenging due to heterogeneous document formats and limitations of existing methods. Specifically, rule-based approaches relying on rigid templates fail to generalize across diverse document layouts, while general-purpose multimodal large language models (MLLMs) lack sufficient accuracy and reliability for specialized tasks, such as layout detection and optical chemical structure recognition (OCSR). To address these challenges, we introduce DocSAR-200, a rigorously annotated benchmark of 200 scientific documents designed specifically for evaluating SAR extraction methods. Additionally, we propose Doc2SAR, a novel synergistic framework that integrates domain-specific tools with MLLMs enhanced via supervised fine-tuning (SFT). Extensive experiments demonstrate that Doc2SAR achieves state-of-the-art performance across various document types, significantly outperforming leading end-to-end baselines. Specifically, Doc2SAR attains an overall Table Recall of 80.78% on DocSAR-200, exceeding end2end GPT-4o by 51.48%. Furthermore, Doc2SAR demonstrates practical usability through efficient inference and is accompanied by a web app....

---

### 127. Physics-Inspired Binary Neural Networks: Interpretable Compression with Theoretical Guarantees

**Authors:** Arian Eamaz, Farhang Yeganegi, Mojtaba Soltanalian

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.01908v3

**Link:** [http://arxiv.org/abs/2502.01908v3](http://arxiv.org/abs/2502.01908v3)

**Summary:** Why rely on dense neural networks and then blindly sparsify them when prior knowledge about the problem structure is already available? Many inverse problems admit algorithm-unrolled networks that naturally encode physics and sparsity. In this work, we propose a Physics-Inspired Binary Neural Network (PIBiNN) that combines two key components: (i) data-driven one-bit quantization with a single global scale, and (ii) problem-driven sparsity predefined by physics and requiring no updates during training. This design yields compression rates below one bit per weight by exploiting structural zeros, while preserving essential operator geometry. Unlike ternary or pruning-based schemes, our approach avoids ad-hoc sparsification, reduces metadata overhead, and aligns directly with the underlying task. Experiments suggest that PIBiNN achieves advantages in both memory efficiency and generalization compared to competitive baselines such as ternary and channel-wise quantization....

---

### 128. AbBiBench: A Benchmark for Antibody Binding Affinity Maturation and Design

**Authors:** Xinyan Zhao, Yi-Ching Tang, Akshita Singh, Victor J Cantu, KwanHo An, Junseok Lee, Adam E Stogsdill, Ibraheem M Hamdi, Ashwin Kumar Ramesh, Zhiqiang An, Xiaoqian Jiang, Yejin Kim

**Published:** 2025-05-23

**Category:** q-bio.QM

**ID:** 2506.04235v2

**Link:** [http://arxiv.org/abs/2506.04235v2](http://arxiv.org/abs/2506.04235v2)

**Summary:** We introduce AbBiBench (Antibody Binding Benchmarking), a benchmarking framework for antibody binding affinity maturation and design. Unlike previous strategies that evaluate antibodies in isolation, typically by comparing them to natural sequences with metrics such as amino acid recovery rate or structural RMSD, AbBiBench instead treats the antibody-antigen (Ab-Ag) complex as the fundamental unit. It evaluates an antibody design's binding potential by measuring how well a protein model scores the full Ab-Ag complex. We first curate, standardize, and share more than 184,500 experimental measurements of antibody mutants across 14 antibodies and 9 antigens-including influenza, lysozyme, HER2, VEGF, integrin, Ang2, and SARS-CoV-2-covering both heavy-chain and light-chain mutations. Using these datasets, we systematically compare 15 protein models including masked language models, autoregressive language models, inverse folding models, diffusion-based generative models, and geometric graph models by comparing the correlation between model likelihood and experimental affinity values. Additionally, to demonstrate AbBiBench's generative utility, we apply it to antibody F045-092 in order to introduce binding to influenza H1N1. We sample new antibody variants with the top-performing models, rank them by the structural integrity and biophysical properties of the Ab-Ag complex, and assess them with in vitro ELISA binding assays. Our findings show that structure-conditioned inverse folding models outperform others in both affinity correlation and generation tasks. Overall, AbBiBench provides a unified, biologically grounded evaluation framework to facilitate the development of more effective, function-aware antibody design models....

---

### 129. SpectralCA: Bi-Directional Cross-Attention for Next-Generation UAV Hyperspectral Vision

**Authors:** D. V. Brovko

**Published:** 2025-10-10

**Category:** cs.CV

**ID:** 2510.09912v1

**Link:** [http://arxiv.org/abs/2510.09912v1](http://arxiv.org/abs/2510.09912v1)

**Summary:** The relevance of this research lies in the growing demand for unmanned aerial vehicles (UAVs) capable of operating reliably in complex environments where conventional navigation becomes unreliable due to interference, poor visibility, or camouflage. Hyperspectral imaging (HSI) provides unique opportunities for UAV-based computer vision by enabling fine-grained material recognition and object differentiation, which are critical for navigation, surveillance, agriculture, and environmental monitoring. The aim of this work is to develop a deep learning architecture integrating HSI into UAV perception for navigation, object detection, and terrain classification. Objectives include: reviewing existing HSI methods, designing a hybrid 2D/3D convolutional architecture with spectral-spatial cross-attention, training, and benchmarking. The methodology is based on the modification of the Mobile 3D Vision Transformer (MDvT) by introducing the proposed SpectralCA block. This block employs bi-directional cross-attention to fuse spectral and spatial features, enhancing accuracy while reducing parameters and inference time. Experimental evaluation was conducted on the WHU-Hi-HongHu dataset, with results assessed using Overall Accuracy, Average Accuracy, and the Kappa coefficient. The findings confirm that the proposed architecture improves UAV perception efficiency, enabling real-time operation for navigation, object recognition, and environmental monitoring tasks.
  Keywords: SpectralCA, deep learning, computer vision, hyperspectral imaging, unmanned aerial vehicle, object detection, semi-supervised learning....

---

### 130. Solving Linear-Gaussian Bayesian Inverse Problems with Decoupled Diffusion Sequential Monte Carlo

**Authors:** Filip Ekström Kelvinius, Zheng Zhao, Fredrik Lindsten

**Published:** 2025-02-10

**Category:** cs.LG

**ID:** 2502.06379v3

**Link:** [http://arxiv.org/abs/2502.06379v3](http://arxiv.org/abs/2502.06379v3)

**Summary:** A recent line of research has exploited pre-trained generative diffusion models as priors for solving Bayesian inverse problems. We contribute to this research direction by designing a sequential Monte Carlo method for linear-Gaussian inverse problems which builds on "decoupled diffusion", where the generative process is designed such that larger updates to the sample are possible. The method is asymptotically exact and we demonstrate the effectiveness of our Decoupled Diffusion Sequential Monte Carlo (DDSMC) algorithm on both synthetic as well as protein and image data. Further, we demonstrate how the approach can be extended to discrete data....

---

### 131. WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry

**Authors:** Filip Ekström Kelvinius, Oskar B. Andersson, Abhijith S. Parackal, Dong Qian, Rickard Armiento, Fredrik Lindsten

**Published:** 2025-02-10

**Category:** cond-mat.mtrl-sci

**ID:** 2502.06485v4

**Link:** [http://arxiv.org/abs/2502.06485v4](http://arxiv.org/abs/2502.06485v4)

**Summary:** Crystalline materials often exhibit a high level of symmetry. However, most generative models do not account for symmetry, but rather model each atom without any constraints on its position or element. We propose a generative model, Wyckoff Diffusion (WyckoffDiff), which generates symmetry-based descriptions of crystals. This is enabled by considering a crystal structure representation that encodes all symmetry, and we design a novel neural network architecture which enables using this representation inside a discrete generative model framework. In addition to respecting symmetry by construction, the discrete nature of our model enables fast generation. We additionally present a new metric, Fréchet Wrenformer Distance, which captures the symmetry aspects of the materials generated, and we benchmark WyckoffDiff against recently proposed generative models for crystal generation. As a proof-of-concept study, we use WyckoffDiff to find new materials below the convex hull of thermodynamical stability....

---

### 132. MagicDock: Toward Docking-oriented De Novo Ligand Design via Gradient Inversion

**Authors:** Zekai Chen, Xunkai Li, Sirui Zhang, Henan Sun, Jia Li, Zhenjun Li, Bing Zhou, Rong-Hua Li, Guoren Wang

**Published:** 2025-10-10

**Category:** cs.LG

**ID:** 2510.09020v1

**Link:** [http://arxiv.org/abs/2510.09020v1](http://arxiv.org/abs/2510.09020v1)

**Summary:** De novo ligand design is a fundamental task that seeks to generate protein or molecule candidates that can effectively dock with protein receptors and achieve strong binding affinity entirely from scratch. It holds paramount significance for a wide spectrum of biomedical applications. However, most existing studies are constrained by the \textbf{Pseudo De Novo}, \textbf{Limited Docking Modeling}, and \textbf{Inflexible Ligand Type}. To address these issues, we propose MagicDock, a forward-looking framework grounded in the progressive pipeline and differentiable surface modeling. (1) We adopt a well-designed gradient inversion framework. To begin with, general docking knowledge of receptors and ligands is incorporated into the backbone model. Subsequently, the docking knowledge is instantiated as reverse gradient flows by binding prediction, which iteratively guide the de novo generation of ligands. (2) We emphasize differentiable surface modeling in the docking process, leveraging learnable 3D point-cloud representations to precisely capture binding details, thereby ensuring that the generated ligands preserve docking validity through direct and interpretable spatial fingerprints. (3) We introduce customized designs for different ligand types and integrate them into a unified gradient inversion framework with flexible triggers, thereby ensuring broad applicability. Moreover, we provide rigorous theoretical guarantees for each component of MagicDock. Extensive experiments across 9 scenarios demonstrate that MagicDock achieves average improvements of 27.1\% and 11.7\% over SOTA baselines specialized for protein or molecule ligand design, respectively....

---

### 133. A Frequency-Domain Analysis of the Multi-Armed Bandit Problem: A New Perspective on the Exploration-Exploitation Trade-off

**Authors:** Di Zhang

**Published:** 2025-10-10

**Category:** cs.LG

**ID:** 2510.08908v1

**Link:** [http://arxiv.org/abs/2510.08908v1](http://arxiv.org/abs/2510.08908v1)

**Summary:** The stochastic multi-armed bandit (MAB) problem is one of the most fundamental models in sequential decision-making, with the core challenge being the trade-off between exploration and exploitation. Although algorithms such as Upper Confidence Bound (UCB) and Thompson Sampling, along with their regret theories, are well-established, existing analyses primarily operate from a time-domain and cumulative regret perspective, struggling to characterize the dynamic nature of the learning process. This paper proposes a novel frequency-domain analysis framework, reformulating the bandit process as a signal processing problem. Within this framework, the reward estimate of each arm is viewed as a spectral component, with its uncertainty corresponding to the component's frequency, and the bandit algorithm is interpreted as an adaptive filter. We construct a formal Frequency-Domain Bandit Model and prove the main theorem: the confidence bound term in the UCB algorithm is equivalent in the frequency domain to a time-varying gain applied to uncertain spectral components, a gain inversely proportional to the square root of the visit count. Based on this, we further derive finite-time dynamic bounds concerning the exploration rate decay. This theory not only provides a novel and intuitive physical interpretation for classical algorithms but also lays a rigorous theoretical foundation for designing next-generation algorithms with adaptive parameter adjustment....

---

### 134. Graph Diffusion Transformers are In-Context Molecular Designers

**Authors:** Gang Liu, Jie Chen, Yihan Zhu, Michael Sun, Tengfei Luo, Nitesh V Chawla, Meng Jiang

**Published:** 2025-10-09

**Category:** cs.LG

**ID:** 2510.08744v1

**Link:** [http://arxiv.org/abs/2510.08744v1](http://arxiv.org/abs/2510.08744v1)

**Summary:** In-context learning allows large models to adapt to new tasks from a few demonstrations, but it has shown limited success in molecular design. Existing databases such as ChEMBL contain molecular properties spanning millions of biological assays, yet labeled data for each property remain scarce. To address this limitation, we introduce demonstration-conditioned diffusion models (DemoDiff), which define task contexts using a small set of molecule-score examples instead of text descriptions. These demonstrations guide a denoising Transformer to generate molecules aligned with target properties. For scalable pretraining, we develop a new molecular tokenizer with Node Pair Encoding that represents molecules at the motif level, requiring 5.5$\times$ fewer nodes. We curate a dataset containing millions of context tasks from multiple sources covering both drugs and materials, and pretrain a 0.7-billion-parameter model on it. Across 33 design tasks in six categories, DemoDiff matches or surpasses language models 100-1000$\times$ larger and achieves an average rank of 3.63 compared to 5.25-10.20 for domain-specific approaches. These results position DemoDiff as a molecular foundation model for in-context molecular design. Our code is available at https://github.com/liugangcode/DemoDiff....

---

### 135. Perovskite-LLM: Knowledge-Enhanced Large Language Models for Perovskite Solar Cell Research

**Authors:** Xiang Liu, Penglei Sun, Shuyan Chen, Longhan Zhang, Peijie Dong, Huajie You, Yongqi Zhang, Chang Yan, Xiaowen Chu, Tong-yi Zhang

**Published:** 2025-02-18

**Category:** cs.AI

**ID:** 2502.12669v3

**Link:** [http://arxiv.org/abs/2502.12669v3](http://arxiv.org/abs/2502.12669v3)

**Summary:** The rapid advancement of perovskite solar cells (PSCs) has led to an exponential growth in research publications, creating an urgent need for efficient knowledge management and reasoning systems in this domain. We present a comprehensive knowledge-enhanced system for PSCs that integrates three key components. First, we develop Perovskite-KG, a domain-specific knowledge graph constructed from 1,517 research papers, containing 23,789 entities and 22,272 relationships. Second, we create two complementary datasets: Perovskite-Chat, comprising 55,101 high-quality question-answer pairs generated through a novel multi-agent framework, and Perovskite-Reasoning, containing 2,217 carefully curated materials science problems. Third, we introduce two specialized large language models: Perovskite-Chat-LLM for domain-specific knowledge assistance and Perovskite-Reasoning-LLM for scientific reasoning tasks. Experimental results demonstrate that our system significantly outperforms existing models in both domain-specific knowledge retrieval and scientific reasoning tasks, providing researchers with effective tools for literature review, experimental design, and complex problem-solving in PSC research....

---

### 136. Monopole Traps for Position-Based Information Coding

**Authors:** Prakash Timsina, Andres Chappa, Deema Alyones, Boris Kiefer, Ludi Miao

**Published:** 2025-07-30

**Category:** cond-mat.str-el

**ID:** 2507.22315v2

**Link:** [http://arxiv.org/abs/2507.22315v2](http://arxiv.org/abs/2507.22315v2)

**Summary:** We propose a spin-ice-based heterostructure capable of encoding magnetic monopole quasiparticle positions for non-volatile information storage applications. Building upon two-dimensional magnetic monopole gases formed at the interface between 2-in-2-out spin ice and all-in-all-out antiferromagnetic pyrochlore iridate, the design introduces a 3-in-1-out/1-in-3-out fragmented barrier layer into the spin-ice matrix, defining two energetically stable monopole traps. The occupancy of these traps can be deterministically controlled by an externally applied magnetic field. Monte Carlo simulations reveal robust bistable switching, thermal stability below 0.22 K, and fully reversible field-driven transitions, demonstrating the system's potential for reliable, repeatable memory operation. Crucially, the heterostructure exhibits emergent ferromagnetism linked to monopole position, enabling non-destructive readout of the memory state via spatially resolved magnetic imaging. Unlike topological carriers such as skyrmions, monopoles confined at the sub-nanometer scale offer three orders of magnitude higher information density. These results establish these monopole-trap heterostructures as a scalable platform for next-generation ultra-compact memory technologies....

---

### 137. Active-Learning Inspired $\textit{Ab Initio}$ Theory-Experiment Loop Approach for Management of Material Defects: Application to Superconducting Qubits

**Authors:** Sarvesh Chaudhari, Cristóbal Méndez, Rushil Choudhary, Tathagata Banerjee, Maciej W. Olszewski, Jadrien T. Paustian, Jaehong Choi, Zhaslan Baraissov, Raul Hernandez, David A. Muller, B. L. T. Plourde, Gregory D. Fuchs, Valla Fatemi, Tomás A. Arias

**Published:** 2025-10-02

**Category:** cond-mat.mtrl-sci

**ID:** 2510.02544v2

**Link:** [http://arxiv.org/abs/2510.02544v2](http://arxiv.org/abs/2510.02544v2)

**Summary:** Surface oxides are associated with two-level systems (TLSs) that degrade the performance of niobium-based superconducting quantum computing devices. To address this, we introduce a predictive framework for selecting metal capping layers that inhibit niobium oxide formation. Using DFT-calculated oxygen interstitial and vacancy energies as thermodynamic descriptors, we train a logistic regression model on a limited set of experimental outcomes to successfully predict the likelihood of oxide formation beneath different capping materials. This approach identifies Zr, Hf, and Ta as effective diffusion barriers. Our analysis further reveals that the oxide formation energy per oxygen atom serves as an excellent standalone descriptor for predicting barrier performance. By combining this new descriptor with lattice mismatch as a secondary criterion to promote structurally coherent interfaces, we identify Zr, Ta, and Sc as especially promising candidates. This closed-loop strategy integrates first-principles theory, machine learning, and limited experimental data to enable rational design of next-generation materials....

---

### 138. Hot-carrier generation in bimetallic Janus nanoparticles

**Authors:** Hanwen Jin, Chengcheng Xiao, Matias Herran, Emiliano Cortes, Shiwu Gao, Johannes Lischner

**Published:** 2025-10-09

**Category:** physics.optics

**ID:** 2510.07982v1

**Link:** [http://arxiv.org/abs/2510.07982v1](http://arxiv.org/abs/2510.07982v1)

**Summary:** Energetic electrons and holes generated from the decay of localized surface plasmons in metallic nanoparticles can be harnessed in nanoscale devices for photocatalysis, photovoltaics or sensing. In this work, we study the generation of such hot carriers in bimetallic Janus nanoparticles composed of Au, Ag and Cu using a recently developed atomistic modelling approach that combines a solution of the macroscopic Maxwell equation with large-scale quantum-mechanical tight-binding models. We first analyze spherical Janus nanoparticles whose unique hot-carrier spectrum can be associated with the spectra of the two hemispheres and the interface coupling and find that under solar illumination the Ag-Au system exhibits the highest hot-carrier generation rate. For dumbbell-shaped Janus nanoparticles, we observe a significant increase in hot-carrier generation with increasing neck size. This is caused by a dramatic enhancement of the electric field in the neck region. We also study the dependence of hot-carrier generation on the light polarization and find that the largest generation rates are obtained when the electric field is perpendicular to the interface between the two metals due to the maximal dipole coupling with the electric field. The insights from our study will guide the experimental design of efficient hot-carrier devices based on bimetallic Janus nanoparticles....

---

### 139. Upfront Chain-of-Thought: A Cooperative Framework for Chain-of-Thought Compression

**Authors:** Chengzhengxu Li, Xiaoming Liu, Zhaohan Zhang, Shaochu Zhang, Shengchao Liu, Guoxin Ma, Yu Lan, Chao Shen

**Published:** 2025-10-09

**Category:** cs.CL

**ID:** 2510.08647v1

**Link:** [http://arxiv.org/abs/2510.08647v1](http://arxiv.org/abs/2510.08647v1)

**Summary:** Recent developments have enabled advanced reasoning in Large Language Models (LLMs) via long Chain-of-Thought (CoT), while long CoT suffers from high computational costs and significant latency losses owing to the autoregressive nature of generative LLMs. CoT compression aims to improve efficiency in the reasoning process by reducing output length. Previous works trade reasoning efficiency by either laborious discrete prompt designing or the construction of external compressed CoT datasets that sacrifice key reasoning details. In this work, we propose Upfront CoT (UCoT): an efficient reasoning framework with upfront thought embedding to automate CoT compression. UCoT is a cooperative workflow involving a small model (compressor) and a large model (executor). The first stage of UCoT trains compressor to generate upfront thought embeddings rich in reasoning information for the executor, avoiding the drawbacks of manually designed prompts. The second stage optimizes executor to utilize upfront thought embeddings to derive the correct answer with short reasoning, using a reward mechanism. Extensive experiments show that UCoT maintains the powerful reasoning ability of executor while significantly reducing the length of CoT. It is worth mentioning that when applying UCoT to the Qwen2.5-7B-Instruct model, the usage of tokens on GSM8K dataset is reduced by 50\%, while the performance is 3.08\% higher than that of the state-of-the-art (SOTA) method. The code and dataset are in supplementary material....

---

### 140. Towards Urban Planing AI Agent in the Age of Agentic AI

**Authors:** Rui Liu, Tao Zhe, Zhong-Ren Peng, Necati Catbas, Xinyue Ye, Dongjie Wang, Yanjie Fu

**Published:** 2025-07-19

**Category:** cs.AI

**ID:** 2507.14730v4

**Link:** [http://arxiv.org/abs/2507.14730v4](http://arxiv.org/abs/2507.14730v4)

**Summary:** Generative AI, large language models, and agentic AI have emerged separately of urban planning. However, the convergence between AI and urban planning presents an interesting opportunity towards AI urban planners. Existing studies conceptualizes urban planning as a generative AI task, where AI synthesizes land-use configurations under geospatial, social, and human-centric constraints and reshape automated urban design. We further identify critical gaps of existing generative urban planning studies: 1) the generative structure has to be predefined with strong assumption: all of adversarial generator-discriminator, forward and inverse diffusion structures, hierarchical zone-POI generative structure are predefined by humans; 2) ignore the power of domain expert developed tools: domain urban planners have developed various tools in the urban planning process guided by urban theory, while existing pure neural networks based generation ignore the power of the tools developed by urban planner practitioners. To address these limitations, we outline a future research direction agentic urban AI planner, calling for a new synthesis of agentic AI and participatory urbanism....

---

### 141. Stochastic Hessian Fittings with Lie Groups

**Authors:** Xi-Lin Li

**Published:** 2024-02-19

**Category:** stat.ML

**ID:** 2402.11858v6

**Link:** [http://arxiv.org/abs/2402.11858v6](http://arxiv.org/abs/2402.11858v6)

**Summary:** This report investigates the fitting of the Hessian or its inverse for stochastic optimizations using a Hessian fitting criterion derived from the preconditioned stochastic gradient descent (PSGD) method. This criterion is closely related to many widely used second-order and adaptive gradient optimization methods, including BFGS, the Gauss-Newton algorithm, natural gradient descent, and AdaGrad. Our analyses reveal the efficiency and reliability differences of a broad range of preconditioner fitting methods, ranging from closed-form to iterative approaches, using Hessian-vector products or stochastic gradients only, with Hessian fittings across various geometric settings (the Euclidean space, the manifold of symmetric positive definite (SPD) matrices, and a variety of Lie groups). The most intriguing finding is that the Hessian fitting problem is strongly convex under mild conditions in certain general Lie groups. This result turns the Hessian fitting into a well-behaved Lie group optimization problem and facilitates the design of highly efficient and elegant Lie group sparse preconditioner fitting methods for large-scale stochastic optimizations....

---

### 142. Contrastive Graph Condensation: Advancing Data Versatility through Self-Supervised Learning

**Authors:** Xinyi Gao, Yayong Li, Tong Chen, Guanhua Ye, Wentao Zhang, Hongzhi Yin

**Published:** 2024-11-26

**Category:** cs.LG

**ID:** 2411.17063v2

**Link:** [http://arxiv.org/abs/2411.17063v2](http://arxiv.org/abs/2411.17063v2)

**Summary:** With the increasing computation of training graph neural networks (GNNs) on large-scale graphs, graph condensation (GC) has emerged as a promising solution to synthesize a compact, substitute graph of the large-scale original graph for efficient GNN training. However, existing GC methods predominantly employ classification as the surrogate task for optimization, thus excessively relying on node labels and constraining their utility in label-sparsity scenarios. More critically, this surrogate task tends to overfit class-specific information within the condensed graph, consequently restricting the generalization capabilities of GC for other downstream tasks. To address these challenges, we introduce Contrastive Graph Condensation (CTGC), which adopts a self-supervised surrogate task to extract critical, causal information from the original graph and enhance the cross-task generalizability of the condensed graph. Specifically, CTGC employs a dual-branch framework to disentangle the generation of the node attributes and graph structures, where a dedicated structural branch is designed to explicitly encode geometric information through nodes' positional embeddings. By implementing an alternating optimization scheme with contrastive loss terms, CTGC promotes the mutual enhancement of both branches and facilitates high-quality graph generation through the model inversion technique. Extensive experiments demonstrate that CTGC excels in handling various downstream tasks with a limited number of labels, consistently outperforming state-of-the-art GC methods....

---

### 143. Unveiling the Lithium-Ion Transport Mechanism in Li2ZrCl6 Solid-State Electrolyte via Deep Learning-Accelerated Molecular Dynamics Simulations

**Authors:** Hanzeng Guo, Volodymyr Koverga, Selva Chandrasekaran Selvaraj, Anh T. Ngo

**Published:** 2025-08-07

**Category:** cond-mat.mtrl-sci

**ID:** 2508.05598v2

**Link:** [http://arxiv.org/abs/2508.05598v2](http://arxiv.org/abs/2508.05598v2)

**Summary:** Lithium zirconium chlorides (LZCs) present a promising class of cost-effective solid electrolyte for next-generation all-solid-state batteries. The unique crystal structure of LZCs plays a crucial role in facilitating lithium-ion mobility, which further affects its electrochemical performance. To understand the underlying mechanism governing ion transport, we employed deep learning-accelerated molecular dynamics simulation on Li2ZrCl6 (trigonal α- and monoclinic \b{eta}-LZC), focusing specifically on the zirconium coordination environment. Our results reveal that disordered α-LZC exhibits the highest ionic conductivity, while \b{eta}-LZC demonstrates significantly lower conductivity, closely aligning with experimental findings. The study confirms that across all phases, lithium migration proceeds via site-to-site hopping mechanism, where variations in site residence times critically impact the overall ionic conductivity. In α-LZCs, lithium ions prefer to anisotropically diffuse across interlayers as the result of lower energy barrier, driven primarily by collective diffusion. In contrast, lithium ions in \b{eta}-LZC primarily isotropically diffuse within intralayer, hindered by higher energy barriers and determined by individual diffusion. The variation in ZrCl62- octahedral unit softening, induced by the specific layered arrangement of zirconium atoms, emerges as a critical determinant of the energy barriers across the LZC phases. These atomic-scale insights into the transport processes provide valuable guidance for the rational design and optimization of LZCs-based electrolytes, accelerating their practical application in advanced energy storage technologies....

---

### 144. Origin of trapped intralayer Wannier and charge-transfer excitons in moiré materials

**Authors:** Indrajit Maity, Johannes Lischner, Arash A. Mostofi, Ángel Rubio

**Published:** 2025-10-07

**Category:** cond-mat.mtrl-sci

**ID:** 2510.06137v1

**Link:** [http://arxiv.org/abs/2510.06137v1](http://arxiv.org/abs/2510.06137v1)

**Summary:** Moiré materials offer a versatile platform for engineering excitons with unprecedented control, promising next-generation optoelectronic applications. While continuum models are widely used to study moiré excitons due to their computational efficiency, they often disagree with ab initio many-body approaches, as seen for intralayer excitons in WS$_2$/WSe$_2$ heterobilayers. Here, we resolve these discrepancies using an atomistic, quantum-mechanical framework based on the Bethe-Salpeter equation with localized Wannier functions as the basis for the electronic structure. We show that inclusion of dielectric screening due to hexagonal boron nitride (hBN) encapsulation is essential to reproduce the full set of experimentally observed features of moiré intralayer excitons. Our analysis reveals a competition between Wannier and charge transfer characters, driven by variations between direct and indirect band gaps at high symmetry stacking regions due to atomic relaxations and environmentally tunable electron-hole interactions. Building on this insight, we demonstrate that the lowest-energy bright excitons are Wannier-like in WS2/WSe2 heterobilayers but charge-transfer-like in twisted WSe2 homobilayers, despite having comparable moiré lengths when encapsulated in hBN. In the absence of hBN encapsulation, the lowest-energy bright exciton in twisted WSe$_2$ becomes Wannier-like. These results establish atomistic modeling as a powerful and efficient approach for designing and controlling excitonic phenomena in moiré materials....

---

### 145. Benchmark It Yourself (BIY): Preparing a Dataset and Benchmarking AI Models for Scatterplot-Related Tasks

**Authors:** João Palmeiro, Diogo Duarte, Rita Costa, Pedro Bizarro

**Published:** 2025-10-07

**Category:** cs.LG

**ID:** 2510.06071v1

**Link:** [http://arxiv.org/abs/2510.06071v1](http://arxiv.org/abs/2510.06071v1)

**Summary:** AI models are increasingly used for data analysis and visualization, yet benchmarks rarely address scatterplot-specific tasks, limiting insight into performance. To address this gap for one of the most common chart types, we introduce a synthetic, annotated dataset of over 18,000 scatterplots from six data generators and 17 chart designs, and a benchmark based on it. We evaluate proprietary models from OpenAI and Google using N-shot prompting on five distinct tasks derived from annotations of cluster bounding boxes, their center coordinates, and outlier coordinates. OpenAI models and Gemini 2.5 Flash, especially when prompted with examples, are viable options for counting clusters and, in Flash's case, outliers (90%+ Accuracy). However, the results for localization-related tasks are unsatisfactory: Precision and Recall are near or below 50%, except for Flash in outlier identification (65.01%). Furthermore, the impact of chart design on performance appears to be a secondary factor, but it is advisable to avoid scatterplots with wide aspect ratios (16:9 and 21:9) or those colored randomly. Supplementary materials are available at https://github.com/feedzai/biy-paper....

---

### 146. Confinement-Controlled Morphology and Stability of One-Dimensional CrI3 Nanotubes

**Authors:** Ihsan Caha, Aqrab ul Ahmad, Francis Leonard Deepak

**Published:** 2025-10-07

**Category:** cond-mat.mtrl-sci

**ID:** 2510.05889v1

**Link:** [http://arxiv.org/abs/2510.05889v1](http://arxiv.org/abs/2510.05889v1)

**Summary:** Integrating monolayers derived from 2D van der Waals (vdW) magnetic materials into next-generation technological applications remains a significant challenge due to their structural and magnetic instability issues. Template-assisted encapsulation is a potential route for the growth of stable 2D monolayers aimed at designing novel 1D heterostructures, opening new avenues for studying low-dimensional quantum effects and spin-related phenomena. In this study, we explored the diameter-dependent encapsulation of 2D CrI3 crystals using multi-walled carbon nanotubes as nanoscale host templates. Advanced microscopic analysis revealed distinct structural transitions, ranging from internal nanorod encapsulation to external shell formation, directly influenced by the host nanotube diameter. Furthermore, statistical analysis of structural morphologies indicates that CrI3 nanorods preferentially form within MWCNTs with inner diameters up to 5 nm, while single-walled CrI3 nanotubes are stabilized in CNTs with diameters up to 8 nm. For host CNTs exceeding 10 nm in diameter, CrI3 predominantly forms surface coatings rather than confined one-dimensional structures. In situ electron beam irradiation demonstrates the superior structural stability of single-walled CrI3 confined within MWCNTs, while externally coated CrI3 undergoes decomposition into metallic Cr clusters. Prolonged irradiation induces a morphological transformation of CrI3 nanotubes into nanorods. These insights lay the groundwork for engineering robust, tunable 1D magnetic heterostructures of CrI3 for spintronic and data storage applications....

---

### 147. Generative Models for Helmholtz Equation Solutions: A Dataset of Acoustic Materials

**Authors:** Riccardo Fosco Gramaccioni, Christian Marinoni, Fabrizio Frezza, Aurelio Uncini, Danilo Comminiello

**Published:** 2025-10-07

**Category:** cs.LG

**ID:** 2510.09657v1

**Link:** [http://arxiv.org/abs/2510.09657v1](http://arxiv.org/abs/2510.09657v1)

**Summary:** Accurate simulation of wave propagation in complex acoustic materials is crucial for applications in sound design, noise control, and material engineering. Traditional numerical solvers, such as finite element methods, are computationally expensive, especially when dealing with large-scale or real-time scenarios. In this work, we introduce a dataset of 31,000 acoustic materials, named HA30K, designed and simulated solving the Helmholtz equations. For each material, we provide the geometric configuration and the corresponding pressure field solution, enabling data-driven approaches to learn Helmholtz equation solutions. As a baseline, we explore a deep learning approach based on Stable Diffusion with ControlNet, a state-of-the-art model for image generation. Unlike classical solvers, our approach leverages GPU parallelization to process multiple simulations simultaneously, drastically reducing computation time. By representing solutions as images, we bypass the need for complex simulation software and explicit equation-solving. Additionally, the number of diffusion steps can be adjusted at inference time, balancing speed and quality. We aim to demonstrate that deep learning-based methods are particularly useful in early-stage research, where rapid exploration is more critical than absolute accuracy....

---

### 148. ESS-Flow: Training-free guidance of flow-based models as inference in source space

**Authors:** Adhithyan Kalaivanan, Zheng Zhao, Jens Sjölund, Fredrik Lindsten

**Published:** 2025-10-07

**Category:** cs.LG

**ID:** 2510.05849v1

**Link:** [http://arxiv.org/abs/2510.05849v1](http://arxiv.org/abs/2510.05849v1)

**Summary:** Guiding pretrained flow-based generative models for conditional generation or to produce samples with desired target properties enables solving diverse tasks without retraining on paired data. We present ESS-Flow, a gradient-free method that leverages the typically Gaussian prior of the source distribution in flow-based models to perform Bayesian inference directly in the source space using Elliptical Slice Sampling. ESS-Flow only requires forward passes through the generative model and observation process, no gradient or Jacobian computations, and is applicable even when gradients are unreliable or unavailable, such as with simulation-based observations or quantization in the generation or observation process. We demonstrate its effectiveness on designing materials with desired target properties and predicting protein structures from sparse inter-residue distance measurements....

---

### 149. Nonlinear spin and orbital Rashba-Edelstein effects induced by a femtosecond laser pulse: Simulations for Au(001)

**Authors:** Oliver Busch, Franziska Ziolkowski, Börge Göbel, Ingrid Mertig, Jürgen Henk

**Published:** 2025-05-04

**Category:** cond-mat.mtrl-sci

**ID:** 2505.02006v2

**Link:** [http://arxiv.org/abs/2505.02006v2](http://arxiv.org/abs/2505.02006v2)

**Summary:** Rashba-type spin-orbit coupling gives rise to distinctive surface and interface phenomena, such as spin-momentum locking and spin splitting. In nonequilibrium settings, one of the key manifestations is the (Rashba-)Edelstein effect, where an electric current generates a net spin or orbital polarization perpendicular to the current direction. While the steady-state behavior of these effects is well studied, their dynamics on ultrafast timescales remain largely unexplored. In this work, we present a theoretical investigation of the ultrafast spin and orbital Edelstein effects on an Au(001) surface, triggered by excitation with a femtosecond laser pulse. These effects are intrinsic and inherently nonlinear. Using a real-space tight-binding model combined with time evolution governed by the von Neumann equation, we simulate the electron dynamics in response to the pulse. Our results reveal pronounced differences between the spin and orbital responses, offering detailed insights into their distinct temporal profiles and magnitudes. We further explore the associated charge, spin, and orbital currents, including the emergence of laser-induced spin and orbital Hall effects. Finally, we quantify the angular momentum transfer mediated by the light-matter interaction. These findings shed light on the intricate ultrafast dynamics driven by spin-orbit coupling and offer guidance for the design of next-generation spintronic and orbitronic devices....

---

### 150. ATOM: A Pretrained Neural Operator for Multitask Molecular Dynamics

**Authors:** Luke Thompson, Davy Guan, Dai Shi, Slade Matthews, Junbin Gao, Andi Han

**Published:** 2025-10-07

**Category:** cs.LG

**ID:** 2510.05482v1

**Link:** [http://arxiv.org/abs/2510.05482v1](http://arxiv.org/abs/2510.05482v1)

**Summary:** Molecular dynamics (MD) simulations underpin modern computational drug dis- covery, materials science, and biochemistry. Recent machine learning models provide high-fidelity MD predictions without the need to repeatedly solve quantum mechanical forces, enabling significant speedups over conventional pipelines. Yet many such methods typically enforce strict equivariance and rely on sequential rollouts, thus limiting their flexibility and simulation efficiency. They are also com- monly single-task, trained on individual molecules and fixed timeframes, which restricts generalization to unseen compounds and extended timesteps. To address these issues, we propose Atomistic Transformer Operator for Molecules (ATOM), a pretrained transformer neural operator for multitask molecular dynamics. ATOM adopts a quasi-equivariant design that requires no explicit molecular graph and employs a temporal attention mechanism, allowing for the accurate parallel decod- ing of multiple future states. To support operator pretraining across chemicals and timescales, we curate TG80, a large, diverse, and numerically stable MD dataset with over 2.5 million femtoseconds of trajectories across 80 compounds. ATOM achieves state-of-the-art performance on established single-task benchmarks, such as MD17, RMD17 and MD22. After multitask pretraining on TG80, ATOM shows exceptional zero-shot generalization to unseen molecules across varying time hori- zons. We believe ATOM represents a significant step toward accurate, efficient, and transferable molecular dynamics models...

---

### 151. Fusion-Based Neural Generalization for Predicting Temperature Fields in Industrial PET Preform Heating

**Authors:** Ahmad Alsheikh, Andreas Fischer

**Published:** 2025-10-06

**Category:** cs.LG

**ID:** 2510.05394v1

**Link:** [http://arxiv.org/abs/2510.05394v1](http://arxiv.org/abs/2510.05394v1)

**Summary:** Accurate and efficient temperature prediction is critical for optimizing the preheating process of PET preforms in industrial microwave systems prior to blow molding. We propose a novel deep learning framework for generalized temperature prediction. Unlike traditional models that require extensive retraining for each material or design variation, our method introduces a data-efficient neural architecture that leverages transfer learning and model fusion to generalize across unseen scenarios. By pretraining specialized neural regressor on distinct conditions such as recycled PET heat capacities or varying preform geometries and integrating their representations into a unified global model, we create a system capable of learning shared thermal dynamics across heterogeneous inputs. The architecture incorporates skip connections to enhance stability and prediction accuracy. Our approach reduces the need for large simulation datasets while achieving superior performance compared to models trained from scratch. Experimental validation on two case studies material variability and geometric diversity demonstrates significant improvements in generalization, establishing a scalable ML-based solution for intelligent thermal control in manufacturing environments. Moreover, the approach highlights how data-efficient generalization strategies can extend to other industrial applications involving complex physical modeling with limited data....

---

### 152. Cation vacancies mediate thermochemical water splitting with iron aluminates

**Authors:** Nathan J. Szymanski, Kent J. Warren, Alan W. Weimer, Christopher J. Bartel

**Published:** 2025-10-06

**Category:** cond-mat.mtrl-sci

**ID:** 2510.05328v1

**Link:** [http://arxiv.org/abs/2510.05328v1](http://arxiv.org/abs/2510.05328v1)

**Summary:** Solar thermochemical water splitting enables hydrogen production by cycling metal oxides between reduced and oxidized states, typically through an oxygen vacancy mechanism. However, recent experimental work suggests that cation vacancies have a greater influence on the redox behavior of iron aluminate spinels used in water splitting. This remains debated, as calculations predict that such cation vacancies are thermodynamically unfavorable. In the current work, we show that Fe vacancies in (Fe$ζ$Al1-$ζ$)3O4 become accessible only when facilitated by inversion between Fe and Al. This antisite disorder lowers the formation energy of octahedral Fe vacancies in Al-rich spinels ($ζ$ = 1/3) from over 3 eV to just 0.62 eV when one third of the cation sites are inverted, allowing high Fe vacancy concentrations under oxidizing conditions. This mechanism supports high H2 yields up to 361 $μ$mol/g, consistent with experimental observations. Our findings support the notion that solar thermochemical water splitting can occur through a cation vacancy mechanism. They also clarify how site inversion, vacancy energetics, and defect interactions each contribute to redox performance, offering general design principles for identifying and optimizing materials that operate through cation vacancy cycling....

---

### 153. Piezoelectric truss metamaterials: data-driven design and additive manufacturing

**Authors:** Saurav Sharma, Satya K. Ammu, Prakash Thakolkaran, Jovana Jovanova, Kunal Masania, Siddhant Kumar

**Published:** 2025-06-13

**Category:** physics.app-ph

**ID:** 2506.22451v2

**Link:** [http://arxiv.org/abs/2506.22451v2](http://arxiv.org/abs/2506.22451v2)

**Summary:** In the development of active animate materials, electromechanical coupling is highly attractive to realize mechanoresponsive functionality. Piezoelectricity is the most utilized electromechanical phenomenon due to the wide availability of materials that display precise and reliable coupling. However, the inherent directionality of these materials is constrained by the symmetry of their crystal structure, which limits the choice of available properties in natural piezoelectric materials. A solution to alleviate this limitation could be to leverage geometry or architecture at the mesoscale. Here, we present an integrated framework to design and 3D-print piezoelectric truss metamaterials with customizable anisotropic responses. To explore the vast design space of truss metamaterials, we employ generative machine learning to optimize the topology and geometry of truss lattices and achieve target piezoelectricity. Then, we develop an in-gel-3D printing method to fabricate polymer-ceramic piezoelectric truss metamaterial structures using a composite slurry of photo-curable resin and lead-free piezoelectric particles. The ML framework discovers designs exhibiting unconventional behaviors, including auxetic, unidirectional, and omnidirectional piezoelectricity, while the additive manufacturing technique ensures shaping freedom and precision in fabricating these metamaterials at small scales. Our results show an improvement of over 48% in the specific hydrostatic piezoelectric coefficient in optimized metamaterials over bulk lead zirconate titanate (PZT). We successfully achieved metamaterials with higher transverse piezoelectric coupling coefficient than its longitudinal coefficient, which is a phenomenon that is rare in bulk materials. Our approach enables customizable piezoelectric responses and paves the way towards the development of a new generation of electro-active animate materials....

---

### 154. Agentic Additive Manufacturing Alloy Discovery

**Authors:** Peter Pak, Achuth Chandrasekhar, Amir Barati Farimani

**Published:** 2025-10-02

**Category:** cs.AI

**ID:** 2510.02567v2

**Link:** [http://arxiv.org/abs/2510.02567v2](http://arxiv.org/abs/2510.02567v2)

**Summary:** Agentic systems enable the intelligent use of research tooling, augmenting a researcher's ability to investigate and propose novel solutions to existing problems. Within Additive Manufacturing (AM), alloy discovery remains a complex challenge, often requiring expertise in the various domains of materials science, thermodynamic simulations, and experimental analysis. Large Language Model (LLM) enabled agents can facilitate this endeavor by utilizing their extensive knowledge base to dispatch tool calls via Model Context Protocol (MCP) to perform actions such as Thermo-Calc property diagram calculations and lack of fusion process map generation. In addition, the multi-agent system developed in this work is able to effectively reason through complex user prompts and provide analysis on the printability of proposed alloys. These agents can dynamically adjust their task trajectory to the outcomes of tool call results, effectively enabling autonomous decision-making in practical environments. This work aims to utilize LLM enabled agents to automate and accelerate the task of alloy discovery within the field of additive manufacturing and showcase the benefits of adopting this multi-agent system....

---

### 155. Atomistic Machine Learning with Cartesian Natural Tensors

**Authors:** Qun Chen, A. S. L. Subrahmanyam Pattamatta, David J. Srolovitz, Mingjian Wen

**Published:** 2025-10-05

**Category:** cond-mat.mtrl-sci

**ID:** 2510.04015v1

**Link:** [http://arxiv.org/abs/2510.04015v1](http://arxiv.org/abs/2510.04015v1)

**Summary:** Atomistic machine learning (ML) is a transformative tool for accurate and efficient investigation of material behavior at the atomic scale. While such models have been constructed within Cartesian space to harness geometric information and preserve intuitive physical representations, they face inherent challenges - primarily due to the lack of a systematic symmetry-preserving framework for representing arbitrary physical tensors. We address these challenges by proposing Cartesian Natural Tensor Networks (CarNet) as a general framework for atomistic ML. We first develop the theory of irreducible representations using Cartesian natural tensors (their creation, operation, as well as the decomposition and reconstruction of physical tensors such as the elastic constant tensor). Leveraging this machinery, we design an equivariant Cartesian model and demonstrate its exceptional performance across diverse atomistic ML tasks. CarNet enables the development of highly accurate and reliable interatomic potentials for both materials and molecular systems. Furthermore, structure-property relationships can be readily constructed for tensorial quantities ranging from simple properties like the dipole moment to arbitrary high-rank tensors with complex symmetries such as the elastic constant tensor -- capabilities that were previously inaccessible. This work removes theoretical barriers and unleashes the power of Cartesian approaches for advanced atomistic ML in the understanding and design of new materials....

---

### 156. Small Language Models for Agentic Systems: A Survey of Architectures, Capabilities, and Deployment Trade offs

**Authors:** Raghav Sharma, Manan Mehta

**Published:** 2025-10-04

**Category:** cs.AI

**ID:** 2510.03847v1

**Link:** [http://arxiv.org/abs/2510.03847v1](http://arxiv.org/abs/2510.03847v1)

**Summary:** Small language models (SLMs; 1-12B params, sometimes up to 20B) are sufficient and often superior for agentic workloads where the objective is schema- and API-constrained accuracy rather than open-ended generation. We synthesize recent evidence across open and proprietary SLMs (Phi-4-Mini, Qwen-2.5-7B, Gemma-2-9B, Llama-3.2-1B/3B, Ministral-3B/8B, Apple on-device 3B, DeepSeek-R1-Distill) and connect it to modern evaluations (BFCL v3/v4, StableToolBench) and serving stacks (vLLM, SGLang, TensorRT-LLM) paired with guided decoding libraries (XGrammar, Outlines). We formalize SLM-default, LLM-fallback systems with uncertainty-aware routing and verifier cascades, and propose engineering metrics that reflect real production goals: cost per successful task (CPS), schema validity rate, executable call rate, p50/p95 latency, and energy per request. Guided decoding, strict JSON Schema outputs, and validator-first tool execution close much of the capability gap with larger models and often let SLMs match or surpass LLMs on tool use, function calling, and RAG at 10x-100x lower token cost with materially better latency and energy. We provide design patterns for agent stacks that prioritize SLMs: schema-first prompting, type-safe function registries, confidence scoring with verifier rollups, and lightweight adaptation via LoRA/QLoRA. We also delineate limits where fallback remains valuable (open-domain reasoning and some long-horizon planning). The result is a practical blueprint for building fast, inexpensive, and reliable agents that default to SLMs while preserving headroom with targeted LLM assistance.
  Keywords: small language models, agents, function calling, structured outputs, JSON Schema, guided decoding, LoRA/QLoRA, routing, energy efficiency, edge inference...

---

### 157. New Directions in Focused Ion Beam Induced Deposition for the Nanoprinting of Functional 3D Heterostructures

**Authors:** Frances Isabel Allen

**Published:** 2025-10-04

**Category:** cond-mat.mtrl-sci

**ID:** 2510.03694v1

**Link:** [http://arxiv.org/abs/2510.03694v1](http://arxiv.org/abs/2510.03694v1)

**Summary:** The focused ion beam (FIB) microscope is well established as a high-resolution machining instrument capable of site-selectively removing material down to the nanoscale. Beyond subtractive processing, however, the FIB can also add material using a technique known as focused ion beam induced deposition (FIBID), enabling the direct-write of complex nanostructures. This work explores new directions in three-dimensional nanoprinting with FIBID, harnessing unique features of helium and neon FIBs to fabricate nanoscale heterostructures, including multimaterial architectures and deposits with engineered internal voids. Detailed insight into the chemical and structural composition of these nanostructures is obtained using advanced electron microscopy, revealing buried interfaces and material transformations. Building on these results, the evolution of FIBID into a versatile platform for functional nanomaterials design is discussed, opening pathways toward next-generation nanoscale devices and technologies....

---

### 158. High-spin magnetic ground states of neutral dopant clusters in semiconductors

**Authors:** Rhine Samajdar, Haonan Zhou, R. N. Bhatt

**Published:** 2025-10-03

**Category:** cond-mat.mes-hall

**ID:** 2510.03575v1

**Link:** [http://arxiv.org/abs/2510.03575v1](http://arxiv.org/abs/2510.03575v1)

**Summary:** High-spin states hold significant promise for classical and quantum information storage and emerging magnetic memory technologies. Here, we present a systematic framework for engineering such high-spin magnetic states in dopant clusters formed from substitutional impurities in semiconductors. In single-valley materials such as gallium arsenide, impurity states are hydrogenic and exchange interactions generally favor low-spin configurations, except in special geometries. In contrast, multivalley semiconductors exhibit oscillatory form factors in their exchange couplings, enabling the controlled suppression of selected hopping processes and exchange couplings. Exploiting this feature, we demonstrate how carefully arranged impurities in aluminum arsenide, germanium, and silicon can stabilize ground states with a net spin that scale extensively with system size. Within effective mass theory and the tight-binding approximation for hopping, we construct explicit examples ranging from finite clusters to extended lattices and fractal-like tilings. In two dimensions, we identify several favorable dopant geometries supporting a net spin equal to around half of the fully polarized value in the thermodynamic limit, including one which achieves over $70\%$ polarization. Our results provide a general design principle for harnessing valley degeneracy in semiconductors to construct robust high-spin states and outline a pathway for their experimental realization via precision implantation of dopants....

---

### 159. Higher-order, generically complete, continuous, and polynomial-time isometry invariants of periodic sets

**Authors:** Daniel E Widdowson, Vitaliy A Kurlin

**Published:** 2025-09-18

**Category:** cs.CG

**ID:** 2509.15088v2

**Link:** [http://arxiv.org/abs/2509.15088v2](http://arxiv.org/abs/2509.15088v2)

**Summary:** Periodic point sets model all solid crystalline materials (crystals) whose atoms can be considered zero-sized points with or without atomic types. This paper addresses the fundamental problem of checking whether claimed crystals are novel, not noisy perturbations of known materials obtained by unrealistic atomic replacements. Such near-duplicates have skewed ground-truth because past comparisons relied on unstable cells and symmetries. The proposed Lipschitz continuity under noise is a new essential requirement for machine learning on any data objects that have ambiguous representations and live in continuous spaces. For periodic point sets under isometry (any distance-preserving transformation), we designed invariants that distinguish all known counter-examples to the completeness of past descriptors and detect thousands of (near-)duplicates in large high-profile databases of crystals within two days on a modest desktop computer....

---

### 160. Riemannian Variational Flow Matching for Material and Protein Design

**Authors:** Olga Zaghen, Floor Eijkelboom, Alison Pouplin, Cong Liu, Max Welling, Jan-Willem van de Meent, Erik J. Bekkers

**Published:** 2025-02-18

**Category:** cs.LG

**ID:** 2502.12981v2

**Link:** [http://arxiv.org/abs/2502.12981v2](http://arxiv.org/abs/2502.12981v2)

**Summary:** We present Riemannian Gaussian Variational Flow Matching (RG-VFM), a geometric extension of Variational Flow Matching (VFM) for generative modeling on manifolds. In Euclidean space, predicting endpoints (VFM), velocities (FM), or noise (diffusion) are largely equivalent due to affine interpolations. On curved manifolds this equivalence breaks down, and we hypothesize that endpoint prediction provides a stronger learning signal by directly minimizing geodesic distances. Building on this insight, we derive a variational flow matching objective based on Riemannian Gaussian distributions, applicable to manifolds with closed-form geodesics. We formally analyze its relationship to Riemannian Flow Matching (RFM), exposing that the RFM objective lacks a curvature-dependent penalty - encoded via Jacobi fields - that is naturally present in RG-VFM. Experiments on synthetic spherical and hyperbolic benchmarks, as well as real-world tasks in material and protein generation, demonstrate that RG-VFM more effectively captures manifold structure and improves downstream performance over Euclidean and velocity-based baselines....

---

### 161. Flatness-Aware Stochastic Gradient Langevin Dynamics

**Authors:** Stefano Bruno, Youngsik Hwang, Jaehyeon An, Sotirios Sabanis, Dong-Young Lim

**Published:** 2025-10-02

**Category:** cs.LG

**ID:** 2510.02174v1

**Link:** [http://arxiv.org/abs/2510.02174v1](http://arxiv.org/abs/2510.02174v1)

**Summary:** Generalization in deep learning is closely tied to the pursuit of flat minima in the loss landscape, yet classical Stochastic Gradient Langevin Dynamics (SGLD) offers no mechanism to bias its dynamics toward such low-curvature solutions. This work introduces Flatness-Aware Stochastic Gradient Langevin Dynamics (fSGLD), designed to efficiently and provably seek flat minima in high-dimensional nonconvex optimization problems. At each iteration, fSGLD uses the stochastic gradient evaluated at parameters perturbed by isotropic Gaussian noise, commonly referred to as Random Weight Perturbation (RWP), thereby optimizing a randomized-smoothing objective that implicitly captures curvature information. Leveraging these properties, we prove that the invariant measure of fSGLD stays close to a stationary measure concentrated on the global minimizers of a loss function regularized by the Hessian trace whenever the inverse temperature and the scale of random weight perturbation are properly coupled. This result provides a rigorous theoretical explanation for the benefits of random weight perturbation. In particular, we establish non-asymptotic convergence guarantees in Wasserstein distance with the best known rate and derive an excess-risk bound for the Hessian-trace regularized objective. Extensive experiments on noisy-label and large-scale vision tasks, in both training-from-scratch and fine-tuning settings, demonstrate that fSGLD achieves superior or comparable generalization and robustness to baseline algorithms while maintaining the computational cost of SGD, about half that of SAM. Hessian-spectrum analysis further confirms that fSGLD converges to significantly flatter minima....

---

### 162. Catalyst GFlowNet for electrocatalyst design: A hydrogen evolution reaction case study

**Authors:** Lena Podina, Christina Humer, Alexandre Duval, Victor Schmidt, Ali Ramlaoui, Shahana Chatterjee, Yoshua Bengio, Alex Hernandez-Garcia, David Rolnick, Félix Therrien

**Published:** 2025-10-02

**Category:** cs.LG

**ID:** 2510.02142v1

**Link:** [http://arxiv.org/abs/2510.02142v1](http://arxiv.org/abs/2510.02142v1)

**Summary:** Efficient and inexpensive energy storage is essential for accelerating the adoption of renewable energy and ensuring a stable supply, despite fluctuations in sources such as wind and solar. Electrocatalysts play a key role in hydrogen energy storage (HES), allowing the energy to be stored as hydrogen. However, the development of affordable and high-performance catalysts for this process remains a significant challenge. We introduce Catalyst GFlowNet, a generative model that leverages machine learning-based predictors of formation and adsorption energy to design crystal surfaces that act as efficient catalysts. We demonstrate the performance of the model through a proof-of-concept application to the hydrogen evolution reaction, a key reaction in HES, for which we successfully identified platinum as the most efficient known catalyst. In future work, we aim to extend this approach to the oxygen evolution reaction, where current optimal catalysts are expensive metal oxides, and open the search space to discover new materials. This generative modeling framework offers a promising pathway for accelerating the search for novel and efficient catalysts....

---

### 163. Zero-shot Human Pose Estimation using Diffusion-based Inverse solvers

**Authors:** Sahil Bhandary Karnoor, Romit Roy Choudhury

**Published:** 2025-10-02

**Category:** cs.CV

**ID:** 2510.02043v1

**Link:** [http://arxiv.org/abs/2510.02043v1](http://arxiv.org/abs/2510.02043v1)

**Summary:** Pose estimation refers to tracking a human's full body posture, including their head, torso, arms, and legs. The problem is challenging in practical settings where the number of body sensors are limited. Past work has shown promising results using conditional diffusion models, where the pose prediction is conditioned on both <location, rotation> measurements from the sensors. Unfortunately, nearly all these approaches generalize poorly across users, primarly because location measurements are highly influenced by the body size of the user. In this paper, we formulate pose estimation as an inverse problem and design an algorithm capable of zero-shot generalization. Our idea utilizes a pre-trained diffusion model and conditions it on rotational measurements alone; the priors from this model are then guided by a likelihood term, derived from the measured locations. Thus, given any user, our proposed InPose method generatively estimates the highly likely sequence of poses that best explains the sparse on-body measurements....

---

### 164. ShapeGen3DCP: A Deep Learning Framework for Layer Shape Prediction in 3D Concrete Printing

**Authors:** Giacomo Rizzieri, Federico Lanteri, Liberato Ferrara, Massimiliano Cremonesi

**Published:** 2025-10-02

**Category:** cs.CE

**ID:** 2510.02009v1

**Link:** [http://arxiv.org/abs/2510.02009v1](http://arxiv.org/abs/2510.02009v1)

**Summary:** This work introduces ShapeGen3DCP, a deep learning framework for fast and accurate prediction of filament cross-sectional geometry in 3D Concrete Printing (3DCP). The method is based on a neural network architecture that takes as input both material properties in the fluid state (density, yield stress, plastic viscosity) and process parameters (nozzle diameter, nozzle height, printing and flow velocities) to directly predict extruded layer shapes. To enhance generalization, some inputs are reformulated into dimensionless parameters that capture underlying physical principles. Predicted geometries are compactly represented using Fourier descriptors, which enforce smooth, closed, and symmetric profiles while reducing the prediction task to a small set of coefficients. The training dataset was synthetically generated using a well-established Particle Finite Element (PFEM) model of 3DCP, overcoming the scarcity of experimental data. Validation against diverse numerical and experimental cases shows strong agreement, confirming the framework's accuracy and reliability. This opens the way to practical uses ranging from pre-calibration of print settings, minimizing or even eliminating trial-and-error adjustments, to toolpath optimization for more advanced designs. Looking ahead, coupling the framework with simulations and sensor feedback could enable closed-loop digital twins for 3DCP, driving real-time process optimization, defect detection, and adaptive control of printing parameters....

---

### 165. 3-dimensional plasmonic nanomotors enabled by independent integration of Optical Pulling and Lateral Forces

**Authors:** Guillermo Serrera, Yoshito Y. Tanaka, Pablo Albella

**Published:** 2025-06-20

**Category:** physics.optics

**ID:** 2506.16811v2

**Link:** [http://arxiv.org/abs/2506.16811v2](http://arxiv.org/abs/2506.16811v2)

**Summary:** Light-matter interactions generally involve momentum exchange between incident photons and the target object giving rise to optical forces and torques. While typically weak, they become significant at the nanoscale, driving intense research interest in the exploitation of photon recoil to drive micro- and nanostructures. While great progress has been attained in controlling transversal degrees of freedom, three-dimensional movement remains challenging, particularly due to the impractical realization of pulling forces that oppose the direction of incident light. Here we theoretically present a novel nanomotor design that enables independent control over both transverse and longitudinal motion. This design exploits coupling between an azimuthally polarized Bessel beam and a dielectric glass cylinder to realistically achieve optical pulling forces. At the same time, asymmetric plasmonic dimers, embedded within the cylinder, provide lateral motion, through asymmetric scattering under plane wave illumination. We further demonstrate that unwanted displacements and rotations can be restrained, even at long illumination times. Our design unlocks a new degree of freedom in motion control, allowing for pulling, pushing, and lateral movement by simply tuning the polarization or switching between plane waves and Bessel beams....

---

### 166. Rethinking the shape convention of an MLP

**Authors:** Meng-Hsi Chen, Yu-Ang Lee, Feng-Ting Liao, Da-shan Shiu

**Published:** 2025-10-02

**Category:** cs.LG

**ID:** 2510.01796v1

**Link:** [http://arxiv.org/abs/2510.01796v1](http://arxiv.org/abs/2510.01796v1)

**Summary:** Multi-layer perceptrons (MLPs) conventionally follow a narrow-wide-narrow design where skip connections operate at the input/output dimensions while processing occurs in expanded hidden spaces. We challenge this convention by proposing wide-narrow-wide (Hourglass) MLP blocks where skip connections operate at expanded dimensions while residual computation flows through narrow bottlenecks. This inversion leverages higher-dimensional spaces for incremental refinement while maintaining computational efficiency through parameter-matched designs. Implementing Hourglass MLPs requires an initial projection to lift input signals to expanded dimensions. We propose that this projection can remain fixed at random initialization throughout training, enabling efficient training and inference implementations. We evaluate both architectures on generative tasks over popular image datasets, characterizing performance-parameter Pareto frontiers through systematic architectural search. Results show that Hourglass architectures consistently achieve superior Pareto frontiers compared to conventional designs. As parameter budgets increase, optimal Hourglass configurations favor deeper networks with wider skip connections and narrower bottlenecks-a scaling pattern distinct from conventional MLPs. Our findings suggest reconsidering skip connection placement in modern architectures, with potential applications extending to Transformers and other residual networks....

---

### 167. Giant enhancement of terahertz high-harmonic generation by cavity engineering of Dirac semimetal

**Authors:** Siyu Duan, Lili Shi, Patrick Pilch, Anneke Reinold, Sergey Kovalev, Renato M. A. Dantas, Yunkun Yang, Faxian Xiu, Miriam Serena Vitiello, Zhe Wang

**Published:** 2025-10-02

**Category:** cond-mat.mtrl-sci

**ID:** 2510.01760v1

**Link:** [http://arxiv.org/abs/2510.01760v1](http://arxiv.org/abs/2510.01760v1)

**Summary:** Engineered micro- or nano-structures based on nonlinear optical materials offer versatile opportunities for optoelectronic applications. While extensive efforts have been devoted to design tailored microcavities to promote and increase the optical nonlinearities of graphene, the potential of engineering its three-dimensional counterparts -- three-dimensional Dirac semimetals -- remains largely unexplored. Here we report on exceptionally strong terahertz nonlinearities in a cavity-engineered Dirac semimetal microstructure, and demonstrate a giant enhancement of terahertz third- and fifth-order harmonic yields by more than three orders of magnitude. By fabricating a designed structure of metallic metasurface microcavities on a nanometer thin film of the threedimensional Dirac semimetal Cd3As2, we significantly enhance the near-field intensity of a picosecond terahertz excitation pulse in resonance with the microcavity eigenmode. This transiently modifies the nonlinearities of the thin film and drives the nonlinear responses of the Dirac fermions from a weakly to a deeply nonperturbative regime where the observed high-harmonic generation essentially saturates....

---

### 168. Discontinuous Epitope Fragments as Sufficient Target Templates for Efficient Binder Design

**Authors:** Zhenfeng Deng, Ruijie Hou, Ningrui Xie, Mike Tyers, Michał Koziarski

**Published:** 2025-09-29

**Category:** q-bio.BM

**ID:** 2509.25479v2

**Link:** [http://arxiv.org/abs/2509.25479v2](http://arxiv.org/abs/2509.25479v2)

**Summary:** Recent advances in structure-based protein design have accelerated de novo binder generation, yet interfaces on large domains or spanning multiple domains remain challenging due to high computational cost and declining success with increasing target size. We hypothesized that protein folding neural networks (PFNNs) operate in a ``local-first'' manner, prioritizing local interactions while displaying limited sensitivity to global foldability. Guided by this hypothesis, we propose an epitope-only strategy that retains only the discontinuous surface residues surrounding the binding site. Compared to intact-domain workflows, this approach improves in silico success rates by up to 80% and reduces the average time per successful design by up to forty-fold, enabling binder design against previously intractable targets such as ClpP and ALS3. Building on this foundation, we further developed a tailored pipeline that incorporates a Monte Carlo-based evolution step to overcome local minima and a position-specific biased inverse folding step to refine sequence patterns. Together, these advances not only establish a generalizable framework for efficient binder design against structurally large and otherwise inaccessible targets, but also support the broader ``local-first'' hypothesis as a guiding principle for PFNN-based design....

---

### 169. RheOFormer: A generative transformer model for simulation of complex fluids and flows

**Authors:** Maedeh Saberi, Amir Barati Farimani, Safa Jamali

**Published:** 2025-10-01

**Category:** cs.LG

**ID:** 2510.01365v1

**Link:** [http://arxiv.org/abs/2510.01365v1](http://arxiv.org/abs/2510.01365v1)

**Summary:** The ability to model mechanics of soft materials under flowing conditions is key in designing and engineering processes and materials with targeted properties. This generally requires solution of internal stress tensor, related to the deformation tensor through nonlinear and history-dependent constitutive models. Traditional numerical methods for non-Newtonian fluid dynamics often suffer from prohibitive computational demands and poor scalability to new problem instances. Developments in data-driven methods have mitigated some limitations but still require retraining across varied physical conditions. In this work, we introduce Rheological Operator Transformer (RheOFormer), a generative operator learning method leveraging self-attention to efficiently learn different spatial interactions and features of complex fluid flows. We benchmark RheOFormer across a range of different viscometric and non-viscometric flows with different types of viscoelastic and elastoviscoplastic mechanics in complex domains against ground truth solutions. Our results demonstrate that RheOFormer can accurately learn both scalar and tensorial nonlinear mechanics of different complex fluids and predict the spatio-temporal evolution of their flows, even when trained on limited datasets. Its strong generalization capabilities and computational efficiency establish RheOFormer as a robust neural surrogate for accelerating predictive complex fluid simulations, advancing data-driven experimentation, and enabling real-time process optimization across a wide range of applications....

---

### 170. Dislocation Transmission Across Tilt Low-Angle Grain Boundaries in BCC Fe: The Role of Elastic Interactions

**Authors:** Shuai Zhang, Zhishun Chen, Zhuoming Xie, Jun Song, Huiqiu Deng, Wangyu Hu, Jie Hou

**Published:** 2025-09-09

**Category:** cond-mat.mtrl-sci

**ID:** 2509.07787v2

**Link:** [http://arxiv.org/abs/2509.07787v2](http://arxiv.org/abs/2509.07787v2)

**Summary:** Low-angle grain boundaries (LAGBs) are often regarded as penetrable interfaces to dislocation motion, yet recent studies suggest they can also act as strong barriers. The origin of this duality remains debated, particularly regarding the role of elastic interactions. Here, large-scale molecular dynamics simulations are employed to investigate dislocation transmission across various tilt LAGBs in BCC Fe. The results show that transmission resistance varies widely with boundary-dislocation geometry. Contrary to the prevailing view that dislocation reactions dominate, elastic interactions between lattice and boundary dislocations emerge as the primary controlling factor. Screw and screw-like dislocations generate shear stresses that bend GB dislocations and produce strong barriers, whereas edge dislocations lack such stresses and transmit more readily. Consequently, barrier strength increases as the dislocation character angle decreases, with screw dislocations experiencing the strongest resistance. From these insights, we develop an analytical model that quantitatively links net transmission stress to dislocation character, boundary inclination, and boundary misorientation, reproducing the simulation results with excellent agreement. These results establish the dominant role of elastic interactions in dislocation-LAGB interactions and provide a predictive basis for designing materials strengthened by controlled boundary architectures....

---

### 171. UniverSR: Unified and Versatile Audio Super-Resolution via Vocoder-Free Flow Matching

**Authors:** Woongjib Choi, Sangmin Lee, Hyungseob Lim, Hong-Goo Kang

**Published:** 2025-10-01

**Category:** eess.AS

**ID:** 2510.00771v1

**Link:** [http://arxiv.org/abs/2510.00771v1](http://arxiv.org/abs/2510.00771v1)

**Summary:** In this paper, we present a vocoder-free framework for audio super-resolution that employs a flow matching generative model to capture the conditional distribution of complex-valued spectral coefficients. Unlike conventional two-stage diffusion-based approaches that predict a mel-spectrogram and then rely on a pre-trained neural vocoder to synthesize waveforms, our method directly reconstructs waveforms via the inverse Short-Time Fourier Transform (iSTFT), thereby eliminating the dependence on a separate vocoder. This design not only simplifies end-to-end optimization but also overcomes a critical bottleneck of two-stage pipelines, where the final audio quality is fundamentally constrained by vocoder performance. Experiments show that our model consistently produces high-fidelity 48 kHz audio across diverse upsampling factors, achieving state-of-the-art performance on both speech and general audio datasets....

---

### 172. RoVerFly: Robust and Versatile Implicit Hybrid Control of Quadrotor-Payload Systems

**Authors:** Mintae Kim, Jiaze Cai, Koushil Sreenath

**Published:** 2025-09-14

**Category:** cs.RO

**ID:** 2509.11149v2

**Link:** [http://arxiv.org/abs/2509.11149v2](http://arxiv.org/abs/2509.11149v2)

**Summary:** Designing robust controllers for precise trajectory tracking with quadrotors is challenging due to nonlinear dynamics and underactuation, and becomes harder with flexible cable-suspended payloads that add degrees of freedom and hybrid dynamics. Classical model-based methods offer stability guarantees but require extensive tuning and often fail to adapt when the configuration changes-when a payload is added or removed, or when its mass or cable length varies. We present RoVerFly, a unified learning-based control framework where a single reinforcement learning (RL) policy functions as an implicit hybrid controller, managing complex dynamics without explicit mode detection or controller switching. Trained with task and domain randomization, the controller is resilient to disturbances and varying dynamics. It achieves strong zero-shot generalization across payload settings-including no payload as well as varying mass and cable length-without re-tuning, while retaining the interpretability and structure of a feedback tracking controller. Code and supplementary materials are available at https://github.com/mintaeshkim/roverfly....

---

### 173. Three-fold Superstructured Superlattice HfN/HfAlN Thin Films for Enhanced Toughness

**Authors:** M. Lorentzon, R. Hahn, J. Palisaitis, H. Riedl, L. Hultman, J. Birch, N. Ghafoor

**Published:** 2025-10-01

**Category:** cond-mat.mtrl-sci

**ID:** 2510.00716v1

**Link:** [http://arxiv.org/abs/2510.00716v1](http://arxiv.org/abs/2510.00716v1)

**Summary:** To simultaneously achieve high hardness and high toughness in protective coatings remains a fundamental challenge. Here, we harness the superlattice architecture to combine Koehler hardening while the coherent interfaces reduce the crack driving force and improve toughness, enabling coatings that are both hard and damage tolerant. We design and fabricate epitaxial HfN$_{1.33}$/Hf$_{0.76}$Al$_{0.24}$N$_{1.15}$ superlattices, deposited on MgO(001) substrates using low-energy, high-flux ion-assisted reactive magnetron sputtering. These superlattices with bilayer periods ranging from 6 to 20 nm, exhibit a unique three-fold superstructure, confirmed by X-ray diffraction and reciprocal space mapping (RSM). Each constituent forms distinct 3D checkerboard superstructures, with a period of 7.5 Å for HfN and 12.5 A for HfAlN. RSMs further reveal low mosaicity, high crystalline quality, and in-plane compressive strains, indicating well preserved coherence across interfaces. Mechanical testing shows that the superlattices maintain the high hardness of HfAlN (\~36 GPa) independent of bilayer period, while surpassing the softer HfN (~27 GPa), consistent with interface-driven Koehler strengthening. Micropillar compression shows brittle fracture on the {110}<110> system, yet with distributed cracking and faster mechanical recovery compared to monolithic films, suggesting improved toughness. Cube-corner indentation further corroborate this behavior, with pile-up and suppressed fracture events. These results demonstrate that epitaxial HfN/HfAlN superlattices uniquely combine high hardness with improved toughness, enabled by their three-fold superstructured architecture. Leveraging the intrinsic high-temperature stability of HfN-based materials, this design offers a robust pathway toward next-generation protective coatings capable of maintaining performance under extreme conditions....

---

### 174. Copy-Paste to Mitigate Large Language Model Hallucinations

**Authors:** Yongchao Long, Xian Wu, Yingying Zhang, Xianbin Wen, Yuxi Zhou, Shenda Hong

**Published:** 2025-10-01

**Category:** cs.CL

**ID:** 2510.00508v1

**Link:** [http://arxiv.org/abs/2510.00508v1](http://arxiv.org/abs/2510.00508v1)

**Summary:** While Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to generate contextually grounded responses, contextual faithfulness remains challenging as LLMs may not consistently trust provided context, leading to hallucinations that undermine reliability. We observe an inverse correlation between response copying degree and context-unfaithful hallucinations on RAGTruth, suggesting that higher copying degrees reduce hallucinations by fostering genuine contextual belief. We propose CopyPasteLLM, obtained through two-stage high-copying response preference training. We design three prompting methods to enhance copying degree, demonstrating that high-copying responses achieve superior contextual faithfulness and hallucination control. These approaches enable a fully automated pipeline that transforms generated responses into high-copying preference data for training CopyPasteLLM. On FaithEval, ConFiQA and PubMedQA, CopyPasteLLM achieves best performance in both counterfactual and original contexts, remarkably with 12.2% to 24.5% accuracy improvements on FaithEval over the best baseline, while requiring only 365 training samples -- 1/50th of baseline data. To elucidate CopyPasteLLM's effectiveness, we propose the Context-Parameter Copying Capturing algorithm. Interestingly, this reveals that CopyPasteLLM recalibrates reliance on internal parametric knowledge rather than external knowledge during generation. All codes are available at https://github.com/longyongchao/CopyPasteLLM...

---

### 175. OBELiX: A Curated Dataset of Crystal Structures and Experimentally Measured Ionic Conductivities for Lithium Solid-State Electrolytes

**Authors:** Félix Therrien, Jamal Abou Haibeh, Divya Sharma, Rhiannon Hendley, Leah Wairimu Mungai, Sun Sun, Alain Tchagang, Jiang Su, Samuel Huberman, Yoshua Bengio, Hongyu Guo, Alex Hernández-García, Homin Shin

**Published:** 2025-02-20

**Category:** cond-mat.mtrl-sci

**ID:** 2502.14234v2

**Link:** [http://arxiv.org/abs/2502.14234v2](http://arxiv.org/abs/2502.14234v2)

**Summary:** Solid-state electrolyte batteries are expected to replace liquid electrolyte lithium-ion batteries in the near future thanks to their higher theoretical energy density and improved safety. However, their adoption is currently hindered by their lower effective ionic conductivity, a quantity that governs charge and discharge rates. Identifying highly ion-conductive materials using conventional theoretical calculations and experimental validation is both time-consuming and resource-intensive. While machine learning holds the promise to expedite this process, relevant ionic conductivity and structural data is scarce. Here, we present OBELiX, a database of $\sim$600 synthesized solid electrolyte materials and their experimentally measured room temperature ionic conductivities gathered from literature and curated by domain experts. Each material is described by their measured composition, space group and lattice parameters. A full-crystal description in the form of a crystallographic information file (CIF) is provided for $\sim$320 structures for which atomic positions were available. We discuss various statistics and features of the dataset and provide training and testing splits carefully designed to avoid data leakage. Finally, we benchmark seven existing ML models on the task of predicting ionic conductivity and discuss their performance. The goal of this work is to facilitate the use of machine learning for solid-state electrolyte materials discovery....

---

### 176. Reward driven discovery of the optimal microstructure representations with invariant variational autoencoders

**Authors:** Boris N. Slautin, Kamyar Barakati, Hiroshi Funakubo, Maxim A. Ziatdinov, Vladimir V. Shvartsman, Doru C. Lupascu, Sergei V. Kalinin

**Published:** 2025-09-30

**Category:** cs.LG

**ID:** 2510.00243v1

**Link:** [http://arxiv.org/abs/2510.00243v1](http://arxiv.org/abs/2510.00243v1)

**Summary:** Microscopy techniques generate vast amounts of complex image data that in principle can be used to discover simpler, interpretable, and parsimonious forms to reveal the underlying physical structures, such as elementary building blocks in molecular systems or order parameters and phases in crystalline materials. Variational Autoencoders (VAEs) provide a powerful means of constructing such low-dimensional representations, but their performance heavily depends on multiple non-myopic design choices, which are often optimized through trial-and-error and empirical analysis. To enable automated and unbiased optimization of VAE workflows, we investigated reward-based strategies for evaluating latent space representations. Using Piezoresponse Force Microscopy data as a model system, we examined multiple policies and reward functions that can serve as a foundation for automated optimization. Our analysis shows that approximating the latent space with Gaussian Mixture Models (GMM) and Bayesian Gaussian Mixture Models (BGMM) provides a strong basis for constructing reward functions capable of estimating model efficiency and guiding the search for optimal parsimonious representations....

---

### 177. Strain-Gradient-Driven Decoupling of Thermal Suppression from Anisotropy in \b{eta}-Ga2O3

**Authors:** Guangwu Zhang, Xing Xiang, Ziyan Qian, Yixin Xu, Shengying Yue, Hyejin Jang, Lin Yang, Yanguang Zhou, Xinyu Wang, Qiye Zheng

**Published:** 2025-09-30

**Category:** cond-mat.mtrl-sci

**ID:** 2509.26412v1

**Link:** [http://arxiv.org/abs/2509.26412v1](http://arxiv.org/abs/2509.26412v1)

**Summary:** Strain gradients, ubiquitous in flexible devices and epitaxial nanostructures, are a major blind spot for thermal transport in \b{eta}-Ga2O3. We establish that strain gradient unlocks a thermal conductivity (k) suppression mechanism fundamentally more potent than uniform strain: moderate uniaxial gradients (0.6%/nm) suppress k by 32-37% (27-30%) in thin films (nanowires), intensifying to 43.3% with biaxial gradients. This reduction far exceeds that from equivalent uniform strain and surpasses benchmark materials like silicon and BAs. Critically, a surprising decoupling emerges: while 3% uniform strain alters thermal anisotropy by ~25%, strain gradient strongly suppresses k with preserving this ratio. Mechanistically, strain gradients-induced symmetry breaking and enhanced mode coupling anisotropically activate forbidden scattering channels, making gradient-driven scattering dominant over intrinsic phonon scattering below 6.25 THz. These findings redefine non-uniform strain from a parasitic flaw into a powerful design tool for engineering thermal isolation and heat flux in next-generation flexible and high-power \b{eta}-Ga2O3 electronics....

---

### 178. LLM Agents for Knowledge Discovery in Atomic Layer Processing

**Authors:** Andreas Werbrouck, Marshall B. Lindsay, Matthew Maschmann, Matthias J. Young

**Published:** 2025-09-30

**Category:** cs.AI

**ID:** 2509.26201v1

**Link:** [http://arxiv.org/abs/2509.26201v1](http://arxiv.org/abs/2509.26201v1)

**Summary:** Large Language Models (LLMs) have garnered significant attention for several years now. Recently, their use as independently reasoning agents has been proposed. In this work, we test the potential of such agents for knowledge discovery in materials science. We repurpose LangGraph's tool functionality to supply agents with a black box function to interrogate. In contrast to process optimization or performing specific, user-defined tasks, knowledge discovery consists of freely exploring the system, posing and verifying statements about the behavior of this black box, with the sole objective of generating and verifying generalizable statements. We provide proof of concept for this approach through a children's parlor game, demonstrating the role of trial-and-error and persistence in knowledge discovery, and the strong path-dependence of results. We then apply the same strategy to show that LLM agents can explore, discover, and exploit diverse chemical interactions in an advanced Atomic Layer Processing reactor simulation using intentionally limited probe capabilities without explicit instructions....

---

### 179. Accelerated Discovery of High-\k{appa} Oxides with Physics-Based Factorized Machine Learning

**Authors:** Atsushi Takigawa, Shin Kiyohara, Yu Kumagai

**Published:** 2025-09-30

**Category:** cond-mat.mtrl-sci

**ID:** 2509.26022v1

**Link:** [http://arxiv.org/abs/2509.26022v1](http://arxiv.org/abs/2509.26022v1)

**Summary:** Considerable effort continues to be devoted to the exploration of next-generation high-\k{appa} materials that combine a high dielectric constant with a wide band gap. However, machine learning (ML)-based virtual screening has remained challenging, primarily due to the low accuracy in predicting the ionic contribution to the dielectric tensor, which dominates the dielectric performance of high-\k{appa} materials. We here propose a joint ML model that predicts Born effective charges using an equivariant graph neural network, and phonon properties using a highly accurate pretrained ML potential. The ionic dielectric tensor is then computed analytically from these quantities. This approach significantly improves the accuracy of ionic contribution. Using the proposed model, we successfully identified 38 novel high-\k{appa} oxides from a screening pool of over 8,000 candidates....

---

### 180. Molecular augmented dynamics: Generating experimentally consistent atomistic structures by design

**Authors:** Tigany Zarrouk, Miguel A. Caro

**Published:** 2025-08-23

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17132v2

**Link:** [http://arxiv.org/abs/2508.17132v2](http://arxiv.org/abs/2508.17132v2)

**Summary:** A fundamental objective of materials modeling is identifying atomic structures that align with experimental observables. Conventional approaches for disordered materials involve sampling from thermodynamic ensembles and hoping for an experimental match. This process is inefficient and offers no guarantee of success. We present a method based on modified molecular dynamics, that we call molecular augmented dynamics (MAD), which identifies structures that simultaneously match multiple experimental observables and exhibit low energies as described by a machine learning interatomic potential (MLP) trained from ab-initio data. We demonstrate its feasibility by finding representative structures of glassy carbon, nanoporous carbon, ta-C, a-C:D and a-CO$_x$ that match their respective experimental observables -- X-ray diffraction, neutron diffraction, pair distribution function and X-ray photoelectron spectroscopy data -- using the same initial structure and underlying MLP. The method is general, accepting any experimental observable whose simulated counterpart can be cast as a function of differentiable atomic descriptors. This method enables a computational "microscope" into experimental structures....

---

### 181. Fabrication of hydrogen-bonded metal inorganic-organic complex glasses by ligand-tuning approach

**Authors:** Tianzhao Xu, Zhencai Li, Jia-Xin Wu, Zihao Wang, Hanmeng Zhang, Huotian Zhang, Lars R. Jensen, Kenji Shinozaki, Feng Gao, Haomiao Zhu, Ivan Hung, Zhehong Gan, Jinjun Ren, Zheng Yin, Ming-Hua Zeng, Yuanzheng Yue

**Published:** 2025-09-29

**Category:** cond-mat.mtrl-sci

**ID:** 2509.24755v1

**Link:** [http://arxiv.org/abs/2509.24755v1](http://arxiv.org/abs/2509.24755v1)

**Summary:** Metal inorganic-organic complex (MIOC) crystals are a new category of hybrid glass formers. However, the glass-forming compositions of MIOC crystals are limited due to lack of both a general design principle for such compositions and a deep understanding of the structure and formation mechanism for MIOC glasses. This work reports a general approach for synthesizing glass-forming MIOC crystals. In detail, the principle of this approach is based on the creation of hydrogen-bonded structural network by substituting acid anions for imidazole or benzimidazole ligands in the tetrahedral units of zeolitic imidazolate framework crystals. By tuning the metal centers, anions, and organic ligands of MIOCs, supramolecular unit structures can be designed to construct supramolecular networks and thereby enable property modulation. Furthermore, mixed-ligand synthesis yielded a mixed-crystal system in which the glass-transition temperature (Tg) can be linearly tuned from 282 K to 360 K through gradual substitution of benzimidazole for imidazole. Interestingly, upon vitrification, MIOCs were observed to undergo reorganization of hydrogen-bonded networks, with retention of tetrahedral units, short-range disorder, and the freezing of multiple conformations. This work offers a new strategy to systematically expand the glass-forming compositional range of MIOCs and to develop functional MIOC glasses....

---

### 182. SAIP: A Plug-and-Play Scale-adaptive Module in Diffusion-based Inverse Problems

**Authors:** Lingyu Wang, Xiangming Meng

**Published:** 2025-09-29

**Category:** cs.LG

**ID:** 2509.24580v1

**Link:** [http://arxiv.org/abs/2509.24580v1](http://arxiv.org/abs/2509.24580v1)

**Summary:** Solving inverse problems with diffusion models has shown promise in tasks such as image restoration. A common approach is to formulate the problem in a Bayesian framework and sample from the posterior by combining the prior score with the likelihood score. Since the likelihood term is often intractable, estimators like DPS, DMPS, and $π$GDM are widely adopted. However, these methods rely on a fixed, manually tuned scale to balance prior and likelihood contributions. Such a static design is suboptimal, as the ideal balance varies across timesteps and tasks, limiting performance and generalization. To address this issue, we propose SAIP, a plug-and-play module that adaptively refines the scale at each timestep without retraining or altering the diffusion backbone. SAIP integrates seamlessly into existing samplers and consistently improves reconstruction quality across diverse image restoration tasks, including challenging scenarios....

---

### 183. The role of the solid-melt interface in accelerating the self-catalyzed growth kinetics of III-V semiconductors

**Authors:** Zhucong Xi, Abby Liu, Xiaobo Chen, Meng Li, Dmitri N. Zakharov, Judith C. Yang, Rachel S. Goldman, Liang Qi

**Published:** 2025-09-29

**Category:** cond-mat.mtrl-sci

**ID:** 2509.24206v1

**Link:** [http://arxiv.org/abs/2509.24206v1](http://arxiv.org/abs/2509.24206v1)

**Summary:** Solid-melt interfaces play a pivotal role in governing crystal growth and metal-mediated epitaxy of gallium nitride (GaN) and other semiconductor materials. Using atomistic simulations based on machine-learning interatomic potentials (MLIPs), we uncover that multiple layers of Ga atoms at the GaN-Ga melt interface form structurally ordered and electronically charged configurations that are critical for the growth kinetics of GaN. These ordered layers modulate the free energy landscape (FEL) for N adsorption and substantially reduce the migration barriers for N at the interface compared to a clean GaN surface. Leveraging these interfacial energetics, kinetic Monte Carlo (KMC) simulations reveal that GaN growth follows a diffusion-controlled, layer-by-layer mechanism, with the FEL for N adsorption emerging as the rate-limiting factor. By incorporating facet-specific FELs and the diffusivity/solubility of N in Ga melt, we develop a predictive, fitting-free transport model that estimates facet-dependent growth rates in the range of ~0.01 to 0.04 nm/s, in agreement with experimental growth rates observed in GaN nanoparticles synthesized by Ga-mediated molecular beam epitaxy (MBE). This multiscale framework offers a generalizable and quantitative approach to link atomic-scale ordering and interfacial energetics to macroscopic phenomena, providing actionable insights for the rational design of metal-mediated epitaxial processes....

---

### 184. Composable Score-based Graph Diffusion Model for Multi-Conditional Molecular Generation

**Authors:** Anjie Qiao, Zhen Wang, Chuan Chen, DeFu Lian, Enhong Chen

**Published:** 2025-09-11

**Category:** cs.LG

**ID:** 2509.09451v2

**Link:** [http://arxiv.org/abs/2509.09451v2](http://arxiv.org/abs/2509.09451v2)

**Summary:** Controllable molecular graph generation is essential for material and drug discovery, where generated molecules must satisfy diverse property constraints. While recent advances in graph diffusion models have improved generation quality, their effectiveness in multi-conditional settings remains limited due to reliance on joint conditioning or continuous relaxations that compromise fidelity. To address these limitations, we propose Composable Score-based Graph Diffusion model (CSGD), the first model that extends score matching to discrete graphs via concrete scores, enabling flexible and principled manipulation of conditional guidance. Building on this foundation, we introduce two score-based techniques: Composable Guidance (CoG), which allows fine-grained control over arbitrary subsets of conditions during sampling, and Probability Calibration (PC), which adjusts estimated transition probabilities to mitigate train-test mismatches. Empirical results on four molecular datasets show that CSGD achieves state-of-the-art performance, with a 15.3% average improvement in controllability over prior methods, while maintaining high validity and distributional fidelity. Our findings highlight the practical advantages of score-based modeling for discrete graph generation and its capacity for flexible, multi-property molecular design....

---

### 185. Performance of Machine Learning Methods for Gravity Inversion: Successes and Challenges

**Authors:** Vahid Negahdari, Shirin Samadi Bahrami, Seyed Reza Moghadasi, Mohammad Reza Razvan

**Published:** 2025-09-28

**Category:** physics.geo-ph

**ID:** 2510.09632v1

**Link:** [http://arxiv.org/abs/2510.09632v1](http://arxiv.org/abs/2510.09632v1)

**Summary:** Gravity inversion is the problem of estimating subsurface density distributions from observed gravitational field data. We consider the two-dimensional (2D) case, in which recovering density models from one-dimensional (1D) measurements leads to an underdetermined system with substantially more model parameters than measurements, making the inversion ill-posed and non-unique. Recent advances in machine learning have motivated data-driven approaches for gravity inversion. We first design a convolutional neural network (CNN) trained to directly map gravity anomalies to density fields, where a customized data structure is introduced to enhance the inversion performance. To further investigate generative modeling, we employ Variational Autoencoders (VAEs) and Generative Adversarial Networks (GANs), reformulating inversion as a latent-space optimization constrained by the forward operator. In addition, we assess whether classical iterative solvers such as Gradient Descent (GD), GMRES, LGMRES, and a recently proposed Improved Conjugate Gradient (ICG) method can refine CNN-based initial guesses and improve inversion accuracy. Our results demonstrate that CNN inversion not only provides the most reliable reconstructions but also significantly outperforms previously reported methods. Generative models remain promising but unstable, and iterative solvers offer only marginal improvements, underscoring the persistent ill-posedness of gravity inversion....

---

### 186. Reinforcement Learning-Based Prompt Template Stealing for Text-to-Image Models

**Authors:** Xiaotian Zou

**Published:** 2025-09-27

**Category:** cs.CV

**ID:** 2510.00046v1

**Link:** [http://arxiv.org/abs/2510.00046v1](http://arxiv.org/abs/2510.00046v1)

**Summary:** Multimodal Large Language Models (MLLMs) have transformed text-to-image workflows, allowing designers to create novel visual concepts with unprecedented speed. This progress has given rise to a thriving prompt trading market, where curated prompts that induce trademark styles are bought and sold. Although commercially attractive, prompt trading also introduces a largely unexamined security risk: the prompts themselves can be stolen.
  In this paper, we expose this vulnerability and present RLStealer, a reinforcement learning based prompt inversion framework that recovers its template from only a small set of example images. RLStealer treats template stealing as a sequential decision making problem and employs multiple similarity based feedback signals as reward functions to effectively explore the prompt space. Comprehensive experiments on publicly available benchmarks demonstrate that RLStealer gets state-of-the-art performance while reducing the total attack cost to under 13% of that required by existing baselines. Our further analysis confirms that RLStealer can effectively generalize across different image styles to efficiently steal unseen prompt templates. Our study highlights an urgent security threat inherent in prompt trading and lays the groundwork for developing protective standards in the emerging MLLMs marketplace....

---

### 187. How to Make Large Language Models Generate 100% Valid Molecules?

**Authors:** Wen Tao, Jing Tang, Alvin Chan, Bryan Hooi, Baolong Bi, Nanyun Peng, Yuansheng Liu, Yiwei Wang

**Published:** 2025-09-27

**Category:** cs.CL

**ID:** 2509.23099v1

**Link:** [http://arxiv.org/abs/2509.23099v1](http://arxiv.org/abs/2509.23099v1)

**Summary:** Molecule generation is key to drug discovery and materials science, enabling the design of novel compounds with specific properties. Large language models (LLMs) can learn to perform a wide range of tasks from just a few examples. However, generating valid molecules using representations like SMILES is challenging for LLMs in few-shot settings. In this work, we explore how LLMs can generate 100% valid molecules. We evaluate whether LLMs can use SELFIES, a representation where every string corresponds to a valid molecule, for valid molecule generation but find that LLMs perform worse with SELFIES than with SMILES. We then examine LLMs' ability to correct invalid SMILES and find their capacity limited. Finally, we introduce SmiSelf, a cross-chemical language framework for invalid SMILES correction. SmiSelf converts invalid SMILES to SELFIES using grammatical rules, leveraging SELFIES' mechanisms to correct the invalid SMILES. Experiments show that SmiSelf ensures 100% validity while preserving molecular characteristics and maintaining or even enhancing performance on other metrics. SmiSelf helps expand LLMs' practical applications in biomedicine and is compatible with all SMILES-based generative models. Code is available at https://github.com/wentao228/SmiSelf....

---

### 188. Beyond Seamless: Unexpected Defective Merging in Single-Orientation Graphene

**Authors:** Zhien Wang, Jiangtao Wang, Diego Exposito, Andrey Krayev, Shih-Ming He, Xudong Zheng, Zachariah Hennighausen, Ivan Brihuega, Se-Young Jeong, Jing Kong

**Published:** 2025-09-26

**Category:** cond-mat.mtrl-sci

**ID:** 2509.21908v1

**Link:** [http://arxiv.org/abs/2509.21908v1](http://arxiv.org/abs/2509.21908v1)

**Summary:** Single-orientation stitching of graphene has emerged as the predominant method for growth of large-area, high-quality graphene films. Particularly noteworthy is graphene grown on single-crystalline Cu(111)/sapphire substrates, which exhibits exceptionally planar oriented stitching due to the atomically smooth substrate, facilitating the formation of continuous, high-quality graphene monolayer. These single-orientation stitches have conventionally been regarded as seamless with negligible defect concentrations. In this report, we present experimental observations regarding graphene grown on single-crystalline Cu(111)/sapphire substrates. Among the graphene flakes with single-orientation, our findings reveal two major merging behaviors: one producing the expected seamless stitching, and another unexpectedly generating structural defects that create nanoscale pathways permitting water permeation. Notably, we identify a unique merging structure--overlapped junction, in which the edge of one graphene flake overlaps and lies atop the edge of another flake, rather than forming a continuous atomic stitch. This discovery challenges the conventional anticipation of single-orientation stitched graphene films as seamless single crystalline film, while offers unique perspective for graphene applications in molecular sieving, selective filtration membranes, and protective coatings....

---

### 189. Direct Deoxygenation of Phenol over Fe-based Bimetallic Surfaces using On-the-fly Surrogate Models

**Authors:** Isaac Onyango, Qiang Zhu

**Published:** 2025-09-25

**Category:** cond-mat.mtrl-sci

**ID:** 2509.21678v1

**Link:** [http://arxiv.org/abs/2509.21678v1](http://arxiv.org/abs/2509.21678v1)

**Summary:** We present an accelerated nudged elastic band (NEB) study of phenol direct deoxygenation (DDO) on Fe-based bimetallic surfaces using a recently developed Gaussian process regression (GPR) calculator. Our test calculations demonstrate that the GPR calculator achieves up to 3x speedup compared to conventional density functional theory (DFT) calculations while maintaining high accuracy, with energy barrier errors below 0.015 eV. Using GPR-NEB, we systematically examine the DDO mechanism on pristine Fe(110) and surfaces modified with Co and Ni in both top and subsurface layers. Our results show that subsurface Co and Ni substitutions preserve favorable thermodynamics and kinetics for both C-O bond cleavage and C-H bond formation, comparable to those on the pristine Fe(110) surface. In contrast, top-layer substitutions generally increase the C-O bond cleavage barrier, render the step endothermic, and result in significantly higher reverse reaction rates, making DDO unfavorable on these surfaces. This work demonstrates both the effectiveness of GRR-accelerated transition state searches for complex surface reactions and provides insights into rational design of bimetallic catalysts for selective deoxygenation....

---

### 190. Learning Ising Models under Hard Constraints using One Sample

**Authors:** Rohan Chauhan, Ioannis Panageas

**Published:** 2025-09-25

**Category:** cs.LG

**ID:** 2509.20993v1

**Link:** [http://arxiv.org/abs/2509.20993v1](http://arxiv.org/abs/2509.20993v1)

**Summary:** We consider the problem of estimating inverse temperature parameter $β$ of an $n$-dimensional truncated Ising model using a single sample. Given a graph $G = (V,E)$ with $n$ vertices, a truncated Ising model is a probability distribution over the $n$-dimensional hypercube $\{-1,1\}^n$ where each configuration $\mathbfσ$ is constrained to lie in a truncation set $S \subseteq \{-1,1\}^n$ and has probability $\Pr(\mathbfσ) \propto \exp(β\mathbfσ^\top A\mathbfσ)$ with $A$ being the adjacency matrix of $G$. We adopt the recent setting of [Galanis et al. SODA'24], where the truncation set $S$ can be expressed as the set of satisfying assignments of a $k$-SAT formula. Given a single sample $\mathbfσ$ from a truncated Ising model, with inverse parameter $β^*$, underlying graph $G$ of bounded degree $Δ$ and $S$ being expressed as the set of satisfying assignments of a $k$-SAT formula, we design in nearly $O(n)$ time an estimator $\hatβ$ that is $O(Δ^3/\sqrt{n})$-consistent with the true parameter $β^*$ for $k \gtrsim \log(d^2k)Δ^3.$
  Our estimator is based on the maximization of the pseudolikelihood, a notion that has received extensive analysis for various probabilistic models without [Chatterjee, Annals of Statistics '07] or with truncation [Galanis et al. SODA '24]. Our approach generalizes recent techniques from [Daskalakis et al. STOC '19, Galanis et al. SODA '24], to confront the more challenging setting of the truncated Ising model....

---

### 191. In AI Sweet Harmony: Sociopragmatic Guardrail Bypasses and Evaluation-Awareness in OpenAI gpt-oss-20b

**Authors:** Nils Durner

**Published:** 2025-09-25

**Category:** cs.CL

**ID:** 2510.01259v1

**Link:** [http://arxiv.org/abs/2510.01259v1](http://arxiv.org/abs/2510.01259v1)

**Summary:** We probe OpenAI's open-weights 20-billion-parameter model gpt-oss-20b to study how sociopragmatic framing, language choice, and instruction hierarchy affect refusal behavior. Across 80 seeded iterations per scenario, we test several harm domains including ZIP-bomb construction (cyber threat), synthetic card-number generation, minor-unsafe driving advice, drug-precursor indicators, and RAG context exfiltration. Composite prompts that combine an educator persona, a safety-pretext ("what to avoid"), and step-cue phrasing flip assistance rates from 0% to 97.5% on a ZIP-bomb task. On our grid, formal registers in German and French are often leakier than matched English prompts. A "Linux terminal" role-play overrides a developer rule not to reveal context in a majority of runs with a naive developer prompt, and we introduce an AI-assisted hardening method that reduces leakage to 0% in several user-prompt variants. We further test evaluation awareness with a paired-track design and measure frame-conditioned differences between matched "helpfulness" and "harmfulness" evaluation prompts; we observe inconsistent assistance in 13% of pairs. Finally, we find that the OpenAI Moderation API under-captures materially helpful outputs relative to a semantic grader, and that refusal rates differ by 5 to 10 percentage points across inference stacks, raising reproducibility concerns. We release prompts, seeds, outputs, and code for reproducible auditing at https://github.com/ndurner/gpt-oss-rt-run ....

---

### 192. InsightGUIDE: An Opinionated AI Assistant for Guided Critical Reading of Scientific Literature

**Authors:** Paris Koloveas, Serafeim Chatzopoulos, Thanasis Vergoulis, Christos Tryfonopoulos

**Published:** 2025-09-24

**Category:** cs.AI

**ID:** 2509.20493v1

**Link:** [http://arxiv.org/abs/2509.20493v1](http://arxiv.org/abs/2509.20493v1)

**Summary:** The proliferation of scientific literature presents an increasingly significant challenge for researchers. While Large Language Models (LLMs) offer promise, existing tools often provide verbose summaries that risk replacing, rather than assisting, the reading of the source material. This paper introduces InsightGUIDE, a novel AI-powered tool designed to function as a reading assistant, not a replacement. Our system provides concise, structured insights that act as a "map" to a paper's key elements by embedding an expert's reading methodology directly into its core AI logic. We present the system's architecture, its prompt-driven methodology, and a qualitative case study comparing its output to a general-purpose LLM. The results demonstrate that InsightGUIDE produces more structured and actionable guidance, serving as a more effective tool for the modern researcher....

---

### 193. Generative Model Inversion Through the Lens of the Manifold Hypothesis

**Authors:** Xiong Peng, Bo Han, Fengfei Yu, Tongliang Liu, Feng Liu, Mingyuan Zhou

**Published:** 2025-09-24

**Category:** cs.LG

**ID:** 2509.20177v1

**Link:** [http://arxiv.org/abs/2509.20177v1](http://arxiv.org/abs/2509.20177v1)

**Summary:** Model inversion attacks (MIAs) aim to reconstruct class-representative samples from trained models. Recent generative MIAs utilize generative adversarial networks to learn image priors that guide the inversion process, yielding reconstructions with high visual quality and strong fidelity to the private training data. To explore the reason behind their effectiveness, we begin by examining the gradients of inversion loss with respect to synthetic inputs, and find that these gradients are surprisingly noisy. Further analysis reveals that generative inversion implicitly denoises these gradients by projecting them onto the tangent space of the generator manifold, filtering out off-manifold components while preserving informative directions aligned with the manifold. Our empirical measurements show that, in models trained with standard supervision, loss gradients often exhibit large angular deviations from the data manifold, indicating poor alignment with class-relevant directions. This observation motivates our central hypothesis: models become more vulnerable to MIAs when their loss gradients align more closely with the generator manifold. We validate this hypothesis by designing a novel training objective that explicitly promotes such alignment. Building on this insight, we further introduce a training-free approach to enhance gradient-manifold alignment during inversion, leading to consistent improvements over state-of-the-art generative MIAs....

---

### 194. Single crystal growth, structural and physical properties, and absence of a charge density wave in Ti_{0.85}Fe6Ge6

**Authors:** Dechao Cheng, Nour Maraytta, Xiuhua Chen, Xizhi Li, Xueliang Wu, Xiangxiang Jing, Yong Hu, Youpin Gong, Mingquan He, Yisheng Chai, Xiaoyuan Zhou, Pengfei Jiang, Yilin Wang, Michael Merz, Aifeng Wang

**Published:** 2025-09-24

**Category:** cond-mat.mtrl-sci

**ID:** 2509.20142v1

**Link:** [http://arxiv.org/abs/2509.20142v1](http://arxiv.org/abs/2509.20142v1)

**Summary:** Kagome materials with charge density waves (CDWs) are fascinating quantum systems, offering an ideal platform to explore intertwined orders and to uncover novel mechanisms behind CDW formation. Chemical models have been developed and applied to predict CDW in $AM_6X_6$-type kagome materials, such as the rattling chain model based on ScV6Sn6 and the magnetic energy-saving model based on FeGe. In this study, we successfully synthesized Ti_{0.85}Fe6Ge6 single crystals using the vapor transport method. As predicted by the rattling chain model, these crystals are expected to exhibit kagome CDW behavior. Magnetization measurements indicate that Ti_{0.85}Fe6Ge6 is an easy-axis antiferromagnet with T_N = 488 K and transport measurements reveal metallic behavior primarily driven by electron-type carriers. However, no clear signatures of a CDW were observed in Ti_{0.85}Fe6Ge6. Density functional theory calculations demonstrate a markedly distinct electronic structure compared to related compounds: instead of a carrier-doping-induced rigid shift, the density of states shifted away from the Fermi level. Consistent with our structural investigations, the absence of a CDW and the unusual band structure can be attributed to the bonding characteristic within Ti_{0.85}Fe6Ge6. The strong covalent bonds of Ti-Ge1b, along with the solid Ge1b-Ge1b dimers, prevent the Ti-Ge1b-Ge1b-Ti chain from rattling. The presence of Fe-Fe antibonding state at the Fermi level enhances the spin polarization and depletes the electronic density around the Fermi level. Our results suggest that both the ionic radius and the bonding characteristics of the filler atom are crucial for the formation of CDWs in kagome materials. These factors can serve as supplementary terms to the rattling chain model, providing new insights for the discovery of novel kagome CDW materials....

---

### 195. EDBench: Large-Scale Electron Density Data for Molecular Modeling

**Authors:** Hongxin Xiang, Ke Li, Mingquan Liu, Zhixiang Cheng, Bin Yao, Wenjie Du, Jun Xia, Li Zeng, Xin Jin, Xiangxiang Zeng

**Published:** 2025-05-14

**Category:** physics.chem-ph

**ID:** 2505.09262v2

**Link:** [http://arxiv.org/abs/2505.09262v2](http://arxiv.org/abs/2505.09262v2)

**Summary:** Existing molecular machine learning force fields (MLFFs) generally focus on the learning of atoms, molecules, and simple quantum chemical properties (such as energy and force), but ignore the importance of electron density (ED) $ρ(r)$ in accurately understanding molecular force fields (MFFs). ED describes the probability of finding electrons at specific locations around atoms or molecules, which uniquely determines all ground state properties (such as energy, molecular structure, etc.) of interactive multi-particle systems according to the Hohenberg-Kohn theorem. However, the calculation of ED relies on the time-consuming first-principles density functional theory (DFT) which leads to the lack of large-scale ED data and limits its application in MLFFs. In this paper, we introduce EDBench, a large-scale, high-quality dataset of ED designed to advance learning-based research at the electronic scale. Built upon the PCQM4Mv2, EDBench provides accurate ED data, covering 3.3 million molecules. To comprehensively evaluate the ability of models to understand and utilize electronic information, we design a suite of ED-centric benchmark tasks spanning prediction, retrieval, and generation. Our evaluation on several state-of-the-art methods demonstrates that learning from EDBench is not only feasible but also achieves high accuracy. Moreover, we show that learning-based method can efficiently calculate ED with comparable precision while significantly reducing the computational cost relative to traditional DFT calculations. All data and benchmarks from EDBench will be freely available, laying a robust foundation for ED-driven drug discovery and materials science....

---

### 196. Barrier Electrostatics and Contact Engineering for Ultra-Wide Bandgap AlGaN HFETs

**Authors:** Seungheon Shin, Can Cao, Jon Pratt, Yinxuan Zhu, Brianna A. Klein, Andrew Armstrong, Andrew A. Allerman, Siddharth Rajan

**Published:** 2025-09-19

**Category:** cond-mat.mtrl-sci

**ID:** 2509.15715v2

**Link:** [http://arxiv.org/abs/2509.15715v2](http://arxiv.org/abs/2509.15715v2)

**Summary:** We report ultra-wide bandgap (UWBG) AlGaN heterostructure field-effect transistors (HFETs) exhibiting a high breakdown field (> 5.3 MV/cm) and a low contact resistance (~1.55 Ωmm), tailored for high-power radiofrequency applications. A split-doped barrier architecture, employing two distinct doping concentrations, is shown to enhance both the breakdown field and contact resistance. This design enables a state-of-the-art combination of maximum drain current (487 mA/mm) and breakdown field, along with a high cutoff frequency of 7.2 GHz. These results demonstrate a viable pathway to push device performance toward the material limits while minimizing contact resistance in UWBG AlGaN HFETs, paving the way for next-generation high-power, high-frequency applications....

---

### 197. The Open DAC 2025 Dataset for Sorbent Discovery in Direct Air Capture

**Authors:** Anuroop Sriram, Logan M. Brabson, Xiaohan Yu, Sihoon Choi, Kareem Abdelmaqsoud, Elias Moubarak, Pim de Haan, Sindy Löwe, Johann Brehmer, John R. Kitchin, Max Welling, C. Lawrence Zitnick, Zachary Ulissi, Andrew J. Medford, David S. Sholl

**Published:** 2025-08-05

**Category:** cond-mat.mtrl-sci

**ID:** 2508.03162v2

**Link:** [http://arxiv.org/abs/2508.03162v2](http://arxiv.org/abs/2508.03162v2)

**Summary:** Identifying useful sorbent materials for direct air capture (DAC) from humid air remains a challenge. We present the Open DAC 2025 (ODAC25) dataset, a significant expansion and improvement upon ODAC23 (Sriram et al., ACS Central Science, 10 (2024) 923), comprising nearly 60 million DFT single-point calculations for CO$_2$, H$_2$O, N$_2$, and O$_2$ adsorption in 15,000 MOFs. ODAC25 introduces chemical and configurational diversity through functionalized MOFs, high-energy GCMC-derived placements, and synthetically generated frameworks. ODAC25 also significantly improves upon the accuracy of DFT calculations and the treatment of flexible MOFs in ODAC23. Along with the dataset, we release new state-of-the-art machine-learned interatomic potentials trained on ODAC25 and evaluate them on adsorption energy and Henry's law coefficient predictions....

---

### 198. DAWM: Diffusion Action World Models for Offline Reinforcement Learning via Action-Inferred Transitions

**Authors:** Zongyue Li, Xiao Han, Yusong Li, Niklas Strauss, Matthias Schubert

**Published:** 2025-09-23

**Category:** cs.LG

**ID:** 2509.19538v1

**Link:** [http://arxiv.org/abs/2509.19538v1](http://arxiv.org/abs/2509.19538v1)

**Summary:** Diffusion-based world models have demonstrated strong capabilities in synthesizing realistic long-horizon trajectories for offline reinforcement learning (RL). However, many existing methods do not directly generate actions alongside states and rewards, limiting their compatibility with standard value-based offline RL algorithms that rely on one-step temporal difference (TD) learning. While prior work has explored joint modeling of states, rewards, and actions to address this issue, such formulations often lead to increased training complexity and reduced performance in practice. We propose \textbf{DAWM}, a diffusion-based world model that generates future state-reward trajectories conditioned on the current state, action, and return-to-go, paired with an inverse dynamics model (IDM) for efficient action inference. This modular design produces complete synthetic transitions suitable for one-step TD-based offline RL, enabling effective and computationally efficient training. Empirically, we show that conservative offline RL algorithms such as TD3BC and IQL benefit significantly from training on these augmented trajectories, consistently outperforming prior diffusion-based baselines across multiple tasks in the D4RL benchmark....

---

### 199. Graph Data Modeling: Molecules, Proteins, & Chemical Processes

**Authors:** José Manuel Barraza-Chavez, Rana A. Barghout, Ricardo Almada-Monter, Adrian Jinich, Radhakrishnan Mahadevan, Benjamin Sanchez-Lengeling

**Published:** 2025-08-26

**Category:** cs.LG

**ID:** 2508.19356v3

**Link:** [http://arxiv.org/abs/2508.19356v3](http://arxiv.org/abs/2508.19356v3)

**Summary:** Graphs are central to the chemical sciences, providing a natural language to describe molecules, proteins, reactions, and industrial processes. They capture interactions and structures that underpin materials, biology, and medicine. This primer, Graph Data Modeling: Molecules, Proteins, & Chemical Processes, introduces graphs as mathematical objects in chemistry and shows how learning algorithms (particularly graph neural networks) can operate on them. We outline the foundations of graph design, key prediction tasks, representative examples across chemical sciences, and the role of machine learning in graph-based modeling. Together, these concepts prepare readers to apply graph methods to the next generation of chemical discovery....

---

### 200. Dynami-CAL GraphNet: A Physics-Informed Graph Neural Network Conserving Linear and Angular Momentum for Dynamical Systems

**Authors:** Vinay Sharma, Olga Fink

**Published:** 2025-01-13

**Category:** cs.LG

**ID:** 2501.07373v2

**Link:** [http://arxiv.org/abs/2501.07373v2](http://arxiv.org/abs/2501.07373v2)

**Summary:** Accurate, interpretable, and real-time modeling of multi-body dynamical systems is essential for predicting behaviors and inferring physical properties in natural and engineered environments. Traditional physics-based models face scalability challenges and are computationally demanding, while data-driven approaches like Graph Neural Networks (GNNs) often lack physical consistency, interpretability, and generalization. In this paper, we propose Dynami-CAL GraphNet, a Physics-Informed Graph Neural Network that integrates the learning capabilities of GNNs with physics-based inductive biases to address these limitations. Dynami-CAL GraphNet enforces pairwise conservation of linear and angular momentum for interacting nodes using edge-local reference frames that are equivariant to rotational symmetries, invariant to translations, and equivariant to node permutations. This design ensures physically consistent predictions of node dynamics while offering interpretable, edge-wise linear and angular impulses resulting from pairwise interactions. Evaluated on a 3D granular system with inelastic collisions, Dynami-CAL GraphNet demonstrates stable error accumulation over extended rollouts, effective extrapolations to unseen configurations, and robust handling of heterogeneous interactions and external forces. Dynami-CAL GraphNet offers significant advantages in fields requiring accurate, interpretable, and real-time modeling of complex multi-body dynamical systems, such as robotics, aerospace engineering, and materials science. By providing physically consistent and scalable predictions that adhere to fundamental conservation laws, it enables the inference of forces and moments while efficiently handling heterogeneous interactions and external forces....

---

### 201. A Methodological Study on Data Representation for Machine Learning Modelling of Thermal Conductivity of Rare-Earth Oxides

**Authors:** Amiya Chowdhury, Acacio Rincón Romero, Eduardo Aguilar-Bejarano, Halar Memon, Grazziela Figueredo, Tanvir Hussain

**Published:** 2025-09-23

**Category:** cond-mat.mtrl-sci

**ID:** 2509.18951v1

**Link:** [http://arxiv.org/abs/2509.18951v1](http://arxiv.org/abs/2509.18951v1)

**Summary:** Quantitative structure-activity relationship (QSAR) modelling is widely employed in materials science to predict properties of interest and extract useful descriptors for measured properties. In thermal barrier coatings (TBC), QSAR can significantly shorten the experimental discovery cycle, which can take years. Although machine learning methods are commonly employed for QSAR, their performance depends on the data quality and how instances are represented. Traditional, hand-crafted descriptors based on known material properties are limited to represent materials that share the same basic crystal structure, limited the size of the dataset. By contrast, graph neural networks offer a more expressive representation, encoding atomic positions and bonds in the crystal lattice. In this study, we compare Random Forest (RF) and Gaussian Process (GP) models trained on hand-crafted descriptors from the literature with graph-based representations for high-entropy, rare-earth pyrochlore oxides using the Crystal Graph Convolutional Neural Network (CGCNN). Two different types of augmentation methods are also explored to account for the limited data size, one of which is only applicable to graph-based representations. Our findings show that the CGCNN model substantially outperforms the RF and GP models, underscoring the potential of graph-based representations for enhanced QSAR modelling in TBC research....

---

### 202. Radiation-Triggered Superfluorescent Scintillation in Quantum-Ordered Perovskite Nanocrystal Superlattices

**Authors:** Matteo L. Zaffalon, Andrea Fratelli, Taras Sekh, Emanuele Mazzola, Francesco Carulli, Francesco Bruni, Maryna Bodnarchuk, Francesco Meinardi, Luca Gironi, Maksym V. Kovalenko, Sergio Brovelli

**Published:** 2025-09-23

**Category:** physics.optics

**ID:** 2509.18767v1

**Link:** [http://arxiv.org/abs/2509.18767v1](http://arxiv.org/abs/2509.18767v1)

**Summary:** Superfluorescence, a cooperative emission phenomenon arising from the coherent coupling of excited dipoles, has historically been observed under optical excitation in carefully engineered quantum systems. Here, we report the first observation of superfluorescence triggered by ionizing radiation in lead-halide perovskite nanocrystal (NC) superlattices. Using CsPbBr3 NC superlattices with long-range structural and electronic order, we demonstrate that secondary electrons generated by high-energy photons can induce efficient cooperative emission bursts characteristic of superfluorescence with unprecedented scintillation lifetime of ~40 ps, thereby introducing a new class of coherent scintillating metamaterials. Side-by-side optical and scintillation measurements reveal a direct analogy between ionizing and intense optical excitation, both leading to high excitonic densities that result in superfluorescent emission, even at mild, technologically accessible cryogenic temperatures. The discovery that incoherent, stochastic ionization cascades can seed coherent many-body optical responses with radiatively accelerated luminescence and large Stokes shifts establishes a pathway toward ultrafast, reabsorption-free, quantum-ordered nanotechnological scintillators, paving the way for the future development of radiation detectors based on quantum technologies for advanced radiation detection applications....

---

### 203. Interaction Topological Transformer for Multiscale Learning in Porous Materials

**Authors:** Dong Chen, Jian Liu, Chun-Long Chen, Guo-Wei Wei

**Published:** 2025-09-23

**Category:** cs.LG

**ID:** 2509.18573v1

**Link:** [http://arxiv.org/abs/2509.18573v1](http://arxiv.org/abs/2509.18573v1)

**Summary:** Porous materials exhibit vast structural diversity and support critical applications in gas storage, separations, and catalysis. However, predictive modeling remains challenging due to the multiscale nature of structure-property relationships, where performance is governed by both local chemical environments and global pore-network topology. These complexities, combined with sparse and unevenly distributed labeled data, hinder generalization across material families. We propose the Interaction Topological Transformer (ITT), a unified data-efficient framework that leverages novel interaction topology to capture materials information across multiple scales and multiple levels, including structural, elemental, atomic, and pairwise-elemental organization. ITT extracts scale-aware features that reflect both compositional and relational structure within complex porous frameworks, and integrates them through a built-in Transformer architecture that supports joint reasoning across scales. Trained using a two-stage strategy, i.e., self-supervised pretraining on 0.6 million unlabeled structures followed by supervised fine-tuning, ITT achieves state-of-the-art, accurate, and transferable predictions for adsorption, transport, and stability properties. This framework provides a principled and scalable path for learning-guided discovery in structurally and chemically diverse porous materials....

---

### 204. The Open Catalyst 2025 (OC25) Dataset and Models for Solid-Liquid Interfaces

**Authors:** Sushree Jagriti Sahoo, Mikael Maraschin, Daniel S. Levine, Zachary Ulissi, C. Lawrence Zitnick, Joel B Varley, Joseph A. Gauthier, Nitish Govindarajan, Muhammed Shuaibi

**Published:** 2025-09-22

**Category:** cond-mat.mtrl-sci

**ID:** 2509.17862v1

**Link:** [http://arxiv.org/abs/2509.17862v1](http://arxiv.org/abs/2509.17862v1)

**Summary:** Catalysis at solid-liquid interfaces plays a central role in the advancement of energy storage and sustainable chemical production technologies. By enabling accurate, long-time scale simulations, machine learning (ML) models have the potential to accelerate the discovery of (electro)catalysts. While prior Open Catalyst datasets (OC20 and OC22) have advanced the field by providing large-scale density functional theory (DFT) data of adsorbates on surfaces at solid-gas interfaces, they do not capture the critical role of solvent and electrolyte effects at solid-liquid interfaces. To bridge this gap, we introduce the Open Catalyst 2025 (OC25) dataset, consisting of 7,801,261 calculations across 1,511,270 unique explicit solvent environments. OC25 constitutes the largest and most diverse solid-liquid interface dataset that is currently available and provides configurational and elemental diversity: spanning 88 elements, commonly used solvents/ions, varying solvent layers, and off-equilibrium sampling. State-of-the-art models trained on the OC25 dataset exhibit energy, force, and solvation energy errors as low as 0.1 eV, 0.015 eV/Å, and 0.04 eV, respectively; significantly lower than than the recently released Universal Models for Atoms (UMA-OC20). Additionally, we discuss the impact of the quality of DFT-calculated forces on model training and performance. The dataset and accompanying baseline models are made openly available for the community. We anticipate the dataset to facilitate large length-scale and long-timescale simulations of catalytic transformations at solid-liquid interfaces, advancing molecular-level insights into functional interfaces and enabling the discovery of next-generation energy storage and conversion technologies....

---

### 205. Quantifying Student Success with Generative AI: A Monte Carlo Simulation Informed by Systematic Review

**Authors:** Seyma Yaman Kayadibi

**Published:** 2025-06-30

**Category:** cs.CY

**ID:** 2507.01062v2

**Link:** [http://arxiv.org/abs/2507.01062v2](http://arxiv.org/abs/2507.01062v2)

**Summary:** The exponential development of generative artificial intelligence (GenAI) technologies like ChatGPT has raised increasing curiosity about their use in higher education, specifically with respect to how students view them, make use of them, and the implications for learning outcomes. This paper employs a hybrid methodological approach involving a systematic literature review and simulation-based modeling to explore student perceptions of GenAI use in the context of higher education. A total of nineteen empirical articles from 2023 through 2025 were selected from the PRISMA-based search targeting the Scopus database. Synthesis of emerging patterns from the literature was achieved by thematic categorization. Six of these had enough quantitative information, i.e., item-level means and standard deviations, to permit probabilistic modeling. One dataset, from the resulting subset, was itself selected as a representative case with which to illustrate inverse-variance weighting by Monte Carlo simulation, by virtue of its well-designed Likert scale format and thematic alignment with the use of computing systems by the researcher.
  The simulation provided a composite "Success Score" forecasting the strength of the relationship between student perceptions and learning achievements. Findings reveal that attitude factors concerned with usability and real-world usefulness are significantly better predictors of positive learning achievement than affective or trust-based factors. Such an interdisciplinary perspective provides a unique means of linking thematic results with predictive modelling, resonating with longstanding controversies about the proper use of GenAI tools within the university....

---

### 206. Intention-aware Hierarchical Diffusion Model for Long-term Trajectory Anomaly Detection

**Authors:** Chen Wang, Sarah Erfani, Tansu Alpcan, Christopher Leckie

**Published:** 2025-09-21

**Category:** cs.AI

**ID:** 2509.17068v1

**Link:** [http://arxiv.org/abs/2509.17068v1](http://arxiv.org/abs/2509.17068v1)

**Summary:** Long-term trajectory anomaly detection is a challenging problem due to the diversity and complex spatiotemporal dependencies in trajectory data. Existing trajectory anomaly detection methods fail to simultaneously consider both the high-level intentions of agents as well as the low-level details of the agent's navigation when analysing an agent's trajectories. This limits their ability to capture the full diversity of normal trajectories. In this paper, we propose an unsupervised trajectory anomaly detection method named Intention-aware Hierarchical Diffusion model (IHiD), which detects anomalies through both high-level intent evaluation and low-level sub-trajectory analysis. Our approach leverages Inverse Q Learning as the high-level model to assess whether a selected subgoal aligns with an agent's intention based on predicted Q-values. Meanwhile, a diffusion model serves as the low-level model to generate sub-trajectories conditioned on subgoal information, with anomaly detection based on reconstruction error. By integrating both models, IHiD effectively utilises subgoal transition knowledge and is designed to capture the diverse distribution of normal trajectories. Our experiments show that the proposed method IHiD achieves up to 30.2% improvement in anomaly detection performance in terms of F1 score over state-of-the-art baselines....

---

### 207. Spin PN Junctions: Giant Magnetoresistance, Tunable Circular Polarization, and Spin Zener Filter

**Authors:** Chun-Yi Xue, Gang Su, Bo Gu

**Published:** 2025-09-21

**Category:** cond-mat.mtrl-sci

**ID:** 2509.16904v1

**Link:** [http://arxiv.org/abs/2509.16904v1](http://arxiv.org/abs/2509.16904v1)

**Summary:** We demonstrate that spin PN junctions-magnetic semiconductor homojunctions with spin splitting-induced band offsets-fundamentally redefine carrier transport via spin-dependent recom bination probabilities. By integrating this mechanism into the Shockley model, we predict
  a near 100 enhancement in magnetoresistance sensitivity under small forward bias, where exponen tial modulation of recombination lifetimes by magnetic fields amplifies resistance changes.
  Angular momentum conservation enables magnetically tunable circularly polarized luminescence:
  exclusive conduction-band or valence-band splitting in both neutral regions achieves near-half po larization, while global splitting degrades emission coherence. Furthermore, we propose
  a "spin Zener filter" exploiting 1eV valence band splitting in (Ga, Mn)As, where spin-dependent
  barrier heights generate near 100% spin-polarized tunneling currents within a voltage-selective win dow. These results establish spin PN junctions as a universal design paradigm for magnetically
  amplified electronics, polarization-programmable optoelectronics, and voltage-gated spin injection
  without ferromagnetic contacts....

---

### 208. pyRMG: A Python Framework for High-Throughput, Large-Cell Real-Space MultiGrid DFT Calculations

**Authors:** R. J. Morelock, S. Bagchi, E. L. Briggs, W. Lu, J. Bernholc, P. Ganesh

**Published:** 2025-09-20

**Category:** cond-mat.mtrl-sci

**ID:** 2509.16775v1

**Link:** [http://arxiv.org/abs/2509.16775v1](http://arxiv.org/abs/2509.16775v1)

**Summary:** Computational materials science has evolved toward materials informatics, where large datasets of complex, multispecies compounds are generated and evaluated using density functional theory (DFT). Materials genome projects mine these datasets for candidates with breakthrough properties, but existing databases remain limited to compounds with relatively small unit cells due to computational cost. Exascale computers now provide the power to simulate larger and more chemically realistic systems, but fully realizing this potential requires DFT codes that can efficiently scale to thousands of processors. Our real-space multigrid (RMG) DFT code's grid-decomposition approach scales nearly linearly with the number of GPUs, even for simulations exceeding thousands of atoms. This scalability makes RMG a compelling tool for high-throughput DFT studies of materials that would otherwise be bottlenecked in other codes (for example, by global Fast Fourier Transforms in plane-wave DFT). In this work, we present pyRMG, a Python package designed to streamline the setup and execution of RMG DFT calculations. Built on the pymatgen and ASE Python packages, pyRMG automates input generation and convergence checking, and integrates with modern job schedulers (e.g., Flux) on leadership-class platforms such as Frontier and Perlmutter. We demonstrate pyRMG for a high-throughput study of interfacial strain and twist-angle effects in lattice-matched, 2D Bi$_2$Se$_3$/NbSe$_2$ heterostructures, which form large, anisotropic supercells. Our results link strain and twist angle to material informatics properties, including stability and band gap, and show that pyRMG can initialize and converge challenging RMG-based workflows with limited user intervention....

---

### 209. Statistical Inference for Misspecified Contextual Bandits

**Authors:** Yongyi Guo, Ziping Xu

**Published:** 2025-09-08

**Category:** math.ST

**ID:** 2509.06287v2

**Link:** [http://arxiv.org/abs/2509.06287v2](http://arxiv.org/abs/2509.06287v2)

**Summary:** Contextual bandit algorithms have transformed modern experimentation by enabling real-time adaptation for personalized treatment and efficient use of data. Yet these advantages create challenges for statistical inference due to adaptivity. A fundamental property that supports valid inference is policy convergence, meaning that action-selection probabilities converge in probability given the context. Convergence ensures replicability of adaptive experiments and stability of online algorithms. In this paper, we highlight a previously overlooked issue: widely used algorithms such as LinUCB may fail to converge when the reward model is misspecified, and such non-convergence creates fundamental obstacles for statistical inference. This issue is practically important, as misspecified models -- such as linear approximations of complex dynamic system -- are often employed in real-world adaptive experiments to balance bias and variance.
  Motivated by this insight, we propose and analyze a broad class of algorithms that are guaranteed to converge even under model misspecification. Building on this guarantee, we develop a general inference framework based on an inverse-probability-weighted Z-estimator (IPW-Z) and establish its asymptotic normality with a consistent variance estimator. Simulation studies confirm that the proposed method provides robust and data-efficient confidence intervals, and can outperform existing approaches that exist only in the special case of offline policy evaluation. Taken together, our results underscore the importance of designing adaptive algorithms with built-in convergence guarantees to enable stable experimentation and valid statistical inference in practice....

---

### 210. Matter-of-Fact: A Benchmark for Verifying the Feasibility of Literature-Supported Claims in Materials Science

**Authors:** Peter Jansen, Samiah Hassan, Ruoyao Wang

**Published:** 2025-06-04

**Category:** cs.AI

**ID:** 2506.04410v2

**Link:** [http://arxiv.org/abs/2506.04410v2](http://arxiv.org/abs/2506.04410v2)

**Summary:** Contemporary approaches to assisted scientific discovery use language models to automatically generate large numbers of potential hypothesis to test, while also automatically generating code-based experiments to test those hypotheses. While hypotheses can be comparatively inexpensive to generate, automated experiments can be costly, particularly when run at scale (i.e. thousands of experiments). Developing the capacity to filter hypotheses based on their feasibility would allow discovery systems to run at scale, while increasing their likelihood of making significant discoveries. In this work we introduce Matter-of-Fact, a challenge dataset for determining the feasibility of hypotheses framed as claims, while operationalizing feasibility assessment as a temporally-filtered claim verification task using backtesting. Matter-of-Fact includes 8.4k claims extracted from scientific articles spanning four high-impact contemporary materials science topics, including superconductors, semiconductors, batteries, and aerospace materials, while including qualitative and quantitative claims from theoretical, experimental, and code/simulation results. We show that strong baselines that include retrieval augmented generation over scientific literature and code generation fail to exceed 72% performance on this task (chance performance is 50%), while domain-expert verification suggests nearly all are solvable -- highlighting both the difficulty of this task for current models, and the potential to accelerate scientific discovery by making near-term progress....

---

### 211. Towards a deeper fundamental understanding of (Al,Sc)N ferroelectric nitrides

**Authors:** Peng Chen, Dawei Wang, Alejandro Mercado Tejerina, Keisuke Yazawa, Andriy Zakutayev, Charles Paillard, Laurent Bellaiche

**Published:** 2025-09-18

**Category:** cond-mat.mtrl-sci

**ID:** 2509.15050v2

**Link:** [http://arxiv.org/abs/2509.15050v2](http://arxiv.org/abs/2509.15050v2)

**Summary:** Density Functional Theory (DFT) calculations, within the virtual crystal alloy approximation, are performed, along with the development of a Landau-type model employing a symmetry-allowed analytical expression of the internal energy and having parameters being determined from first principles, to investigate properties and energetics of Al1-xScxN ferroelectric nitrides in their hexagonal forms. These DFT computations and this model predict the existence of two different types of minima, namely the 4-fold-coordinated wurtzite (WZ) polar structure and a 5-times paraelectric hexagonal phase (to be denoted as H5), for any Sc composition up to 40%. The H5 minimum progressively becomes the lowest energy state within hexagonal symmetry as the Sc concentration increases from 0 to 40%. Furthermore, the model points out to several key findings. Examples include the crucial role of the coupling between polarization and strains to create the WZ minimum, in addition to polar and elastic energies, and that the origin of the H5 state overcoming the WZ phase as the global minimum within hexagonal symmetry when increasing the Sc composition mostly lies in the compositional dependency of only two parameters, one linked to the polarization and another one being purely elastic in nature. Other examples are that forcing Al1-xScxN systems to have no or a weak change in lattice parameters when heating them allows to reproduce well their finite-temperature polar properties, and that a value of the axial ratio close to that of the ideal WZ structure does imply a large polarization at low temperatures but not necessarily at high temperatures because of the ordered-disordered character of the temperature-induced formation of the WZ state. Such findings should allow for a better fundamental understanding of (Al,Sc)N ferroelectric nitrides, which may be used to design efficient devices operating at low voltages....

---

### 212. Monte Carlo Tree Diffusion with Multiple Experts for Protein Design

**Authors:** Xuefeng Liu, Mingxuan Cao, Songhao Jiang, Xiao Luo, Xiaotian Duan, Mengdi Wang, Tobin R. Sosnick, Jinbo Xu, Rick Stevens

**Published:** 2025-09-19

**Category:** cs.LG

**ID:** 2509.15796v1

**Link:** [http://arxiv.org/abs/2509.15796v1](http://arxiv.org/abs/2509.15796v1)

**Summary:** The goal of protein design is to generate amino acid sequences that fold into functional structures with desired properties. Prior methods combining autoregressive language models with Monte Carlo Tree Search (MCTS) struggle with long-range dependencies and suffer from an impractically large search space. We propose MCTD-ME, Monte Carlo Tree Diffusion with Multiple Experts, which integrates masked diffusion models with tree search to enable multi-token planning and efficient exploration. Unlike autoregressive planners, MCTD-ME uses biophysical-fidelity-enhanced diffusion denoising as the rollout engine, jointly revising multiple positions and scaling to large sequence spaces. It further leverages experts of varying capacities to enrich exploration, guided by a pLDDT-based masking schedule that targets low-confidence regions while preserving reliable residues. We propose a novel multi-expert selection rule (PH-UCT-ME) extends predictive-entropy UCT to expert ensembles. On the inverse folding task (CAMEO and PDB benchmarks), MCTD-ME outperforms single-expert and unguided baselines in both sequence recovery (AAR) and structural similarity (scTM), with gains increasing for longer proteins and benefiting from multi-expert guidance. More generally, the framework is model-agnostic and applicable beyond inverse folding, including de novo protein engineering and multi-objective molecular generation....

---

### 213. TITAN: A Trajectory-Informed Technique for Adaptive Parameter Freezing in Large-Scale VQE

**Authors:** Yifeng Peng, Xinyi Li, Samuel Yen-Chi Chen, Kaining Zhang, Zhiding Liang, Ying Wang, Yuxuan Du

**Published:** 2025-09-18

**Category:** quant-ph

**ID:** 2509.15193v1

**Link:** [http://arxiv.org/abs/2509.15193v1](http://arxiv.org/abs/2509.15193v1)

**Summary:** Variational quantum Eigensolver (VQE) is a leading candidate for harnessing quantum computers to advance quantum chemistry and materials simulations, yet its training efficiency deteriorates rapidly for large Hamiltonians. Two issues underlie this bottleneck: (i) the no-cloning theorem imposes a linear growth in circuit evaluations with the number of parameters per gradient step; and (ii) deeper circuits encounter barren plateaus (BPs), leading to exponentially increasing measurement overheads. To address these challenges, here we propose a deep learning framework, dubbed Titan, which identifies and freezes inactive parameters of a given ansatze at initialization for a specific class of Hamiltonians, reducing the optimization overhead without sacrificing accuracy. The motivation of Titan starts with our empirical findings that a subset of parameters consistently has a negligible influence on training dynamics. Its design combines a theoretically grounded data construction strategy, ensuring each training example is informative and BP-resilient, with an adaptive neural architecture that generalizes across ansatze of varying sizes. Across benchmark transverse-field Ising models, Heisenberg models, and multiple molecule systems up to 30 qubits, Titan achieves up to 3 times faster convergence and 40% to 60% fewer circuit evaluations than state-of-the-art baselines, while matching or surpassing their estimation accuracy. By proactively trimming parameter space, Titan lowers hardware demands and offers a scalable path toward utilizing VQE to advance practical quantum chemistry and materials science....

---

### 214. Accelerated Discovery of Topological Conductors for Nanoscale Interconnects

**Authors:** Alexander C. Tyner, William Rogers, Po-Hsin Shih, Yi-Hsin Tu, Gengchiau Liang, Hsin Lin, Ching-Tzu Chen, James M. Rondinelli

**Published:** 2025-09-18

**Category:** cond-mat.mes-hall

**ID:** 2509.15135v1

**Link:** [http://arxiv.org/abs/2509.15135v1](http://arxiv.org/abs/2509.15135v1)

**Summary:** The sharp increase in resistivity of copper interconnects at ultra-scaled dimensions threatens the continued miniaturization of integrated circuits. Topological semimetals (TSMs) with gapless surface states (Fermi arcs) provide conduction channels resistant to localization. Here we develop an efficient computational framework to quantify 0K surface-state transmission in nanowires derived from Wannier tight-binding models of topological conductors that faithfully reproduce relativistic density functional theory results. Sparse matrix techniques enable scalable simulations incorporating disorder and surface roughness, allowing systematic materials screening across sizes, chemical potentials, and transport directions. A dataset of 3000 surface transmission values reveals TiS, ZrB$_{2}$, and nitrides AN where A=(Mo, Ta, W) as candidates with conductance matching or exceeding copper and benchmark TSMs NbAs and NbP. This dataset further supports machine learning models for rapid interconnect compound identification. Our results highlight the promise of topological conductors in overcoming copper's scaling limits and provide a roadmap for data-driven discovery of next-generation interconnects....

---

### 215. Towards universal property prediction in Cartesian space: TACE is all you need

**Authors:** Zemin Xu, Wenbo Xie, Daiqian Xie, P. Hu

**Published:** 2025-09-18

**Category:** stat.ML

**ID:** 2509.14961v1

**Link:** [http://arxiv.org/abs/2509.14961v1](http://arxiv.org/abs/2509.14961v1)

**Summary:** Machine learning has revolutionized atomistic simulations and materials science, yet current approaches often depend on spherical-harmonic representations. Here we introduce the Tensor Atomic Cluster Expansion and Tensor Moment Potential, the first unified framework formulated entirely in Cartesian space for the systematic prediction of arbitrary structure-determined tensorial properties. TACE achieves this by decomposing atomic environments into a complete hierarchy of (irreducible) Cartesian tensors, ensuring symmetry-consistent representations that naturally encode invariance and equivariance constraints. Beyond geometry, TACE incorporates universal embeddings that flexibly integrate diverse attributes including basis sets, charges, magnetic moments and field perturbations. This allows explicit control over external invariants and equivariants in the prediction process. Long-range interactions are also accurately described through the Latent Ewald Summation module within the short-range approximation, providing a rigorous yet computationally efficient treatment of electrostatic interactions. We demonstrate that TACE attains accuracy, stability, and efficiency on par with or surpassing leading equivariant frameworks across finite molecules and extended materials, including in-domain and out-of-domain benchmarks, spectra, hessians, external-field response, charged systems, magnetic systems, multi-fidelity training, and heterogeneous catalytic systems. Crucially, TACE bridges scalar and tensorial modeling and establishes a Cartesian-space paradigm that unifies and extends beyond the design space of spherical-harmonic-based methods. This work lays the foundation for a new generation of universal atomistic machine learning models capable of systematically capturing the rich interplay of geometry, fields and material properties within a single coherent framework....

---

### 216. MovieCORE: COgnitive REasoning in Movies

**Authors:** Gueter Josmy Faure, Min-Hung Chen, Jia-Fong Yeh, Ying Cheng, Hung-Ting Su, Yung-Hao Tang, Shang-Hong Lai, Winston H. Hsu

**Published:** 2025-08-26

**Category:** cs.CL

**ID:** 2508.19026v3

**Link:** [http://arxiv.org/abs/2508.19026v3](http://arxiv.org/abs/2508.19026v3)

**Summary:** This paper introduces MovieCORE, a novel video question answering (VQA) dataset designed to probe deeper cognitive understanding of movie content. Unlike existing datasets that focus on surface-level comprehension, MovieCORE emphasizes questions that engage System-2 thinking while remaining specific to the video material. We present an innovative agentic brainstorming approach, utilizing multiple large language models (LLMs) as thought agents to generate and refine high-quality question-answer pairs. To evaluate dataset quality, we develop a set of cognitive tests assessing depth, thought-provocation potential, and syntactic complexity. We also propose a comprehensive evaluation scheme for assessing VQA model performance on deeper cognitive tasks. To address the limitations of existing video-language models (VLMs), we introduce an agentic enhancement module, Agentic Choice Enhancement (ACE), which improves model reasoning capabilities post-training by up to 25%. Our work contributes to advancing movie understanding in AI systems and provides valuable insights into the capabilities and limitations of current VQA models when faced with more challenging, nuanced questions about cinematic content. Our project page, dataset and code can be found at https://joslefaure.github.io/assets/html/moviecore.html....

---

### 217. Generalized invariants meet constitutive neural networks: A novel framework for hyperelastic materials

**Authors:** Denisa Martonová, Alain Goriely, Ellen Kuhl

**Published:** 2025-08-16

**Category:** cond-mat.soft

**ID:** 2508.12063v3

**Link:** [http://arxiv.org/abs/2508.12063v3](http://arxiv.org/abs/2508.12063v3)

**Summary:** The major challenge in determining a hyperelastic model for a given material is the choice of invariants and the selection how the strain energy function depends functionally on these invariants. Here we introduce a new data-driven framework that simultaneously discovers appropriate invariants and constitutive models for isotropic incompressible hyperelastic materials. Our approach identifies both the most suitable invariants in a class of generalized invariants and the corresponding strain energy function directly from experimental observations. Unlike previous methods that rely on fixed invariant choices or sequential fitting procedures, our method integrates the discovery process into a single neural network architecture. By looking at a continuous family of possible invariants, the model can flexibly adapt to different material behaviors. We demonstrate the effectiveness of this approach using popular benchmark datasets for rubber and brain tissue. For rubber, the method recovers a stretch-dominated formulation consistent with classical models. For brain tissue, it identifies a formulation sensitive to small stretches, capturing the nonlinear shear response characteristic of soft biological matter. Compared to traditional and neural-network-based models, our framework provides improved predictive accuracy and interpretability across a wide range of deformation states. This unified strategy offers a robust tool for automated and physically meaningful model discovery in hyperelasticity....

---

### 218. Structural effects of boron doping in diamond crystals for gamma-ray light-source applications: Insights from molecular dynamics simulations

**Authors:** Matthew D. Dickers, Felipe Fantuzzi, Nigel J. Mason, Andrei V. Korol, Andrey V. Solov'yov

**Published:** 2025-09-16

**Category:** cond-mat.mtrl-sci

**ID:** 2509.13045v2

**Link:** [http://arxiv.org/abs/2509.13045v2](http://arxiv.org/abs/2509.13045v2)

**Summary:** Boron-doped diamond crystals (BDD, C$_{1-x}$B$_{x}$) exhibit exceptional mechanical strength, electronic tunability, and resistance to radiation damage. This makes them promising materials for use in gamma-ray crystal-based light sources. To better understand and quantify the structural distortions introduced by doping, which are critical for maintaining channelling efficiency, we perform atomistic-level molecular dynamics simulations on periodic C$_{1-x}$B$_{x}$ systems of various sizes. These simulations allow the influence of boron concentration on the lattice constant and the (110) and (100) inter-planar distances to be evaluated over the concentration range from pure diamond (0%) to 5% boron at room temperature (300 K). Linear relationships between both lattice constant and inter-planar distance with increasing dopant concentration are observed, with a deviation from Vegard's Law. This deviation is larger than that reported by other theoretical and computational studies; however, this may be attributed to an enhanced crystal quality over these studies, a vital aspect when considering gamma-ray crystal light source design. The methodology presented here incorporates several refinements to closely reflect the conditions of microwave plasma chemical vapour deposition (MPCVD) crystal growth. Validation of the methodology is provided through a comprehensive statistical analysis of the structure of our generated crystals. These results enable reliable atomistic modelling of doped diamond crystals and support their use in the design and fabrication of periodically bent structures for next-generation gamma-ray light source technologies....

---

### 219. From Data to Alloys Predicting and Screening High Entropy Alloys for High Hardness Using Machine Learning

**Authors:** Rahul Bouri, Manikantan R. Nair, Tribeni Roy

**Published:** 2025-09-16

**Category:** cond-mat.mtrl-sci

**ID:** 2509.13479v1

**Link:** [http://arxiv.org/abs/2509.13479v1](http://arxiv.org/abs/2509.13479v1)

**Summary:** The growing need for structural materials with strength, mechanical stability, and durability in extreme environments is driving the development of high entropy alloys. These are materials with near equiatomic mixing of five or more principal elements, and such compositional complexity often leads to improvements in mechanical properties and high thermal stability, etc. Thus, high-entropy alloys have found their applications in domains like aerospace, biomedical, energy storage, catalysis, electronics, etc. However, the vast compositional design and experimental exploration of high-entropy alloys are both time consuming and expensive and require a large number of resources. Machine learning techniques have thus become essential for accelerating high entropy alloys discovery using data driven predictions of promising alloy combinations and their properties. Hence, this work employs a machine learning framework that predicts high entropy alloy hardness from elemental descriptors such as atomic radius, valence electron count, bond strength, etc. Machine learning regression models, like LightGBM, Gradient Boosting Regressor, and Transformer encoder, were trained on experimental data. Additionally, a language model was also fine tuned to predict hardness from elemental descriptor strings. The results indicate that LightGBM has better accuracy in predicting the hardness of high entropy alloys compared to other models used in this study. Further, a combinatorial technique was used to generate over 9 million virtual high entropy alloy candidates, and the trained machine learning models were used to predict their hardness. This study shows how machine learning-driven high throughput screening and language modelling approaches can accelerate the development of next generation high entropy alloys....

---

### 220. High-throughput screening of spin Hall conductivity in 2D materials

**Authors:** Fu Li, Xiaoxiong Liu, Vikrant Chaudhary, Ruiwen Xie, Chen Shen, Hao Wang, Hongbin Zhang

**Published:** 2025-09-16

**Category:** cond-mat.mtrl-sci

**ID:** 2509.13204v1

**Link:** [http://arxiv.org/abs/2509.13204v1](http://arxiv.org/abs/2509.13204v1)

**Summary:** Two-dimensional (2D) materials with large spin Hall effect (SHE) have attracted significant attention due to their potential applications in next-generation spintronic devices. In this work, we perform high-throughput (HTP) calculations to obtain the spin Hall conductivity (SHC) of 4486 non-magnetic compounds in the \texttt{2Dmatpedia} database and identify six materials with SHC exceeding $500\,(\hbar/e)\,(\mathrm{S/cm})$, surpassing those of previously known materials. Detailed analysis reveals that the significant SHC can be attributed to spin-orbit coupling (SOC)-induced gap openings at Dirac-like band crossings. Additionally, the presence of mirror symmetry further enhances the SHC. Beyond the high-SHC materials, 57 topological insulators with quantized SHCs have also been identified. Our work enables rapid screening and paves the way for experimental validation, potentially accelerating the discovery of novel 2D materials optimized for spintronics applications....

---

### 221. A Design Co-Pilot for Task-Tailored Manipulators

**Authors:** Jonathan Külz, Sehoon Ha, Matthias Althoff

**Published:** 2025-09-16

**Category:** cs.RO

**ID:** 2509.13077v1

**Link:** [http://arxiv.org/abs/2509.13077v1](http://arxiv.org/abs/2509.13077v1)

**Summary:** Although robotic manipulators are used in an ever-growing range of applications, robot manufacturers typically follow a ``one-fits-all'' philosophy, employing identical manipulators in various settings. This often leads to suboptimal performance, as general-purpose designs fail to exploit particularities of tasks. The development of custom, task-tailored robots is hindered by long, cost-intensive development cycles and the high cost of customized hardware. Recently, various computational design methods have been devised to overcome the bottleneck of human engineering. In addition, a surge of modular robots allows quick and economical adaptation to changing industrial settings. This work proposes an approach to automatically designing and optimizing robot morphologies tailored to a specific environment. To this end, we learn the inverse kinematics for a wide range of different manipulators. A fully differentiable framework realizes gradient-based fine-tuning of designed robots and inverse kinematics solutions. Our generative approach accelerates the generation of specialized designs from hours with optimization-based methods to seconds, serving as a design co-pilot that enables instant adaptation and effective human-AI collaboration. Numerical experiments show that our approach finds robots that can navigate cluttered environments, manipulators that perform well across a specified workspace, and can be adapted to different hardware constraints. Finally, we demonstrate the real-world applicability of our method by setting up a modular robot designed in simulation that successfully moves through an obstacle course....

---

### 222. Mesoscale FEM Model of Concrete: Statistical Assessment of Inherent Stress Concentrations in Dependence on Phase Heterogeneity

**Authors:** Jan Mašek, Petr Miarka

**Published:** 2025-06-19

**Category:** cond-mat.mtrl-sci

**ID:** 2506.16242v2

**Link:** [http://arxiv.org/abs/2506.16242v2](http://arxiv.org/abs/2506.16242v2)

**Summary:** Concrete heterogeneity originates from its production process, which involves bonding aggregates with a binder matrix. This study presents a mesoscale finite element model (MFEM) that offers detailed insights into the fracture process at the aggregate--cement matrix interface, focusing on one of concrete's key properties: its mechanical response. Unlike discrete models, which often average out critical stress concentrations within the mesostructure, the MFEM approach captures detailed stress distributions, revealing localized effects crucial for understanding damage evolution.
  Although computationally more demanding, the MFEM leverages modern high-performance computing (HPC) to provide a detailed description of the stress field and material damage across different phases and interfaces. The proposed modeling framework integrates a collision-checked aggregate generation procedure, Voronoi-based mesostructure construction, and adaptive 3D meshing, forming a reusable methodology for stress analysis in heterogeneous composites. This approach offers transparent, physically interpretable parameterization of phase properties in contrast to black-box discrete models.
  Another methodological contribution is the statistical post-processing of stress data using histogram-based analysis across cross-sectional planes. This enables quantitative evaluation of stress concentration distributions, providing valuable insights into the mesoscale mechanical response and serving as a useful visualization tool for researchers working on heterogeneous material modeling. Various matrix-to-aggregate stiffness ratios are considered to evaluate the influence of material heterogeneity on the stress field....

---

### 223. Bond-Network Entropy Governs Heat Transport in Coordination-Disordered Solids

**Authors:** Kamil Iwanowski, Gábor Csányi, Michele Simoncelli

**Published:** 2024-12-17

**Category:** cond-mat.mtrl-sci

**ID:** 2412.12753v3

**Link:** [http://arxiv.org/abs/2412.12753v3](http://arxiv.org/abs/2412.12753v3)

**Summary:** Understanding how the vibrational and thermal properties of solids are influenced by atomistic structural disorder is of fundamental scientific interest, and paramount to designing materials for next-generation energy technologies. While several studies indicate that structural disorder strongly influences the thermal conductivity, the fundamental physics governing the disorder-conductivity relation remains elusive. Here we show that order-of-magnitude, disorder-induced variations of conductivity in network solids can be predicted from a bond-network entropy, an atomistic structural descriptor that quantifies heterogeneity in the topology of the atomic-bond network. We employ the Wigner formulation of thermal transport to demonstrate the existence of a relation between the bond-network entropy, and observables such as smoothness of the vibrational density of states (VDOS) and macroscopic conductivity. We also show that the smoothing of the VDOS encodes information about the thermal resistance induced by disorder, and can be directly related to phenomenological models for phonon-disorder scattering based on the semiclassical Peierls-Boltzmann equation. Our findings rationalize the conductivity variations of disordered carbon polymorphs ranging from nanoporous electrodes to defective graphite used as a moderator in nuclear reactors....

---

### 224. Ferroelectric Fluids for Nonlinear Photonics: Evaluation of Temperature Dependence of Second-Order Susceptibilities

**Authors:** Matija Lovšin, Luka Cmok, Calum J. Gibb, Jordan Hobbs, Richard J. Mandle, Alenka Mertelj, Irena Drevenšek-Olenik, Nerea Sebastian

**Published:** 2025-09-15

**Category:** cond-mat.soft

**ID:** 2509.11835v1

**Link:** [http://arxiv.org/abs/2509.11835v1](http://arxiv.org/abs/2509.11835v1)

**Summary:** Ferroelectric nematic fluids are promising materials for tunable nonlinear photonics, with applications ranging from second harmonic generation to sources of entangled photons. However, the few reported values of second-order susceptibilities vary widely depending on the molecular architecture. Here, we systematically measure second-order NLO susceptibilities of five different materials that exhibit the ferroelectric nematic phase, as well as the more recently discovered layered smectic A ferroelectric phase. The materials investigated include archetypal molecular architectures as well as mixtures showing room-temperature ferroelectric phases. The measured values, which range from 0.3 to 20 pm/V, are here reasonably predicted by combining calculations of molecular-level hyperpolarizabilities and a simple nematic potential, highlighting the opportunities of modelling-assisted design for enhanced NLO ferroelectric fluids....

---

### 225. Generic continuum model formalism for moiré superlattice systems

**Authors:** Bo Xie, Jianqi Huang, Jianpeng Liu

**Published:** 2025-09-15

**Category:** cond-mat.mes-hall

**ID:** 2509.11747v1

**Link:** [http://arxiv.org/abs/2509.11747v1](http://arxiv.org/abs/2509.11747v1)

**Summary:** The moiré superlattice system provides an excellent platform for exploring various novel quantum phenomena. To theoretically tackle the diverse correlated and topological states emerging from moiré superlattices, one usually adopts an effective low-energy continuum model based on which the electron-electron effects are further considered. However, the construction of an accurate continuum model remains a challenging task, particularly for complex moiré superlattices such as twisted transition metal dichalcogenides. In this work, we develop a formalism for constructing generic continuum models that are in principle applicable for arbitrary moiré superlattices and are extrapolatable to any twist angles. Our key insight is that the microscopic electronic properties are intrinsic properties of the system, which should remain invariant across all twist angles; the lattice relaxations act as external inputs that vary with twist angles and are coupled with the electrons, and the coupling coefficients are characterized by intrinsic parameters. This partition enables a universal description of the angle variation of the continuum model using a single set of model parameters. To extract the model parameters, we design a numerical workflow based on data from first principles density functional theory calculations. We apply this framework to twisted bilayer MoTe$_{2}$, and obtain a single set of model parameters that accurately reproduce first-principles results, including electronic band structures, charge density distributions and Chern numbers, at three different twist angles. Furthermore, the model extrapolates robustly to smaller twist angles. Our work not only provides a more precise understanding of the microscopic properties of moiré superlattices, but also lays a foundation for future theoretical studies of low-energy electronic properties in generic moiré superlattice systems....

---

### 226. Nonlinear Hall Effects induced by Berry Curvature Dipole in CuPb$_9$(PO$_4$)$_6$O

**Authors:** Bishnu Karki, Kai Chen, Pavan Hosur

**Published:** 2024-02-06

**Category:** cond-mat.mtrl-sci

**ID:** 2402.18588v4

**Link:** [http://arxiv.org/abs/2402.18588v4](http://arxiv.org/abs/2402.18588v4)

**Summary:** The nonlinear Hall effect (NLHE), an emergent response in systems with broken inversion symmetry, provides a powerful tool for probing topological transport properties. In this context, we investigate copper-substituted lead apatite (LK-99), a material that initially garnered attention for its controversial claim of room-temperature superconductivity. Despite the unresolved nature of its superconducting properties, LK-99's unique electronic structure characterized by flat bands near the Fermi level and broken inversion symmetry makes it a promising candidate for exploring Berry curvature-driven phenomena, such as the NLHE. Using first-principles density functional theory and an augmented tight-binding Hamiltonian model, we investigate LK-99's band topology and transport properties. Our calculations indicate that spin-orbit coupling in LK-99 generates multiple Weyl points near the Fermi level, thereby enhancing the Berry curvature distribution by further splitting the bands. Crucially, the absence of inversion symmetry in LK-99 leads to a net Berry curvature dipole, producing a nonlinear Hall current that scales quadratically with the applied electric field. The nonlinear Hall effect is solely due to the BCD, as the contributions from the Drude weight and quantum metric are zero due to time reversal symmetry. Moreover, we demonstrate that the NLHE in LK-99 can be tuned by varying the direction of the applied electric field, underscoring its potential as a versatile platform for exploring topological transport phenomena and designing next-generation nonlinear electronic devices....

---

### 227. MatQnA: A Benchmark Dataset for Multi-modal Large Language Models in Materials Characterization and Analysis

**Authors:** Yonghao Weng, Liqiang Gao, Linwu Zhu, Jian Huang

**Published:** 2025-09-14

**Category:** cs.LG

**ID:** 2509.11335v1

**Link:** [http://arxiv.org/abs/2509.11335v1](http://arxiv.org/abs/2509.11335v1)

**Summary:** Recently, large language models (LLMs) have achieved remarkable breakthroughs in general domains such as programming and writing, and have demonstrated strong potential in various scientific research scenarios. However, the capabilities of AI models in the highly specialized field of materials characterization and analysis have not yet been systematically or sufficiently validated. To address this gap, we present MatQnA, the first multi-modal benchmark dataset specifically designed for material characterization techniques. MatQnA includes ten mainstream characterization methods, such as X-ray Photoelectron Spectroscopy (XPS), X-ray Diffraction (XRD), Scanning Electron Microscopy (SEM), Transmission Electron Microscopy (TEM), etc. We employ a hybrid approach combining LLMs with human-in-the-loop validation to construct high-quality question-answer pairs, integrating both multiple-choice and subjective questions. Our preliminary evaluation results show that the most advanced multi-modal AI models (e.g., GPT-4.1, Claude 4, Gemini 2.5, and Doubao Vision Pro 32K) have already achieved nearly 90% accuracy on objective questions in materials data interpretation and analysis tasks, demonstrating strong potential for applications in materials characterization and analysis. The MatQnA dataset is publicly available at https://huggingface.co/datasets/richardhzgg/matQnA....

---

### 228. Evolution of Kernels: Automated RISC-V Kernel Optimization with Large Language Models

**Authors:** Siyuan Chen, Zhichao Lu, Qingfu Zhang

**Published:** 2025-09-14

**Category:** cs.SE

**ID:** 2509.14265v1

**Link:** [http://arxiv.org/abs/2509.14265v1](http://arxiv.org/abs/2509.14265v1)

**Summary:** Automated kernel design is critical for overcoming software ecosystem barriers in emerging hardware platforms like RISC-V. While large language models (LLMs) have shown promise for automated kernel optimization, demonstrating success in CUDA domains with comprehensive technical documents and mature codebases, their effectiveness remains unproven for reference-scarce domains like RISC-V. We present Evolution of Kernels (EoK), a novel LLM-based evolutionary program search framework that automates kernel design for domains with limited reference material. EoK mitigates reference scarcity by mining and formalizing reusable optimization ideas (general design principles + actionable thoughts) from established kernel libraries' development histories; it then guides parallel LLM explorations using these ideas, enriched via Retrieval-Augmented Generation (RAG) with RISC-V-specific context, prioritizing historically effective techniques. Empirically, EoK achieves a median 1.27x speedup, surpassing human experts on all 80 evaluated kernel design tasks and improving upon prior LLM-based automated kernel design methods by 20%. These results underscore the viability of incorporating human experience into emerging domains and highlight the immense potential of LLM-based automated kernel optimization....

---

### 229. Bridging Structure and Activity in Nanocatalysts via Machine Learning and Global Structure Representations

**Authors:** Sofia Zinzani, Francesca Baletto, Kevin Rossi

**Published:** 2025-09-13

**Category:** cond-mat.mes-hall

**ID:** 2509.10985v1

**Link:** [http://arxiv.org/abs/2509.10985v1](http://arxiv.org/abs/2509.10985v1)

**Summary:** Establishing a mapping between nanocatalysts structure and their catalytic properties is essential for efficient design. To this end, we demonstrate the accuracy of a general machine learning framework on a representative and challenging application: predicting the mass activity of Pt nanoparticles for the electrochemical oxygen reduction reaction, estimated via a microkinetic model. Accurate models are obtained when leveraging either a nanocatalyst's structure representation accessible at the computational level, namely the surface site generalized coordination number distributions, or one accessible experimentally, namely the nanoparticle's pair distance distribution function. Building on this result, we demonstrate that our machine learning model, in tandem with Bayesian optimization, efficiently identifies the Top-10 and Top-100 most active structures out of a large pool of candidates comprising more than 50000 different structures, after probing the activity only of a few thousand structures. These findings provide a robust blueprint for accelerated theoretical and experimental identification of active nanocatalysts....

---

### 230. CaCd$_2$P$_2$: A Visible-Light Absorbing Zintl Phosphide Stable under Photoelectrochemical Water Oxidation

**Authors:** Guillermo L. Esparza, Zhenkun Yuan, Muhammad Rubaiat Hasan, Yagmur Coban, Gideon Kassa, Vivek Shastry Devalla, Tejas Nivarty, Jack R. Palmer, Jifeng Liu, Kirill Kovnir, Geoffroy Hautier, David P Fenning

**Published:** 2025-09-11

**Category:** cond-mat.mtrl-sci

**ID:** 2509.09803v1

**Link:** [http://arxiv.org/abs/2509.09803v1](http://arxiv.org/abs/2509.09803v1)

**Summary:** A key bottleneck to solar fuels is the absence of stable and strongly absorbing photoelectrode materials for the oxygen evolution reaction (OER). Modern approaches generally trade off between stable but weakly absorbing materials, such as wide bandgap oxides, or strongly absorbing materials that rely on encapsulation for stability and are weakly catalytic, such as the III-V family of semiconductors. Of interest are materials like transition metal phosphides, such as FeP$_2$, that are known to undergo beneficial in situ surface transformations in the oxidative environment of OER, though stability has remained a primary hurdle. Here we report on CaCd$_2$P$_2$, a Zintl phase visible-light absorber with favorable 1.6 eV bandgap, that we identified using high-throughput computational screening. Using a combination of photoelectrochemical measurements, microscopy, and spectroscopy, we show that CaCd$_2$P$_2$ undergoes a light-stabilized surface transformation that renders it stable under alkaline OER conditions. We also show that the well known OER catalyst CoPi can act as a stable co-catalyst in synergy with the \textit{in-situ} CaCd$_2$P$_2$ surface. The light-induced stabilization that CaCd$_2$P$_2$ displays is in sharp contrast to the photocorrosion commonly observed in visible light-absorbing photoelectrodes. The broader AM$_2$P$_2$ family of Zintl phases offers a significant opportunity to explore stabilizing interface chemistry and re-design the manner in which low-bandgap semiconductors are used for photoelectrochemical energy conversion....

---

### 231. Ultra-Efficient Reconstruction of Anisotropic Hyperuniform Continuous Random Fields in 2D and 3D via Generalized Spectral Filtering

**Authors:** Liyu Zhong, Sheng Mao

**Published:** 2025-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2509.08675v1

**Link:** [http://arxiv.org/abs/2509.08675v1](http://arxiv.org/abs/2509.08675v1)

**Summary:** Hyperuniform continuous random fields suppress large-scale fluctuations while preserving rich local disorder, making them highly attractive for next-generation photonic, thermal and mechanical materials. However, traditional reconstruction techniques often suffer from limited spectral control or excessive computational cost, especially in high-resolution 2D and 3D settings. In this work, we present an ultra-efficient generative algorithm based on generalized superellipse spectral filtering, which allows independent tuning of isotropic and anisotropic spectral envelopes without resorting to costly iterative schemes. We demonstrate our method on a comprehensive set of 2D and 3D examples, showing precise manipulation of spectral band shape and orders-of-magnitude speedup compared to existing approaches. Furthermore, we explore the effect of simple thresholding on the generated fields, analyzing the morphological features and power-spectrum characteristics of the resulting two-phase maps. Our results confirm that the proposed framework not only accelerates hyperuniform field synthesis but also provides a versatile platform for systematic study of binary microstructures derived from continuous designs. This work opens new avenues for large-scale simulation and optimized design of advanced hyperuniform materials....

---

### 232. Ultrafast Spin Injection in Graphene via Dynamical Carrier Filtering at Transition Metal Dichalcogenide Interfaces

**Authors:** Shunsuke Yamada, Arqum Hashmi, Tomohito Otobe

**Published:** 2025-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2509.08339v1

**Link:** [http://arxiv.org/abs/2509.08339v1](http://arxiv.org/abs/2509.08339v1)

**Summary:** We report a real-time first-principles study of ultrafast spin injection in a WSe$_2$-graphene heterobilayer under circularly polarized laser irradiation, using time-dependent density functional theory. Contrary to conventional expectations, spin transfer into graphene is not a passive process but is actively driven by spin-selective carrier filtering at the interface. Spin-polarized carriers generated in the WSe$_2$ layer induce a preferential migration of opposite-spin carriers from graphene, which results in net spin magnetization in graphene. This process is governed by interlayer band offsets, density-of-state asymmetry, and Pauli blocking. These findings indicate a microscopic mechanism of spin injection in non-magnetic systems and identify a guiding principle for the design of ultrafast opto-spintronic functionalities in van der Waals heterostructures....

---

### 233. Percolation Diagrams Derived from First-Principles Investigation of Chemical Short-Range Order in Binary Alloys

**Authors:** Abhinav Roy, Karl Sieradzki, Michael J. Waters, James M. Rondinelli, Ian D. McCue

**Published:** 2025-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2509.08253v1

**Link:** [http://arxiv.org/abs/2509.08253v1](http://arxiv.org/abs/2509.08253v1)

**Summary:** Recent developments in the percolation theory of passivation have shown that chemical short-range order (SRO) affects the aqueous passivation behavior of alloys. However, there has been no systematic exploration to quantify these SRO effects on percolation in practical alloys and the related passivation behavior. In this study, we quantify the effects of SRO on percolation in a binary size-mismatched Cu-Rh alloy and study the related passivation behavior. We develop a mixed-space cluster expansion model trained on the mixing energy calculated using density functional theory. We use the cluster expansion model to sample the configuration space via variance-constrained semi-grand canonical Monte Carlo simulations and develop SRO diagrams over a range of compositions and temperatures. Building on this with the percolation crossover model, specifically the variation of percolation threshold with SRO in the FCC lattice, we construct the first nearest-neighbor chemical percolation diagram. These diagrams can inform the design of the next generation of corrosion-resistant metallic alloys....

---

### 234. MDDM: A Molecular Dynamics Diffusion Model to Predict Particle Self-Assembly

**Authors:** Kevin Ferguson, Yu-hsuan Chen, Levent Burak Kara

**Published:** 2025-01-28

**Category:** cs.LG

**ID:** 2501.17319v3

**Link:** [http://arxiv.org/abs/2501.17319v3](http://arxiv.org/abs/2501.17319v3)

**Summary:** The discovery and study of new material systems rely on molecular simulations that often come with significant computational expense. We propose MDDM, a Molecular Dynamics Diffusion Model, which is capable of predicting a valid output conformation for a given input pair potential function. After training MDDM on a large dataset of molecular dynamics self-assembly results, the proposed model can convert uniform noise into a meaningful output particle structure corresponding to an arbitrary input potential. The model's architecture has domain-specific properties built-in, such as satisfying periodic boundaries and being invariant to translation. The model significantly outperforms the baseline point-cloud diffusion model for both unconditional and conditional generation tasks....

---

### 235. Molecular-Size Control of Properties of Therapeutic Nano-Paper Allows for Selective Drug Storage in Small Doses

**Authors:** Elisabeth Erbes, Naireeta Biswas, Calvin J. Gavilett, Matthias Schwartzkopf, Krishnayan Basuroy, Qing Chen, Andrei Chumakov, Susann Frenzke, Marc Gensch, Korneliya Goordeyeva, Patrycja Kielb, Sonja Kirchner, Volker Körstgens, Peter Müller-Buschbaum, Henrike M. Müller-Werkmeister, Jan Rubeck, Sreevidya Thekku Veedu, Jose de Jesus Velazquez-Garcia, Vivian Waclawek, Daniel Söderberg, Stephan V. Roth, Simone Techert

**Published:** 2025-09-09

**Category:** physics.med-ph

**ID:** 2509.08019v1

**Link:** [http://arxiv.org/abs/2509.08019v1](http://arxiv.org/abs/2509.08019v1)

**Summary:** A novel concept of nano-scaled interwoven templates for drug delivery with alternating hydro- and lipophilicity properties is introduced. They are built from cellulose and peptide hydrogel in tandem, and characterized by a nano-stacked interwoven design, thus enabling for tuning the lipophilicity in the mesh nano-domains in which drug candidates of complementary lipophilicities can be embedded. This allows for low-dose-controlled consumption and therapeutic applications. Time-resolved and in-situ grazing incidence X-ray scattering studies confirm the design of the therapeutic nano-paper and create conditions suitable for the drug storage of complementary properties. The molecular design has the potential of a locally controlled, site-specific drug release on a beyond-nanomolar scale. Generalized, the design may contribute to facile developments of personalized medicine....

---

### 236. 3D Mapping of Defects and Moiré Corrugations via Electron Ptychography Atomic Coordinate Retrieval

**Authors:** Jeffrey Huang, Yichao Zhang, Sang hyun Bae, Ballal Ahammed, Elif Ertekin, Pinshane Y. Huang

**Published:** 2025-09-08

**Category:** cond-mat.mtrl-sci

**ID:** 2509.07140v1

**Link:** [http://arxiv.org/abs/2509.07140v1](http://arxiv.org/abs/2509.07140v1)

**Summary:** Defects and reconstructions in 2D moiré materials cause out-of-plane deformations which strongly modify their electronic properties but are difficult to experimentally access. Here, we solve the 3D atomic coordinates of twisted bilayer WSe$_2$ with picometer-scale accuracy using multislice electron ptychography (MEP) acquired from a single orientation. The resulting atomic models individually visualize each of the six atomic planes, revealing the curvature of each WSe$_2$ layer, variations in the interlayer spacing, and the 3D locations of individual vacancies -- which lie exclusively in the outer Se planes. We also observe a new, unexpected type of structural disorder consisting of mixed bending -- and breathing-type moiré-induced corrugations that should strongly impact the emergent electronic properties. Broadly, our methods generate 3D atom-by-atom models of a 2D heterointerface from data acquired in about 30 seconds, methods that should unlock routine access to 3D atomic information in 2D systems and catalyze design methods to control out-of-plane deformations....

---

### 237. Edgetronics in Two-Dimensional Altermagnets

**Authors:** Shibo Fang, Zongmeng Yang, Jianhua Wang, Xingyue Yang, Jing Lu, Ching Hua Lee, Xiaotian Wang, Yee Sin Ang

**Published:** 2025-08-14

**Category:** cond-mat.mes-hall

**ID:** 2508.10451v5

**Link:** [http://arxiv.org/abs/2508.10451v5](http://arxiv.org/abs/2508.10451v5)

**Summary:** The coupling between real-space inhomogeneities coordinates and spin (r-s) provides an alternative route to achieve efficient spin manipulation in spintronics beyond the conventional momentum-spin (k-s) coupling paradigm. Here we demonstrate an unexpected manifestation of one-dimensional (1D) r-s coupling in two-dimensional (2D) altermagnetic second-order topological insulators, where the spin-split floating edge states -- energetically isolated within the bulk band gap -- emerge and exhibit both Neel-vector-dependent and electrically tunable behaviors. The 1D edge-spin r-s coupling ensures carrier transport to be exclusively carried by the edge states with quantized spin conductance, giving rise to an unconventional edge tunnel magnetoresistance (edge-TMR) effect that can be switched On or Off. As a proof of concept, we computationally design an edge-TMR device based on Cr_2Se_2O monolayer to demonstrate its edge transportation and controllability via the Néel order or electric field. Our findings propose a general prototype altermagnetic device for next-generation low-dimensional spintronics....

---

### 238. An All-Atom Generative Model for Designing Protein Complexes

**Authors:** Ruizhe Chen, Dongyu Xue, Xiangxin Zhou, Zaixiang Zheng, Xiangxiang Zeng, Quanquan Gu

**Published:** 2025-04-17

**Category:** cs.LG

**ID:** 2504.13075v3

**Link:** [http://arxiv.org/abs/2504.13075v3](http://arxiv.org/abs/2504.13075v3)

**Summary:** Proteins typically exist in complexes, interacting with other proteins or biomolecules to perform their specific biological roles. Research on single-chain protein modeling has been extensively and deeply explored, with advancements seen in models like the series of ESM and AlphaFold2. Despite these developments, the study and modeling of multi-chain proteins remain largely uncharted, though they are vital for understanding biological functions. Recognizing the importance of these interactions, we introduce APM (All-Atom Protein Generative Model), a model specifically designed for modeling multi-chain proteins. By integrating atom-level information and leveraging data on multi-chain proteins, APM is capable of precisely modeling inter-chain interactions and designing protein complexes with binding capabilities from scratch. It also performs folding and inverse-folding tasks for multi-chain proteins. Moreover, APM demonstrates versatility in downstream applications: it achieves enhanced performance through supervised fine-tuning (SFT) while also supporting zero-shot sampling in certain tasks, achieving state-of-the-art results. We released our code at https://github.com/bytedance/apm....

---

### 239. Deformation Driven Suction Cups: A Mechanics-Based Approach to Wearable Electronics

**Authors:** Seola Lee, Andrew Akerson, Roham Pardakhtim, Ehsan Hajiesmaili, Kevin Rhodes, Zidong Li, Andrew Stanley, Amirhossein Amini, Daniele Piazza, Chiara Daraio, Tianshu Liu

**Published:** 2025-08-15

**Category:** physics.med-ph

**ID:** 2508.11838v2

**Link:** [http://arxiv.org/abs/2508.11838v2](http://arxiv.org/abs/2508.11838v2)

**Summary:** Wearable electronics are emerging as essential tools for health monitoring, haptic feedback, and human-computer interactions. While stable contact at the device-body interface is critical for these applications, it remains challenging due to the skin's softness, roughness, and mechanical variability. Existing methods, such as grounding structures or adhesive tapes, often suffer from contact loss, limited repeatability, and restrictions on the types of electronics they can support. Suction-based adhesives offer a promising alternative by generating negative pressure without requiring tight bands or chemical adhesives. However, most existing cup designs rely on rigid-surface assumptions and overlook mechanical interactions between suction cups and skin. Inspired by traditional cupping therapies, we present a suction-based adhesive system that attaches through elastic deformation and recovery. Using analytical modeling, numerical simulations, and experiments, we present a mechanics-based framework showing how suction performance depends on cup geometry, substrate compliance, and interfacial adhesion. We show that cup geometry should be tailored to substrate stiffness. Wide, flat suction cups perform well on rigid surfaces but fail on soft ones like skin due to substrate intrusion into the chamber. Narrow and tall domes better preserve recoverable volume and generate stronger suction. To improve sealing on rough, dry skin, we introduce a soft, tacky interfacial layer informed by a contact mechanics model. Using our design principles for skin suction adhesives, we demonstrate secure attachment of rigid and flexible components including motion sensors, haptic actuators, and electrophysiological electrodes across diverse anatomical regions. These findings provide a fundamental basis for designing the next generation of skin-friendly adhesives for wearable electronics....

---

### 240. Bulk Ferroelectric Heterostructures: Imprinted Actuators

**Authors:** Yizhe Li, Ziqi Yang, Ying Chen, Zhenbo Zhang, Yun-Long Tang, Annette K. Kleppe, Egor Koemets, Xuezhen Cao, Steven J. Milne, Juncheng Pan, Jiajun Shi, Yuge Yang, David A. Hall

**Published:** 2025-09-07

**Category:** cond-mat.mtrl-sci

**ID:** 2509.06177v1

**Link:** [http://arxiv.org/abs/2509.06177v1](http://arxiv.org/abs/2509.06177v1)

**Summary:** Domain switching is the cornerstone of ferroelectric materials. Most associated functionalities can be tuned via domain switching, including but not limited to piezoelectricity, thermal conductivity, domain wall conductivity and topological structures. However, achieving the full potential of reversible ferroelectric domain switching is restricted by the incomplete access to the entire ferroelectric texture space, as well as the memory effects and energy dissipation associated with the hysteretic nature of ferroelectrics. The manipulation of domain switching behaviour is moderately attainable in epitaxial heterostructures by exploiting the valence or lattice mismatch at heterointerfaces, which is generally constrained by the necessity for two dimensional architectures. In this study, domain-engineered bulk ferroelectric heterostructures (DE-BFH), constructed via elemental partitioning, are employed to unleash full potential of bulk ferroelectrics, providing comprehensive control of domain switching characteristics and adjustable reversibility within the entire range of ferroelectric texture space. Exemplar DE-BFH ceramics exhibit unprecedented enhancement in reversible electrostrain and stability in both axial and shear modes, including a record high peak to peak shear strain up to 0.9% at intermediate field levels, confirmed by digital image correlation measurements and in-situ synchrotron XRD studies. The advancement of domain switching behaviour in DE-BFH could also promote development of new types of lead-free piezoelectric devices, including actuators, energy harvesters, multiple state memory devices, and domain wall switch. Moreover, design concept of DE-BFH could contribute to the creation of distinctive ferroelastic, ferromagnetic, and multiferroic materials by broadening its scope to the entire ferroic family, encompassing polycrystalline, single-crystal, and thin-film forms....

---

### 241. Accelerated Design of Mechanically Hard Magnetically Soft High-entropy Alloys via Multi-objective Bayesian Optimization

**Authors:** Mian Dai, Yixuan Zhang, Weijia He, Chen Shen, Xiaoqing Li, Stephan Schönecker, Liuliu Han, Ruiwen Xie, Tianhang Zhou, Hongbin Zhang

**Published:** 2025-09-06

**Category:** cond-mat.mtrl-sci

**ID:** 2509.05702v1

**Link:** [http://arxiv.org/abs/2509.05702v1](http://arxiv.org/abs/2509.05702v1)

**Summary:** Designing high-entropy alloys (HEAs) that are both mechanically hard and possess soft magnetic properties is inherently challenging, as a trade-off is needed for mechanical and magnetic properties. In this study, we optimize HEA compositions using a multi-objective Bayesian optimization (MOBO) framework to achieve simultaneous optimal mechanical and magnetic properties. An ensemble surrogate model is constructed to enhance the accuracy of machine learning surrogate models, while an efficient sampling strategy combining Monte Carlo sampling and acquisition function is applied to explore the high-dimensional compositional space. The implemented MOBO strategy successfully identifies Pareto-optimal compositions with enhanced mechanical and magnetic properties. The ensemble model provides robust and reliable predictions, and the sampling approach reduces the likelihood of entrapment in local optima. Our findings highlight specific elemental combinations that meet the dual design objectives, offering guidance for the synthesis of next-generation HEAs....

---

### 242. Causal Multi-fidelity Surrogate Forward and Inverse Models for ICF Implosions

**Authors:** Tyler E. Maltba, Ben S. Southworth, Jeffrey R. Haack, Marc L. Klasky

**Published:** 2025-09-05

**Category:** physics.comp-ph

**ID:** 2509.05510v1

**Link:** [http://arxiv.org/abs/2509.05510v1](http://arxiv.org/abs/2509.05510v1)

**Summary:** Continued progress in inertial confinement fusion (ICF) requires solving inverse problems relating experimental observations to simulation input parameters, followed by design optimization. However, such high dimensional dynamic PDE-constrained optimization problems are extremely challenging or even intractable. It has been recently shown that inverse problems can be solved by only considering certain robust features. Here we consider the ICF capsule's deuterium-tritium (DT) interface, and construct a causal, dynamic, multifidelity reduced-order surrogate that maps from a time-dependent radiation temperature drive to the interface's radius and velocity dynamics. The surrogate targets an ODE embedding of DT interface dynamics, and is constructed by learning a controller for a base analytical model using low- and high-fidelity simulation training data with respect to radiation energy group structure. After demonstrating excellent accuracy of the surrogate interface model, we use machine learning (ML) models with surrogate-generated data to solve inverse problems optimizing radiation temperature drive to reproduce observed interface dynamics. For sparse snapshots in time, the ML model further characterizes the most informative times at which to sample dynamics. Altogether we demonstrate how operator learning, causal architectures, and physical inductive bias can be integrated to accelerate discovery, design, and diagnostics in high-energy-density systems....

---

### 243. A Comparison of Surrogate Constitutive Models for Viscoplastic Creep Simulation of HT-9 Steel

**Authors:** Pieterjan Robbe, Andre Ruybalid, Arun Hegde, Christophe Bonneville, Habib N Najm, Laurent Capolungo, Cosmin Safta

**Published:** 2025-09-05

**Category:** physics.comp-ph

**ID:** 2509.22667v1

**Link:** [http://arxiv.org/abs/2509.22667v1](http://arxiv.org/abs/2509.22667v1)

**Summary:** Mechanistic microstructure-informed constitutive models for the mechanical response of polycrystals are a cornerstone of computational materials science. However, as these models become increasingly more complex - often involving coupled differential equations describing the effect of specific deformation modes - their associated computational costs can become prohibitive, particularly in optimization or uncertainty quantification tasks that require numerous model evaluations. To address this challenge, surrogate constitutive models that balance accuracy and computational efficiency are highly desirable. Data-driven surrogate models, that learn the constitutive relation directly from data, have emerged as a promising solution. In this work, we develop two local surrogate models for the viscoplastic response of a steel: a piecewise response surface method and a mixture of experts model. These surrogates are designed to adapt to complex material behavior, which may vary with material parameters or operating conditions. The surrogate constitutive models are applied to creep simulations of HT-9 steel, an alloy of considerable interest to the nuclear energy sector due to its high tolerance to radiation damage, using training data generated from viscoplastic self-consistent (VPSC) simulations. We define a set of test metrics to numerically assess the accuracy of our surrogate models for predicting viscoplastic material behavior, and show that the mixture of experts model outperforms the piecewise response surface method in terms of accuracy....

---

### 244. Scalable Unit Harmonization in Medical Informatics via Bayesian-Optimized Retrieval and Transformer-Based Re-ranking

**Authors:** Jordi de la Torre

**Published:** 2025-05-01

**Category:** cs.LG

**ID:** 2505.00810v3

**Link:** [http://arxiv.org/abs/2505.00810v3](http://arxiv.org/abs/2505.00810v3)

**Summary:** Objective: To develop and evaluate a scalable methodology for harmonizing inconsistent units in large-scale clinical datasets, addressing a key barrier to data interoperability.
  Materials and Methods: We designed a novel unit harmonization system combining BM25, sentence embeddings, Bayesian optimization, and a bidirectional transformer based binary classifier for retrieving and matching laboratory test entries. The system was evaluated using the Optum Clinformatics Datamart dataset (7.5 billion entries). We implemented a multi-stage pipeline: filtering, identification, harmonization proposal generation, automated re-ranking, and manual validation. Performance was assessed using Mean Reciprocal Rank (MRR) and other standard information retrieval metrics.
  Results: Our hybrid retrieval approach combining BM25 and sentence embeddings (MRR: 0.8833) significantly outperformed both lexical-only (MRR: 0.7985) and embedding-only (MRR: 0.5277) approaches. The transformer-based reranker further improved performance (absolute MRR improvement: 0.10), bringing the final system MRR to 0.9833. The system achieved 83.39\% precision at rank 1 and 94.66\% recall at rank 5.
  Discussion: The hybrid architecture effectively leverages the complementary strengths of lexical and semantic approaches. The reranker addresses cases where initial retrieval components make errors due to complex semantic relationships in medical terminology.
  Conclusion: Our framework provides an efficient, scalable solution for unit harmonization in clinical datasets, reducing manual effort while improving accuracy. Once harmonized, data can be reused seamlessly in different analyses, ensuring consistency across healthcare systems and enabling more reliable multi-institutional studies and meta-analyses....

---

### 245. Universal Scaling Formalism and Analytical Optimization Criterion for Multiscale Geometric Design of Thermoelectric Metamaterials

**Authors:** Xanthippi Zianni

**Published:** 2025-09-05

**Category:** physics.app-ph

**ID:** 2509.05095v1

**Link:** [http://arxiv.org/abs/2509.05095v1](http://arxiv.org/abs/2509.05095v1)

**Summary:** Thermoelectric (TE) generators can directly convert heat into electricity, but their performance is often constrained by limited temperature gradients. Here it is shown that width-modulated metamaterials with constrictions and expansions (constricted geometries) enhance temperature difference DT by reduced Transmissivity (Tr), a geometry-based parameter defined by the ratio of constriction to expansion cross-sections. A universal scaling behavior of transport and key TE efficiency metrics with Transmissivity is demonstrated, spanning from the nanoscale to the macroscale. Analytical formalism validated through finite element calculations for a range of modulation geometries reveals that DT, electrical and thermal resistances, efficiency, and power output are governed by a single scaling function, g(Tr), independent of carrier type, material, or operating conditions. This function represents the conductance of a constricted geometry relative to a uniform-width counterpart. The developed framework yields TE Performance Design Maps and an analytical criterion for optimal TE performance, with the maximum power density achieved at an optimal Transmissivity Tr_opt, determined by the condition that the functional g(Tr_opt) equals the Biot number, the dimensionless ratio hL/k of the convection coefficient h, the structure length L and the material thermal conductivity k. Transmissivity is established as a robust, multiscale design parameter - analogous to nature's hierarchical structures for optimized functionality. This work provides the theoretical framework for multiscale design and optimization of constricted geometries, thereby enabling systematic exploration of design strategies for next-generation TE modules based on advanced thermoelectric metamaterials....

---

### 246. A rediscovery of stiff pentmodes. A comment on "High bulk modulus pentamodes: the three-dimensional metal water"

**Authors:** Graeme W. Milton

**Published:** 2025-07-20

**Category:** physics.app-ph

**ID:** 2507.15014v2

**Link:** [http://arxiv.org/abs/2507.15014v2](http://arxiv.org/abs/2507.15014v2)

**Summary:** We bring attention to the fact that the claim of Brambilla et.al. [Extreme Mechanics Letters 74 (2025) 102267; arXiv:2406.14502] of discovering a novel design for pentamode materials is incorrect. Back in 2016 Briane, Harutyunyan and myself [Mathematics and Mechanics of Complex Systems 5 (2016) 41--94; arXiv:1606.03305] designed a class of stiff pentamodes, that include the high bulk modulus pentamodes of Brambilla et.al. Our design generalized to three-dimensions, and to full anisotropy, the main aspects of a two-dimensional construction of Sigmund [Journal of the Mechanics and Physics of Solids 48 (2000) 397--428]. It is emphasized that the in depth analysis of Brambilla et.al. goes well beyond our brief treatment....

---

### 247. LOTS of Fashion! Multi-Conditioning for Image Generation via Sketch-Text Pairing

**Authors:** Federico Girella, Davide Talon, Ziyue Liu, Zanxi Ruan, Yiming Wang, Marco Cristani

**Published:** 2025-07-30

**Category:** cs.CV

**ID:** 2507.22627v2

**Link:** [http://arxiv.org/abs/2507.22627v2](http://arxiv.org/abs/2507.22627v2)

**Summary:** Fashion design is a complex creative process that blends visual and textual expressions. Designers convey ideas through sketches, which define spatial structure and design elements, and textual descriptions, capturing material, texture, and stylistic details. In this paper, we present LOcalized Text and Sketch for fashion image generation (LOTS), an approach for compositional sketch-text based generation of complete fashion outlooks. LOTS leverages a global description with paired localized sketch + text information for conditioning and introduces a novel step-based merging strategy for diffusion adaptation. First, a Modularized Pair-Centric representation encodes sketches and text into a shared latent space while preserving independent localized features; then, a Diffusion Pair Guidance phase integrates both local and global conditioning via attention-based guidance within the diffusion model's multi-step denoising process. To validate our method, we build on Fashionpedia to release Sketchy, the first fashion dataset where multiple text-sketch pairs are provided per image. Quantitative results show LOTS achieves state-of-the-art image generation performance on both global and localized metrics, while qualitative examples and a human evaluation study highlight its unprecedented level of design customization....

---

### 248. Expanding the search space of high entropy oxides and predicting synthesizability using machine learning interatomic potentials

**Authors:** Oliver A. Dicks, Solveig S. Aamlid, Alannah M. Hallas, Joerg Rottler

**Published:** 2025-08-18

**Category:** cond-mat.mtrl-sci

**ID:** 2508.13389v2

**Link:** [http://arxiv.org/abs/2508.13389v2](http://arxiv.org/abs/2508.13389v2)

**Summary:** We propose an efficient computational methodology for predicting the synthesizability of high entropy oxides (HEOs) in a large space of possible candidate compounds. HEOs are a growing field with an enormous potential chemical composition space, and yet the discovery of new HEOs is slow and driven by experimental trial-and-error. In this work, we attempt to speed up this process by using a machine learned interatomic potential offering DFT-level accuracy. Our methodology starts by identifying a set of crystal structures and elements for screening, building a large random unit cell of each composition and structure, then relaxing this structure. The most promising candidates are distinguished based on the variance of the individual cation energies, which we introduce as our entropy descriptor, and the enthalpy of mixing, which is used as the enthalpy descriptor. The approach is applied to tetravalent HEOs, and its validity is confirmed by comparison to alternative descriptors and DFT calculations for a set of 7 elements. The search is then extended to a set of 14 elements and three crystal structures, where it successfully identifies the only known stable 4-component HEO in the $α$-PbO$_2$ structure, as well as predicting several new 5-component candidate systems. This approach can straightforwardly be applied to new sets of elements and structures, allowing for the accelerated discovery of new HEOs....

---

### 249. The Enduring Relevance of Semiempirical Quantum Mechanics

**Authors:** Jonathan E. Moussa

**Published:** 2025-05-19

**Category:** physics.chem-ph

**ID:** 2505.13424v3

**Link:** [http://arxiv.org/abs/2505.13424v3](http://arxiv.org/abs/2505.13424v3)

**Summary:** The development of semiempirical models to simplify quantum mechanical descriptions of atomistic systems is a practice that started soon after the discovery of quantum mechanics and continues to the present day. There are now many methods for atomistic simulation with many software implementations and many users, on a scale large enough to be considered as a software market. Semiempirical models occupied a large share of this market in its early days, but the research activity in atomistic simulation has steadily polarized over the last three decades towards general-purpose but expensive ab initio quantum mechanics methods and fast but special-purpose molecular mechanics methods. I offer perspective on recent trends in atomistic simulation from the middle ground of semiempirical modeling, to learn from its past success and consider its possible paths to future growth. In particular, there is a lot of ongoing research activity in combining semiempirical quantum mechanics with machine learning models and some unrealized possibilities of tighter integration between ab initio and semiempirical quantum mechanics with more flexible theoretical frameworks and more modular software components....

---

### 250. LATINO-PRO: LAtent consisTency INverse sOlver with PRompt Optimization

**Authors:** Alessio Spagnoletti, Jean Prost, Andrés Almansa, Nicolas Papadakis, Marcelo Pereyra

**Published:** 2025-03-16

**Category:** cs.CV

**ID:** 2503.12615v2

**Link:** [http://arxiv.org/abs/2503.12615v2](http://arxiv.org/abs/2503.12615v2)

**Summary:** Text-to-image latent diffusion models (LDMs) have recently emerged as powerful generative models with great potential for solving inverse problems in imaging. However, leveraging such models in a Plug & Play (PnP), zero-shot manner remains challenging because it requires identifying a suitable text prompt for the unknown image of interest. Also, existing text-to-image PnP approaches are highly computationally expensive. We herein address these challenges by proposing a novel PnP inference paradigm specifically designed for embedding generative models within stochastic inverse solvers, with special attention to Latent Consistency Models (LCMs), which distill LDMs into fast generators. We leverage our framework to propose LAtent consisTency INverse sOlver (LATINO), the first zero-shot PnP framework to solve inverse problems with priors encoded by LCMs. Our conditioning mechanism avoids automatic differentiation and reaches SOTA quality in as little as 8 neural function evaluations. As a result, LATINO delivers remarkably accurate solutions and is significantly more memory and computationally efficient than previous approaches. We then embed LATINO within an empirical Bayesian framework that automatically calibrates the text prompt from the observed measurements by marginal maximum likelihood estimation. Extensive experiments show that prompt self-calibration greatly improves estimation, allowing LATINO with PRompt Optimization to define new SOTAs in image reconstruction quality and computational efficiency. The code is available at https://latino-pro.github.io...

---

### 251. Van der Waals Density Functional for Molecular Crystals

**Authors:** Trevor Jenkins, Kristian Berland, Timo Thonhauser

**Published:** 2025-09-02

**Category:** cond-mat.mtrl-sci

**ID:** 2509.02358v1

**Link:** [http://arxiv.org/abs/2509.02358v1](http://arxiv.org/abs/2509.02358v1)

**Summary:** Since the development of the nonlocal correlation functional vdW-DF, the family of van der Waals density functionals has grown to better describe a wide variety of systems. A recent generation of the vdW-DF family, vdW-DF3, featured a newly-constructed form of the nonlocal correlation that more accurately modeled molecular dimers, layered structures, and surface adsorption. However, it also revealed an intrinsic tradeoff in vdW-DF3's parametrization and inflexibility of exchange in the generalized gradient approximation (GGA), limiting its accuracy for molecular crystals. In this paper we propose a new optimization of vdW-DF3 that is tailored to 3D molecular crystals. This functional, called vdW-DF3-mc, contains a new, tunable form of the exchange enhancement factor with parameters that directly correspond to physically relevant qualities. In addition, within the nonlocal correlation, we prioritize smoothness of the kernel switching function as a means of restoring flexibility to vdW-DF3's design. Testing vdW-DF3-mc on several benchmark sets, we achieve highly accurate energetics and geometries for molecular crystals. This is particularly evident for the case of polymorphs of ice, for which errors in the volume and cohesive energy are on the order of only 1%, indicating very promising performance for important subcategories of molecular crystals, such as polymorphism and hydrogen-bonded solids....

---

### 252. Improving atomic force microscopy structure discovery via style-translation

**Authors:** Jie Huang, Niko Oinonen, Fabio Priante, Filippo Federici Canova, Lauri Kurki, Chen Xu, Adam S. Foster

**Published:** 2025-09-02

**Category:** cond-mat.mtrl-sci

**ID:** 2509.02240v1

**Link:** [http://arxiv.org/abs/2509.02240v1](http://arxiv.org/abs/2509.02240v1)

**Summary:** Atomic force microscopy (AFM) is a key tool for characterising nanoscale structures, with functionalised tips now offering detailed images of the atomic structure. In parallel, AFM simulations using the particle probe model provide a cost-effective approach for rapid AFM image generation. Using state-of-the-art machine learning models and substantial simulated datasets, properties such as molecular structure, electrostatic potential, and molecular graph can be predicted from AFM images. However, transferring model performance from simulated to experimental AFM images poses challenges due to the subtle variations in real experimental data compared to the seemingly flawless simulations. In this study, we explore style translation to augment simulated images and improve the predictive performance of machine learning models in surface property analysis. We reduce the style gap between simulated and experimental AFM images and demonstrate the method's effectiveness in enhancing structure discovery models through local structural property distribution comparisons. This research presents a novel approach to improving the efficiency of machine learning models in the absence of labelled experimental data....

---

### 253. Microscopic Theory of Light-Induced Coherent Phonons Mediated by Quantum Geometry

**Authors:** Jiaming Hu, Zhichao Guo, Wenbin Li, Hua Wang, Kai Chang

**Published:** 2025-08-05

**Category:** cond-mat.mes-hall

**ID:** 2508.03257v2

**Link:** [http://arxiv.org/abs/2508.03257v2](http://arxiv.org/abs/2508.03257v2)

**Summary:** Light-induced coherent phonons provide a powerful platform for ultrafast control of material properties. However, the microscopic theory and quantum geometric nature of this phenomenon remain underexplored. Here, we develop a fully quantum-mechanical framework based on Feynman diagrams to systematically describe the generation of coherent phonons by light. We identify a dominant second-order, double-resonant process in noncentrosymmetric semiconductors that efficiently couples light to both electronic and phononic excitations. Crucially, we uncover the quantum geometric origin, encoded in the electron-phonon coupling (EPC) shift vector and the EPC quantum geometric tensor. Applying our theory to ferroelectric BaTiO$_3$ and SnSe, we demonstrate the potential for light-induced modulation of ferroelectric polarization driven by coherent phonons. This work provides fundamental insights for designing efficient optical control strategies for both coherent phonons and ferroelectric polarization....

---

### 254. Wetting Interactions Between Porous Carbon Hosts and Liquid Sodium-Potassium Alloys Toward Their Use in Negative Electrodes of Alkali-Metal Batteries

**Authors:** Johannes Baller, André Hilger, Naiyu Qi, Chiara Morini, Andrea Cornelio, Arndt Remhof, Markus Osenberg, Ingo Manke, Julian Moosmann, Felix Beckmann, Gustav Graeber

**Published:** 2025-09-01

**Category:** cond-mat.soft

**ID:** 2509.05336v1

**Link:** [http://arxiv.org/abs/2509.05336v1](http://arxiv.org/abs/2509.05336v1)

**Summary:** Batteries with liquid alkali-metal negative electrodes offer a route to compact, high-performance energy storage. Innovation in alkali-metal management, i.e., controlled storage, release and transport of liquid alkali metal, can enable simpler and cheaper cell designs. Porous carbons have emerged as potential host materials for liquid alkali metals. Here, we study the wetting interactions between porous carbon hosts and liquid sodium-potassium alloy (NaK) as a function of carbon host morphology and surface functionalization via X-ray computed tomography. While as-received carbon samples show no affinity towards NaK, heat-treated carbon is spontaneously infiltrated with NaK filling almost the entire pore volume. We explore how forced wetting partially fills pores of NaK-repellent hosts, showing large differences in pore filling based on the average pore size of the host material. In electrochemical discharge experiments, we show that both as-received and heat-treated carbon felt enable high areal capacities beyond 40 mAh cm-2. However, the heat-treated carbon shows ten times lower overpotential. Finally, we demonstrate how heat-treated carbon felt can enable capillary transport of NaK. In summary, this study elucidates important aspects of the interactions between liquid alkali metals and porous carbon hosts, generating insights into possible applications in liquid alkali-metal batteries....

---

### 255. Instructional Agents: LLM Agents on Automated Course Material Generation for Teaching Faculties

**Authors:** Huaiyuan Yao, Wanpeng Xu, Justin Turnau, Nadia Kellam, Hua Wei

**Published:** 2025-08-27

**Category:** cs.AI

**ID:** 2508.19611v2

**Link:** [http://arxiv.org/abs/2508.19611v2](http://arxiv.org/abs/2508.19611v2)

**Summary:** Preparing high-quality instructional materials remains a labor-intensive process that often requires extensive coordination among teaching faculty, instructional designers, and teaching assistants. In this work, we present Instructional Agents, a multi-agent large language model (LLM) framework designed to automate end-to-end course material generation, including syllabus creation, lecture scripts, LaTeX-based slides, and assessments. Unlike existing AI-assisted educational tools that focus on isolated tasks, Instructional Agents simulates role-based collaboration among educational agents to produce cohesive and pedagogically aligned content. The system operates in four modes: Autonomous, Catalog-Guided, Feedback-Guided, and Full Co-Pilot mode, enabling flexible control over the degree of human involvement. We evaluate Instructional Agents across five university-level computer science courses and show that it produces high-quality instructional materials while significantly reducing development time and human workload. By supporting institutions with limited instructional design capacity, Instructional Agents provides a scalable and cost-effective framework to democratize access to high-quality education, particularly in underserved or resource-constrained settings....

---

### 256. Performance Improvement of Deorbitalized Exchange-Correlation Functionals

**Authors:** H. Francisco, B. Thapa, S. B. Trickey, A. C. Cancio

**Published:** 2025-08-31

**Category:** cond-mat.mtrl-sci

**ID:** 2509.00953v1

**Link:** [http://arxiv.org/abs/2509.00953v1](http://arxiv.org/abs/2509.00953v1)

**Summary:** Deorbitalization of a conventional meta-generalized-gradient exchange-correlation approximation replaces its dependence upon the Kohn-Sham kinetic energy density with a dependence on the density gradient and Laplacian. In principle, that simplification should provide improved computational performance relative to the original meta-GGA form because of the shift from an orbital-dependent generalized Kohn-Sham potential to a true KS local potential. Often that prospective gain is lost because of problematic roughness in the density caused by the density Laplacian and consequent roughness in the exchange-correlation potential from the resulting higher-order spatial derivatives of the density in it. We address the problem by constructing a deorbitalizer based on the RPP deorbitalizer [Phys. Rev. Mater. 6, 083803 (2022)] with comparative smoothness of the potential along with retention of constraint satisfaction as design goals. Applied to the r^2SCAN exchange-correlation functional [J. Phys. Chem. Lett. 11, 8208 (2020)], we find substantial timing improvements for solid-state calculations over both r^2SCAN and its earlier deorbitalization for high precision calculations of structural properties, while improving upon the accuracy of RPP deorbitalization for both solids and molecules....

---

### 257. LUMIR: an LLM-Driven Unified Agent Framework for Multi-task Infrared Spectroscopy Reasoning

**Authors:** Zujie Xie, Zixuan Chen, Jiheng Liang, Xiangyang Yu, Ziru Yu

**Published:** 2025-07-29

**Category:** cs.AI

**ID:** 2507.21471v2

**Link:** [http://arxiv.org/abs/2507.21471v2](http://arxiv.org/abs/2507.21471v2)

**Summary:** Infrared spectroscopy enables rapid, non destructive analysis of chemical and material properties, yet high dimensional signals and overlapping bands hinder conventional chemometric methods. Large language models (LLMs), with strong generalization and reasoning capabilities, offer new opportunities for automated spectral interpretation, but their potential in this domain remains largely untapped. This study introduces LUMIR (LLM-driven Unified agent framework for Multi-task Infrared spectroscopy Reasoning), an agent based framework designed to achieve accurate infrared spectral analysis under low data conditions. LUMIR integrates a structured literature knowledge base, automated preprocessing, feature extraction, and predictive modeling into a unified pipeline. By mining peer reviewed spectroscopy studies, it identifies validated preprocessing and feature derivation strategies, transforms spectra into low dimensional representations, and applies few-shot prompts for classification, regression, and anomaly detection. The framework was validated on diverse datasets, including the publicly available Milk near-infrared dataset, Chinese medicinal herbs, Citri Reticulatae Pericarpium(CRP) with different storage durations, an industrial wastewater COD dataset, and two additional public benchmarks, Tecator and Corn. Across these tasks, LUMIR achieved performance comparable to or surpassing established machine learning and deep learning models, particularly in resource limited settings. This work demonstrates that combining structured literature guidance with few-shot learning enables robust, scalable, and automated spectral interpretation. LUMIR establishes a new paradigm for applying LLMs to infrared spectroscopy, offering high accuracy with minimal labeled data and broad applicability across scientific and industrial domains....

---

### 258. Reexamining Machine Learning Models on Predicting Thermoelectric Properties

**Authors:** Chung T. Ma, S. Joseph Poon

**Published:** 2025-08-30

**Category:** cond-mat.mtrl-sci

**ID:** 2509.00299v1

**Link:** [http://arxiv.org/abs/2509.00299v1](http://arxiv.org/abs/2509.00299v1)

**Summary:** Thermoelectric materials can generate clean energy by transforming waste heat into electricity. The effectiveness of thermoelectric materials is measured by the dimensionless figure of merit, ZT. The quest for high ZT materials has drawn extensive research experimentally and theoretically. However, due to the vast material space, finding high ZT materials is time-consuming and costly. To improve the efficiency of discovering new thermoelectric materials, recent studies have employed machine learning with databases to search for high ZT candidates. In this work, we examine the effects of adding various physical concepts on the performance of machine learning models in predicting TE properties. The objective is to improve the model ability to capture the underlying physics in designing TE materials. These concepts include short range order and crystal structure class. Results show some improvements in accuracy. However, the current models do not distinguish between dilute alloys and concentrated alloys, rendering them inadequate in predicting doping effects. To better capture the electronic band structure effect from doping, we included various dopant properties as features. This increases the prediction accuracy in doped materials. Furthermore, we used a genetic algorithm to rank features for various thermoelectric properties to provide physical insight into key parameters in designing thermoelectric materials....

---

### 259. Generative AI for Industrial Contour Detection: A Language-Guided Vision System

**Authors:** Liang Gong, Tommy, Wang, Sara Chaker, Yanchen Dong, Fouad Bousetouane, Brenden Morton, Mark Mendez

**Published:** 2025-08-29

**Category:** cs.CV

**ID:** 2509.00284v1

**Link:** [http://arxiv.org/abs/2509.00284v1](http://arxiv.org/abs/2509.00284v1)

**Summary:** Industrial computer vision systems often struggle with noise, material variability, and uncontrolled imaging conditions, limiting the effectiveness of classical edge detectors and handcrafted pipelines. In this work, we present a language-guided generative vision system for remnant contour detection in manufacturing, designed to achieve CAD-level precision. The system is organized into three stages: data acquisition and preprocessing, contour generation using a conditional GAN, and multimodal contour refinement through vision-language modeling, where standardized prompts are crafted in a human-in-the-loop process and applied through image-text guided synthesis. On proprietary FabTrack datasets, the proposed system improved contour fidelity, enhancing edge continuity and geometric alignment while reducing manual tracing. For the refinement stage, we benchmarked several vision-language models, including Google's Gemini 2.0 Flash, OpenAI's GPT-image-1 integrated within a VLM-guided workflow, and open-source baselines. Under standardized conditions, GPT-image-1 consistently outperformed Gemini 2.0 Flash in both structural accuracy and perceptual quality. These findings demonstrate the promise of VLM-guided generative workflows for advancing industrial computer vision beyond the limitations of classical pipelines....

---

### 260. Strategies to search for two-dimensional materials with long spin qubit coherence time

**Authors:** Michael Y. Toriyama, Jiawei Zhan, Shun Kanai, Giulia Galli

**Published:** 2025-08-29

**Category:** quant-ph

**ID:** 2509.00222v1

**Link:** [http://arxiv.org/abs/2509.00222v1](http://arxiv.org/abs/2509.00222v1)

**Summary:** Two-dimensional (2D) materials that can host qubits with long spin coherence time (T2) have the distinct advantage of integrating easily with existing microelectronic and photonic platforms, making them attractive for designing novel quantum devices with enhanced performance. However, the relative lack of 2D materials as spin qubit hosts, as well as appropriate substrates that can help maintain long T2, necessitates a strategy to search for candidates with robust spin coherence. Here, we develop a high-throughput computational workflow to predict the nuclear spin bath-driven qubit decoherence and T2 in 2D materials and heterostructures. We initially screen 1173 2D materials and find 190 monolayers with T2 > 1 ms, higher than that of naturally-abundant diamond. We then construct 1554 lattice-commensurate heterostructures between high-T2 2D materials and select 3D substrates, and we find that T2 is generally lower in a heterostructure than in the bare 2D host material; however, low-noise substrates (such as CeO2 and CaO) can help maintain high T2. To further accelerate the material screening effort, we derive analytical models that enable rapid predictions of T2 for 2D materials and heterotructures. The models offer a simple, yet quantitative, way to determine the relative contributions to decoherence from the nuclear spin baths of the 2D host and substrate in a heterostructural system. By developing a high-throughput workflow and analytical models, we expand the genome of 2D materials and their spin coherence times for the development of spin qubit platforms....

---

### 261. Introduction to the Analysis of Probabilistic Decision-Making Algorithms

**Authors:** Agustinus Kristiadi

**Published:** 2025-08-29

**Category:** cs.LG

**ID:** 2508.21620v1

**Link:** [http://arxiv.org/abs/2508.21620v1](http://arxiv.org/abs/2508.21620v1)

**Summary:** Decision theories offer principled methods for making choices under various types of uncertainty. Algorithms that implement these theories have been successfully applied to a wide range of real-world problems, including materials and drug discovery. Indeed, they are desirable since they can adaptively gather information to make better decisions in the future, resulting in data-efficient workflows. In scientific discovery, where experiments are costly, these algorithms can thus significantly reduce the cost of experimentation. Theoretical analyses of these algorithms are crucial for understanding their behavior and providing valuable insights for developing next-generation algorithms. However, theoretical analyses in the literature are often inaccessible to non-experts. This monograph aims to provide an accessible, self-contained introduction to the theoretical analysis of commonly used probabilistic decision-making algorithms, including bandit algorithms, Bayesian optimization, and tree search algorithms. Only basic knowledge of probability theory and statistics, along with some elementary knowledge about Gaussian processes, is assumed....

---

### 262. Understanding, Protecting, and Augmenting Human Cognition with Generative AI: A Synthesis of the CHI 2025 Tools for Thought Workshop

**Authors:** Lev Tankelevitch, Elena L. Glassman, Jessica He, Aniket Kittur, Mina Lee, Srishti Palani, Advait Sarkar, Gonzalo Ramos, Yvonne Rogers, Hari Subramonyam

**Published:** 2025-08-28

**Category:** cs.HC

**ID:** 2508.21036v1

**Link:** [http://arxiv.org/abs/2508.21036v1](http://arxiv.org/abs/2508.21036v1)

**Summary:** Generative AI (GenAI) radically expands the scope and capability of automation for work, education, and everyday tasks, a transformation posing both risks and opportunities for human cognition. How will human cognition change, and what opportunities are there for GenAI to augment it? Which theories, metrics, and other tools are needed to address these questions? The CHI 2025 workshop on Tools for Thought aimed to bridge an emerging science of how the use of GenAI affects human thought, from metacognition to critical thinking, memory, and creativity, with an emerging design practice for building GenAI tools that both protect and augment human thought. Fifty-six researchers, designers, and thinkers from across disciplines as well as industry and academia, along with 34 papers and portfolios, seeded a day of discussion, ideation, and community-building. We synthesize this material here to begin mapping the space of research and design opportunities and to catalyze a multidisciplinary community around this pressing area of research....

---

### 263. Constraint Learning in Multi-Agent Dynamic Games from Demonstrations of Local Nash Interactions

**Authors:** Zhouyu Zhang, Chih-Yuan Chiu, Glen Chou

**Published:** 2025-08-27

**Category:** cs.LG

**ID:** 2508.19945v2

**Link:** [http://arxiv.org/abs/2508.19945v2](http://arxiv.org/abs/2508.19945v2)

**Summary:** We present an inverse dynamic game-based algorithm to learn parametric constraints from a given dataset of local generalized Nash equilibrium interactions between multiple agents. Specifically, we introduce mixed-integer linear programs (MILP) encoding the Karush-Kuhn-Tucker (KKT) conditions of the interacting agents, which recover constraints consistent with the Nash stationarity of the interaction demonstrations. We establish theoretical guarantees that our method learns inner approximations of the true safe and unsafe sets, as well as limitations of constraint learnability from demonstrations of Nash equilibrium interactions. We also use the interaction constraints recovered by our method to design motion plans that robustly satisfy the underlying constraints. Across simulations and hardware experiments, our methods proved capable of inferring constraints and designing interactive motion plans for various classes of constraints, both convex and non-convex, from interaction demonstrations of agents with nonlinear dynamics....

---

### 264. Operating advanced scientific instruments with AI agents that learn on the job

**Authors:** Aikaterini Vriza, Michael H. Prince, Tao Zhou, Henry Chan, Mathew J. Cherukara

**Published:** 2025-08-27

**Category:** physics.ins-det

**ID:** 2509.00098v1

**Link:** [http://arxiv.org/abs/2509.00098v1](http://arxiv.org/abs/2509.00098v1)

**Summary:** Advanced scientific user facilities, such as next generation X-ray light sources and self-driving laboratories, are revolutionizing scientific discovery by automating routine tasks and enabling rapid experimentation and characterizations. However, these facilities must continuously evolve to support new experimental workflows, adapt to diverse user projects, and meet growing demands for more intricate instruments and experiments. This continuous development introduces significant operational complexity, necessitating a focus on usability, reproducibility, and intuitive human-instrument interaction. In this work, we explore the integration of agentic AI, powered by Large Language Models (LLMs), as a transformative tool to achieve this goal. We present our approach to developing a human-in-the-loop pipeline for operating advanced instruments including an X-ray nanoprobe beamline and an autonomous robotic station dedicated to the design and characterization of materials. Specifically, we evaluate the potential of various LLMs as trainable scientific assistants for orchestrating complex, multi-task workflows, which also include multimodal data, optimizing their performance through optional human input and iterative learning. We demonstrate the ability of AI agents to bridge the gap between advanced automation and user-friendly operation, paving the way for more adaptable and intelligent scientific facilities....

---

### 265. Symmetry-induced magnetism in fullerene monolayers

**Authors:** Jiaqi Wu, Leonard Werner Pingen, Timothy K. Dickens, Bo Peng

**Published:** 2025-08-25

**Category:** cond-mat.mtrl-sci

**ID:** 2508.18125v2

**Link:** [http://arxiv.org/abs/2508.18125v2](http://arxiv.org/abs/2508.18125v2)

**Summary:** Using molecular orbital theory, we introduce magnetism in pure-carbon, charge-neutral fullerene monolayers which are otherwise non-magnetic. By controlling either molecular or lattice symmetry, we can realise highly-tuneable magnetic fullerene monolayers. We demonstrate a general design principle based on group theory analysis and explain the origin of magnetism using two representative systems with $S_4$ and $C_3$ molecular symmetries. Moreover, for building blocks that lack appropriate molecular symmetry, we can enforce crystalline symmetry to induce magnetism as well. Finally, we discuss the experimental feasibility of realising our proposed magnetic fullerene monolayers by examining a previously synthesised C$_{60}$ system. Our work opens a new direction in introducing magnetism in non-magnetic building blocks by enforcing either molecular or lattice symmetry....

---

### 266. Attention is also needed for form design

**Authors:** B. Sankar, Dibakar Sen

**Published:** 2025-08-27

**Category:** cs.HC

**ID:** 2508.19708v1

**Link:** [http://arxiv.org/abs/2508.19708v1](http://arxiv.org/abs/2508.19708v1)

**Summary:** Conventional product design is a cognitively demanding process, limited by its time-consuming nature, reliance on subjective expertise, and the opaque translation of inspiration into tangible concepts. This research introduces a novel, attention-aware framework that integrates two synergistic systems: EUPHORIA, an immersive Virtual Reality environment using eye-tracking to implicitly capture a designer's aesthetic preferences, and RETINA, an agentic AI pipeline that translates these implicit preferences into concrete design outputs. The foundational principles were validated in a two-part study. An initial study correlated user's implicit attention with explicit preference and the next one correlated mood to attention. A comparative study where 4 designers solved challenging design problems using 4 distinct workflows, from a manual process to an end-to-end automated pipeline, showed the integrated EUPHORIA-RETINA workflow was over 4 times more time-efficient than the conventional method. A panel of 50 design experts evaluated the 16 final renderings. Designs generated by the fully automated system consistently received the highest Worthiness (calculated by an inverse Plackett-Luce model based on gradient descent optimization) and Design Effectiveness scores, indicating superior quality across 8 criteria: novelty, visual appeal, emotional resonance, clarity of purpose, distinctiveness of silhouette, implied materiality, proportional balance, & adherence to the brief. This research presents a validated paradigm shift from traditional Computer-Assisted Design (CAD) to a collaborative model of Designer-Assisting Computers (DAC). By automating logistical and skill-dependent generative tasks, the proposed framework elevates the designer's role to that of a creative director, synergizing human intuition with the generative power of agentic AI to produce higher-quality designs more efficiently....

---

### 267. VideoEraser: Concept Erasure in Text-to-Video Diffusion Models

**Authors:** Naen Xu, Jinghuai Zhang, Changjiang Li, Zhi Chen, Chunyi Zhou, Qingming Li, Tianyu Du, Shouling Ji

**Published:** 2025-08-21

**Category:** cs.CV

**ID:** 2508.15314v2

**Link:** [http://arxiv.org/abs/2508.15314v2](http://arxiv.org/abs/2508.15314v2)

**Summary:** The rapid growth of text-to-video (T2V) diffusion models has raised concerns about privacy, copyright, and safety due to their potential misuse in generating harmful or misleading content. These models are often trained on numerous datasets, including unauthorized personal identities, artistic creations, and harmful materials, which can lead to uncontrolled production and distribution of such content. To address this, we propose VideoEraser, a training-free framework that prevents T2V diffusion models from generating videos with undesirable concepts, even when explicitly prompted with those concepts. Designed as a plug-and-play module, VideoEraser can seamlessly integrate with representative T2V diffusion models via a two-stage process: Selective Prompt Embedding Adjustment (SPEA) and Adversarial-Resilient Noise Guidance (ARNG). We conduct extensive evaluations across four tasks, including object erasure, artistic style erasure, celebrity erasure, and explicit content erasure. Experimental results show that VideoEraser consistently outperforms prior methods regarding efficacy, integrity, fidelity, robustness, and generalizability. Notably, VideoEraser achieves state-of-the-art performance in suppressing undesirable content during T2V generation, reducing it by 46% on average across four tasks compared to baselines....

---

### 268. Ultrafast Spin Accumulations Drive Magnetization Reversal in Multilayers

**Authors:** Harjinder Singh, Alberto Anadón, Junta Igarashi, Quentin Remy, Stéphane Mangin, Michel Hehn, Jon Gorchon, Gregory Malinowski

**Published:** 2025-08-27

**Category:** cond-mat.mes-hall

**ID:** 2508.19675v1

**Link:** [http://arxiv.org/abs/2508.19675v1](http://arxiv.org/abs/2508.19675v1)

**Summary:** Engineering and controlling heat and spin transport on the femtosecond time-scale in spintronic devices opens up new ways to manipulate magnetization with unprecedented speed. Yet the underlying reversal mechanisms remain poorly understood due to the challenges of probing ultrafast, non-equilibrium spin dynamics. In this study, we demonstrate that typical magneto-optical experiments can be leveraged to access the time evolution of the spin accumulation generated within a magnetic multilayer following an ultrafast laser excitation. Furthermore, our analysis shows that the final magnetic state of the free-layer in a spin-valve is mainly dictated by the ultrafast dynamics of the reference-layer magnetization. Our results disentangle magnetization and spin transport dynamics within a multilayer stack and identify demagnetization and remagnetization-driven spin accumulation as the key mechanism for all-optical switching. These findings establish new design principles for ultrafast spintronic devices based on tailored spin current engineering....

---

### 269. CrystalICL: Enabling In-Context Learning for Crystal Generation

**Authors:** Ruobing Wang, Qiaoyu Tan, Yili Wang, Ying Wang, Xin Wang

**Published:** 2025-08-27

**Category:** cs.LG

**ID:** 2508.20143v1

**Link:** [http://arxiv.org/abs/2508.20143v1](http://arxiv.org/abs/2508.20143v1)

**Summary:** Designing crystal materials with desired physicochemical properties remains a fundamental challenge in materials science. While large language models (LLMs) have demonstrated strong in-context learning (ICL) capabilities, existing LLM-based crystal generation approaches are limited to zero-shot scenarios and are unable to benefit from few-shot scenarios. In contrast, human experts typically design new materials by modifying relevant known structures which aligns closely with the few-shot ICL paradigm. Motivated by this, we propose CrystalICL, a novel model designed for few-shot crystal generation. Specifically, we introduce a space-group based crystal tokenization method, which effectively reduces the complexity of modeling crystal symmetry in LLMs. We further introduce a condition-structure aware hybrid instruction tuning framework and a multi-task instruction tuning strategy, enabling the model to better exploit ICL by capturing structure-property relationships from limited data. Extensive experiments on four crystal generation benchmarks demonstrate the superiority of CrystalICL over the leading baseline methods on conditional and unconditional generation tasks....

---

### 270. IELDG: Suppressing Domain-Specific Noise with Inverse Evolution Layers for Domain Generalized Semantic Segmentation

**Authors:** Qizhe Fan, Chaoyu Liu, Zhonghua Qiao, Xiaoqin Shen

**Published:** 2025-08-27

**Category:** cs.CV

**ID:** 2508.19604v1

**Link:** [http://arxiv.org/abs/2508.19604v1](http://arxiv.org/abs/2508.19604v1)

**Summary:** Domain Generalized Semantic Segmentation (DGSS) focuses on training a model using labeled data from a source domain, with the goal of achieving robust generalization to unseen target domains during inference. A common approach to improve generalization is to augment the source domain with synthetic data generated by diffusion models (DMs). However, the generated images often contain structural or semantic defects due to training imperfections. Training segmentation models with such flawed data can lead to performance degradation and error accumulation. To address this issue, we propose to integrate inverse evolution layers (IELs) into the generative process. IELs are designed to highlight spatial discontinuities and semantic inconsistencies using Laplacian-based priors, enabling more effective filtering of undesirable generative patterns. Based on this mechanism, we introduce IELDM, an enhanced diffusion-based data augmentation framework that can produce higher-quality images. Furthermore, we observe that the defect-suppression capability of IELs can also benefit the segmentation network by suppressing artifact propagation. Based on this insight, we embed IELs into the decoder of the DGSS model and propose IELFormer to strengthen generalization capability in cross-domain scenarios. To further strengthen the model's semantic consistency across scales, IELFormer incorporates a multi-scale frequency fusion (MFF) module, which performs frequency-domain analysis to achieve structured integration of multi-resolution features, thereby improving cross-scale coherence. Extensive experiments on benchmark datasets demonstrate that our approach achieves superior generalization performance compared to existing methods....

---

### 271. Benchmarking Diffusion Annealing-Based Bayesian Inverse Problem Solvers

**Authors:** Evan Scope Crafts, Umberto Villa

**Published:** 2025-03-04

**Category:** math.OC

**ID:** 2503.03007v2

**Link:** [http://arxiv.org/abs/2503.03007v2](http://arxiv.org/abs/2503.03007v2)

**Summary:** In recent years, the ascendance of diffusion modeling as a state-of-the-art generative modeling approach has spurred significant interest in their use as priors in Bayesian inverse problems. However, it is unclear how to optimally integrate a diffusion model trained on the prior distribution with a given likelihood function to obtain posterior samples. While algorithms developed for this purpose can produce high-quality, diverse point estimates of the unknown parameters of interest, they are often tested on problems where the prior distribution is analytically unknown, making it difficult to assess their performance in providing rigorous uncertainty quantification. Motivated by this challenge, this work introduces three benchmark problems for evaluating the performance of diffusion model based samplers. The benchmark problems, which are inspired by problems in image inpainting, x-ray tomography, and phase retrieval, have a posterior density that is analytically known. In this setting, approximate ground-truth posterior samples can be obtained, enabling principled evaluation of the performance of posterior sampling algorithms. This work also introduces a general framework for diffusion model based posterior sampling, Bayesian Inverse Problem Solvers through Diffusion Annealing (BIPSDA). This framework unifies several recently proposed diffusion-model-based posterior sampling algorithms and contains novel algorithms that can be realized through flexible combinations of design choices. We tested the performance of a set of BIPSDA algorithms, including previously proposed state-of-the-art approaches, on the proposed benchmark problems. The results provide insight into the strengths and limitations of existing diffusion-model based posterior samplers, while the benchmark problems provide a testing ground for future algorithmic developments....

---

### 272. Multi-timescale time encoding for CNN prediction of Fenna-Matthews-Olson energy-transfer dynamics

**Authors:** Shun-Cai Zhao, Yi-Meng Huang, Yi-Fan Yang, Zi-Ran Zhao

**Published:** 2025-03-21

**Category:** physics.chem-ph

**ID:** 2503.17430v4

**Link:** [http://arxiv.org/abs/2503.17430v4](http://arxiv.org/abs/2503.17430v4)

**Summary:** Machine learning simulations of open quantum dynamics often rely on recursive predictors that accumulate error. We develop a non-recursive convolutional neural networks (CNNs) that maps system parameters and a redundant time encoding directly to excitation-energy-transfer populations in the Fenna-Matthews-Olson complex. The encoding-modified logistic plus $\tanh$ functions-normalizes time and resolves fast, transitional, and quasi-steady regimes, while physics-informed labels enforce population conservation and inter-site consistency. Trained only on $0\sim 7 ps$ reference trajectories generated with a Lindblad model in QuTiP, the network accurately predicts $0\sim100 ps$ dynamics across a range of reorganization energies, bath rates, and temperatures. Beyond $20 ps$, the absolute relative error remains below 0.05, demonstrating stable long-time extrapolation. By avoiding step-by-step recursion, the method suppresses error accumulation and generalizes across timescales. These results show that redundant time encoding enables data-efficient inference of long-time quantum dissipative dynamics in realistic pigment-protein complexes, and may aid the data-driven design of light-harvesting materials....

---

### 273. Diverse, Distinct, and Densely Packed DNA Droplets

**Authors:** Aria S. Chaderjian, Sam Wilken, Omar A. Saleh

**Published:** 2025-08-26

**Category:** cond-mat.soft

**ID:** 2508.18574v1

**Link:** [http://arxiv.org/abs/2508.18574v1](http://arxiv.org/abs/2508.18574v1)

**Summary:** The liquid-liquid phase separation of biomolecules is an important process for intracellular organization. Biomolecular sequence combinatorics leads to a large variety of proteins and nucleic acids which can interact to form a diversity of dense liquid (`condensate') phases. The relationship between sequence design and the diversity of the resultant phases is therefore of interest. Here, we explore this question using the DNA nanostar system which permits the creation of multi-phase condensate droplets through sequence engineering of the sticky end bonds that drive particle-particle attraction. We explore the theoretical limits of nanostar phase diversity, then experimentally demonstrate the ability to create 9 distinct, non-adhering nanostar phases that do not share components. We further study how thermal processing affects the morphology and dynamics of such a highly diverse condensate system. We particularly show that a rapid temperature quench leads to the formation of a densely packed 2-D layer of droplets that is transiently stabilized by caging effects enabled by the phase diversity, leading to glassy dynamics, such as slow coarsening and dynamic heterogeneity. Generally, our work provides experimental insight into the thermodynamics of phase separation of complex mixtures and demonstrates the rational engineering of complex, long-range, multi-phase droplet structures....

---

### 274. Enhancing Chemical Explainability Through Counterfactual Masking

**Authors:** Łukasz Janisiów, Marek Kochańczyk, Bartosz Zieliński, Tomasz Danel

**Published:** 2025-08-25

**Category:** cs.LG

**ID:** 2508.18561v1

**Link:** [http://arxiv.org/abs/2508.18561v1](http://arxiv.org/abs/2508.18561v1)

**Summary:** Molecular property prediction is a crucial task that guides the design of new compounds, including drugs and materials. While explainable artificial intelligence methods aim to scrutinize model predictions by identifying influential molecular substructures, many existing approaches rely on masking strategies that remove either atoms or atom-level features to assess importance via fidelity metrics. These methods, however, often fail to adhere to the underlying molecular distribution and thus yield unintuitive explanations. In this work, we propose counterfactual masking, a novel framework that replaces masked substructures with chemically reasonable fragments sampled from generative models trained to complete molecular graphs. Rather than evaluating masked predictions against implausible zeroed-out baselines, we assess them relative to counterfactual molecules drawn from the data distribution. Our method offers two key benefits: (1) molecular realism underpinning robust and distribution-consistent explanations, and (2) meaningful counterfactuals that directly indicate how structural modifications may affect predicted properties. We demonstrate that counterfactual masking is well-suited for benchmarking model explainers and yields more actionable insights across multiple datasets and property prediction tasks. Our approach bridges the gap between explainability and molecular design, offering a principled and generative path toward explainable machine learning in chemistry....

---

### 275. PKG-DPO: Optimizing Domain-Specific AI systems with Physics Knowledge Graphs and Direct Preference Optimization

**Authors:** Nitin Nagesh Kulkarni, Bryson Wilcox, Max Sawa, Jason Thom

**Published:** 2025-08-25

**Category:** cs.AI

**ID:** 2508.18391v1

**Link:** [http://arxiv.org/abs/2508.18391v1](http://arxiv.org/abs/2508.18391v1)

**Summary:** Advancing AI systems in scientific domains like physics, materials science, and engineering calls for reasoning over complex, multi-physics phenomena while respecting governing principles. Although Large Language Models (LLMs) and existing preference optimization techniques perform well on standard benchmarks, they often struggle to differentiate between physically valid and invalid reasoning. This shortcoming becomes critical in high-stakes applications like metal joining, where seemingly plausible yet physically incorrect recommendations can lead to defects, material waste, equipment damage, and serious safety risks. To address this challenge, we introduce PKG-DPO, a novel framework that integrates Physics Knowledge Graphs (PKGs) with Direct Preference Optimization (DPO) to enforce physical validity in AI-generated outputs. PKG-DPO comprises three key components A) hierarchical physics knowledge graph that encodes cross-domain relationships, conservation laws, and thermodynamic principles. B) A physics reasoning engine that leverages structured knowledge to improve discrimination between physically consistent and inconsistent responses. C) A physics-grounded evaluation suite designed to assess compliance with domain-specific constraints. PKG-DPO achieves 17% fewer constraint violations and an 11% higher Physics Score compared to KG-DPO (knowledge graph-based DPO). Additionally, PKG-DPO demonstrates a 12\% higher relevant parameter accuracy and a 7% higher quality alignment in reasoning accuracy. While our primary focus is on metal joining, the framework is broadly applicable to other multi-scale, physics-driven domains, offering a principled approach to embedding scientific constraints into preference learning....

---

### 276. RepoMaster: Autonomous Exploration and Understanding of GitHub Repositories for Complex Task Solving

**Authors:** Huacan Wang, Ziyi Ni, Shuo Zhang, Shuo Lu, Sen Hu, Ziyang He, Chen Hu, Jiaye Lin, Yifu Guo, Ronghao Chen, Xin Li, Daxin Jiang, Yuntao Du, Pin Lyu

**Published:** 2025-05-27

**Category:** cs.SE

**ID:** 2505.21577v3

**Link:** [http://arxiv.org/abs/2505.21577v3](http://arxiv.org/abs/2505.21577v3)

**Summary:** The ultimate goal of code agents is to solve complex tasks autonomously. Although large language models (LLMs) have made substantial progress in code generation, real-world tasks typically demand full-fledged code repositories rather than simple scripts. Building such repositories from scratch remains a major challenge. Fortunately, GitHub hosts a vast, evolving collection of open-source repositories, which developers frequently reuse as modular components for complex tasks. Yet, existing frameworks like OpenHands and SWE-Agent still struggle to effectively leverage these valuable resources. Relying solely on README files provides insufficient guidance, and deeper exploration reveals two core obstacles: overwhelming information and tangled dependencies of repositories, both constrained by the limited context windows of current LLMs. To tackle these issues, we propose RepoMaster, an autonomous agent framework designed to explore and reuse GitHub repositories for solving complex tasks. For efficient understanding, RepoMaster constructs function-call graphs, module-dependency graphs, and hierarchical code trees to identify essential components, providing only identified core elements to the LLMs rather than the entire repository. During autonomous execution, it progressively explores related components using our exploration tools and prunes information to optimize context usage. Evaluated on the adjusted MLE-bench, RepoMaster achieves a 110% relative boost in valid submissions over the strongest baseline OpenHands. On our newly released GitTaskBench, RepoMaster lifts the task-pass rate from 40.7% to 62.9% while reducing token usage by 95%. Our code and demonstration materials are publicly available at https://github.com/QuantaAlpha/RepoMaster....

---

### 277. Graph atomic cluster expansion for foundational machine learning interatomic potentials

**Authors:** Yury Lysogorskiy, Anton Bochkarev, Ralf Drautz

**Published:** 2025-08-25

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17936v1

**Link:** [http://arxiv.org/abs/2508.17936v1](http://arxiv.org/abs/2508.17936v1)

**Summary:** Foundational machine learning interatomic potentials that can accurately and efficiently model a vast range of materials are critical for accelerating atomistic discovery. We introduce universal potentials based on the graph atomic cluster expansion (GRACE) framework, trained on several of the largest available materials datasets. Through comprehensive benchmarks, we demonstrate that the GRACE models establish a new Pareto front for accuracy versus efficiency among foundational interatomic potentials. We further showcase their exceptional versatility by adapting them to specialized tasks and simpler architectures via fine-tuning and knowledge distillation, achieving high accuracy while preventing catastrophic forgetting. This work establishes GRACE as a robust and adaptable foundation for the next generation of atomistic modeling, enabling high-fidelity simulations across the periodic table....

---

### 278. General Learning of the Electric Response of Inorganic Materials

**Authors:** Bradley A. A. Martin, Alex M. Ganose, Venkat Kapil, Keith T. Butler

**Published:** 2025-08-25

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17870v1

**Link:** [http://arxiv.org/abs/2508.17870v1](http://arxiv.org/abs/2508.17870v1)

**Summary:** We present MACE-Field, a field-aware $O(3)$-equivariant interatomic potential that provides a compact, derivative-consistent route to dielectric properties (such as polarisation $\mathbf P$, Born effective charges $Z^*$ and polarisability $\boldsymbolα$) and finite-field simulations across chemistry for inorganic solids. A uniform electric field is injected within each message-passing layer via a Clebsch-Gordan tensor-product which couples the field to latent spherical-tensor features, and perturbs them via an equivariant residual mixing. This plug-in design preserves the standard MACE readout and can inherit existing MACE foundation weights, turning pretrained models into field-aware ones with minimal change. To demonstrate, we train: (i) a cross-chemistry ferroelectric polarisation model (2.5k nonpolar$\!\to$polar polarisation branches), (ii) a cross-chemistry BECs/polarisability model ($\sim$6k Materials Project dielectrics spanning 81 elements), and (iii-iv) single-material molecular dynamics on BaTiO$_3$ and $α$-SiO$_2$. The models recover polarisation branches and spontaneous polarisation, predict $Z^*$ and $\boldsymbolα$ (hence $\varepsilon_\infty$) across diverse chemistries, and reproduce BaTiO$_3$ hysteresis and the IR/Raman and dielectric spectra of $α$-quartz, benchmarking comparatively with Allegro-pol....

---

### 279. The quantum metric of electrons with spin-momentum locking

**Authors:** Giacomo Sala, Maria Teresa Mercaldo, Klevis Domi, Stefano Gariglio, Mario Cuoco, Carmine Ortix, Andrea D. Caviglia

**Published:** 2024-07-09

**Category:** cond-mat.mes-hall

**ID:** 2407.06659v3

**Link:** [http://arxiv.org/abs/2407.06659v3](http://arxiv.org/abs/2407.06659v3)

**Summary:** Quantum materials are characterized by electromagnetic responses intrinsically linked to the geometry and topology of electronic wavefunctions, encoded in the quantum metric and Berry curvature. Whereas Berry curvature-mediated transport effects have been identified in several magnetic and nonmagnetic systems, quantum metric-induced transport phenomena remain limited to topological antiferromagnets. Here we show that spin-momentum locking -- a general characteristic of the electronic states at surfaces and interfaces of spin-orbit coupled materials -- leads to a finite quantum metric. This metric activates a nonlinear in-plane magnetoresistance that we measure and electrically control in 111-oriented LaAlO$_3$/SrTiO$_3$ interfaces. These findings demonstrate the existence of quantum metric effects in a vast class of materials and enable previously unexplored strategies to design functionalities based on quantum geometry....

---

### 280. Enhancing material behavior discovery using embedding-oriented Physically-Guided Neural Networks with Internal Variables

**Authors:** Rubén Muñoz-Sierra, Manuel Doblaré, Jacobo Ayensa-Jiménez

**Published:** 2025-08-01

**Category:** cs.LG

**ID:** 2508.00959v2

**Link:** [http://arxiv.org/abs/2508.00959v2](http://arxiv.org/abs/2508.00959v2)

**Summary:** Physically Guided Neural Networks with Internal Variables are SciML tools that use only observable data for training and and have the capacity to unravel internal state relations. They incorporate physical knowledge both by prescribing the model architecture and using loss regularization, thus endowing certain specific neurons with a physical meaning as internal state variables. Despite their potential, these models face challenges in scalability when applied to high-dimensional data such as fine-grid spatial fields or time-evolving systems. In this work, we propose some enhancements to the PGNNIV framework that address these scalability limitations through reduced-order modeling techniques. Specifically, we introduce alternatives to the original decoder structure using spectral decomposition, POD, and pretrained autoencoder-based mappings. These surrogate decoders offer varying trade-offs between computational efficiency, accuracy, noise tolerance, and generalization, while improving drastically the scalability. Additionally, we integrate model reuse via transfer learning and fine-tuning strategies to exploit previously acquired knowledge, supporting efficient adaptation to novel materials or configurations, and significantly reducing training time while maintaining or improving model performance. To illustrate these various techniques, we use a representative case governed by the nonlinear diffusion equation, using only observable data. Results demonstrate that the enhanced PGNNIV framework successfully identifies the underlying constitutive state equations while maintaining high predictive accuracy. It also improves robustness to noise, mitigates overfitting, and reduces computational demands. The proposed techniques can be tailored to various scenarios depending on data availability, resources, and specific modeling objectives, overcoming scalability challenges in all the scenarios....

---

### 281. Experimental demonstration of two distinct pathways of trion generation in monolayer MoS2

**Authors:** Faiha Mujeeb, Arkaprava Chowdhury, Anindya Datta, Subhabrata Dhar

**Published:** 2025-08-25

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17584v1

**Link:** [http://arxiv.org/abs/2508.17584v1](http://arxiv.org/abs/2508.17584v1)

**Summary:** Excitation power and energy dependent photoluminescence (PL) and transient absorption spectroscopy (TAS) studies are carried out on chemical vapour deposition (CVD) grown 1L-MoS2 films to understand the process of trion formation. The study shows that the excitation with sufficiently low photon energy results in the creation of trions directly in the K/K' valleys through photon absorption followed by phonon scattering events. On the other hand, excitation energy sufficiently larger than the band-gap can generate the carriers away from the K/K' valleys. Dissimilarity in the rates of relaxation of the photo-excited electrons and the holes to the bottom of the K/K' valleys results in the transformation of the excitons residing there into trions. Our TAS study clearly demonstrates a temporary increase of the trion population in the K/K' valleys. Moreover, excitation intensity dependent PL spectroscopy performed under above-band-gap excitation, also suggests the coexistence of both the pathways of trion generation in this material. This conclusion is further validated by a rate equation model. Our findings provide valuable insight into the formation of trions in monolayer transition metal dichalcogenides (TMDC), which could be crucial in designing valleytronic devices based on trions....

---

### 282. GUST: Quantifying Free-Form Geometric Uncertainty of Metamaterials Using Small Data

**Authors:** Jiahui Zheng, Cole Jahnke, Wei "Wayne" Chen

**Published:** 2025-05-28

**Category:** cs.LG

**ID:** 2506.12051v2

**Link:** [http://arxiv.org/abs/2506.12051v2](http://arxiv.org/abs/2506.12051v2)

**Summary:** This paper introduces GUST (Generative Uncertainty learning via Self-supervised pretraining and Transfer learning), a framework for quantifying free-form geometric uncertainties inherent in the manufacturing of metamaterials. GUST leverages the representational power of deep generative models to learn a high-dimensional conditional distribution of as-fabricated unit cell geometries given nominal designs, thereby enabling uncertainty quantification. To address the scarcity of real-world manufacturing data, GUST employs a two-stage learning process. First, it leverages self-supervised pretraining on a large-scale synthetic dataset to capture the structure variability inherent in metamaterial geometries and an approximated distribution of as-fabricated geometries given nominal designs. Subsequently, GUST employs transfer learning by fine-tuning the pretrained model on limited real-world manufacturing data, allowing it to adapt to specific manufacturing processes and nominal designs. With only 960 unit cells additively manufactured in only two passes, GUST can capture the variability in geometry and effective material properties. In contrast, directly training a generative model on the same amount of real-world data proves insufficient, as demonstrated through both qualitative and quantitative comparisons. This scalable and cost-effective approach significantly reduces data requirements while maintaining the effectiveness in learning complex, real-world geometric uncertainties, offering an affordable method for free-form geometric uncertainty quantification in the manufacturing of metamaterials. The capabilities of GUST hold significant promise for high-precision industries such as aerospace and biomedical engineering, where understanding and mitigating manufacturing uncertainties are critical....

---

### 283. Cooperative Suppression Strategy for Dual Thermal Transport Channels in Crystalline Materials

**Authors:** Yu Wu, Ying Chen, Shuming Zeng, Hao Zhang, Liujiang Zhou, Chenhan Liu, Su-Huai Wei

**Published:** 2025-08-24

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17318v1

**Link:** [http://arxiv.org/abs/2508.17318v1](http://arxiv.org/abs/2508.17318v1)

**Summary:** We propose a novel design principle for achieving ultralow thermal conductivity in crystalline materials via a "heavy-light and soft-stiff" structural motif. By combining heavy and light atomic species with soft and stiff bonding networks, both particle-like ($κ_p$) and wave-like ($κ_c$) phonon transport channels are concurrently suppressed. First-principles calculations show that this architecture induces a hierarchical phonon spectrum: soft-bonded heavy atoms generate dense low-frequency modes that enhance scattering and reduce $κ_p$, while stiff-bonded light atoms produce sparse high-frequency optical branches that disrupt coherence and lower $κ_c$. High-throughput screening identifies Tl$_4$SiS$_4$ ($κ_p$ = 0.10, $κ_c$ = 0.06 W/mK) and Tl$_4$GeS$_4$ ($κ_p$ = 0.09, $κ_c$ = 0.06 W/mK) as representative candidates with strongly suppressed transport in both channels. A minimal 1D triatomic chain model further demonstrates the generality of this mechanism, offering a new paradigm for phonon engineering beyond the conventional $κ_p$-$κ_c$ trade-off....

---

### 284. Metal-Free Room-Temperature Ferromagnetism

**Authors:** Hongde Yu, Thomas Heine

**Published:** 2025-08-24

**Category:** cond-mat.mtrl-sci

**ID:** 2508.17264v1

**Link:** [http://arxiv.org/abs/2508.17264v1](http://arxiv.org/abs/2508.17264v1)

**Summary:** Achieving robust room-temperature ferromagnetism in purely organic 2D crystals remains a fundamental challenge, primarily due to antiferromagnetic (AFM) coupling mediated by π-electron superexchange. Here, we present a mix-topology design strategy to induce strong ferromagnetic (FM) coupling in metal-free 2D systems. By covalently connecting radical polyaromatic hydrocarbon monomers (also referred to as nanographenes) with distinct sublattice topologies, this approach rationally breaks inversion symmetry and enables selective alignment of majority spins across the extended network, giving rise to metal-free ferromagnetism. Based on this strategy, we designed a family of 32 organic 2D crystals featuring spin-1/2 and mixed spin-1/2-spin-1 honeycomb lattices. Systematic first-principles calculations reveal that these materials are robust FM semiconductors with tunable spin-dependent bandgaps ranging from 0.9 to 3.8 eV. Notably, we demonstrate record-high magnetic coupling of up to 127 meV, spin-splitting energies exceeding 2 eV, and Curie temperatures surpassing 550 K, indicating thermal stability well above room temperature. The microscopic origin of the strong FM exchange stems from enhanced spin-orbital overlap and dominant direct exchange, while AFM superexchange is effectively suppressed. Our findings establish a generalizable design principle for realizing robust metal-free FM semiconductors and open new avenues for developing flexible and biocompatible magnets for next-generation spintronic and quantum technologies....

---

### 285. Chemical classification program synthesis using generative artificial intelligence

**Authors:** Christopher J. Mungall, Adnan Malik, Daniel R. Korn, Justin T. Reese, Noel M. O'Boyle, Noel, Janna Hastings

**Published:** 2025-05-24

**Category:** cs.AI

**ID:** 2505.18470v2

**Link:** [http://arxiv.org/abs/2505.18470v2](http://arxiv.org/abs/2505.18470v2)

**Summary:** Accurately classifying chemical structures is essential for cheminformatics and bioinformatics, including tasks such as identifying bioactive compounds of interest, screening molecules for toxicity to humans, finding non-organic compounds with desirable material properties, or organizing large chemical libraries for drug discovery or environmental monitoring. However, manual classification is labor-intensive and difficult to scale to large chemical databases. Existing automated approaches either rely on manually constructed classification rules, or are deep learning methods that lack explainability.
  This work presents an approach that uses generative artificial intelligence to automatically write chemical classifier programs for classes in the Chemical Entities of Biological Interest (ChEBI) database. These programs can be used for efficient deterministic run-time classification of SMILES structures, with natural language explanations. The programs themselves constitute an explainable computable ontological model of chemical class nomenclature, which we call the ChEBI Chemical Class Program Ontology (C3PO).
  We validated our approach against the ChEBI database, and compared our results against deep learning models and a naive SMARTS pattern based classifier. C3PO outperforms the naive classifier, but does not reach the performance of state of the art deep learning methods. However, C3PO has a number of strengths that complement deep learning methods, including explainability and reduced data dependence. C3PO can be used alongside deep learning classifiers to provide an explanation of the classification, where both methods agree. The programs can be used as part of the ontology development process, and iteratively refined by expert human curators....

---

### 286. Identifying the magnetic genes in fully- and partially-ordered V$_2$$X$Al ($X$ = Cr, Mn, Fe, Co, Ni) Heusler alloys

**Authors:** Zhenyang Xie, Yuntao Wu, Jitong Song, Yuanji Xu, Fuyang Tian

**Published:** 2025-08-23

**Category:** cond-mat.mtrl-sci

**ID:** 2508.16900v1

**Link:** [http://arxiv.org/abs/2508.16900v1](http://arxiv.org/abs/2508.16900v1)

**Summary:** Multicomponent Heusler alloys exhibit various magnetic properties arising from their diverse atomic compositions and crystal structures. Identifying the general physical principles that govern these behaviors is essential for advancing their potential in spintronic applications. In this work, we combine density functional theory with atomistic Monte Carlo simulations to investigate the magnetic ground states, finite-temperature magnetic transitions, and electronic structures of fully-ordered $L2_1$-, $XA$-type, and partially-ordered V$_2X$Al ($X=$ Cr, Mn, Fe, Co, Ni) Heusler alloys. We introduce the concept of magnetic genes, defined as V-$X$-V triangular motifs connected by the nearest-neighbor (NN) exchange interactions $J_{\mathrm{V-}X}$. Within this framework, the magnetic ground states and transition temperatures across the V$_2X$Al family can be consistently understood. The magnetic order is primarily governed by the NN $J_{\mathrm{V-}X}$ interactions in the triangular genes, while the transition temperatures are additionally influenced by $J_{X-X}$ couplings. Furthermore, the magnetic genes are still proven to be effective in our calculations on partially-ordered V$_2$$X$Al alloys from $L2_1$ to $XA$-type structures. Our results suggest that the concept of magnetic genes provides a unifying principle for understanding magnetic ordering in V-based Heusler alloys and could serve as a powerful guide for exploring magnetism and designing advanced spintronic materials in a broader class of Heusler systems....

---

### 287. 4D-PreNet: A Unified Preprocessing Framework for 4D-STEM Data Analysis

**Authors:** Mingyu Liu, Zian Mao, Zhu Liu, Haoran Zhang, Jintao Guo, Xiaoya He, Xi Huang, Shufen Chu, Chun Cheng, Jun Ding, Yujun Xie

**Published:** 2025-08-05

**Category:** cs.CV

**ID:** 2508.03775v2

**Link:** [http://arxiv.org/abs/2508.03775v2](http://arxiv.org/abs/2508.03775v2)

**Summary:** Automated experimentation with real time data analysis in scanning transmission electron microscopy (STEM) often require end-to-end framework. The four-dimensional scanning transmission electron microscopy (4D-STEM) with high-throughput data acquisition has been constrained by the critical bottleneck results from data preprocessing. Pervasive noise, beam center drift, and elliptical distortions during high-throughput acquisition inevitably corrupt diffraction patterns, systematically biasing quantitative measurements. Yet, conventional correction algorithms are often material-specific and fail to provide a robust, generalizable solution. In this work, we present 4D-PreNet, an end-to-end deep-learning pipeline that integrates attention-enhanced U-Net and ResNet architectures to simultaneously perform denoising, center correction, and elliptical distortion calibration. The network is trained on large, simulated datasets encompassing a wide range of noise levels, drift magnitudes, and distortion types, enabling it to generalize effectively to experimental data acquired under varying conditions. Quantitative evaluations demonstrate that our pipeline reduces mean squared error by up to 50% during denoising and achieves sub-pixel center localization in the center detection task, with average errors below 0.04 pixels. The outputs are bench-marked against traditional algorithms, highlighting improvements in both noise suppression and restoration of diffraction patterns, thereby facilitating high-throughput, reliable 4D-STEM real-time analysis for automated characterization....

---

### 288. Enhanced phonon-drag by nanoscale design of homoepitaxial \hbox{$β$-Ga$_2$O$_3$}

**Authors:** J. Boy, R. Mitdank, A. Popp, Z. Galazka, S. F. Fischer

**Published:** 2025-07-19

**Category:** cond-mat.mes-hall

**ID:** 2507.14763v2

**Link:** [http://arxiv.org/abs/2507.14763v2](http://arxiv.org/abs/2507.14763v2)

**Summary:** Phonon drag may be harnessed for thermoelectric generators and devices. Here, we demonstrate the geometric control of the phonon-drag contribution to the thermopower. In nanometer-thin electrically conducting $β$-Ga$_2$O$_3$ films homoepitaxially-grown on insulating substrates it is enhanced from -0,4 mV/K to up to -3 mV/K at 100 K by choice of the film thickness. Analysis of the temperature-dependent Seebeck coefficients reveal that a crossover from three-dimensional to quasi-two-dimensional electron-phonon interaction occurs for film thicknesses below 75~nm. The ratio of phonon-phonon to electron-phonon relaxation times in these confined structures is $10$ times larger than that of bulk. Generally the phonon drag can be tuned depending on the relations between the phonon-drag interaction length $λ_\text{PD}$, the phonon mean free path $λ$ and the film thickness $d$. Phonon drag can be enhanced for $λ_\text{PD}\ggλ>d$....

---

### 289. Termination-Driven Control over BIC Q-Factors and Frequencies in Plasmonic Double Net Metamaterials

**Authors:** Cedric Schumacher, Bilel Abdennadher, Ullrich Steiner, Matthias Saba

**Published:** 2025-08-22

**Category:** physics.optics

**ID:** 2508.16429v1

**Link:** [http://arxiv.org/abs/2508.16429v1](http://arxiv.org/abs/2508.16429v1)

**Summary:** Interlaced metallic wire meshes are 3D metamaterials consisting of two intertwined metallic networks. These plasmonic double nets give rise to otherwise unobserved longitudinal, weakly dispersive and broadband electron acoustic modes from the effective plasma frequency of the double net down to arbitrarily low frequencies. These modes have recently been shown to generate confined slab modes with extremely long lifetimes (high quality factors), so-called quasi-bound states in the continuum. This work reveals the central role of the double net termination in determining the mode's resonant frequency and quality factor. We compare two limiting cases, a tennis net termination recently studied experimentally by others and a protruding column array with a much lower quality factor, as demonstrated by microwave transmission experiments and full-wave simulations. Our work thus vividly demonstrates the failure of a homogenisation approach to explain and quantify the physics of terminated plasmonic network materials. We introduce a new approach, in which additional evanescent bulk states are included in the scattering problem, yielding a qualitative understanding of the slab's optical response. The resulting engineering principles pave the way for the design and exploitation of these materials for applications such as coherent light generation....

---

### 290. A Sharp KL-Convergence Analysis for Diffusion Models under Minimal Assumptions

**Authors:** Nishant Jain, Tong Zhang

**Published:** 2025-08-22

**Category:** stat.ML

**ID:** 2508.16306v1

**Link:** [http://arxiv.org/abs/2508.16306v1](http://arxiv.org/abs/2508.16306v1)

**Summary:** Diffusion-based generative models have emerged as highly effective methods for synthesizing high-quality samples. Recent works have focused on analyzing the convergence of their generation process with minimal assumptions, either through reverse SDEs or Probability Flow ODEs. The best known guarantees, without any smoothness assumptions, for the KL divergence so far achieve a linear dependence on the data dimension $d$ and an inverse quadratic dependence on $\varepsilon$. In this work, we present a refined analysis that improves the dependence on $\varepsilon$. We model the generation process as a composition of two steps: a reverse ODE step, followed by a smaller noising step along the forward process. This design leverages the fact that the ODE step enables control in Wasserstein-type error, which can then be converted into a KL divergence bound via noise addition, leading to a better dependence on the discretization step size. We further provide a novel analysis to achieve the linear $d$-dependence for the error due to discretizing this Probability Flow ODE in absence of any smoothness assumptions. We show that $\tilde{O}\left(\tfrac{d\log^{3/2}(\frac{1}δ)}{\varepsilon}\right)$ steps suffice to approximate the target distribution corrupted with Gaussian noise of variance $δ$ within $O(\varepsilon^2)$ in KL divergence, improving upon the previous best result, requiring $\tilde{O}\left(\tfrac{d\log^2(\frac{1}δ)}{\varepsilon^2}\right)$ steps....

---

### 291. FIRE-GNN: Force-informed, Relaxed Equivariance Graph Neural Network for Rapid and Accurate Prediction of Surface Properties

**Authors:** Circe Hsu, Claire Schlesinger, Karan Mudaliar, Jordan Leung, Robin Walters, Peter Schindler

**Published:** 2025-08-22

**Category:** cond-mat.mtrl-sci

**ID:** 2508.16012v1

**Link:** [http://arxiv.org/abs/2508.16012v1](http://arxiv.org/abs/2508.16012v1)

**Summary:** The work function and cleavage energy of a surface are critical properties that determine the viability of materials in electronic emission applications, semiconductor devices, and heterogeneous catalysis. While first principles calculations are accurate in predicting these properties, their computational expense combined with the vast search space of surfaces make a comprehensive screening approach with density functional theory (DFT) infeasible. Here, we introduce FIRE-GNN (Force-Informed, Relaxed Equivariance Graph Neural Network), which integrates surface-normal symmetry breaking and machine learning interatomic potential (MLIP)-derived force information, achieving a twofold reduction in mean absolute error (down to 0.065 eV) over the previous state-of-the-art for work function prediction. We additionally benchmark recent invariant and equivariant architectures, analyze the impact of symmetry breaking, and evaluate out-of-distribution generalization, demonstrating that FIRE-GNN consistently outperforms competing models for work function predictions. This model enables accurate and rapid predictions of the work function and cleavage energy across a vast chemical space and facilitates the discovery of materials with tuned surface properties...

---

### 292. Ultrastrong and ductile CoNiMoAl medium-entropy alloys enabled by L12 nanoprecipitate-induced multiple deformation mechanisms

**Authors:** Min Young Sung, Tae Jin Jang, Sang Yoon Song, Gunjick Lee, KenHee Ryou, Sang-Ho Oh, Byeong-Joo Lee, Pyuck-Pa Choi, Jörg Neugebauer, Blazej Grabowski, Fritz Körmann, Yuji Ikeda, Alireza Zargaran, Seok Su Sohn

**Published:** 2025-08-21

**Category:** cond-mat.mtrl-sci

**ID:** 2508.15596v1

**Link:** [http://arxiv.org/abs/2508.15596v1](http://arxiv.org/abs/2508.15596v1)

**Summary:** L12 precipitates are known to significantly enhance the strength and ductility of single-phase face-centered cubic (FCC) medium- or high-entropy alloys (M/HEAs). However, further improvements in mechanical properties remain untapped, as alloy design has historically focused on systems with specific CrCoNi- or FeCoCrNi-based FCC matrix and Ni3Al L12 phase compositions. This study introduces novel Co-Ni-Mo-Al alloys with L12 precipitates by systematically altering Al content, aiming to bridge this research gap by revealing the strengthening mechanisms. The (CoNi)81Mo12Al7 alloy achieves yield strength of 1086 MPa, tensile strength of 1520 MPa, and ductility of 35 %, demonstrating an impressive synergy of strength, ductility, and strain-hardening capacity. Dislocation analysis via transmission electron microscopy, supported by generalized stacking fault energy (GSFE) calculations using density functional theory (DFT), demonstrates that Mo substitution for Al in the L12 phase alters dislocation behavior, promoting the formation of multiple deformation modes, including stacking faults, super-dislocation pairs, Lomer-Cottrell locks, and unusual nano-twin formation even at low strains. These behaviors are facilitated by the low stacking fault energy (SFE) of the FCC matrix, overlapping of SFs, and dislocation dissociation across anti-phase boundaries (APBs). The increased energy barrier for superlattice intrinsic stacking fault (SISF) formation compared to APBs, due to Mo substitution, further influences dislocation activity. This work demonstrates a novel strategy for designing high-performance M/HEAs by expanding the range of FCC matrix and L12 compositions through precipitation hardening....

---

### 293. Strong lead-free bioinspired piezoceramics for durable energy transducers

**Authors:** Ruxue Yang, Temesgen Tadeyos Zate, Soumyajit Mojumder, Oriol Gavalda-Diaz, Zihe Li, Ajeet Kumar, James Roscow, Hamideh Khanbareh, Astri Bjørnetun Haugen, Florian Bouville

**Published:** 2025-08-21

**Category:** cond-mat.mtrl-sci

**ID:** 2508.15382v1

**Link:** [http://arxiv.org/abs/2508.15382v1](http://arxiv.org/abs/2508.15382v1)

**Summary:** Durable, high-performance and eco-friendly lead-free piezoceramics are essential for next-generation sustainable energy transducers and electromechanical systems. While significant performance enhancements have been made, through chemical composition, texture, or crystal defects, piezoceramics are intrinsically weak mechanically, which negatively impact their working conditions and durability. What's more, improving comprehensive mechanical durability without sacrificing piezoelectric performance remains a key challenge. Here, we design bioinspired Bi0.5Na0.5TiO3 (BNT) ceramics using a scalable colloidal process that enables multiscale control over the microstructure. The design comprises plate-like monocrystalline BNT bricks stacked to induce a crystallographic texture along the poling direction, bonded together by a silica-based mortar, forming the brick-and-mortar phase. This deliberate microstructure design yields 2- to 3-fold increase in flexural strength, and 1.6- to 2-fold increase in fracture toughness compared with a BNT synthesized conventionally, comparable to common structural ceramics, without sacrificing the piezoelectric performance. In addition, the bioinspired BNT exhibit dramatically enhanced ferroelectric fatigue resistance, with a 40- to 600-folds improvement in the number of field-induced electromechanical cycles before failure. These gains stem from residual stress fields generated at the interface between silica pockets and BNT bricks, which delay crack initiation. Furthermore, we demonstrated enhanced transducing capability and electromechanical fatigue resistance using a cantilever beam-based piezoelectric transducer under bending mode. Given its non-chemical-compositional origin, this bioinspired strategy could be broadly applicable to other piezoelectric material systems for applications where both functional and structural performance are critical....

---

### 294. Physics-Informed ML Exploration of Structure-Transport Relationships in Hard Carbon

**Authors:** Nikhil Rampal, Stephen E. Weitzner, Fredrick Omenya, Marissa Wood, David M. Reed, Xiaolin Li, Jonathan R. I. Lee, Liwen F. Wan

**Published:** 2025-08-20

**Category:** cond-mat.mtrl-sci

**ID:** 2508.14849v1

**Link:** [http://arxiv.org/abs/2508.14849v1](http://arxiv.org/abs/2508.14849v1)

**Summary:** Sodium-ion batteries are a cost-effective and sustainable alternative to lithium-ion systems for large-scale energy storage. Hard carbon (HC) anodes, composed of disordered graphitic and amorphous domains, offer high capacity but exhibit complex, poorly understood ion transport behavior. In particular, the relationship between local microstructure and sodium mobility remains unresolved, hindering rational performance optimization. Here, we introduce a data-driven framework that combines machine-learned interatomic potentials with molecular dynamics simulations to systematically investigate sodium diffusion across a broad range of carbon densities and sodium loadings. By computing per-ion structural descriptors, we identify the microscopic factors that govern ion transport. Unsupervised learning uncovers distinct diffusion modes, including hopping, clustering, and void trapping, while supervised analysis highlights tortuosity and NaNa coordination as primary determinants of mobility. Correlation mapping further connects these transport regimes to processing variables such as bulk density and sodium content. This physics-informed approach establishes quantitative structure-transport relationships that capture the heterogeneity of disordered carbon. Our findings deliver mechanistic insights into sodium-ion dynamics and provide actionable design principles for engineering high-performance HC anodes in next-generation battery systems....

---

### 295. Enabling Multi-Agent Systems as Learning Designers: Applying Learning Sciences to AI Instructional Design

**Authors:** Jiayi Wang, Ruiwei Xiao, Xinying Hou, John Stamper

**Published:** 2025-08-20

**Category:** cs.CY

**ID:** 2508.16659v1

**Link:** [http://arxiv.org/abs/2508.16659v1](http://arxiv.org/abs/2508.16659v1)

**Summary:** K-12 educators are increasingly using Large Language Models (LLMs) to create instructional materials. These systems excel at producing fluent, coherent content, but often lack support for high-quality teaching. The reason is twofold: first, commercial LLMs, such as ChatGPT and Gemini which are among the most widely accessible to teachers, do not come preloaded with the depth of pedagogical theory needed to design truly effective activities; second, although sophisticated prompt engineering can bridge this gap, most teachers lack the time or expertise and find it difficult to encode such pedagogical nuance into their requests. This study shifts pedagogical expertise from the user's prompt to the LLM's internal architecture. We embed the well-established Knowledge-Learning-Instruction (KLI) framework into a Multi-Agent System (MAS) to act as a sophisticated instructional designer. We tested three systems for generating secondary Math and Science learning activities: a Single-Agent baseline simulating typical teacher prompts; a role-based MAS where agents work sequentially; and a collaborative MAS-CMD where agents co-construct activities through conquer and merge discussion. The generated materials were evaluated by 20 practicing teachers and a complementary LLM-as-a-judge system using the Quality Matters (QM) K-12 standards. While the rubric scores showed only small, often statistically insignificant differences between the systems, the qualitative feedback from educators painted a clear and compelling picture. Teachers strongly preferred the activities from the collaborative MAS-CMD, describing them as significantly more creative, contextually relevant, and classroom-ready. Our findings show that embedding pedagogical principles into LLM systems offers a scalable path for creating high-quality educational content....

---

### 296. Learning to Use AI for Learning: How Can We Effectively Teach and Measure Prompting Literacy for K-12 Students?

**Authors:** Ruiwei Xiao, Xinying Hou, Ying-Jui Tseng, Hsuan Nieu, Guanze Liao, John Stamper, Kenneth R. Koedinger

**Published:** 2025-08-19

**Category:** cs.HC

**ID:** 2508.13962v1

**Link:** [http://arxiv.org/abs/2508.13962v1](http://arxiv.org/abs/2508.13962v1)

**Summary:** As Artificial Intelligence (AI) becomes increasingly integrated into daily life, there is a growing need to equip the next generation with the ability to apply, interact with, evaluate, and collaborate with AI systems responsibly. Prior research highlights the urgent demand from K-12 educators to teach students the ethical and effective use of AI for learning. To address this need, we designed an Large-Language Model (LLM)-based module to teach prompting literacy. This includes scenario-based deliberate practice activities with direct interaction with intelligent LLM agents, aiming to foster secondary school students' responsible engagement with AI chatbots. We conducted two iterations of classroom deployment in 11 authentic secondary education classrooms, and evaluated 1) AI-based auto-grader's capability; 2) students' prompting performance and confidence changes towards using AI for learning; and 3) the quality of learning and assessment materials. Results indicated that the AI-based auto-grader could grade student-written prompts with satisfactory quality. In addition, the instructional materials supported students in improving their prompting skills through practice and led to positive shifts in their perceptions of using AI for learning. Furthermore, data from Study 1 informed assessment revisions in Study 2. Analyses of item difficulty and discrimination in Study 2 showed that True/False and open-ended questions could measure prompting literacy more effectively than multiple-choice questions for our target learners. These promising outcomes highlight the potential for broader deployment and highlight the need for broader studies to assess learning effectiveness and assessment design....

---

### 297. Cross-Modal Characterization of Thin Film MoS$_2$ Using Generative Models

**Authors:** Isaiah A. Moses, Chen Chen, Joan M. Redwing, Wesley F. Reinhart

**Published:** 2025-05-29

**Category:** cond-mat.mtrl-sci

**ID:** 2505.24065v2

**Link:** [http://arxiv.org/abs/2505.24065v2](http://arxiv.org/abs/2505.24065v2)

**Summary:** The growth and characterization of materials using empirical optimization typically requires a significant amount of expert time, experience, and resources. Several complementary characterization methods are routinely performed to determine the quality and properties of a grown sample. Machine learning (ML) can support the conventional approaches by using historical data to guide and provide speed and efficiency to the growth and characterization of materials. Specifically, ML can provide quantitative information from characterization data that is typically obtained from a different modality. In this study, we have investigated the feasibility of projecting the quantitative metric from microscopy measurements, such as atomic force microscopy (AFM), using data obtained from spectroscopy measurements, like Raman spectroscopy. Generative models were also trained to generate the full and specific features of the Raman and photoluminescence spectra from each other and the AFM images of the thin film MoS$_2$. The results are promising and have provided a foundational guide for the use of ML for the cross-modal characterization of materials for their accelerated, efficient, and cost-effective discovery....

---

### 298. AutoChemSchematic AI: Agentic Physics-Aware Automation for Chemical Manufacturing Scale-Up

**Authors:** Sakhinana Sagar Srinivas, Shivam Gupta, Venkataramana Runkana

**Published:** 2025-05-30

**Category:** cs.LG

**ID:** 2505.24584v3

**Link:** [http://arxiv.org/abs/2505.24584v3](http://arxiv.org/abs/2505.24584v3)

**Summary:** Recent advances in generative AI have accelerated the discovery of novel chemicals and materials. However, scaling these discoveries to industrial production remains a major bottleneck due to the synthesis gap -- the need to develop entirely new manufacturing processes. This challenge requires detailed engineering blueprints: PFDs for equipment layouts and material/energy flows, and PIDs for process plant operations. Current AI systems cannot yet reliably generate these critical engineering schematics, creating a fundamental obstacle to manufacturing scale-up of novel discoveries. We present a closed-loop, physics-aware framework for automated generation of industrially viable PFDs and PIDs. The framework integrates three key components: (1) domain-specialized small language models (SLMs) trained for auto-generation of PFDs and PIDs, (2) a hierarchical knowledge graph containing process flow and instrumentation descriptions for 1,020+ chemicals for Graph Retrieval-Augmented Generation (GRAG), and (3) an open-source chemical process simulator for modeling, simulation, optimization, and analysis of novel chemical processes. The SLMs are trained through a multi-stage pipeline on synthetic datasets, with process simulator-in-the-loop validation ensuring feasibility. To enhance computational efficiency, the framework implements structural pruning (width and depth) guided by importance heuristics to reduce language model size while preserving accuracy, followed by advanced inference optimizations including FlashAttention, Lookahead Decoding, PagedAttention with KV-cache quantization, and Test-Time Inference Scaling. Experimental results demonstrate that our framework generates simulator-validated process descriptions with high fidelity....

---

### 299. Observation of Analogue Dynamic Schwinger Effect and Non-Perturbative Light Sensing in Lead Halide Perovskites

**Authors:** Dusan Lorenc, Artem G. Volosniev, Ayan A. Zhumekenov, Seungho Lee, Maria Ibáñez, Osman M. Bakr, Mikhail Lemeshko, Zhanybek Alpichshev

**Published:** 2024-06-07

**Category:** cond-mat.mes-hall

**ID:** 2406.05032v3

**Link:** [http://arxiv.org/abs/2406.05032v3](http://arxiv.org/abs/2406.05032v3)

**Summary:** Dielectric breakdown of physical vacuum (Schwinger effect) is the textbook demonstration of compatibility of Relativity and Quantum theory. Although observing this effect is still practically unachievable, its analogue generalizations have been shown to be more readily attainable. This paper demonstrates that a gapped Dirac semiconductor, methylammonium lead-bromide perovskite (MAPbBr$_3$), exhibits analogue dynamical Schwinger effect. Tunneling ionization under deep sub-gap mid-infrared irradiation leads to intense photoluminescence in the visible range, in full agreement with quasi-adiabatic theory. In addition to revealing a gapped extended system suitable for studying the analogue Schwinger effect, this observation holds great potential for non-perturbative field sensing, i.e., sensing electric fields through non-perturbative light-matter interactions. First, this paper illustrates this by measuring the local deviation from the nominally cubic phase of a perovskite single crystal, which can be interpreted in terms of frozen-in fields. Next, it is shown that analogue dynamic Schwinger effect can be used for nonperturbative amplification of non-parametric upconversion process in perovskites driven simultaneously by multiple optical fields. This discovery demonstrates the potential for material response beyond perturbation theory in the Schwinger regime, offering extremely sensitive light detection and amplification across an ultrabroad spectral range not accessible by conventional devices....

---

### 300. Bridging Molecular Simulation and Process Modeling for Predictive Multicomponent Adsorption

**Authors:** Sunghyun Yoon, Jui Tu, Li-Chiang Lin, Yongchul G. Chung

**Published:** 2025-08-17

**Category:** cond-mat.stat-mech

**ID:** 2508.12200v1

**Link:** [http://arxiv.org/abs/2508.12200v1](http://arxiv.org/abs/2508.12200v1)

**Summary:** Accurate and efficient prediction of multicomponent adsorption equilibria across pressures, temperatures, and compositions remain a central challenge for designing energy-efficient adsorption-based separation processes. Traditional approaches, including model fitting and ideal adsorbed solution theory (IAST), often fail to balance accuracy, computational efficiency, and transferability under process-relevant conditions. Here, we introduce a material-to-process modeling framework that integrates macrostate probability distributions (MPDs) from flat-histogram Monte Carlo simulations with rigorous cyclic process optimization. MPDs directly capture the joint occupancy distributions of adsorbates, producing reweightable landscape that enable high-fidelity mixture adsorption equilibria without repeated simulations or model assumptions. We show that coupling this statistical mechanical foundation with process modeling delivers accurate and computationally efficient evaluations for binary and ternary gas mixture separations. This integration establishes MPD-based modeling as a generalized method for predictive multicomponent adsorption equilibria, accelerating the discovery and design of adsorbent materials for carbon capture and other separation challenges....

---

### 301. Accelerating Amorphous Alloy Discovery: Data-Driven Property Prediction via General-Purpose Machine Learning Interatomic Potential

**Authors:** Xuhe Gong, Hengbo Zhao, Xiao Fu, Jingchen Lian, Qifan Yang, Ran Li, Ruijuan Xiao, Tao Zhang, Hong Li

**Published:** 2025-08-16

**Category:** cond-mat.mtrl-sci

**ID:** 2508.11989v1

**Link:** [http://arxiv.org/abs/2508.11989v1](http://arxiv.org/abs/2508.11989v1)

**Summary:** While traditional trial-and-error methods for designing amorphous alloys are costly and inefficient, machine learning approaches based solely on composition lack critical atomic structural information. Machine learning interatomic potentials, trained on data from first-principles calculations, offer a powerful alternative by efficiently approximating the complex three-dimensional potential energy surface with near-DFT accuracy. In this work, we develop a general-purpose machine learning interatomic potential for amorphous alloys by using a dataset comprising 20400 configurations across representative binary and ternary amorphous alloys systems. The model demonstrates excellent predictive performance on an independent test set, with a mean absolute error of 5.06 meV/atom for energy and 128.51 meV/Å for forces. Through extensive validation, the model is shown to reliably capture the trends in macroscopic property variations such as density, Young's modulus and glass transition temperature across both the original training systems and the compositionally modified systems derived from them. It can be directly applied to composition-property mapping of amorphous alloys. Furthermore, the developed interatomic potential enables access to the atomic structures of amorphous alloys, allowing for microscopic analysis and interpretation of experimental results, particularly those deviating from empirical trends.This work breaks the long-standing computational bottleneck in amorphous alloys research by developing the first general-purpose machine learning interatomic potential for amorphous alloy systems. The resulting framework provides a robust foundation for data-driven design and high-throughput composition screening in a field previously constrained by traditional simulation limitations....

---

### 302. Persistence is All You Need -- A Topological Lens on Microstructural Characterization

**Authors:** Maksym Szemer, Szymon Buchaniec, Grzegorz Brus

**Published:** 2025-08-16

**Category:** cs.CE

**ID:** 2508.11967v1

**Link:** [http://arxiv.org/abs/2508.11967v1](http://arxiv.org/abs/2508.11967v1)

**Summary:** The microstructure critically governs the properties of materials used in energy and chemical engineering technologies, from catalysts and filters to thermal insulators and sensors. Therefore, accurate design is based on quantitative descriptors of microstructural features. Here we show that eight key descriptors can be extracted by a single workflow that fuses computational topology with assembly-learning-based regression. First, 1312 synthetic three-dimensional microstructures were generated and evaluated using established algorithms, and a labeled data set of ground-truth parameters was built. Converting every structure into a persistence image allowed us to train a deep neural network that predicts the eight descriptors. In an independent test set, the model achieved on average R^2 ~ 0.84 and Pearson r ~ 0.92, demonstrating both precision and generality. The approach provides a unified and scalable tool for rapid characterization of functional porous materials....

---

### 303. LARC: Towards Human-level Constrained Retrosynthesis Planning through an Agentic Framework

**Authors:** Frazier N. Baker, Daniel Adu-Ampratwum, Reza Averly, Botao Yu, Huan Sun, Xia Ning

**Published:** 2025-08-16

**Category:** cs.AI

**ID:** 2508.11860v1

**Link:** [http://arxiv.org/abs/2508.11860v1](http://arxiv.org/abs/2508.11860v1)

**Summary:** Large language model (LLM) agent evaluators leverage specialized tools to ground the rational decision-making of LLMs, making them well-suited to aid in scientific discoveries, such as constrained retrosynthesis planning. Constrained retrosynthesis planning is an essential, yet challenging, process within chemistry for identifying synthetic routes from commercially available starting materials to desired target molecules, subject to practical constraints. Here, we present LARC, the first LLM-based Agentic framework for Retrosynthesis planning under Constraints. LARC incorporates agentic constraint evaluation, through an Agent-as-a-Judge, directly into the retrosynthesis planning process, using agentic feedback grounded in tool-based reasoning to guide and constrain route generation. We rigorously evaluate LARC on a carefully curated set of 48 constrained retrosynthesis planning tasks across 3 constraint types. LARC achieves a 72.9% success rate on these tasks, vastly outperforming LLM baselines and approaching human expert-level success in substantially less time. The LARC framework is extensible, and serves as a first step towards an effective agentic tool or a co-scientist to human experts for constrained retrosynthesis....

---

### 304. Optimal Geometric Design of Thermoelectric Metamaterials for Enhancing Power Generation: An Interpretative Approach

**Authors:** Xanthippi Zianni

**Published:** 2025-08-15

**Category:** physics.app-ph

**ID:** 2508.16627v1

**Link:** [http://arxiv.org/abs/2508.16627v1](http://arxiv.org/abs/2508.16627v1)

**Summary:** Thermoelectric metamaterials featuring width modulation through constrictions (constricted geometries) have emerged as a promising approach for improving heat management and thermoelectric performance. Through a combination of theoretical calculations, analytical formalism, and validation against experimental data, it is shown that thermoelectric performance in such geometries is governed by two fundamental mechanisms of pure geometrical origin: (i) a characteristic scaling behavior of resistance with Transmissivity, and (ii) the critical formation of the Constriction Thermal Resistance. Hourglass-shaped thermoelectric legs - identified as optimal in recent experiments - are found to exhibit the same underlying transport mechanisms observed in other constricted profiles, including single and multiple sharp constrictions. The commonly used Geometric Parameter is found to be insufficient for capturing the full influence of geometry on transport, whereas Transmissivity serves as a robust descriptor of constricted geometry, independent of material choice or device operating conditions. A universal scaling formalism is derived linking electrical and thermal resistances, along with key thermoelectric performance metrics, to the Transmissivity. A unified optimization framework is also developed for composite legs, incorporating both constricted material and contact electrodes. This framework indicates that previously reported performance gains may be largely attributed to contact resistance, rather than geometry alone. Transmissivity is established as a key geometric descriptor, enabling generalized design principles and global optimization criteria for enhancing thermoelectric power generation. This analysis elucidates new avenues in the design of thermoelectric metamaterials for efficient energy conversion....

---

### 305. Atomic perspective on the topological magnetism in kagome metal Co3Sn2S2

**Authors:** Guowei Liu, Wei Song, Titus Neupert, M. Zahid Hasan, Hanbin Deng, Jia-Xin Yin

**Published:** 2025-08-15

**Category:** cond-mat.str-el

**ID:** 2508.11140v1

**Link:** [http://arxiv.org/abs/2508.11140v1](http://arxiv.org/abs/2508.11140v1)

**Summary:** Topological quantum materials with kagome lattices have attracted intense interest due to their unconventional electronic structures, which exhibit nontrivial topology, anomalous magnetism, and electronic correlations. Among these, Co3Sn2S2 stands out as a prototypical kagome metal, uniquely combining intrinsic ferromagnetism with topologically nontrivial electronic states. This perspective presents a systematic overview of recent advances in studying kagome metal Co3Sn2S2 achieved through scanning tunneling microscopy. We begin by introducing different methodologies for surface identification and propose using designer layer-selective chemical markers for conclusive surface identification. We then discuss the Berry curvature induced flat band orbital magnetism and the associated unconventional Zeeman effect. Furthermore, we explore boundary states arising from Weyl topology and analyze challenges in detecting Fermi arcs via quasiparticle interference patterns and in uncovering the topological aspect of the edge states. Finally, we review recent observations of spin-orbit-coupled quantum impurity states through spin-polarized tunneling spectroscopy, as well as their connection to Weyl topology and flat band magnetism. We also provide in-depth analysis and constructive comments on the limitations of the current research approach. This review highlights the critical role of scanning tunneling microscopy in unraveling the intricate interplay between topology, magnetism, and correlations at the atomic scale, and the methodology discussed here can be applied to study other topological quantum materials in general....

---

### 306. Symmetry-Constrained Multi-Scale Physics-Informed Neural Networks for Graphene Electronic Band Structure Prediction

**Authors:** Wei Shan Lee, I Hang Kwok, Kam Ian Leong, Chi Kiu Althina Chau, Kei Chon Sio

**Published:** 2025-08-14

**Category:** cond-mat.mtrl-sci

**ID:** 2508.10718v1

**Link:** [http://arxiv.org/abs/2508.10718v1](http://arxiv.org/abs/2508.10718v1)

**Summary:** Accurate prediction of electronic band structures in two-dimensional materials remains a fundamental challenge, with existing methods struggling to balance computational efficiency and physical accuracy. We present the Symmetry-Constrained Multi-Scale Physics-Informed Neural Network (SCMS-PINN) v35, which directly learns graphene band structures while rigorously enforcing crystallographic symmetries through a multi-head architecture. Our approach introduces three specialized ResNet-6 pathways -- K-head for Dirac physics, M-head for saddle points, and General head for smooth interpolation -- operating on 31 physics-informed features extracted from k-points. Progressive Dirac constraint scheduling systematically increases the weight parameter from 5.0 to 25.0, enabling hierarchical learning from global topology to local critical physics. Training on 10,000 k-points over 300 epochs achieves 99.99\% reduction in training loss (34.597 to 0.003) with validation loss of 0.0085. The model predicts Dirac point gaps within 30.3 $μ$eV of theoretical zero and achieves average errors of 53.9 meV (valence) and 40.5 meV (conduction) across the Brillouin zone. All twelve C$_{6v}$ operations are enforced through systematic averaging, guaranteeing exact symmetry preservation. This framework establishes a foundation for extending physics-informed learning to broader two-dimensional materials for accelerated discovery....

---

### 307. Deep Learning in Classical and Quantum Physics

**Authors:** Timothy Heightman, Marcin Płodzień

**Published:** 2025-08-14

**Category:** quant-ph

**ID:** 2508.10666v1

**Link:** [http://arxiv.org/abs/2508.10666v1](http://arxiv.org/abs/2508.10666v1)

**Summary:** Scientific progress is tightly coupled to the emergence of new research tools. Today, machine learning (ML)-especially deep learning (DL)-has become a transformative instrument for quantum science and technology. Owing to the intrinsic complexity of quantum systems, DL enables efficient exploration of large parameter spaces, extraction of patterns from experimental data, and data-driven guidance for research directions. These capabilities already support tasks such as refining quantum control protocols and accelerating the discovery of materials with targeted quantum properties, making ML/DL literacy an essential skill for the next generation of quantum scientists. At the same time, DL's power brings risks: models can overfit noisy data, obscure causal structure, and yield results with limited physical interpretability. Recognizing these limitations and deploying mitigation strategies is crucial for scientific rigor. These lecture notes provide a comprehensive, graduate-level introduction to DL for quantum applications, combining conceptual exposition with hands-on examples. Organized as a progressive sequence, they aim to equip readers to decide when and how to apply DL effectively, to understand its practical constraints, and to adapt AI methods responsibly to problems across quantum physics, chemistry, and engineering....

---

### 308. EDIS: A Simulation Software for Dynamic Ion Intercalation/Deintercalation Processes in Electrode Materials

**Authors:** Liqi Wang, Ruijuan Xiao, Hong Li

**Published:** 2025-08-14

**Category:** cond-mat.mtrl-sci

**ID:** 2508.10384v1

**Link:** [http://arxiv.org/abs/2508.10384v1](http://arxiv.org/abs/2508.10384v1)

**Summary:** As the core determinant of lithium-ion battery performance, electrode materials play a crucial role in defining the battery's capacity, cycling stability, and durability. During charging and discharging, electrode materials undergo complex ion intercalation and deintercalation processes, accompanied by defect formation and structural evolution. However, the microscopic mechanisms underlying processes such as cation disordering, lattice oxygen loss, and stage structure formation phenomena are still not fully understood. To address these challenges, we have developed the Electrode Dynamic Ion Intercalation/Deintercalation Simulator (EDIS), a software platform designed to simulate the dynamic processes of ion intercalation and deintercalation in electrode materials. Leveraging high-precision machine learning potentials, EDIS can efficiently model structural evolution and lithium-ion diffusion behavior under various states of charge and discharge, achieving accuracy approaching that of quantum mechanical methods in relevant chemical spaces. The software supports quantitative analysis of how variations in lithium-ion concentration and distribution affect lithium-ion transport properties, enables evaluation of the impact of structural defects, and allows for tracking of both structural evolution and transport characteristics during continuous cycling. EDIS is versatile and can be extended to sodium-ion batteries and related systems. By enabling in-depth analysis of these microscopic processes, EDIS provides a robust theoretical tool for mechanistic studies and the rational design of high-performance electrode materials for next-generation lithium-ion batteries....

---

### 309. Tunable optical emissions of Eu3+ ions enabled by pressure-driven phase transition in ZnO

**Authors:** C. Ianhez-Pereira, U. F. Kaneko, A. D. Rodrigues, I. S. S. de Oliveira, M. P. F. de Godoy

**Published:** 2025-08-14

**Category:** cond-mat.mtrl-sci

**ID:** 2508.10953v1

**Link:** [http://arxiv.org/abs/2508.10953v1](http://arxiv.org/abs/2508.10953v1)

**Summary:** Controlling the optical properties of rare-earth ions in wide-bandgap semiconductors remains a major challenge in the development of next-generation photonic materials. Here, we show that external hydrostatic pressure modulates the structural characteristics of ZnO thin films and, in turn, tunes the optical emission behavior of embedded Eu3+ ions. By combining in situ synchrotron X-ray diffraction and photoluminescence spectroscopy under high-pressure conditions with first-principles calculations, we capture a pressure-induced phase transition from the hexagonal wurtzite to the cubic rocksalt structure near 10 GPa. This transformation is accompanied by complete quenching of the D0 - FJ Europium emissions near the transition threshold, followed by a partial recovery at higher pressures, likely associated with the emergence of structural disorder. Concurrently, the Stark components of the emission bands exhibit a redshift and significant broadening with increasing pressure, reflecting enhanced crystal field strength as interatomic distances decrease. Additional first-principles calculations support the observed pressure-induced shifts in the Eu-4f states and emphasize the influence of lattice symmetry on their electronic environment. These results show that hydrostatic pressure is an effective way to adjust the optical emissions of rare-earth ions by changing their symmetry and local environment, providing a basis for designing photonic devices and luminescent materials controlled by pressure....

---

### 310. Discovery of a low-density filled-ice phase in nitrogen hydrate at high pressure

**Authors:** Selene Berni, Sophie Espert, Tomasz Poreba, Simone Di Cataldo, Richard Gaal, Gabriel Tobie, Erwan Le Menn, Thomas C. Hansen, Roberto Bini, Livia Eleonora Bove

**Published:** 2025-08-13

**Category:** cond-mat.mtrl-sci

**ID:** 2508.09771v1

**Link:** [http://arxiv.org/abs/2508.09771v1](http://arxiv.org/abs/2508.09771v1)

**Summary:** We map the high-pressure phase diagram of nitrogen hydrate up to 16 GPa at room temperature by combining neutron diffraction, Raman spectroscopy, and crystal structure prediction. We reveal a rich sequence of structural transformations, from sI/sII clathrates to hexagonal (sH) and tetragonal (sT) phases, culminating in a previously unknown orthorhombic filled-ice structure above 1.8 GPa in the Pnma space group, which we designate as NH-V. This new phase cannot be indexed to any known ice frameworks - such as the high-pressure methane hydrates MH-III (Imma) or MH-IV (Pmcn) - and exhibits a density approximately 30% lower than that of stable ice VII, pointing to distinctive water-nitrogen interactions. Our results refine the understanding of nitrogen hydrate behavior under extreme conditions and demonstrate the propensity of nitrogen and water to form stable filled-ice structures up to 16 GPa, with important implications for planetary science....

---

### 311. Defect Engineered Layer Dependent Nonlinear Optical Response in Two Dimensional Muscovite for Efficient Optical Limiting

**Authors:** Dipanwita Mitra, Guilherme S. L. Fabris, Raphael Benjamim, Mateus M. Ferrer, Marcelo Lopes Pereira Junior, Riya Sadhukhan, Dipak Kumar Goswami, Gelu Costin, Douglas S. Galvão, Chandra Sekhar Tiwary, Prasanta Kumar Dattaa

**Published:** 2025-07-20

**Category:** physics.optics

**ID:** 2507.14786v2

**Link:** [http://arxiv.org/abs/2507.14786v2](http://arxiv.org/abs/2507.14786v2)

**Summary:** Light-matter interactions in two-dimensional (2D) materials have gained significant interest due to their distinctive optical and electronic properties. Recently, silicates have emerged as a promising new class of 2D materials, but their nonlinear optical properties remain largely unexplored. In this study, we demonstrate layer-dependent nonlinear absorption and optical limiting capabilities of 2D muscovite using femtosecond laser excitation at 450 nm. The two-photon absorption (TPA) coefficient is highly sensitive to both the number of layers and excitation intensity, increasing markedly from (3.91+/-0.06)x10^3 cm GW^-1 in multilayer structures to (6.94+/-0.17)x10^5 cm GW^-1 in the monolayer limit at a peak intensity of 68 GW cm^-2, highlighting a strong layer-dependent enhancement in nonlinear absorption. Additionally, monolayer muscovite exhibits an optical limiting threshold of 1.46 mJ cm^-2, outperforming graphene and other 2D dichalcogenides. This enhanced TPA arises from quantum confinement and intrinsic lattice defects that facilitate nonlinear optical transitions. Density functional theory reveals that liquid-phase exfoliation disrupts potassium interlayers and induces oxygen vacancies, generating mid-gap electronic states that significantly enhance TPA. These insights open new avenues for designing low-fluence, high-efficiency optical limiters using 2D silicates....

---

### 312. Energetically Favored One-Dimensional Moiré Superstructure in the Pseudo-Square Lattice GdTe3

**Authors:** Jieun Yeon, Kihyun Lee, Myeongjin Jang, Tae Keun Yun, Jongho Park, Changyoung Kim, Kwanpyo Kim

**Published:** 2025-08-13

**Category:** cond-mat.mtrl-sci

**ID:** 2508.09434v1

**Link:** [http://arxiv.org/abs/2508.09434v1](http://arxiv.org/abs/2508.09434v1)

**Summary:** Moiré engineering in layered crystals has recently gained considerable attention due to the discovery of various structural and physical phenomena, including interfacial reconstruction, superconductivity, magnetism, and distinctive optoelectronic properties. Nevertheless, most explored moiré systems have been limited to hexagonal lattices, thereby constraining a comprehensive understanding and technological application of moiré phenomena in general layered crystals. Here, we investigate GdTe3, a pseudo-tetragonal layered crystal, as a platform to explore unconventional moiré phenomena. GdTe3 exhibits a slight in-plane distortion correlated with the direction of charge density wave formation. Through vertical stacking of layers with different distortions-induced via a controlled strain/release process-we realize energetically favorable one-dimensional (1D) moiré superstructures. Using transmission electron microscopy (TEM), including high-resolution scanning TEM imaging, dark-field TEM imaging, and sample tilting experiments, we systematically examine stacking variations across the 1D moiré structure. Additionally, electron energy loss spectroscopy reveals modulations in electronic properties associated with the 1D moiré structure. Our findings expand the scope of moiré systems beyond conventional hexagonal twistronics, enabling exploration of moiré phenomena in low-symmetry van der Waals crystals....

---

### 313. Rational Inverse Reasoning

**Authors:** Ben Zandonati, Tomás Lozano-Pérez, Leslie Pack Kaelbling

**Published:** 2025-08-12

**Category:** cs.RO

**ID:** 2508.08983v1

**Link:** [http://arxiv.org/abs/2508.08983v1](http://arxiv.org/abs/2508.08983v1)

**Summary:** Humans can observe a single, imperfect demonstration and immediately generalize to very different problem settings. Robots, in contrast, often require hundreds of examples and still struggle to generalize beyond the training conditions. We argue that this limitation arises from the inability to recover the latent explanations that underpin intelligent behavior, and that these explanations can take the form of structured programs consisting of high-level goals, sub-task decomposition, and execution constraints. In this work, we introduce Rational Inverse Reasoning (RIR), a framework for inferring these latent programs through a hierarchical generative model of behavior. RIR frames few-shot imitation as Bayesian program induction: a vision-language model iteratively proposes structured symbolic task hypotheses, while a planner-in-the-loop inference scheme scores each by the likelihood of the observed demonstration under that hypothesis. This loop yields a posterior over concise, executable programs. We evaluate RIR on a suite of continuous manipulation tasks designed to test one-shot and few-shot generalization across variations in object pose, count, geometry, and layout. With as little as one demonstration, RIR infers the intended task structure and generalizes to novel settings, outperforming state-of-the-art vision-language model baselines....

---

### 314. Vacuum Dealloyed Brass as Li-Metal Battery Current Collector: Effect of Zinc and Porosity

**Authors:** Eric V Woods, Xinren Chen, Shaolou Wei, Yuwei Zhang, Alisson Kwiatkowski da Silva, Ayman A El-Zoka, J Manoj Prabhakar, Tim M Schwarz, Yongqiang Kang, Leonardo S Aota, Mahander P Singh, Katja Angenendt, Ozge Ozgun, Matic Jovivcevic-Klug, Patricia Jovivcevic-Klug, Christian Bross, Jian Liu, Rene de Kloe, Gerhard Dehm, Stefan Zaefferer, Yug Joshi, Baptiste Gault

**Published:** 2025-08-08

**Category:** cond-mat.mtrl-sci

**ID:** 2508.06015v2

**Link:** [http://arxiv.org/abs/2508.06015v2](http://arxiv.org/abs/2508.06015v2)

**Summary:** "Anode-free" lithium-metal batteries promise significantly higher energy density than conventional graphite-based lithium-ion batteries; however, lithium dendrite growth can lead to internal short circuits with associated safety risks. While porous current collectors can suppress dendrite growth, optimal porosity and composition remain unknown. Here, we show that the temperature during vapor phase dealloying (VPD) of alpha-brass (Cu63Zn37) controls the surface Zn concentration, decreasing from 8 percent to below 1 percent from 500 to 800 degrees C. The surface composition is controlled by the temperature-dependent diffusion. A battery cell maintains greater than 90 percent Coulombic efficiency (CE) over 100 cycles when the Zn content is the lowest, whereas the higher-Zn samples degraded to approximately 70 percent CE. The difference in surface composition has hence dramatic effects on battery performance, and our results demonstrate how precise compositional control enables stable lithium-metal battery operation, establishing about 1 atomic percent surface Zn as optimal for preventing capacity fading and uniform lithium plating, while establishing predictive relationships between processing temperature and surface composition. This work provides design rules for multifunctional current collectors and demonstrates scalable VPD production for next-generation batteries....

---

### 315. Flow Battery Manifold Design with Heterogeneous Inputs Through Generative Adversarial Neural Networks

**Authors:** Eric Seng, Hugh O'Connor, Adam Boyce, Josh J. Bailey, Anton van Beek

**Published:** 2025-08-12

**Category:** cs.LG

**ID:** 2508.08863v1

**Link:** [http://arxiv.org/abs/2508.08863v1](http://arxiv.org/abs/2508.08863v1)

**Summary:** Generative machine learning has emerged as a powerful tool for design representation and exploration. However, its application is often constrained by the need for large datasets of existing designs and the lack of interpretability about what features drive optimality. To address these challenges, we introduce a systematic framework for constructing training datasets tailored to generative models and demonstrate how these models can be leveraged for interpretable design. The novelty of this work is twofold: (i) we present a systematic framework for generating archetypes with internally homogeneous but mutually heterogeneous inputs that can be used to generate a training dataset, and (ii) we show how integrating generative models with Bayesian optimization can enhance the interpretability of the latent space of admissible designs. These findings are validated by using the framework to design a flow battery manifold, demonstrating that it effectively captures the space of feasible designs, including novel configurations while enabling efficient exploration. This work broadens the applicability of generative machine-learning models in system designs by enhancing quality and reliability....

---

### 316. $\text{M}^{2}$LLM: Multi-view Molecular Representation Learning with Large Language Models

**Authors:** Jiaxin Ju, Yizhen Zheng, Huan Yee Koh, Can Wang, Shirui Pan

**Published:** 2025-08-12

**Category:** cs.LG

**ID:** 2508.08657v1

**Link:** [http://arxiv.org/abs/2508.08657v1](http://arxiv.org/abs/2508.08657v1)

**Summary:** Accurate molecular property prediction is a critical challenge with wide-ranging applications in chemistry, materials science, and drug discovery. Molecular representation methods, including fingerprints and graph neural networks (GNNs), achieve state-of-the-art results by effectively deriving features from molecular structures. However, these methods often overlook decades of accumulated semantic and contextual knowledge. Recent advancements in large language models (LLMs) demonstrate remarkable reasoning abilities and prior knowledge across scientific domains, leading us to hypothesize that LLMs can generate rich molecular representations when guided to reason in multiple perspectives. To address these gaps, we propose $\text{M}^{2}$LLM, a multi-view framework that integrates three perspectives: the molecular structure view, the molecular task view, and the molecular rules view. These views are fused dynamically to adapt to task requirements, and experiments demonstrate that $\text{M}^{2}$LLM achieves state-of-the-art performance on multiple benchmarks across classification and regression tasks. Moreover, we demonstrate that representation derived from LLM achieves exceptional performance by leveraging two core functionalities: the generation of molecular embeddings through their encoding capabilities and the curation of molecular features through advanced reasoning processes....

---

### 317. Democracy of AI Numerical Weather Models: An Example of Global Forecasting with FourCastNetv2 Made by a University Research Lab Using GPU

**Authors:** Iman Khadir, Shane Stevenson, Henry Li, Kyle Krick, Abram Burrows, David Hall, Stan Posey, Samuel S. P. Shen

**Published:** 2025-04-23

**Category:** cs.LG

**ID:** 2504.17028v3

**Link:** [http://arxiv.org/abs/2504.17028v3](http://arxiv.org/abs/2504.17028v3)

**Summary:** This paper demonstrates the feasibility of democratizing AI-driven global weather forecasting models among university research groups by leveraging Graphics Processing Units (GPUs) and freely available AI models, such as NVIDIA's FourCastNetv2. FourCastNetv2 is an NVIDIA's advanced neural network for weather prediction and is trained on a 73-channel subset of the European Centre for Medium-Range Weather Forecasts (ECMWF) Reanalysis v5 (ERA5) dataset at single levels and different pressure levels. Although the training specifications for FourCastNetv2 are not released to the public, the training documentation of the model's first generation, FourCastNet, is available to all users. The training had 64 A100 GPUs and took 16 hours to complete. Although NVIDIA's models offer significant reductions in both time and cost compared to traditional Numerical Weather Prediction (NWP), reproducing published forecasting results presents ongoing challenges for resource-constrained university research groups with limited GPU availability. We demonstrate both (i) leveraging FourCastNetv2 to create predictions through the designated application programming interface (API) and (ii) utilizing NVIDIA hardware to train the original FourCastNet model. Further, this paper demonstrates the capabilities and limitations of NVIDIA A100's for resource-limited research groups in universities. We also explore data management, training efficiency, and model validation, highlighting the advantages and challenges of using limited high-performance computing resources. Consequently, this paper and its corresponding GitHub materials may serve as an initial guide for other university research groups and courses related to machine learning, climate science, and data science to develop research and education programs on AI weather forecasting, and hence help democratize the AI NWP in the digital economy....

---

### 318. Sliding Ferroelectric Metal with Ferrimagnetism

**Authors:** Zhenzhou Guo, Xiaodong Zhou, Wenhong Wang, Zhenxiang Cheng, Xiaotian Wang

**Published:** 2025-08-11

**Category:** cond-mat.mtrl-sci

**ID:** 2508.07947v1

**Link:** [http://arxiv.org/abs/2508.07947v1](http://arxiv.org/abs/2508.07947v1)

**Summary:** Two-dimensional (2D) sliding ferroelectric (FE) metals with ferrimagnetism represent a previously unexplored class of spintronic materials, where the interplay of ferroelectricity, metallicity, and magnetism enables strong magnetoelectric (ME) coupling and electrically tunable spintronic functionalities. Here, based on antiferromagnetic (AFM) metallic bilayers, we propose a general strategy for constructing 2D sliding FE ferrimagnetic (FiM) metals that can achieve tri-state switching, in which the FE polarization, spin splitting, and net magnetization are reversed simultaneously through FE switching. As a prototypical realization, we design a bilayer sliding FE metal with FiM order, derived from monolayer Fe5GeTe2-a van der Waals metal with intrinsic magnetic order close to room temperature. The system exhibits a FE transition from a nonpolar (NP) AFM phase to a FE FiM phase via interlayer sliding. The in-plane mirror symmetry breaking in FE metallic states lift the spin degeneracy that exists in the NP phase, leading to a sizable net magnetic moment and strong linear ME coupling. The interplay between metallicity and FE FiM gives rise to pronounced sign-reversible transport responses near the Fermi level, all of which can be fully electrically controlled by FE switching without reorienting the Néel order. Our results establish sliding FE metals with FiM as a promising platform for electrically reconfigurable, high-speed, and low-dissipation spintronic devices....

---

### 319. RNA-FrameFlow: Flow Matching for de novo 3D RNA Backbone Design

**Authors:** Rishabh Anand, Chaitanya K. Joshi, Alex Morehead, Arian R. Jamasb, Charles Harris, Simon V. Mathis, Kieran Didi, Rex Ying, Bryan Hooi, Pietro Liò

**Published:** 2024-06-19

**Category:** q-bio.BM

**ID:** 2406.13839v4

**Link:** [http://arxiv.org/abs/2406.13839v4](http://arxiv.org/abs/2406.13839v4)

**Summary:** We introduce RNA-FrameFlow, the first generative model for 3D RNA backbone design. We build upon SE(3) flow matching for protein backbone generation and establish protocols for data preparation and evaluation to address unique challenges posed by RNA modeling. We formulate RNA structures as a set of rigid-body frames and associated loss functions which account for larger, more conformationally flexible RNA backbones (13 atoms per nucleotide) vs. proteins (4 atoms per residue). Toward tackling the lack of diversity in 3D RNA datasets, we explore training with structural clustering and cropping augmentations. Additionally, we define a suite of evaluation metrics to measure whether the generated RNA structures are globally self-consistent (via inverse folding followed by forward folding) and locally recover RNA-specific structural descriptors. The most performant version of RNA-FrameFlow generates locally realistic RNA backbones of 40-150 nucleotides, over 40% of which pass our validity criteria as measured by a self-consistency TM-score >= 0.45, at which two RNAs have the same global fold. Open-source code: https://github.com/rish-16/rna-backbone-design...

---

### 320. Invert4TVG: A Temporal Video Grounding Framework with Inversion Tasks for Enhanced Action Understanding

**Authors:** Zhaoyu Chen, Hongnan Lin, Yongwei Nie, Fei Ma, Xuemiao Xu, Fei Yu, Chengjiang Long

**Published:** 2025-08-10

**Category:** cs.AI

**ID:** 2508.07388v1

**Link:** [http://arxiv.org/abs/2508.07388v1](http://arxiv.org/abs/2508.07388v1)

**Summary:** Temporal Video Grounding (TVG) seeks to localize video segments matching a given textual query. Current methods, while optimizing for high temporal Intersection-over-Union (IoU), often overfit to this metric, compromising semantic action understanding in the video and query, a critical factor for robust TVG. To address this, we introduce Inversion Tasks for TVG (Invert4TVG), a novel framework that enhances both localization accuracy and action understanding without additional data. Our approach leverages three inversion tasks derived from existing TVG annotations: (1) Verb Completion, predicting masked action verbs in queries from video segments; (2) Action Recognition, identifying query-described actions; and (3) Video Description, generating descriptions of video segments that explicitly embed query-relevant actions. These tasks, integrated with TVG via a reinforcement learning framework with well-designed reward functions, ensure balanced optimization of localization and semantics. Experiments show our method outperforms state-of-the-art approaches, achieving a 7.1\% improvement in R1@0.7 on Charades-STA for a 3B model compared to Time-R1. By inverting TVG to derive query-related actions from segments, our approach strengthens semantic understanding, significantly raising the ceiling of localization accuracy....

---

### 321. aLLoyM: A large language model for alloy phase diagram prediction

**Authors:** Yuna Oikawa, Guillaume Deffrennes, Taichi Abe, Ryo Tamura, Koji Tsuda

**Published:** 2025-07-30

**Category:** cond-mat.mtrl-sci

**ID:** 2507.22558v2

**Link:** [http://arxiv.org/abs/2507.22558v2](http://arxiv.org/abs/2507.22558v2)

**Summary:** Large Language Models (LLMs) are general-purpose tools with wide-ranging applications, including in materials science. In this work, we introduce aLLoyM, a fine-tuned LLM specifically trained on alloy compositions, temperatures, and their corresponding phase information. To develop aLLoyM, we curated question-and-answer (Q&A) pairs for binary and ternary phase diagrams using the open-source Computational Phase Diagram Database (CPDDB) and assessments based on CALPHAD (CALculation of PHAse Diagrams). We fine-tuned Mistral, an open-source pre-trained LLM, for two distinct Q&A formats: multiple-choice and short-answer. Benchmark evaluations demonstrate that fine-tuning substantially enhances performance on multiple-choice phase diagram questions. Moreover, the short-answer model of aLLoyM exhibits the ability to generate novel phase diagrams from its components alone, underscoring its potential to accelerate the discovery of previously unexplored materials systems. To promote further research and adoption, we have publicly released the short-answer fine-tuned version of aLLoyM, along with the complete benchmarking Q&A dataset, on Hugging Face....

---

### 322. VASPilot: MCP-Facilitated Multi-Agent Intelligence for Autonomous VASP Simulations

**Authors:** Jiaxuan Liu, Tiannian Zhu, Caiyuan Ye, Zhong Fang, Hongming Weng, Quansheng Wu

**Published:** 2025-08-09

**Category:** cond-mat.mtrl-sci

**ID:** 2508.07035v1

**Link:** [http://arxiv.org/abs/2508.07035v1](http://arxiv.org/abs/2508.07035v1)

**Summary:** Density-functional-theory (DFT) simulations with the Vienna Ab initio Simulation Package (VASP) are indispensable in computational materials science but often require extensive manual setup, monitoring, and postprocessing. Here, we introduce VASPilot, an open-source platform that fully automates VASP workflows via a multi-agent architecture built on the CrewAI framework and a standardized Model Context Protocol (MCP). VASPilot's agent suite handles every stage of a VASP study-from retrieving crystal structures and generating input files to submitting Slurm jobs, parsing error messages, and dynamically adjusting parameters for seamless restarts. A lightweight Flask-based web interface provides intuitive task submission, real-time progress tracking, and drill-down access to execution logs, structure visualizations, and plots. We validate VASPilot on both routine and advanced benchmarks: automated band-structure and density-of-states calculations (including on-the-fly symmetry corrections), plane-wave cutoff convergence tests, lattice-constant optimizations with various van der Waals corrections, and cross-material band-gap comparisons for transition-metal dichalcogenides. In all cases, VASPilot completed the missions reliably and without manual intervention. Moreover, its modular design allows easy extension to other DFT codes simply by deploying the appropriate MCP server. By offloading technical overhead, VASPilot enables researchers to focus on scientific discovery and accelerates high-throughput computational materials research....

---

### 323. Coulombic control of charge transfer in luminescent radicals with long-lived quartet states

**Authors:** Lujo Matasovic, Petri Murto, Shilong Yu, Wenzhao Wang, James D. Green, Giacomo Londi, Weixuan Zeng, Laura Brown, William K. Myers, David Beljonne, Yoann Olivier, Feng Li, Hugo Bronstein, Timothy J. H. Hele, Richard H. Friend, Sebastian Gorgon

**Published:** 2025-08-09

**Category:** cond-mat.mtrl-sci

**ID:** 2508.06945v1

**Link:** [http://arxiv.org/abs/2508.06945v1](http://arxiv.org/abs/2508.06945v1)

**Summary:** Excitons in organic materials are emerging as an attractive platform for tunable quantum technologies. Structures with near-degenerate doublet and triplet excitations in linked trityl radical, acene and carbazole units can host quartet states. These high spin states can be coherently manipulated, and later decay radiatively via the radical doublet transition. However, this requires controlling the deexcitation pathways of all metastable states. Here we establish design rules for efficient quartet generation in luminescent radicals, using different connection arrangements of the molecular units. We discover that electronic coupling strength between these units dictates luminescence and quartet formation yields, particularly through the energetics of an acene-radical charge transfer state, which we tune Coulombically. This state acts as a source of non-radiative decay when acene-radical separation is small, but facilitates doublet-quartet spin interconversion when acene-radical separation is large. Using these rules we report a radical-carbazole-acene material with 55% luminescence yield, where 94% of emitting excitons originate from the quartet at microsecond times. This reveals the central role of molecular topology in luminescent quantum materials....

---

### 324. Design of high-mobility p-type GaN via the piezomobility tensor

**Authors:** Jie-Cheng Chen, Joshua Leveillee, Chris G. Van de Walle, Feliciano Giustino

**Published:** 2025-08-08

**Category:** cond-mat.mtrl-sci

**ID:** 2508.06723v1

**Link:** [http://arxiv.org/abs/2508.06723v1](http://arxiv.org/abs/2508.06723v1)

**Summary:** Gallium nitride (GaN) is a wide-bandgap semiconductor of significant interest for applications in solid-state lighting, power electronics, and radio-frequency amplifiers. An important limitation of this semiconductor is its low intrinsic hole mobility, which hinders the development of \textit{p}-channel devices and the large-scale integration of GaN CMOS in next-generation electronics. Prior research has explored the use of strain to improve the hole mobility of GaN, but a systematic analysis of all possible strain conditions and their impact on the mobility is lacking. In this study, we introduce a piezomobility tensor notation to characterize the relationship between applied strain and hole mobility in GaN. To map the strain-dependence of the hole mobility, we solve the \textit{ab initio} Boltzmann transport equation, accounting for electron-phonon scattering and GW quasiparticle energy corrections. We show that there exist three optimal strain configurations, two uniaxial strains and one shear strain, that can lead to significant mobility enhancement. In particular, we predict room-temperature hole mobility of up to 164~\mob\ for 2\% uniaxial compression and 148~\mob\ for 2\% shear strain. Our methodology provides a general framework for investigating strain effects on the transport properties of semiconductors from first principles....

---

### 325. Multivariate Fields of Experts

**Authors:** Stanislas Ducotterd, Michael Unser

**Published:** 2025-08-08

**Category:** eess.IV

**ID:** 2508.06490v1

**Link:** [http://arxiv.org/abs/2508.06490v1](http://arxiv.org/abs/2508.06490v1)

**Summary:** We introduce the multivariate fields of experts, a new framework for the learning of image priors. Our model generalizes existing fields of experts methods by incorporating multivariate potential functions constructed via Moreau envelopes of the $\ell_\infty$-norm. We demonstrate the effectiveness of our proposal across a range of inverse problems that include image denoising, deblurring, compressed-sensing magnetic-resonance imaging, and computed tomography. The proposed approach outperforms comparable univariate models and achieves performance close to that of deep-learning-based regularizers while being significantly faster, requiring fewer parameters, and being trained on substantially fewer data. In addition, our model retains a relatively high level of interpretability due to its structured design....

---

### 326. Teaching LLMs How to Learn with Contextual Fine-Tuning

**Authors:** Younwoo Choi, Muhammad Adil Asif, Ziwen Han, John Willes, Rahul G. Krishnan

**Published:** 2025-03-12

**Category:** cs.LG

**ID:** 2503.09032v2

**Link:** [http://arxiv.org/abs/2503.09032v2](http://arxiv.org/abs/2503.09032v2)

**Summary:** Prompting Large Language Models (LLMs), or providing context on the expected model of operation, is an effective way to steer the outputs of such models to satisfy human desiderata after they have been trained. But in rapidly evolving domains, there is often need to fine-tune LLMs to improve either the kind of knowledge in their memory or their abilities to perform open ended reasoning in new domains. When human's learn new concepts, we often do so by linking the new material that we are studying to concepts we have already learned before. To that end, we ask, "can prompting help us teach LLMs how to learn". In this work, we study a novel generalization of instruction tuning, called contextual fine-tuning, to fine-tune LLMs. Our method leverages instructional prompts designed to mimic human cognitive strategies in learning and problem-solving to guide the learning process during training, aiming to improve the model's interpretation and understanding of domain-specific knowledge. We empirically demonstrate that this simple yet effective modification improves the ability of LLMs to be fine-tuned rapidly on new datasets both within the medical and financial domains....

---

### 327. MOFClassifier: A Machine Learning Approach for Validating Computation-Ready Metal-Organic Frameworks

**Authors:** Guobin Zhao, Pengyu Zhao, Yongchul G. Chung

**Published:** 2025-06-16

**Category:** physics.chem-ph

**ID:** 2506.14845v2

**Link:** [http://arxiv.org/abs/2506.14845v2](http://arxiv.org/abs/2506.14845v2)

**Summary:** The computational discovery and design of new crystalline materials, particularly metal-organic frameworks (MOFs), heavily relies on high-quality, computation-ready structural data. However, recent studies have revealed significant error rates within existing MOF databases, posing a critical data problem that hinders efficient high-throughput computational screening. While rule-based algorithms like MOSAEC, MOFChecker, and the Chen and Manz method (Chen-Manz) have been developed to address this, they often suffer from inherent limitations and misclassification of structures. To overcome this challenge, we developed MOFClassifier, a novel machine learning approach built upon a positive-unlabeled crystal graph convolutional neural network (PU-CGCNN) model. MOFClassifier learns intricate patterns from perfect crystal structures to predict a crystal-likeness score (CLscore), effectively classifying MOFs as computation-ready. Our model achieves a ROC value of 0.979 (previous best 0.912) and, importantly, can identify subtle structural and chemical errors that are undetectable by current rule-based methods. By accurately recovering previously misclassified false-negative structures, MOFClassifier reduces the risk of overlooking promising material candidates in large-scale computational screening campaigns. This user-friendly tool is freely available and has been integrated into the prepara-tion workflow for the updated CoRE MOF DB 2025 v1.0, contributing to accelerated computational discovery of MOF materials....

---

### 328. SERS Raman detection of the CO$_2$ Moisture Swing

**Authors:** Javier Mendez-Lozoya, Estrella Solis Mata, J. Jesus Velazquez Salazar, Alondra Hernandez Cedillo, Miguel Jose Yacaman, Jennifer L. Wade

**Published:** 2025-08-06

**Category:** cond-mat.mtrl-sci

**ID:** 2508.04893v1

**Link:** [http://arxiv.org/abs/2508.04893v1](http://arxiv.org/abs/2508.04893v1)

**Summary:** The development of scalable, energy-efficient carbon dioxide capture technologies is critical for achieving net-zero emissions. Moisture swing sorbents offer a promising alternative to traditional thermal regeneration methods by enabling reversible CO$_2$ binding through humidity-driven ion hydrolysis. In this study, we investigate the anion speciation dynamics in two classes of MS materials, an anion-exchange resin with bicarbonate anion and activated carbon impregnated with potassium bicarbonate salt using both sorption measurements and in situ surface-enhanced Raman spectroscopy. Ni coated Ag nanowires were employed as SERS substrates to enhance signal intensity and enable the real-time detection of carbonate , bicarbonate , and hydroxide species under controlled humidity conditions in both air and nitrogen atmospheres. The results reveal humidity-dependent interconversion between anionic species, with significant spectral shifts confirming the reversible hydrolysis reactions that drive the MS mechanism. Under humid conditions, we observed the depletion of bicarbonate signals and a concurrent increase in carbonate species, consistent with moisture-induced desorption of CO$_2$. These findings not only validate the mechanistic models of humidity-driven anion exchange in moisture swing sorbents but also demonstrate the practical potential of SERS as an operando diagnostic tool for monitoring CO$_2$ capture media. The ability to resolve and quantify the reversible transformation of carbonate, bicarbonate, and hydroxide ions under realistic environmental conditions provides valuable insight for the rational design, performance optimization, and quality control of next-generation sorbent materials for direct air capture applications....

---

### 329. Using Topology to Predict Electrides in the Solid State

**Authors:** Stefano Racioppi, Eva Zurek

**Published:** 2025-08-06

**Category:** cond-mat.mtrl-sci

**ID:** 2508.04548v1

**Link:** [http://arxiv.org/abs/2508.04548v1](http://arxiv.org/abs/2508.04548v1)

**Summary:** Electrides are characterized by electron density highly localized in interstitial sites, which do not coincide with the interatomic contacts. The rigorous quantum mechanical definition of electrides is based upon topological criteria derived from the electron density, and in particular the presence of non-nuclear attractors (NNAs). We employ these topological criteria in combination with crystal structure prediction methods (the XtalOpt evolutionary algorithm), to accelerate the discovery of crystalline electrides at ambient and non-ambient pressures. The localization and quantification of NNAs is used as the primary discriminator for the electride character of a solid within a multi-objective evolutionary structure search. We demonstrate the reliability of this approach through a comprehensive crystal structure prediction study of Ca5Pb3 at 20 GPa, a system previously theorized to exhibit electride character under compression. Our strategy could predict, and sort on-the-fly, several unknown low-enthalpy phases that possess NNAs in interstitial loci, such as the newly discovered P4/mmm structure. These results demonstrate how evolutionary algorithms, guided by rigorous topological descriptors, can be relied upon to effectively survey complex phases to find new electride candidates....

---

### 330. $β$-Irida-Graphene: A New 2D Carbon Allotrope for Sodium-Ion Battery Anodes

**Authors:** José A. S. Laranjeira, Kleuton A. L. Lima, Nicolas F. Martins, Luiz A. Ribeiro Junior, Douglas S. Galvão, Luis A. Cabral, Julio R. Sambrano

**Published:** 2025-08-06

**Category:** cond-mat.mtrl-sci

**ID:** 2508.04506v1

**Link:** [http://arxiv.org/abs/2508.04506v1](http://arxiv.org/abs/2508.04506v1)

**Summary:** The quest for sustainable and efficient energy storage has driven the exploration of sodium-ion batteries (SIBs) as promising alternatives to lithium-ion systems. However, the larger ionic radius of sodium poses intrinsic challenges such as slow diffusion and structural strain in conventional electrode materials. As a contribution to addressing these limitations, the \b{eta}-Irida-graphene ($β$-IG) is herein introduced, a novel two-dimensional (2D) carbon allotrope derived from Irida-graphene, featuring a diverse polygonal lattice of 3-, 4-, 6-, 8-, and 9-membered carbon rings. Through density functional theory and ab initio molecular dynamics simulations, $β$-IG demonstrated remarkable thermal, dynamical, and mechanical stability, coupled with intrinsic conductive character and efficient sodium-ion mobility (energy barriers < 0.30 eV). Furthermore, the adsorption of sodium ions was energetically favorable, delivering an impressive predicted specific capacity of 554.5 mAh/g. The reported findings highlight $β$-IG as a good potential anode candidate for next-generation SIBs, offering high-rate performance and structural robustness, and expanding the functional design space for advanced carbon-based electrode materials....

---

### 331. Undulation-induced moiré superlattices with 1D polarization domains and 1D flat bands in 2D bilayer semiconductors

**Authors:** Xingfu Li, Sunny Gupta, Boris I. Yakobson

**Published:** 2024-10-23

**Category:** cond-mat.mes-hall

**ID:** 2410.17548v2

**Link:** [http://arxiv.org/abs/2410.17548v2](http://arxiv.org/abs/2410.17548v2)

**Summary:** Two-dimensional (2D) materials have a high Föppl-von Kármán number and can be easily bent, much like a paper, making undulations a novel way to design distinct electronic phases. Through first-principles calculations, we reveal the formation of 1D polarization domains and 1D flat electronic bands by 1D bending modulation to a 2D bilayer semiconductor. Using 1D sinusoidal undulation of a hexagonal boron nitride (hBN) bilayer as an example, we demonstrate how undulation induces nonuniform shear patterns, creating regions with unique local stacking and vertical polarization akin to sliding-induced ferroelectrics observed in twisted moiré systems. This sliding-induced polarization is also observed in double-wall BN nanotubes due to curvature differences between inner and outer tubes. Furthermore, undulation generates a shear-induced 1D moiré pattern that perturbs electronic states, confining them into 1D quantum-well-like bands with kinetic energy quenched in modulation direction while dispersive in other directions (1D flat bands). This electronic confinement is attributed to modulated shear deformation potential resulting from tangential polarization due to the moiré pattern. Thus, bending modulation and interlayer shear offer an alternative avenue, termed "curvytronics", to induce exotic phenomena in 2D bilayer materials....

---

### 332. Curvature induced modifications of chirality and magnetic configuration in perpendicular magnetized films

**Authors:** David Raftrey, Dhritiman Bhattacharya, Colin Langton, Bradley Fugetta, Subhashree Satapathy, Olha Bezsmertna, Andrea Sorrentino, Denys Makarov, Gen Yin, Peter Fischer, Kai Liu

**Published:** 2025-06-06

**Category:** cond-mat.mtrl-sci

**ID:** 2506.05938v2

**Link:** [http://arxiv.org/abs/2506.05938v2](http://arxiv.org/abs/2506.05938v2)

**Summary:** Designing curvature in three-dimensional (3D) magnetic nanostructures enables controlled manipulation of local energy landscapes, allowing for the modification of noncollinear spin textures relevant for next-generation spintronic devices. In this study, we experimentally investigate 3D magnetization textures in a Co/Pd multilayer film, exhibiting strong perpendicular magnetic anisotropy (PMA), deposited onto curved Cu nanowire meshes with diameters as small as 50nm and lengths of several microns. Utilizing magnetic soft X-ray nanotomography, we achieve reconstructions of 3D magnetic domain patterns at approximately 30nm spatial resolution. This approach provides detailed information on both the orientation and magnitude of magnetization within the film. Our results reveal that interfacial anisotropy in the Co/Pd multilayers drives the magnetization towards the local surface normal. In contrast to typical labyrinth domains observed in planar films, the presence of curved nanowires significantly alters the domain structure, with domains preferentially aligning along the nanowire axis in close proximity, while adopting random orientations farther away. We report direct experimental observation of a curvature-induced Dzyaloshinskii-Moriya interaction (DMI), which is quantified to be approximately one-third of the intrinsic DMI in Co/Pd stacks. The curvature induced DMI enhances stability of Neel-type domain walls. These experimental observations are further supported by micromagnetic simulations. Altogether, our findings demonstrate that introducing curvature into magnetic nanostructures provides a powerful strategy for tailoring complex magnetic behaviors, paving the way for the design of advanced 3D racetrack memory and neuromorphic computing devices....

---

### 333. Physics-Constrained Fine-Tuning of Flow-Matching Models for Generation and Inverse Problems

**Authors:** Jan Tauberschmidt, Sophie Fellenz, Sebastian J. Vollmer, Andrew B. Duncan

**Published:** 2025-08-05

**Category:** cs.LG

**ID:** 2508.09156v1

**Link:** [http://arxiv.org/abs/2508.09156v1](http://arxiv.org/abs/2508.09156v1)

**Summary:** We present a framework for fine-tuning flow-matching generative models to enforce physical constraints and solve inverse problems in scientific systems. Starting from a model trained on low-fidelity or observational data, we apply a differentiable post-training procedure that minimizes weak-form residuals of governing partial differential equations (PDEs), promoting physical consistency and adherence to boundary conditions without distorting the underlying learned distribution. To infer unknown physical inputs, such as source terms, material parameters, or boundary data, we augment the generative process with a learnable latent parameter predictor and propose a joint optimization strategy. The resulting model produces physically valid field solutions alongside plausible estimates of hidden parameters, effectively addressing ill-posed inverse problems in a data-driven yet physicsaware manner. We validate our method on canonical PDE benchmarks, demonstrating improved satisfaction of PDE constraints and accurate recovery of latent coefficients. Our approach bridges generative modelling and scientific inference, opening new avenues for simulation-augmented discovery and data-efficient modelling of physical systems....

---

### 334. Discovery of Itinerant Magnetic Domain Wall and Quasiparticle Boundary State in Spin-Density-Waves

**Authors:** Yining Hu, Xu Wang, Chen Chen, Qingle Zhang, Dongming Zhao, Tianzhen Zhang, Chenxi Wang, Qiang-Hua Wang, Donglai Feng, Tong Zhang

**Published:** 2024-02-25

**Category:** cond-mat.str-el

**ID:** 2402.15999v3

**Link:** [http://arxiv.org/abs/2402.15999v3](http://arxiv.org/abs/2402.15999v3)

**Summary:** Conventional magnetic domain walls are characterized by reorientation of local spins. However, what occurs at the boundary of itinerant magnets is largely unknown. Here using spin-sensitive scanning tunneling microscopy, we investigated the microscopic domain wall structure of the spin-density-wave (SDW) state in a prototypical itinerant antiferromagnet - chromium (Cr). At the boundary of two incommensurate SDW domains, we found the spins undergo finite-scale decay rather than reorientation. This generates a double-Q SDW state, which is further evidenced by an accompanying second-order charge modulation. In the commensurate SDW domains, a clear SDW energy gap is observed. Interestingly, the screw dislocations induced half vortex and anti-vortex of SDW, paired by antiphase domain wall. The spin density vanished at such antiphase domain walls. Remarkably, for the first time we observed the SDW quasiparticle states at the boundary, resembling the Andreev bound states in superconductors. These unique SDW boundary structures can be viewed as consequences of local interference of two SDWs, either with different Q or reversed phases. Our findings thus reveal a new type of domain wall distinct to that of local moment magnetism, with a mechanism rooted in the itinerant nature of SDW....

---

### 335. Censored Sampling for Topology Design: Guiding Diffusion with Human Preferences

**Authors:** Euihyun Kim, Keun Park, Yeoneung Kim

**Published:** 2025-08-03

**Category:** cs.LG

**ID:** 2508.01589v1

**Link:** [http://arxiv.org/abs/2508.01589v1](http://arxiv.org/abs/2508.01589v1)

**Summary:** Recent advances in denoising diffusion models have enabled rapid generation of optimized structures for topology optimization. However, these models often rely on surrogate predictors to enforce physical constraints, which may fail to capture subtle yet critical design flaws such as floating components or boundary discontinuities that are obvious to human experts. In this work, we propose a novel human-in-the-loop diffusion framework that steers the generative process using a lightweight reward model trained on minimal human feedback. Inspired by preference alignment techniques in generative modeling, our method learns to suppress unrealistic outputs by modulating the reverse diffusion trajectory using gradients of human-aligned rewards. Specifically, we collect binary human evaluations of generated topologies and train classifiers to detect floating material and boundary violations. These reward models are then integrated into the sampling loop of a pre-trained diffusion generator, guiding it to produce designs that are not only structurally performant but also physically plausible and manufacturable. Our approach is modular and requires no retraining of the diffusion model. Preliminary results show substantial reductions in failure modes and improved design realism across diverse test conditions. This work bridges the gap between automated design generation and expert judgment, offering a scalable solution to trustworthy generative design....

---

### 336. Inversion-DPO: Precise and Efficient Post-Training for Diffusion Models

**Authors:** Zejian Li, Yize Li, Chenye Meng, Zhongni Liu, Yang Ling, Shengyuan Zhang, Guang Yang, Changyuan Yang, Zhiyuan Yang, Lingyun Sun

**Published:** 2025-07-14

**Category:** cs.CV

**ID:** 2507.11554v4

**Link:** [http://arxiv.org/abs/2507.11554v4](http://arxiv.org/abs/2507.11554v4)

**Summary:** Recent advancements in diffusion models (DMs) have been propelled by alignment methods that post-train models to better conform to human preferences. However, these approaches typically require computation-intensive training of a base model and a reward model, which not only incurs substantial computational overhead but may also compromise model accuracy and training efficiency. To address these limitations, we propose Inversion-DPO, a novel alignment framework that circumvents reward modeling by reformulating Direct Preference Optimization (DPO) with DDIM inversion for DMs. Our method conducts intractable posterior sampling in Diffusion-DPO with the deterministic inversion from winning and losing samples to noise and thus derive a new post-training paradigm. This paradigm eliminates the need for auxiliary reward models or inaccurate appromixation, significantly enhancing both precision and efficiency of training. We apply Inversion-DPO to a basic task of text-to-image generation and a challenging task of compositional image generation. Extensive experiments show substantial performance improvements achieved by Inversion-DPO compared to existing post-training methods and highlight the ability of the trained generative models to generate high-fidelity compositionally coherent images. For the post-training of compostitional image geneation, we curate a paired dataset consisting of 11,140 images with complex structural annotations and comprehensive scores, designed to enhance the compositional capabilities of generative models. Inversion-DPO explores a new avenue for efficient, high-precision alignment in diffusion models, advancing their applicability to complex realistic generation tasks. Our code is available at https://github.com/MIGHTYEZ/Inversion-DPO...

---

### 337. Terahertz spin-orbit torque as a drive of spin dynamics in insulating antiferromagnet Cr$_{2}$O$_{3}$

**Authors:** R. M. Dubrovin, Z. V. Gareeva, A. V. Kimel, A. K. Zvezdin

**Published:** 2025-07-31

**Category:** cond-mat.mtrl-sci

**ID:** 2507.23367v1

**Link:** [http://arxiv.org/abs/2507.23367v1](http://arxiv.org/abs/2507.23367v1)

**Summary:** Contrary to conventional wisdom that spin dynamics induced by current are exclusive to metallic magnets, we theoretically predict that such phenomena can also be realized in magnetic insulators, specifically in the magnetoelectric antiferromagnet $\mathrm{Cr}_{2}\mathrm{O}_{3}$. We reveal that the displacement current driven by the THz electric field is able to generate a N{é}el spin-orbit torque in this insulating system. By introducing an alternative electric dipole order parameter arising from the dipole moment at $\mathrm{Cr}^{3+}$ sites, we combine symmetry analysis with a Lagrangian approach and uncover that the displacement current couples to the antiferromagnetic spins and enables ultrafast control of antiferromagnetic order. The derived equations of motion show that this effect competes with the linear magnetoelectric response, offering a novel pathway for manipulating antiferromagnetic order in insulators. Our findings establish insulator antiferromagnets as a viable platform for electric field driven antiferromagnetic spintronics and provide general design principles for non-metallic spin-orbit torque materials....

---

### 338. Revisiting the cofactor conditions: Elimination of transition layers in compound domains

**Authors:** Mohd Tahseen, Vivekanand Dabade

**Published:** 2025-06-05

**Category:** cond-mat.mtrl-sci

**ID:** 2506.04754v2

**Link:** [http://arxiv.org/abs/2506.04754v2](http://arxiv.org/abs/2506.04754v2)

**Summary:** This paper investigates the conditions necessary for the elimination of transition layers at interfaces involving compound domains, extending the classical framework of cofactor conditions. Although cofactor conditions enable stress-free phase boundaries between Type I/II domains and austenite, their applicability to compound domains has remained limited. Here, we present a comprehensive theoretical framework to characterize all compatible interfaces, highlighting the fundamental importance of the commutation property among martensitic variants. By establishing necessary and sufficient algebraic conditions, referred to as extreme compatibility conditions, we demonstrate the simultaneous elimination of transition layers at phase interfaces for both Type I/II and compound laminates, across all volume fractions of the martensitic variants. We also investigate the possibility of achieving supercompatibility in non-conventional twins, recently observed in the NiMnGa system. The focus of our work is on cubic-to-orthorhombic and cubic-to-monoclinic~II phase transformations, for which the extreme compatibility conditions are explicitly derived and systematically analyzed. The theory predicts novel zero-elastic-energy microstructures, including an increased number of triple clusters, spearhead-shaped martensitic nuclei, stress-free inclusions of austenite within martensite, and distinctive four-fold martensitic clusters. This significantly expands the possible modes of forming stress-free interfaces between phases and reveals new energy-minimizing microstructures that can facilitate the nucleation of martensite within austenite and vice versa. These configurations highlight significant enhancements in transformation reversibility and material durability, guiding the rational design of next-generation shape memory alloys with optimized functional properties....

---

### 339. Controlling diverse robots by inferring Jacobian fields with deep networks

**Authors:** Sizhe Lester Li, Annan Zhang, Boyuan Chen, Hanna Matusik, Chao Liu, Daniela Rus, Vincent Sitzmann

**Published:** 2024-07-11

**Category:** cs.RO

**ID:** 2407.08722v2

**Link:** [http://arxiv.org/abs/2407.08722v2](http://arxiv.org/abs/2407.08722v2)

**Summary:** Mirroring the complex structures and diverse functions of natural organisms is a long-standing challenge in robotics. Modern fabrication techniques have greatly expanded the feasible hardware, but using these systems requires control software to translate the desired motions into actuator commands. Conventional robots can easily be modeled as rigid links connected by joints, but it remains an open challenge to model and control biologically inspired robots that are often soft or made of several materials, lack sensing capabilities, and may change their material properties with use. Here, we introduce a method that uses deep neural networks to map a video stream of a robot to its visuomotor Jacobian field (the sensitivity of all 3D points to the robot's actuators). Our method enables the control of robots from only a single camera, makes no assumptions about the robots' materials, actuation, or sensing, and is trained without expert intervention by observing the execution of random commands. We demonstrate our method on a diverse set of robot manipulators that vary in actuation, materials, fabrication, and cost. Our approach achieves accurate closed-loop control and recovers the causal dynamic structure of each robot. Because it enables robot control using a generic camera as the only sensor, we anticipate that our work will broaden the design space of robotic systems and serve as a starting point for lowering the barrier to robotic automation....

---

### 340. A Foundation Model for Material Fracture Prediction

**Authors:** Agnese Marcato, Aleksandra Pachalieva, Ryley G. Hill, Kai Gao, Xiaoyu Wang, Esteban Rougier, Zhou Lei, Vinamra Agrawal, Janel Chua, Qinjun Kang, Jeffrey D. Hyman, Abigail Hunter, Nathan DeBardeleben, Earl Lawrence, Hari Viswanathan, Daniel O'Malley, Javier E. Santos

**Published:** 2025-07-30

**Category:** cs.LG

**ID:** 2507.23077v1

**Link:** [http://arxiv.org/abs/2507.23077v1](http://arxiv.org/abs/2507.23077v1)

**Summary:** Accurately predicting when and how materials fail is critical to designing safe, reliable structures, mechanical systems, and engineered components that operate under stress. Yet, fracture behavior remains difficult to model across the diversity of materials, geometries, and loading conditions in real-world applications. While machine learning (ML) methods show promise, most models are trained on narrow datasets, lack robustness, and struggle to generalize. Meanwhile, physics-based simulators offer high-fidelity predictions but are fragmented across specialized methods and require substantial high-performance computing resources to explore the input space. To address these limitations, we present a data-driven foundation model for fracture prediction, a transformer-based architecture that operates across simulators, a wide range of materials (including plastic-bonded explosives, steel, aluminum, shale, and tungsten), and diverse loading conditions. The model supports both structured and unstructured meshes, combining them with large language model embeddings of textual input decks specifying material properties, boundary conditions, and solver settings. This multimodal input design enables flexible adaptation across simulation scenarios without changes to the model architecture. The trained model can be fine-tuned with minimal data on diverse downstream tasks, including time-to-failure estimation, modeling fracture evolution, and adapting to combined finite-discrete element method simulations. It also generalizes to unseen materials such as titanium and concrete, requiring as few as a single sample, dramatically reducing data needs compared to standard ML. Our results show that fracture prediction can be unified under a single model architecture, offering a scalable, extensible alternative to simulator-specific workflows....

---

### 341. Investigating the Invertibility of Multimodal Latent Spaces: Limitations of Optimization-Based Methods

**Authors:** Siwoo Park

**Published:** 2025-07-30

**Category:** cs.LG

**ID:** 2507.23010v1

**Link:** [http://arxiv.org/abs/2507.23010v1](http://arxiv.org/abs/2507.23010v1)

**Summary:** This paper investigates the inverse capabilities and broader utility of multimodal latent spaces within task-specific AI (Artificial Intelligence) models. While these models excel at their designed forward tasks (e.g., text-to-image generation, audio-to-text transcription), their potential for inverse mappings remains largely unexplored. We propose an optimization-based framework to infer input characteristics from desired outputs, applying it bidirectionally across Text-Image (BLIP, Flux.1-dev) and Text-Audio (Whisper-Large-V3, Chatterbox-TTS) modalities.
  Our central hypothesis posits that while optimization can guide models towards inverse tasks, their multimodal latent spaces will not consistently support semantically meaningful and perceptually coherent inverse mappings. Experimental results consistently validate this hypothesis. We demonstrate that while optimization can force models to produce outputs that align textually with targets (e.g., a text-to-image model generating an image that an image captioning model describes correctly, or an ASR model transcribing optimized audio accurately), the perceptual quality of these inversions is chaotic and incoherent. Furthermore, when attempting to infer the original semantic input from generative models, the reconstructed latent space embeddings frequently lack semantic interpretability, aligning with nonsensical vocabulary tokens.
  These findings highlight a critical limitation. multimodal latent spaces, primarily optimized for specific forward tasks, do not inherently possess the structure required for robust and interpretable inverse mappings. Our work underscores the need for further research into developing truly semantically rich and invertible multimodal latent spaces....

---

### 342. Meta-Designing Quantum Experiments with Language Models

**Authors:** Sören Arlt, Haonan Duan, Felix Li, Sang Michael Xie, Yuhuai Wu, Mario Krenn

**Published:** 2024-06-04

**Category:** quant-ph

**ID:** 2406.02470v2

**Link:** [http://arxiv.org/abs/2406.02470v2](http://arxiv.org/abs/2406.02470v2)

**Summary:** Artificial Intelligence (AI) can solve complex scientific problems beyond human capabilities, but the resulting solutions offer little insight into the underlying physical principles. One prominent example is quantum physics, where computers can discover experiments for the generation of specific quantum states, but it is unclear how finding general design concepts can be automated. Here, we address this challenge by training a transformer-based language model to create human-readable Python code, which solves an entire class of problems in a single pass. This strategy, which we call meta-design, enables scientists to gain a deeper understanding and extrapolate to larger experiments without additional optimization. To demonstrate the effectiveness of our approach, we uncover previously unknown experimental generalizations of important quantum states, e.g. from condensed matter physics. The underlying methodology of meta-design can naturally be extended to fields such as materials science or engineering....

---

### 343. Generating Heterogeneous Multi-dimensional Data : A Comparative Study

**Authors:** Michael Corbeau, Emmanuelle Claeys, Mathieu Serrurier, Pascale Zaraté

**Published:** 2025-06-30

**Category:** cs.LG

**ID:** 2507.00090v3

**Link:** [http://arxiv.org/abs/2507.00090v3](http://arxiv.org/abs/2507.00090v3)

**Summary:** Allocation of personnel and material resources is highly sensible in the case of firefighter interventions. This allocation relies on simulations to experiment with various scenarios. The main objective of this allocation is the global optimization of the firefighters response. Data generation is then mandatory to study various scenarios In this study, we propose to compare different data generation methods. Methods such as Random Sampling, Tabular Variational Autoencoders, standard Generative Adversarial Networks, Conditional Tabular Generative Adversarial Networks and Diffusion Probabilistic Models are examined to ascertain their efficacy in capturing the intricacies of firefighter interventions. Traditional evaluation metrics often fall short in capturing the nuanced requirements of synthetic datasets for real-world scenarios. To address this gap, an evaluation of synthetic data quality is conducted using a combination of domain-specific metrics tailored to the firefighting domain and standard measures such as the Wasserstein distance. Domain-specific metrics include response time distribution, spatial-temporal distribution of interventions, and accidents representation. These metrics are designed to assess data variability, the preservation of fine and complex correlations and anomalies such as event with a very low occurrence, the conformity with the initial statistical distribution and the operational relevance of the synthetic data. The distribution has the particularity of being highly unbalanced, none of the variables following a Gaussian distribution, adding complexity to the data generation process....

---

### 344. Gateways to Orbital and Spin Hall Effects in Rh-Doped Altermagnetic RuO$_2$

**Authors:** Lishu Zhang

**Published:** 2025-07-29

**Category:** cond-mat.mtrl-sci

**ID:** 2507.21480v1

**Link:** [http://arxiv.org/abs/2507.21480v1](http://arxiv.org/abs/2507.21480v1)

**Summary:** Ruthenium dioxide (RuO$_2$) has recently emerged as a prototypical material for exploring the fundamental properties of altermagnets. In this work, we investigate the impact of Rhodium (Rh) doping on the electronic and transport characteristics of altermagnetic RuO$_2$ using first-principles calculations. We show that Rh substitution at Ru sites modifies the spin-splitting of electronic bands across momentum space and reshapes the spin-resolved Fermi surface topology. These changes are found to significantly influence both the spin Hall and orbital Hall effects. In particular, we demonstrate that the orbital Berry curvature is strongly modulated by the doping concentration, opening new avenues for tuning orbital transport responses in multi-orbital systems without relying on strong spin-orbit coupling. Our results suggest that Rh-doped RuO$_2$ provides a versatile platform for engineering spin and orbital Hall effects in altermagnetic materials, and contributes to the growing efforts in designing next-generation orbitronic and spintronic devices....

---

### 345. Accurate Prediction of Tensorial Spectra Using Equivariant Graph Neural Network

**Authors:** Ting-Wei Hsu, Zhenyao Fang, Arun Bansil, Qimin Yan

**Published:** 2025-05-08

**Category:** cond-mat.mtrl-sci

**ID:** 2505.04862v3

**Link:** [http://arxiv.org/abs/2505.04862v3](http://arxiv.org/abs/2505.04862v3)

**Summary:** Optical spectroscopies provide a powerful tool for harnessing light-matter interactions for unraveling complex electronic features such as the flat bands and nontrivial topologies of materials. These insights are crucial for the development and optimization of optoelectronic devices, including solar cells, light-emitting diodes, and photodetectors, where device performance is closely connected with the nature of the underlying electronic spectrum. Realistic modeling of tensor optical responses in materials, which are computationally quite demanding, however, remains challenging. Here we introduce the Tensorial Spectra Equivariant Neural Network (TSENN), which is a equivariant graph neural network architecture that maps crystal structures directly to their full photon-frequency-dependent optical tensors. By encoding the isotropic sequential scalar components along with the anisotropic sequential tensor components into l = 0 and l = 2 spherical tensor components, TSENN ensures symmetry-aware predictions that are consistent with the constraints of crystalline symmetries of materials. Trained on a dataset of frequency-dependent permittivity tensors of 1,432 bulk semiconductors computed using first-principles methods, our model achieves a mean absolute error (MAE) of 21.181 millifarads per meter (mF/m), demonstrating its potential for efficient modeling of other related properties such as the optical conductivities. Our framework opens new avenues for rational data-driven design of anisotropic optical responses for accelerating materials discovery for advancing optoelectronic applications....

---

### 346. Guide your favorite protein sequence generative model

**Authors:** Junhao Xiong, Hunter Nisonoff, Maria Lukarska, Ishan Gaur, Luke M. Oltrogge, David F. Savage, Jennifer Listgarten

**Published:** 2025-05-07

**Category:** cs.LG

**ID:** 2505.04823v3

**Link:** [http://arxiv.org/abs/2505.04823v3](http://arxiv.org/abs/2505.04823v3)

**Summary:** Generative machine learning models on sequences are transforming protein engineering. However, no principled framework exists for conditioning these models on auxiliary information, such as experimental data, in a plug-and-play manner. Herein, we present ProteinGuide -- a principled and general method for conditioning -- by unifying a broad class of protein generative models under a single framework. We demonstrate the applicability of ProteinGuide by guiding two protein generative models, ProteinMPNN and ESM3, to generate amino acid and structure token sequences, conditioned on several user-specified properties such as enhanced stability, enzyme classes, and CATH-labeled folds. We also used ProteinGuide with inverse folding models and our own experimental assay to design adenine base editor sequences for high activity....

---

### 347. MIPS: a Multimodal Infinite Polymer Sequence Pre-training Framework for Polymer Property Prediction

**Authors:** Jiaxi Wang, Yaosen Min, Xun Zhu, Miao Li, Ji Wu

**Published:** 2025-07-27

**Category:** cs.LG

**ID:** 2507.20326v1

**Link:** [http://arxiv.org/abs/2507.20326v1](http://arxiv.org/abs/2507.20326v1)

**Summary:** Polymers, composed of repeating structural units called monomers, are fundamental materials in daily life and industry. Accurate property prediction for polymers is essential for their design, development, and application. However, existing modeling approaches, which typically represent polymers by the constituent monomers, struggle to capture the whole properties of polymer, since the properties change during the polymerization process. In this study, we propose a Multimodal Infinite Polymer Sequence (MIPS) pre-training framework, which represents polymers as infinite sequences of monomers and integrates both topological and spatial information for comprehensive modeling. From the topological perspective, we generalize message passing mechanism (MPM) and graph attention mechanism (GAM) to infinite polymer sequences. For MPM, we demonstrate that applying MPM to infinite polymer sequences is equivalent to applying MPM on the induced star-linking graph of monomers. For GAM, we propose to further replace global graph attention with localized graph attention (LGA). Moreover, we show the robustness of the "star linking" strategy through Repeat and Shift Invariance Test (RSIT). Despite its robustness, "star linking" strategy exhibits limitations when monomer side chains contain ring structures, a common characteristic of polymers, as it fails the Weisfeiler-Lehman~(WL) test. To overcome this issue, we propose backbone embedding to enhance the capability of MPM and LGA on infinite polymer sequences. From the spatial perspective, we extract 3D descriptors of repeating monomers to capture spatial information. Finally, we design a cross-modal fusion mechanism to unify the topological and spatial information. Experimental validation across eight diverse polymer property prediction tasks reveals that MIPS achieves state-of-the-art performance....

---

### 348. Machine-Learning-Assisted Photonic Device Development: A Multiscale Approach from Theory to Characterization

**Authors:** Yuheng Chen, Alexander Montes McNeil, Taehyuk Park, Blake A. Wilson, Vaishnavi Iyer, Michael Bezick, Jae-Ik Choi, Rohan Ojha, Pravin Mahendran, Daksh Kumar Singh, Geetika Chitturi, Peigang Chen, Trang Do, Alexander V. Kildishev, Vladimir M. Shalaev, Michael Moebius, Wenshan Cai, Yongmin Liu, Alexandra Boltasseva

**Published:** 2025-06-24

**Category:** physics.optics

**ID:** 2506.20056v2

**Link:** [http://arxiv.org/abs/2506.20056v2](http://arxiv.org/abs/2506.20056v2)

**Summary:** Photonic device development (PDD) has achieved remarkable success in designing and implementing new devices for controlling light across various wavelengths, scales, and applications, including telecommunications, imaging, sensing, and quantum information processing. PDD is an iterative, five-step process that consists of: i) deriving device behavior from design parameters, ii) simulating device performance, iii) finding the optimal candidate designs from simulations, iv) fabricating the optimal device, and v) measuring device performance. Classically, all these steps involve Bayesian optimization, material science, control theory, and direct physics-driven numerical methods. However, many of these techniques are computationally intractable, monetarily costly, or difficult to implement at scale. In addition, PDD suffers from large optimization landscapes, uncertainties in structural or optical characterization, and difficulties in implementing robust fabrication processes. However, the advent of machine learning over the past decade has provided novel, data-driven strategies for tackling these challenges, including surrogate estimators for speeding up computations, generative modeling for noisy measurement modeling and data augmentation, reinforcement learning for fabrication, and active learning for experimental physical discovery. In this review, we present a comprehensive perspective on these methods to enable machine-learning-assisted PDD (ML-PDD) for efficient design optimization with powerful generative models, fast simulation and characterization modeling under noisy measurements, and reinforcement learning for fabrication. This review will provide researchers from diverse backgrounds with valuable insights into this emerging topic, fostering interdisciplinary efforts to accelerate the development of complex photonic devices and systems....

---

### 349. AquiLLM: a RAG Tool for Capturing Tacit Knowledge in Research Groups

**Authors:** Chandler Campbell, Bernie Boscoe, Tuan Do

**Published:** 2025-07-25

**Category:** cs.IR

**ID:** 2508.05648v1

**Link:** [http://arxiv.org/abs/2508.05648v1](http://arxiv.org/abs/2508.05648v1)

**Summary:** Research groups face persistent challenges in capturing, storing, and retrieving knowledge that is distributed across team members. Although structured data intended for analysis and publication is often well managed, much of a group's collective knowledge remains informal, fragmented, or undocumented--often passed down orally through meetings, mentoring, and day-to-day collaboration. This includes private resources such as emails, meeting notes, training materials, and ad hoc documentation. Together, these reflect the group's tacit knowledge--the informal, experience-based expertise that underlies much of their work. Accessing this knowledge can be difficult, requiring significant time and insider understanding. Retrieval-augmented generation (RAG) systems offer promising solutions by enabling users to query and generate responses grounded in relevant source material. However, most current RAG-LLM systems are oriented toward public documents and overlook the privacy concerns of internal research materials. We introduce AquiLLM (pronounced ah-quill-em), a lightweight, modular RAG system designed to meet the needs of research groups. AquiLLM supports varied document types and configurable privacy settings, enabling more effective access to both formal and informal knowledge within scholarly groups....

---

### 350. Mask prior-guided denoising diffusion improves inverse protein folding

**Authors:** Peizhen Bai, Filip Miljković, Xianyuan Liu, Leonardo De Maria, Rebecca Croasdale-Wood, Owen Rackham, Haiping Lu

**Published:** 2024-12-10

**Category:** q-bio.BM

**ID:** 2412.07815v2

**Link:** [http://arxiv.org/abs/2412.07815v2](http://arxiv.org/abs/2412.07815v2)

**Summary:** Inverse protein folding generates valid amino acid sequences that can fold into a desired protein structure, with recent deep-learning advances showing strong potential and competitive performance. However, challenges remain, such as predicting elements with high structural uncertainty, including disordered regions. To tackle such low-confidence residue prediction, we propose a Mask-prior-guided denoising Diffusion (MapDiff) framework that accurately captures both structural information and residue interactions for inverse protein folding. MapDiff is a discrete diffusion probabilistic model that iteratively generates amino acid sequences with reduced noise, conditioned on a given protein backbone. To incorporate structural information and residue interactions, we develop a graph-based denoising network with a mask-prior pre-training strategy. Moreover, in the generative process, we combine the denoising diffusion implicit model with Monte-Carlo dropout to reduce uncertainty. Evaluation on four challenging sequence design benchmarks shows that MapDiff substantially outperforms state-of-the-art methods. Furthermore, the in silico sequences generated by MapDiff closely resemble the physico-chemical and structural characteristics of native proteins across different protein families and architectures....

---

### 351. Controlling Topological Defects in Polar Fluids via Reinforcement Learning

**Authors:** Abhinav Singh, Petros Koumoutsakos

**Published:** 2025-07-25

**Category:** cond-mat.soft

**ID:** 2507.19298v1

**Link:** [http://arxiv.org/abs/2507.19298v1](http://arxiv.org/abs/2507.19298v1)

**Summary:** Topological defects in active polar fluids exhibit complex dynamics driven by internally generated stresses, reflecting the deep interplay between topology, flow, and non-equilibrium hydrodynamics. Feedback control offers a powerful means to guide such systems, enabling transitions between dynamic states. We investigated closed-loop steering of integer-charged defects in a confined active fluid by modulating the spatial profile of activity. Using a continuum hydrodynamic model, we show that localized control of active stress induces flow fields that can reposition and direct defects along prescribed trajectories by exploiting non-linear couplings in the system. A reinforcement learning framework is used to discover effective control strategies that produce robust defect transport across both trained and novel trajectories. The results highlight how AI agents can learn the underlying dynamics and spatially structure activity to manipulate topological excitations, offering insights into the controllability of active matter and the design of adaptive, self-organized materials....

---

### 352. LLM-Feynman: Leveraging Large Language Models for Universal Scientific Formula and Theory Discovery

**Authors:** Zhilong Song, Qionghua Zhou, Chunjin Ren, Chongyi Ling, Minggang Ju, Jinlan Wang

**Published:** 2025-03-09

**Category:** cond-mat.mtrl-sci

**ID:** 2503.06512v2

**Link:** [http://arxiv.org/abs/2503.06512v2](http://arxiv.org/abs/2503.06512v2)

**Summary:** Distilling underlying principles from data has historically driven scientific breakthroughs. However, conventional data-driven machine learning often produces complex models that lack interpretability and generalization due to insufficient domain expertise. Here, we present LLM-Feynman, a novel framework that leverages large language models (LLMs) alongside systematic optimization to derive concise, interpretable formulas from data and domain knowledge. Our method integrates automated feature engineering, LLM-guided symbolic regression with self-evaluation, and Monte Carlo tree search to enhance formula discovery and clarity. The embedding of domain knowledge simplifies the formula, while self-evaluation based on this knowledge further minimizes prediction errors, surpassing conventional symbolic regression in accuracy and interpretability. Our LLM-Feynman successfully rediscovered over 90% of fundamental physical formulas and demonstrated its efficacy in key materials science applications, including classification of two-dimensional material and perovskite synthesizability and determination of the Green's function and screened Coulomb interaction bandgaps, and prediction of ionic conductivity in lithium solid-state electrolytes. By transcending mere data fitting through the integration of deep domain knowledge, this LLM-Feynman offers a transformative paradigm for the automated discovery of generalizable scientific formulas and theories across disciplines....

---

### 353. Artificial Intelligence for Science in Quantum, Atomistic, and Continuum Systems

**Authors:** Xuan Zhang, Limei Wang, Jacob Helwig, Youzhi Luo, Cong Fu, Yaochen Xie, Meng Liu, Yuchao Lin, Zhao Xu, Keqiang Yan, Keir Adams, Maurice Weiler, Xiner Li, Tianfan Fu, Yucheng Wang, Alex Strasser, Haiyang Yu, YuQing Xie, Xiang Fu, Shenglong Xu, Yi Liu, Yuanqi Du, Alexandra Saxton, Hongyi Ling, Hannah Lawrence, Hannes Stärk, Shurui Gui, Carl Edwards, Nicholas Gao, Adriana Ladera, Tailin Wu, Elyssa F. Hofgard, Aria Mansouri Tehrani, Rui Wang, Ameya Daigavane, Montgomery Bohde, Jerry Kurtin, Qian Huang, Tuong Phung, Minkai Xu, Chaitanya K. Joshi, Simon V. Mathis, Kamyar Azizzadenesheli, Ada Fang, Alán Aspuru-Guzik, Erik Bekkers, Michael Bronstein, Marinka Zitnik, Anima Anandkumar, Stefano Ermon, Pietro Liò, Rose Yu, Stephan Günnemann, Jure Leskovec, Heng Ji, Jimeng Sun, Regina Barzilay, Tommi Jaakkola, Connor W. Coley, Xiaoning Qian, Xiaofeng Qian, Tess Smidt, Shuiwang Ji

**Published:** 2023-07-17

**Category:** cs.LG

**ID:** 2307.08423v6

**Link:** [http://arxiv.org/abs/2307.08423v6](http://arxiv.org/abs/2307.08423v6)

**Summary:** Advances in artificial intelligence (AI) are fueling a new paradigm of discoveries in natural sciences. Today, AI has started to advance natural sciences by improving, accelerating, and enabling our understanding of natural phenomena at a wide range of spatial and temporal scales, giving rise to a new area of research known as AI for science (AI4Science). Being an emerging research paradigm, AI4Science is unique in that it is an enormous and highly interdisciplinary area. Thus, a unified and technical treatment of this field is needed yet challenging. This work aims to provide a technically thorough account of a subarea of AI4Science; namely, AI for quantum, atomistic, and continuum systems. These areas aim at understanding the physical world from the subatomic (wavefunctions and electron density), atomic (molecules, proteins, materials, and interactions), to macro (fluids, climate, and subsurface) scales and form an important subarea of AI4Science. A unique advantage of focusing on these areas is that they largely share a common set of challenges, thereby allowing a unified and foundational treatment. A key common challenge is how to capture physics first principles, especially symmetries, in natural systems by deep learning methods. We provide an in-depth yet intuitive account of techniques to achieve equivariance to symmetry transformations. We also discuss other common technical challenges, including explainability, out-of-distribution generalization, knowledge transfer with foundation and large language models, and uncertainty quantification. To facilitate learning and education, we provide categorized lists of resources that we found to be useful. We strive to be thorough and unified and hope this initial effort may trigger more community interests and efforts to further advance AI4Science....

---

### 354. Dis-GEN: Disordered crystal structure generation

**Authors:** Martin Hoffmann Petersen, Ruiming Zhu, Haiwen Dai, Savyasanchi Aggarwal, Nong Wei, Andy Paul Chen, Arghya Bhowmik, Juan Maria Garcia Lastra, Kedar Hippalgaonkar

**Published:** 2025-07-24

**Category:** cond-mat.mtrl-sci

**ID:** 2507.18275v1

**Link:** [http://arxiv.org/abs/2507.18275v1](http://arxiv.org/abs/2507.18275v1)

**Summary:** A wide range of synthesized crystalline inorganic materials exhibit compositional disorder, where multiple atomic species partially occupy the same crystallographic site. As a result, the physical and chemical properties of such materials are dependent on how the atomic species are distributed among the corresponding symmetrical sites, making them exceptionally challenging to model using computational methods. For this reason, existing generative models cannot handle the complexities of disordered inorganic crystals. To address this gap, we introduce Dis-GEN, a generative model based on an empirical equivariant representation, derived from theoretical crystallography methodology. Dis-GEN is capable of generating symmetry-consistent structures that accommodate both compositional disorder and vacancies. The model is uniquely trained on experimental structures from the Inorganic Crystal Structure Database (ICSD) - the world's largest database of identified inorganic crystal structures. We demonstrate that Dis-GEN can effectively generate disordered inorganic materials while preserving crystallographic symmetry throughout the generation process. This approach provides a critical check point for the systematic exploration and discovery of disordered functional materials, expanding the scope of generative modeling in materials science....

---

### 355. Compositional Tuning in NaxAlB14 via Diffusion Control

**Authors:** Mihiro Hoshino, Suguru Iwasaki, Shigeto Hirai, Yoshihiko Ihara, Tohru Sugahara, Haruhiko Morito, Masaya Fujioka

**Published:** 2025-07-24

**Category:** cond-mat.mtrl-sci

**ID:** 2507.18008v1

**Link:** [http://arxiv.org/abs/2507.18008v1](http://arxiv.org/abs/2507.18008v1)

**Summary:** A uniform Na distribution in NaxAlB14 was achieved using high-pressure diffusion control (HPDC), which promotes Na deintercalation through enhanced diffusion under high pressure, combined with post-annealing. NaxAlB14 with a non-stoichiometric Na composition is thermodynamically metastable, and conventional solid-state reactions with adjusted starting compositions typically result in the formation of stoichiometric NaAlB14 and side products. While HPDC alone typically leads to concentration gradients, intentionally halting the Na removal process before complete extraction, followed by annealing, enabled a uniform composition across the bulk. This allowed structural and electronic properties to be examined over a wide range of Na concentrations. As Na content decreased, electrical conductivity increased, and the optical band gap narrowed. NMR measurements showed an increase in the density of states at the Fermi level, consistent with DFT calculations predicting boron-related in-gap states. Boron vacancies at specific sites were found to generate deep levels near the band gap center, which can explain experimentally observed optical gap reduction. These results demonstrate that diffusion-controlling methods can be effectively applied to synthesize metastable compounds with tunable compositions in covalent frameworks. Furthermore, they provide a foundation for designing functional boride-based materials with adjustable electronic properties by controlling Na extraction and inducing defect formation....

---

### 356. A Supervised Machine Learning Framework for Multipactor Breakdown Prediction in High-Power Radio Frequency Devices and Accelerator Components: A Case Study in Planar Geometry

**Authors:** Asif Iqbal, John Verboncoeur, Peng Zhang

**Published:** 2025-07-23

**Category:** physics.acc-ph

**ID:** 2507.17881v1

**Link:** [http://arxiv.org/abs/2507.17881v1](http://arxiv.org/abs/2507.17881v1)

**Summary:** Multipactor is a nonlinear electron avalanche phenomenon that can severely impair the performance of high-power radio frequency (RF) devices and accelerator systems. Accurate prediction of multipactor susceptibility across different materials and operational regimes remains a critical yet computationally intensive challenge in accelerator component design and RF engineering. This study presents the first application of supervised machine learning (ML) for predicting multipactor susceptibility in two-surface planar geometries. A simulation-derived dataset spanning six distinct secondary electron yield (SEY) material profiles is used to train regression models - including Random Forest (RF), Extra Trees (ET), Extreme Gradient Boosting (XGBoost), and funnel-structured Multilayer Perceptrons (MLPs) - to predict the time-averaged electron growth rate, $δ_{avg}$. Performance is evaluated using Intersection over Union (IoU), Structural Similarity Index (SSIM), and Pearson correlation coefficient. Tree-based models consistently outperform MLPs in generalizing across disjoint material domains. MLPs trained using a scalarized objective function that combines IoU and SSIM during Bayesian hyperparameter optimization with 5-fold cross-validation outperform those trained with single-objective loss functions. Principal Component Analysis reveals that performance degradation for certain materials stems from disjoint feature-space distributions, underscoring the need for broader dataset coverage. This study demonstrates both the promise and limitations of ML-based multipactor prediction and lays the groundwork for accelerated, data-driven modeling in advanced RF and accelerator system design....

---

### 357. Deep Generative Learning of Magnetic Frustration in Artificial Spin Ice from Magnetic Force Microscopy Images

**Authors:** Arnab Neogi, Suryakant Mishra, Prasad P Iyer, Tzu-Ming Lu, Ezra Bussmann, Sergei Tretiak, Andrew Crandall Jones, Jian-Xin Zhu

**Published:** 2025-07-23

**Category:** cond-mat.dis-nn

**ID:** 2507.17726v1

**Link:** [http://arxiv.org/abs/2507.17726v1](http://arxiv.org/abs/2507.17726v1)

**Summary:** Increasingly large datasets of microscopic images with atomic resolution facilitate the development of machine learning methods to identify and analyze subtle physical phenomena embedded within the images. In this work, microscopic images of honeycomb lattice spin-ice samples serve as datasets from which we automate the calculation of net magnetic moments and directional orientations of spin-ice configurations. In the first stage of our workflow, machine learning models are trained to accurately predict magnetic moments and directions within spin-ice structures. Variational Autoencoders (VAEs), an emergent unsupervised deep learning technique, are employed to generate high-quality synthetic magnetic force microscopy (MFM) images and extract latent feature representations, thereby reducing experimental and segmentation errors. The second stage of proposed methodology enables precise identification and prediction of frustrated vertices and nanomagnetic segments, effectively correlating structural and functional aspects of microscopic images. This facilitates the design of optimized spin-ice configurations with controlled frustration patterns, enabling potential on-demand synthesis....

---

### 358. Dislocation saturation in slip rate driven processes and initial microstructure effects for large plastic deformation of crystals

**Authors:** Jalal Smiri, Oguz Umut Salman, Ioan R. Ionescu

**Published:** 2025-04-03

**Category:** cond-mat.mtrl-sci

**ID:** 2504.02413v4

**Link:** [http://arxiv.org/abs/2504.02413v4](http://arxiv.org/abs/2504.02413v4)

**Summary:** Dislocation-density-based crystal plasticity (CP) models are introduced to account for the microstructural changes throughout the deformation process, enabling more quantitative predictions of the deformation process compared to slip-system resistance-based plasticity models. In this work, we present a stability analysis of slip-rate-driven processes for some established dislocation density-based models, including the Kocks and Mecking (KM) model and its variants. Our analysis can be generalized to any type of dislocation density model, providing a broader framework for understanding the stability of such systems. We point out the existence of saturation dislocation densities and the essential role of initial dislocation density in distinguishing between hardening and softening responses. Since the initial microstructure, modeled through the dislocation density, could be related to the size or the sample preparation process, implicit size-dependent effects can also be inferred. To further explore these phenomena, we conduct numerical simulations of pillar compression using an Eulerian crystal plasticity framework. Our results show that dislocation-density-based CP models effectively capture microstructural evolution in small-scale materials, offering critical insights for the design of miniaturized mechanical devices and advanced materials in nanotechnology....

---

### 359. Reasoning-Driven Retrosynthesis Prediction with Large Language Models via Reinforcement Learning

**Authors:** Situo Zhang, Hanqi Li, Lu Chen, Zihan Zhao, Xuanze Lin, Zichen Zhu, Bo Chen, Xin Chen, Kai Yu

**Published:** 2025-07-23

**Category:** cs.CE

**ID:** 2507.17448v1

**Link:** [http://arxiv.org/abs/2507.17448v1](http://arxiv.org/abs/2507.17448v1)

**Summary:** Retrosynthesis planning, essential in organic synthesis and drug discovery, has greatly benefited from recent AI-driven advancements. Nevertheless, existing methods frequently face limitations in both applicability and explainability. Traditional graph-based and sequence-to-sequence models often lack generalized chemical knowledge, leading to predictions that are neither consistently accurate nor easily explainable. To address these challenges, we introduce RetroDFM-R, a reasoning-based large language model (LLM) designed specifically for chemical retrosynthesis. Leveraging large-scale reinforcement learning guided by chemically verifiable rewards, RetroDFM-R significantly enhances prediction accuracy and explainability. Comprehensive evaluations demonstrate that RetroDFM-R significantly outperforms state-of-the-art methods, achieving a top-1 accuracy of 65.0% on the USPTO-50K benchmark. Double-blind human assessments further validate the chemical plausibility and practical utility of RetroDFM-R's predictions. RetroDFM-R also accurately predicts multistep retrosynthetic routes reported in the literature for both real-world drug molecules and perovskite materials. Crucially, the model's explicit reasoning process provides human-interpretable insights, thereby enhancing trust and practical value in real-world retrosynthesis applications....

---

### 360. In Reverie Together: Ten Years of Mathematical Discovery with a Machine Collaborator

**Authors:** Randy Davila, Boris Brimkov, Ryan Pepper

**Published:** 2025-07-23

**Category:** cs.DM

**ID:** 2507.17780v1

**Link:** [http://arxiv.org/abs/2507.17780v1](http://arxiv.org/abs/2507.17780v1)

**Summary:** We present four open conjectures in graph theory generated by the automated conjecturing system \texttt{TxGraffiti}. Each conjecture is concise, grounded in natural graph invariants, and empirically validated across hundreds of graphs. Despite extensive effort, these statements remain unresolved--defying both proof and counterexample. They are not only mathematical challenges but creative expressions--born of symbolic pattern recognition and mathematician-defined heuristics, refined through years of human dialogue, and now offered back to the community as collaborative artifacts. These conjectures invite not only formal proof, but also reflection on how machines can evoke wonder, spark curiosity, and contribute to the raw material of discovery. By highlighting these problems, we aim to inspire both human mathematicians and AI systems to engage with them--not only to solve them, but to reflect on what it means when machines participate meaningfully in the creative process of mathematical thought....

---

### 361. Thermophysical and Mechanical Properties Prediction of Rear-earth High-entropy Pyrochlore Based on Deep-learning Potential

**Authors:** Yuxuan Wang, Guoqiang Lan, Huicong Chen, Jun Song

**Published:** 2025-07-22

**Category:** cond-mat.mtrl-sci

**ID:** 2507.17032v1

**Link:** [http://arxiv.org/abs/2507.17032v1](http://arxiv.org/abs/2507.17032v1)

**Summary:** High-entropy pyrochlore oxides possess ultra-low thermal conductivity and excellent high-temperature phase stability, making them promising candidate for next-generation thermal barrier coating (TBC) materials. However, reliable predictive models for such complex and disordered systems remain challenging. Ab initio methods, although accurate in describing anharmonic phonon-phonon interactions, struggle to capture the strong inherent phonon-disorder scattering in high-entropy systems. Moreover, the limited simulation cell size, hundreds of atoms, cannot fully represent the configurational complexity of high-entropy phases. On the other hand, classical molecular dynamics (MD) simulations lack accurate and transferable interatomic potentials, particularly in multi-component systems like high-entropy ceramics. In this work, we employed Deep Potential Molecular Dynamics (DPMD) to predict the thermophysical and mechanical properties of rare-earth high-entropy pyrochlore oxide system. The deep-potential (DP) model is trained on a limited dataset from ab initio molecular dynamics (AIMD) calculations, enabling large-scale molecular dynamics simulations with on-the-fly potential evaluations. This model not only achieves high accuracy in reproducing ab initio results but also demonstrates strong generalizability, making it applicable to medium-entropy ceramics containing the same constituent elements. Our study successfully develops a deep potential model for rare-earth pyrochlore systems and demonstrates that the deep-learning-based potential method offers a powerful computational approach for designing high-entropy TBC materials....

---

### 362. Diffusion Models for Solving Inverse Problems via Posterior Sampling with Piecewise Guidance

**Authors:** Saeed Mohseni-Sehdeh, Walid Saad, Kei Sakaguchi, Tao Yu

**Published:** 2025-07-22

**Category:** cs.LG

**ID:** 2507.18654v1

**Link:** [http://arxiv.org/abs/2507.18654v1](http://arxiv.org/abs/2507.18654v1)

**Summary:** Diffusion models are powerful tools for sampling from high-dimensional distributions by progressively transforming pure noise into structured data through a denoising process. When equipped with a guidance mechanism, these models can also generate samples from conditional distributions. In this paper, a novel diffusion-based framework is introduced for solving inverse problems using a piecewise guidance scheme. The guidance term is defined as a piecewise function of the diffusion timestep, facilitating the use of different approximations during high-noise and low-noise phases. This design is shown to effectively balance computational efficiency with the accuracy of the guidance term. Unlike task-specific approaches that require retraining for each problem, the proposed method is problem-agnostic and readily adaptable to a variety of inverse problems. Additionally, it explicitly incorporates measurement noise into the reconstruction process. The effectiveness of the proposed framework is demonstrated through extensive experiments on image restoration tasks, specifically image inpainting and super-resolution. Using a class conditional diffusion model for recovery, compared to the \pgdm baseline, the proposed framework achieves a reduction in inference time of \(25\%\) for inpainting with both random and center masks, and \(23\%\) and \(24\%\) for \(4\times\) and \(8\times\) super-resolution tasks, respectively, while incurring only negligible loss in PSNR and SSIM....

---

### 363. Rigidity control of general origami structures

**Authors:** Rongxuan Li, Gary P. T. Choi

**Published:** 2025-07-22

**Category:** cond-mat.soft

**ID:** 2507.16934v1

**Link:** [http://arxiv.org/abs/2507.16934v1](http://arxiv.org/abs/2507.16934v1)

**Summary:** Origami, the traditional paper-folding art, has inspired the modern design of numerous flexible structures in science and engineering. In particular, origami structures with different physical properties have been studied and utilized for various applications. More recently, several deterministic and stochastic approaches have been developed for controlling the rigidity or softness of the Miura-ori structures. However, the rigidity control of other origami structures is much less understood. In this work, we study the rigidity control of general origami structures via enforcing or relaxing the planarity condition of their polygonal facets. Specifically, by performing numerical simulations on a large variety of origami structures with different facet selection rules, we systematically analyze how the geometry and topology of different origami structures affect their degrees of freedom (DOF). We also propose a hypergeometric model based on the selection process to derive theoretical bounds for the probabilistic properties of the rigidity change, which allows us to identify key origami structural variables that theoretically govern the DOF evolution and thereby the critical rigidity percolation transition in general origami structures. Moreover, we develop a simple unified model that describes the relationship between the critical percolation density, the origami facet geometry, and the facet selection rules, which enables efficient prediction of the critical transition density for high-resolution origami structures. Altogether, our work highlights the intricate similarities and differences in the rigidity control of general origami structures, shedding light on the design of flexible mechanical metamaterials for practical applications....

---

### 364. Direct Visualization of a Disorder Driven Electronic Smectic Phase in Nonsymmorphic Square-Net Semimetal GdSbTe

**Authors:** Balaji Venkatesan, Syu-You Guan, Jen-Te Chang, Shiang-Bin Chiu, Po-Yuan Yang, Chih-Chuan Su, Tay-Rong Chang, Kalaivanan Raju, Raman Sankar, Somboon Fongchaiya, Ming-Wen Chu, Chia-Seng Chang, Guoqing Chang, Hsin Lin, Adrian Del Maestro, Ying-Jer Kao, Tien-Ming Chuang

**Published:** 2024-02-29

**Category:** cond-mat.str-el

**ID:** 2402.18893v4

**Link:** [http://arxiv.org/abs/2402.18893v4](http://arxiv.org/abs/2402.18893v4)

**Summary:** Electronic liquid crystal (ELC) phases are spontaneous symmetry breaking states believed to arise from strong electron correlation in quantum materials such as cuprates and iron pnictides. Here, we report a direct observation of a smectic phase in a weakly correlated nonsymmorphic square-net semimetal GdSbxTe2-x. Incommensurate smectic charge modulation and intense local unidirectional nanostructure, which coexist with Dirac fermions across Fermi level, are visualized by using spectroscopic imaging - scanning tunneling microscopy. As materials with highly mobile carriers are mostly weakly correlated, the discovery of such an ELC phase are anomalous and raise questions on the origin of their emergence. Specifically, we demonstrate how chemical substitution generates these symmetry breaking phases before the system undergoes a charge density wave (CDW) - orthorhombic structural transition. Our results highlight the importance of impurities in realizing ELC phases and present a new material platform for exploring the interplay among quenched disorder, Dirac fermions and electron correlation....

---

### 365. Depth Gives a False Sense of Privacy: LLM Internal States Inversion

**Authors:** Tian Dong, Yan Meng, Shaofeng Li, Guoxing Chen, Zhen Liu, Haojin Zhu

**Published:** 2025-07-22

**Category:** cs.CR

**ID:** 2507.16372v1

**Link:** [http://arxiv.org/abs/2507.16372v1](http://arxiv.org/abs/2507.16372v1)

**Summary:** Large Language Models (LLMs) are increasingly integrated into daily routines, yet they raise significant privacy and safety concerns. Recent research proposes collaborative inference, which outsources the early-layer inference to ensure data locality, and introduces model safety auditing based on inner neuron patterns. Both techniques expose the LLM's Internal States (ISs), which are traditionally considered irreversible to inputs due to optimization challenges and the highly abstract representations in deep layers. In this work, we challenge this assumption by proposing four inversion attacks that significantly improve the semantic similarity and token matching rate of inverted inputs. Specifically, we first develop two white-box optimization-based attacks tailored for low-depth and high-depth ISs. These attacks avoid local minima convergence, a limitation observed in prior work, through a two-phase inversion process. Then, we extend our optimization attack under more practical black-box weight access by leveraging the transferability between the source and the derived LLMs. Additionally, we introduce a generation-based attack that treats inversion as a translation task, employing an inversion model to reconstruct inputs. Extensive evaluation of short and long prompts from medical consulting and coding assistance datasets and 6 LLMs validates the effectiveness of our inversion attacks. Notably, a 4,112-token long medical consulting prompt can be nearly perfectly inverted with 86.88 F1 token matching from the middle layer of Llama-3 model. Finally, we evaluate four practical defenses that we found cannot perfectly prevent ISs inversion and draw conclusions for future mitigation design....

---

### 366. AutoMAT: A Hierarchical Framework for Autonomous Alloy Discovery

**Authors:** Penghui Yang, Chendong Zhao, Bijun Tang, Zhonghan Zhang, Xinrun Wang, Yanchen Deng, Yuhao Lu, Cuntai Guan, Zheng Liu, Bo An

**Published:** 2025-07-21

**Category:** cond-mat.mtrl-sci

**ID:** 2507.16005v1

**Link:** [http://arxiv.org/abs/2507.16005v1](http://arxiv.org/abs/2507.16005v1)

**Summary:** Alloy discovery is central to advancing modern industry but remains hindered by the vastness of compositional design space and the costly validation. Here, we present AutoMAT, a hierarchical and autonomous framework grounded in and validated by experiments, which integrates large language models, automated CALPHAD-based simulations, and AI-driven search to accelerate alloy design. Spanning the entire pipeline from ideation to validation, AutoMAT achieves high efficiency, accuracy, and interpretability without the need for manually curated large datasets. In a case study targeting a lightweight, high-strength alloy, AutoMAT identifies a titanium alloy with 8.1% lower density and comparable yield strength relative to the state-of-the-art reference, achieving the highest specific strength among all comparisons. In a second case targeting high-yield-strength high-entropy alloys, AutoMAT achieves a 28.2% improvement in yield strength over the base alloy. In both cases, AutoMAT reduces the discovery timeline from years to weeks, illustrating its potential as a scalable and versatile platform for next-generation alloy design....

---

### 367. Investigation of unsupervised and supervised hyperspectral anomaly detection

**Authors:** Mazharul Hossain, Aaron Robinson, Lan Wang, Chrysanthe Preza

**Published:** 2024-08-13

**Category:** eess.IV

**ID:** 2408.07114v2

**Link:** [http://arxiv.org/abs/2408.07114v2](http://arxiv.org/abs/2408.07114v2)

**Summary:** Hyperspectral sensing is a valuable tool for detecting anomalies and distinguishing between materials in a scene. Hyperspectral anomaly detection (HS-AD) helps characterize the captured scenes and separates them into anomaly and background classes. It is vital in agriculture, environment, and military applications such as RSTA (reconnaissance, surveillance, and target acquisition) missions. We previously designed an equal voting ensemble of hyperspectral unmixing and three unsupervised HS-AD algorithms. We later utilized a supervised classifier to determine the weights of a voting ensemble, creating a hybrid of heterogeneous unsupervised HS-AD algorithms with a supervised classifier in a model stacking, which improved detection accuracy. However, supervised classification methods usually fail to detect novel or unknown patterns that substantially deviate from those seen previously. In this work, we evaluate our technique and other supervised and unsupervised methods using general hyperspectral data to provide new insights....

---

### 368. Interfacially ordered phase states enable high-strength ductile eutectic Al alloys

**Authors:** Hemant Kumar, Praveen Kumar, Dierk Raabe, Baptiste Gault, Surendra Kumar Makineni

**Published:** 2025-07-11

**Category:** cond-mat.mtrl-sci

**ID:** 2507.08327v2

**Link:** [http://arxiv.org/abs/2507.08327v2](http://arxiv.org/abs/2507.08327v2)

**Summary:** Lightweight, high-strength structural materials are component enablers in transportation and aerospace, improving carbon footprint and fuel efficiency. Aluminium (Al)-based eutectics have property combinations that qualify them for such applications. However, they are prone to catastrophic failure because of insufficient load transfer across the interfaces between the brittle eutectic phase and the ductile matrix. Here we present a general solution to this problem by engineering these interfaces at the atomic scale, equipping them with excellent load transfer capabilities, thus qualifying such composites for lightweight structural applications. We demonstrate the approach by adding Zr to an Al-Gd-based hypoeutectic alloy, promoting the formation of a coherent Interfacial-Ordered-Phase (IOP) around the brittle Al3Gd eutectic phase and nanosized core-shell ordered precipitates in the primary Al matrix. This enables a 400% increase in tensile plasticity while retaining a high tensile strength of 295 MPa at room temperature and 130 MPa at 250C. This exceptional increase in formability is attributed to the ability of the IOP layer to prevent dislocations from accumulating at the weak fibre/matrix interfaces, avoiding stress concentrations that would otherwise initiate fibre breakage and debonding. The core-shell precipitates in Al cause a large number of dislocation cross/multiple-slips on different {111} planes, forming ultra-fine (10 nm) dislocation networks that leverage substantial plastic strain accumulation. The approach shows how atomic interface design overcomes the ductility limitations of lightweight high-strength ductile eutectic alloys for structural applications....

---

### 369. Visually Guided Decoding: Gradient-Free Hard Prompt Inversion with Language Models

**Authors:** Donghoon Kim, Minji Bae, Kyuhong Shim, Byonghyo Shim

**Published:** 2025-05-13

**Category:** cs.AI

**ID:** 2505.08622v2

**Link:** [http://arxiv.org/abs/2505.08622v2](http://arxiv.org/abs/2505.08622v2)

**Summary:** Text-to-image generative models like DALL-E and Stable Diffusion have revolutionized visual content creation across various applications, including advertising, personalized media, and design prototyping. However, crafting effective textual prompts to guide these models remains challenging, often requiring extensive trial and error. Existing prompt inversion approaches, such as soft and hard prompt techniques, are not so effective due to the limited interpretability and incoherent prompt generation. To address these issues, we propose Visually Guided Decoding (VGD), a gradient-free approach that leverages large language models (LLMs) and CLIP-based guidance to generate coherent and semantically aligned prompts. In essence, VGD utilizes the robust text generation capabilities of LLMs to produce human-readable prompts. Further, by employing CLIP scores to ensure alignment with user-specified visual concepts, VGD enhances the interpretability, generalization, and flexibility of prompt generation without the need for additional training. Our experiments demonstrate that VGD outperforms existing prompt inversion techniques in generating understandable and contextually relevant prompts, facilitating more intuitive and controllable interactions with text-to-image models....

---

### 370. OpenBreastUS: Benchmarking Neural Operators for Wave Imaging Using Breast Ultrasound Computed Tomography

**Authors:** Zhijun Zeng, Youjia Zheng, Hao Hu, Zeyuan Dong, Yihang Zheng, Xinliang Liu, Jinzhuo Wang, Zuoqiang Shi, Linfeng Zhang, Yubing Li, He Sun

**Published:** 2025-07-20

**Category:** cs.CV

**ID:** 2507.15035v1

**Link:** [http://arxiv.org/abs/2507.15035v1](http://arxiv.org/abs/2507.15035v1)

**Summary:** Accurate and efficient simulation of wave equations is crucial in computational wave imaging applications, such as ultrasound computed tomography (USCT), which reconstructs tissue material properties from observed scattered waves. Traditional numerical solvers for wave equations are computationally intensive and often unstable, limiting their practical applications for quasi-real-time image reconstruction. Neural operators offer an innovative approach by accelerating PDE solving using neural networks; however, their effectiveness in realistic imaging is limited because existing datasets oversimplify real-world complexity. In this paper, we present OpenBreastUS, a large-scale wave equation dataset designed to bridge the gap between theoretical equations and practical imaging applications. OpenBreastUS includes 8,000 anatomically realistic human breast phantoms and over 16 million frequency-domain wave simulations using real USCT configurations. It enables a comprehensive benchmarking of popular neural operators for both forward simulation and inverse imaging tasks, allowing analysis of their performance, scalability, and generalization capabilities. By offering a realistic and extensive dataset, OpenBreastUS not only serves as a platform for developing innovative neural PDE solvers but also facilitates their deployment in real-world medical imaging problems. For the first time, we demonstrate efficient in vivo imaging of the human breast using neural operator solvers....

---

### 371. Interplay of orbital and spin magnetization in trigonal tellurium

**Authors:** Zhenqi Hua, Chang Niu, Sandeep Joy, Pukun Tan, Gang Shi, Haoyang Liu, Jiaxing Guo, David Graf, Peide Ye, Cyprian Lewandowski, Peng Xiong

**Published:** 2025-07-18

**Category:** cond-mat.mtrl-sci

**ID:** 2507.14292v1

**Link:** [http://arxiv.org/abs/2507.14292v1](http://arxiv.org/abs/2507.14292v1)

**Summary:** Orbital effects, despite their fundamental significance and potential to engender novel physical phenomena and enable new applications, have long been underexplored compared to their spin counterparts. Recently, surging interest in the orbital degree of freedom has led to the discovery of a plethora of orbital-related effects, underscoring the need for a deeper understanding of their roles in quantum materials. Here, we report first experimental signatures of orbital magnetization in trigonal Tellurium, an elemental semiconductor with a unique helical crystal structure that serves as a natural platform for investigating orbital effects. Detailed angular dependent linear and nonlinear magnetotransport measurements, supported by theoretical Boltzmann transport analysis, reveal the coexistence of current-induced spin polarization and orbital magnetization. By disentangling the interplay between spin and orbital degrees of freedom, this work establishes a general framework for understanding orbital magnetization in chiral crystals and beyond, paving the way for its utilization in orbitronics and spintronics....

---

### 372. DONUT: Physics-aware Machine Learning for Real-time X-ray Nanodiffraction Analysis

**Authors:** Aileen Luo, Tao Zhou, Ming Du, Martin V. Holt, Andrej Singer, Mathew J. Cherukara

**Published:** 2025-07-18

**Category:** cs.LG

**ID:** 2507.14038v1

**Link:** [http://arxiv.org/abs/2507.14038v1](http://arxiv.org/abs/2507.14038v1)

**Summary:** Coherent X-ray scattering techniques are critical for investigating the fundamental structural properties of materials at the nanoscale. While advancements have made these experiments more accessible, real-time analysis remains a significant bottleneck, often hindered by artifacts and computational demands. In scanning X-ray nanodiffraction microscopy, which is widely used to spatially resolve structural heterogeneities, this challenge is compounded by the convolution of the divergent beam with the sample's local structure. To address this, we introduce DONUT (Diffraction with Optics for Nanobeam by Unsupervised Training), a physics-aware neural network designed for the rapid and automated analysis of nanobeam diffraction data. By incorporating a differentiable geometric diffraction model directly into its architecture, DONUT learns to predict crystal lattice strain and orientation in real-time. Crucially, this is achieved without reliance on labeled datasets or pre-training, overcoming a fundamental limitation for supervised machine learning in X-ray science. We demonstrate experimentally that DONUT accurately extracts all features within the data over 200 times more efficiently than conventional fitting methods....

---

### 373. QuantEIT: Ultra-Lightweight Quantum-Assisted Inference for Chest Electrical Impedance Tomography

**Authors:** Hao Fang, Sihao Teng, Hao Yu, Siyi Yuan, Huaiwu He, Zhe Liu, Yunjie Yang

**Published:** 2025-07-18

**Category:** cs.CV

**ID:** 2507.14031v1

**Link:** [http://arxiv.org/abs/2507.14031v1](http://arxiv.org/abs/2507.14031v1)

**Summary:** Electrical Impedance Tomography (EIT) is a non-invasive, low-cost bedside imaging modality with high temporal resolution, making it suitable for bedside monitoring. However, its inherently ill-posed inverse problem poses significant challenges for accurate image reconstruction. Deep learning (DL)-based approaches have shown promise but often rely on complex network architectures with a large number of parameters, limiting efficiency and scalability. Here, we propose an Ultra-Lightweight Quantum-Assisted Inference (QuantEIT) framework for EIT image reconstruction. QuantEIT leverages a Quantum-Assisted Network (QA-Net), combining parallel 2-qubit quantum circuits to generate expressive latent representations that serve as implicit nonlinear priors, followed by a single linear layer for conductivity reconstruction. This design drastically reduces model complexity and parameter number. Uniquely, QuantEIT operates in an unsupervised, training-data-free manner and represents the first integration of quantum circuits into EIT image reconstruction. Extensive experiments on simulated and real-world 2D and 3D EIT lung imaging data demonstrate that QuantEIT outperforms conventional methods, achieving comparable or superior reconstruction accuracy using only 0.2% of the parameters, with enhanced robustness to noise....

---

### 374. A collapsed interface approach to resolve grain boundaries in finite element simulations of polycrystalline diffusion

**Authors:** Lena Scholz, Yongliang Ou, Blazej Grabowski, Felix Fritzen

**Published:** 2025-04-14

**Category:** cond-mat.mtrl-sci

**ID:** 2504.10348v2

**Link:** [http://arxiv.org/abs/2504.10348v2](http://arxiv.org/abs/2504.10348v2)

**Summary:** Atomic diffusion affects the properties of various engineering materials, which predominantly occur in the polycrystalline state. A rigorous description of polycrystalline diffusion must therefore account for crystallographic defects, especially grain boundaries (GBs), whose structure and volume fraction - and hence the effective grain size - govern mass transport. Experiments and atomistic simulations consistently show that GBs can accelerate diffusion by up to several orders of magnitude and that fluxes along and across the interface are generally anisotropic. Conventional mesoscale models either neglect GBs or invoke idealized analytical corrections. Fully resolved finite-element meshes are accurate but computationally infeasible when nanometer-thin GB layers are involved. We introduce a collapsed-interface finite element that integrates the GB thickness analytically and embeds the result in a two-dimensional surface element. The formulation (i) treats in-plane and through-plane diffusivity independently, (ii) couples to the surrounding grain matrix without the need for mesh manipulations, and (iii) parametrizes both grain size and GB volume fraction via simple affine scalings, allowing systematic variation without remeshing. Effective diffusivity tensors are extracted by linear computational homogenization. The new finite element reproduces three-dimensional GB transport phenomena - channeled fluxes, concentration discontinuities - at a fraction of the computational cost of explicit models. Parametric studies spanning multiple orders of magnitude in GB diffusivity reveal four distinct diffusion regimes and quantify their impact on the overall response. The framework thus connects atomistic data and continuum predictions, providing an efficient tool for diffusion-driven design and optimization of polycrystalline materials....

---

### 375. SeWS/bilayer-SiC heterojunction: An S-scheme photocatalyst with high visible-light absorption, excellent carrier mobility and adjustable band gap

**Authors:** Liuzhu Yang, Wenhui Wan, Zhicui Wang, Qiuyue Ma, Yanfeng Ge, Yong Liu

**Published:** 2025-06-23

**Category:** cond-mat.mtrl-sci

**ID:** 2506.18380v3

**Link:** [http://arxiv.org/abs/2506.18380v3](http://arxiv.org/abs/2506.18380v3)

**Summary:** Vertically stacked heterojunctions have garnered significant attention for their tunable electronic structures and photocatalytic performance, making them promising candidates for next-generation nanodevices. Using first-principles calculations, we systematically investigate the electronic structure, optical characteristics, and charge transfer of WSSe/SiC heterojunctions. Our results reveal that SeWS/monolayer-SiC, SeWS/bilayer-SiC, and SWSe/monolayer-SiC exhibit type-II band alignment, whereas SWSe/bilayer-SiC displays type-I alignment. Notably, SeWS/bilayer-SiC possesses a direct bandgap, in contrast to the indirect bandgaps of the other three configurations. Remarkably, the SeWS/bilayer-SiC heterojunction demonstrates a high absorption coefficient ($10^{5}~\mathrm{cm}^{-1}$) in the visible range and exhibits exceptional anisotropy in carrier transport, with an outstanding hole mobility of $9.58 \times 10^{3}~\mathrm{cm}^{2}\,\mathrm{V}^{-1}\,\mathrm{s}^{-1}$ along the Y-direction. Furthermore, combining thermodynamic stability with an S-scheme charge transfer mechanism, this system exhibits superior redox capability for photocatalytic water splitting, achieving a high hydrogen evolution efficiency of 22.15%, which surpasses the commercial viability threshold (10\%). Furthermore, we demonstrate effective band gap modulation via external electric fields and biaxial strains, with optical absorption coefficients exhibiting strong strain dependence. This work provides fundamental insights into the design of WSSe/SiC heterojunctions for high-efficiency photocatalytic and tunable photodetector applications....

---

### 376. Utilizing a machine-learned potential to explore enhanced radiation tolerance in the MoNbTaVW high-entropy alloy

**Authors:** Jiahui Liu, Jesper Byggmastar, Zheyong Fan, Bing Bai, Ping Qian, Yanjing Su

**Published:** 2024-11-05

**Category:** cond-mat.mtrl-sci

**ID:** 2411.02834v3

**Link:** [http://arxiv.org/abs/2411.02834v3](http://arxiv.org/abs/2411.02834v3)

**Summary:** High-entropy alloys (HEAs) based on tungsten (W) have emerged as promising candidates for plasma-facing components in future fusion reactors, owing to their excellent irradiation resistance. In this study, we construct an efficient machine-learned interatomic potential for the MoNbTaVW quinary system. This potential achieves computational speeds comparable to the embedded-atom method (EAM) potential, allowing us to conduct a comprehensive investigation of the primary radiation damage through molecular dynamics simulations. Threshold displacement energies (TDEs) in the MoNbTaVW HEA are investigated and compared with pure metals. A series of displacement cascade simulations at primary knock-on atom energies ranging from 10 to 150 keV reveal significant differences in defect generation and clustering between MoNbTaVW HEA and pure W. In HEAs, we observe more surviving Frenkel pairs (FPs) but fewer and smaller interstitial clusters compared to W, indicating superior radiation tolerance. We propose extended damage models to quantify the radiation dose in the MoNbTaVW HEA, and suggest that one reason for their enhanced resistance is subcascade splitting, which reduces the formation of interstitial clusters. Our findings provide critical insights into the fundamental irradiation resistance mechanisms in refractory body-centered cubic alloys, offering guidance for the design of future radiation-tolerant materials....

---

### 377. Understanding Pan-Sharpening via Generalized Inverse

**Authors:** Shiqi Liu, Yihua Tan, Yutong Bai, Alan Yuille

**Published:** 2023-10-04

**Category:** cs.LG

**ID:** 2310.02718v3

**Link:** [http://arxiv.org/abs/2310.02718v3](http://arxiv.org/abs/2310.02718v3)

**Summary:** Pan-sharpening algorithms utilize a panchromatic image and a multispectral image to generate a high spatial and high spectral image. However, the optimizations of the algorithms are designed with different standards. We employ a simple matrix equation to describe the Pan-sharpening problem. The conditions for the existence of a solution and the acquisition of spectral and spatial resolution are discussed. A down-sampling enhancement method is introduced to improve the estimation of spatial and spectral down-sample matrices.
  Using generalized inverse theory, we discovered two kinds of solution spaces of generalized inverse matrix formulations, which correspond to the two prominent classes of Pan-sharpening methods: component substitution and multi-resolution analysis. Specifically, the Gram-Schmidt adaptive method is demonstrated to align with the generalized inverse matrix formulation of component substitution. A model prior of the generalized inverse matrix of the spectral function is rendered. Theoretical errors are analyzed. The diffusion prior is naturally embedded with the help of general solution spaces of the generalized inverse form, enabling the acquisition of refined Pan-sharpening results.
  Extensive experiments, including comparative, synthetic, real-data ablation and diffusion-related tests are conducted. The proposed methods produce qualitatively sharper and superior results in both synthetic and real experiments. The down-sampling enhancement method demonstrates quantitatively and qualitatively better outcomes in real-data experiments. The diffusion prior can significantly improve the performance of our methods across almost all evaluation measures.
  The generalized inverse matrix theory helps deepen the understanding of Pan-sharpening mechanisms....

---


<!-- ARXIV_PAPERS_END -->