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

## New Papers (6)

*Last updated: 2025-11-27 06:17:25 (SGT)*

### 1. Image2Gcode: Image-to-G-code Generation for Additive Manufacturing Using Diffusion-Transformer Model

**Authors:** Ziyue Wang, Yayati Jadhav, Peter Pak, Amir Barati Farimani

**Published:** 2025-11-25

**Category:** cs.LG

**ID:** 2511.20636v1

**Link:** [http://arxiv.org/abs/2511.20636v1](http://arxiv.org/abs/2511.20636v1)

**Summary:** Mechanical design and manufacturing workflows conventionally begin with conceptual design, followed by the creation of a computer-aided design (CAD) model and fabrication through material-extrusion (MEX) printing. This process requires converting CAD geometry into machine-readable G-code through slicing and path planning. While each step is well established, dependence on CAD modeling remains a major bottleneck: constructing object-specific 3D geometry is slow and poorly suited to rapid prototyping. Even minor design variations typically necessitate manual updates in CAD software, making iteration time-consuming and difficult to scale. To address this limitation, we introduce Image2Gcode, an end-to-end data-driven framework that bypasses the CAD stage and generates printer-ready G-code directly from images and part drawings. Instead of relying on an explicit 3D model, a hand-drawn or captured 2D image serves as the sole input. The framework first extracts slice-wise structural cues from the image and then employs a denoising diffusion probabilistic model (DDPM) over G-code sequences. Through iterative denoising, the model transforms Gaussian noise into executable print-move trajectories with corresponding extrusion parameters, establishing a direct mapping from visual input to native toolpaths. By producing structured G-code directly from 2D imagery, Image2Gcode eliminates the need for CAD or STL intermediates, lowering the entry barrier for additive manufacturing and accelerating the design-to-fabrication cycle. This approach supports on-demand prototyping from simple sketches or visual references and integrates with upstream 2D-to-3D reconstruction modules to enable an automated pipeline from concept to physical artifact. The result is a flexible, computationally efficient framework that advances accessibility in design iteration, repair workflows, and distributed manufacturing....

---

### 2. Universe of Thoughts: Enabling Creative Reasoning with Large Language Models

**Authors:** Yuto Suzuki, Farnoush Banaei-Kashani

**Published:** 2025-11-25

**Category:** cs.AI

**ID:** 2511.20471v1

**Link:** [http://arxiv.org/abs/2511.20471v1](http://arxiv.org/abs/2511.20471v1)

**Summary:** Reasoning based on Large Language Models (LLMs) has garnered increasing attention due to outstanding performance of these models in mathematical and complex logical tasks. Beginning with the Chain-of-Thought (CoT) prompting technique, numerous reasoning methods have emerged that decompose problems into smaller, sequential steps (or thoughts). However, existing reasoning models focus on conventional problem-solving and do not necessarily generate creative solutions by ``creative reasoning''. In domains where the solution space is expansive and conventional solutions are suboptimal, such as drug discovery or business strategization, creative reasoning to discover innovative solutions is crucial. To address this gap, first we introduce a computational framework for creative reasoning inspired by established cognitive science principles. With this framework, we propose three core creative reasoning paradigms, namely, \textit{combinational}, \textit{exploratory}, and \textit{transformative} reasoning, where each offers specific directions for systematic exploration of the universe of thoughts to generate creative solutions. Next, to materialize this framework using LLMs, we introduce the \textit{Universe of Thoughts} (or \textit{UoT}, for short), a novel set of methods to implement the aforementioned three creative processes. Finally, we introduce three novel tasks that necessitate creative problem-solving, along with an evaluation benchmark to assess creativity from three orthogonal perspectives: feasibility as constraint, and utility and novelty as metrics. With a comparative analysis against the state-of-the-art (SOTA) reasoning techniques as well as representative commercial models with reasoning capability, we show that UoT demonstrates superior performance in creative reasoning....

---

### 3. Diffusion for Fusion: Designing Stellarators with Generative AI

**Authors:** Misha Padidar, Teresa Huang, Andrew Giuliani, Marina Spivak

**Published:** 2025-11-25

**Category:** cs.LG

**ID:** 2511.20445v1

**Link:** [http://arxiv.org/abs/2511.20445v1](http://arxiv.org/abs/2511.20445v1)

**Summary:** Stellarators are a prospective class of fusion-based power plants that confine a hot plasma with three-dimensional magnetic fields. Typically framed as a PDE-constrained optimization problem, stellarator design is a time-consuming process that can take hours to solve on a computing cluster. Developing fast methods for designing stellarators is crucial for advancing fusion research. Given the recent development of large datasets of optimized stellarators, machine learning approaches have emerged as a potential candidate. Motivated by this, we present an open inverse problem to the machine learning community: to rapidly generate high-quality stellarator designs which have a set of desirable characteristics. As a case study in the problem space, we train a conditional diffusion model on data from the QUASR database to generate quasisymmetric stellarator designs with desirable characteristics (aspect ratio and mean rotational transform). The diffusion model is applied to design stellarators with characteristics not seen during training. We provide evaluation protocols and show that many of the generated stellarators exhibit solid performance: less than 5% deviation from quasisymmetry and the target characteristics. The modest deviation from quasisymmetry highlights an opportunity to reach the sub 1% target. Beyond the case study, we share multiple promising avenues for generative modeling to advance stellarator design....

---

### 4. KKL Observer Synthesis for Nonlinear Systems via Physics-Informed Learning

**Authors:** M. Umar B. Niazi, John Cao, Matthieu Barreau, Karl Henrik Johansson

**Published:** 2025-01-20

**Category:** eess.SY

**ID:** 2501.11655v2

**Link:** [http://arxiv.org/abs/2501.11655v2](http://arxiv.org/abs/2501.11655v2)

**Summary:** This paper proposes a novel learning approach for designing Kazantzis-Kravaris/Luenberger (KKL) observers for autonomous nonlinear systems. The design of a KKL observer involves finding an injective map that transforms the system state into a higher-dimensional observer state, whose dynamics is linear and stable. The observer's state is then mapped back to the original system coordinates via the inverse map to obtain the state estimate. However, finding this transformation and its inverse is quite challenging. We propose learning the forward mapping using a physics-informed neural network, and then learning its inverse mapping with a conventional feedforward neural network. Theoretical guarantees for the robustness of state estimation against approximation error and system uncertainties are provided, including non-asymptotic learning guarantees that link approximation quality to finite sample sizes. The effectiveness of the proposed approach is demonstrated through numerical simulations on benchmark examples, showing superior generalization capability outside the training domain compared to state-of-the-art methods....

---

### 5. iRadioDiff: Physics-Informed Diffusion Model for Indoor Radio Map Construction and Localization

**Authors:** Xiucheng Wang, Tingwei Yuan, Yang Cao, Nan Cheng, Ruijin Sun, Weihua Zhuang

**Published:** 2025-11-25

**Category:** cs.LG

**ID:** 2511.20015v1

**Link:** [http://arxiv.org/abs/2511.20015v1](http://arxiv.org/abs/2511.20015v1)

**Summary:** Radio maps (RMs) serve as environment-aware electromagnetic (EM) representations that connect scenario geometry and material properties to the spatial distribution of signal strength, enabling localization without costly in-situ measurements. However, constructing high-fidelity indoor RMs remains challenging due to the prohibitive latency of EM solvers and the limitations of learning-based methods, which often rely on sparse measurements or assumptions of homogeneous material, which are misaligned with the heterogeneous and multipath-rich nature of indoor environments. To overcome these challenges, we propose iRadioDiff, a sampling-free diffusion-based framework for indoor RM construction. iRadioDiff is conditioned on access point (AP) positions, and physics-informed prompt encoded by material reflection and transmission coefficients. It further incorporates multipath-critical priors, including diffraction points, strong transmission boundaries, and line-of-sight (LoS) contours, to guide the generative process via conditional channels and boundary-weighted objectives. This design enables accurate modeling of nonstationary field discontinuities and efficient construction of physically consistent RMs. Experiments demonstrate that iRadioDiff achieves state-of-the-art performance in indoor RM construction and received signal strength based indoor localization, which offers effective generalization across layouts and material configurations. Code is available at https://github.com/UNIC-Lab/iRadioDiff....

---

### 6. CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery

**Authors:** Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu, Wentao Li, Fankun Zeng, Siwei Fu, Hao Zhang, Xiaonan Wang

**Published:** 2025-11-23

**Category:** cond-mat.mtrl-sci

**ID:** 2511.19500v1

**Link:** [http://arxiv.org/abs/2511.19500v1](http://arxiv.org/abs/2511.19500v1)

**Summary:** Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials....

---


<!-- ARXIV_PAPERS_END -->