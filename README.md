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

## New Papers (200)

*Last updated: 2025-07-16 13:01:48 (SGT)*

### 1. Quantum-Annealing Enhanced Machine Learning for Interpretable Phase Classification of High-Entropy Alloys

**Authors:** Diego Ibarra Hoyos, Gia-Wei Chern, Israel Klich, Joseph Poon

**Published:** 2025-07-14

**Category:** cond-mat.mtrl-sci

**ID:** 2507.10237v1

**Link:** [http://arxiv.org/abs/2507.10237v1](http://arxiv.org/abs/2507.10237v1)

**Summary:** High entropy alloys (HEAs) offer unprecedented compositional flexibility for
designing advanced materials, yet predicting their crystallographic phases
remains a key bottleneck due to limited data and complex phase formation
behavior. Here, we present a quantum-enhanced machine learning framework that
leverages quantum annealing to enhance phase classification in HEAs. Our
pipeline integrates Quantum Boosting (QBoost) for interpretable feature
selection and classification, with Quantum Support Vector Machines (QSVM) that
use quantum-enhanced kernels to capture nonlinear relationships between
physical descriptors. By reformulating both models as Quadratic Unconstrained
Binary Optimization (QUBO) problems, we exploit the efficient sampling
capabilities of quantum annealers to achieve rapid training and robust
generalization, demonstrating notable runtime reductions relative to classical
baselines in our setup. We target six key phases: FCC, BCC, Sigma, Laves,
Heusler, and AlXY B2, and benchmark model performance using both
cross-validation and a rigorously curated test set of prior experimentally
synthesized HEAs. The results confirm strong alignment between predicted and
measured phases. Our findings demonstrate that quantum-enhanced classifiers
match or exceed classical models in accuracy and offer insights grounded in
interpretable physical descriptors. This work constitutes an important step
toward practical quantum acceleration in materials discovery pipelines....

---

### 2. Open Materials Generation with Stochastic Interpolants

**Authors:** Philipp Hoellmer, Thomas Egg, Maya M. Martirossyan, Eric Fuemmeler, Zeren Shui, Amit Gupta, Pawan Prakash, Adrian Roitberg, Mingjie Liu, George Karypis, Mark Transtrum, Richard G. Hennig, Ellad B. Tadmor, Stefano Martiniani

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.02582v2

**Link:** [http://arxiv.org/abs/2502.02582v2](http://arxiv.org/abs/2502.02582v2)

**Summary:** The discovery of new materials is essential for enabling technological
advancements. Computational approaches for predicting novel materials must
effectively learn the manifold of stable crystal structures within an infinite
design space. We introduce Open Materials Generation (OMatG), a unifying
framework for the generative design and discovery of inorganic crystalline
materials. OMatG employs stochastic interpolants (SI) to bridge an arbitrary
base distribution to the target distribution of inorganic crystals via a broad
class of tunable stochastic processes, encompassing both diffusion models and
flow matching as special cases. In this work, we adapt the SI framework by
integrating an equivariant graph representation of crystal structures and
extending it to account for periodic boundary conditions in unit cell
representations. Additionally, we couple the SI flow over spatial coordinates
and lattice vectors with discrete flow matching for atomic species. We
benchmark OMatG's performance on two tasks: Crystal Structure Prediction (CSP)
for specified compositions, and 'de novo' generation (DNG) aimed at discovering
stable, novel, and unique structures. In our ground-up implementation of OMatG,
we refine and extend both CSP and DNG metrics compared to previous works. OMatG
establishes a new state of the art in generative modeling for materials
discovery, outperforming purely flow-based and diffusion-based implementations.
These results underscore the importance of designing flexible deep learning
frameworks to accelerate progress in materials science. The OMatG code is
available at https://github.com/FERMat-ML/OMatG....

---

### 3. MBFormer: A General Transformer-based Learning Paradigm for Many-body Interactions in Real Materials

**Authors:** Bowen Hou, Xian Xu, Jinyuan Wu, Diana Y. Qiu

**Published:** 2025-07-07

**Category:** cond-mat.mtrl-sci

**ID:** 2507.05480v1

**Link:** [http://arxiv.org/abs/2507.05480v1](http://arxiv.org/abs/2507.05480v1)

**Summary:** Recently, radical progress in machine learning (ML) has revolutionized
computational materials science, enabling unprecedentedly rapid materials
discovery and property prediction, but the quantum many-body problem -- which
is the key to understanding excited-state properties, ranging from transport to
optics -- remains challenging due to the complexity of the nonlocal and
energy-dependent interactions. Here, we propose a symmetry-aware, grid-free,
transformer-based model, MBFormer, that is designed to learn the entire
many-body hierarchy directly from mean-field inputs, exploiting the attention
mechanism to accurately capture many-body correlations between mean-field
states. As proof of principle, we demonstrate the capability of MBFormer in
predicting results based on the GW plus Bethe Salpeter equation (GW-BSE)
formalism, including quasiparticle energies, exciton energies, exciton
oscillator strengths, and exciton wavefunction distribution. Our model is
trained on a dataset of 721 two-dimensional materials from the C2DB database,
achieving state-of-the-art performance with a low prediction mean absolute
error (MAE) on the order of 0.1-0.2 eV for state-level quasiparticle and
exciton energies across different materials. Moreover, we show explicitly that
the attention mechanism plays a crucial role in capturing many-body
correlations. Our framework provides an end-to-end platform from ground states
to general many-body prediction in real materials, which could serve as a
foundation model for computational materials science....

---

### 4. $\varphi$-Adapt: A Physics-Informed Adaptation Learning Approach to 2D Quantum Material Discovery

**Authors:** Hoang-Quan Nguyen, Xuan Bac Nguyen, Sankalp Pandey, Tim Faltermeier, Nicholas Borys, Hugh Churchill, Khoa Luu

**Published:** 2025-07-07

**Category:** cs.CV

**ID:** 2507.05184v1

**Link:** [http://arxiv.org/abs/2507.05184v1](http://arxiv.org/abs/2507.05184v1)

**Summary:** Characterizing quantum flakes is a critical step in quantum hardware
engineering because the quality of these flakes directly influences qubit
performance. Although computer vision methods for identifying two-dimensional
quantum flakes have emerged, they still face significant challenges in
estimating flake thickness. These challenges include limited data, poor
generalization, sensitivity to domain shifts, and a lack of physical
interpretability. In this paper, we introduce one of the first Physics-informed
Adaptation Learning approaches to overcome these obstacles. We focus on two
main issues, i.e., data scarcity and generalization. First, we propose a new
synthetic data generation framework that produces diverse quantum flake samples
across various materials and configurations, reducing the need for
time-consuming manual collection. Second, we present $\varphi$-Adapt, a
physics-informed adaptation method that bridges the performance gap between
models trained on synthetic data and those deployed in real-world settings.
Experimental results show that our approach achieves state-of-the-art
performance on multiple benchmarks, outperforming existing methods. Our
proposed approach advances the integration of physics-based modeling and domain
adaptation. It also addresses a critical gap in leveraging synthesized data for
real-world 2D material analysis, offering impactful tools for deep learning and
materials science communities....

---

### 5. Machine Learning-Based Prediction of Metal-Organic Framework Materials: A Comparative Analysis of Multiple Models

**Authors:** Zhuo Zheng, Keyan Liu, Xiyuan Zhu

**Published:** 2025-07-06

**Category:** cs.LG

**ID:** 2507.04493v1

**Link:** [http://arxiv.org/abs/2507.04493v1](http://arxiv.org/abs/2507.04493v1)

**Summary:** Metal-organic frameworks (MOFs) have emerged as promising materials for
various applications due to their unique structural properties and versatile
functionalities. This study presents a comprehensive investigation of machine
learning approaches for predicting MOF material properties. We employed five
different machine learning models: Random Forest, XGBoost, LightGBM, Support
Vector Machine, and Neural Network, to analyze and predict MOF characteristics
using a dataset from the Kaggle platform. The models were evaluated using
multiple performance metrics, including RMSE, R^2, MAE, and cross-validation
scores. Results demonstrated that the Random Forest model achieved superior
performance with an R^2 value of 0.891 and RMSE of 0.152, significantly
outperforming other models. LightGBM showed remarkable computational
efficiency, completing training in 25.7 seconds while maintaining high
accuracy. Our comparative analysis revealed that ensemble learning methods
generally exhibited better performance than traditional single models in MOF
property prediction. This research provides valuable insights into the
application of machine learning in materials science and establishes a robust
framework for future MOF material design and property prediction....

---

### 6. TopoMAS: Large Language Model Driven Topological Materials Multiagent System

**Authors:** Baohua Zhang, Xin Li, Huangchao Xu, Zhong Jin, Quansheng Wu, Ce Li

**Published:** 2025-07-05

**Category:** cond-mat.mtrl-sci

**ID:** 2507.04053v1

**Link:** [http://arxiv.org/abs/2507.04053v1](http://arxiv.org/abs/2507.04053v1)

**Summary:** Topological materials occupy a frontier in condensed-matter physics thanks to
their remarkable electronic and quantum properties, yet their cross-scale
design remains bottlenecked by inefficient discovery workflows. Here, we
introduce TopoMAS (Topological materials Multi-Agent System), an interactive
human-AI framework that seamlessly orchestrates the entire materials-discovery
pipeline: from user-defined queries and multi-source data retrieval, through
theoretical inference and crystal-structure generation, to first-principles
validation. Crucially, TopoMAS closes the loop by autonomously integrating
computational outcomes into a dynamic knowledge graph, enabling continuous
knowledge refinement. In collaboration with human experts, it has already
guided the identification of novel topological phases SrSbO3, confirmed by
first-principles calculations. Comprehensive benchmarks demonstrate robust
adaptability across base Large Language Model, with the lightweight Qwen2.5-72B
model achieving 94.55% accuracy while consuming only 74.3-78.4% of tokens
required by Qwen3-235B and 83.0% of DeepSeek-V3's usage--delivering responses
twice as fast as Qwen3-235B. This efficiency establishes TopoMAS as an
accelerator for computation-driven discovery pipelines. By harmonizing rational
agent orchestration with a self-evolving knowledge graph, our framework not
only delivers immediate advances in topological materials but also establishes
a transferable, extensible paradigm for materials-science domain....

---

### 7. Synthesizable by Design: A Retrosynthesis-Guided Framework for Molecular Analog Generation

**Authors:** Shuan Chen, Gunwook Nam, Yousung Jung

**Published:** 2025-07-03

**Category:** physics.chem-ph

**ID:** 2507.02752v1

**Link:** [http://arxiv.org/abs/2507.02752v1](http://arxiv.org/abs/2507.02752v1)

**Summary:** The disconnect between AI-generated molecules with desirable properties and
their synthetic feasibility remains a critical bottleneck in computational drug
and material discovery. While generative AI has accelerated the proposal of
candidate molecules, many of these structures prove challenging or impossible
to synthesize using established chemical reactions. Here, we introduce
SynTwins, a novel retrosynthesis-guided molecular analog design framework that
designs synthetically accessible molecular analogs by emulating expert chemist
strategies through a three-step process: retrosynthesis, similar building block
searching, and virtual synthesis. In comparative evaluations, SynTwins
demonstrates superior performance in generating synthetically accessible
analogs compared to state-of-the-art machine learning models while maintaining
high structural similarity to original target molecules. Furthermore, when
integrated with existing molecule optimization frameworks, our hybrid approach
produces synthetically feasible molecules with property profiles comparable to
unconstrained molecule generators, yet its synthesizability ensured. Our
comprehensive benchmarking across diverse molecular datasets demonstrates that
SynTwins effectively bridges the gap between computational design and
experimental synthesis, providing a practical solution for accelerating the
discovery of synthesizable molecules with desired properties for a wide range
of applications....

---

### 8. Advancing Magnetic Materials Discovery -- A structure-based machine learning approach for magnetic ordering and magnetic moment prediction

**Authors:** Apoorv Verma, Junaid Jami, Amrita Bhattacharya

**Published:** 2025-07-02

**Category:** cond-mat.mtrl-sci

**ID:** 2507.01913v1

**Link:** [http://arxiv.org/abs/2507.01913v1](http://arxiv.org/abs/2507.01913v1)

**Summary:** Accurately predicting magnetic behavior across diverse materials systems
remains a longstanding challenge due to the complex interplay of structural and
electronic factors and is pivotal for the accelerated discovery and design of
next-generation magnetic materials. In this work, a refined descriptor is
proposed that significantly improves the prediction of two critical magnetic
properties -- magnetic ordering (Ferromagnetic vs. Ferrimagnetic) and magnetic
moment per atom -- using only the structural information of materials. Unlike
previous models limited to Mn-based or lanthanide-transition metal compounds,
the present approach generalizes across a diverse dataset of 5741 stable,
binary and ternary, ferromagnetic and ferrimagnetic compounds sourced from the
Materials Project. Leveraging an enriched elemental vector representation and
advanced feature engineering, including nonlinear terms and reduced matrix
sparsity, the LightGBM-based model achieves an accuracy of 82.4% for magnetic
ordering classification and balanced recall across FM and FiM classes,
addressing a key limitation in prior studies. The model predicts magnetic
moment per atom with a correlation coefficient of 0.93, surpassing the Hund's
matrix and orbital field matrix descriptors. Additionally, it accurately
estimates formation energy per atom, enabling assessment of both magnetic
behavior and material stability. This generalized and computationally efficient
framework offers a robust tool for high-throughput screening of magnetic
materials with tailored properties....

---

### 9. Rotational Sampling: A Plug-and-Play Encoder for Rotation-Invariant 3D Molecular GNNs

**Authors:** Dian Jin

**Published:** 2025-07-01

**Category:** cs.LG

**ID:** 2507.01073v1

**Link:** [http://arxiv.org/abs/2507.01073v1](http://arxiv.org/abs/2507.01073v1)

**Summary:** Graph neural networks (GNNs) have achieved remarkable success in molecular
property prediction. However, traditional graph representations struggle to
effectively encode the inherent 3D spatial structures of molecules, as
molecular orientations in 3D space introduce significant variability, severely
limiting model generalization and robustness. Existing approaches primarily
focus on rotation-invariant and rotation-equivariant methods. Invariant methods
often rely heavily on prior knowledge and lack sufficient generalizability,
while equivariant methods suffer from high computational costs. To address
these limitations, this paper proposes a novel plug-and-play 3D encoding module
leveraging rotational sampling. By computing the expectation over the SO(3)
rotational group, the method naturally achieves approximate rotational
invariance. Furthermore, by introducing a carefully designed post-alignment
strategy, strict invariance can be achieved without compromising performance.
Experimental evaluations on the QM9 and C10 Datasets demonstrate superior
predictive accuracy, robustness, and generalization performance compared to
existing methods. Moreover, the proposed approach maintains low computational
complexity and enhanced interpretability, providing a promising direction for
efficient and effective handling of 3D molecular information in drug discovery
and material design....

---

### 10. Process-aware and high-fidelity microstructure generation using stable diffusion

**Authors:** Hoang Cuong Phan, Minh Tien Tran, Chihun Lee, Hoheok Kim, Sehyok Oh, Dong-Kyu Kim, Ho Won Lee

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00459v1

**Link:** [http://arxiv.org/abs/2507.00459v1](http://arxiv.org/abs/2507.00459v1)

**Summary:** Synthesizing realistic microstructure images conditioned on processing
parameters is crucial for understanding process-structure relationships in
materials design. However, this task remains challenging due to limited
training micrographs and the continuous nature of processing variables. To
overcome these challenges, we present a novel process-aware generative modeling
approach based on Stable Diffusion 3.5 Large (SD3.5-Large), a state-of-the-art
text-to-image diffusion model adapted for microstructure generation. Our method
introduces numeric-aware embeddings that encode continuous variables (annealing
temperature, time, and magnification) directly into the model's conditioning,
enabling controlled image generation under specified process conditions and
capturing process-driven microstructural variations. To address data scarcity
and computational constraints, we fine-tune only a small fraction of the
model's weights via DreamBooth and Low-Rank Adaptation (LoRA), efficiently
transferring the pre-trained model to the materials domain. We validate realism
using a semantic segmentation model based on a fine-tuned U-Net with a VGG16
encoder on 24 labeled micrographs. It achieves 97.1% accuracy and 85.7% mean
IoU, outperforming previous methods. Quantitative analyses using physical
descriptors and spatial statistics show strong agreement between synthetic and
real microstructures. Specifically, two-point correlation and lineal-path
errors remain below 2.1% and 0.6%, respectively. Our method represents the
first adaptation of SD3.5-Large for process-aware microstructure generation,
offering a scalable approach for data-driven materials design....

---

### 11. Establishing baselines for generative discovery of inorganic crystals

**Authors:** Nathan J. Szymanski, Christopher J. Bartel

**Published:** 2025-01-04

**Category:** cond-mat.mtrl-sci

**ID:** 2501.02144v2

**Link:** [http://arxiv.org/abs/2501.02144v2](http://arxiv.org/abs/2501.02144v2)

**Summary:** Generative artificial intelligence offers a promising avenue for materials
discovery, yet its advantages over traditional methods remain unclear. In this
work, we introduce and benchmark two baseline approaches - random enumeration
of charge-balanced prototypes and data-driven ion exchange of known compounds -
against four generative techniques based on diffusion models, variational
autoencoders, and large language models. Our results show that established
methods such as ion exchange are better at generating novel materials that are
stable, although many of these closely resemble known compounds. In contrast,
generative models excel at proposing novel structural frameworks and, when
sufficient training data is available, can more effectively target properties
such as electronic band gap and bulk modulus. To enhance the performance of
both the baseline and generative approaches, we implement a post-generation
screening step in which all proposed structures are passed through stability
and property filters from pre-trained machine learning models including
universal interatomic potentials. This low-cost filtering step leads to
substantial improvement in the success rates of all methods, remains
computationally efficient, and ultimately provides a practical pathway toward
more effective generative strategies for materials discovery. By establishing
baselines for comparison, this work highlights opportunities for continued
advancement of generative models, especially for the targeted generation of
novel materials that are thermodynamically stable....

---

### 12. deCIFer: Crystal Structure Prediction from Powder Diffraction Data using Autoregressive Language Models

**Authors:** Frederik Lizak Johansen, Ulrik Friis-Jensen, Erik Bjørnager Dam, Kirsten Marie Ørnsbjerg Jensen, Rocío Mercado, Raghavendra Selvan

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.02189v3

**Link:** [http://arxiv.org/abs/2502.02189v3](http://arxiv.org/abs/2502.02189v3)

**Summary:** Novel materials drive progress across applications from energy storage to
electronics. Automated characterization of material structures with machine
learning methods offers a promising strategy for accelerating this key step in
material design. In this work, we introduce an autoregressive language model
that performs crystal structure prediction (CSP) from powder diffraction data.
The presented model, deCIFer, generates crystal structures in the widely used
Crystallographic Information File (CIF) format and can be conditioned on powder
X-ray diffraction (PXRD) data. Unlike earlier works that primarily rely on
high-level descriptors like composition, deCIFer is also able to use
diffraction data to perform CSP. We train deCIFer on nearly 2.3M crystal
structures and validate on diverse sets of PXRD patterns for characterizing
challenging inorganic crystal systems. Qualitative checks and quantitative
assessments using the residual weighted profile show that deCIFer produces
structures that more accurately match the target diffraction data. Notably,
deCIFer can achieve a 94% match rate on test data. deCIFer bridges experimental
diffraction data with computational CSP, lending itself as a powerful tool for
crystal structure characterization....

---

### 13. Mic-hackathon 2024: Hackathon on Machine Learning for Electron and Scanning Probe Microscopy

**Authors:** Utkarsh Pratiush, Austin Houston, Kamyar Barakati, Aditya Raghavan, Dasol Yoon, Harikrishnan KP, Zhaslan Baraissov, Desheng Ma, Samuel S. Welborn, Mikolaj Jakowski, Shawn-Patrick Barhorst, Alexander J. Pattison, Panayotis Manganaris, Sita Sirisha Madugula, Sai Venkata Gayathri Ayyagari, Vishal Kennedy, Ralph Bulanadi, Michelle Wang, Kieran J. Pang, Ian Addison-Smith, Willy Menacho, Horacio V. Guzman, Alexander Kiefer, Nicholas Furth, Nikola L. Kolev, Mikhail Petrov, Viktoriia Liu, Sergey Ilyev, Srikar Rairao, Tommaso Rodani, Ivan Pinto-Huguet, Xuli Chen, Josep Cruañes, Marta Torrens, Jovan Pomar, Fanzhi Su, Pawan Vedanti, Zhiheng Lyu, Xingzhi Wang, Lehan Yao, Amir Taqieddin, Forrest Laskowski, Xiangyu Yin, Yu-Tsun Shao, Benjamin Fein-Ashley, Yi Jiang, Vineet Kumar, Himanshu Mishra, Yogesh Paul, Adib Bazgir, Rama chandra Praneeth Madugula, Yuwen Zhang, Pravan Omprakash, Jian Huang, Eric Montufar-Morales, Vivek Chawla, Harshit Sethi, Jie Huang, Lauri Kurki, Grace Guinan, Addison Salvador, Arman Ter-Petrosyan, Madeline Van Winkle, Steven R. Spurgeon, Ganesh Narasimha, Zijie Wu, Richard Liu, Yongtao Liu, Boris Slautin, Andrew R Lupini, Rama Vasudevan, Gerd Duscher, Sergei V. Kalinin

**Published:** 2025-06-10

**Category:** cond-mat.mtrl-sci

**ID:** 2506.08423v2

**Link:** [http://arxiv.org/abs/2506.08423v2](http://arxiv.org/abs/2506.08423v2)

**Summary:** Microscopy is a primary source of information on materials structure and
functionality at nanometer and atomic scales. The data generated is often
well-structured, enriched with metadata and sample histories, though not always
consistent in detail or format. The adoption of Data Management Plans (DMPs) by
major funding agencies promotes preservation and access. However, deriving
insights remains difficult due to the lack of standardized code ecosystems,
benchmarks, and integration strategies. As a result, data usage is inefficient
and analysis time is extensive. In addition to post-acquisition analysis, new
APIs from major microscope manufacturers enable real-time, ML-based analytics
for automated decision-making and ML-agent-controlled microscope operation.
Yet, a gap remains between the ML and microscopy communities, limiting the
impact of these methods on physics, materials discovery, and optimization.
Hackathons help bridge this divide by fostering collaboration between ML
researchers and microscopy experts. They encourage the development of novel
solutions that apply ML to microscopy, while preparing a future workforce for
instrumentation, materials science, and applied ML. This hackathon produced
benchmark datasets and digital twins of microscopes to support community growth
and standardized workflows. All related code is available at GitHub:
https://github.com/KalininGroup/Mic-hackathon-2024-codes-publication/tree/1.0.0.1...

---

### 14. Exploring the Capabilities of the Frontier Large Language Models for Nuclear Energy Research

**Authors:** Ahmed Almeldein, Mohammed Alnaggar, Rick Archibald, Tom Beck, Arpan Biswas, Rike Bostelmann, Wes Brewer, Chris Bryan, Christopher Calle, Cihangir Celik, Rajni Chahal, Jong Youl Choi, Arindam Chowdhury, Mark Cianciosa, Franklin Curtis, Gregory Davidson, Sebastian De Pascuale, Lisa Fassino, Ana Gainaru, Yashika Ghai, Luke Gibson, Qian Gong, Christopher Greulich, Scott Greenwood, Cory Hauck, Ehab Hassan, Rinkle Juneja, Soyoung Kang, Scott Klasky, Atul Kumar, Vineet Kumar, Paul Laiu, Calvin Lear, Yan-Ru Lin, Jono McConnell, Furkan Oz, Rishi Pillai, Anant Raj, Pradeep Ramuhalli, Marie Romedenne, Samantha Sabatino, José Salcedo-Pérez, Nathan D. See, Arpan Sircar, Punam Thankur, Tim Younkin, Xiao-Ying Yu, Prashant Jain, Tom Evans, Prasanna Balaprakash

**Published:** 2025-06-10

**Category:** physics.comp-ph

**ID:** 2506.19863v2

**Link:** [http://arxiv.org/abs/2506.19863v2](http://arxiv.org/abs/2506.19863v2)

**Summary:** The AI for Nuclear Energy workshop at Oak Ridge National Laboratory evaluated
the potential of Large Language Models (LLMs) to accelerate fusion and fission
research. Fourteen interdisciplinary teams explored diverse nuclear science
challenges using ChatGPT, Gemini, Claude, and other AI models over a single
day. Applications ranged from developing foundation models for fusion reactor
control to automating Monte Carlo simulations, predicting material degradation,
and designing experimental programs for advanced reactors. Teams employed
structured workflows combining prompt engineering, deep research capabilities,
and iterative refinement to generate hypotheses, prototype code, and research
strategies. Key findings demonstrate that LLMs excel at early-stage
exploration, literature synthesis, and workflow design, successfully
identifying research gaps and generating plausible experimental frameworks.
However, significant limitations emerged, including difficulties with novel
materials designs, advanced code generation for modeling and simulation, and
domain-specific details requiring expert validation. The successful outcomes
resulted from expert-driven prompt engineering and treating AI as a
complementary tool rather than a replacement for physics-based methods. The
workshop validated AI's potential to accelerate nuclear energy research through
rapid iteration and cross-disciplinary synthesis while highlighting the need
for curated nuclear-specific datasets, workflow automation, and specialized
model development. These results provide a roadmap for integrating AI tools
into nuclear science workflows, potentially reducing development cycles for
safer, more efficient nuclear energy systems while maintaining rigorous
scientific standards....

---

### 15. Symmetry Classification of Magnetic Orders and Emergence of Spin-Orbit Magnetism

**Authors:** Yuntian Liu, Xiaobing Chen, Yutong Yu, Qihang Liu

**Published:** 2025-06-25

**Category:** cond-mat.mtrl-sci

**ID:** 2506.20739v1

**Link:** [http://arxiv.org/abs/2506.20739v1](http://arxiv.org/abs/2506.20739v1)

**Summary:** Magnetism, a fundamental concept predating condensed matter physics, has
achieved significant advancements in recent decades, driven by its potential
for next-generation storage devices. Meanwhile, the classification of magnetic
orders, even for the most fundamental concepts like ferromagnetism (FM) and
antiferromagnetism (AFM), has encountered unprecedented challenges since the
discovery of unconventional magnets and advancements in antiferromagnetic
spintronics. Here, we present a rigorous classification of magnetic order using
state-of-the-art spin space group (SSG) theory. Based on whether the net
magnetic moment is constrained to zero by SSG, magnetic order is unambiguously
dichotomized into FM (including ferrimagnetism) and AFM. Additionally, we
classify AFM geometries into four categories -- primary, bi-color, spiral, and
multi-axial -- based on periodic spin propagation beyond the symmetry
operations of magnetic space groups. We then introduce a distinct magnetic
phase, dubbed spin-orbit magnetism, characterized by its unique behavior
involving the spin-orbit coupling (SOC) order parameter and SOC-driven phase
transition. We further create an oriented SSG description, i.e., SSG with a
fixed magnetic configuration, apply the framework to 2,065 experimentally
validated magnetic materials in MAGNDATA database, and identify over 220
spin-orbit magnets with distinct spin and orbital magnetization mechanisms.
Implemented by the online program FINDSPINGROUP, our work establishes a
universal symmetry standard for magnetic order classification, offering new
understandings of unconventional magnets and broad applicability in spintronics
and quantum material design....

---

### 16. Massive Atomic Diversity: a compact universal dataset for atomistic machine learning

**Authors:** Arslan Mazitov, Sofiia Chorna, Guillaume Fraux, Marnik Bercx, Giovanni Pizzi, Sandip De, Michele Ceriotti

**Published:** 2025-06-24

**Category:** cond-mat.mtrl-sci

**ID:** 2506.19674v1

**Link:** [http://arxiv.org/abs/2506.19674v1](http://arxiv.org/abs/2506.19674v1)

**Summary:** The development of machine-learning models for atomic-scale simulations has
benefited tremendously from the large databases of materials and molecular
properties computed in the past two decades using electronic-structure
calculations. More recently, these databases have made it possible to train
universal models that aim at making accurate predictions for arbitrary atomic
geometries and compositions. The construction of many of these databases was
however in itself aimed at materials discovery, and therefore targeted
primarily to sample stable, or at least plausible, structures and to make the
most accurate predictions for each compound - e.g. adjusting the calculation
details to the material at hand. Here we introduce a dataset designed
specifically to train machine learning models that can provide reasonable
predictions for arbitrary structures, and that therefore follows a different
philosophy. Starting from relatively small sets of stable structures, the
dataset is built to contain massive atomic diversity (MAD) by aggressively
distorting these configurations, with near-complete disregard for the stability
of the resulting configurations. The electronic structure details, on the other
hand, are chosen to maximize consistency rather than to obtain the most
accurate prediction for a given structure, or to minimize computational effort.
The MAD dataset we present here, despite containing fewer than 100k structures,
has already been shown to enable training universal interatomic potentials that
are competitive with models trained on traditional datasets with two to three
orders of magnitude more structures. We describe in detail the philosophy and
details of the construction of the MAD dataset. We also introduce a
low-dimensional structural latent space that allows us to compare it with other
popular datasets and that can be used as a general-purpose materials
cartography tool....

---

### 17. Machine Learning-Driven Insights into Excitonic Effects in 2D Materials

**Authors:** Ahsan Javed, Sajid Ali

**Published:** 2025-01-02

**Category:** cond-mat.mtrl-sci

**ID:** 2501.01092v2

**Link:** [http://arxiv.org/abs/2501.01092v2](http://arxiv.org/abs/2501.01092v2)

**Summary:** Understanding excitonic effects in two-dimensional (2D) materials is critical
for advancing their potential in next-generation electronic and photonic
devices. In this study, we introduce a machine learning (ML)-based framework to
predict exciton binding energies in 2D materials, offering a computationally
efficient alternative to traditional methods such as many-body perturbation
theory (GW) and the Bethe-Salpeter equation. Leveraging data from the
Computational 2D Materials Database (C2DB), our ML models establish connections
between cheaply available material descriptors and complex excitonic
properties, significantly accelerating the screening process for materials with
pronounced excitonic effects. Additionally, Bayesian optimization with Gaussian
process regression was employed to efficiently filter materials with largest
exciton binding energies, further enhancing the discovery process. Although
developed for 2D systems, this approach is versatile and can be extended to
three-dimensional materials, broadening its applicability in materials
discovery....

---

### 18. Efficient Crystal Structure Prediction Using Genetic Algorithm and Universal Neural Network Potential

**Authors:** Takuya Shibayama, Hideaki Imamura, Katsuhiko Nishimra, Kohei Shinohara, Chikashi Shinagawa, So Takamoto, Ju Li

**Published:** 2025-03-27

**Category:** cond-mat.mtrl-sci

**ID:** 2503.21201v2

**Link:** [http://arxiv.org/abs/2503.21201v2](http://arxiv.org/abs/2503.21201v2)

**Summary:** Crystal structure prediction (CSP) is crucial for identifying stable crystal
structures in given systems and is a prerequisite for computational atomistic
simulations. Recent advances in neural network potentials (NNPs) have reduced
the computational cost of CSP. However, searching for stable crystal structures
across the entire composition space in multicomponent systems remains a
significant challenge. Here, we propose a novel genetic algorithm (GA) -based
CSP method using a universal NNP. Our GA-based methods are designed to
efficiently expand convex hull volumes while preserving the diversity of
crystal structures. This approach draws inspiration from the similarity between
convex hull updates and Pareto front evolution in multi-objective optimization.
Our evaluation shows that the present method outperforms the symmetry-aware
random structure generation, achieving a larger convex hull with fewer trials.
We demonstrated that our approach, combined with the developed universal NNP
(PFP), can accurately reproduce and explore phase diagrams obtained through DFT
calculations; this indicates the validity of PFP across a wide range of crystal
structures and element combinations. This study, which integrates a universal
NNP with a GA-based CSP method, highlights the promise of these methods in
materials discovery....

---

### 19. Nature Language Model: Deciphering the Language of Nature for Scientific Discovery

**Authors:** Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan-Jyue Chen, Zekun Guo, Yeqi Bai, Pan Deng, Yaosen Min, Ziheng Lu, Hongxia Hao, Han Yang, Jielan Li, Chang Liu, Jia Zhang, Jianwei Zhu, Ran Bi, Kehan Wu, Wei Zhang, Kaiyuan Gao, Qizhi Pei, Qian Wang, Xixian Liu, Yanting Li, Houtian Zhu, Yeqing Lu, Mingqian Ma, Zun Wang, Tian Xie, Krzysztof Maziarz, Marwin Segler, Zhao Yang, Zilong Chen, Yu Shi, Shuxin Zheng, Lijun Wu, Chen Hu, Peggy Dai, Tie-Yan Liu, Haiguang Liu, Tao Qin

**Published:** 2025-02-11

**Category:** cs.AI

**ID:** 2502.07527v3

**Link:** [http://arxiv.org/abs/2502.07527v3](http://arxiv.org/abs/2502.07527v3)

**Summary:** Foundation models have revolutionized natural language processing and
artificial intelligence, significantly enhancing how machines comprehend and
generate human languages. Inspired by the success of these foundation models,
researchers have developed foundation models for individual scientific domains,
including small molecules, materials, proteins, DNA, RNA and even cells.
However, these models are typically trained in isolation, lacking the ability
to integrate across different scientific domains. Recognizing that entities
within these domains can all be represented as sequences, which together form
the "language of nature", we introduce Nature Language Model (NatureLM), a
sequence-based science foundation model designed for scientific discovery.
Pre-trained with data from multiple scientific domains, NatureLM offers a
unified, versatile model that enables various applications including: (i)
generating and optimizing small molecules, proteins, RNA, and materials using
text instructions; (ii) cross-domain generation/design, such as
protein-to-molecule and protein-to-RNA generation; and (iii) top performance
across different domains, matching or surpassing state-of-the-art specialist
models. NatureLM offers a promising generalist approach for various scientific
tasks, including drug discovery (hit generation/optimization, ADMET
optimization, synthesis), novel material design, and the development of
therapeutic proteins or nucleotides. We have developed NatureLM models in
different sizes (1 billion, 8 billion, and 46.7 billion parameters) and
observed a clear improvement in performance as the model size increases....

---

### 20. AI-Assisted Rapid Crystal Structure Generation Towards a Target Local Environment

**Authors:** Osman Goni Ridwan, Sylvain Pitié, Monish Soundar Raj, Dong Dai, Gilles Frapper, Hongfei Xue, Qiang Zhu

**Published:** 2025-06-09

**Category:** cond-mat.mtrl-sci

**ID:** 2506.08224v1

**Link:** [http://arxiv.org/abs/2506.08224v1](http://arxiv.org/abs/2506.08224v1)

**Summary:** In the field of material design, traditional crystal structure prediction
approaches require extensive structural sampling through computationally
expensive energy minimization methods using either force fields or quantum
mechanical simulations. While emerging artificial intelligence (AI) generative
models have shown great promise in generating realistic crystal structures more
rapidly, most existing models fail to account for the unique symmetries and
periodicity of crystalline materials, and they are limited to handling
structures with only a few tens of atoms per unit cell. Here, we present a
symmetry-informed AI generative approach called Local Environment
Geometry-Oriented Crystal Generator (LEGO-xtal) that overcomes these
limitations. Our method generates initial structures using AI models trained on
an augmented small dataset, and then optimizes them using machine learning
structure descriptors rather than traditional energy-based optimization. We
demonstrate the effectiveness of LEGO-xtal by expanding from 25 known
low-energy sp2 carbon allotropes to over 1,700, all within 0.5 eV/atom of the
ground-state energy of graphite. This framework offers a generalizable strategy
for the targeted design of materials with modular building blocks, such as
metal-organic frameworks and next-generation battery materials....

---

### 21. Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists

**Authors:** Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, Shuiwang Ji

**Published:** 2025-06-05

**Category:** cs.AI

**ID:** 2506.05616v2

**Link:** [http://arxiv.org/abs/2506.05616v2](http://arxiv.org/abs/2506.05616v2)

**Summary:** We aim at designing language agents with greater autonomy for crystal
materials discovery. While most of existing studies restrict the agents to
perform specific tasks within predefined workflows, we aim to automate workflow
planning given high-level goals and scientist intuition. To this end, we
propose Materials Agent unifying Planning, Physics, and Scientists, known as
MAPPS. MAPPS consists of a Workflow Planner, a Tool Code Generator, and a
Scientific Mediator. The Workflow Planner uses large language models (LLMs) to
generate structured and multi-step workflows. The Tool Code Generator
synthesizes executable Python code for various tasks, including invoking a
force field foundation model that encodes physics. The Scientific Mediator
coordinates communications, facilitates scientist feedback, and ensures
robustness through error reflection and recovery. By unifying planning,
physics, and scientists, MAPPS enables flexible and reliable materials
discovery with greater autonomy, achieving a five-fold improvement in
stability, uniqueness, and novelty rates compared with prior generative models
when evaluated on the MP-20 data. We provide extensive experiments across
diverse tasks to show that MAPPS is a promising framework for autonomous
materials discovery....

---

### 22. Neural networks for the prediction of peel force for skin adhesive interface using FEM simulation

**Authors:** Ashish Masarkar, Rakesh Gupta, Naga Neehar Dingari, Beena Rai

**Published:** 2025-06-09

**Category:** physics.med-ph

**ID:** 2506.19855v1

**Link:** [http://arxiv.org/abs/2506.19855v1](http://arxiv.org/abs/2506.19855v1)

**Summary:** Studying the peeling behaviour of adhesives on skin is vital for advancing
biomedical applications such as medical adhesives and transdermal patches.
Traditional methods like experimental testing and finite element method (FEM),
though considered gold standards, are resource-intensive, computationally
expensive and time-consuming, particularly when analysing a wide material
parameter space. In this study, we present a neural network-based approach to
predict the minimum peel force (F_min) required for adhesive detachment from
skin tissue, limiting the need for repeated FEM simulations and significantly
reducing the computational cost. Leveraging a dataset generated from FEM
simulations of 90 degree peel test with varying adhesive and fracture mechanics
parameters, our neural network model achieved high accuracy, validated through
rigorous 5-fold cross-validation. The final architecture was able to predict a
wide variety of skin-adhesive peeling behaviour, exhibiting a mean squared
error (MSE) of 3.66*10^-7 and a R^2 score of 0.94 on test set, demonstrating
robust performance. This work introduces a reliable, computationally efficient
method for predicting adhesive behaviour, significantly reducing simulation
time while maintaining accuracy. This integration of machine learning with
high-fidelity biomechanical simulations enables efficient design and
optimization of skin-adhesive systems, providing a scalable framework for
future research in computational dermato-mechanics and bio-adhesive material
design....

---

### 23. Training-Free Constrained Generation With Stable Diffusion Models

**Authors:** Stefano Zampini, Jacob K. Christopher, Luca Oneto, Davide Anguita, Ferdinando Fioretto

**Published:** 2025-02-08

**Category:** cs.LG

**ID:** 2502.05625v3

**Link:** [http://arxiv.org/abs/2502.05625v3](http://arxiv.org/abs/2502.05625v3)

**Summary:** Stable diffusion models represent the state-of-the-art in data synthesis
across diverse domains and hold transformative potential for applications in
science and engineering, e.g., by facilitating the discovery of novel solutions
and simulating systems that are computationally intractable to model
explicitly. While there is increasing effort to incorporate physics-based
constraints into generative models, existing techniques are either limited in
their applicability to latent diffusion frameworks or lack the capability to
strictly enforce domain-specific constraints. To address this limitation this
paper proposes a novel integration of stable diffusion models with constrained
optimization frameworks, enabling the generation of outputs satisfying
stringent physical and functional requirements. The effectiveness of this
approach is demonstrated through material design experiments requiring
adherence to precise morphometric properties, challenging inverse design tasks
involving the generation of materials inducing specific stress-strain
responses, and copyright-constrained content generation tasks....

---

### 24. Learning Design-Score Manifold to Guide Diffusion Models for Offline Optimization

**Authors:** Tailin Zhou, Zhilin Chen, Wenlong Lyu, Zhitang Chen, Danny H. K. Tsang, Jun Zhang

**Published:** 2025-06-06

**Category:** cs.LG

**ID:** 2506.05680v1

**Link:** [http://arxiv.org/abs/2506.05680v1](http://arxiv.org/abs/2506.05680v1)

**Summary:** Optimizing complex systems, from discovering therapeutic drugs to designing
high-performance materials, remains a fundamental challenge across science and
engineering, as the underlying rules are often unknown and costly to evaluate.
Offline optimization aims to optimize designs for target scores using
pre-collected datasets without system interaction. However, conventional
approaches may fail beyond training data, predicting inaccurate scores and
generating inferior designs. This paper introduces ManGO, a diffusion-based
framework that learns the design-score manifold, capturing the design-score
interdependencies holistically. Unlike existing methods that treat design and
score spaces in isolation, ManGO unifies forward prediction and backward
generation, attaining generalization beyond training data. Key to this is its
derivative-free guidance for conditional generation, coupled with adaptive
inference-time scaling that dynamically optimizes denoising paths. Extensive
evaluations demonstrate that ManGO outperforms 24 single- and 10
multi-objective optimization methods across diverse domains, including
synthetic tasks, robot control, material design, DNA sequence, and real-world
engineering optimization....

---

### 25. eGAD! double descent is explained by Generalized Aliasing Decomposition

**Authors:** Mark K. Transtrum, Gus L. W. Hart, Tyler J. Jarvis, Jared P. Whitehead

**Published:** 2024-08-15

**Category:** math.ST

**ID:** 2408.08294v4

**Link:** [http://arxiv.org/abs/2408.08294v4](http://arxiv.org/abs/2408.08294v4)

**Summary:** A central problem in data science is to use potentially noisy samples of an
unknown function to predict values for unseen inputs. In classical statistics,
predictive error is understood as a trade-off between the bias and the variance
that balances model simplicity with its ability to fit complex functions.
However, over-parameterized models exhibit counterintuitive behaviors, such as
"double descent" in which models of increasing complexity exhibit decreasing
generalization error. Others may exhibit more complicated patterns of
predictive error with multiple peaks and valleys. Neither double descent nor
multiple descent phenomena are well explained by the bias-variance
decomposition.
  We introduce a novel decomposition that we call the generalized aliasing
decomposition (GAD) to explain the relationship between predictive performance
and model complexity. The GAD decomposes the predictive error into three parts:
1) model insufficiency, which dominates when the number of parameters is much
smaller than the number of data points, 2) data insufficiency, which dominates
when the number of parameters is much greater than the number of data points,
and 3) generalized aliasing, which dominates between these two extremes.
  We demonstrate the applicability of the GAD to diverse applications,
including random feature models from machine learning, Fourier transforms from
signal processing, solution methods for differential equations, and predictive
formation enthalpy in materials discovery. Because key components of the GAD
can be explicitly calculated from the relationship between model class and
samples without seeing any data labels, it can answer questions related to
experimental design and model selection before collecting data or performing
experiments. We further demonstrate this approach on several examples and
discuss implications for predictive modeling and data science....

---

### 26. Probing the Limit of Heat Transfer in Inorganic Crystals with Deep Learning

**Authors:** Jielan Li, Zekun Chen, Qian Wang, Han Yang, Ziheng Lu, Guanzhi Li, Shuizhou Chen, Yu Zhu, Xixian Liu, Junfu Tan, Mingfa Tang, Yichi Zhou, Claudio Zeni, Andrew Fowler, Daniel Zügner, Robert Pinsler, Matthew Horton, Tian Xie, Tie-Yan Liu, Haiguang Liu, Tao Qin, Bing Lv, Davide Donadio, Hongxia Hao

**Published:** 2025-03-14

**Category:** cond-mat.mtrl-sci

**ID:** 2503.11568v2

**Link:** [http://arxiv.org/abs/2503.11568v2](http://arxiv.org/abs/2503.11568v2)

**Summary:** Heat transfer is a fundamental property of matter. Research spanning decades
has attempted to discover materials with exceptional thermal conductivity, yet
the upper limit remains unknown. Using deep learning accelerated crystal
structure prediction and first-principles calculation, we systematically
explore the thermal conductivity landscape of inorganic crystals. We
brute-force over half a million ordered crystalline structures, encompassing an
extensive coverage of local energy minima in binary compounds with up to four
atoms per primitive cell. We confirm diamond sets the upper bound of thermal
conductivity within our search space, very likely also among all stable
crystalline solids at ambient conditions. We also identify over 20 novel
crystals surpassing silicon in thermal conductivity, validated by density
functional theory. These include a semiconductor TaN with ultrahigh thermal
conductivity (~900 $\mathrm{W\cdot m^{-1}\cdot K^{-1}}$), and metallic
compounds such as MnV that exhibit high lattice and electronic thermal
conductivity simultaneously, a distinctive feature not observed before. These
results as well as the deep learning-driven screening method, redefine the
landscape of thermal transport and establish a large open-access database for
future materials discovery....

---

### 27. MOFGPT: Generative Design of Metal-Organic Frameworks using Language Models

**Authors:** Srivathsan Badrinarayanan, Rishikesh Magar, Akshay Antony, Radheesh Sharma Meda, Amir Barati Farimani

**Published:** 2025-05-30

**Category:** cs.LG

**ID:** 2506.00198v1

**Link:** [http://arxiv.org/abs/2506.00198v1](http://arxiv.org/abs/2506.00198v1)

**Summary:** The discovery of Metal-Organic Frameworks (MOFs) with application-specific
properties remains a central challenge in materials chemistry, owing to the
immense size and complexity of their structural design space. Conventional
computational screening techniques such as molecular simulations and density
functional theory (DFT), while accurate, are computationally prohibitive at
scale. Machine learning offers an exciting alternative by leveraging
data-driven approaches to accelerate materials discovery. The complexity of
MOFs, with their extended periodic structures and diverse topologies, creates
both opportunities and challenges for generative modeling approaches. To
address these challenges, we present a reinforcement learning-enhanced,
transformer-based framework for the de novo design of MOFs. Central to our
approach is MOFid, a chemically-informed string representation encoding both
connectivity and topology, enabling scalable generative modeling. Our pipeline
comprises three components: (1) a generative GPT model trained on MOFid
sequences, (2) MOFormer, a transformer-based property predictor, and (3) a
reinforcement learning (RL) module that optimizes generated candidates via
property-guided reward functions. By integrating property feedback into
sequence generation, our method drives the model toward synthesizable,
topologically valid MOFs with desired functional attributes. This work
demonstrates the potential of large language models, when coupled with
reinforcement learning, to accelerate inverse design in reticular chemistry and
unlock new frontiers in computational MOF discovery....

---

### 28. A Straightforward Gradient-Based Approach for High-Tc Superconductor Design: Leveraging Domain Knowledge via Adaptive Constraints

**Authors:** Akihiro Fujii, Anh Khoa Augustin Lu, Koji Shimizu, Satoshi Watanabe

**Published:** 2024-03-20

**Category:** cond-mat.supr-con

**ID:** 2403.13627v2

**Link:** [http://arxiv.org/abs/2403.13627v2](http://arxiv.org/abs/2403.13627v2)

**Summary:** Materials design aims to discover novel compounds with desired properties.
However, prevailing strategies face critical trade-offs. Conventional
element-substitution approaches readily and adaptively incorporate various
domain knowledge but remain confined to a narrow search space. In contrast,
deep generative models efficiently explore vast compositional landscapes, yet
they struggle to flexibly integrate domain knowledge. To address these
trade-offs, we propose a gradient-based material design framework that combines
these strengths, offering both efficiency and adaptability. In our method,
chemical compositions are optimised to achieve target properties by using
property prediction models and their gradients. In order to seamlessly enforce
diverse constraints, including those reflecting domain insights such as
oxidation states, discretised compositional ratios, types of elements, and
their abundance, we apply masks and employ a special loss function, namely the
integer loss. Furthermore, we initialise the optimisation using promising
candidates from existing dataset, effectively guiding the search away from
unfavourable regions and thus helping to avoid poor solutions. Our approach
demonstrates a more efficient exploration of superconductor candidates,
uncovering candidate materials with higher critical temperature than
conventional element-substitution and generative models. Importantly, it could
propose new compositions beyond those found in existing databases, including
new hydride superconductors absent from the training dataset but which share
compositional similarities with materials found in literature. This synergy of
domain knowledge and machine-learning-based scalability provides a robust
foundation for rapid, adaptive, and comprehensive materials design for
superconductors and beyond....

---

### 29. Rethinking Gradient-Based Methods: Multi-Property Materials Design Beyond Differentiable Targets

**Authors:** Akihiro Fujii, Yoshitaka Ushiku, Koji Shimizu, Anh Khoa Augustin Lu, Satoshi Watanabe

**Published:** 2024-10-11

**Category:** cond-mat.mtrl-sci

**ID:** 2410.08562v4

**Link:** [http://arxiv.org/abs/2410.08562v4](http://arxiv.org/abs/2410.08562v4)

**Summary:** Gradient-based methods offer a simple, efficient strategy for materials
design by directly optimizing candidates using gradients from pretrained
property predictors. However, their use in crystal structure optimization is
hindered by two key challenges: handling non-differentiable constraints, such
as charge neutrality and structural fidelity, and susceptibility to poor local
minima. We revisit and extend the gradient-based methods to address these
issues. We propose Simultaneous Multi-property Optimization using Adaptive
Crystal Synthesizer (SMOACS), which integrates oxidation-number masks and
template-based initialization to enforce non-differentiable constraints, avoid
poor local minima, and flexibly incorporate additional constraints without
retraining. SMOACS enables multi-property optimization. including exceptional
targets such as high-temperature superconductivity, and scales to large crystal
systems, both persistent challenges for generative models, even those enhanced
with gradient-based guidance from property predictors. In experiments on five
target properties and three datasets, SMOACS outperforms generative models and
Bayesian optimization methods, successfully designing 135-atom perovskite
structures that satisfy multiple property targets and constraints, a task at
which the other methods fail entirely....

---

### 30. Machine Learning - Driven Materials Discovery: Unlocking Next-Generation Functional Materials -- A minireview

**Authors:** Dilshod Nematov, Mirabbos Hojamberdiev

**Published:** 2025-03-22

**Category:** cond-mat.mtrl-sci

**ID:** 2503.18975v2

**Link:** [http://arxiv.org/abs/2503.18975v2](http://arxiv.org/abs/2503.18975v2)

**Summary:** The rapid advancement of machine learning and artificial intelligence
(AI)-driven techniques is revolutionizing materials discovery, property
prediction, and material design by minimizing human intervention and
accelerating scientific progress. This review provides a comprehensive overview
of smart, machine learning (ML)-driven approaches, emphasizing their role in
predicting material properties, discovering novel compounds, and optimizing
material structures. Key methodologies ranging from deep learning, graph neural
networks, and Bayesian optimization to automated generative models, such as
generative adversarial networks (GANs) and variational autoencoders (VAEs)
enable the autonomous design of materials with tailored functionalities. By
leveraging AutoML frameworks (e.g., AutoGluon, TPOT, and H2O.ai), researchers
can automate the model selection, hyperparameter tuning, and feature
engineering, significantly improving the efficiency of materials informatics.
Furthermore, the integration of AI-driven robotic laboratories and
high-throughput computing has established a fully automated pipeline for rapid
synthesis and experimental validation, drastically reducing the time and cost
of material discovery. This review highlights real-world applications of
automated ML-driven approaches in predicting mechanical, thermal, electrical,
and optical properties of materials, demonstrating successful cases in
superconductors, catalysts, photovoltaics, and energy storage systems. We also
address key challenges, such as data quality, interpretability, and the
integration of AutoML with quantum computing, which are essential for future
advancements. Ultimately, the synergy between AI, automated experimentation,
and computational modeling transforms the way the materials are discovered,
optimized, and designed, paving the way for next-generation innovations in
energy, electronics, and nanotechnology....

---

### 31. A Generation Framework with Strict Constraints for Crystal Materials Design

**Authors:** Chao Huang, Jiahui Chen, Chen Chen, Chunyan Chen, Renjie Su, Shiyu Du, ChenChen, Hongrui Liang, Daojing Lin

**Published:** 2024-11-13

**Category:** cs.AI

**ID:** 2411.08464v2

**Link:** [http://arxiv.org/abs/2411.08464v2](http://arxiv.org/abs/2411.08464v2)

**Summary:** The design of crystal materials plays a critical role in areas such as new
energy development, biomedical engineering, and semiconductors. Recent advances
in data-driven methods have enabled the generation of diverse crystal
structures. However, most existing approaches still rely on random sampling
without strict constraints, requiring multiple post-processing steps to
identify stable candidates with the desired physical and chemical properties.
In this work, we present a new constrained generation framework that takes
multiple constraints as input and enables the generation of crystal structures
with specific chemical and properties. In this framework, intermediate
constraints, such as symmetry information and composition ratio, are generated
by a constraint generator based on large language models (LLMs), which
considers the target properties. These constraints are then used by a
subsequent crystal structure generator to ensure that the structure generation
process is under control. Our method generates crystal structures with a
probability of meeting the target properties that is more than twice that of
existing approaches. Furthermore, nearly 100% of the generated crystals
strictly adhere to predefined chemical composition, eliminating the risks of
supply chain during production....

---

### 32. teMatDb: A High-Quality Thermoelectric Material Database with Self-Consistent ZT Filtering

**Authors:** Byungki Ryu, Ji Hui Son, Sungjin Park, Jaywan Chung, Hye-Jin Lim, SuJi Park, Yujeong Do, SuDong Park

**Published:** 2025-05-25

**Category:** cond-mat.mtrl-sci

**ID:** 2505.19150v2

**Link:** [http://arxiv.org/abs/2505.19150v2](http://arxiv.org/abs/2505.19150v2)

**Summary:** This study presents a curated thermoelectric material database, teMatDb,
constructed by digitizing literature-reported data. It includes
temperature-dependent thermoelectric properties (TEPs), Seebeck coefficient,
electrical resistivity, thermal conductivity, and figure of merit (ZT), along
with metadata on materials and their corresponding publications. A
self-consistent ZT (Sc-ZT) filter set was developed to measure ZT errors by
comparing reported ZT's from figures with ZT's recalculated from digitized
TEPs. Using this Sc-ZT protocol, we generated tMatDb272, comprising 14,717
temperature-property pairs from 272 high-quality TEP sets across 262
publications. The method identifies various types of ZT errors, such as
resolution error, publication bias, ZT overestimation, interpolation and
extrapolation error, and digitization noise, and excludes inconsistent samples
from the dataset. teMatDb272 and the Sc-ZT filtering framework offer a robust
dataset for data-driven and machine-learning-based materials design, device
modeling, and future thermoelectric research....

---

### 33. Materials Generation in the Era of Artificial Intelligence: A Comprehensive Survey

**Authors:** Zhixun Li, Bin Cao, Rui Jiao, Liang Wang, Ding Wang, Yang Liu, Dingshuo Chen, Jia Li, Qiang Liu, Yu Rong, Liang Wang, Tong-yi Zhang, Jeffrey Xu Yu

**Published:** 2025-05-22

**Category:** cond-mat.mtrl-sci

**ID:** 2505.16379v1

**Link:** [http://arxiv.org/abs/2505.16379v1](http://arxiv.org/abs/2505.16379v1)

**Summary:** Materials are the foundation of modern society, underpinning advancements in
energy, electronics, healthcare, transportation, and infrastructure. The
ability to discover and design new materials with tailored properties is
critical to solving some of the most pressing global challenges. In recent
years, the growing availability of high-quality materials data combined with
rapid advances in Artificial Intelligence (AI) has opened new opportunities for
accelerating materials discovery. Data-driven generative models provide a
powerful tool for materials design by directly create novel materials that
satisfy predefined property requirements. Despite the proliferation of related
work, there remains a notable lack of up-to-date and systematic surveys in this
area. To fill this gap, this paper provides a comprehensive overview of recent
progress in AI-driven materials generation. We first organize various types of
materials and illustrate multiple representations of crystalline materials. We
then provide a detailed summary and taxonomy of current AI-driven materials
generation approaches. Furthermore, we discuss the common evaluation metrics
and summarize open-source codes and benchmark datasets. Finally, we conclude
with potential future directions and challenges in this fast-growing field. The
related sources can be found at
https://github.com/ZhixunLEE/Awesome-AI-for-Materials-Generation....

---

### 34. Transforming the Hybrid Cloud for Emerging AI Workloads

**Authors:** Deming Chen, Alaa Youssef, Ruchi Pendse, André Schleife, Bryan K. Clark, Hendrik Hamann, Jingrui He, Teodoro Laino, Lav Varshney, Yuxiong Wang, Avirup Sil, Reyhaneh Jabbarvand, Tianyin Xu, Volodymyr Kindratenko, Carlos Costa, Sarita Adve, Charith Mendis, Minjia Zhang, Santiago Núñez-Corrales, Raghu Ganti, Mudhakar Srivatsa, Nam Sung Kim, Josep Torrellas, Jian Huang, Seetharami Seelam, Klara Nahrstedt, Tarek Abdelzaher, Tamar Eilam, Huimin Zhao, Matteo Manica, Ravishankar Iyer, Martin Hirzel, Vikram Adve, Darko Marinov, Hubertus Franke, Hanghang Tong, Elizabeth Ainsworth, Han Zhao, Deepak Vasisht, Minh Do, Sahil Suneja, Fabio Oliveira, Giovanni Pacifici, Ruchir Puri, Priya Nagpurkar

**Published:** 2024-11-20

**Category:** cs.DC

**ID:** 2411.13239v2

**Link:** [http://arxiv.org/abs/2411.13239v2](http://arxiv.org/abs/2411.13239v2)

**Summary:** This white paper, developed through close collaboration between IBM Research
and UIUC researchers within the IIDAI Institute, envisions transforming hybrid
cloud systems to meet the growing complexity of AI workloads through
innovative, full-stack co-design approaches, emphasizing usability,
manageability, affordability, adaptability, efficiency, and scalability. By
integrating cutting-edge technologies such as generative and agentic AI,
cross-layer automation and optimization, unified control plane, and composable
and adaptive system architecture, the proposed framework addresses critical
challenges in energy efficiency, performance, and cost-effectiveness.
Incorporating quantum computing as it matures will enable quantum-accelerated
simulations for materials science, climate modeling, and other high-impact
domains. Collaborative efforts between academia and industry are central to
this vision, driving advancements in foundation models for material design and
climate solutions, scalable multimodal data processing, and enhanced
physics-based AI emulators for applications like weather forecasting and carbon
sequestration. Research priorities include advancing AI agentic systems, LLM as
an Abstraction (LLMaaA), AI model optimization and unified abstractions across
heterogeneous infrastructure, end-to-end edge-cloud transformation, efficient
programming model, middleware and platform, secure infrastructure,
application-adaptive cloud systems, and new quantum-classical collaborative
workflows. These ideas and solutions encompass both theoretical and practical
research questions, requiring coordinated input and support from the research
community. This joint initiative aims to establish hybrid clouds as secure,
efficient, and sustainable platforms, fostering breakthroughs in AI-driven
applications and scientific discovery across academia, industry, and society....

---

### 35. Inverse Design of Metal-Organic Frameworks Using Quantum Natural Language Processing

**Authors:** Shinyoung Kang, Jihan Kim

**Published:** 2024-05-20

**Category:** cs.LG

**ID:** 2405.11783v2

**Link:** [http://arxiv.org/abs/2405.11783v2](http://arxiv.org/abs/2405.11783v2)

**Summary:** In this study, we explore the potential of using quantum natural language
processing (QNLP) to inverse design metal-organic frameworks (MOFs) with
targeted properties. Specifically, by analyzing 450 hypothetical MOF structures
consisting of 3 topologies, 10 metal nodes and 15 organic ligands, we
categorize these structures into four distinct classes for pore volume and
$CO_{2}$ Henry's constant values. We then compare various QNLP models (i.e. the
bag-of-words, DisCoCat (Distributional Compositional Categorical), and
sequence-based models) to identify the most effective approach to process the
MOF dataset. Using a classical simulator provided by the IBM Qiskit, the
bag-of-words model is identified to be the optimum model, achieving validation
accuracies of 88.6% and 78.0% for binary classification tasks on pore volume
and $CO_{2}$ Henry's constant, respectively. Further, we developed multi-class
classification models tailored to the probabilistic nature of quantum circuits,
with average test accuracies of 92% and 80% across different classes for pore
volume and $CO_{2}$ Henry's constant datasets. Finally, the performance of
generating MOF with target properties showed accuracies of 93.5% for pore
volume and 87% for $CO_{2}$ Henry's constant, respectively. Although our
investigation covers only a fraction of the vast MOF search space, it marks a
promising first step towards using quantum computing for materials design,
offering a new perspective through which to explore the complex landscape of
MOFs....

---

### 36. Re-experiment Smart: a Novel Method to Enhance Data-driven Prediction of Mechanical Properties of Epoxy Polymers

**Authors:** Wanshan Cui, Yejin Jeong, Inwook Song, Gyuri Kim, Minsang Kwon, Donghun Lee

**Published:** 2025-05-19

**Category:** cond-mat.soft

**ID:** 2506.01994v1

**Link:** [http://arxiv.org/abs/2506.01994v1](http://arxiv.org/abs/2506.01994v1)

**Summary:** Accurate prediction of polymer material properties through data-driven
approaches greatly accelerates novel material development by reducing redundant
experiments and trial-and-error processes. However, inevitable outliers in
empirical measurements can severely skew machine learning results, leading to
erroneous prediction models and suboptimal material designs. To address this
limitation, we propose a novel approach to enhance dataset quality efficiently
by integrating multi-algorithm outlier detection with selective
re-experimentation of unreliable outlier cases. To validate the empirical
effectiveness of the approach, we systematically construct a new dataset
containing 701 measurements of three key mechanical properties: glass
transition temperature ($T_g$), tan $\delta$ peak, and crosslinking density
($v_{c}$). To demonstrate its general applicability, we report the performance
improvements across multiple machine learning models, including Elastic Net,
SVR, Random Forest, and TPOT, to predict the three key properties. Our method
reliably reduces prediction error (RMSE) and significantly improves accuracy
with minimal additional experimental work, requiring only about 5% of the
dataset to be re-measured. These findings highlight the importance of data
quality enhancement in achieving reliable machine learning applications in
polymer science and present a scalable strategy for improving predictive
reliability in materials science....

---

### 37. Texture- and Stress-Dependent Electromechanical Response in Ferroelectric PZT: Insights from a Micromechanical Model

**Authors:** Saujatya Mandal, Debashish Das

**Published:** 2025-03-15

**Category:** cond-mat.mtrl-sci

**ID:** 2503.12057v2

**Link:** [http://arxiv.org/abs/2503.12057v2](http://arxiv.org/abs/2503.12057v2)

**Summary:** The electromechanical response of PbZr0.52Ti0.48O3 (PZT) near the
morphotropic phase boundary (MPB) is strongly influenced by crystallographic
texture and residual stress, both of which affect domain switching behavior.
While these effects are critical for optimizing sensors, actuators, and MEMS
devices, their combined influence remains poorly understood. We present a
computational micromechanical model that captures texture- and stress-dependent
polarization switching in MPB PZT. The framework incorporates both tetragonal
and rhombohedral domain switching, along with interphase transformations,
enabling accurate simulation of nonlinear electromechanical behavior. The model
reproduces key experimental trends, including enhanced piezoelectric response
in (001)-textured ceramics, and degradation under high in-plane stress. The
implementation, provided as open-source MATLAB code, offers an accessible
platform for experimentalists and materials designers to explore and interpret
electromechanical behavior. By linking microstructural orientation and stress
state to macroscopic response, this work provides a practical tool for
understanding and designing next-generation piezoelectric materials....

---

### 38. MatTools: Benchmarking Large Language Models for Materials Science Tools

**Authors:** Siyu Liu, Jiamin Xu, Beilin Ye, Bo Hu, David J. Srolovitz, Tongqi Wen

**Published:** 2025-05-16

**Category:** cond-mat.mtrl-sci

**ID:** 2505.10852v1

**Link:** [http://arxiv.org/abs/2505.10852v1](http://arxiv.org/abs/2505.10852v1)

**Summary:** Large language models (LLMs) are increasingly applied to materials science
questions, including literature comprehension, property prediction, materials
discovery and alloy design. At the same time, a wide range of physics-based
computational approaches have been developed in which materials properties can
be calculated. Here, we propose a benchmark application to evaluate the
proficiency of LLMs to answer materials science questions through the
generation and safe execution of codes based on such physics-based
computational materials science packages. MatTools is built on two
complementary components: a materials simulation tool question-answer (QA)
benchmark and a real-world tool-usage benchmark. We designed an automated
methodology to efficiently collect real-world materials science tool-use
examples. The QA benchmark, derived from the pymatgen (Python Materials
Genomics) codebase and documentation, comprises 69,225 QA pairs that assess the
ability of an LLM to understand materials science tools. The real-world
benchmark contains 49 tasks (138 subtasks) requiring the generation of
functional Python code for materials property calculations. Our evaluation of
diverse LLMs yields three key insights: (1)Generalists outshine
specialists;(2)AI knows AI; and (3)Simpler is better. MatTools provides a
standardized framework for assessing and improving LLM capabilities for
materials science tool applications, facilitating the development of more
effective AI systems for materials science and general scientific research....

---

### 39. 34 Examples of LLM Applications in Materials Science and Chemistry: Towards Automation, Assistants, Agents, and Accelerated Scientific Discovery

**Authors:** Yoel Zimmermann, Adib Bazgir, Alexander Al-Feghali, Mehrad Ansari, Joshua Bocarsly, L. Catherine Brinson, Yuan Chiang, Defne Circi, Min-Hsueh Chiu, Nathan Daelman, Matthew L. Evans, Abhijeet S. Gangan, Janine George, Hassan Harb, Ghazal Khalighinejad, Sartaaj Takrim Khan, Sascha Klawohn, Magdalena Lederbauer, Soroush Mahjoubi, Bernadette Mohr, Seyed Mohamad Moosavi, Aakash Naik, Aleyna Beste Ozhan, Dieter Plessers, Aritra Roy, Fabian Schöppach, Philippe Schwaller, Carla Terboven, Katharina Ueltzen, Yue Wu, Shang Zhu, Jan Janssen, Calvin Li, Ian Foster, Ben Blaiszik

**Published:** 2025-05-05

**Category:** cs.LG

**ID:** 2505.03049v2

**Link:** [http://arxiv.org/abs/2505.03049v2](http://arxiv.org/abs/2505.03049v2)

**Summary:** Large Language Models (LLMs) are reshaping many aspects of materials science
and chemistry research, enabling advances in molecular property prediction,
materials design, scientific automation, knowledge extraction, and more. Recent
developments demonstrate that the latest class of models are able to integrate
structured and unstructured data, assist in hypothesis generation, and
streamline research workflows. To explore the frontier of LLM capabilities
across the research lifecycle, we review applications of LLMs through 34 total
projects developed during the second annual Large Language Model Hackathon for
Applications in Materials Science and Chemistry, a global hybrid event. These
projects spanned seven key research areas: (1) molecular and material property
prediction, (2) molecular and material design, (3) automation and novel
interfaces, (4) scientific communication and education, (5) research data
management and automation, (6) hypothesis generation and evaluation, and (7)
knowledge extraction and reasoning from the scientific literature.
Collectively, these applications illustrate how LLMs serve as versatile
predictive models, platforms for rapid prototyping of domain-specific tools,
and much more. In particular, improvements in both open source and proprietary
LLM performance through the addition of reasoning, additional training data,
and new techniques have expanded effectiveness, particularly in low-data
environments and interdisciplinary research. As LLMs continue to improve, their
integration into scientific workflows presents both new opportunities and new
challenges, requiring ongoing exploration, continued refinement, and further
research to address reliability, interpretability, and reproducibility....

---

### 40. InvDesFlow-AL: Active Learning-based Workflow for Inverse Design of Functional Materials

**Authors:** Xiao-Qi Han, Peng-Jie Guo, Ze-Feng Gao, Hao Sun, Zhong-Yi Lu

**Published:** 2025-05-14

**Category:** cond-mat.mtrl-sci

**ID:** 2505.09203v1

**Link:** [http://arxiv.org/abs/2505.09203v1](http://arxiv.org/abs/2505.09203v1)

**Summary:** Developing inverse design methods for functional materials with specific
properties is critical to advancing fields like renewable energy, catalysis,
energy storage, and carbon capture. Generative models based on diffusion
principles can directly produce new materials that meet performance
constraints, thereby significantly accelerating the material design process.
However, existing methods for generating and predicting crystal structures
often remain limited by low success rates. In this work, we propose a novel
inverse material design generative framework called InvDesFlow-AL, which is
based on active learning strategies. This framework can iteratively optimize
the material generation process to gradually guide it towards desired
performance characteristics. In terms of crystal structure prediction, the
InvDesFlow-AL model achieves an RMSE of 0.0423 {\AA}, representing an 32.96%
improvement in performance compared to exsisting generative models.
Additionally, InvDesFlow-AL has been successfully validated in the design of
low-formation-energy and low-Ehull materials. It can systematically generate
materials with progressively lower formation energies while continuously
expanding the exploration across diverse chemical spaces. These results fully
demonstrate the effectiveness of the proposed active learning-driven generative
model in accelerating material discovery and inverse design. To further prove
the effectiveness of this method, we took the search for BCS superconductors
under ambient pressure as an example explored by InvDesFlow-AL. As a result, we
successfully identified Li\(_2\)AuH\(_6\) as a conventional BCS superconductor
with an ultra-high transition temperature of 140 K. This discovery provides
strong empirical support for the application of inverse design in materials
science....

---

### 41. Quotient Complex Transformer (QCformer) for Perovskite Data Analysis

**Authors:** Xinyu You, Xiang Liu, Chuan-Shen Hu, Kelin Xia, Tze Chien Sum

**Published:** 2025-05-14

**Category:** cs.LG

**ID:** 2505.09174v1

**Link:** [http://arxiv.org/abs/2505.09174v1](http://arxiv.org/abs/2505.09174v1)

**Summary:** The discovery of novel functional materials is crucial in addressing the
challenges of sustainable energy generation and climate change. Hybrid
organic-inorganic perovskites (HOIPs) have gained attention for their
exceptional optoelectronic properties in photovoltaics. Recently, geometric
deep learning, particularly graph neural networks (GNNs), has shown strong
potential in predicting material properties and guiding material design.
However, traditional GNNs often struggle to capture the periodic structures and
higher-order interactions prevalent in such systems. To address these
limitations, we propose a novel representation based on quotient complexes
(QCs) and introduce the Quotient Complex Transformer (QCformer) for material
property prediction. A material structure is modeled as a quotient complex,
which encodes both pairwise and many-body interactions via simplices of varying
dimensions and captures material periodicity through a quotient operation. Our
model leverages higher-order features defined on simplices and processes them
using a simplex-based Transformer module. We pretrain QCformer on benchmark
datasets such as the Materials Project and JARVIS, and fine-tune it on HOIP
datasets. The results show that QCformer outperforms state-of-the-art models in
HOIP property prediction, demonstrating its effectiveness. The quotient complex
representation and QCformer model together contribute a powerful new tool for
predictive modeling of perovskite materials....

---

### 42. Bridging Theory and Experiment in Materials Discovery: Machine-Learning-Assisted Prediction of Synthesizable Structures

**Authors:** Yu Xin, Peng Liu, Zhuohang Xie, Wenhui Mi, Pengyue Gao, Hong Jian Zhao, Jian Lv, Yanchao Wang, Yanming Ma

**Published:** 2025-05-14

**Category:** cond-mat.mtrl-sci

**ID:** 2505.09161v1

**Link:** [http://arxiv.org/abs/2505.09161v1](http://arxiv.org/abs/2505.09161v1)

**Summary:** Even though thermodynamic energy-based crystal structure prediction (CSP) has
revolutionized materials discovery, the energy-driven CSP approaches often
struggle to identify experimentally realizable metastable materials synthesized
through kinetically controlled pathways, creating a critical gap between
theoretical predictions and experimental synthesis. Here, we propose a
synthesizability-driven CSP framework that integrates symmetry-guided structure
derivation with a Wyckoff encode-based machine-learning model, allowing for the
efficient localization of subspaces likely to yield highly synthesizable
structures. Within the identified promising subspaces, a structure-based
synthesizability evaluation model, fine-tuned using recently synthesized
structures to enhance predictive accuracy, is employed in conjunction with ab
initio calculations to systematically identify synthesizable candidates. The
framework successfully reproduces 13 experimentally known XSe (X = Sc, Ti, Mn,
Fe, Ni, Cu, Zn) structures, demonstrating its effectiveness in predicting
synthesizable structures. Notably, 92,310 structures are filtered from the
554,054 candidates predicted by GNoME, exhibiting great potential for promising
synthesizability. Additionally, eight thermodynamically favorable Hf-X-O (X =
Ti, V, and Mn) structures have been identified, among which three HfV$_2$O$_7$
candidates exhibit high synthesizability, presenting viable candidates for
experimental realization and potentially associated with experimentally
observed temperature-induced phase transitions. This work establishes a
data-driven paradigm for machine-learning-assisted inorganic materials
synthesis, highlighting its potential to bridge the gap between computational
predictions and experimental realization while unlocking new opportunities for
the targeted discovery of novel functional materials....

---

### 43. Image-Guided Microstructure Optimization using Diffusion Models: Validated with Li-Mn-rich Cathode Precursors

**Authors:** Geunho Choi, Changhwan Lee, Jieun Kim, Insoo Ye, Keeyoung Jung, Inchul Park

**Published:** 2025-05-12

**Category:** cond-mat.mtrl-sci

**ID:** 2505.07906v1

**Link:** [http://arxiv.org/abs/2505.07906v1](http://arxiv.org/abs/2505.07906v1)

**Summary:** Microstructure often dictates materials performance, yet it is rarely treated
as an explicit design variable because microstructure is hard to quantify,
predict, and optimize. Here, we introduce an image centric, closed-loop
framework that makes microstructural morphology into a controllable objective
and demonstrate its use case with Li- and Mn-rich layered oxide cathode
precursors. This work presents an integrated, AI driven framework for the
predictive design and optimization of lithium-ion battery cathode precursor
synthesis. This framework integrates a diffusion-based image generation model,
a quantitative image analysis pipeline, and a particle swarm optimization (PSO)
algorithm. By extracting key morphological descriptors such as texture,
sphericity, and median particle size (D50) from SEM images, the platform
accurately predicts SEM like morphologies resulting from specific
coprecipitation conditions, including reaction time-, solution concentration-,
and pH-dependent structural changes. Optimization then pinpoints synthesis
parameters that yield user defined target morphologies, as experimentally
validated by the close agreement between predicted and synthesized structures.
This framework offers a practical strategy for data driven materials design,
enabling both forward prediction and inverse design of synthesis conditions and
paving the way toward autonomous, image guided microstructure engineering....

---

### 44. DiffCrysGen: A Score-Based Diffusion Model for Design of Diverse Inorganic Crystalline Materials

**Authors:** Sourav Mal, Subhankar Mishra, Prasenjit Sen

**Published:** 2025-05-12

**Category:** cond-mat.mtrl-sci

**ID:** 2505.07442v1

**Link:** [http://arxiv.org/abs/2505.07442v1](http://arxiv.org/abs/2505.07442v1)

**Summary:** Crystal structure generation is a foundational challenge in materials
discovery, particularly in designing functional inorganic crystalline materials
with desired properties. Most existing diffusion-based generative models for
crystals rely on complex, hand-crafted priors and modular architectures to
separately model atom types, atomic positions, and lattice parameters. These
methods often require customized diffusion processes and conditional denoising,
which can introduce additional model complexities and inconsistencies. Here we
introduce DiffCrysGen, a fully data-driven, score-based diffusion model that
jointly learns the distribution of all structural components in crystalline
materials. With crystal structure representation as unified 2D matrices,
DiffCrysGen bypasses the need for task-specific priors or decoupled modules,
enabling end-to-end generation of atom types, fractional coordinates, and
lattice parameters within a single framework. Our model learns crystallographic
symmetry and chemical validity directly from large-scale datasets, allowing it
to scale to complex materials discovery tasks. As a demonstration, we applied
DiffCrysGen to the design of rare-earth-free magnetic materials with high
saturation magnetization, showing its effectiveness in generating stable,
diverse, and property-aligned candidates for sustainable magnet applications....

---

### 45. Genetic Algorithm-Accelerated Computational Discovery of Liquid Crystal Polymers with Enhanced Optical Properties

**Authors:** Jianing Zhou, Yuge Huang, Arman Boromand, Keian Noori, Lafe Purvis, Chulwoo Oh, Lu Lu, Zachary W. Ulissi, Vahe Gharakhanyan, Xinyue Zhang

**Published:** 2025-05-09

**Category:** cond-mat.soft

**ID:** 2505.13477v1

**Link:** [http://arxiv.org/abs/2505.13477v1](http://arxiv.org/abs/2505.13477v1)

**Summary:** Liquid crystal polymers with exceptional optical properties are highly
promising for next-generation virtual, augmented, and mixed reality (VR/AR/MR)
technologies, serving as high-performance, compact, lightweight, and
cost-effective optical components. However, the growing demands for optical
transparency and high refractive index in advanced optical devices present a
challenge for material discovery. In this study, we develop a novel approach
that integrates first-principles calculations with genetic algorithms to
accelerate the discovery of liquid crystal polymers with low visible absorption
and high refractive index. By iterating within a predefined space of molecular
building blocks, our approach rapidly identifies reactive mesogens that meet
target specifications. Additionally, it provides valuable insights into the
relationships between molecular structure and properties. This strategy not
only accelerates material screening but also uncovers key molecular design
principles, offering a systematic and scalable alternative to traditional
trial-and-error methods....

---

### 46. Magnetothermal Properties with Sampled Effective Local Field Estimation

**Authors:** Nicholas Brawand, Nima Leclerc, Emiko Zumbro

**Published:** 2025-05-09

**Category:** cond-mat.mtrl-sci

**ID:** 2505.06431v1

**Link:** [http://arxiv.org/abs/2505.06431v1](http://arxiv.org/abs/2505.06431v1)

**Summary:** We introduce a first-principles method for predicting the magnetothermal
properties of solid-state materials, which we call Sampled Effective Local
Field Estimation. This approach achieves over two orders of magnitude
improvement in sample efficiency compared to current state-of-the-art methods,
as demonstrated on representative material systems. We validate our predictions
against experimental data for well-characterized magnetic materials, showing
excellent agreement. The method is fully automated and requires minimal
computational resources, making it well suited for integration into
high-throughput materials discovery workflows. Our method offers a scalable and
accurate predictive framework that can accelerate the design of next-generation
materials for magnetic refrigeration, cryogenic cooling, and magnetic memory
technologies....

---

### 47. A Unified Predictive and Generative Solution for Liquid Electrolyte Formulation

**Authors:** Zhenze Yang, Yifan Wu, Xu Han, Ziqing Zhang, Haoen Lai, Zhenliang Mu, Tianze Zheng, Siyuan Liu, Zhichen Pu, Zhi Wang, Zhiao Yu, Sheng Gong, Wen Yan

**Published:** 2025-04-25

**Category:** cond-mat.mtrl-sci

**ID:** 2504.18728v2

**Link:** [http://arxiv.org/abs/2504.18728v2](http://arxiv.org/abs/2504.18728v2)

**Summary:** Liquid electrolytes are critical components of next-generation energy storage
systems, enabling fast ion transport, minimizing interfacial resistance, and
ensuring electrochemical stability for long-term battery performance. However,
measuring electrolyte properties and designing formulations remain
experimentally and computationally expensive. In this work, we present a
unified framework for designing liquid electrolyte formulation, integrating a
forward predictive model with an inverse generative approach. Leveraging both
computational and experimental data collected from literature and extensive
molecular simulations, we train a predictive model capable of accurately
estimating electrolyte properties from ionic conductivity to solvation
structure. Our physics-informed architecture preserves permutation invariance
and incorporates empirical dependencies on temperature and salt concentration,
making it broadly applicable to property prediction tasks across molecular
mixtures. Furthermore, we introduce -- to the best of our knowledge -- the
first generative machine learning framework for molecular mixture design,
demonstrated on electrolyte systems. This framework supports
multi-condition-constrained generation, addressing the inherently
multi-objective nature of materials design. This unified framework advances
data-driven electrolyte design and can be readily extended to other complex
chemical systems beyond electrolytes....

---

### 48. Materials discovery acceleration by using condition generative methodology

**Authors:** Caiyuan Ye, Yuzhi Wang, Xintian Xie, Tiannian Zhu, Jiaxuan Liu, Yuqing He, Lili Zhang, Junwei Zhang, Zhong Fang, Lei Wang, Zhipan Liu, Hongming Weng, Quansheng Wu

**Published:** 2025-04-30

**Category:** cond-mat.mtrl-sci

**ID:** 2505.00076v1

**Link:** [http://arxiv.org/abs/2505.00076v1](http://arxiv.org/abs/2505.00076v1)

**Summary:** With the rapid advancement of AI technologies, generative models have been
increasingly employed in the exploration of novel materials. By integrating
traditional computational approaches such as density functional theory (DFT)
and molecular dynamics (MD), existing generative models, including diffusion
models and autoregressive models, have demonstrated remarkable potential in the
discovery of novel materials. However, their efficiency in goal-directed
materials design remains suboptimal. In this work we developed a highly
transferable, efficient and robust conditional generation framework, PODGen, by
integrating a general generative model with multiple property prediction
models. Based on PODGen, we designed a workflow for the high-throughput
crystals conditional generation which is used to search new topological
insulators (TIs). Our results show that the success rate of generating TIs
using our framework is 5.3 times higher than that of the unconstrained
approach. More importantly, while general methods rarely produce gapped TIs,
our framework succeeds consistently, highlighting an effectively $\infty$
improvement. This demonstrates that conditional generation significantly
enhances the efficiency of targeted material discovery. Using this method, we
generated tens of thousands of new topological materials and conducted further
first-principles calculations on those with promising application potential.
Furthermore, we identified promising, synthesizable topological (crystalline)
insulators such as CsHgSb, NaLaB$_{12}$, Bi$_4$Sb$_2$Se$_3$, Be$_3$Ta$_2$Si and
Be$_2$W....

---

### 49. Tunable stacking-driven topological phase transitions in pnictide layers

**Authors:** Arjyama Bordoloi, Daniel Kaplan, Sobhit Singh

**Published:** 2025-04-29

**Category:** cond-mat.mes-hall

**ID:** 2504.21126v1

**Link:** [http://arxiv.org/abs/2504.21126v1](http://arxiv.org/abs/2504.21126v1)

**Summary:** Nonmagnetic topological insulators (TIs) are known for their robust metallic
surface/edge states that are protected by time-reversal symmetry, making them
promising candidates for next-generation spintronic and nanoelectronic devices.
Traditional approaches to realizing TIs have focused on inducing band inversion
via strong spin-orbit coupling (SOC), yet many materials with substantial SOC
often remain topologically trivial. In this work, we present a materials-design
strategy for engineering topologically non-trivial phases, e.g., quantum spin
Hall phases, by vertically stacking topologically trivial Rashba monolayers in
an inverted fashion. Using BiSb as a prototype system, we demonstrate that
while the BiSb monolayer is topologically trivial (despite having significant
SOC), an inverted BiSb-SbBi bilayer configuration realizes a non-trivial
topological phase with enhanced spin Hall conductivity. We further reveal a
delicate interplay between the SOC strength and the interlayer electron
tunneling that governs the emergence of a nontrivial topological phase in the
bilayer heterostructure. This phase can be systematically tuned using an
external electric field, providing an experimentally accessible means of
controlling the system's topology. Our magnetotransport studies further
validate this interplay, by revealing g-factor suppression and the emergence a
zeroth Landau level. Notably, the inverted bilayer heterostructure exhibits a
robust and tunable spin Hall effect, with performance comparable to that of
state-of-the-art materials. Thus, our findings unveil an alternative pathway
for designing and engineering functional properties in 2D topological systems
using topologically trivial constituent monolayers....

---

### 50. Graph Neural Network Prediction of Nonlinear Optical Properties

**Authors:** Yomn Alkabakibi, Congwei Xie, Artem R. Oganov

**Published:** 2025-04-28

**Category:** cond-mat.mtrl-sci

**ID:** 2504.19987v1

**Link:** [http://arxiv.org/abs/2504.19987v1](http://arxiv.org/abs/2504.19987v1)

**Summary:** Nonlinear optical (NLO) materials for generating lasers via second harmonic
generation (SHG) are highly sought in today's technology. However, discovering
novel materials with considerable SHG is challenging due to the time-consuming
and costly nature of both experimental methods and first-principles
calculations. In this study, we present a deep learning approach using the
Atomistic Line Graph Neural Network (ALIGNN) to predict NLO properties.
Sourcing data from the Novel Opto-Electronic Materials Discovery (NOEMD)
database and using the Kurtz-Perry (KP) coefficient as the key target, we
developed a robust model capable of accurately estimating nonlinear optical
responses. Our results demonstrate that the model achieves 82.5% accuracy at a
tolerated absolute error up to 1 pm/V and relative error not exceeding 0.5.
This work highlights the potential of deep learning in accelerating the
discovery and design of advanced optical materials with desired properties....

---

### 51. In Situ Nanometer-Resolution Strain and Orientation Mapping for Gas-Solid Reactions via Precession-Assisted Four-dimensional Scanning Transmission Electron Microscopy

**Authors:** Yongwen Sun, Ying Han, Dan Zhou, Athanassios S. Galanis, Alejandro Gomez-Perez, Ke Wang, Stavros Nicolopoulos, Hugo Perez Garza, Yang Yang

**Published:** 2025-04-26

**Category:** cond-mat.mtrl-sci

**ID:** 2504.18918v1

**Link:** [http://arxiv.org/abs/2504.18918v1](http://arxiv.org/abs/2504.18918v1)

**Summary:** Chemomechanical interactions in gas or liquid environments are crucial for
the functionality and longevity of various materials used in sustainable energy
technologies, such as rechargeable batteries, water-splitting catalysts, and
next-generation nuclear reactors. A comprehensive understanding of nanoscale
strain evolution involved in these processes can advance our knowledge of
underlying mechanisms and facilitate material design improvements. However,
traditional microscopy workflows face challenges due to trade-offs between
field of view (FOV), spatial resolution, temporal resolution, and electron beam
damage, particularly in gas or liquid environments. Here, we demonstrate in
situ nanometer-resolution strain and orientation mapping in a
temperature-controlled gas environment with a large FOV. This is achieved by
integrating a microelectromechanical system (MEMS)-based closed-cell TEM
holder, precession-assisted four-dimensional scanning transmission electron
microscopy (4D-STEM), and a direct electron detector (DED). Using the strain
evolution during zirconium initial oxidation as a case study, we first outline
critical strategies for focused ion beam gas-cell sample preparation and
gas-phase TEM workflows to enhance experimental success. We then show that
integrating DED with precession electron diffraction and optimizing gas
pressure substantially improve the quantity and quality of the detected Bragg
peaks in nano-beam electron diffraction patterns, enabling more precise strain
measurements. Furthermore, we introduce a practical protocol to pause the
reactions, allowing sufficient time for 4D-STEM data collection while ensuring
the temporal resolution needed to resolve material dynamics. Our methodology
and workflow provide a robust framework for quantitative analysis of
chemomechanical evolutions in materials exposed to gas or liquid environments....

---

### 52. Predicting Stress in Two-phase Random Materials and Super-Resolution Method for Stress Images by Embedding Physical Information

**Authors:** Tengfei Xing, Xiaodan Ren, Jie Li

**Published:** 2025-04-26

**Category:** cond-mat.mtrl-sci

**ID:** 2504.18854v1

**Link:** [http://arxiv.org/abs/2504.18854v1](http://arxiv.org/abs/2504.18854v1)

**Summary:** Stress analysis is an important part of material design. For materials with
complex microstructures, such as two-phase random materials (TRMs), material
failure is often accompanied by stress concentration. Phase interfaces in
two-phase materials are critical for stress concentration. Therefore, the
prediction error of stress at phase boundaries is crucial. In practical
engineering, the pixels of the obtained material microstructure images are
limited, which limits the resolution of stress images generated by deep
learning methods, making it difficult to observe stress concentration regions.
Existing Image Super-Resolution (ISR) technologies are all based on data-driven
supervised learning. However, stress images have natural physical constraints,
which provide new ideas for new ISR technologies. In this study, we constructed
a stress prediction framework for TRMs. First, the framework uses a proposed
Multiple Compositions U-net (MC U-net) to predict stress in low-resolution
material microstructures. By considering the phase interface information of the
microstructure, the MC U-net effectively reduces the problem of excessive
prediction errors at phase boundaries. Secondly, a Mixed Physics-Informed
Neural Network (MPINN) based method for stress ISR (SRPINN) was proposed. By
introducing the constraints of physical information, the new method does not
require paired stress images for training and can increase the resolution of
stress images to any multiple. This enables a multiscale analysis of the stress
concentration regions at phase boundaries. Finally, we performed stress
analysis on TRMs with different phase volume fractions and loading states
through transfer learning. The results show the proposed stress prediction
framework has satisfactory accuracy and generalization ability....

---

### 53. Global Stress Generation and Spatiotemporal Super-Resolution Physics-Informed Operator under Dynamic Loading for Two-Phase Random Materials

**Authors:** Tengfei Xing, Xiaodan Ren, Jie Li

**Published:** 2025-04-26

**Category:** cs.LG

**ID:** 2505.01438v1

**Link:** [http://arxiv.org/abs/2505.01438v1](http://arxiv.org/abs/2505.01438v1)

**Summary:** Material stress analysis is a critical aspect of material design and
performance optimization. Under dynamic loading, the global stress evolution in
materials exhibits complex spatiotemporal characteristics, especially in
two-phase random materials (TRMs). Such kind of material failure is often
associated with stress concentration, and the phase boundaries are key
locations where stress concentration occurs. In practical engineering
applications, the spatiotemporal resolution of acquired microstructural data
and its dynamic stress evolution is often limited. This poses challenges for
deep learning methods in generating high-resolution spatiotemporal stress
fields, particularly for accurately capturing stress concentration regions. In
this study, we propose a framework for global stress generation and
spatiotemporal super-resolution in TRMs under dynamic loading. First, we
introduce a diffusion model-based approach, named as Spatiotemporal Stress
Diffusion (STS-diffusion), for generating global spatiotemporal stress data.
This framework incorporates Space-Time U-Net (STU-net), and we systematically
investigate the impact of different attention positions on model accuracy.
Next, we develop a physics-informed network for spatiotemporal
super-resolution, termed as Spatiotemporal Super-Resolution Physics-Informed
Operator (ST-SRPINN). The proposed ST-SRPINN is an unsupervised learning
method. The influence of data-driven and physics-informed loss function weights
on model accuracy is explored in detail. Benefiting from physics-based
constraints, ST-SRPINN requires only low-resolution stress field data during
training and can upscale the spatiotemporal resolution of stress fields to
arbitrary magnifications....

---

### 54. Practical approaches for crystal structure predictions with inpainting generation and universal interatomic potentials

**Authors:** Peichen Zhong, Xinzhe Dai, Bowen Deng, Gerbrand Ceder, Kristin A. Persson

**Published:** 2025-04-23

**Category:** cond-mat.mtrl-sci

**ID:** 2504.16893v1

**Link:** [http://arxiv.org/abs/2504.16893v1](http://arxiv.org/abs/2504.16893v1)

**Summary:** We present Crystal Host-Guided Generation (CHGGen), a diffusion-based
framework for crystal structure prediction. Unconditional generation with
diffusion models demonstrates limited efficacy in identifying symmetric
crystals as the unit cell size increases. CHGGen addresses this limitation
through conditional generation with the inpainting method, which optimizes a
fraction of atomic positions within a predefined and symmetrized host
structure. We demonstrate the method on the ZnS-P$_2$S$_5$ and Li-Si chemical
systems, where the inpainting method generates a higher fraction of symmetric
structures than unconditional generation. The practical significance of CHGGen
extends to enabling the structural modification of crystal structures,
particularly for systems with partial occupancy, surface absorption and
defects. The inpainting method also allows for seamless integration with other
generative models, providing a versatile framework for accelerating materials
discovery....

---

### 55. Constrained composite Bayesian optimization for rational synthesis of polymeric particles

**Authors:** Fanjin Wang, Maryam Parhizkar, Anthony Harker, Mohan Edirisinghe

**Published:** 2024-11-06

**Category:** cs.LG

**ID:** 2411.10471v2

**Link:** [http://arxiv.org/abs/2411.10471v2](http://arxiv.org/abs/2411.10471v2)

**Summary:** Polymeric nano- and micro-scale particles have critical roles in tackling
critical healthcare and energy challenges with their miniature characteristics.
However, tailoring their synthesis process to meet specific design targets has
traditionally depended on domain expertise and costly trial-and-errors.
Recently, modeling strategies, particularly Bayesian optimization (BO), have
been proposed to aid materials discovery for maximized/minimized properties.
Coming from practical demands, this study for the first time integrates
constrained and composite Bayesian optimization (CCBO) to perform efficient
target value optimization under black-box feasibility constraints and limited
data for laboratory experimentation. Using a synthetic problem that simulates
electrospraying, a model nanomanufacturing process, CCBO strategically avoided
infeasible conditions and efficiently optimized particle production towards
predefined size targets, surpassing standard BO pipelines and providing
decisions comparable to human experts. Further laboratory experiments validated
CCBO capability to guide the rational synthesis of poly(lactic-co-glycolic
acid) (PLGA) particles with diameters of 300 nm and 3.0 $\mu$m via
electrospraying. With minimal initial data and unknown experiment constraints,
CCBO reached the design targets within 4 iterations. Overall, the CCBO approach
presents a versatile and holistic optimization paradigm for next-generation
target-driven particle synthesis empowered by artificial intelligence (AI)....

---

### 56. System of Agentic AI for the Discovery of Metal-Organic Frameworks

**Authors:** Theo Jaffrelot Inizan, Sherry Yang, Aaron Kaplan, Yen-hsu Lin, Jian Yin, Saber Mirzaei, Mona Abdelgaid, Ali H. Alawadhi, KwangHwan Cho, Zhiling Zheng, Ekin Dogus Cubuk, Christian Borgs, Jennifer T. Chayes, Kristin A. Persson, Omar M. Yaghi

**Published:** 2025-04-18

**Category:** cond-mat.mtrl-sci

**ID:** 2504.14110v1

**Link:** [http://arxiv.org/abs/2504.14110v1](http://arxiv.org/abs/2504.14110v1)

**Summary:** Generative models and machine learning promise accelerated material discovery
in MOFs for CO2 capture and water harvesting but face significant challenges
navigating vast chemical spaces while ensuring synthetizability. Here, we
present MOFGen, a system of Agentic AI comprising interconnected agents: a
large language model that proposes novel MOF compositions, a diffusion model
that generates crystal structures, quantum mechanical agents that optimize and
filter candidates, and synthetic-feasibility agents guided by expert rules and
machine learning. Trained on all experimentally reported MOFs and computational
databases, MOFGen generated hundreds of thousands of novel MOF structures and
synthesizable organic linkers. Our methodology was validated through
high-throughput experiments and the successful synthesis of five "AI-dreamt"
MOFs, representing a major step toward automated synthesizable material
discovery....

---

### 57. Design Topological Materials by Reinforcement Fine-Tuned Generative Model

**Authors:** Haosheng Xu, Dongheng Qian, Zhixuan Liu, Yadong Jiang, Jing Wang

**Published:** 2025-04-17

**Category:** cond-mat.mtrl-sci

**ID:** 2504.13048v1

**Link:** [http://arxiv.org/abs/2504.13048v1](http://arxiv.org/abs/2504.13048v1)

**Summary:** Topological insulators (TIs) and topological crystalline insulators (TCIs)
are materials with unconventional electronic properties, making their discovery
highly valuable for practical applications. However, such materials,
particularly those with a full band gap, remain scarce. Given the limitations
of traditional approaches that scan known materials for candidates, we focus on
the generation of new topological materials through a generative model.
Specifically, we apply reinforcement fine-tuning (ReFT) to a pre-trained
generative model, thereby aligning the model's objectives with our material
design goals. We demonstrate that ReFT is effective in enhancing the model's
ability to generate TIs and TCIs, with minimal compromise on the stability of
the generated materials. Using the fine-tuned model, we successfully identify a
large number of new topological materials, with Ge$_2$Bi$_2$O$_6$ serving as a
representative example--a TI with a full band gap of 0.26 eV, ranking among the
largest known in this category....

---

### 58. Design Editing for Offline Model-based Optimization

**Authors:** Ye Yuan, Youyuan Zhang, Can Chen, Haolun Wu, Zixuan Li, Jianmo Li, James J. Clark, Xue Liu

**Published:** 2024-05-22

**Category:** cs.LG

**ID:** 2405.13964v4

**Link:** [http://arxiv.org/abs/2405.13964v4](http://arxiv.org/abs/2405.13964v4)

**Summary:** Offline model-based optimization (MBO) aims to maximize a black-box objective
function using only an offline dataset of designs and scores. These tasks span
various domains, such as robotics, material design, and protein and molecular
engineering. A common approach involves training a surrogate model using
existing designs and their corresponding scores, and then generating new
designs through gradient-based updates with respect to the surrogate model.
This method suffers from the out-of-distribution issue, where the surrogate
model may erroneously predict high scores for unseen designs. To address this
challenge, we introduce a novel method, Design Editing for Offline Model-based
Optimization (DEMO), which leverages a diffusion prior to calibrate overly
optimized designs. DEMO first generates pseudo design candidates by performing
gradient ascent with respect to a surrogate model. While these pseudo design
candidates contain information beyond the offline dataset, they might be
invalid or have erroneously high predicted scores. Therefore, to address this
challenge while utilizing the information provided by pseudo design candidates,
we propose an editing process to refine these pseudo design candidates. We
introduce noise to the pseudo design candidates and subsequently denoise them
with a diffusion prior trained on the offline dataset, ensuring they align with
the distribution of valid designs. Empirical evaluations on seven offline MBO
tasks show that, with properly tuned hyperparameters, DEMOs score is
competitive with the best previously reported scores in the literature....

---

### 59. Towards High-Voltage Cathodes for Zinc-Ion Batteries: Discovery Pipeline and Material Design Rules

**Authors:** Roberta Pascazio, Qian Chen, Haoming Howard Li, Aaron D. Kaplan, Kristin A. Persson

**Published:** 2025-04-16

**Category:** cond-mat.mtrl-sci

**ID:** 2504.11678v1

**Link:** [http://arxiv.org/abs/2504.11678v1](http://arxiv.org/abs/2504.11678v1)

**Summary:** Efficient energy storage systems are crucial to address the intermittency of
renewable energy sources. As multivalent batteries, Zn-ion batteries (ZIBs),
while inherently low voltage, offer a promising low cost alternative to Li-ion
batteries due to viable use of zinc as the anode. However, to maximize the
potential impact of ZIBs, rechargable cathodes with improved Zn diffusion are
needed. To better understand the chemical and structural factors influencing
Zn-ion mobility within battery electrode materials, we employ a high-throughput
computational screening approach to systematically evaluate candidate
intercalation hosts for ZIB cathodes, expanding the chemical search space on
empty intercalation hosts that do not contain Zn. We leverage a high-throughput
screening funnel to identify promising cathodes in ZIBs, integrating screening
criteria with DFT-based calculations of Zn$^{2+}$ intercalation and diffusion
inside the host materials. Using this data, we identify the design principles
that favor Zn-ion mobility in candidate cathode materials. Building on previous
work on divalent ion cathodes, this study broadens the chemical space for
next-generation multivalent energy storage systems....

---

### 60. MatWheel: Addressing Data Scarcity in Materials Science Through Synthetic Data

**Authors:** Wentao Li, Yizhe Chen, Jiangjie Qiu, Xiaonan Wang

**Published:** 2025-04-12

**Category:** cs.LG

**ID:** 2504.09152v1

**Link:** [http://arxiv.org/abs/2504.09152v1](http://arxiv.org/abs/2504.09152v1)

**Summary:** Data scarcity and the high cost of annotation have long been persistent
challenges in the field of materials science. Inspired by its potential in
other fields like computer vision, we propose the MatWheel framework, which
train the material property prediction model using the synthetic data generated
by the conditional generative model. We explore two scenarios: fully-supervised
and semi-supervised learning. Using CGCNN for property prediction and Con-CDVAE
as the conditional generative model, experiments on two data-scarce material
property datasets from Matminer database are conducted. Results show that
synthetic data has potential in extreme data-scarce scenarios, achieving
performance close to or exceeding that of real samples in all two tasks. We
also find that pseudo-labels have little impact on generated data quality.
Future work will integrate advanced models and optimize generation conditions
to boost the effectiveness of the materials data flywheel....

---

### 61. PriM: Principle-Inspired Material Discovery through Multi-Agent Collaboration

**Authors:** Zheyuan Lai, Yingming Pu

**Published:** 2025-04-09

**Category:** cs.LG

**ID:** 2504.08810v1

**Link:** [http://arxiv.org/abs/2504.08810v1](http://arxiv.org/abs/2504.08810v1)

**Summary:** Complex chemical space and limited knowledge scope with biases holds immense
challenge for human scientists, yet in automated materials discovery. Existing
intelligent methods relies more on numerical computation, leading to
inefficient exploration and results with hard-interpretability. To bridge this
gap, we introduce a principles-guided material discovery system powered by
language inferential multi-agent system (MAS), namely PriM. Our framework
integrates automated hypothesis generation with experimental validation in a
roundtable system of MAS, enabling systematic exploration while maintaining
scientific rigor. Based on our framework, the case study of nano helix
demonstrates higher materials exploration rate and property value while
providing transparent reasoning pathways. This approach develops an
automated-and-transparent paradigm for material discovery, with broad
implications for rational design of functional materials. Code is publicly
available at our \href{https://github.com/amair-lab/PriM}{GitHub}....

---

### 62. Structured Extraction of Process Structure Properties Relationships in Materials Science

**Authors:** Amit K Verma, Zhisong Zhang, Junwon Seo, Robin Kuo, Runbo Jiang, Emma Strubell, Anthony D Rollett

**Published:** 2025-04-04

**Category:** cs.CL

**ID:** 2504.03979v1

**Link:** [http://arxiv.org/abs/2504.03979v1](http://arxiv.org/abs/2504.03979v1)

**Summary:** With the advent of large language models (LLMs), the vast unstructured text
within millions of academic papers is increasingly accessible for materials
discovery, although significant challenges remain. While LLMs offer promising
few- and zero-shot learning capabilities, particularly valuable in the
materials domain where expert annotations are scarce, general-purpose LLMs
often fail to address key materials-specific queries without further
adaptation. To bridge this gap, fine-tuning LLMs on human-labeled data is
essential for effective structured knowledge extraction. In this study, we
introduce a novel annotation schema designed to extract generic
process-structure-properties relationships from scientific literature. We
demonstrate the utility of this approach using a dataset of 128 abstracts, with
annotations drawn from two distinct domains: high-temperature materials (Domain
I) and uncertainty quantification in simulating materials microstructure
(Domain II). Initially, we developed a conditional random field (CRF) model
based on MatBERT, a domain-specific BERT variant, and evaluated its performance
on Domain I. Subsequently, we compared this model with a fine-tuned LLM (GPT-4o
from OpenAI) under identical conditions. Our results indicate that fine-tuning
LLMs can significantly improve entity extraction performance over the BERT-CRF
baseline on Domain I. However, when additional examples from Domain II were
incorporated, the performance of the BERT-CRF model became comparable to that
of the GPT-4o model. These findings underscore the potential of our schema for
structured knowledge extraction and highlight the complementary strengths of
both modeling approaches....

---

### 63. Accurate and efficient protocols for high-throughput first-principles materials simulations

**Authors:** Gabriel de Miranda Nascimento, Flaviano José dos Santos, Marnik Bercx, Davide Grassano, Giovanni Pizzi, Nicola Marzari

**Published:** 2025-04-04

**Category:** cond-mat.mtrl-sci

**ID:** 2504.03962v1

**Link:** [http://arxiv.org/abs/2504.03962v1](http://arxiv.org/abs/2504.03962v1)

**Summary:** Advancements in theoretical and algorithmic approaches, workflow engines, and
an ever-increasing computational power have enabled a novel paradigm for
materials discovery through first-principles high-throughput simulations. A
major challenge in these efforts is to automate the selection of parameters
used by simulation codes to deliver numerical precision and computational
efficiency. Here, we propose a rigorous methodology to assess the quality of
self-consistent DFT calculations with respect to smearing and $k$-point
sampling across a wide range of crystalline materials. For this goal, we
develop criteria to reliably estimate average errors on total energies, forces,
and other properties as a function of the desired computational efficiency,
while consistently controlling $k$-point sampling errors. The present results
provide automated protocols (named standard solid-state protocols or SSSP) for
selecting optimized parameters based on different choices of precision and
efficiency tradeoffs. These are available through open-source tools that range
from interactive input generators for DFT codes to high-throughput workflows....

---

### 64. RAFFLE: Active learning accelerated interface structure prediction

**Authors:** Ned Thaddeus Taylor, Joe Pitfield, Francis Huw Davies, Steven Paul Hepplestone

**Published:** 2025-04-03

**Category:** cond-mat.mtrl-sci

**ID:** 2504.02528v1

**Link:** [http://arxiv.org/abs/2504.02528v1](http://arxiv.org/abs/2504.02528v1)

**Summary:** Interfaces between materials play a crucial role in the performance of most
devices. However, predicting the structure of a material interface is
computationally demanding due to the vast configuration space, which requires
evaluating an unfeasibly large number of highly complex structures. We
introduce RAFFLE, a software package designed to efficiently explore low-energy
interface configurations between any two crystals. RAFFLE leverages physical
insights and genetic algorithms to intelligently sample the configuration
space, using dynamically evolving 2-, 3-, and 4-body distribution functions as
generalised structural descriptors. These descriptors are iteratively updated
through active learning, which inform atom placement strategies. RAFFLE's
effectiveness is demonstrated across a diverse set of systems, including bulk
materials, intercalation structures, and interfaces. When tested on bulk
aluminium and MoS$_2$, it successfully identifies known ground-state and
high-pressure phases. Applied to intercalation systems, it predicts stable
intercalant phases. For Si|Ge interfaces, RAFFLE identifies intermixing as a
strain compensation mechanism, generating reconstructions that are more stable
than abrupt interfaces. By accelerating interface structure prediction, RAFFLE
offers a powerful tool for materials discovery, enabling efficient exploration
of complex configuration spaces....

---

### 65. CrystalFormer-RL: Reinforcement Fine-Tuning for Materials Design

**Authors:** Zhendong Cao, Lei Wang

**Published:** 2025-04-03

**Category:** cond-mat.mtrl-sci

**ID:** 2504.02367v1

**Link:** [http://arxiv.org/abs/2504.02367v1](http://arxiv.org/abs/2504.02367v1)

**Summary:** Reinforcement fine-tuning has instrumental enhanced the instruction-following
and reasoning abilities of large language models. In this work, we explore the
applications of reinforcement fine-tuning to the autoregressive
transformer-based materials generative model CrystalFormer (arXiv:2403.15734)
using discriminative machine learning models such as interatomic potentials and
property prediction models. By optimizing reward signals-such as energy above
the convex hull and material property figures of merit-reinforcement
fine-tuning infuses knowledge from discriminative models into generative
models. The resulting model, CrystalFormer-RL, shows enhanced stability in
generated crystals and successfully discovers crystals with desirable yet
conflicting material properties, such as substantial dielectric constant and
band gap simultaneously. Notably, we observe that reinforcement fine-tuning
enables not only the property-guided novel material design ability of
generative pre-trained model but also unlocks property-driven material
retrieval from the unsupervised pre-training dataset. Leveraging rewards from
discriminative models to fine-tune materials generative models opens an
exciting gateway to the synergies of the machine learning ecosystem for
materials....

---

### 66. Accelerating the discovery of high-performance nonlinear optical materials using active learning and high-throughput screening

**Authors:** Victor Trinquet, Matthew L. Evans, Gian-Marco Rignanese

**Published:** 2025-04-02

**Category:** cond-mat.mtrl-sci

**ID:** 2504.01526v1

**Link:** [http://arxiv.org/abs/2504.01526v1](http://arxiv.org/abs/2504.01526v1)

**Summary:** Due to their abundant use in all-solid-state lasers, nonlinear optical (NLO)
crystals are needed for many applications across diverse fields such as
medicine and communication. However, because of conflicting requirements, the
design of suitable inorganic crystals with strong second-harmonic generation
(SHG) has proven to be challenging to both experimentalists and computational
scientists. In this work, we leverage a data-driven approach to accelerate the
search for high-performance NLO materials. We construct an extensive pool of
candidates using databases within the OPTIMADE federation and employ an active
learning strategy to gather optimal data while iteratively improving a machine
learning model. The result is a publicly accessible dataset of $\sim$2,200
computed SHG tensors using density-functional perturbation theory. We further
assess the performance of machine learning models on SHG prediction and
introduce a multi-fidelity correction-learning scheme to refine data accuracy.
This study represents a significant step towards data-driven materials
discovery in the NLO field and demonstrates how new materials can be screened
in an automated fashion....

---

### 67. Electronic density of states as the descriptor of elastic bond strength, ductility, and local lattice distortion in BCC refractory alloys

**Authors:** Dharmendra Pant, Dilpuneet S. Aidhy

**Published:** 2024-11-07

**Category:** cond-mat.mtrl-sci

**ID:** 2411.05179v2

**Link:** [http://arxiv.org/abs/2411.05179v2](http://arxiv.org/abs/2411.05179v2)

**Summary:** Although electronic density of states (DOS) is fundamental to materials
properties, its general relationship to mechanical properties of alloys is not
well established. In this paper, using density functional theory (DFT)
calculations, we show that the electronic occupancy at the Fermi level, N(Ef),
obtained from DOS is a key descriptor of alloy strength and ductility. Our
comprehensive analysis of numerous body centered cubic (BCC) refractory high
entropy alloys (RHEAs) shows an overwhelming correlation that low N(Ef)
indicates strong bonds that have high stiffness resulting in high elastic
constants. High bond stiffness indicates presence of covalent nature of bonds
that are directional in nature resulting in resistance to deformation leading
to high bulk (B) and shear (G) moduli. Consequently, N(Ef) provides a direct
correlation to the tendency of alloy ductility evidenced in the Pugh ratio
(G/B). As stiffer bonds result in lower local lattice distortion (LLD), N(Ef)
are LLD are also found to be corelated which opens up a correlation to solid
solution strengthening and yield strength. Thus, this work unveils fundamental
correlations between N(Ef) and (1) elastic bond strength, (2) ductility, and
(3) LLD. These correlations open opportunities for the design of high strength
high ductile RHEAs....

---

### 68. Accelerated Inorganic Materials Design with Generative AI Agents

**Authors:** Izumi Takahara, Teruyasu Mizoguchi, Bang Liu

**Published:** 2025-04-01

**Category:** cond-mat.mtrl-sci

**ID:** 2504.00741v1

**Link:** [http://arxiv.org/abs/2504.00741v1](http://arxiv.org/abs/2504.00741v1)

**Summary:** Designing inorganic crystalline materials with tailored properties is
critical to technological innovation, yet current generative computational
methods often struggle to efficiently explore desired targets with sufficient
interpretability. Here, we present MatAgent, a generative approach for
inorganic materials discovery that harnesses the powerful reasoning
capabilities of large language models (LLMs). By combining a diffusion-based
generative model for crystal structure estimation with a predictive model for
property evaluation, MatAgent uses iterative, feedback-driven guidance to steer
material exploration precisely toward user-defined targets. Integrated with
external cognitive tools-including short-term memory, long-term memory, the
periodic table, and a comprehensive materials knowledge base-MatAgent emulates
human expert reasoning to vastly expand the accessible compositional space. Our
results demonstrate that MatAgent robustly directs exploration toward desired
properties while consistently achieving high compositional validity,
uniqueness, and material novelty. This framework thus provides a highly
interpretable, practical, and versatile AI-driven solution to accelerate the
discovery and design of next-generation inorganic materials....

---

### 69. Force-Free Molecular Dynamics Through Autoregressive Equivariant Networks

**Authors:** Fabian L. Thiemann, Thiago Reschützegger, Massimiliano Esposito, Tseden Taddese, Juan D. Olarte-Plata, Fausto Martelli

**Published:** 2025-03-31

**Category:** physics.comp-ph

**ID:** 2503.23794v1

**Link:** [http://arxiv.org/abs/2503.23794v1](http://arxiv.org/abs/2503.23794v1)

**Summary:** Molecular dynamics (MD) simulations play a crucial role in scientific
research. Yet their computational cost often limits the timescales and system
sizes that can be explored. Most data-driven efforts have been focused on
reducing the computational cost of accurate interatomic forces required for
solving the equations of motion. Despite their success, however, these machine
learning interatomic potentials (MLIPs) are still bound to small time-steps. In
this work, we introduce TrajCast, a transferable and data-efficient framework
based on autoregressive equivariant message passing networks that directly
updates atomic positions and velocities lifting the constraints imposed by
traditional numerical integration. We benchmark our framework across various
systems, including a small molecule, crystalline material, and bulk liquid,
demonstrating excellent agreement with reference MD simulations for structural,
dynamical, and energetic properties. Depending on the system, TrajCast allows
for forecast intervals up to $30\times$ larger than traditional MD time-steps,
generating over 15 ns of trajectory data per day for a solid with more than
4,000 atoms. By enabling efficient large-scale simulations over extended
timescales, TrajCast can accelerate materials discovery and explore physical
phenomena beyond the reach of traditional simulations and experiments. An
open-source implementation of TrajCast is accessible under
https://github.com/IBM/trajcast....

---

### 70. Accelerating High-Efficiency Organic Photovoltaic Discovery via Pretrained Graph Neural Networks and Generative Reinforcement Learning

**Authors:** Jiangjie Qiu, Hou Hei Lam, Xiuyuan Hu, Wentao Li, Siwei Fu, Fankun Zeng, Hao Zhang, Xiaonan Wang

**Published:** 2025-03-31

**Category:** cs.LG

**ID:** 2503.23766v1

**Link:** [http://arxiv.org/abs/2503.23766v1](http://arxiv.org/abs/2503.23766v1)

**Summary:** Organic photovoltaic (OPV) materials offer a promising avenue toward
cost-effective solar energy utilization. However, optimizing donor-acceptor
(D-A) combinations to achieve high power conversion efficiency (PCE) remains a
significant challenge. In this work, we propose a framework that integrates
large-scale pretraining of graph neural networks (GNNs) with a GPT-2
(Generative Pretrained Transformer 2)-based reinforcement learning (RL)
strategy to design OPV molecules with potentially high PCE. This approach
produces candidate molecules with predicted efficiencies approaching 21\%,
although further experimental validation is required. Moreover, we conducted a
preliminary fragment-level analysis to identify structural motifs recognized by
the RL model that may contribute to enhanced PCE, thus providing design
guidelines for the broader research community. To facilitate continued
discovery, we are building the largest open-source OPV dataset to date,
expected to include nearly 3,000 donor-acceptor pairs. Finally, we discuss
plans to collaborate with experimental teams on synthesizing and characterizing
AI-designed molecules, which will provide new data to refine and improve our
predictive and generative models....

---

### 71. Fast Direct: Query-Efficient Online Black-box Guidance for Diffusion-model Target Generation

**Authors:** Kim Yong Tan, Yueming Lyu, Ivor Tsang, Yew-Soon Ong

**Published:** 2025-02-02

**Category:** cs.LG

**ID:** 2502.01692v5

**Link:** [http://arxiv.org/abs/2502.01692v5](http://arxiv.org/abs/2502.01692v5)

**Summary:** Guided diffusion-model generation is a promising direction for customizing
the generation process of a pre-trained diffusion model to address specific
downstream tasks. Existing guided diffusion models either rely on training the
guidance model with pre-collected datasets or require the objective functions
to be differentiable. However, for most real-world tasks, offline datasets are
often unavailable, and their objective functions are often not differentiable,
such as image generation with human preferences, molecular generation for drug
discovery, and material design. Thus, we need an $\textbf{online}$ algorithm
capable of collecting data during runtime and supporting a $\textbf{black-box}$
objective function. Moreover, the $\textbf{query efficiency}$ of the algorithm
is also critical because the objective evaluation of the query is often
expensive in real-world scenarios. In this work, we propose a novel and simple
algorithm, $\textbf{Fast Direct}$, for query-efficient online black-box target
generation. Our Fast Direct builds a pseudo-target on the data manifold to
update the noise sequence of the diffusion model with a universal direction,
which is promising to perform query-efficient guided generation. Extensive
experiments on twelve high-resolution ($\small {1024 \times 1024}$) image
target generation tasks and six 3D-molecule target generation tasks show
$\textbf{6}\times$ up to $\textbf{10}\times$ query efficiency improvement and
$\textbf{11}\times$ up to $\textbf{44}\times$ query efficiency improvement,
respectively. Our implementation is publicly available at:
https://github.com/kimyong95/guide-stable-diffusion/tree/fast-direct...

---

### 72. AI-Driven Defect Engineering for Advanced Thermoelectric Materials

**Authors:** Chu-Liang Fu, Mouyang Cheng, Nguyen Tuan Hung, Eunbi Rha, Zhantao Chen, Ryotaro Okabe, Denisse Córdova Carrizales, Manasi Mandal, Yongqiang Cheng, Mingda Li

**Published:** 2025-03-24

**Category:** cond-mat.mtrl-sci

**ID:** 2503.19148v1

**Link:** [http://arxiv.org/abs/2503.19148v1](http://arxiv.org/abs/2503.19148v1)

**Summary:** Thermoelectric materials offer a promising pathway to directly convert waste
heat to electricity. However, achieving high performance remains challenging
due to intrinsic trade-offs between electrical conductivity, the Seebeck
coefficient, and thermal conductivity, which are further complicated by the
presence of defects. This review explores how artificial intelligence (AI) and
machine learning (ML) are transforming thermoelectric materials design.
Advanced ML approaches including deep neural networks, graph-based models, and
transformer architectures, integrated with high-throughput simulations and
growing databases, effectively capture structure-property relationships in a
complex multiscale defect space and overcome the curse of dimensionality. This
review discusses AI-enhanced defect engineering strategies such as composition
optimization, entropy and dislocation engineering, and grain boundary design,
along with emerging inverse design techniques for generating materials with
targeted properties. Finally, it outlines future opportunities in novel physics
mechanisms and sustainability, highlighting the critical role of AI in
accelerating the discovery of thermoelectric materials....

---

### 73. Offline Model-Based Optimization: Comprehensive Review

**Authors:** Minsu Kim, Jiayao Gu, Ye Yuan, Taeyoung Yun, Zixuan Liu, Yoshua Bengio, Can Chen

**Published:** 2025-03-21

**Category:** cs.LG

**ID:** 2503.17286v1

**Link:** [http://arxiv.org/abs/2503.17286v1](http://arxiv.org/abs/2503.17286v1)

**Summary:** Offline optimization is a fundamental challenge in science and engineering,
where the goal is to optimize black-box functions using only offline datasets.
This setting is particularly relevant when querying the objective function is
prohibitively expensive or infeasible, with applications spanning protein
engineering, material discovery, neural architecture search, and beyond. The
main difficulty lies in accurately estimating the objective landscape beyond
the available data, where extrapolations are fraught with significant epistemic
uncertainty. This uncertainty can lead to objective hacking(reward hacking),
exploiting model inaccuracies in unseen regions, or other spurious
optimizations that yield misleadingly high performance estimates outside the
training distribution. Recent advances in model-based optimization(MBO) have
harnessed the generalization capabilities of deep neural networks to develop
offline-specific surrogate and generative models. Trained with carefully
designed strategies, these models are more robust against out-of-distribution
issues, facilitating the discovery of improved designs. Despite its growing
impact in accelerating scientific discovery, the field lacks a comprehensive
review. To bridge this gap, we present the first thorough review of offline
MBO. We begin by formalizing the problem for both single-objective and
multi-objective settings and by reviewing recent benchmarks and evaluation
metrics. We then categorize existing approaches into two key areas: surrogate
modeling, which emphasizes accurate function approximation in
out-of-distribution regions, and generative modeling, which explores
high-dimensional design spaces to identify high-performing designs. Finally, we
examine the key challenges and propose promising directions for advancement in
this rapidly evolving field including safe control of superintelligent systems....

---

### 74. Quantum defects in 2D transition metal dichalcogenides for THz-technologies

**Authors:** Jingda Zhang, Su Ying Quek

**Published:** 2023-11-18

**Category:** cond-mat.mtrl-sci

**ID:** 2311.11092v2

**Link:** [http://arxiv.org/abs/2311.11092v2](http://arxiv.org/abs/2311.11092v2)

**Summary:** Substitutional transition metal (TM) point defects have recently been
controllably introduced in two-dimensional (2D) transition metal
dichalcogenides. We identify quantum defect candidates through a first
principles materials discovery approach with 25 TM elements substituting Mo and
W in 2D MoS2 and WSe2, respectively. We elucidate trends in the charge
transition levels for these 50 systems and report the existence of defects with
spin-triplet ground states and a zero field splitting (ZFS) in the terahertz
(THz) regime, in contrast to typical gigahertz values. These defects can couple
to resonant near-infrared radiation, providing a route to applications as high
fidelity qubits controlled by spin-dependent optical transitions. The THz ZFS
implies that these high-fidelity operations can take place at higher
temperatures compared to the case for GHz qubits. Our results also point toward
the possibility of realizing a single photon THz emitter. This work broadens
the scope of quantum defects, laying the foundation for next generation THz
quantum technologies, a timely and significant research area given the rapid
advancement in the development of THz sources and detectors....

---

### 75. Multi-property directed generative design of inorganic materials through Wyckoff-augmented transfer learning

**Authors:** Shuya Yamazaki, Wei Nong, Ruiming Zhu, Kostya S. Novoselov, Andrey Ustyuzhanin, Kedar Hippalgaonkar

**Published:** 2025-03-21

**Category:** cond-mat.mtrl-sci

**ID:** 2503.16784v1

**Link:** [http://arxiv.org/abs/2503.16784v1](http://arxiv.org/abs/2503.16784v1)

**Summary:** Accelerated materials discovery is an urgent demand to drive advancements in
fields such as energy conversion, storage, and catalysis. Property-directed
generative design has emerged as a transformative approach for rapidly
discovering new functional inorganic materials with multiple desired properties
within vast and complex search spaces. However, this approach faces two primary
challenges: data scarcity for functional properties and the multi-objective
optimization required to balance competing tasks. Here, we present a
multi-property-directed generative framework designed to overcome these
limitations and enhance site symmetry-compliant crystal generation beyond P1
(translational) symmetry. By incorporating Wyckoff-position-based data
augmentation and transfer learning, our framework effectively handles sparse
and small functional datasets, enabling the generation of new stable materials
simultaneously conditioned on targeted space group, band gap, and formation
energy. Using this approach, we identified previously unknown thermodynamically
and lattice-dynamically stable semiconductors in tetragonal, trigonal, and
cubic systems, with bandgaps ranging from 0.13 to 2.20 eV, as validated by
density functional theory (DFT) calculations. Additionally, we assessed their
thermoelectric descriptors using DFT, indicating their potential suitability
for thermoelectric applications. We believe our integrated framework represents
a significant step forward in generative design of inorganic materials....

---

### 76. Dynamic Backtracking in GFlowNets: Enhancing Decision Steps with Reward-Dependent Adjustment Mechanisms

**Authors:** Shuai Guo, Jielei Chu, Lin Ma, Zhaoyu Li, Tianrui Li

**Published:** 2024-04-08

**Category:** cs.LG

**ID:** 2404.05576v6

**Link:** [http://arxiv.org/abs/2404.05576v6](http://arxiv.org/abs/2404.05576v6)

**Summary:** Generative Flow Networks (GFlowNets or GFNs) are probabilistic models
predicated on Markov flows, and they employ specific amortization algorithms to
learn stochastic policies that generate compositional substances including
biomolecules, chemical materials, etc. With a strong ability to generate
high-performance biochemical molecules, GFNs accelerate the discovery of
scientific substances, effectively overcoming the time-consuming,
labor-intensive, and costly shortcomings of conventional material discovery
methods. However, previous studies rarely focus on accumulating exploratory
experience by adjusting generative structures, which leads to disorientation in
complex sampling spaces. Efforts to address this issue, such as LS-GFN, are
limited to local greedy searches and lack broader global adjustments. This
paper introduces a novel variant of GFNs, the Dynamic Backtracking GFN
(DB-GFN), which improves the adaptability of decision-making steps through a
reward-based dynamic backtracking mechanism. DB-GFN allows backtracking during
the network construction process according to the current state's reward value,
thereby correcting disadvantageous decisions and exploring alternative pathways
during the exploration process. When applied to generative tasks involving
biochemical molecules and genetic material sequences, DB-GFN outperforms GFN
models such as LS-GFN and GTB, as well as traditional reinforcement learning
methods, in sample quality, sample exploration quantity, and training
convergence speed. Additionally, owing to its orthogonal nature, DB-GFN shows
great potential in future improvements of GFNs, and it can be integrated with
other strategies to achieve higher search performance....

---

### 77. FastCHGNet: Training one Universal Interatomic Potential to 1.5 Hours with 32 GPUs

**Authors:** Yuanchang Zhou, Siyu Hu, Chen Wang, Lin-Wang Wang, Guangming Tan, Weile Jia

**Published:** 2024-12-30

**Category:** cs.DC

**ID:** 2412.20796v2

**Link:** [http://arxiv.org/abs/2412.20796v2](http://arxiv.org/abs/2412.20796v2)

**Summary:** Graph neural network universal interatomic potentials (GNN-UIPs) have
demonstrated remarkable generalization and transfer capabilities in material
discovery and property prediction. These models can accelerate molecular
dynamics (MD) simulation by several orders of magnitude while maintaining
\textit{ab initio} accuracy, making them a promising new paradigm in material
simulations. One notable example is Crystal Hamiltonian Graph Neural Network
(CHGNet), pretrained on the energies, forces, stresses, and magnetic moments
from the MPtrj dataset, representing a state-of-the-art GNN-UIP model for
charge-informed MD simulations. However, training the CHGNet model is
time-consuming(8.3 days on one A100 GPU) for three reasons: (i) requiring
multi-layer propagation to reach more distant atom information, (ii) requiring
second-order derivatives calculation to finish weights updating and (iii) the
implementation of reference CHGNet does not fully leverage the computational
capabilities. This paper introduces FastCHGNet, an optimized CHGNet, with three
contributions: Firstly, we design innovative Force/Stress Readout modules to
decompose Force/Stress prediction. Secondly, we adopt massive optimizations
such as kernel fusion, redundancy bypass, etc, to exploit GPU computation power
sufficiently. Finally, we extend CHGNet to support multiple GPUs and propose a
load-balancing technique to enhance GPU utilization. Numerical results show
that FastCHGNet reduces memory footprint by a factor of 3.59. The final
training time of FastCHGNet can be decreased to \textbf{1.53 hours} on 32 GPUs
without sacrificing model accuracy....

---

### 78. 3D Multiphase Heterogeneous Microstructure Generation Using Conditional Latent Diffusion Models

**Authors:** Nirmal Baishnab, Ethan Herron, Aditya Balu, Soumik Sarkar, Adarsh Krishnamurthy, Baskar Ganapathysubramanian

**Published:** 2025-03-12

**Category:** cond-mat.mtrl-sci

**ID:** 2503.10711v1

**Link:** [http://arxiv.org/abs/2503.10711v1](http://arxiv.org/abs/2503.10711v1)

**Summary:** The ability to generate 3D multiphase microstructures on-demand with targeted
attributes can greatly accelerate the design of advanced materials. Here, we
present a conditional latent diffusion model (LDM) framework that rapidly
synthesizes high-fidelity 3D multiphase microstructures tailored to user
specifications. Using this approach, we generate diverse two-phase and
three-phase microstructures at high resolution (volumes of $128 \times 128
\times 64$ voxels, representing $>10^6$ voxels each) within seconds, overcoming
the scalability and time limitations of traditional simulation-based methods.
Key design features, such as desired volume fractions and tortuosities, are
incorporated as controllable inputs to guide the generative process, ensuring
that the output structures meet prescribed statistical and topological targets.
Moreover, the framework predicts corresponding manufacturing (processing)
parameters for each generated microstructure, helping to bridge the gap between
digital microstructure design and experimental fabrication. While demonstrated
on organic photovoltaic (OPV) active-layer morphologies, the flexible
architecture of our approach makes it readily adaptable to other material
systems and microstructure datasets. By combining computational efficiency,
adaptability, and experimental relevance, this framework addresses major
limitations of existing methods and offers a powerful tool for accelerated
materials discovery....

---

### 79. Materials Discovery With Quantum-Enhanced Machine Learning Algorithms

**Authors:** Ignacio F. Graña, Savvas Varsamopoulos, Tatsuhito Ando, Hiroyuki Maeshima, Nobuyuki N. Matsuzawa

**Published:** 2025-03-12

**Category:** cond-mat.mtrl-sci

**ID:** 2503.09517v1

**Link:** [http://arxiv.org/abs/2503.09517v1](http://arxiv.org/abs/2503.09517v1)

**Summary:** Materials discovery is a computationally intensive process that requires
exploring vast chemical spaces to identify promising candidates with desirable
properties. In this work, we propose using quantum-enhanced machine learning
algorithms following the extremal learning framework to predict novel
heteroacene structures with low hole reorganization energy $\lambda$, a key
property for organic semiconductors. We leverage chemical data generated in a
previous large-scale virtual screening to construct three initial training
datasets containing 54, 99 and 119 molecules encoded using $N=7,16$ and 22
bits, respectively. Furthermore, a sequential learning process is employed to
augment the initial training data with compounds predicted by the algorithms
through iterative retraining. Both algorithms are able to successfully
extrapolate to heteroacene structures with lower $\lambda$ than in the initial
dataset, demonstrating good generalization capabilities even when the amount of
initial data is limited. We observe an improvement in the quality of the
predicted compounds as the number of encoding bits $N$ increases, which offers
an exciting prospect for applying the algorithms to richer chemical spaces that
require larger values of $N$ and hence, in perspective, larger quantum circuits
to deploy the proposed quantum-enhanced protocols....

---

### 80. To Use or Not to Use a Universal Force Field

**Authors:** Denan Li, Jiyuan Yang, Xiangkai Chen, Lintao Yu, Shi Liu

**Published:** 2025-03-11

**Category:** physics.comp-ph

**ID:** 2503.08207v1

**Link:** [http://arxiv.org/abs/2503.08207v1](http://arxiv.org/abs/2503.08207v1)

**Summary:** Artificial intelligence (AI) is revolutionizing scientific research,
particularly in computational materials science, by enabling more accurate and
efficient simulations. Machine learning force fields (MLFFs) have emerged as
powerful tools for molecular dynamics (MD) simulations, potentially offering
quantum-mechanical accuracy with the efficiency of classical MD. This
Perspective evaluates the viability of universal MLFFs for simulating complex
materials systems from the standpoint of a potential practitioner. Using the
temperature-driven ferroelectric-paraelectric phase transition of PbTiO$_3$ as
a benchmark, we assess leading universal force fields, including CHGNet, MACE,
M3GNet, and GPTFF, alongside specialized models like UniPero. While universal
MLFFs trained on PBE-derived datasets perform well in predicting equilibrium
properties, they largely fail to capture realistic finite-temperature phase
transitions under constant-pressure MD, often exhibiting unphysical
instabilities. These shortcomings stem from inherited biases in
exchange-correlation functionals and limited generalization to anharmonic
interactions governing dynamic behavior. However, fine-tuning universal models
or employing system-specific MLFFs like UniPero successfully restores
predictive accuracy. We advocates for hybrid approaches combining universal
pretraining with targeted optimization, improved error quantification
frameworks, and community-driven benchmarks to advance MLFFs as robust tools
for computational materials discovery....

---

### 81. Accelerated Discovery of Vanadium Oxide Compositions: A WGAN-VAE Framework for Materials Design

**Authors:** Danial Ebrahimzadeh, Sarah S. Sharif, Yaser M. Banad

**Published:** 2025-01-08

**Category:** cond-mat.mtrl-sci

**ID:** 2501.04604v2

**Link:** [http://arxiv.org/abs/2501.04604v2](http://arxiv.org/abs/2501.04604v2)

**Summary:** The discovery of novel materials with tailored electronic properties is
crucial for modern device technologies, but time-consuming empirical methods
hamper progress. We present an inverse design framework combining an enhanced
Wasserstein Generative Adversarial Network (WGAN) with a specialized
Variational Autoencoder (VAE) to accelerate the discovery of stable vanadium
oxide (V-O) compositions. Our approach features (1) a WGAN with integrated
stability constraints and formation energy predictions, enabling direct
generation of thermodynamically feasible structures, and (2) a refined VAE
capturing atomic positions and lattice parameters while maintaining chemical
validity. Applying this framework, we generated 451 unique V-O compositions,
with 91 stable and 44 metastable under rigorous thermodynamic criteria.
Notably, we uncovered several novel V2O3 configurations with formation energies
below the Materials Project convex hull, revealing previously unknown stable
phases. Detailed spin-polarized DFT+U calculations showed distinct electronic
behaviors, including promising half-metallic characteristics. Our approach
outperforms existing methods in both quality and stability, demonstrating about
a 20 percent stability rate under strict criteria compared to earlier
benchmarks. Additionally, phonon calculations performed on selected
compositions confirm dynamic stability: minor imaginary modes at 0 K likely
stem from finite-size effects or known phase transitions, suggesting that these
materials remain stable or metastable in practical conditions. These findings
establish our framework as a powerful tool for accelerated materials discovery
and highlight promising V-O candidates for next-generation electronic devices....

---

### 82. CrystalGRW: Generative Modeling of Crystal Structures with Targeted Properties via Geodesic Random Walks

**Authors:** Krit Tangsongcharoen, Teerachote Pakornchote, Chayanon Atthapak, Natthaphon Choomphon-anomakhun, Annop Ektarawong, Björn Alling, Christopher Sutton, Thiti Bovornratanaraks, Thiparat Chotibut

**Published:** 2025-01-15

**Category:** cond-mat.mtrl-sci

**ID:** 2501.08998v2

**Link:** [http://arxiv.org/abs/2501.08998v2](http://arxiv.org/abs/2501.08998v2)

**Summary:** Determining whether a candidate crystalline material is thermodynamically
stable depends on identifying its true ground-state structure, a central
challenge in computational materials science. We introduce CrystalGRW, a
diffusion-based generative model on Riemannian manifolds that proposes novel
crystal configurations and can predict stable phases validated by density
functional theory. The crystal properties, such as fractional coordinates,
atomic types, and lattice matrices, are represented on suitable Riemannian
manifolds, ensuring that new predictions generated through the diffusion
process preserve the periodicity of crystal structures. We incorporate an
equivariant graph neural network to also account for rotational and
translational symmetries during the generation process. CrystalGRW demonstrates
the ability to generate realistic crystal structures that are close to their
ground states with accuracy comparable to existing models, while also enabling
conditional control, such as specifying a desired crystallographic point group.
These features help accelerate materials discovery and inverse design by
offering stable, symmetry-consistent crystal candidates for experimental
validation....

---

### 83. Integrating Predictive and Generative Capabilities by Latent Space Design via the DKL-VAE Model

**Authors:** Boris N. Slautin, Utkarsh Pratiush, Doru C. Lupascu, Maxim A. Ziatdinov, Sergei V. Kalinin

**Published:** 2025-03-04

**Category:** cs.LG

**ID:** 2503.02978v1

**Link:** [http://arxiv.org/abs/2503.02978v1](http://arxiv.org/abs/2503.02978v1)

**Summary:** We introduce a Deep Kernel Learning Variational Autoencoder (VAE-DKL)
framework that integrates the generative power of a Variational Autoencoder
(VAE) with the predictive nature of Deep Kernel Learning (DKL). The VAE learns
a latent representation of high-dimensional data, enabling the generation of
novel structures, while DKL refines this latent space by structuring it in
alignment with target properties through Gaussian Process (GP) regression. This
approach preserves the generative capabilities of the VAE while enhancing its
latent space for GP-based property prediction. We evaluate the framework on two
datasets: a structured card dataset with predefined variational factors and the
QM9 molecular dataset, where enthalpy serves as the target function for
optimization. The model demonstrates high-precision property prediction and
enables the generation of novel out-of-training subset structures with desired
characteristics. The VAE-DKL framework offers a promising approach for
high-throughput material discovery and molecular design, balancing structured
latent space organization with generative flexibility....

---

### 84. Pre-training Graph Neural Networks with Structural Fingerprints for Materials Discovery

**Authors:** Shuyi Jia, Shitij Govil, Manav Ramprasad, Victor Fung

**Published:** 2025-03-03

**Category:** cond-mat.mtrl-sci

**ID:** 2503.01227v1

**Link:** [http://arxiv.org/abs/2503.01227v1](http://arxiv.org/abs/2503.01227v1)

**Summary:** In recent years, pre-trained graph neural networks (GNNs) have been developed
as general models which can be effectively fine-tuned for various potential
downstream tasks in materials science, and have shown significant improvements
in accuracy and data efficiency. The most widely used pre-training methods
currently involve either supervised training to fit a general force field or
self-supervised training by denoising atomic structures equilibrium. Both
methods require datasets generated from quantum mechanical calculations, which
quickly become intractable when scaling to larger datasets. Here we propose a
novel pre-training objective which instead uses cheaply-computed structural
fingerprints as targets while maintaining comparable performance across a range
of different structural descriptors. Our experiments show this approach can act
as a general strategy for pre-training GNNs with application towards large
scale foundational models for atomistic data....

---

### 85. Multi-objective optimization for targeted self-assembly among competing polymorphs

**Authors:** Sambarta Chatterjee, William M. Jacobs

**Published:** 2024-01-20

**Category:** cond-mat.soft

**ID:** 2401.11234v3

**Link:** [http://arxiv.org/abs/2401.11234v3](http://arxiv.org/abs/2401.11234v3)

**Summary:** Most approaches for designing self-assembled materials focus on the
thermodynamic stability of a target structure or crystal polymorph. Yet in
practice, the outcome of a self-assembly process is often controlled by kinetic
pathways. Here we present an efficient machine learning-guided design algorithm
to identify globally optimal interaction potentials that maximize both the
thermodynamic yield and kinetic accessibility of a target polymorph. We show
that optimal potentials exist along a Pareto front, indicating the possibility
of a trade-off between the thermodynamic and kinetic objectives. Although the
extent of this trade-off depends on the target polymorph and the assembly
conditions, we generically find that the trade-off arises from a competition
among alternative polymorphs: The most kinetically optimal potentials, which
favor the target polymorph on short timescales, tend to stabilize a competing
polymorph at longer times. Our work establishes a general-purpose approach for
multi-objective self-assembly optimization, reveals fundamental trade-offs
between crystallization speed and defect formation in the presence of competing
polymorphs, and suggests guiding principles for materials design algorithms
that optimize for kinetic accessibility....

---

### 86. Large Language Models Are Innate Crystal Structure Generators

**Authors:** Jingru Gan, Peichen Zhong, Yuanqi Du, Yanqiao Zhu, Chenru Duan, Haorui Wang, Carla P. Gomes, Kristin A. Persson, Daniel Schwalbe-Koda, Wei Wang

**Published:** 2025-02-28

**Category:** cond-mat.mtrl-sci

**ID:** 2502.20933v1

**Link:** [http://arxiv.org/abs/2502.20933v1](http://arxiv.org/abs/2502.20933v1)

**Summary:** Crystal structure generation is fundamental to materials discovery, enabling
the prediction of novel materials with desired properties. While existing
approaches leverage Large Language Models (LLMs) through extensive fine-tuning
on materials databases, we show that pre-trained LLMs can inherently generate
stable crystal structures without additional training. Our novel framework
MatLLMSearch integrates pre-trained LLMs with evolutionary search algorithms,
achieving a 78.38% metastable rate validated by machine learning interatomic
potentials and 31.7% DFT-verified stability via quantum mechanical
calculations, outperforming specialized models such as CrystalTextLLM. Beyond
crystal structure generation, we further demonstrate that our framework can be
readily adapted to diverse materials design tasks, including crystal structure
prediction and multi-objective optimization of properties such as deformation
energy and bulk modulus, all without fine-tuning. These results establish
pre-trained LLMs as versatile and effective tools for materials discovery,
opening up new venues for crystal structure generation with reduced
computational overhead and broader accessibility....

---

### 87. NExT-Mol: 3D Diffusion Meets 1D Language Modeling for 3D Molecule Generation

**Authors:** Zhiyuan Liu, Yanchen Luo, Han Huang, Enzhi Zhang, Sihang Li, Junfeng Fang, Yaorui Shi, Xiang Wang, Kenji Kawaguchi, Tat-Seng Chua

**Published:** 2025-02-18

**Category:** q-bio.QM

**ID:** 2502.12638v2

**Link:** [http://arxiv.org/abs/2502.12638v2](http://arxiv.org/abs/2502.12638v2)

**Summary:** 3D molecule generation is crucial for drug discovery and material design.
While prior efforts focus on 3D diffusion models for their benefits in modeling
continuous 3D conformers, they overlook the advantages of 1D SELFIES-based
Language Models (LMs), which can generate 100% valid molecules and leverage the
billion-scale 1D molecule datasets. To combine these advantages for 3D molecule
generation, we propose a foundation model -- NExT-Mol: 3D Diffusion Meets 1D
Language Modeling for 3D Molecule Generation. NExT-Mol uses an extensively
pretrained molecule LM for 1D molecule generation, and subsequently predicts
the generated molecule's 3D conformers with a 3D diffusion model. We enhance
NExT-Mol's performance by scaling up the LM's model size, refining the
diffusion neural architecture, and applying 1D to 3D transfer learning.
Notably, our 1D molecule LM significantly outperforms baselines in
distributional similarity while ensuring validity, and our 3D diffusion model
achieves leading performances in conformer prediction. Given these improvements
in 1D and 3D modeling, NExT-Mol achieves a 26% relative improvement in 3D FCD
for de novo 3D generation on GEOM-DRUGS, and a 13% average relative gain for
conditional 3D generation on QM9-2014. Our codes and pretrained checkpoints are
available at https://github.com/acharkq/NExT-Mol....

---

### 88. Agentic Mixture-of-Workflows for Multi-Modal Chemical Search

**Authors:** Tiffany J. Callahan, Nathaniel H. Park, Sara Capponi

**Published:** 2025-02-26

**Category:** cs.AI

**ID:** 2502.19629v1

**Link:** [http://arxiv.org/abs/2502.19629v1](http://arxiv.org/abs/2502.19629v1)

**Summary:** The vast and complex materials design space demands innovative strategies to
integrate multidisciplinary scientific knowledge and optimize materials
discovery. While large language models (LLMs) have demonstrated promising
reasoning and automation capabilities across various domains, their application
in materials science remains limited due to a lack of benchmarking standards
and practical implementation frameworks. To address these challenges, we
introduce Mixture-of-Workflows for Self-Corrective Retrieval-Augmented
Generation (CRAG-MoW) - a novel paradigm that orchestrates multiple agentic
workflows employing distinct CRAG strategies using open-source LLMs. Unlike
prior approaches, CRAG-MoW synthesizes diverse outputs through an orchestration
agent, enabling direct evaluation of multiple LLMs across the same problem
domain. We benchmark CRAG-MoWs across small molecules, polymers, and chemical
reactions, as well as multi-modal nuclear magnetic resonance (NMR) spectral
retrieval. Our results demonstrate that CRAG-MoWs achieve performance
comparable to GPT-4o while being preferred more frequently in comparative
evaluations, highlighting the advantage of structured retrieval and multi-agent
synthesis. By revealing performance variations across data types, CRAG-MoW
provides a scalable, interpretable, and benchmark-driven approach to optimizing
AI architectures for materials discovery. These insights are pivotal in
addressing fundamental gaps in benchmarking LLMs and autonomous AI agents for
scientific applications....

---

### 89. Inverse Materials Design by Large Language Model-Assisted Generative Framework

**Authors:** Yun Hao, Che Fan, Beilin Ye, Wenhao Lu, Zhen Lu, Peilin Zhao, Zhifeng Gao, Qingyao Wu, Yanhui Liu, Tongqi Wen

**Published:** 2025-02-25

**Category:** cond-mat.mtrl-sci

**ID:** 2502.18127v1

**Link:** [http://arxiv.org/abs/2502.18127v1](http://arxiv.org/abs/2502.18127v1)

**Summary:** Deep generative models hold great promise for inverse materials design, yet
their efficiency and accuracy remain constrained by data scarcity and model
architecture. Here, we introduce AlloyGAN, a closed-loop framework that
integrates Large Language Model (LLM)-assisted text mining with Conditional
Generative Adversarial Networks (CGANs) to enhance data diversity and improve
inverse design. Taking alloy discovery as a case study, AlloyGAN systematically
refines material candidates through iterative screening and experimental
validation. For metallic glasses, the framework predicts thermodynamic
properties with discrepancies of less than 8% from experiments, demonstrating
its robustness. By bridging generative AI with domain knowledge and validation
workflows, AlloyGAN offers a scalable approach to accelerate the discovery of
materials with tailored properties, paving the way for broader applications in
materials science....

---

### 90. Active Learning for Conditional Inverse Design with Crystal Generation and Foundation Atomic Models

**Authors:** Zhuoyuan Li, Siyu Liu, Beilin Ye, David J. Srolovitz, Tongqi Wen

**Published:** 2025-02-24

**Category:** cond-mat.mtrl-sci

**ID:** 2502.16984v1

**Link:** [http://arxiv.org/abs/2502.16984v1](http://arxiv.org/abs/2502.16984v1)

**Summary:** Artificial intelligence (AI) is transforming materials science, enabling both
theoretical advancements and accelerated materials discovery. Recent progress
in crystal generation models, which design crystal structures for targeted
properties, and foundation atomic models (FAMs), which capture interatomic
interactions across the periodic table, has significantly improved inverse
materials design. However, an efficient integration of these two approaches
remains an open challenge. Here, we present an active learning framework that
combines crystal generation models and foundation atomic models to enhance the
accuracy and efficiency of inverse design. As a case study, we employ Con-CDVAE
to generate candidate crystal structures and MACE-MP-0 FAM as one of the
high-throughput screeners for bulk modulus evaluation. Through iterative active
learning, we demonstrate that Con-CDVAE progressively improves its accuracy in
generating crystals with target properties, highlighting the effectiveness of a
property-driven fine-tuning process. Our framework is general to accommodate
different crystal generation and foundation atomic models, and establishes a
scalable approach for AI-driven materials discovery. By bridging generative
modeling with atomic-scale simulations, this work paves the way for more
accurate and efficient inverse materials design....

---

### 91. Agentic Deep Graph Reasoning Yields Self-Organizing Knowledge Networks

**Authors:** Markus J. Buehler

**Published:** 2025-02-18

**Category:** cs.AI

**ID:** 2502.13025v1

**Link:** [http://arxiv.org/abs/2502.13025v1](http://arxiv.org/abs/2502.13025v1)

**Summary:** We present an agentic, autonomous graph expansion framework that iteratively
structures and refines knowledge in situ. Unlike conventional knowledge graph
construction methods relying on static extraction or single-pass learning, our
approach couples a reasoning-native large language model with a continually
updated graph representation. At each step, the system actively generates new
concepts and relationships, merges them into a global graph, and formulates
subsequent prompts based on its evolving structure. Through this
feedback-driven loop, the model organizes information into a scale-free network
characterized by hub formation, stable modularity, and bridging nodes that link
disparate knowledge clusters. Over hundreds of iterations, new nodes and edges
continue to appear without saturating, while centrality measures and shortest
path distributions evolve to yield increasingly distributed connectivity. Our
analysis reveals emergent patterns, such as the rise of highly connected 'hub'
concepts and the shifting influence of 'bridge' nodes, indicating that agentic,
self-reinforcing graph construction can yield open-ended, coherent knowledge
structures. Applied to materials design problems, we present compositional
reasoning experiments by extracting node-specific and synergy-level principles
to foster genuinely novel knowledge synthesis, yielding cross-domain ideas that
transcend rote summarization and strengthen the framework's potential for
open-ended scientific discovery. We discuss other applications in scientific
discovery and outline future directions for enhancing scalability and
interpretability....

---

### 92. Diffusion Models for Molecules: A Survey of Methods and Tasks

**Authors:** Liang Wang, Chao Song, Zhiyuan Liu, Yu Rong, Qiang Liu, Shu Wu, Liang Wang

**Published:** 2025-02-13

**Category:** cs.LG

**ID:** 2502.09511v1

**Link:** [http://arxiv.org/abs/2502.09511v1](http://arxiv.org/abs/2502.09511v1)

**Summary:** Generative tasks about molecules, including but not limited to molecule
generation, are crucial for drug discovery and material design, and have
consistently attracted significant attention. In recent years, diffusion models
have emerged as an impressive class of deep generative models, sparking
extensive research and leading to numerous studies on their application to
molecular generative tasks. Despite the proliferation of related work, there
remains a notable lack of up-to-date and systematic surveys in this area.
Particularly, due to the diversity of diffusion model formulations, molecular
data modalities, and generative task types, the research landscape is
challenging to navigate, hindering understanding and limiting the area's
growth. To address this, this paper conducts a comprehensive survey of
diffusion model-based molecular generative methods. We systematically review
the research from the perspectives of methodological formulations, data
modalities, and task types, offering a novel taxonomy. This survey aims to
facilitate understanding and further flourishing development in this area. The
relevant papers are summarized at:
https://github.com/AzureLeon1/awesome-molecular-diffusion-models....

---

### 93. On Sequential Fault-Intolerant Process Planning

**Authors:** Andrzej Kaczmarczyk, Davin Choo, Niclas Boehmer, Milind Tambe, Haifeng Xu

**Published:** 2025-02-07

**Category:** cs.AI

**ID:** 2502.04998v1

**Link:** [http://arxiv.org/abs/2502.04998v1](http://arxiv.org/abs/2502.04998v1)

**Summary:** We propose and study a planning problem we call Sequential Fault-Intolerant
Process Planning (SFIPP). SFIPP captures a reward structure common in many
sequential multi-stage decision problems where the planning is deemed
successful only if all stages succeed. Such reward structures are different
from classic additive reward structures and arise in important applications
such as drug/material discovery, security, and quality-critical product design.
We design provably tight online algorithms for settings in which we need to
pick between different actions with unknown success chances at each stage. We
do so both for the foundational case in which the behavior of actions is
deterministic, and the case of probabilistic action outcomes, where we
effectively balance exploration for learning and exploitation for planning
through the usage of multi-armed bandit algorithms. In our empirical
evaluations, we demonstrate that the specialized algorithms we develop, which
leverage additional information about the structure of the SFIPP instance,
outperform our more general algorithm....

---

### 94. FF7: A Code Package for High-throughput Calculations and Constructing Materials Database

**Authors:** Tiancheng Ma, Zihan Zhang, Shuting Wu, Defang Duan, Tian Cui

**Published:** 2025-02-07

**Category:** cond-mat.mtrl-sci

**ID:** 2502.04984v1

**Link:** [http://arxiv.org/abs/2502.04984v1](http://arxiv.org/abs/2502.04984v1)

**Summary:** Decades accumulation of theory simulations lead to boom in material database,
which combined with machine learning methods has been a valuable driver for the
data-intensive material discovery, i.e., the fourth research paradigm. However,
construction of segmented databases and data reuse in generic databases with
uniform parameters still lack easy-to-use code tools. We herein develop a code
package named FF7 (Fast Funnel with 7 modules) to provide command-line based
interactive interface for performing customized high-throughput calculations
and building your own handy databases. Data correlation studies and material
property prediction can progress by built-in installation-free artificial
neural network module and various post processing functions are also supported
by auxiliary module. This paper shows the usage of FF7 code package and
demonstrates its usefulness by example of database driven thermodynamic
stability high-throughput calculation and machine learning model for predicting
the superconducting critical temperature of clathrate hydrides....

---

### 95. Cliqueformer: Model-Based Optimization with Structured Transformers

**Authors:** Jakub Grudzien Kuba, Pieter Abbeel, Sergey Levine

**Published:** 2024-10-17

**Category:** cs.LG

**ID:** 2410.13106v3

**Link:** [http://arxiv.org/abs/2410.13106v3](http://arxiv.org/abs/2410.13106v3)

**Summary:** Large neural networks excel at prediction tasks, but their application to
design problems, such as protein engineering or materials discovery, requires
solving offline model-based optimization (MBO) problems. While predictive
models may not directly translate to effective design, recent MBO algorithms
incorporate reinforcement learning and generative modeling approaches.
Meanwhile, theoretical work suggests that exploiting the target function's
structure can enhance MBO performance. We present Cliqueformer, a
transformer-based architecture that learns the black-box function's structure
through functional graphical models (FGM), addressing distribution shift
without relying on explicit conservative approaches. Across various domains,
including chemical and genetic design tasks, Cliqueformer demonstrates superior
performance compared to existing methods....

---

### 96. AI-driven materials design: a mini-review

**Authors:** Mouyang Cheng, Chu-Liang Fu, Ryotaro Okabe, Abhijatmedhi Chotrattanapituk, Artittaya Boonkird, Nguyen Tuan Hung, Mingda Li

**Published:** 2025-02-05

**Category:** cond-mat.mtrl-sci

**ID:** 2502.02905v1

**Link:** [http://arxiv.org/abs/2502.02905v1](http://arxiv.org/abs/2502.02905v1)

**Summary:** Materials design is an important component of modern science and technology,
yet traditional approaches rely heavily on trial-and-error and can be
inefficient. Computational techniques, enhanced by modern artificial
intelligence (AI), have greatly accelerated the design of new materials. Among
these approaches, inverse design has shown great promise in designing materials
that meet specific property requirements. In this mini-review, we summarize key
computational advancements for materials design over the past few decades. We
follow the evolution of relevant materials design techniques, from
high-throughput forward machine learning (ML) methods and evolutionary
algorithms, to advanced AI strategies like reinforcement learning (RL) and deep
generative models. We highlight the paradigm shift from conventional screening
approaches to inverse generation driven by deep generative models. Finally, we
discuss current challenges and future perspectives of materials inverse design.
This review may serve as a brief guide to the approaches, progress, and outlook
of designing future functional materials with technological relevance....

---

### 97. Emerging Microelectronic Materials by Design: Navigating Combinatorial Design Space with Scarce and Dispersed Data

**Authors:** Hengrui Zhang, Alexandru B. Georgescu, Suraj Yerramilli, Christopher Karpovich, Daniel W. Apley, Elsa A. Olivetti, James M. Rondinelli, Wei Chen

**Published:** 2024-12-23

**Category:** cond-mat.mtrl-sci

**ID:** 2412.17283v2

**Link:** [http://arxiv.org/abs/2412.17283v2](http://arxiv.org/abs/2412.17283v2)

**Summary:** The increasing demands of sustainable energy, electronics, and biomedical
applications call for next-generation functional materials with unprecedented
properties. Of particular interest are emerging materials that display
exceptional physical properties, making them promising candidates in
energy-efficient microelectronic devices. As the conventional Edisonian
approach becomes significantly outpaced by growing societal needs, emerging
computational modeling and machine learning (ML) methods are employed for the
rational design of materials. However, the complex physical mechanisms, cost of
first-principles calculations, and the dispersity and scarcity of data pose
challenges to both physics-based and data-driven materials modeling. Moreover,
the combinatorial composition-structure design space is high-dimensional and
often disjoint, making design optimization nontrivial. In this Account, we
review a team effort toward establishing a framework that integrates
data-driven and physics-based methods to address these challenges and
accelerate materials design. We begin by presenting our integrated materials
design framework and its three components in a general context. We then provide
an example of applying this materials design framework to metal-insulator
transition (MIT) materials, a specific type of emerging materials with
practical importance in next-generation memory technologies. We identify
multiple new materials which may display this property and propose pathways for
their synthesis. Finally, we identify some outstanding challenges in
data-driven materials design, such as materials data quality issues and
property-performance mismatch. We seek to raise awareness of these overlooked
issues hindering materials design, thus stimulating efforts toward developing
methods to mitigate the gaps....

---

### 98. How Can We Engineer Electronic Transitions Through Twisting and Stacking in TMDC Bilayers and Heterostructures? A First-Principles Approach

**Authors:** Yu-Hsiu Lin, William P. Comaskey, Jose L. Mendoza-Cortes

**Published:** 2024-05-09

**Category:** cond-mat.mtrl-sci

**ID:** 2405.06096v2

**Link:** [http://arxiv.org/abs/2405.06096v2](http://arxiv.org/abs/2405.06096v2)

**Summary:** Layered two-dimensional (2D) materials exhibit unique properties, expanding
opportunities in material design. We investigate MX$_2$ transition metal
dichalcogenides (TMDCs) (M = Mo, W; X = S, Se, Te) in homo- and heterobilayers
with different stacking and twist angles. Twisted bilayers introduce Moir\'e
patterns, significantly altering electronic properties. Using first-principles
Density Functional Theory (DFT) with range-separated hybrid functionals, we
examine 30 MX$_2$ combinations, revealing how stacking and composition
influence stability and band gap energy (E$_g$). Notably, the MoTe$_2$/WSe$_2$
heterostructure with a 60\textdegree~shift maintains a direct band gap,
highlighting its potential for applications. Homobilayers under low-strain
conditions exhibit diverse stacking-dependent electronic behaviors, where
MoS$_2$, WS$_2$, and WSe$_2$ transition between direct and indirect band gaps
at specific twist angles. MoS$_2$ can even switch between semiconductor and
metallic states. Critical twist angles (17.9\textdegree, 42.1\textdegree,
77.9\textdegree, and 102.1\textdegree) in twisted WS$_2$ and WSe$_2$ bilayers
yield symmetric Moir\'e patterns with tunable band gaps. Our findings emphasize
that controlling heterostructures and twist angles is a powerful strategy for
engineering electronic properties, offering a pathway for next-generation
materials....

---

### 99. Engineering Point Defects in MoS2 for Tailored Material Properties using Large Language Models

**Authors:** Abdalaziz Al-Maeeni, Denis Derkach, Andrey Ustyuzhanin

**Published:** 2025-01-28

**Category:** cond-mat.mtrl-sci

**ID:** 2501.17279v1

**Link:** [http://arxiv.org/abs/2501.17279v1](http://arxiv.org/abs/2501.17279v1)

**Summary:** The tunability of physical properties in transition metal dichalcogenides
(TMDCs) through point defect engineering offers significant potential for the
development of next-generation optoelectronic and high-tech applications.
Building upon prior work on machine learning-driven material design, this study
focuses on the systematic introduction and manipulation of point defects in
MoS2 to tailor their properties. Leveraging a comprehensive dataset generated
via density functional theory (DFT) calculations, we explore the effects of
various defect types and concentrations on the mate rial characteristics of
TMDCs. Our methodology integrates the use of pre-trained large language models
to generate defect configurations, enabling efficient predictions of
defect-induced property modifications. This research differs from traditional
methods of material generation and discovery by utilizing the latest advances
in transformer model architecture, which have proven to be efficient and
accurate discrete predictors. In contrast to high-throughput methods where
configurations are generated randomly and then screened based on their physical
properties, our approach not only enhances the understanding of defect-property
relationships in TMDCs but also provides a robust framework for designing
materials with bespoke properties. This facilitates the advancement of
materials science and technology....

---

### 100. Foundational Large Language Models for Materials Research

**Authors:** Vaibhav Mishra, Somaditya Singh, Dhruv Ahlawat, Mohd Zaki, Vaibhav Bihani, Hargun Singh Grover, Biswajit Mishra, Santiago Miret, Mausam, N. M. Anoop Krishnan

**Published:** 2024-12-12

**Category:** cond-mat.mtrl-sci

**ID:** 2412.09560v2

**Link:** [http://arxiv.org/abs/2412.09560v2](http://arxiv.org/abs/2412.09560v2)

**Summary:** Materials discovery and development are critical for addressing global
challenges. Yet, the exponential growth in materials science literature
comprising vast amounts of textual data has created significant bottlenecks in
knowledge extraction, synthesis, and scientific reasoning. Large Language
Models (LLMs) offer unprecedented opportunities to accelerate materials
research through automated analysis and prediction. Still, their effective
deployment requires domain-specific adaptation for understanding and solving
domain-relevant tasks. Here, we present LLaMat, a family of foundational models
for materials science developed through continued pretraining of LLaMA models
on an extensive corpus of materials literature and crystallographic data.
Through systematic evaluation, we demonstrate that LLaMat excels in
materials-specific NLP and structured information extraction while maintaining
general linguistic capabilities. The specialized LLaMat-CIF variant
demonstrates unprecedented capabilities in crystal structure generation,
predicting stable crystals with high coverage across the periodic table.
Intriguingly, despite LLaMA-3's superior performance in comparison to LLaMA-2,
we observe that LLaMat-2 demonstrates unexpectedly enhanced domain-specific
performance across diverse materials science tasks, including structured
information extraction from text and tables, more particularly in crystal
structure generation, a potential adaptation rigidity in overtrained LLMs.
Altogether, the present work demonstrates the effectiveness of domain
adaptation towards developing practically deployable LLM copilots for materials
research. Beyond materials science, our findings reveal important
considerations for domain adaptation of LLMs, such as model selection, training
methodology, and domain-specific performance, which may influence the
development of specialized scientific AI systems....

---

### 101. The Impact of Mechanical Strain on Magnetic and Structural Properties of 2D Materials: A Monte Carlo study

**Authors:** Aytac Celik

**Published:** 2025-01-26

**Category:** cond-mat.mtrl-sci

**ID:** 2501.15626v1

**Link:** [http://arxiv.org/abs/2501.15626v1](http://arxiv.org/abs/2501.15626v1)

**Summary:** The inherent flexibility of two dimensional materials allows for efficient
manipulation of their physical properties through strain application, which is
essential for the development of advanced nanoscale devices. This study aimed
to understand the impact of mechanical strain on the magnetic properties of two
dimensional materials using Monte Carlo simulations. The effects of several
strain states on the magnetic properties were investigated using the Lennard
Jones potential and bond length-dependent exchange interactions. The key
parameters analyzed include the Lindemann coefficient, radial distribution
function, and magnetization in relation to temperature and magnetic field. The
results indicate that applying biaxial tensile strain generally reduces the
critical temperature. In contrast, the biaxial compressive strain increased Tc
within the elastic range, but decreased at higher strain levels. Both
compressive and tensile strains significantly influence the ferromagnetic
properties and structural ordering, as evidenced by magnetization hysteresis.
Notably, pure shear strain did not induce disorder, leaving the magnetization
unaffected. In addition, our findings suggest the potential of domain-formation
mechanisms. This study provides comprehensive insights into the influence of
mechanical strain on the magnetic behavior and structural integrity of 2D
materials, offering valuable guidance for future research and advanced material
design applications....

---

### 102. Materials design criteria for ultra-high thermoelectric power factors in metals

**Authors:** Patrizio Graziosi, Kim-Isabelle Mehnert, Rajeev Dutt, Jan-Willem G. Bos, Neophytos Neophytou

**Published:** 2025-01-18

**Category:** cond-mat.mtrl-sci

**ID:** 2501.10790v1

**Link:** [http://arxiv.org/abs/2501.10790v1](http://arxiv.org/abs/2501.10790v1)

**Summary:** Metals have high electronic conductivities, but very low Seebeck
coefficients, which traditionally make them unsuitable for thermoelectric
materials. Recent studies, however, showed that metals can deliver ultra-high
thermoelectric power factors (PFs) under certain conditions. In this work, we
theoretically examine the electronic structure and electronic transport
specifications which allow for such high PFs. Using Boltzmann transport (BTE)
simulations and a multi-band electronic structure model, we show that metals
with: i) high degree of transport asymmetry between their bands, ii) strong
inter-band scattering, and iii) a large degree of band overlap, can provide
ultra-high power factors. We show that each of these characteristics adds to
the steepness of the transport distribution function of the BTE, which allows
for an increase of the Seebeck coefficient to sizable values, simultaneously
with an increase in the electrical conductivity. This work generalizes the
concept that transport asymmetry (i.e., mixture of energy regions of high and
low contributions to the electrical conductivity), through a combination of
different band masses, scattering strengths, or energy filtering scenarios,
etc., can indeed result in very high thermoelectric power factors, even in the
absence of a material bandgap. Under certain conditions, transport asymmetry
can over-compensate any performance degradation to the PF due to bipolar
conduction and the naturally low Seebeck coefficients that otherwise exist in
this class of materials....

---

### 103. In-situ graph reasoning and knowledge expansion using Graph-PReFLexOR

**Authors:** Markus J. Buehler

**Published:** 2025-01-14

**Category:** cs.AI

**ID:** 2501.08120v1

**Link:** [http://arxiv.org/abs/2501.08120v1](http://arxiv.org/abs/2501.08120v1)

**Summary:** The pursuit of automated scientific discovery has fueled progress from
symbolic logic to modern AI, forging new frontiers in reasoning and pattern
recognition. Transformers function as potential systems, where every possible
relationship remains latent potentiality until tasks impose constraints, akin
to measurement. Yet, refining their sampling requires more than probabilistic
selection: solutions must conform to specific structures or rules, ensuring
consistency and the invocation of general principles. We present
Graph-PReFLexOR (Graph-based Preference-based Recursive Language Modeling for
Exploratory Optimization of Reasoning), a framework that combines graph
reasoning with symbolic abstraction to dynamically expand domain knowledge.
Inspired by reinforcement learning, Graph-PReFLexOR defines reasoning as a
structured mapping, where tasks yield knowledge graphs, abstract patterns, and
ultimately, final answers. Inspired by category theory, it encodes concepts as
nodes and their relationships as edges, supporting hierarchical inference and
adaptive learning through isomorphic representations. Demonstrations include
hypothesis generation, materials design, and creative reasoning, such as
discovering relationships between mythological concepts like 'thin places' with
materials science. We propose a 'knowledge garden growth' strategy that
integrates insights across domains, promoting interdisciplinary connections.
Results with a 3-billion-parameter Graph-PReFLexOR model show superior
reasoning depth and adaptability, underscoring the potential for transparent,
multidisciplinary AI-driven discovery. It lays the groundwork for general
autonomous reasoning solutions....

---

### 104. DenseGNN: universal and scalable deeper graph neural networks for high-performance property prediction in crystals and molecules

**Authors:** Hongwei Du, Jiamin Wang, Jian Hui, Lanting Zhang, Hong Wang

**Published:** 2025-01-05

**Category:** cond-mat.mtrl-sci

**ID:** 2501.03278v1

**Link:** [http://arxiv.org/abs/2501.03278v1](http://arxiv.org/abs/2501.03278v1)

**Summary:** Generative models generate vast numbers of hypothetical materials,
necessitating fast, accurate models for property prediction. Graph Neural
Networks (GNNs) excel in this domain but face challenges like high training
costs, domain adaptation issues, and over-smoothing. We introduce DenseGNN,
which employs Dense Connectivity Network (DCN), Hierarchical Node-Edge-Graph
Residual Networks (HRN), and Local Structure Order Parameters Embedding (LOPE)
to address these challenges. DenseGNN achieves state-of-the-art performance on
datasets such as JARVIS-DFT, Materials Project, and QM9, improving the
performance of models like GIN, Schnet, and Hamnet on materials datasets. By
optimizing atomic embeddings and reducing computational costs, DenseGNN enables
deeper architectures and surpasses other GNNs in crystal structure distinction,
approaching X-ray diffraction method accuracy. This advances materials
discovery and design....

---

### 105. Reflections from the 2024 Large Language Model (LLM) Hackathon for Applications in Materials Science and Chemistry

**Authors:** Yoel Zimmermann, Adib Bazgir, Zartashia Afzal, Fariha Agbere, Qianxiang Ai, Nawaf Alampara, Alexander Al-Feghali, Mehrad Ansari, Dmytro Antypov, Amro Aswad, Jiaru Bai, Viktoriia Baibakova, Devi Dutta Biswajeet, Erik Bitzek, Joshua D. Bocarsly, Anna Borisova, Andres M Bran, L. Catherine Brinson, Marcel Moran Calderon, Alessandro Canalicchio, Victor Chen, Yuan Chiang, Defne Circi, Benjamin Charmes, Vikrant Chaudhary, Zizhang Chen, Min-Hsueh Chiu, Judith Clymo, Kedar Dabhadkar, Nathan Daelman, Archit Datar, Wibe A. de Jong, Matthew L. Evans, Maryam Ghazizade Fard, Giuseppe Fisicaro, Abhijeet Sadashiv Gangan, Janine George, Jose D. Cojal Gonzalez, Michael Götte, Ankur K. Gupta, Hassan Harb, Pengyu Hong, Abdelrahman Ibrahim, Ahmed Ilyas, Alishba Imran, Kevin Ishimwe, Ramsey Issa, Kevin Maik Jablonka, Colin Jones, Tyler R. Josephson, Greg Juhasz, Sarthak Kapoor, Rongda Kang, Ghazal Khalighinejad, Sartaaj Khan, Sascha Klawohn, Suneel Kuman, Alvin Noe Ladines, Sarom Leang, Magdalena Lederbauer, Sheng-Lun, Liao, Hao Liu, Xuefeng Liu, Stanley Lo, Sandeep Madireddy, Piyush Ranjan Maharana, Shagun Maheshwari, Soroush Mahjoubi, José A. Márquez, Rob Mills, Trupti Mohanty, Bernadette Mohr, Seyed Mohamad Moosavi, Alexander Moßhammer, Amirhossein D. Naghdi, Aakash Naik, Oleksandr Narykov, Hampus Näsström, Xuan Vu Nguyen, Xinyi Ni, Dana O'Connor, Teslim Olayiwola, Federico Ottomano, Aleyna Beste Ozhan, Sebastian Pagel, Chiku Parida, Jaehee Park, Vraj Patel, Elena Patyukova, Martin Hoffmann Petersen, Luis Pinto, José M. Pizarro, Dieter Plessers, Tapashree Pradhan, Utkarsh Pratiush, Charishma Puli, Andrew Qin, Mahyar Rajabi, Francesco Ricci, Elliot Risch, Martiño Ríos-García, Aritra Roy, Tehseen Rug, Hasan M Sayeed, Markus Scheidgen, Mara Schilling-Wilhelmi, Marcel Schloz, Fabian Schöppach, Julia Schumann, Philippe Schwaller, Marcus Schwarting, Samiha Sharlin, Kevin Shen, Jiale Shi, Pradip Si, Jennifer D'Souza, Taylor Sparks, Suraj Sudhakar, Leopold Talirz, Dandan Tang, Olga Taran, Carla Terboven, Mark Tropin, Anastasiia Tsymbal, Katharina Ueltzen, Pablo Andres Unzueta, Archit Vasan, Tirtha Vinchurkar, Trung Vo, Gabriel Vogel, Christoph Völker, Jan Weinreich, Faradawn Yang, Mohd Zaki, Chi Zhang, Sylvester Zhang, Weijie Zhang, Ruijie Zhu, Shang Zhu, Jan Janssen, Calvin Li, Ian Foster, Ben Blaiszik

**Published:** 2024-11-20

**Category:** cs.LG

**ID:** 2411.15221v2

**Link:** [http://arxiv.org/abs/2411.15221v2](http://arxiv.org/abs/2411.15221v2)

**Summary:** Here, we present the outcomes from the second Large Language Model (LLM)
Hackathon for Applications in Materials Science and Chemistry, which engaged
participants across global hybrid locations, resulting in 34 team submissions.
The submissions spanned seven key application areas and demonstrated the
diverse utility of LLMs for applications in (1) molecular and material property
prediction; (2) molecular and material design; (3) automation and novel
interfaces; (4) scientific communication and education; (5) research data
management and automation; (6) hypothesis generation and evaluation; and (7)
knowledge extraction and reasoning from scientific literature. Each team
submission is presented in a summary table with links to the code and as brief
papers in the appendix. Beyond team results, we discuss the hackathon event and
its hybrid format, which included physical hubs in Toronto, Montreal, San
Francisco, Berlin, Lausanne, and Tokyo, alongside a global online hub to enable
local and virtual collaboration. Overall, the event highlighted significant
improvements in LLM capabilities since the previous year's hackathon,
suggesting continued expansion of LLMs for applications in materials science
and chemistry research. These outcomes demonstrate the dual utility of LLMs as
both multipurpose models for diverse machine learning tasks and platforms for
rapid prototyping custom applications in scientific research....

---

### 106. Genetic-guided GFlowNets for Sample Efficient Molecular Optimization

**Authors:** Hyeonah Kim, Minsu Kim, Sanghyeok Choi, Jinkyoo Park

**Published:** 2024-02-05

**Category:** q-bio.BM

**ID:** 2402.05961v4

**Link:** [http://arxiv.org/abs/2402.05961v4](http://arxiv.org/abs/2402.05961v4)

**Summary:** The challenge of discovering new molecules with desired properties is crucial
in domains like drug discovery and material design. Recent advances in deep
learning-based generative methods have shown promise but face the issue of
sample efficiency due to the computational expense of evaluating the reward
function. This paper proposes a novel algorithm for sample-efficient molecular
optimization by distilling a powerful genetic algorithm into deep generative
policy using GFlowNets training, the off-policy method for amortized inference.
This approach enables the deep generative policy to learn from domain
knowledge, which has been explicitly integrated into the genetic algorithm. Our
method achieves state-of-the-art performance in the official molecular
optimization benchmark, significantly outperforming previous methods. It also
demonstrates effectiveness in designing inhibitors against SARS-CoV-2 with
substantially fewer reward calls....

---

### 107. Discovery of 2D Materials via Symmetry-Constrained Diffusion Model

**Authors:** Shihang Xu, Shibing Chu, Rami Mrad, Zhejun Zhang, Zhelin Li, Runxian Jiao, Yuanping Chen

**Published:** 2024-12-24

**Category:** cond-mat.mtrl-sci

**ID:** 2412.18414v1

**Link:** [http://arxiv.org/abs/2412.18414v1](http://arxiv.org/abs/2412.18414v1)

**Summary:** Generative model for 2D materials has shown significant promise in
accelerating the material discovery process. The stability and performance of
these materials are strongly influenced by their underlying symmetry. However,
existing generative models for 2D materials often neglect symmetry constraints,
which limits both the diversity and quality of the generated structures. Here,
we introduce a symmetry-constrained diffusion model (SCDM) that integrates
space group symmetry into the generative process. By incorporating Wyckoff
positions, the model ensures adherence to symmetry principles, leading to the
generation of 2,000 candidate structures. DFT calculations were conducted to
evaluate the convex hull energies of these structures after structural
relaxation. From the generated samples, 843 materials that met the energy
stability criteria (Ehull < 0.6 eV/atom) were identified. Among these, six
candidates were selected for further stability analysis, including phonon band
structure evaluations and electronic properties investigations, all of which
exhibited phonon spectrum stability. To benchmark the performance of SCDM, a
symmetry-unconstrained diffusion model was also evaluated via crystal structure
prediction model. The results highlight that incorporating symmetry constraints
enhances the effectiveness of generated 2D materials, making a contribution to
the discovery of 2D materials through generative modeling....

---

### 108. Electron-Induced Radiation Chemistry in Environmental Transmission Electron Microscopy

**Authors:** Kunmo Koo, Nikhil S. Chellam, Sangyoon Shim, Chad A. Mirkin, George C. Schatz, Xiaobing Hu, Vinayak P. Dravid

**Published:** 2024-02-27

**Category:** cond-mat.mtrl-sci

**ID:** 2402.17928v3

**Link:** [http://arxiv.org/abs/2402.17928v3](http://arxiv.org/abs/2402.17928v3)

**Summary:** Environmental transmission electron microscopy (E-TEM) enables direct
observation of nanoscale chemical processes crucial for catalysis and materials
design. However, the high-energy electron probe can dramatically alter reaction
pathways through radiolysis - the dissociation of molecules under electron beam
irradiation. While extensively studied in liquid-cell TEM, the impact of
radiolysis in gas-phase reactions remains unexplored. Here, we present a
numerical model elucidating radiation chemistry in both gas and liquid E-TEM
environments. Our findings reveal that while gas-phase E-TEM generates
radiolytic species with lower reactivity than liquid-phase systems, these
species can accumulate to reaction-altering concentrations, particularly at
elevated pressures. We validate our model through two case studies: the
radiation-promoted oxidation of aluminum nanocubes and disproportionation of
carbon monoxide. In both cases, increasing the electron beam dose rate directly
accelerates their reaction kinetics, as demonstrated by enhanced AlOx growth
and carbon deposition. Based on these insights, we establish practical
guidelines for controlling radiolysis in closed-cell nanoreactors. This work
not only resolves a fundamental challenge in electron microscopy but also
advances our ability to rationally design materials with sub-Angstrom
resolution....

---

### 109. A Decision Transformer Approach to Grain Boundary Network Optimization

**Authors:** Christopher W. Adair, Oliver K. Johnson

**Published:** 2024-12-19

**Category:** cond-mat.mtrl-sci

**ID:** 2412.15393v1

**Link:** [http://arxiv.org/abs/2412.15393v1](http://arxiv.org/abs/2412.15393v1)

**Summary:** As microstructure property models improve, additional information from
crystallographic degrees of freedom and grain boundary networks (GBNs) can be
included in microstructure design problems. However, the high dimensional
nature of including this information precludes the use of many common
optimization approaches and requires less efficient methods to generate quality
designs. Previous work demonstrated that human-in-the-loop optimization,
instantiated as a video game, achieved high-quality, efficient solutions to
these design problems. However, such data is expensive to obtain. In the
present work, we show how a Decision Transformer machine learning (ML) model
can be used to learn from the optimization trajectories generated by human
players, and subsequently solve materials design problems. We compare the ML
optimization trajectories against players and a common global optimization
algorithm: simulated annealing (SA). We find that the ML model exhibits a
validation accuracy of 84% against player decisions, and achieves solutions of
comparable quality to SA (92%), but does so using three orders of magnitude
fewer iterations. We find that the ML model generalizes in important and
surprising ways, including the ability to train using a simple constitutive
structure-property model and then solve microstructure design problems for a
different, higher-fidelity, constitutive structure-property model without any
retraining. These results demonstrate the potential of Decision Transformer
models for the solution of materials design problems....

---

### 110. Superionic Ionic Conductor Discovery via Multiscale Topological Learning

**Authors:** Dong Chen, Bingxu Wang, Shunning Li, Wentao Zhang, Kai Yang, Yongli Song, Guo-Wei Wei, Feng Pan

**Published:** 2024-12-16

**Category:** cond-mat.mtrl-sci

**ID:** 2412.11398v1

**Link:** [http://arxiv.org/abs/2412.11398v1](http://arxiv.org/abs/2412.11398v1)

**Summary:** Lithium superionic conductors (LSICs) are crucial for next-generation
solid-state batteries, offering exceptional ionic conductivity and enhanced
safety for renewable energy and electric vehicles. However, their discovery is
extremely challenging due to the vast chemical space, limited labeled data, and
the understanding of complex structure-function relationships required for
optimizing ion transport. This study introduces a multiscale topological
learning (MTL) framework, integrating algebraic topology and unsupervised
learning to tackle these challenges efficiently. By modeling lithium-only and
lithium-free substructures, the framework extracts multiscale topological
features and introduces two topological screening metrics-cycle density and
minimum connectivity distance-to ensure structural connectivity and ion
diffusion compatibility. Promising candidates are clustered via unsupervised
algorithms to identify those resembling known superionic conductors. For final
refinement, candidates that pass chemical screening undergo ab initio molecular
dynamics simulations for validation. This approach led to the discovery of 14
novel LSICs, four of which have been independently validated in recent
experiments. This success accelerates the identification of LSICs and
demonstrates broad adaptability, offering a scalable tool for addressing
complex materials discovery challenges....

---

### 111. Leveraging Chemistry Foundation Models to Facilitate Structure Focused Retrieval Augmented Generation in Multi-Agent Workflows for Catalyst and Materials Design

**Authors:** Nathaniel H. Park, Tiffany J. Callahan, James L. Hedrick, Tim Erdmann, Sara Capponi

**Published:** 2024-08-21

**Category:** cs.AI

**ID:** 2408.11793v2

**Link:** [http://arxiv.org/abs/2408.11793v2](http://arxiv.org/abs/2408.11793v2)

**Summary:** Molecular property prediction and generative design via deep learning models
has been the subject of intense research given its potential to accelerate
development of new, high-performance materials. More recently, these workflows
have been significantly augmented with the advent of large language models
(LLMs) and systems of autonomous agents capable of utilizing pre-trained models
to make predictions in the context of more complex research tasks. While
effective, there is still room for substantial improvement within agentic
systems on the retrieval of salient information for material design tasks.
Within this context, alternative uses of predictive deep learning models, such
as leveraging their latent representations to facilitate cross-modal retrieval
augmented generation within agentic systems for task-specific materials design,
has remained unexplored. Herein, we demonstrate that large, pre-trained
chemistry foundation models can serve as a basis for enabling
structure-focused, semantic chemistry information retrieval for both
small-molecules, complex polymeric materials, and reactions. Additionally, we
show the use of chemistry foundation models in conjunction with multi-modal
models such as OpenCLIP facilitate unprecedented queries and information
retrieval across multiple characterization data domains. Finally, we
demonstrate the integration of these models within multi-agent systems to
facilitate structure and topological-based natural language queries and
information retrieval for different research tasks....

---

### 112. Three-Dimensional Construction of Hyperuniform, Nonhyperuniform and Antihyperuniform Random Media via Spectral Density Functions and Their Transport Properties

**Authors:** Wenlong Shi, Yang Jiao, Salvatore Torquato

**Published:** 2024-12-12

**Category:** cond-mat.mtrl-sci

**ID:** 2412.08974v1

**Link:** [http://arxiv.org/abs/2412.08974v1](http://arxiv.org/abs/2412.08974v1)

**Summary:** Rigorous theories connecting physical properties of a heterogeneous material
to its microstructure offer a promising avenue to guide the computational
material design and optimization. We present here an efficient Fourier-space
based computational framework and employ a variety of analytical ${\tilde
\chi}_{_V}({k})$ functions that satisfy all known necessary conditions to
construct 3D disordered stealthy hyperuniform, standard hyperuniform,
nonhyperuniform, and antihyperuniform two-phase heterogeneous material systems
at varying phase volume fractions. We show that a rich spectrum of distinct
structures within each of the above classes of materials can be generated by
tuning correlations in the system across length scales. We present the first
realization of antihyperuniform two-phase heterogeneous materials in 3D, which
are characterized by a power-law autocovariance function $\chi_{_V}(r)$ and
contain clusters of dramatically different sizes and morphologies. We also
determine the diffusion spreadability ${\cal S}(t)$ and estimate the fluid
permeability $k$ associated with all of the constructed materials directly from
the corresponding ${\tilde \chi}_{_V}({k})$ functions. We find that varying the
length-scale parameter within each class of ${\tilde \chi}_{_V}({k})$ functions
can also lead to orders of magnitude variation of ${\cal S}(t)$ at intermediate
and long time scales. Moreover, we find that increasing solid volume fraction
$\phi_1$ and correlation length $a$ in the constructed media generally leads to
a decrease in the dimensionless fluid permeability $k/a^2$. These results
indicate the feasibility of employing parameterized ${\tilde \chi}_{_V}({k})$
for designing composites with targeted transport properties....

---

### 113. Fundamental Microscopic Properties as Predictors of Large-Scale Quantities of Interest: Validation through Grain Boundary Energy Trends

**Authors:** Benjamin A. Jasperson, Ilia Nikiforov, Amit Samanta, Brandon Runnels, Harley T. Johnson, Ellad B. Tadmor

**Published:** 2024-11-25

**Category:** cond-mat.mtrl-sci

**ID:** 2411.16770v2

**Link:** [http://arxiv.org/abs/2411.16770v2](http://arxiv.org/abs/2411.16770v2)

**Summary:** Correlations between fundamental microscopic properties computable from first
principles, which we term canonical properties, and complex large-scale
quantities of interest (QoIs) provide an avenue to predictive materials
discovery. We propose that such correlations can be efficiently discovered
through simulations utilizing approximate interatomic potentials (IPs), which
serve as an ensemble of "synthetic materials." As a proof of principle we build
a regression model relating canonical properties to the symmetric tilt grain
boundary (GB) energy curves in face-centered cubic crystals, characterized by
the scaling factor in the universal lattice matching model of Runnels et al.
(2016), which we take to be our QoI. Our analysis recovers known correlations
of GB energy to other properties and discovers new ones. We also demonstrate,
using available density functional theory (DFT) GB energy data, that the
regression model constructed from IP data is consistent with DFT results,
confirming the assumption that the IPs and DFT belong to same statistical pool
and thereby validating the approach. Regression models constructed in this
fashion can be used to predict large-scale QoIs based on first-principles data
and provide a general method for training IPs for QoIs beyond the scope of
first-principles calculations....

---

### 114. Accelerating Manufacturing Scale-Up from Material Discovery Using Agentic Web Navigation and Retrieval-Augmented AI for Process Engineering Schematics Design

**Authors:** Sakhinana Sagar Srinivas, Akash Das, Shivam Gupta, Venkataramana Runkana

**Published:** 2024-12-08

**Category:** cs.LG

**ID:** 2412.05937v1

**Link:** [http://arxiv.org/abs/2412.05937v1](http://arxiv.org/abs/2412.05937v1)

**Summary:** Process Flow Diagrams (PFDs) and Process and Instrumentation Diagrams (PIDs)
are critical tools for industrial process design, control, and safety. However,
the generation of precise and regulation-compliant diagrams remains a
significant challenge, particularly in scaling breakthroughs from material
discovery to industrial production in an era of automation and digitalization.
This paper introduces an autonomous agentic framework to address these
challenges through a twostage approach involving knowledge acquisition and
generation. The framework integrates specialized sub-agents for retrieving and
synthesizing multimodal data from publicly available online sources and
constructs ontological knowledge graphs using a Graph Retrieval-Augmented
Generation (Graph RAG) paradigm. These capabilities enable the automation of
diagram generation and open-domain question answering (ODQA) tasks with high
contextual accuracy. Extensive empirical experiments demonstrate the frameworks
ability to deliver regulation-compliant diagrams with minimal expert
intervention, highlighting its practical utility for industrial applications....

---

### 115. Transfer Learning for Deep Learning-based Prediction of Lattice Thermal Conductivity

**Authors:** L. Klochko, M. d'Aquin, A. Togo, L. Chaput

**Published:** 2024-11-27

**Category:** cs.LG

**ID:** 2411.18259v1

**Link:** [http://arxiv.org/abs/2411.18259v1](http://arxiv.org/abs/2411.18259v1)

**Summary:** Machine learning promises to accelerate the material discovery by enabling
high-throughput prediction of desirable macro-properties from atomic-level
descriptors or structures. However, the limited data available about precise
values of these properties have been a barrier, leading to predictive models
with limited precision or the ability to generalize. This is particularly true
of lattice thermal conductivity (LTC): existing datasets of precise (ab initio,
DFT-based) computed values are limited to a few dozen materials with little
variability. Based on such datasets, we study the impact of transfer learning
on both the precision and generalizability of a deep learning model
(ParAIsite). We start from an existing model (MEGNet~\cite{Chen2019}) and show
that improvements are obtained by fine-tuning a pre-trained version on
different tasks. Interestingly, we also show that a much greater improvement is
obtained when first fine-tuning it on a large datasets of low-quality
approximations of LTC (based on the AGL model) and then applying a second phase
of fine-tuning with our high-quality, smaller-scale datasets. The promising
results obtained pave the way not only towards a greater ability to explore
large databases in search of low thermal conductivity materials but also to
methods enabling increasingly precise predictions in areas where quality data
are rare....

---

### 116. A Multi-agent Framework for Materials Laws Discovery

**Authors:** Bo Hu, Siyu Liu, Beilin Ye, Yun Hao, Tongqi Wen

**Published:** 2024-11-25

**Category:** cond-mat.mtrl-sci

**ID:** 2411.16416v1

**Link:** [http://arxiv.org/abs/2411.16416v1](http://arxiv.org/abs/2411.16416v1)

**Summary:** Uncovering the underlying laws governing correlations between different
materials properties, and the structure-composition-property relationship, is
essential for advancing materials theory and enabling efficient materials
design. With recent advances in artificial intelligence (AI), particularly in
large language models (LLMs), symbolic regression has emerged as a powerful
method for deriving explicit formulas for materials laws. LLMs, with their
pre-trained, cross-disciplinary knowledge, present a promising direction in "AI
for Materials". In this work, we introduce a multi-agent framework based on
LLMs specifically designed for symbolic regression in materials science. We
demonstrate the effectiveness of the framework using the glass-forming ability
(GFA) of metallic glasses as a case study, employing three characteristic
temperatures as independent variables. Our framework derived an interpretable
formula to describe GFA, achieving a correlation coefficient of up to 0.948
with low formula complexity. This approach outperforms standard packages such
as GPlearn and demonstrates a ~30% improvement over random generation methods,
owing to integrated memory and reflection mechanisms. The proposed framework
can be extended to discover laws in various materials applications, supporting
new materials design and enhancing the interpretation of experimental and
simulation data....

---

### 117. Accelerating CALPHAD-based Phase Diagram Predictions in Complex Alloys Using Universal Machine Learning Potentials: Opportunities and Challenges

**Authors:** Siya Zhu, Raymundo Arróyave, Doğuhan Sarıtürk

**Published:** 2024-11-22

**Category:** cond-mat.mtrl-sci

**ID:** 2411.15351v1

**Link:** [http://arxiv.org/abs/2411.15351v1](http://arxiv.org/abs/2411.15351v1)

**Summary:** Accurate phase diagram prediction is crucial for understanding alloy
thermodynamics and advancing materials design. While traditional CALPHAD
methods are robust, they are resource-intensive and limited by experimentally
assessed data. This work explores the use of machine learning interatomic
potentials (MLIPs) such as M3GNet, CHGNet, MACE, SevenNet, and ORB to
significantly accelerate phase diagram calculations by using the Alloy
Theoretic Automated Toolkit (ATAT) to map calculations of the energies and free
energies of atomistic systems to CALPHAD-compatible thermodynamic descriptions.
Using case studies including Cr-Mo, Cu-Au, and Pt-W, we demonstrate that MLIPs,
particularly ORB, achieve computational speedups exceeding three orders of
magnitude compared to DFT while maintaining phase stability predictions within
acceptable accuracy. Extending this approach to liquid phases and ternary
systems like Cr-Mo-V highlights its versatility for high-entropy alloys and
complex chemical spaces. This work demonstrates that MLIPs, integrated with
tools like ATAT within a CALPHAD framework, provide an efficient and accurate
framework for high-throughput thermodynamic modeling, enabling rapid
exploration of novel alloy systems. While many challenges remain to be
addressed, the accuracy of some of these MLIPs (ORB in particular) are on the
verge of paving the way toward high-throughput generation of CALPHAD
thermodynamic descriptions of multi-component, multi-phase alloy systems....

---

### 118. Accelerating active learning materials discovery with FAIR data and workflows: a case study for alloy melting temperatures

**Authors:** Mohnish Harwani, Juan C. Verduzco, Brian H. Lee, Alejandro Strachan

**Published:** 2024-11-20

**Category:** cond-mat.mtrl-sci

**ID:** 2411.13689v1

**Link:** [http://arxiv.org/abs/2411.13689v1](http://arxiv.org/abs/2411.13689v1)

**Summary:** Active learning (AL) is a powerful sequential optimization approach that has
shown great promise in the discovery of new materials. However, a major
challenge remains the acquisition of the initial data and the development of
workflows to generate new data at each iteration. In this study, we demonstrate
a significant speedup in an optimization task by reusing a published simulation
workflow available for online simulations and its associated data repository,
where the results of each workflow run are automatically stored. Both the
workflow and its data follow FAIR (findable, accessible, interoperable, and
reusable) principles using nanoHUB's infrastructure. The workflow employs
molecular dynamics to calculate the melting temperature of multi-principal
component alloys. We leveraged all prior data not only to develop an accurate
machine learning model to start the sequential optimization but also to
optimize the simulation parameters and accelerate convergence. Prior work
showed that finding the alloy composition with the highest melting temperature
required testing 15 alloy compositions, and establishing the melting
temperature for each composition took, on average, 4 simulations. By developing
a workflow that utilizes the FAIR data in the nanoHUB database, we reduced the
number of simulations per composition to one and found the alloy with the
lowest melting temperature testing only three compositions. This second
optimization, therefore, shows a speedup of 10x as compared to models that do
not access the FAIR databases....

---

### 119. Graph neural network framework for energy mapping of hybrid monte-carlo molecular dynamics simulations of Medium Entropy Alloys

**Authors:** Mashaekh Tausif Ehsan, Saifuddin Zafar, Apurba Sarker, Sourav Das Suvro, Mohammad Nasim Hasan

**Published:** 2024-11-20

**Category:** cond-mat.mtrl-sci

**ID:** 2411.13670v1

**Link:** [http://arxiv.org/abs/2411.13670v1](http://arxiv.org/abs/2411.13670v1)

**Summary:** Machine learning (ML) methods have drawn significant interest in material
design and discovery. Graph neural networks (GNNs), in particular, have
demonstrated strong potential for predicting material properties. The present
study proposes a graph-based representation for modeling medium-entropy alloys
(MEAs). Hybrid Monte-Carlo molecular dynamics (MC/MD) simulations are employed
to achieve thermally stable structures across various annealing temperatures in
an MEA. These simulations generate dump files and potential energy labels,
which are used to construct graph representations of the atomic configurations.
Edges are created between each atom and its 12 nearest neighbors without
incorporating explicit edge features. These graphs then serve as input for a
Graph Convolutional Neural Network (GCNN) based ML model to predict the
system's potential energy. The GCNN architecture effectively captures the local
environment and chemical ordering within the MEA structure. The GCNN-based ML
model demonstrates strong performance in predicting potential energy at
different steps, showing satisfactory results on both the training data and
unseen configurations. Our approach presents a graph-based modeling framework
for MEAs and high-entropy alloys (HEAs), which effectively captures the local
chemical order (LCO) within the alloy structure. This allows us to predict key
material properties influenced by LCO in both MEAs and HEAs, providing deeper
insights into how atomic-scale arrangements affect the properties of these
alloys....

---

### 120. Vertical Validation: Evaluating Implicit Generative Models for Graphs on Thin Support Regions

**Authors:** Mai Elkady, Thu Bui, Bruno Ribeiro, David I. Inouye

**Published:** 2024-11-20

**Category:** cs.LG

**ID:** 2411.13358v1

**Link:** [http://arxiv.org/abs/2411.13358v1](http://arxiv.org/abs/2411.13358v1)

**Summary:** There has been a growing excitement that implicit graph generative models
could be used to design or discover new molecules for medicine or material
design. Because these molecules have not been discovered, they naturally lie in
unexplored or scarcely supported regions of the distribution of known
molecules. However, prior evaluation methods for implicit graph generative
models have focused on validating statistics computed from the thick support
(e.g., mean and variance of a graph property). Therefore, there is a mismatch
between the goal of generating novel graphs and the evaluation methods. To
address this evaluation gap, we design a novel evaluation method called
Vertical Validation (VV) that systematically creates thin support regions
during the train-test splitting procedure and then reweights generated samples
so that they can be compared to the held-out test data. This procedure can be
seen as a generalization of the standard train-test procedure except that the
splits are dependent on sample features. We demonstrate that our method can be
used to perform model selection if performance on thin support regions is the
desired goal. As a side benefit, we also show that our approach can better
detect overfitting as exemplified by memorization....

---

### 121. Large Language Models for Material Property Predictions: elastic constant tensor prediction and materials design

**Authors:** Siyu Liu, Tongqi Wen, Beilin Ye, Zhuoyuan Li, David J. Srolovitz

**Published:** 2024-11-19

**Category:** cond-mat.mtrl-sci

**ID:** 2411.12280v1

**Link:** [http://arxiv.org/abs/2411.12280v1](http://arxiv.org/abs/2411.12280v1)

**Summary:** Efficient and accurate prediction of material properties is critical for
advancing materials design and applications. The rapid-evolution of large
language models (LLMs) presents a new opportunity for material property
predictions, complementing experimental measurements and multi-scale
computational methods. We focus on predicting the elastic constant tensor, as a
case study, and develop domain-specific LLMs for predicting elastic constants
and for materials discovery. The proposed ElaTBot LLM enables simultaneous
prediction of elastic constant tensors, bulk modulus at finite temperatures,
and the generation of new materials with targeted properties. Moreover, the
capabilities of ElaTBot are further enhanced by integrating with general LLMs
(GPT-4o) and Retrieval-Augmented Generation (RAG) for prediction. A specialized
variant, ElaTBot-DFT, designed for 0 K elastic constant tensor prediction,
reduces the prediction errors by 33.1% compared with domain-specific, material
science LLMs (Darwin) trained on the same dataset. This natural language-based
approach lowers the barriers to computational materials science and highlights
the broader potential of LLMs for material property predictions and inverse
design....

---

### 122. SynCoTrain: A Dual Classifier PU-learning Framework for Synthesizability Prediction

**Authors:** Sasan Amariamir, Janine George, Philipp Benner

**Published:** 2024-11-18

**Category:** cond-mat.mtrl-sci

**ID:** 2411.12011v1

**Link:** [http://arxiv.org/abs/2411.12011v1](http://arxiv.org/abs/2411.12011v1)

**Summary:** Material discovery is a cornerstone of modern science, driving advancements
in diverse disciplines from biomedical technology to climate solutions.
Predicting synthesizability, a critical factor in realizing novel materials,
remains a complex challenge due to the limitations of traditional heuristics
and thermodynamic proxies. While stability metrics such as formation energy
offer partial insights, they fail to account for kinetic factors and
technological constraints that influence synthesis outcomes. These challenges
are further compounded by the scarcity of negative data, as failed synthesis
attempts are often unpublished or context-specific.
  We present SynCoTrain, a semi-supervised machine learning model designed to
predict the synthesizability of materials. SynCoTrain employs a co-training
framework leveraging two complementary graph convolutional neural networks:
SchNet and ALIGNN. By iteratively exchanging predictions between classifiers,
SynCoTrain mitigates model bias and enhances generalizability. Our approach
uses Positive and Unlabeled (PU) Learning to address the absence of explicit
negative data, iteratively refining predictions through collaborative learning.
  The model demonstrates robust performance, achieving high recall on internal
and leave-out test sets. By focusing on oxide crystals, a well-characterized
material family with extensive experimental data, we establish SynCoTrain as a
reliable tool for predicting synthesizability while balancing dataset
variability and computational efficiency. This work highlights the potential of
co-training to advance high-throughput materials discovery and generative
research, offering a scalable solution to the challenge of synthesizability
prediction....

---

### 123. Machine learning for structure-guided materials and process design

**Authors:** Lukas Morand, Tarek Iraki, Johannes Dornheim, Stefan Sandfeld, Norbert Link, Dirk Helm

**Published:** 2023-12-22

**Category:** cond-mat.mtrl-sci

**ID:** 2312.14552v3

**Link:** [http://arxiv.org/abs/2312.14552v3](http://arxiv.org/abs/2312.14552v3)

**Summary:** In recent years, there has been a growing interest in accelerated materials
innovation in the context of the process-structure-property chain. In this
regard, it is essential to take into account manufacturing processes and tailor
materials design approaches to support downstream process design approaches. As
a major step into this direction, we present a holistic and generic
optimization approach that covers the entire process-structure-property chain
in materials engineering. Our approach specifically employs machine learning to
address two critical identification problems: a materials design problem, which
involves identifying near-optimal material microstructures that exhibit desired
properties, and a process design problem that is to find an optimal processing
path to manufacture these microstructures. Both identification problems are
typically ill-posed, which presents a significant challenge for solution
approaches. However, the non-unique nature of these problems offers an
important advantage for processing: By having several target microstructures
that perform similarly well, processes can be efficiently guided towards
manufacturing the best reachable microstructure. The functionality of the
approach is demonstrated at manufacturing crystallographic textures with
desired properties in a simulated metal forming process....

---

### 124. Tensegrity-Inspired Polymer Films: Progressive Bending Stiffness through Multipolymeric Patterning

**Authors:** Rikima Kuwada, Shuto Ito, Yuta Shimoda, Haruka Fukunishi, Ryota Onishi, Daisuke Ishii, Mikihiro Hayashi

**Published:** 2024-11-05

**Category:** cond-mat.soft

**ID:** 2411.02982v2

**Link:** [http://arxiv.org/abs/2411.02982v2](http://arxiv.org/abs/2411.02982v2)

**Summary:** Materials with J-shaped stress-strain behavior under uniaxial stretching,
where strength increases as deformation progresses, have been developed through
various materials designs. On the other hand, polymer materials that
progressively stiffen under bending remain unrealized. To address this gap,
this study drew inspiration from membrane tensegrity structures, which achieve
structural stability by balancing compressive forces in rods and tensile forces
in membrane. Notably, some of these structures exhibit increased stiffness
under bending. Using a multipolymer patterning technique, we developed a
polymer film exhibiting membrane tensegrity-like properties that stiffens under
bending. This effect results from membrane tension generated by rod protrusions
and an increase in second moment of area at regions with maximum curvature....

---

### 125. Efficient Symmetry-Aware Materials Generation via Hierarchical Generative Flow Networks

**Authors:** Tri Minh Nguyen, Sherif Abdulkader Tawfik, Truyen Tran, Sunil Gupta, Santu Rana, Svetha Venkatesh

**Published:** 2024-11-06

**Category:** cs.LG

**ID:** 2411.04323v1

**Link:** [http://arxiv.org/abs/2411.04323v1](http://arxiv.org/abs/2411.04323v1)

**Summary:** Discovering new solid-state materials requires rapidly exploring the vast
space of crystal structures and locating stable regions. Generating stable
materials with desired properties and compositions is extremely difficult as we
search for very small isolated pockets in the exponentially many possibilities,
considering elements from the periodic table and their 3D arrangements in
crystal lattices. Materials discovery necessitates both optimized solution
structures and diversity in the generated material structures. Existing methods
struggle to explore large material spaces and generate diverse samples with
desired properties and requirements. We propose the Symmetry-aware Hierarchical
Architecture for Flow-based Traversal (SHAFT), a novel generative model
employing a hierarchical exploration strategy to efficiently exploit the
symmetry of the materials space to generate crystal structures given desired
properties. In particular, our model decomposes the exponentially large
materials space into a hierarchy of subspaces consisting of symmetric space
groups, lattice parameters, and atoms. We demonstrate that SHAFT significantly
outperforms state-of-the-art iterative generative methods, such as Generative
Flow Networks (GFlowNets) and Crystal Diffusion Variational AutoEncoders
(CDVAE), in crystal structure generation tasks, achieving higher validity,
diversity, and stability of generated structures optimized for target
properties and requirements....

---

### 126. Navigating Chemical Space with Latent Flows

**Authors:** Guanghao Wei, Yining Huang, Chenru Duan, Yue Song, Yuanqi Du

**Published:** 2024-05-07

**Category:** cs.LG

**ID:** 2405.03987v3

**Link:** [http://arxiv.org/abs/2405.03987v3](http://arxiv.org/abs/2405.03987v3)

**Summary:** Recent progress of deep generative models in the vision and language domain
has stimulated significant interest in more structured data generation such as
molecules. However, beyond generating new random molecules, efficient
exploration and a comprehensive understanding of the vast chemical space are of
great importance to molecular science and applications in drug design and
materials discovery. In this paper, we propose a new framework, ChemFlow, to
traverse chemical space through navigating the latent space learned by molecule
generative models through flows. We introduce a dynamical system perspective
that formulates the problem as learning a vector field that transports the mass
of the molecular distribution to the region with desired molecular properties
or structure diversity. Under this framework, we unify previous approaches on
molecule latent space traversal and optimization and propose alternative
competing methods incorporating different physical priors. We validate the
efficacy of ChemFlow on molecule manipulation and single- and multi-objective
molecule optimization tasks under both supervised and unsupervised molecular
discovery settings. Codes and demos are publicly available on GitHub at
https://github.com/garywei944/ChemFlow....

---

### 127. Unleashing the power of novel conditional generative approaches for new materials discovery

**Authors:** Lev Novitskiy, Vladimir Lazarev, Mikhail Tiutiulnikov, Nikita Vakhrameev, Roman Eremin, Innokentiy Humonen, Andrey Kuznetsov, Denis Dimitrov, Semen Budennyy

**Published:** 2024-11-05

**Category:** cond-mat.mtrl-sci

**ID:** 2411.03156v1

**Link:** [http://arxiv.org/abs/2411.03156v1](http://arxiv.org/abs/2411.03156v1)

**Summary:** For a very long time, computational approaches to the design of new materials
have relied on an iterative process of finding a candidate material and
modeling its properties. AI has played a crucial role in this regard, helping
to accelerate the discovery and optimization of crystal properties and
structures through advanced computational methodologies and data-driven
approaches. To address the problem of new materials design and fasten the
process of new materials search, we have applied latest generative approaches
to the problem of crystal structure design, trying to solve the inverse
problem: by given properties generate a structure that satisfies them without
utilizing supercomputer powers. In our work we propose two approaches: 1)
conditional structure modification: optimization of the stability of an
arbitrary atomic configuration, using the energy difference between the most
energetically favorable structure and all its less stable polymorphs and 2)
conditional structure generation. We used a representation for materials that
includes the following information: lattice, atom coordinates, atom types,
chemical features, space group and formation energy of the structure. The loss
function was optimized to take into account the periodic boundary conditions of
crystal structures. We have applied Diffusion models approach, Flow matching,
usual Autoencoder (AE) and compared the results of the models and approaches.
As a metric for the study, physical PyMatGen matcher was employed: we compare
target structure with generated one using default tolerances. So far, our
modifier and generator produce structures with needed properties with accuracy
41% and 82% respectively. To prove the offered methodology efficiency,
inference have been carried out, resulting in several potentially new
structures with formation energy below the AFLOW-derived convex hulls....

---

### 128. Ultrafast all-optical generation of pure spin and valley currents

**Authors:** Deepika Gill, Sangeeta Sharma, Sam Shallcross

**Published:** 2024-11-04

**Category:** cond-mat.mes-hall

**ID:** 2411.02371v1

**Link:** [http://arxiv.org/abs/2411.02371v1](http://arxiv.org/abs/2411.02371v1)

**Summary:** Pure currents comprise the flow of a two state quantum freedom -- for example
the electron spin -- in the absence of charge flow. Radically different from
the charge currents that underpin present day electronics, in two dimensional
materials possessing additional two state freedoms such as valley index they
offer profound possibilities for miniaturization and energy efficiency in a
next generation spin- and valley- tronics. Here we demonstrate a robust
multi-pump light wave protocol capable of generating both pure spin and valley
currents on femtosecond times. The generation time is determined by the 2d
material gap, with the creation of pure spin current in WSe2 at 40 fs and pure
valley current in bilayer graphene at ~200 fs. Our all-optical approach demands
no special material design, requiring only a gapped valley active material, and
is thus applicable to a wide range of 2d materials....

---

### 129. Smallest [5,6]fullerene as building blocks for 2D networks with superior stability and enhanced photocatalytic performance

**Authors:** Jiaqi Wu, Bo Peng

**Published:** 2024-09-23

**Category:** cond-mat.mtrl-sci

**ID:** 2409.15421v2

**Link:** [http://arxiv.org/abs/2409.15421v2](http://arxiv.org/abs/2409.15421v2)

**Summary:** The assembly of molecules to form covalent networks can create varied lattice
structures with distinct physical and chemical properties from conventional
atomic lattices. Using the smallest stable [5,6]fullerene units as building
blocks, various 2D C$_{24}$ networks can be formed with superior stability and
strength compared to the recently synthesised monolayer polymeric C$_{60}$.
Monolayer C$_{24}$ harnesses the properties of both carbon crystals and
fullerene molecules, such as stable chemical bonds, suitable band gaps and
large surface area, facilitating photocatalytic water splitting. The electronic
band gaps of C$_{24}$ are comparable to TiO$_2$, providing appropriate band
edges with sufficient external potential for overall water splitting over the
acidic and neutral pH range. Upon photoexcitation, strong solar absorption
enabled by strongly bound bright excitons can generate carriers effectively,
while the type-II band alignment between C$_{24}$ and other 2D monolayers can
separate electrons and holes in individual layers simultaneously. Additionally,
the number of surface active sites of C$_{24}$ monolayers are three times more
than that of their C$_{60}$ counterparts in a much wider pH range, providing
spontaneous reaction pathways for hydrogen evolution reaction. Our work
provides insights into materials design using tunable building blocks of
fullerene units with tailored functions for energy generation, conversion and
storage....

---

### 130. FlowLLM: Flow Matching for Material Generation with Large Language Models as Base Distributions

**Authors:** Anuroop Sriram, Benjamin Kurt Miller, Ricky T. Q. Chen, Brandon M. Wood

**Published:** 2024-10-30

**Category:** cs.LG

**ID:** 2410.23405v1

**Link:** [http://arxiv.org/abs/2410.23405v1](http://arxiv.org/abs/2410.23405v1)

**Summary:** Material discovery is a critical area of research with the potential to
revolutionize various fields, including carbon capture, renewable energy, and
electronics. However, the immense scale of the chemical space makes it
challenging to explore all possible materials experimentally. In this paper, we
introduce FlowLLM, a novel generative model that combines large language models
(LLMs) and Riemannian flow matching (RFM) to design novel crystalline
materials. FlowLLM first fine-tunes an LLM to learn an effective base
distribution of meta-stable crystals in a text representation. After converting
to a graph representation, the RFM model takes samples from the LLM and
iteratively refines the coordinates and lattice parameters. Our approach
significantly outperforms state-of-the-art methods, increasing the generation
rate of stable materials by over three times and increasing the rate for
stable, unique, and novel crystals by $\sim50\%$ - a huge improvement on a
difficult problem. Additionally, the crystals generated by FlowLLM are much
closer to their relaxed state when compared with another leading model,
significantly reducing post-hoc computational cost....

---

### 131. SLICES-PLUS: A Crystal Representation Leveraging Spatial Symmetry

**Authors:** Baoning Wang, Zhiyuan Xu, Zhiyu Han, Qiwen Nie, Hang Xiao, Gang Yan

**Published:** 2024-10-30

**Category:** physics.comp-ph

**ID:** 2410.22828v1

**Link:** [http://arxiv.org/abs/2410.22828v1](http://arxiv.org/abs/2410.22828v1)

**Summary:** In recent years, the realm of crystalline materials has witnessed a surge in
the development of generative models, predominantly aimed at the inverse design
of crystals with tailored physical properties. However, spatial symmetry, which
serves as a significant inductive bias, is often not optimally harnessed in the
design process. This oversight tends to result in crystals with lower symmetry,
potentially limiting the practical applications of certain functional
materials. To bridge this gap, we introduce SLICES-PLUS, an enhanced variant of
SLICES that emphasizes spatial symmetry. Our experiments in classification and
generation have shown that SLICES-PLUS exhibits greater sensitivity and
robustness in learning crystal symmetries compared to the original SLICES.
Furthermore, by integrating SLICES-PLUS with a customized MatterGPT model, we
have demonstrated its exceptional capability to target specific physical
properties and crystal systems with precision. Finally, we explore
autoregressive generation towards multiple elastic properties in few-shot
learning. Our research represents a significant step forward in the realm of
computational materials discovery....

---

### 132. Large Language Model-Guided Prediction Toward Quantum Materials Synthesis

**Authors:** Ryotaro Okabe, Zack West, Abhijatmedhi Chotrattanapituk, Mouyang Cheng, Denisse Córdova Carrizales, Weiwei Xie, Robert J. Cava, Mingda Li

**Published:** 2024-10-28

**Category:** cond-mat.mtrl-sci

**ID:** 2410.20976v1

**Link:** [http://arxiv.org/abs/2410.20976v1](http://arxiv.org/abs/2410.20976v1)

**Summary:** The synthesis of inorganic crystalline materials is essential for modern
technology, especially in quantum materials development. However, designing
efficient synthesis workflows remains a significant challenge due to the
precise experimental conditions and extensive trial and error. Here, we present
a framework using large language models (LLMs) to predict synthesis pathways
for inorganic materials, including quantum materials. Our framework contains
three models: LHS2RHS, predicting products from reactants; RHS2LHS, predicting
reactants from products; and TGT2CEQ, generating full chemical equations for
target compounds. Fine-tuned on a text-mined synthesis database, our model
raises accuracy from under 40% with pretrained models, to under 80% using
conventional fine-tuning, and further to around 90% with our proposed
generalized Tanimoto similarity, while maintaining robust to additional
synthesis steps. Our model further demonstrates comparable performance across
materials with varying degrees of quantumness quantified using quantum weight,
indicating that LLMs offer a powerful tool to predict balanced chemical
equations for quantum materials discovery....

---

### 133. MatExpert: Decomposing Materials Discovery by Mimicking Human Experts

**Authors:** Qianggang Ding, Santiago Miret, Bang Liu

**Published:** 2024-10-26

**Category:** cond-mat.mtrl-sci

**ID:** 2410.21317v1

**Link:** [http://arxiv.org/abs/2410.21317v1](http://arxiv.org/abs/2410.21317v1)

**Summary:** Material discovery is a critical research area with profound implications for
various industries. In this work, we introduce MatExpert, a novel framework
that leverages Large Language Models (LLMs) and contrastive learning to
accelerate the discovery and design of new solid-state materials. Inspired by
the workflow of human materials design experts, our approach integrates three
key stages: retrieval, transition, and generation. First, in the retrieval
stage, MatExpert identifies an existing material that closely matches the
desired criteria. Second, in the transition stage, MatExpert outlines the
necessary modifications to transform this material formulation to meet specific
requirements outlined by the initial user query. Third, in the generation
state, MatExpert performs detailed computations and structural generation to
create new materials based on the provided information. Our experimental
results demonstrate that MatExpert outperforms state-of-the-art methods in
material generation tasks, achieving superior performance across various
metrics including validity, distribution, and stability. As such, MatExpert
represents a meaningful advancement in computational material discovery using
langauge-based generative models....

---

### 134. Generative Design of Functional Metal Complexes Utilizing the Internal Knowledge of Large Language Models

**Authors:** Jieyu Lu, Zhangde Song, Qiyuan Zhao, Yuanqi Du, Yirui Cao, Haojun Jia, Chenru Duan

**Published:** 2024-10-21

**Category:** physics.chem-ph

**ID:** 2410.18136v1

**Link:** [http://arxiv.org/abs/2410.18136v1](http://arxiv.org/abs/2410.18136v1)

**Summary:** Designing functional transition metal complexes (TMCs) faces challenges due
to the vast search space of metals and ligands, requiring efficient
optimization strategies. Traditional genetic algorithms (GAs) are commonly
used, employing random mutations and crossovers driven by explicit mathematical
objectives to explore this space. Transferring knowledge between different GA
tasks, however, is difficult. We integrate large language models (LLMs) into
the evolutionary optimization framework (LLM-EO) and apply it in both single-
and multi-objective optimization for TMCs. We find that LLM-EO surpasses
traditional GAs by leveraging the chemical knowledge of LLMs gained during
their extensive pretraining. Remarkably, without supervised fine-tuning, LLMs
utilize the full historical data from optimization processes, outperforming
those focusing only on top-performing TMCs. LLM-EO successfully identifies
eight of the top-20 TMCs with the largest HOMO-LUMO gaps by proposing only 200
candidates out of a 1.37 million TMCs space. Through prompt engineering using
natural language, LLM-EO introduces unparalleled flexibility into
multi-objective optimizations, thereby circumventing the necessity for
intricate mathematical formulations. As generative models, LLMs can suggest new
ligands and TMCs with unique properties by merging both internal knowledge and
external chemistry data, thus combining the benefits of efficient optimization
and molecular generation. With increasing potential of LLMs as pretrained
foundational models and new post-training inference strategies, we foresee
broad applications of LLM-based evolutionary optimization in chemistry and
materials design....

---

### 135. LifeGPT: Topology-Agnostic Generative Pretrained Transformer Model for Cellular Automata

**Authors:** Jaime A. Berkovich, Markus J. Buehler

**Published:** 2024-09-03

**Category:** cs.AI

**ID:** 2409.12182v2

**Link:** [http://arxiv.org/abs/2409.12182v2](http://arxiv.org/abs/2409.12182v2)

**Summary:** Conway's Game of Life (Life), a well known algorithm within the broader class
of cellular automata (CA), exhibits complex emergent dynamics, with extreme
sensitivity to initial conditions. Modeling and predicting such intricate
behavior without explicit knowledge of the system's underlying topology
presents a significant challenge, motivating the development of algorithms that
can generalize across various grid configurations and boundary conditions. We
develop a decoder-only generative pretrained transformer (GPT) model to solve
this problem, showing that our model can simulate Life on a toroidal grid with
no prior knowledge on the size of the grid, or its periodic boundary conditions
(LifeGPT). LifeGPT is topology-agnostic with respect to its training data and
our results show that a GPT model is capable of capturing the deterministic
rules of a Turing-complete system with near-perfect accuracy, given
sufficiently diverse training data. We also introduce the idea of an
`autoregressive autoregressor' to recursively implement Life using LifeGPT. Our
results pave the path towards true universal computation within a large
language model framework, synthesizing of mathematical analysis with natural
language processing, and probing AI systems for situational awareness about the
evolution of such algorithms without ever having to compute them. Similar GPTs
could potentially solve inverse problems in multicellular self-assembly by
extracting CA-compatible rulesets from real-world biological systems to create
new predictive models, which would have significant consequences for the fields
of bioinspired materials, tissue engineering, and architected materials design....

---

### 136. Open Materials 2024 (OMat24) Inorganic Materials Dataset and Models

**Authors:** Luis Barroso-Luque, Muhammed Shuaibi, Xiang Fu, Brandon M. Wood, Misko Dzamba, Meng Gao, Ammar Rizvi, C. Lawrence Zitnick, Zachary W. Ulissi

**Published:** 2024-10-16

**Category:** cond-mat.mtrl-sci

**ID:** 2410.12771v1

**Link:** [http://arxiv.org/abs/2410.12771v1](http://arxiv.org/abs/2410.12771v1)

**Summary:** The ability to discover new materials with desirable properties is critical
for numerous applications from helping mitigate climate change to advances in
next generation computing hardware. AI has the potential to accelerate
materials discovery and design by more effectively exploring the chemical space
compared to other computational methods or by trial-and-error. While
substantial progress has been made on AI for materials data, benchmarks, and
models, a barrier that has emerged is the lack of publicly available training
data and open pre-trained models. To address this, we present a Meta FAIR
release of the Open Materials 2024 (OMat24) large-scale open dataset and an
accompanying set of pre-trained models. OMat24 contains over 110 million
density functional theory (DFT) calculations focused on structural and
compositional diversity. Our EquiformerV2 models achieve state-of-the-art
performance on the Matbench Discovery leaderboard and are capable of predicting
ground-state stability and formation energies to an F1 score above 0.9 and an
accuracy of 20 meV/atom, respectively. We explore the impact of model size,
auxiliary denoising objectives, and fine-tuning on performance across a range
of datasets including OMat24, MPtraj, and Alexandria. The open release of the
OMat24 dataset and models enables the research community to build upon our
efforts and drive further advancements in AI-assisted materials science....

---

### 137. 3M-Diffusion: Latent Multi-Modal Diffusion for Language-Guided Molecular Structure Generation

**Authors:** Huaisheng Zhu, Teng Xiao, Vasant G Honavar

**Published:** 2024-03-11

**Category:** cs.LG

**ID:** 2403.07179v2

**Link:** [http://arxiv.org/abs/2403.07179v2](http://arxiv.org/abs/2403.07179v2)

**Summary:** Generating molecular structures with desired properties is a critical task
with broad applications in drug discovery and materials design. We propose
3M-Diffusion, a novel multi-modal molecular graph generation method, to
generate diverse, ideally novel molecular structures with desired properties.
3M-Diffusion encodes molecular graphs into a graph latent space which it then
aligns with the text space learned by encoder-based LLMs from textual
descriptions. It then reconstructs the molecular structure and atomic
attributes based on the given text descriptions using the molecule decoder. It
then learns a probabilistic mapping from the text space to the latent molecular
graph space using a diffusion model. The results of our extensive experiments
on several datasets demonstrate that 3M-Diffusion can generate high-quality,
novel and diverse molecular graphs that semantically match the textual
description provided....

---

### 138. A method for the automatic generation of a minimal basis set of structural templates for material phase-space exploration

**Authors:** Caja Annweiler, Simone Di Cataldo, Maurits W. Haverkort, Lilia Boeri

**Published:** 2024-10-02

**Category:** cond-mat.mtrl-sci

**ID:** 2410.01641v1

**Link:** [http://arxiv.org/abs/2410.01641v1](http://arxiv.org/abs/2410.01641v1)

**Summary:** We present a novel method for predicting binary phase diagrams through the
automatic construction of a minimal basis set of representative templates. The
core assumption is that any materials space can be divided into a small number
of regions with similar chemical tendencies and bonding properties, and that a
minimal set of templates can efficiently represent the key chemical trends
across the different regions. By combining data-driven techniques with
ab-initio crystal structure prediction, we can efficiently partition the
materials space and construct templates reflecting variations in chemical
behavior. Preliminary results demonstrate that our method predicts binary
convex hulls with accuracy comparable to resource-intensive EA searches, while
achieving a significant reduction in computational time (by a factor of 25).
The method can be extended to ternary and multinary systems, enabling efficient
high-throughput exploration and mapping of complex material spaces. By
providing a transformative solution for high-throughput materials discovery,
our approach paves the way for uncovering advanced quantum materials and
accelerating in silico design....

---

### 139. Nonlinear Inverse Design of Mechanical Multi-Material Metamaterials Enabled by Video Denoising Diffusion and Structure Identifier

**Authors:** Jaewan Park, Shashank Kushwaha, Junyan He, Seid Koric, Qibang Liu, Iwona Jasiuk, Diab Abueidda

**Published:** 2024-09-20

**Category:** cs.AI

**ID:** 2409.13908v2

**Link:** [http://arxiv.org/abs/2409.13908v2](http://arxiv.org/abs/2409.13908v2)

**Summary:** Metamaterials, synthetic materials with customized properties, have emerged
as a promising field due to advancements in additive manufacturing. These
materials derive unique mechanical properties from their internal lattice
structures, which are often composed of multiple materials that repeat
geometric patterns. While traditional inverse design approaches have shown
potential, they struggle to map nonlinear material behavior to multiple
possible structural configurations. This paper presents a novel framework
leveraging video diffusion models, a type of generative artificial Intelligence
(AI), for inverse multi-material design based on nonlinear stress-strain
responses. Our approach consists of two key components: (1) a fields generator
using a video diffusion model to create solution fields based on target
nonlinear stress-strain responses, and (2) a structure identifier employing two
UNet models to determine the corresponding multi-material 2D design. By
incorporating multiple materials, plasticity, and large deformation, our
innovative design method allows for enhanced control over the highly nonlinear
mechanical behavior of metamaterials commonly seen in real-world applications.
It offers a promising solution for generating next-generation metamaterials
with finely tuned mechanical characteristics....

---

### 140. Are LLMs Ready for Real-World Materials Discovery?

**Authors:** Santiago Miret, N M Anoop Krishnan

**Published:** 2024-02-07

**Category:** cond-mat.mtrl-sci

**ID:** 2402.05200v2

**Link:** [http://arxiv.org/abs/2402.05200v2](http://arxiv.org/abs/2402.05200v2)

**Summary:** Large Language Models (LLMs) create exciting possibilities for powerful
language processing tools to accelerate research in materials science. While
LLMs have great potential to accelerate materials understanding and discovery,
they currently fall short in being practical materials science tools. In this
position paper, we show relevant failure cases of LLMs in materials science
that reveal current limitations of LLMs related to comprehending and reasoning
over complex, interconnected materials science knowledge. Given those
shortcomings, we outline a framework for developing Materials Science LLMs
(MatSci-LLMs) that are grounded in materials science knowledge and hypothesis
generation followed by hypothesis testing. The path to attaining performant
MatSci-LLMs rests in large part on building high-quality, multi-modal datasets
sourced from scientific literature where various information extraction
challenges persist. As such, we describe key materials science information
extraction challenges which need to be overcome in order to build large-scale,
multi-modal datasets that capture valuable materials science knowledge.
Finally, we outline a roadmap for applying future MatSci-LLMs for real-world
materials discovery via: 1. Automated Knowledge Base Generation; 2. Automated
In-Silico Material Design; and 3. MatSci-LLM Integrated Self-Driving Materials
Laboratories....

---

### 141. Learning Ordering in Crystalline Materials with Symmetry-Aware Graph Neural Networks

**Authors:** Jiayu Peng, James Damewood, Jessica Karaguesian, Jaclyn R. Lunger, Rafael Gómez-Bombarelli

**Published:** 2024-09-20

**Category:** cond-mat.mtrl-sci

**ID:** 2409.13851v1

**Link:** [http://arxiv.org/abs/2409.13851v1](http://arxiv.org/abs/2409.13851v1)

**Summary:** Graph convolutional neural networks (GCNNs) have become a machine learning
workhorse for screening the chemical space of crystalline materials in fields
such as catalysis and energy storage, by predicting properties from structures.
Multicomponent materials, however, present a unique challenge since they can
exhibit chemical (dis)order, where a given lattice structure can encompass a
variety of elemental arrangements ranging from highly ordered structures to
fully disordered solid solutions. Critically, properties like stability,
strength, and catalytic performance depend not only on structures but also on
orderings. To enable rigorous materials design, it is thus critical to ensure
GCNNs are capable of distinguishing among atomic orderings. However, the
ordering-aware capability of GCNNs has been poorly understood. Here, we
benchmark various neural network architectures for capturing the
ordering-dependent energetics of multicomponent materials in a custom-made
dataset generated with high-throughput atomistic simulations. Conventional
symmetry-invariant GCNNs were found unable to discern the structural difference
between the diverse symmetrically inequivalent atomic orderings of the same
material, while symmetry-equivariant model architectures could inherently
preserve and differentiate the distinct crystallographic symmetries of various
orderings....

---

### 142. Classification-based detection and quantification of cross-domain data bias in materials discovery

**Authors:** Giovanni Trezza, Eliodoro Chiavazzo

**Published:** 2023-11-16

**Category:** cond-mat.other

**ID:** 2311.09891v2

**Link:** [http://arxiv.org/abs/2311.09891v2](http://arxiv.org/abs/2311.09891v2)

**Summary:** It stands to reason that the amount and the quality of data is of key
importance for setting up accurate AI-driven models. Among others, a
fundamental aspect to consider is the bias introduced during sample selection
in database generation. This is particularly relevant when a model is trained
on a specialized dataset to predict a property of interest, and then applied to
forecast the same property over samples having a completely different genesis.
Indeed, the resulting biased model will likely produce unreliable predictions
for many of those out-of-the-box samples. Neglecting such an aspect may hinder
the AI-based discovery process, even when high quality, sufficiently large and
highly reputable data sources are available. In this regard, with
superconducting and thermoelectric materials as two prototypical case studies
in the field of energy material discovery, we present and validate a new method
(based on a classification strategy) capable of detecting, quantifying and
circumventing the presence of cross-domain data bias....

---

### 143. Imprinted atomic displacements drive spin-orbital order in a vanadate perovskite

**Authors:** P. Radhakrishnan, K. S. Rabinovich, A. V. Boris, K. Fürsich, M. Minola, G. Christiani, G. Logvenov, B. Keimer, E. Benckiser

**Published:** 2024-09-19

**Category:** cond-mat.mtrl-sci

**ID:** 2409.12871v1

**Link:** [http://arxiv.org/abs/2409.12871v1](http://arxiv.org/abs/2409.12871v1)

**Summary:** Perovskites with the generic composition ABO$_3$ exhibit an enormous variety
of quantum states such as magnetism, orbital order, ferroelectricity and
superconductivity. Their flexible and comparatively simple structure allows for
facile chemical substitution and cube-on-cube combination of different
compounds in atomically sharp epitaxial heterostructures. However, already in
the bulk, the diverse physical properties of perovskites and their anisotropy
are determined by small deviations from the ideal perovskite structure, which
are difficult to control. Here we show that directional imprinting of atomic
displacements in the antiferromagnetic Mott insulator YVO$_3$ is achieved by
depositing epitaxial films on different facets of an isostructural substrate.
These facets were chosen such that other control parameters, including strain
and polarity mismatch with the overlayer, remain unchanged. We use polarized
Raman scattering and spectral ellipsometry to detect signatures of staggered
orbital and magnetic order, and demonstrate distinct spin-orbital ordering
patterns on different facets. These observations can be attributed to the
influence of specific octahedral rotation and cation displacement patterns,
which are imprinted by the substrate facet, on the covalency of the bonds and
the superexchange interactions in YVO$_3$. Well beyond established
strain-engineering strategies, our results show that substrate-induced
templating of lattice distortion patterns constitutes a powerful pathway for
materials design....

---

### 144. Influence of Ru composition deviation from stoichiometry on intrinsic spin-to-charge conversion in SrRuO3

**Authors:** Shingo Kaneta-Takada, Yuki K. Wakabayashi, Hikari Shinya, Yoshitaka Taniyasu, Hideki Yamamoto, Yoshiharu Krockenberger, Masaaki Tanaka, Shinobu Ohya

**Published:** 2024-09-19

**Category:** cond-mat.mtrl-sci

**ID:** 2409.12598v1

**Link:** [http://arxiv.org/abs/2409.12598v1](http://arxiv.org/abs/2409.12598v1)

**Summary:** Interconversion between charge and spin currents is a key phenomenon in
realizing next-generation spintronic devices. Highly efficient spin-charge
interconversion is expected to occur at band crossing points in materials with
large spin-orbit interactions due to enhanced spin Berry curvature. On the
other hand, if defects and/or impurities are present, they affect the
electronic band structure, which in turn reduces the spin Berry curvature.
Although defects and impurities are generally numerous in materials, their
influence on the spin Berry curvature and, consequently, spin-charge
interconversion has often been overlooked. In this paper, we perform
spin-pumping experiments for stoichiometric SrRuO3 and non-stoichiometric
SrRu0.7O3 films at 300 K, where the films are in paramagnetic states, to
examine how Ru composition deviation from the stoichiometric condition
influences the spin-to-charge conversion, showing that SrRuO3 has a larger spin
Hall angle than SrRu0.7O3. We derive the band structures of paramagnetic SrRuO3
and SrRu0.75O3 using first-principles calculations, indicating that the spin
Hall conductivity originating from the spin Berry curvature decreases when the
Ru deficiency is incorporated, which agrees with the experimental results. Our
results suggest that point-defect- and impurity control is essential to fully
exploit the intrinsic spin Berry curvature and large spin-charge
interconversion function of materials. These insights help us with material
designs for efficient spin-charge interconversions....

---

### 145. Construction and sampling of alloy cluster expansions -- A tutorial

**Authors:** Pernilla Ekborg-Tanner, Petter Rosander, Erik Fransson, Paul Erhart

**Published:** 2024-05-23

**Category:** cond-mat.mtrl-sci

**ID:** 2405.14787v2

**Link:** [http://arxiv.org/abs/2405.14787v2](http://arxiv.org/abs/2405.14787v2)

**Summary:** Crystalline alloys and related mixed systems make up a large family of
materials with high tunability which have been proposed as the solution to a
large number of energy related materials design problems. Due to the presence
of chemical order and disorder in these systems, neither experimental efforts
nor ab-initio computational methods alone are sufficient to span the inherently
large configuration space. Therefore, fast and accurate models are necessary.
To this end, cluster expansions have been widely and successfully used for the
past decades. Cluster expansions are generalized Ising models designed to
predict the energy of any atomic configuration of a system after training on a
small subset of the available configurations. Constructing and sampling a
cluster expansion consists of multiple steps that have to be performed with
care. In this tutorial, we provide a comprehensive guide to this process,
highlighting important considerations and potential pitfalls. The tutorial
consists of three parts, starting with cluster expansion construction for a
relatively simple system, continuing with strategies for more challenging
systems such as surfaces and closing with examples of Monte Carlo sampling of
cluster expansions to study order-disorder transitions and phase diagrams....

---

### 146. A Perspective on AI-Guided Molecular Simulations in VR: Exploring Strategies for Imitation Learning in Hyperdimensional Molecular Systems

**Authors:** Mohamed Dhouioui, Jonathan Barnoud, Rhoslyn Roebuck Williams, Harry J. Stroud, Phil Bates, David R. Glowacki

**Published:** 2024-09-11

**Category:** cs.LG

**ID:** 2409.07189v1

**Link:** [http://arxiv.org/abs/2409.07189v1](http://arxiv.org/abs/2409.07189v1)

**Summary:** Molecular dynamics simulations are a crucial computational tool for
researchers to understand and engineer molecular structure and function in
areas such as drug discovery, protein engineering, and material design. Despite
their utility, MD simulations are expensive, owing to the high dimensionality
of molecular systems. Interactive molecular dynamics in virtual reality
(iMD-VR) has recently been developed as a 'human-in-the-loop' strategy, which
leverages high-performance computing to accelerate the researcher's ability to
solve the hyperdimensional sampling problem. By providing an immersive 3D
environment that enables visualization and manipulation of real-time molecular
motion, iMD-VR enables researchers and students to efficiently and intuitively
explore and navigate these complex, high-dimensional systems. iMD-VR platforms
offer a unique opportunity to quickly generate rich datasets that capture human
experts' spatial insight regarding molecular structure and function. This paper
explores the possibility of employing user-generated iMD-VR datasets to train
AI agents via imitation learning (IL). IL is an important technique in robotics
that enables agents to mimic complex behaviors from expert demonstrations, thus
circumventing the need for explicit programming or intricate reward design. We
review the utilization of IL for manipulation tasks in robotics and discuss how
iMD-VR recordings could be used to train IL models for solving specific
molecular 'tasks'. We then investigate how such approaches could be applied to
the data captured from iMD-VR recordings. Finally, we outline the future
research directions and potential challenges of using AI agents to augment
human expertise to efficiently navigate conformational spaces, highlighting how
this approach could provide valuable insight across domains such as materials
science, protein engineering, and computer-aided drug design....

---

### 147. Beyond designer's knowledge: Generating materials design hypotheses via large language models

**Authors:** Quanliang Liu, Maciej P. Polak, So Yeon Kim, MD Al Amin Shuvo, Hrishikesh Shridhar Deodhar, Jeongsoo Han, Dane Morgan, Hyunseok Oh

**Published:** 2024-09-10

**Category:** cs.LG

**ID:** 2409.06756v1

**Link:** [http://arxiv.org/abs/2409.06756v1](http://arxiv.org/abs/2409.06756v1)

**Summary:** Materials design often relies on human-generated hypotheses, a process
inherently limited by cognitive constraints such as knowledge gaps and limited
ability to integrate and extract knowledge implications, particularly when
multidisciplinary expertise is required. This work demonstrates that large
language models (LLMs), coupled with prompt engineering, can effectively
generate non-trivial materials hypotheses by integrating scientific principles
from diverse sources without explicit design guidance by human experts. These
include design ideas for high-entropy alloys with superior cryogenic properties
and halide solid electrolytes with enhanced ionic conductivity and formability.
These design ideas have been experimentally validated in high-impact
publications in 2023 not available in the LLM training data, demonstrating the
LLM's ability to generate highly valuable and realizable innovative ideas not
established in the literature. Our approach primarily leverages materials
system charts encoding processing-structure-property relationships, enabling
more effective data integration by condensing key information from numerous
papers, and evaluation and categorization of numerous hypotheses for human
cognition, both through the LLM. This LLM-driven approach opens the door to new
avenues of artificial intelligence-driven materials discovery by accelerating
design, democratizing innovation, and expanding capabilities beyond the
designer's direct knowledge....

---

### 148. VQCrystal: Leveraging Vector Quantization for Discovery of Stable Crystal Structures

**Authors:** ZiJie Qiu, Luozhijie Jin, Zijian Du, Hongyu Chen, Yan Cen, Siqi Sun, Yongfeng Mei, Hao Zhang

**Published:** 2024-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2409.06191v1

**Link:** [http://arxiv.org/abs/2409.06191v1](http://arxiv.org/abs/2409.06191v1)

**Summary:** Discovering functional crystalline materials through computational methods
remains a formidable challenge in materials science. Here, we introduce
VQCrystal, an innovative deep learning framework that leverages discrete latent
representations to overcome key limitations in current approaches to crystal
generation and inverse design. VQCrystal employs a hierarchical VQ-VAE
architecture to encode global and atom-level crystal features, coupled with a
machine learning-based inter-atomic potential(IAP) model and a genetic
algorithm to realize property-targeted inverse design. Benchmark evaluations on
diverse datasets demonstrate VQCrystal's advanced capabilities in
representation learning and novel crystal discovery. Notably, VQCrystal
achieves state-of-the-art performance with 91.93\% force validity and a
Fr\'echet Distance of 0.152 on MP-20, indicating both strong validity and high
diversity in the sampling process. To demonstrate real-world applicability, we
apply VQCrystal for both 3D and 2D material design. For 3D materials, the
density-functional theory validation confirmed that 63.04\% of bandgaps and
99\% of formation energies of the 56 filtered materials matched the target
range. Moreover, 437 generated materials were validated as existing entries in
the full database outside the training set. For the discovery of 2D materials,
73.91\% of 23 filtered structures exhibited high stability with formation
energies below -1 eV/atom. Our results highlight VQCrystal's potential to
accelerate the discovery of novel materials with tailored properties....

---

### 149. Performance of Exchange-Correlation Approximations to Density-Functional Theory for Rare-earth Oxides

**Authors:** Mary Kathleen Caucci, Jacob T. Sivak, Saeed S. I. Almishal, Christina M. Rost, Ismaila Dabo, Jon-Paul Maria, Susan B. Sinnott

**Published:** 2024-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2409.06145v1

**Link:** [http://arxiv.org/abs/2409.06145v1](http://arxiv.org/abs/2409.06145v1)

**Summary:** Rare-earth oxides (REOs) are an important class of materials owing to their
unique properties, including high ionic conductivities, large dielectric
constants, and elevated melting temperatures, making them relevant to several
technological applications such as catalysis, ionic conduction, and sensing.
The ability to predict these properties at moderate computational cost is
essential to guiding materials discovery and optimizing materials performance.
Although density-functional theory (DFT) is the favored approach for predicting
electronic and atomic structures, its accuracy is limited in describing strong
electron correlation and localization inherent to REOs. The newly developed
strongly constrained and appropriately normed (SCAN) meta-generalized-gradient
approximations (meta-GGAs) promise improved accuracy in modeling these strongly
correlated systems. We assess the performance of these meta-GGAs on binary REOs
by comparing the numerical accuracy of thirteen exchange-correlation
approximations in predicting structural, magnetic, and electronic properties.
Hubbard U corrections for self-interaction errors and spin-orbit coupling are
systematically considered. Our comprehensive assessment offers insights into
the physical properties and functional performance of REOs predicted by
first-principles and provides valuable guidance for selecting optimal DFT
functionals for exploring these materials....

---

### 150. SciAgents: Automating scientific discovery through multi-agent intelligent graph reasoning

**Authors:** Alireza Ghafarollahi, Markus J. Buehler

**Published:** 2024-09-09

**Category:** cs.AI

**ID:** 2409.05556v1

**Link:** [http://arxiv.org/abs/2409.05556v1](http://arxiv.org/abs/2409.05556v1)

**Summary:** A key challenge in artificial intelligence is the creation of systems capable
of autonomously advancing scientific understanding by exploring novel domains,
identifying complex patterns, and uncovering previously unseen connections in
vast scientific data. In this work, we present SciAgents, an approach that
leverages three core concepts: (1) the use of large-scale ontological knowledge
graphs to organize and interconnect diverse scientific concepts, (2) a suite of
large language models (LLMs) and data retrieval tools, and (3) multi-agent
systems with in-situ learning capabilities. Applied to biologically inspired
materials, SciAgents reveals hidden interdisciplinary relationships that were
previously considered unrelated, achieving a scale, precision, and exploratory
power that surpasses traditional human-driven research methods. The framework
autonomously generates and refines research hypotheses, elucidating underlying
mechanisms, design principles, and unexpected material properties. By
integrating these capabilities in a modular fashion, the intelligent system
yields material discoveries, critique and improve existing hypotheses, retrieve
up-to-date data about existing research, and highlights their strengths and
limitations. Our case studies demonstrate scalable capabilities to combine
generative AI, ontological representations, and multi-agent modeling,
harnessing a `swarm of intelligence' similar to biological systems. This
provides new avenues for materials discovery and accelerates the development of
advanced materials by unlocking Nature's design principles....

---

### 151. Fine-tuning large language models for domain adaptation: Exploration of training strategies, scaling, model merging and synergistic capabilities

**Authors:** Wei Lu, Rachel K. Luu, Markus J. Buehler

**Published:** 2024-09-05

**Category:** cs.CL

**ID:** 2409.03444v1

**Link:** [http://arxiv.org/abs/2409.03444v1](http://arxiv.org/abs/2409.03444v1)

**Summary:** The advancement of Large Language Models (LLMs) for domain applications in
fields such as materials science and engineering depends on the development of
fine-tuning strategies that adapt models for specialized, technical
capabilities. In this work, we explore the effects of Continued Pretraining
(CPT), Supervised Fine-Tuning (SFT), and various preference-based optimization
approaches, including Direct Preference Optimization (DPO) and Odds Ratio
Preference Optimization (ORPO), on fine-tuned LLM performance. Our analysis
shows how these strategies influence model outcomes and reveals that the
merging of multiple fine-tuned models can lead to the emergence of capabilities
that surpass the individual contributions of the parent models. We find that
model merging leads to new functionalities that neither parent model could
achieve alone, leading to improved performance in domain-specific assessments.
Experiments with different model architectures are presented, including Llama
3.1 8B and Mistral 7B models, where similar behaviors are observed. Exploring
whether the results hold also for much smaller models, we use a tiny LLM with
1.7 billion parameters and show that very small LLMs do not necessarily feature
emergent capabilities under model merging, suggesting that model scaling may be
a key component. In open-ended yet consistent chat conversations between a
human and AI models, our assessment reveals detailed insights into how
different model variants perform and show that the smallest model achieves a
high intelligence score across key criteria including reasoning depth,
creativity, clarity, and quantitative precision. Other experiments include the
development of image generation prompts based on disparate biological material
design concepts, to create new microstructures, architectural concepts, and
urban design based on biological materials-inspired construction principles....

---

### 152. Scalable Crystal Structure Relaxation Using an Iteration-Free Deep Generative Model with Uncertainty Quantification

**Authors:** Ziduo Yang, Yi-Ming Zhao, Xian Wang, Xiaoqing Liu, Xiuying Zhang, Yifan Li, Qiujie Lv, Calvin Yu-Chian Chen, Lei Shen

**Published:** 2024-04-01

**Category:** cond-mat.mtrl-sci

**ID:** 2404.00865v2

**Link:** [http://arxiv.org/abs/2404.00865v2](http://arxiv.org/abs/2404.00865v2)

**Summary:** In computational molecular and materials science, determining equilibrium
structures is the crucial first step for accurate subsequent property
calculations. However, the recent discovery of millions of new crystals and
complex twisted structures has challenged traditional computational methods,
both ab initio and machine-learning-based, due to their computationally
intensive iterative processes. To address these scalability issues, here we
introduce DeepRelax, a deep generative model capable of performing geometric
crystal structure relaxation rapidly and without iterations. DeepRelax learns
the equilibrium structural distribution, enabling it to predict relaxed
structures directly from their unrelaxed ones. The ability to perform
structural relaxation at the millisecond level per structure, combined with the
scalability of parallel processing, makes DeepRelax particularly useful for
large-scale virtual screening. We demonstrate DeepRelax's reliability and
robustness by applying it to five diverse databases, including oxides,
Materials Project, two-dimensional materials, van der Waals crystals, and
crystals with point defects. DeepRelax consistently shows high accuracy and
efficiency, validated by density functional theory calculations. Finally, we
enhance its trustworthiness by integrating uncertainty quantification. This
work significantly accelerates computational workflows, offering a robust and
trustworthy machine-learning method for material discovery and advancing the
application of AI for science. Code for DeepRelax is available at
https://github.com/Shen-Group/DeepRelax....

---

### 153. Multi-Fidelity Active Learning with GFlowNets

**Authors:** Alex Hernandez-Garcia, Nikita Saxena, Moksh Jain, Cheng-Hao Liu, Yoshua Bengio

**Published:** 2023-06-20

**Category:** cs.LG

**ID:** 2306.11715v2

**Link:** [http://arxiv.org/abs/2306.11715v2](http://arxiv.org/abs/2306.11715v2)

**Summary:** In the last decades, the capacity to generate large amounts of data in
science and engineering applications has been growing steadily. Meanwhile,
machine learning has progressed to become a suitable tool to process and
utilise the available data. Nonetheless, many relevant scientific and
engineering problems present challenges where current machine learning methods
cannot yet efficiently leverage the available data and resources. For example,
in scientific discovery, we are often faced with the problem of exploring very
large, structured and high-dimensional spaces. Moreover, the high fidelity,
black-box objective function is often very expensive to evaluate. Progress in
machine learning methods that can efficiently tackle such challenges would help
accelerate currently crucial areas such as drug and materials discovery. In
this paper, we propose a multi-fidelity active learning algorithm with
GFlowNets as a sampler, to efficiently discover diverse, high-scoring
candidates where multiple approximations of the black-box function are
available at lower fidelity and cost. Our evaluation on molecular discovery
tasks shows that multi-fidelity active learning with GFlowNets can discover
high-scoring candidates at a fraction of the budget of its single-fidelity
counterpart while maintaining diversity, unlike RL-based alternatives. These
results open new avenues for multi-fidelity active learning to accelerate
scientific discovery and engineering design....

---

### 154. AlabOS: A Python-based Reconfigurable Workflow Management Framework for Autonomous Laboratories

**Authors:** Yuxing Fei, Bernardus Rendy, Rishi Kumar, Olympia Dartsi, Hrushikesh P. Sahasrabuddhe, Matthew J. McDermott, Zheren Wang, Nathan J. Szymanski, Lauren N. Walters, David Milsted, Yan Zeng, Anubhav Jain, Gerbrand Ceder

**Published:** 2024-05-22

**Category:** cond-mat.mtrl-sci

**ID:** 2405.13930v2

**Link:** [http://arxiv.org/abs/2405.13930v2](http://arxiv.org/abs/2405.13930v2)

**Summary:** The recent advent of autonomous laboratories, coupled with algorithms for
high-throughput screening and active learning, promises to accelerate materials
discovery and innovation. As these autonomous systems grow in complexity, the
demand for robust and efficient workflow management software becomes
increasingly critical. In this paper, we introduce AlabOS, a general-purpose
software framework for orchestrating experiments and managing resources, with
an emphasis on automated laboratories for materials synthesis and
characterization. AlabOS features a reconfigurable experiment workflow model
and a resource reservation mechanism, enabling the simultaneous execution of
varied workflows composed of modular tasks while eliminating conflicts between
tasks. To showcase its capability, we demonstrate the implementation of AlabOS
in a prototype autonomous materials laboratory, A-Lab, with around 3,500
samples synthesized over 1.5 years....

---

### 155. Generative Design of Crystal Structures by Point Cloud Representations and Diffusion Model

**Authors:** Zhelin Li, Rami Mrad, Runxian Jiao, Guan Huang, Jun Shan, Shibing Chu, Yuanping Chen

**Published:** 2024-01-24

**Category:** cs.AI

**ID:** 2401.13192v3

**Link:** [http://arxiv.org/abs/2401.13192v3](http://arxiv.org/abs/2401.13192v3)

**Summary:** Efficiently generating energetically stable crystal structures has long been
a challenge in material design, primarily due to the immense arrangement of
atoms in a crystal lattice. To facilitate the discovery of stable material, we
present a framework for the generation of synthesizable materials, leveraging a
point cloud representation to encode intricate structural information. At the
heart of this framework lies the introduction of a diffusion model as its
foundational pillar. To gauge the efficacy of our approach, we employ it to
reconstruct input structures from our training datasets, rigorously validating
its high reconstruction performance. Furthermore, we demonstrate the profound
potential of Point Cloud-Based Crystal Diffusion (PCCD) by generating entirely
new materials, emphasizing their synthesizability. Our research stands as a
noteworthy contribution to the advancement of materials design and synthesis
through the cutting-edge avenue of generative design instead of the
conventional substitution or experience-based discovery....

---

### 156. Cross-Modal Learning for Chemistry Property Prediction: Large Language Models Meet Graph Machine Learning

**Authors:** Sakhinana Sagar Srinivas, Venkataramana Runkana

**Published:** 2024-08-27

**Category:** cs.LG

**ID:** 2408.14964v1

**Link:** [http://arxiv.org/abs/2408.14964v1](http://arxiv.org/abs/2408.14964v1)

**Summary:** In the field of chemistry, the objective is to create novel molecules with
desired properties, facilitating accurate property predictions for applications
such as material design and drug screening. However, existing graph deep
learning methods face limitations that curb their expressive power. To address
this, we explore the integration of vast molecular domain knowledge from Large
Language Models (LLMs) with the complementary strengths of Graph Neural
Networks (GNNs) to enhance performance in property prediction tasks. We
introduce a Multi-Modal Fusion (MMF) framework that synergistically harnesses
the analytical prowess of GNNs and the linguistic generative and predictive
abilities of LLMs, thereby improving accuracy and robustness in predicting
molecular properties. Our framework combines the effectiveness of GNNs in
modeling graph-structured data with the zero-shot and few-shot learning
capabilities of LLMs, enabling improved predictions while reducing the risk of
overfitting. Furthermore, our approach effectively addresses distributional
shifts, a common challenge in real-world applications, and showcases the
efficacy of learning cross-modal representations, surpassing state-of-the-art
baselines on benchmark datasets for property prediction tasks....

---

### 157. Space Group Informed Transformer for Crystalline Materials Generation

**Authors:** Zhendong Cao, Xiaoshan Luo, Jian Lv, Lei Wang

**Published:** 2024-03-23

**Category:** cond-mat.mtrl-sci

**ID:** 2403.15734v2

**Link:** [http://arxiv.org/abs/2403.15734v2](http://arxiv.org/abs/2403.15734v2)

**Summary:** We introduce CrystalFormer, a transformer-based autoregressive model
specifically designed for space group-controlled generation of crystalline
materials. The incorporation of space group symmetry significantly simplifies
the crystal space, which is crucial for data and compute efficient generative
modeling of crystalline materials. Leveraging the prominent discrete and
sequential nature of the Wyckoff positions, CrystalFormer learns to generate
crystals by directly predicting the species and locations of
symmetry-inequivalent atoms in the unit cell. We demonstrate the advantages of
CrystalFormer in standard tasks such as symmetric structure initialization and
element substitution compared to conventional methods implemented in popular
crystal structure prediction software. Moreover, we showcase the application of
CrystalFormer of property-guided materials design in a plug-and-play manner.
Our analysis shows that CrystalFormer ingests sensible solid-state chemistry
knowledge and heuristics by compressing the material dataset, thus enabling
systematic exploration of crystalline materials. The simplicity, generality,
and flexibility of CrystalFormer position it as a promising architecture to be
the foundational model of the entire crystalline materials space, heralding a
new era in materials modeling and discovery....

---

### 158. MatterGPT: A Generative Transformer for Multi-Property Inverse Design of Solid-State Materials

**Authors:** Yan Chen, Xueru Wang, Xiaobin Deng, Yilun Liu, Xi Chen, Yunwei Zhang, Lei Wang, Hang Xiao

**Published:** 2024-08-14

**Category:** cond-mat.mtrl-sci

**ID:** 2408.07608v1

**Link:** [http://arxiv.org/abs/2408.07608v1](http://arxiv.org/abs/2408.07608v1)

**Summary:** Inverse design of solid-state materials with desired properties represents a
formidable challenge in materials science. Although recent generative models
have demonstrated potential, their adoption has been hindered by limitations
such as inefficiency, architectural constraints and restricted open-source
availability. The representation of crystal structures using the SLICES
(Simplified Line-Input Crystal-Encoding System) notation as a string of
characters enables the use of state-of-the-art natural language processing
models, such as Transformers, for crystal design. Drawing inspiration from the
success of GPT models in generating coherent text, we trained a generative
Transformer on the next-token prediction task to generate solid-state materials
with targeted properties. We demonstrate MatterGPT's capability to generate de
novo crystal structures with targeted single properties, including both
lattice-insensitive (formation energy) and lattice-sensitive (band gap)
properties. Furthermore, we extend MatterGPT to simultaneously target multiple
properties, addressing the complex challenge of multi-objective inverse design
of crystals. Our approach showcases high validity, uniqueness, and novelty in
generated structures, as well as the ability to generate materials with
properties beyond the training data distribution. This work represents a
significant step forward in computational materials discovery, offering a
powerful and open tool for designing materials with tailored properties for
various applications in energy, electronics, and beyond....

---

### 159. Representation-space diffusion models for generating periodic materials

**Authors:** Anshuman Sinha, Shuyi Jia, Victor Fung

**Published:** 2024-08-13

**Category:** cond-mat.mtrl-sci

**ID:** 2408.07213v1

**Link:** [http://arxiv.org/abs/2408.07213v1](http://arxiv.org/abs/2408.07213v1)

**Summary:** Generative models hold the promise of significantly expediting the materials
design process when compared to traditional human-guided or rule-based
methodologies. However, effectively generating high-quality periodic structures
of materials on limited but diverse datasets remains an ongoing challenge. Here
we propose a novel approach for periodic structure generation which fully
respect the intrinsic symmetries, periodicity, and invariances of the structure
space. Namely, we utilize differentiable, physics-based, structural descriptors
which can describe periodic systems and satisfy the necessary invariances, in
conjunction with a denoising diffusion model which generates new materials
within this descriptor or representation space. Reconstruction is then
performed on these representations using gradient-based optimization to recover
the corresponding Cartesian positions of the crystal structure. This approach
differs significantly from current methods by generating materials in the
representation space, rather than in the Cartesian space, which is made
possible using an efficient reconstruction algorithm. Consequently, known
issues with respecting periodic boundaries and translational and rotational
invariances during generation can be avoided, and the model training process
can be greatly simplified. We show this approach is able to provide competitive
performance on established benchmarks compared to current state-of-the-art
methods....

---

### 160. Deep learning generative model for crystal structure prediction

**Authors:** Xiaoshan Luo, Zhenyu Wang, Pengyue Gao, Jian Lv, Yanchao Wang, Changfeng Chen, Yanming Ma

**Published:** 2024-03-16

**Category:** cond-mat.mtrl-sci

**ID:** 2403.10846v2

**Link:** [http://arxiv.org/abs/2403.10846v2](http://arxiv.org/abs/2403.10846v2)

**Summary:** Recent advances in deep learning generative models (GMs) have created high
capabilities in accessing and assessing complex high-dimensional data, allowing
superior efficiency in navigating vast material configuration space in search
of viable structures. Coupling such capabilities with physically significant
data to construct trained models for materials discovery is crucial to moving
this emerging field forward. Here, we present a universal GM for crystal
structure prediction (CSP) via a conditional crystal diffusion variational
autoencoder (Cond-CDVAE) approach, which is tailored to allow user-defined
material and physical parameters such as composition and pressure. This model
is trained on an expansive dataset containing over 670,000 local minimum
structures, including a rich spectrum of high-pressure structures, along with
ambient-pressure structures in Materials Project database. We demonstrate that
the Cond-CDVAE model can generate physically plausible structures with high
fidelity under diverse pressure conditions without necessitating local
optimization, accurately predicting 59.3% of the 3,547 unseen ambient-pressure
experimental structures within 800 structure samplings, with the accuracy rate
climbing to 83.2% for structures comprising fewer than 20 atoms per unit cell.
These results meet or exceed those achieved via conventional CSP methods based
on global optimization. The present findings showcase substantial potential of
GMs in the realm of CSP....

---

### 161. Scientific Exploration with Expert Knowledge (SEEK) in Autonomous Scanning Probe Microscopy with Active Learning

**Authors:** Utkarsh Pratiush, Hiroshi Funakubo, Rama Vasudevan, Sergei V. Kalinin, Yongtao Liu

**Published:** 2024-08-04

**Category:** cond-mat.mtrl-sci

**ID:** 2408.02071v1

**Link:** [http://arxiv.org/abs/2408.02071v1](http://arxiv.org/abs/2408.02071v1)

**Summary:** Microscopy techniques have played vital roles in materials science, biology,
and nanotechnology, offering high-resolution imaging and detailed insights into
properties at nanoscale and atomic level. The automation of microscopy
experiments, in combination with machine learning approaches, is a
transformative advancement, offering increased efficiency, reproducibility, and
the capability to perform complex experiments. Our previous work on autonomous
experimentation with scanning probe microscopy (SPM) demonstrated an active
learning framework using deep kernel learning (DKL) for structure-property
relationship discovery. This approach has demonstrated broad applications in
various microscopy techniques. Here, to address limitations of workflows based
on DKL, we developed methods to incorporate prior knowledge and human interest
into DKL-based workflows and implemented these workflows in SPM. By integrating
expected rewards from structure libraries or spectroscopic features, we
enhanced the exploration efficiency of autonomous microscopy, demonstrating
more efficient and targeted exploration in autonomous microscopy. We
demonstrated the application of these methods in SPM, but we suggest that these
methods can be seamlessly applied to other microscopy and imaging techniques.
Furthermore, the concept can be adapted for general Bayesian optimization in
material discovery across a broad range of autonomous experimental fields....

---

### 162. Rapid Discovery of Graphene Nanocrystals Using DFT and Bayesian Optimization with Neural Network Kernel

**Authors:** Şener Özönder, H. Kübra Küçükkartal

**Published:** 2022-08-16

**Category:** cond-mat.mtrl-sci

**ID:** 2208.07612v2

**Link:** [http://arxiv.org/abs/2208.07612v2](http://arxiv.org/abs/2208.07612v2)

**Summary:** Density functional theory (DFT) is a powerful computational method used to
obtain physical and chemical properties of materials. In the materials
discovery framework, it is often necessary to virtually screen a large and
high-dimensional chemical space to find materials with desired properties.
However, grid searching a large chemical space with DFT is inefficient due to
its high computational cost. We propose an approach utilizing Bayesian
optimization (BO) with an artificial neural network kernel to enable smart
search. This method leverages the BO algorithm, where the neural network,
trained on a limited number of DFT results, determines the most promising
regions of the chemical space to explore in subsequent iterations. This
approach aims to discover materials with target properties while minimizing the
number of DFT calculations required. To demonstrate the effectiveness of this
method, we investigated 63 doped graphene quantum dots (GQDs) with sizes
ranging from 1 to 2 nm to find the structure with the highest light absorbance.
Using time-dependent DFT (TDDFT) only 12 times, we achieved a significant
reduction in computational cost, approximately 20% of what would be required
for a full grid search, by employing the BO algorithm with a neural network
kernel. Considering that TDDFT calculations for a single GQD require about half
a day of wall time on high-performance computing nodes, this reduction is
substantial. Our approach can be generalized to the discovery of new drugs,
chemicals, crystals, and alloys with high-dimensional and large chemical
spaces, offering a scalable solution for various applications in materials
science....

---

### 163. PSP-GEN: Stochastic inversion of the Process-Structure-Property chain in materials design through deep, generative probabilistic modeling

**Authors:** Yaohua Zang, Phaedon-Stelios Koutsourelakis

**Published:** 2024-08-02

**Category:** cond-mat.mtrl-sci

**ID:** 2408.01114v1

**Link:** [http://arxiv.org/abs/2408.01114v1](http://arxiv.org/abs/2408.01114v1)

**Summary:** Inverse material design is a cornerstone challenge in materials science, with
significant applications across many industries. Traditional approaches that
invert the structure-property (SP) linkage to identify microstructures with
targeted properties often overlook the feasibility of production processes,
leading to microstructures that may not be manufacturable. Achieving both
desired properties and a realizable manufacturing procedure necessitates
inverting the entire Process-Structure-Property (PSP) chain. However, this task
is fraught with challenges, including stochasticity along the whole modeling
chain, the high dimensionality of microstructures and process parameters, and
the inherent ill-posedness of the inverse problem. This paper proposes a novel
framework, named PSP-GEN, for the goal-oriented material design that
effectively addresses these challenges by modeling the entire PSP chain with a
deep generative model. It employs two sets of continuous, microstructure- and
property-aware, latent variables, the first of which provides a
lower-dimensional representation that captures the stochastic aspects of
microstructure generation, while the second is a direct link to processing
parameters. This structured, low-dimensional embedding not only simplifies the
handling of high-dimensional microstructure data but also facilitates the
application of gradient-based optimization techniques. The effectiveness and
efficiency of this method are demonstrated in the inverse design of two-phase
materials, where the objective is to design microstructures with target
effective permeability. We compare state-of-the-art alternatives in challenging
settings involving limited training data, target property regions for which no
training data is available, and design tasks where the process parameters and
microstructures have high-dimensional representations....

---

### 164. Unlocking Thermoelectric Potential: A Machine Learning Stacking Approach for Half Heusler Alloys

**Authors:** Vipin K. E, Prahallad Padhan

**Published:** 2024-08-01

**Category:** cond-mat.mtrl-sci

**ID:** 2408.00466v1

**Link:** [http://arxiv.org/abs/2408.00466v1](http://arxiv.org/abs/2408.00466v1)

**Summary:** Thermoelectric properties of Half Heusler alloys are predicted by adopting an
ensemble modelling approach, specifically the stacking model integrated using
Random Forest and XGBoost scheme. Leveraging a diverse dataset encompassing
thermal conductivity, the Seebeck coefficient, electrical conductivity, and the
figure of merit (ZT), the study demonstrates superior predictive performance of
the stacking Model, outperforming individual base models with high R2 values.
Key features such as temperature, mean Covalent Radius, and average deviation
of the Gibbs energy per atom emerge as critical influencers, highlighting their
pivotal roles in optimizing thermoelectric behavior. The unification of Random
Forest and XGBoost in the stacking model effectively captures nuanced
relationships, offering a holistic understanding of thermoelectric performance
in Half Heusler alloys. This work advances predictive modelling in
thermoelectricity and provides valuable insights for strategic material design,
paving the way for enhanced efficiency and performance in thermoelectric
applications. The ensemble modelling framework, coupled with insightful feature
selection and meticulous engineering, establishes a robust foundation for
future research in pursuing high-performance thermoelectric materials....

---

### 165. Low dimensional fragment-based descriptors for property predictions in inorganic materials with machine learning

**Authors:** Md Mohaiminul Islam

**Published:** 2024-07-30

**Category:** cond-mat.mtrl-sci

**ID:** 2407.21146v1

**Link:** [http://arxiv.org/abs/2407.21146v1](http://arxiv.org/abs/2407.21146v1)

**Summary:** In recent times, the use of machine learning in materials design and
discovery has aided to accelerate the discovery of innovative materials with
extraordinary properties, which otherwise would have been driven by a laborious
and time-consuming trial-and-error process. In this study, a simple yet
powerful fragment-based descriptor, Low Dimensional Fragment Descriptors
(LDFD), is proposed to work in conjunction with machine learning models to
predict important properties of a wide range of inorganic materials such as
perovskite oxides, metal halide perovskites, alloys, semiconductor, and other
materials system and can also be extended to work with interfaces. To predict
properties, the generation of descriptors requires only the structural formula
of the materials and, in presence of identical structure in the dataset,
additional system properties as input. And the generation of descriptors
involves few steps, encoding the formula in binary space and reduction of
dimensionality, allowing easy implementation and prediction. To evaluate
descriptor performance, six known datasets with up to eight components were
compared. The method was applied to properties such as band gaps of perovskites
and semiconductors, lattice constant of magnetic alloys, bulk/shear modulus of
superhard alloys, critical temperature of superconductors, formation enthalpy
and energy above hull convex of perovskite oxides. An advanced python-based
data mining tool matminer was utilized for the collection of data. The
prediction accuracies are equivalent to the quality of the training data and
show comparable effectiveness as previous studies. This method should be
extendable to any inorganic material systems which can be subdivided into
layers or crystal structures with more than one atom site, and with the
progress of data mining the performance should get better with larger and
unbiased datasets....

---

### 166. Targeted Adaptive Design

**Authors:** Carlo Graziani, Marieme Ngom

**Published:** 2022-05-27

**Category:** cs.LG

**ID:** 2205.14208v3

**Link:** [http://arxiv.org/abs/2205.14208v3](http://arxiv.org/abs/2205.14208v3)

**Summary:** Modern advanced manufacturing and advanced materials design often require
searches of relatively high-dimensional process control parameter spaces for
settings that result in optimal structure, property, and performance
parameters. The mapping from the former to the latter must be determined from
noisy experiments or from expensive simulations. We abstract this problem to a
mathematical framework in which an unknown function from a control space to a
design space must be ascertained by means of expensive noisy measurements,
which locate optimal control settings generating desired design features within
specified tolerances, with quantified uncertainty. We describe targeted
adaptive design (TAD), a new algorithm that performs this sampling task
efficiently. TAD creates a Gaussian process surrogate model of the unknown
mapping at each iterative stage, proposing a new batch of control settings to
sample experimentally and optimizing the updated log-predictive likelihood of
the target design. TAD either stops upon locating a solution with uncertainties
that fit inside the tolerance box or uses a measure of expected future
information to determine that the search space has been exhausted with no
solution. TAD thus embodies the exploration-exploitation tension in a manner
that recalls, but is essentially different from, Bayesian optimization and
optimal experimental design....

---

### 167. Dismai-Bench: Benchmarking and designing generative models using disordered materials and interfaces

**Authors:** Adrian Xiao Bin Yong, Tianyu Su, Elif Ertekin

**Published:** 2024-04-10

**Category:** cond-mat.mtrl-sci

**ID:** 2404.06734v2

**Link:** [http://arxiv.org/abs/2404.06734v2](http://arxiv.org/abs/2404.06734v2)

**Summary:** Generative models have received significant attention in recent years for
materials science applications, particularly in the area of inverse design for
materials discovery. However, these models are usually assessed based on newly
generated, unverified materials, which provide a narrow evaluation of a model's
performance. Also, current efforts for inorganic materials have predominantly
focused on small crystals, even though the capability to generate large
disordered structures would significantly expand the applicability of
generative modeling. In this work, we present the Disordered Materials &
Interfaces Benchmark (Dismai-Bench), a generative model benchmark that uses
datasets of disordered alloys, interfaces, and amorphous silicon (256-264 atoms
per structure). Models are trained on each dataset independently, and evaluated
through direct structural comparisons between training and generated
structures. Benchmarking was performed on two graph diffusion models and two
(coordinate-based) U-Net diffusion models. The graph models were found to
significantly outperform the U-Net models due to the higher expressive power of
graphs. While noise in the less expressive models can assist in discovering
materials by facilitating exploration beyond the training distribution, these
models face significant challenges when confronted with more complex
structures. To further demonstrate the benefits of this benchmarking in the
development process of a generative model, we considered the case of developing
a point-cloud-based generative adversarial network (GAN) to generate low-energy
disordered interfaces. We show that the best performing architecture, CryinGAN,
outperforms the U-Net models, and is competitive against the graph models
despite its lack of invariances and weaker expressive power. This work provides
a new framework and insights to guide the development of future generative
models....

---

### 168. AtomAgents: Alloy design and discovery through physics-aware multi-modal multi-agent artificial intelligence

**Authors:** Alireza Ghafarollahi, Markus J. Buehler

**Published:** 2024-07-13

**Category:** cs.AI

**ID:** 2407.10022v1

**Link:** [http://arxiv.org/abs/2407.10022v1](http://arxiv.org/abs/2407.10022v1)

**Summary:** The design of alloys is a multi-scale problem that requires a holistic
approach that involves retrieving relevant knowledge, applying advanced
computational methods, conducting experimental validations, and analyzing the
results, a process that is typically reserved for human experts. Machine
learning (ML) can help accelerate this process, for instance, through the use
of deep surrogate models that connect structural features to material
properties, or vice versa. However, existing data-driven models often target
specific material objectives, offering limited flexibility to integrate
out-of-domain knowledge and cannot adapt to new, unforeseen challenges. Here,
we overcome these limitations by leveraging the distinct capabilities of
multiple AI agents that collaborate autonomously within a dynamic environment
to solve complex materials design tasks. The proposed physics-aware generative
AI platform, AtomAgents, synergizes the intelligence of large language models
(LLM) the dynamic collaboration among AI agents with expertise in various
domains, including knowledge retrieval, multi-modal data integration,
physics-based simulations, and comprehensive results analysis across modalities
that includes numerical data and images of physical simulation results. The
concerted effort of the multi-agent system allows for addressing complex
materials design problems, as demonstrated by examples that include
autonomously designing metallic alloys with enhanced properties compared to
their pure counterparts. Our results enable accurate prediction of key
characteristics across alloys and highlight the crucial role of solid solution
alloying to steer the development of advanced metallic alloys. Our framework
enhances the efficiency of complex multi-objective design tasks and opens new
avenues in fields such as biomedical materials engineering, renewable energy,
and environmental sustainability....

---

### 169. T2MAT (text-to-materials): A universal framework for generating material structures with goal properties from a single sentence

**Authors:** Zhilong Song, Shuaihua Lu, Qionghua Zhou, Jinlan Wang

**Published:** 2024-07-09

**Category:** cond-mat.mtrl-sci

**ID:** 2407.06489v1

**Link:** [http://arxiv.org/abs/2407.06489v1](http://arxiv.org/abs/2407.06489v1)

**Summary:** Artificial Intelligence-Generated Content (AIGC)-content autonomously
produced by AI systems without human intervention-has significantly boosted
efficiency across various fields. However, the AIGC in material science faces
challenges in the ability to efficiently discover innovative materials that
surpass existing databases, alongside the invariances and stability
considerations of crystal structures. To address these challenges, we develop
T2MAT (Text-to-Material), a comprehensive framework processing from a
user-input sentence to inverse design material structures with goal properties
beyond the existing database via globally exploring chemical space, followed by
an entirely automated workflow of first principal validation. Furthermore, we
propose CGTNet (Crystal Graph Transformer NETwork), a novel graph neural
network model that captures long-term interactions, to enhance the accuracy and
data efficiency of property prediction and thereby improve the reliability of
inverse design. Through these contributions, T2MAT minimizes the dependency on
human expertise and significantly enhances the efficiency of designing novel,
high-performance functional materials, thereby actualizing AIGC in the
materials design domain....

---

### 170. MolTRES: Improving Chemical Language Representation Learning for Molecular Property Prediction

**Authors:** Jun-Hyung Park, Yeachan Kim, Mingyu Lee, Hyuntae Park, SangKeun Lee

**Published:** 2024-07-09

**Category:** physics.chem-ph

**ID:** 2408.01426v1

**Link:** [http://arxiv.org/abs/2408.01426v1](http://arxiv.org/abs/2408.01426v1)

**Summary:** Chemical representation learning has gained increasing interest due to the
limited availability of supervised data in fields such as drug and materials
design. This interest particularly extends to chemical language representation
learning, which involves pre-training Transformers on SMILES sequences --
textual descriptors of molecules. Despite its success in molecular property
prediction, current practices often lead to overfitting and limited scalability
due to early convergence. In this paper, we introduce a novel chemical language
representation learning framework, called MolTRES, to address these issues.
MolTRES incorporates generator-discriminator training, allowing the model to
learn from more challenging examples that require structural understanding. In
addition, we enrich molecular representations by transferring knowledge from
scientific literature by integrating external materials embedding. Experimental
results show that our model outperforms existing state-of-the-art models on
popular molecular property prediction tasks....

---

### 171. ML-extendable framework for multiphysics-multiscale simulation workflow and data management using Kadi4Mat

**Authors:** Somnath Bharech, Yangyiwei Yang, Michael Selzer, Britta Nestler, Bai-Xiang Xu

**Published:** 2024-07-02

**Category:** cond-mat.mtrl-sci

**ID:** 2407.02162v1

**Link:** [http://arxiv.org/abs/2407.02162v1](http://arxiv.org/abs/2407.02162v1)

**Summary:** As material modeling and simulation has become vital for modern materials
science, research data with distinctive physical principles and extensive
volume are generally required for full elucidation of the material behavior
across all relevant scales. Effective workflow and data management, with
corresponding metadata descriptions, helps leverage the full potential of
data-driven analyses for computer-aided material design. In this work, we
propose a research workflow and data management (RWDM) framework to manage
complex workflows and resulting research (meta)data, while following FAIR
principles. Multiphysics multiscale simulations for additive manufacturing
investigations are treated as showcase and implemented on Kadi4Mat: an open
source research data infrastructure. The input and output data of the
simulations, together with the associated setups and scripts realizing the
simulation workflow, are curated in corresponding standardized Kadi4Mat records
with extendibility for further research and data-driven analyses. These records
are interlinked to indicate information flow and form an ontology based
knowledge graph. Automation scheme for performing high-throughput simulation
and post-processing integrated with the proposed RWDM framework is also
presented....

---

### 172. From design to device: challenges and opportunities in computational discovery of p-type transparent conductors

**Authors:** Rachel Woods-Robinson, Monica Morales-Masis, Geoffroy Hautier, Andrea Crovetto

**Published:** 2024-02-29

**Category:** physics.app-ph

**ID:** 2402.19378v2

**Link:** [http://arxiv.org/abs/2402.19378v2](http://arxiv.org/abs/2402.19378v2)

**Summary:** A high-performance p-type transparent conductor (TC) does not yet exist, but
could lead to advances in a wide range of optoelectronic applications and
enable new architectures for, e.g., next-generation photovoltaic (PV) devices.
High-throughput computational material screenings have been a promising
approach to filter databases and identify new p-type TC candidates, and some of
these predictions have been experimentally validated. However, most of these
predicted candidates do not have experimentally-achieved properties on par with
n-type TCs used in solar cells, and therefore have not yet been used in
commercial devices. Thus, there is still a significant divide between
transforming predictions into results that are actually achievable in the lab,
and an even greater lag in scaling predicted materials into functional devices.
In this perspective, we outline some of the major disconnects in this materials
discovery process -- from scaling computational predictions into synthesizable
crystals and thin films in the laboratory, to scaling lab-grown films into
real-world solar devices -- and share insights to inform future strategies for
TC discovery and design....

---

### 173. AtomGPT: Atomistic Generative Pre-trained Transformer for Forward and Inverse Materials Design

**Authors:** Kamal Choudhary

**Published:** 2024-05-06

**Category:** cond-mat.mtrl-sci

**ID:** 2405.03680v2

**Link:** [http://arxiv.org/abs/2405.03680v2](http://arxiv.org/abs/2405.03680v2)

**Summary:** Large language models (LLMs) such as generative pretrained transformers
(GPTs) have shown potential for various commercial applications, but their
applicability for materials design remains underexplored. In this article, we
introduce AtomGPT, a model specifically developed for materials design based on
transformer architectures, to demonstrate the capability for both atomistic
property prediction and structure generation. We show that a combination of
chemical and structural text descriptions can efficiently predict material
properties with accuracy comparable to graph neural network models, including
formation energies, electronic bandgaps from two different methods and
superconducting transition temperatures. Furthermore, we demonstrate that
AtomGPT can generate atomic structures for tasks such as designing new
superconductors, with the predictions validated through density functional
theory calculations. This work paves the way for leveraging LLMs in forward and
inverse materials design, offering an efficient approach to the discovery and
optimization of materials....

---

### 174. Thin Film Synthesis, Structural Analysis, and Magnetic Properties of Novel Ternary Transition Metal Nitride MnCoN2

**Authors:** Sita Dugu, Rebecca W Smaha, Shaham Quadir, Andrew Treglia, Shaun ODonnell, Julia Martin, Sharad Mahatara, Glenn Teeter, Stephan Lany, James R Neilson, Sage R Bauers

**Published:** 2024-06-20

**Category:** cond-mat.mtrl-sci

**ID:** 2406.14443v1

**Link:** [http://arxiv.org/abs/2406.14443v1](http://arxiv.org/abs/2406.14443v1)

**Summary:** Recent high-throughput computational searches have predicted many novel
ternary nitride compounds providing new opportunities for materials discovery
in under explored phase spaces. Nevertheless, there are hardly any predictions
and/or syntheses that incorporate only transition metals into new ternary
nitrides. Here, we report on the synthesis, structure, and properties of
MnCoN$_2$, a new ternary nitride material comprising only transition metals and
N. We find that crystalline MnCoN$_2$ can be stabilized over its competing
binaries, and over a tendency of this system to become amorphous, by
controlling growth temperature within a narrow window slightly above ambient
condition. We find that single-phase MnCoN$_2$ thin films form in a
cation-disordered rocksalt crystal structure, which is supported by ab-initio
calculations. X-ray photoelectron spectroscopy analysis suggests that MnCoN$_2$
is sensitive to oxygen through various oxides and hydroxides binding to cobalt
on the surface. X-ray absorption spectroscopy is used to verify that Mn$^{3+}$
and Co$^{3+}$ cations exist in an octahedrally-coordinated environment, which
is distinct from a combination of CoN and MnN binaries and in agreement with
the rocksalt-based crystal structure prediction. Magnetic measurements suggest
that MnCoN$_2$ has a canted antiferromagnetic ground state below 10 K. We
extract a Weiss temperature of $\theta$ = -49.7 K, highlighting the
antiferromagnetic correlations in MnCoN$_2$....

---

### 175. LLMatDesign: Autonomous Materials Discovery with Large Language Models

**Authors:** Shuyi Jia, Chao Zhang, Victor Fung

**Published:** 2024-06-19

**Category:** cond-mat.mtrl-sci

**ID:** 2406.13163v1

**Link:** [http://arxiv.org/abs/2406.13163v1](http://arxiv.org/abs/2406.13163v1)

**Summary:** Discovering new materials can have significant scientific and technological
implications but remains a challenging problem today due to the enormity of the
chemical space. Recent advances in machine learning have enabled data-driven
methods to rapidly screen or generate promising materials, but these methods
still depend heavily on very large quantities of training data and often lack
the flexibility and chemical understanding often desired in materials
discovery. We introduce LLMatDesign, a novel language-based framework for
interpretable materials design powered by large language models (LLMs).
LLMatDesign utilizes LLM agents to translate human instructions, apply
modifications to materials, and evaluate outcomes using provided tools. By
incorporating self-reflection on its previous decisions, LLMatDesign adapts
rapidly to new tasks and conditions in a zero-shot manner. A systematic
evaluation of LLMatDesign on several materials design tasks, in silico,
validates LLMatDesign's effectiveness in developing new materials with
user-defined target properties in the small data regime. Our framework
demonstrates the remarkable potential of autonomous LLM-guided materials
discovery in the computational setting and towards self-driving laboratories in
the future....

---

### 176. Optimal pre-train/fine-tune strategies for accurate material property predictions

**Authors:** Reshma Devi, Keith T. Butler, Gopalakrishnan Sai Gautam

**Published:** 2024-06-19

**Category:** cond-mat.mtrl-sci

**ID:** 2406.13142v1

**Link:** [http://arxiv.org/abs/2406.13142v1](http://arxiv.org/abs/2406.13142v1)

**Summary:** Overcoming the challenge of limited data availability within materials
science is crucial for the broad-based applicability of machine learning within
materials science. One pathway to overcome this limited data availability is to
use the framework of transfer learning (TL), where a pre-trained (PT) machine
learning model (on a larger dataset) can be fine-tuned (FT) on a target
(typically smaller) dataset. Our study systematically explores the
effectiveness of various PT/FT strategies to learn and predict material
properties with limited data. Specifically, we leverage graph neural networks
(GNNs) to PT/FT on seven diverse curated materials datasets, encompassing sizes
ranging from 941 to 132,752 datapoints. We consider datasets that cover a
spectrum of material properties, ranging from band gaps (electronic) to
formation energies (thermodynamic) and shear moduli (mechanical). We study the
influence of PT and FT dataset sizes, strategies that can be employed for FT,
and other hyperparameters on pair-wise TL among the datasets considered. We
find our pair-wise PT-FT models to consistently outperform models trained from
scratch on the target datasets. Importantly, we develop a GNN framework that is
simultaneously PT on multiple properties (MPT), enabling the construction of
generalized GNN models. Our MPT models outperform pair-wise PT-FT models on
several datasets considered, and more significantly, on a 2D material band gap
dataset that is completely out-of-distribution from the PT datasets. Finally,
we expect our PT/FT and MPT frameworks to be generalizable to other GNNs and
materials properties, which can accelerate materials design and discovery for
various applications....

---

### 177. Universal materials model of deep-learning density functional theory Hamiltonian

**Authors:** Yuxiang Wang, Yang Li, Zechen Tang, He Li, Zilong Yuan, Honggeng Tao, Nianlong Zou, Ting Bao, Xinghao Liang, Zezhou Chen, Shanghua Xu, Ce Bian, Zhiming Xu, Chong Wang, Chen Si, Wenhui Duan, Yong Xu

**Published:** 2024-06-15

**Category:** physics.comp-ph

**ID:** 2406.10536v1

**Link:** [http://arxiv.org/abs/2406.10536v1](http://arxiv.org/abs/2406.10536v1)

**Summary:** Realizing large materials models has emerged as a critical endeavor for
materials research in the new era of artificial intelligence, but how to
achieve this fantastic and challenging objective remains elusive. Here, we
propose a feasible pathway to address this paramount pursuit by developing
universal materials models of deep-learning density functional theory
Hamiltonian (DeepH), enabling computational modeling of the complicated
structure-property relationship of materials in general. By constructing a
large materials database and substantially improving the DeepH method, we
obtain a universal materials model of DeepH capable of handling diverse
elemental compositions and material structures, achieving remarkable accuracy
in predicting material properties. We further showcase a promising application
of fine-tuning universal materials models for enhancing specific materials
models. This work not only demonstrates the concept of DeepH's universal
materials model but also lays the groundwork for developing large materials
models, opening up significant opportunities for advancing artificial
intelligence-driven materials discovery....

---

### 178. Accelerating Scientific Discovery with Generative Knowledge Extraction, Graph-Based Representation, and Multimodal Intelligent Graph Reasoning

**Authors:** Markus J. Buehler

**Published:** 2024-03-18

**Category:** cs.LG

**ID:** 2403.11996v3

**Link:** [http://arxiv.org/abs/2403.11996v3](http://arxiv.org/abs/2403.11996v3)

**Summary:** Leveraging generative Artificial Intelligence (AI), we have transformed a
dataset comprising 1,000 scientific papers into an ontological knowledge graph.
Through an in-depth structural analysis, we have calculated node degrees,
identified communities and connectivities, and evaluated clustering
coefficients and betweenness centrality of pivotal nodes, uncovering
fascinating knowledge architectures. The graph has an inherently scale-free
nature, is highly connected, and can be used for graph reasoning by taking
advantage of transitive and isomorphic properties that reveal unprecedented
interdisciplinary relationships that can be used to answer queries, identify
gaps in knowledge, propose never-before-seen material designs, and predict
material behaviors. We compute deep node embeddings for combinatorial node
similarity ranking for use in a path sampling strategy links dissimilar
concepts that have previously not been related. One comparison revealed
structural parallels between biological materials and Beethoven's 9th Symphony,
highlighting shared patterns of complexity through isomorphic mapping. In
another example, the algorithm proposed a hierarchical mycelium-based composite
based on integrating path sampling with principles extracted from Kandinsky's
'Composition VII' painting. The resulting material integrates an innovative set
of concepts that include a balance of chaos/order, adjustable porosity,
mechanical strength, and complex patterned chemical functionalization. We
uncover other isomorphisms across science, technology and art, revealing a
nuanced ontology of immanence that reveal a context-dependent heterarchical
interplay of constituents. Graph-based generative AI achieves a far higher
degree of novelty, explorative capacity, and technical detail, than
conventional approaches and establishes a widely useful framework for
innovation by revealing hidden connections....

---

### 179. Representing Molecules as Random Walks Over Interpretable Grammars

**Authors:** Michael Sun, Minghao Guo, Weize Yuan, Veronika Thost, Crystal Elaine Owens, Aristotle Franklin Grosz, Sharvaa Selvan, Katelyn Zhou, Hassan Mohiuddin, Benjamin J Pedretti, Zachary P Smith, Jie Chen, Wojciech Matusik

**Published:** 2024-03-13

**Category:** cs.LG

**ID:** 2403.08147v3

**Link:** [http://arxiv.org/abs/2403.08147v3](http://arxiv.org/abs/2403.08147v3)

**Summary:** Recent research in molecular discovery has primarily been devoted to small,
drug-like molecules, leaving many similarly important applications in material
design without adequate technology. These applications often rely on more
complex molecular structures with fewer examples that are carefully designed
using known substructures. We propose a data-efficient and interpretable model
for representing and reasoning over such molecules in terms of graph grammars
that explicitly describe the hierarchical design space featuring motifs to be
the design basis. We present a novel representation in the form of random walks
over the design space, which facilitates both molecule generation and property
prediction. We demonstrate clear advantages over existing methods in terms of
performance, efficiency, and synthesizability of predicted molecules, and we
provide detailed insights into the method's chemical interpretability....

---

### 180. Molecular Modelling of Aqueous Batteries

**Authors:** Alicia van Hees, Zhan-Yun Zhang, Aishwarya Sudhama, Chao Zhang

**Published:** 2024-06-01

**Category:** cond-mat.mtrl-sci

**ID:** 2406.00468v1

**Link:** [http://arxiv.org/abs/2406.00468v1](http://arxiv.org/abs/2406.00468v1)

**Summary:** Aqueous batteries play an increasingly important role for the development of
sustainable and safety-prioritised energy storage solutions. Compared to
conventional lithium-ion batteries, the cell chemistry in aqueous batteries
share many common features with those of electrolyzer and pseudo-capacitor
systems because of the involvement of aqueous electrolyte and proton activity.
This imposes the needs for a better understanding of the corresponding ion
solvation, intercalation and electron transfer processes at atomistic scale.
Therefore, this chapter provides an up-to-date overview of molecular modelling
techniques and their applications in aqueous batteries. In particular, we
emphasize on the dynamical and reactive description of aqueous battery systems
brought in by density functional theory-based molecular dynamics simulation
(DFTMD) and its machine-learning (ML) accelerated counterpart. Moreover, we
also cover the recent advancement of generative artificial intelligence (AI) in
molecular and materials design of aqueous batteries. Case studies presented
here include popular aqueous battery systems, such as water-in-salt
electrolytes, proton-coupled cathode materials, Zn-ion batteries as well as
organic redox flow batteries....

---

### 181. UniIF: Unified Molecule Inverse Folding

**Authors:** Zhangyang Gao, Jue Wang, Cheng Tan, Lirong Wu, Yufei Huang, Siyuan Li, Zhirui Ye, Stan Z. Li

**Published:** 2024-05-29

**Category:** cs.AI

**ID:** 2405.18968v1

**Link:** [http://arxiv.org/abs/2405.18968v1](http://arxiv.org/abs/2405.18968v1)

**Summary:** Molecule inverse folding has been a long-standing challenge in chemistry and
biology, with the potential to revolutionize drug discovery and material
science. Despite specified models have been proposed for different small- or
macro-molecules, few have attempted to unify the learning process, resulting in
redundant efforts. Complementary to recent advancements in molecular structure
prediction, such as RoseTTAFold All-Atom and AlphaFold3, we propose the unified
model UniIF for the inverse folding of all molecules. We do such unification in
two levels: 1) Data-Level: We propose a unified block graph data form for all
molecules, including the local frame building and geometric feature
initialization. 2) Model-Level: We introduce a geometric block attention
network, comprising a geometric interaction, interactive attention and virtual
long-term dependency modules, to capture the 3D interactions of all molecules.
Through comprehensive evaluations across various tasks such as protein design,
RNA design, and material design, we demonstrate that our proposed method
surpasses state-of-the-art methods on all tasks. UniIF offers a versatile and
effective solution for general molecule inverse folding....

---

### 182. Inverse Design of Promising Alloys for Electrocatalytic CO$_2$ Reduction via Generative Graph Neural Networks Combined with Bird Swarm Algorithm

**Authors:** Zhilong Song, Linfeng Fan, Shuaihua Lu, Qionghua Zhou, Chongyi Ling, Jinlan Wang

**Published:** 2024-05-29

**Category:** cond-mat.mtrl-sci

**ID:** 2405.18891v1

**Link:** [http://arxiv.org/abs/2405.18891v1](http://arxiv.org/abs/2405.18891v1)

**Summary:** Directly generating material structures with optimal properties is a
long-standing goal in material design. One of the fundamental challenges lies
in how to overcome the limitation of traditional generative models to
efficiently explore the global chemical space rather than a small localized
space. Herein, we develop a framework named MAGECS to address this dilemma, by
integrating the bird swarm algorithm and supervised graph neural network to
effectively navigate the generative model in the immense chemical space towards
materials with target properties. As a demonstration, MAGECS is applied to
design compelling alloy electrocatalysts for CO$_2$ reduction reaction
(CO$_2$RR) and works extremely well. Specifically, the chemical space of
CO$_2$RR is effectively explored, where over 250,000 promising structures with
high activity have been generated and notably, the proportion of desired
structures is 2.5-fold increased. Moreover, five predicted alloys, i.e., CuAl,
AlPd, Sn$_2$Pd$_5$, Sn$_9$Pd$_7$, and CuAlSe$_2$ are successfully synthesized
and characterized experimentally, two of which exhibit about 90% Faraday
efficiency of CO$_2$RR, and CuAl achieved 76% efficiency for C$_2$ products.
This pioneering application of inverse design in CO$_2$RR catalysis showcases
the potential of MAGECS to dramatically accelerate the development of
functional materials, paving the way for fully automated, artificial
intelligence-driven material design....

---

### 183. Procedural Construction of Atomistic Polyurethane Block Copolymer Models for High Throughput Simulations

**Authors:** Dominic Robe, Adrian Menzel, Andrew W Phillips, Elnaz Hajizadeh

**Published:** 2024-05-24

**Category:** cond-mat.mtrl-sci

**ID:** 2405.15226v1

**Link:** [http://arxiv.org/abs/2405.15226v1](http://arxiv.org/abs/2405.15226v1)

**Summary:** In this work, methods are presented to automatically generate a fully
atomistic LAMMPS models of arbitrary linear multiblock polyurethane copolymers.
The routine detailed here receives as parameters the number of repeat units per
hard block, the number of units in a soft block, and the number of soft blocks
per chain, as well as chemical formulae of three monomers which will form the
hard component, soft component, and chain extender. A routine is detailed for
converting the chemical structure of a free monomer to the urethane bonded
repeat units in a polymer. The python package RadonPy is leveraged to assemble
these units into blocks, and the blocks into copolymers. Care is taken in this
work to ensure that plausible atomic charges are assigned to repeat units in
different parts of the chain. The static structure factor is calculated for a
variety of chemistries, and the results compared with wide angle x-ray
scattering data from experiments with corresponding composition. The generated
models reproduce the amorphous halo observed in the scattering data as well as
some of the finer details. Structure factor calculations are decomposed into
the partial structure factors to interrogate the structural properties of the
two block types separately. Parametric surveys are carried out of the effects
of various parameters, including temperature, soft block length, and block
connectivity on the observed structure. The routine detailed here for
constructing models is robust enough to be executed automatically in a high
throughput workflow for material design and discovery....

---

### 184. A Generative Model for Accelerated Inverse Modelling Using a Novel Embedding for Continuous Variables

**Authors:** Sébastien Bompas, Stefan Sandfeld

**Published:** 2023-11-19

**Category:** cs.LG

**ID:** 2311.11343v3

**Link:** [http://arxiv.org/abs/2311.11343v3](http://arxiv.org/abs/2311.11343v3)

**Summary:** In materials science, the challenge of rapid prototyping materials with
desired properties often involves extensive experimentation to find suitable
microstructures. Additionally, finding microstructures for given properties is
typically an ill-posed problem where multiple solutions may exist. Using
generative machine learning models can be a viable solution which also reduces
the computational cost. This comes with new challenges because, e.g., a
continuous property variable as conditioning input to the model is required. We
investigate the shortcomings of an existing method and compare this to a novel
embedding strategy for generative models that is based on the binary
representation of floating point numbers. This eliminates the need for
normalization, preserves information, and creates a versatile embedding space
for conditioning the generative model. This technique can be applied to
condition a network on any number, to provide fine control over generated
microstructure images, thereby contributing to accelerated materials design....

---

### 185. Optical materials discovery and design with federated databases and machine learning

**Authors:** Victor Trinquet, Matthew L. Evans, Cameron J. Hargreaves, Pierre-Paul De Breuck, Gian-Marco Rignanese

**Published:** 2024-05-18

**Category:** cond-mat.mtrl-sci

**ID:** 2405.11393v1

**Link:** [http://arxiv.org/abs/2405.11393v1](http://arxiv.org/abs/2405.11393v1)

**Summary:** Combinatorial and guided screening of materials space with density-functional
theory and related approaches has provided a wealth of hypothetical inorganic
materials, which are increasingly tabulated in open databases. The OPTIMADE API
is a standardised format for representing crystal structures, their measured
and computed properties, and the methods for querying and filtering them from
remote resources. Currently, the OPTIMADE federation spans over 20 data
providers, rendering over 30 million structures accessible in this way, many of
which are novel and have only recently been suggested by machine learning-based
approaches. In this work, we outline our approach to non-exhaustively screen
this dynamic trove of structures for the next-generation of optical materials.
By applying MODNet, a neural network-based model for property prediction,
within a combined active learning and high-throughput computation framework, we
isolate particular structures and chemistries that should be most fruitful for
further theoretical calculations and for experimental study as
high-refractive-index materials. By making explicit use of automated
calculations, federated dataset curation and machine learning, and by releasing
these publicly, the workflows presented here can be periodically re-assessed as
new databases implement OPTIMADE, and new hypothetical materials are suggested....

---

### 186. Towards Informatics-Driven Design of Nuclear Waste Forms

**Authors:** Vinay I. Hegde, Miroslava Peterson, Sarah I. Allec, Xiaonan Lu, Thiruvillamalai Mahadevan, Thanh Nguyen, Jayani Kalahe, Jared Oshiro, Robert J. Seffens, Ethan K. Nickerson, Jincheng Du, Brian J. Riley, John D. Vienna, James E. Saal

**Published:** 2024-05-16

**Category:** cond-mat.mtrl-sci

**ID:** 2405.09897v1

**Link:** [http://arxiv.org/abs/2405.09897v1](http://arxiv.org/abs/2405.09897v1)

**Summary:** Informatics-driven approaches, such as machine learning and sequential
experimental design, have shown the potential to drastically impact
next-generation materials discovery and design. In this perspective, we present
a few guiding principles for applying informatics-based methods towards the
design of novel nuclear waste forms. We advocate for adopting a system design
approach, and describe the effective usage of data-driven methods in every
stage of such a design process. We demonstrate how this approach can optimally
leverage physics-based simulations, machine learning surrogates, and
experimental synthesis and characterization, within a feedback-driven
closed-loop sequential learning framework. We discuss the importance of
incorporating domain knowledge into the representation of materials, the
construction and curation of datasets, the development of predictive property
models, and the design and execution of experiments. We illustrate the
application of this approach by successfully designing and validating Na- and
Nd-containing phosphate-based ceramic waste forms. Finally, we discuss open
challenges in such informatics-driven workflows and present an outlook for
their widespread application for the cleanup of nuclear wastes....

---

### 187. Materials Discovery with Extreme Properties via Reinforcement Learning-Guided Combinatorial Chemistry

**Authors:** Hyunseung Kim, Haeyeon Choi, Dongju Kang, Won Bo Lee, Jonggeol Na

**Published:** 2023-03-21

**Category:** q-bio.BM

**ID:** 2303.11833v2

**Link:** [http://arxiv.org/abs/2303.11833v2](http://arxiv.org/abs/2303.11833v2)

**Summary:** The goal of most materials discovery is to discover materials that are
superior to those currently known. Fundamentally, this is close to
extrapolation, which is a weak point for most machine learning models that
learn the probability distribution of data. Herein, we develop reinforcement
learning-guided combinatorial chemistry, which is a rule-based molecular
designer driven by trained policy for selecting subsequent molecular fragments
to get a target molecule. Since our model has the potential to generate all
possible molecular structures that can be obtained from combinations of
molecular fragments, unknown molecules with superior properties can be
discovered. We theoretically and empirically demonstrate that our model is more
suitable for discovering better compounds than probability
distribution-learning models. In an experiment aimed at discovering molecules
that hit seven extreme target properties, our model discovered 1,315 of all
target-hitting molecules and 7,629 of five target-hitting molecules out of
100,000 trials, whereas the probability distribution-learning models failed.
Moreover, it has been confirmed that every molecule generated under the binding
rules of molecular fragments is 100% chemically valid. To illustrate the
performance in actual problems, we also demonstrate that our models work well
on two practical applications: discovering protein docking molecules and HIV
inhibitors....

---

### 188. One Noise to Rule Them All: Learning a Unified Model of Spatially-Varying Noise Patterns

**Authors:** Arman Maesumi, Dylan Hu, Krishi Saripalli, Vladimir G. Kim, Matthew Fisher, Sören Pirk, Daniel Ritchie

**Published:** 2024-04-25

**Category:** cs.GR

**ID:** 2404.16292v1

**Link:** [http://arxiv.org/abs/2404.16292v1](http://arxiv.org/abs/2404.16292v1)

**Summary:** Procedural noise is a fundamental component of computer graphics pipelines,
offering a flexible way to generate textures that exhibit "natural" random
variation. Many different types of noise exist, each produced by a separate
algorithm. In this paper, we present a single generative model which can learn
to generate multiple types of noise as well as blend between them. In addition,
it is capable of producing spatially-varying noise blends despite not having
access to such data for training. These features are enabled by training a
denoising diffusion model using a novel combination of data augmentation and
network conditioning techniques. Like procedural noise generators, the model's
behavior is controllable via interpretable parameters and a source of
randomness. We use our model to produce a variety of visually compelling noise
textures. We also present an application of our model to improving inverse
procedural material design; using our model in place of fixed-type noise nodes
in a procedural material graph results in higher-fidelity material
reconstructions without needing to know the type of noise in advance....

---

### 189. A Genetic Algorithm For Convex Hull Optimisation

**Authors:** Scott Donaldson, Robert A. Lawrence, Matt I. J. Probert

**Published:** 2024-04-22

**Category:** cond-mat.mtrl-sci

**ID:** 2404.14354v1

**Link:** [http://arxiv.org/abs/2404.14354v1](http://arxiv.org/abs/2404.14354v1)

**Summary:** Computationally efficient and automated generation of convex hulls is
desirable for high throughput materials discovery of thermodynamically stable
multi-species crystal structures. A convex hull genetic algorithm is proposed
that uses methodology adapted from multi-objective optimisation techniques to
optimise the convex hull itself as an object, enabling efficient discovery of
convex hulls for N >= 2 species. This method, when tested on a LiSi system
utilising pre-trained machine learned potentials, was found to be able to
efficiently discover reported structures as well as new potential LiSi
candidate structures....

---

### 190. Extracting Geometry and Topology of Orange Pericarps for the Design of Bioinspired Energy Absorbing Materials

**Authors:** Chelsea Fox, Kyle Chen, Micaela Antonini, Tommaso Magrini, Chiara Daraio

**Published:** 2024-04-20

**Category:** cond-mat.mtrl-sci

**ID:** 2404.13351v1

**Link:** [http://arxiv.org/abs/2404.13351v1](http://arxiv.org/abs/2404.13351v1)

**Summary:** As a result of evolution, many biological materials have developed irregular
structures that lead to outstanding mechanical properties, like high
stiffness-to-weight ratios and good energy absorption. To reproduce these
properties in synthetic materials, biomimicry typically replicates the
irregular natural structure, often leading to fabrication challenges. Here, we
present a bioinspired material design method that instead reduces the irregular
natural structure to a finite set of building blocks, also known as tiles, and
rules to connect them, and then uses these elements as instructions to generate
synthetic materials with mechanical properties similar to the biological
materials. We demonstrate the method using the pericarp of the orange, a member
of the citrus family known for its protective, energy-absorbing capabilities.
We generate polymer samples and characterize them under quasi-static and
dynamic compression and observe spatially-varying stiffness and good energy
absorption, as seen in the biological materials. By quantifying which tiles and
connectivity rules locally deform in response to loading, we determine how to
spatially control the stiffness and energy absorption....

---

### 191. Dynamic Observation Policies in Observation Cost-Sensitive Reinforcement Learning

**Authors:** Colin Bellinger, Mark Crowley, Isaac Tamblyn

**Published:** 2023-07-05

**Category:** cs.LG

**ID:** 2307.02620v3

**Link:** [http://arxiv.org/abs/2307.02620v3](http://arxiv.org/abs/2307.02620v3)

**Summary:** Reinforcement learning (RL) has been shown to learn sophisticated control
policies for complex tasks including games, robotics, heating and cooling
systems and text generation. The action-perception cycle in RL, however,
generally assumes that a measurement of the state of the environment is
available at each time step without a cost. In applications such as materials
design, deep-sea and planetary robot exploration and medicine, however, there
can be a high cost associated with measuring, or even approximating, the state
of the environment. In this paper, we survey the recently growing literature
that adopts the perspective that an RL agent might not need, or even want, a
costly measurement at each time step. Within this context, we propose the Deep
Dynamic Multi-Step Observationless Agent (DMSOA), contrast it with the
literature and empirically evaluate it on OpenAI gym and Atari Pong
environments. Our results, show that DMSOA learns a better policy with fewer
decision steps and measurements than the considered alternative from the
literature....

---

### 192. Superior Polymeric Gas Separation Membrane Designed by Explainable Graph Machine Learning

**Authors:** Jiaxin Xu, Agboola Suleiman, Gang Liu, Michael Perez, Renzheng Zhang, Meng Jiang, Ruilan Guo, Tengfei Luo

**Published:** 2024-04-16

**Category:** cond-mat.mtrl-sci

**ID:** 2404.10903v1

**Link:** [http://arxiv.org/abs/2404.10903v1](http://arxiv.org/abs/2404.10903v1)

**Summary:** Gas separation using polymer membranes promises to dramatically drive down
the energy, carbon, and water intensity of traditional thermally driven
separation, but developing the membrane materials is challenging. Here, we
demonstrate a novel graph machine learning (ML) strategy to guide the
experimental discovery of synthesizable polymer membranes with performances
simultaneously exceeding the empirical upper bounds in multiple industrially
important gas separation tasks. Two predicted candidates are synthesized and
experimentally validated to perform beyond the upper bounds for multiple gas
pairs (O2/N2, H2/CH4, and H2/N2). Notably, the O2/N2 separation selectivity is
1.6-6.7 times higher than existing polymer membranes. The molecular origin of
the high performance is revealed by combining the inherent interpretability of
our ML model, experimental characterization, and molecule-level simulation. Our
study presents a unique explainable ML-experiment combination to tackle
challenging energy material design problems in general, and the discovered
polymers are beneficial for industrial gas separation....

---

### 193. ANTN: Bridging Autoregressive Neural Networks and Tensor Networks for Quantum Many-Body Simulation

**Authors:** Zhuo Chen, Laker Newhouse, Eddie Chen, Di Luo, Marin Soljačić

**Published:** 2023-04-04

**Category:** quant-ph

**ID:** 2304.01996v3

**Link:** [http://arxiv.org/abs/2304.01996v3](http://arxiv.org/abs/2304.01996v3)

**Summary:** Quantum many-body physics simulation has important impacts on understanding
fundamental science and has applications to quantum materials design and
quantum technology. However, due to the exponentially growing size of the
Hilbert space with respect to the particle number, a direct simulation is
intractable. While representing quantum states with tensor networks and neural
networks are the two state-of-the-art methods for approximate simulations, each
has its own limitations in terms of expressivity and inductive bias. To address
these challenges, we develop a novel architecture, Autoregressive Neural
TensorNet (ANTN), which bridges tensor networks and autoregressive neural
networks. We show that Autoregressive Neural TensorNet parameterizes normalized
wavefunctions, allows for exact sampling, generalizes the expressivity of
tensor networks and autoregressive neural networks, and inherits a variety of
symmetries from autoregressive neural networks. We demonstrate our approach on
quantum state learning as well as finding the ground state of the challenging
2D $J_1$-$J_2$ Heisenberg model with different systems sizes and coupling
parameters, outperforming both tensor networks and autoregressive neural
networks. Our work opens up new opportunities for quantum many-body physics
simulation, quantum technology design, and generative modeling in artificial
intelligence....

---

### 194. General theory for longitudinal nonreciprocal charge transport

**Authors:** Hong Jian Zhao, Lingling Tao, Yuhao Fu, Laurent Bellaiche, Yanming Ma

**Published:** 2024-04-15

**Category:** cond-mat.mtrl-sci

**ID:** 2404.10186v1

**Link:** [http://arxiv.org/abs/2404.10186v1](http://arxiv.org/abs/2404.10186v1)

**Summary:** The longitudinal nonreciprocal charge transport (NCT) in crystalline
materials is a highly non-trivial phenomenon, motivating the design of next
generation two-terminal rectification devices (e.g., semiconductor diodes
beyond PN junctions). The practical application of such devices is built upon
crystalline materials whose longitudinal NCT occurs at room temperature and
under low magnetic field. However, materials of this type are rather rare and
elusive, and theory guiding the discovery of these materials is lacking. Here,
we develop such a theory within the framework of semiclassical Boltzmann
transport theory. By symmetry analysis, we classify the complete 122 magnetic
point groups with respect to the longitudinal NCT phenomenon. The
symmetry-adapted Hamiltonian analysis further uncovers a previously overlooked
mechanism for this phenomenon. Our theory guides the first-principles
prediction of longitudinal NCT in multiferroic \epsilon-Fe2O3 semiconductor
that possibly occurs at room temperature, without the application of external
magnetic field. These findings advance our fundamental understandings of
longitudinal NCT in crystalline materials, and aid the corresponding materials
discoveries....

---

### 195. Universal Machine Learning Kohn-Sham Hamiltonian for Materials

**Authors:** Yang Zhong, Hongyu Yu, Jihui Yang, Xingyu Guo, Hongjun Xiang, Xingao Gong

**Published:** 2024-02-14

**Category:** physics.comp-ph

**ID:** 2402.09251v2

**Link:** [http://arxiv.org/abs/2402.09251v2](http://arxiv.org/abs/2402.09251v2)

**Summary:** While density functional theory (DFT) serves as a prevalent computational
approach in electronic structure calculations, its computational demands and
scalability limitations persist. Recently, leveraging neural networks to
parameterize the Kohn-Sham DFT Hamiltonian has emerged as a promising avenue
for accelerating electronic structure computations. Despite advancements,
challenges such as the necessity for computing extensive DFT training data to
explore each new system and the complexity of establishing accurate ML models
for multi-elemental materials still exist. Addressing these hurdles, this study
introduces a universal electronic Hamiltonian model trained on Hamiltonian
matrices obtained from first-principles DFT calculations of nearly all crystal
structures on the Materials Project. We demonstrate its generality in
predicting electronic structures across the whole periodic table, including
complex multi-elemental systems, solid-state electrolytes, Moir\'e twisted
bilayer heterostructure, and metal-organic frameworks (MOFs). Moreover, we
utilize the universal model to conduct high-throughput calculations of
electronic structures for crystals in GeNOME datasets, identifying 3,940
crystals with direct band gaps and 5,109 crystals with flat bands. By offering
a reliable efficient framework for computing electronic properties, this
universal Hamiltonian model lays the groundwork for advancements in diverse
fields, such as easily providing a huge data set of electronic structures and
also making the materials design across the whole periodic table possible....

---

### 196. A Prompt-Engineered Large Language Model, Deep Learning Workflow for Materials Classification

**Authors:** Siyu Liu, Tongqi Wen, A. S. L. Subrahmanyam Pattamatta, David J. Srolovitz

**Published:** 2024-01-31

**Category:** cond-mat.mtrl-sci

**ID:** 2401.17788v2

**Link:** [http://arxiv.org/abs/2401.17788v2](http://arxiv.org/abs/2401.17788v2)

**Summary:** Large language models (LLMs) have demonstrated rapid progress across a wide
array of domains. Owing to the very large number of parameters and training
data in LLMs, these models inherently encompass an expansive and comprehensive
materials knowledge database, far exceeding the capabilities of individual
researcher. Nonetheless, devising methods to harness the knowledge embedded
within LLMs for the design and discovery of novel materials remains a
formidable challenge. We introduce a general approach for addressing materials
classification problems, which incorporates LLMs, prompt engineering, and deep
learning. Utilizing a dataset of metallic glasses as a case study, our
methodology achieved an improvement of up to 463% in prediction accuracy
compared to conventional classification models. These findings underscore the
potential of leveraging textual knowledge generated by LLMs for materials
especially in the common situation where datasets are sparse, thereby promoting
innovation in materials discovery and design....

---

### 197. Efficient first principles based modeling via machine learning: from simple representations to high entropy materials

**Authors:** Kangming Li, Kamal Choudhary, Brian DeCost, Michael Greenwood, Jason Hattrick-Simpers

**Published:** 2024-03-22

**Category:** cond-mat.mtrl-sci

**ID:** 2403.15579v1

**Link:** [http://arxiv.org/abs/2403.15579v1](http://arxiv.org/abs/2403.15579v1)

**Summary:** High-entropy materials (HEMs) have recently emerged as a significant category
of materials, offering highly tunable properties. However, the scarcity of HEM
data in existing density functional theory (DFT) databases, primarily due to
computational expense, hinders the development of effective modeling strategies
for computational materials discovery. In this study, we introduce an open DFT
dataset of alloys and employ machine learning (ML) methods to investigate the
material representations needed for HEM modeling. Utilizing high-throughput DFT
calculations, we generate a comprehensive dataset of 84k structures,
encompassing both ordered and disordered alloys across a spectrum of up to
seven components and the entire compositional range. We apply descriptor-based
models and graph neural networks to assess how material information is captured
across diverse chemical-structural representations. We first evaluate the
in-distribution performance of ML models to confirm their predictive accuracy.
Subsequently, we demonstrate the capability of ML models to generalize between
ordered and disordered structures, between low-order and high-order alloys, and
between equimolar and non-equimolar compositions. Our findings suggest that ML
models can generalize from cost-effective calculations of simpler systems to
more complex scenarios. Additionally, we discuss the influence of dataset size
and reveal that the information loss associated with the use of unrelaxed
structures could significantly degrade the generalization performance. Overall,
this research sheds light on several critical aspects of HEM modeling and
offers insights for data-driven atomistic modeling of HEMs....

---

### 198. WyCryst: Wyckoff Inorganic Crystal Generator Framework

**Authors:** Ruiming Zhu, Wei Nong, Shuya Yamazaki, Kedar Hippalgaonkar

**Published:** 2023-11-29

**Category:** cond-mat.mtrl-sci

**ID:** 2311.17916v2

**Link:** [http://arxiv.org/abs/2311.17916v2](http://arxiv.org/abs/2311.17916v2)

**Summary:** Generative design marks a significant data-driven advancement in the
exploration of novel inorganic materials, which entails learning the symmetry
equivalent to the crystal structure prediction (CSP) task and subsequent
learning of their target properties. Generative models have been developed in
the last few years that use custom Variational Autoencoders (VAEs), Generative
Adversarial Networks (GANs), and diffusion models. While periodicity and global
Euclidian symmetry in three dimensions through translations, rotations and
reflections have recently been accounted for, symmetry constraints within
allowed space groups have not. This is especially important because the final
step involves energy relaxation on the generated crystal structures to find the
relaxed crystal structure, typically using Density Functional Theory (DFT). To
address this explicitly, we introduce a generative design framework (WyCryst),
composed of three pivotal components: 1) a Wyckoff position based inorganic
crystal representation, 2) a property-directed VAE model and 3) an automated
DFT workflow for structure refinement. Our model selectively generates
materials that follow the ground truth of unit cell space group symmetry by
encoding the Wyckoff representation for each space group. We successfully
reproduce a variety of existing materials: CaTiO3 (space group, SG No. 62 and
221), CsPbI3 (SG No. 221), BaTiO3 (SG No. 160), and CuInS2 (SG No.122) for both
ground state as well as polymorphic structure predictions. We also generate
several new ternary materials not found in the inorganic materials database
(Materials Project), which are proved to be stable, retaining their symmetry,
and we also check their phonon stability, using our automated DFT workflow
highlighting the validity of our approach. We believe our symmetry-aware
WyCryst takes a vital step towards AI-driven inorganic materials discovery....

---

### 199. QH9: A Quantum Hamiltonian Prediction Benchmark for QM9 Molecules

**Authors:** Haiyang Yu, Meng Liu, Youzhi Luo, Alex Strasser, Xiaofeng Qian, Xiaoning Qian, Shuiwang Ji

**Published:** 2023-06-15

**Category:** physics.chem-ph

**ID:** 2306.09549v4

**Link:** [http://arxiv.org/abs/2306.09549v4](http://arxiv.org/abs/2306.09549v4)

**Summary:** Supervised machine learning approaches have been increasingly used in
accelerating electronic structure prediction as surrogates of first-principle
computational methods, such as density functional theory (DFT). While numerous
quantum chemistry datasets focus on chemical properties and atomic forces, the
ability to achieve accurate and efficient prediction of the Hamiltonian matrix
is highly desired, as it is the most important and fundamental physical
quantity that determines the quantum states of physical systems and chemical
properties. In this work, we generate a new Quantum Hamiltonian dataset, named
as QH9, to provide precise Hamiltonian matrices for 999 or 2998 molecular
dynamics trajectories and 130,831 stable molecular geometries, based on the QM9
dataset. By designing benchmark tasks with various molecules, we show that
current machine learning models have the capacity to predict Hamiltonian
matrices for arbitrary molecules. Both the QH9 dataset and the baseline models
are provided to the community through an open-source benchmark, which can be
highly valuable for developing machine learning methods and accelerating
molecular and materials design for scientific and technological applications.
Our benchmark is publicly available at
https://github.com/divelab/AIRS/tree/main/OpenDFT/QHBench....

---

### 200. Energy-conserving equivariant GNN for elasticity of lattice architected metamaterials

**Authors:** Ivan Grega, Ilyes Batatia, Gábor Csányi, Sri Karlapati, Vikram S. Deshpande

**Published:** 2024-01-30

**Category:** cs.LG

**ID:** 2401.16914v2

**Link:** [http://arxiv.org/abs/2401.16914v2](http://arxiv.org/abs/2401.16914v2)

**Summary:** Lattices are architected metamaterials whose properties strongly depend on
their geometrical design. The analogy between lattices and graphs enables the
use of graph neural networks (GNNs) as a faster surrogate model compared to
traditional methods such as finite element modelling. In this work, we generate
a big dataset of structure-property relationships for strut-based lattices. The
dataset is made available to the community which can fuel the development of
methods anchored in physical principles for the fitting of fourth-order
tensors. In addition, we present a higher-order GNN model trained on this
dataset. The key features of the model are (i) SE(3) equivariance, and (ii)
consistency with the thermodynamic law of conservation of energy. We compare
the model to non-equivariant models based on a number of error metrics and
demonstrate its benefits in terms of predictive performance and reduced
training requirements. Finally, we demonstrate an example application of the
model to an architected material design task. The methods which we developed
are applicable to fourth-order tensors beyond elasticity such as piezo-optical
tensor etc....

---


<!-- ARXIV_PAPERS_END -->