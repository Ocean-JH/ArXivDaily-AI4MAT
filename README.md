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

## New Papers (9)

*Last updated: 2025-12-05 06:16:27 (SGT)*

### 1. Machine Learning Pipeline for Denoising Low Signal-To-Noise Ratio and Out-of-Distribution Transmission Electron Microscopy Datasets

**Authors:** Brian Lee, Meng Li, Judith C Yang, Dmitri N Zakharov, Xiaohui Qu

**Published:** 2025-12-03

**Category:** cond-mat.mtrl-sci

**ID:** 2512.04045v1

**Link:** [http://arxiv.org/abs/2512.04045v1](http://arxiv.org/abs/2512.04045v1)

**Summary:** High-resolution transmission electron microscopy (HRTEM) is crucial for observing material's structural and morphological evolution at Angstrom scales, but the electron beam can alter these processes. Devices such as CMOS-based direct-electron detectors operating in electron-counting mode can be utilized to substantially reduce the electron dosage. However, the resulting images often lead to low signal-to-noise ratio, which requires frame integration that sacrifices temporal resolution. Several machine learning (ML) models have been recently developed to successfully denoise HRTEM images. Yet, these models are often computationally expensive and their inference speeds on GPUs are outpaced by the imaging speed of advanced detectors, precluding in situ analysis. Furthermore, the performance of these denoising models on datasets with imaging conditions that deviate from the training datasets have not been evaluated. To mitigate these gaps, we propose a new self-supervised ML denoising pipeline specifically designed for time-series HRTEM images. This pipeline integrates a blind-spot convolution neural network with pre-processing and post-processing steps including drift correction and low-pass filtering. Results demonstrate that our model outperforms various other ML and non-ML denoising methods in noise reduction and contrast enhancement, leading to improved visual clarity of atomic features. Additionally, the model is drastically faster than U-Net-based ML models and demonstrates excellent out-of-distribution generalization. The model's computational inference speed is in the order of milliseconds per image, rendering it suitable for application in in-situ HRTEM experiments....

---

### 2. Fast & Efficient Normalizing Flows and Applications of Image Generative Models

**Authors:** Sandeep Nagar

**Published:** 2025-12-03

**Category:** cs.CV

**ID:** 2512.04039v1

**Link:** [http://arxiv.org/abs/2512.04039v1](http://arxiv.org/abs/2512.04039v1)

**Summary:** This thesis presents novel contributions in two primary areas: advancing the efficiency of generative models, particularly normalizing flows, and applying generative models to solve real-world computer vision challenges. The first part introduce significant improvements to normalizing flow architectures through six key innovations: 1) Development of invertible 3x3 Convolution layers with mathematically proven necessary and sufficient conditions for invertibility, (2) introduction of a more efficient Quad-coupling layer, 3) Design of a fast and efficient parallel inversion algorithm for kxk convolutional layers, 4) Fast & efficient backpropagation algorithm for inverse of convolution, 5) Using inverse of convolution, in Inverse-Flow, for the forward pass and training it using proposed backpropagation algorithm, and 6) Affine-StableSR, a compact and efficient super-resolution model that leverages pre-trained weights and Normalizing Flow layers to reduce parameter count while maintaining performance.
  The second part: 1) An automated quality assessment system for agricultural produce using Conditional GANs to address class imbalance, data scarcity and annotation challenges, achieving good accuracy in seed purity testing; 2) An unsupervised geological mapping framework utilizing stacked autoencoders for dimensionality reduction, showing improved feature extraction compared to conventional methods; 3) We proposed a privacy preserving method for autonomous driving datasets using on face detection and image inpainting; 4) Utilizing Stable Diffusion based image inpainting for replacing the detected face and license plate to advancing privacy-preserving techniques and ethical considerations in the field.; and 5) An adapted diffusion model for art restoration that effectively handles multiple types of degradation through unified fine-tuning....

---

### 3. Influence of a generative parameter on the mechanical performance of topological interlocking assemblies of a hexagonal block

**Authors:** Lukas Schnelle, Meike Weiß, Reymond Akpanya, Kai-Uwe Schröder, Alice C. Niemeyer

**Published:** 2025-12-03

**Category:** cond-mat.mtrl-sci

**ID:** 2512.03941v1

**Link:** [http://arxiv.org/abs/2512.03941v1](http://arxiv.org/abs/2512.03941v1)

**Summary:** A topological interlocking assembly is an arrangement of blocks, where all blocks are kinematically constrained by their neighboring blocks and a fixed frame. This concept has been known for a long time, attracting recent interest due to its advantageous mechanical properties, such as reusability, redundancy and limited crack propagation. New mathematical methods enable the generation of vast numbers of new topologically interlocking blocks. A natural next question is the quantification of the mechanical performance of these new blocks. We conduct a numerical study of topological interlocking assemblies whose blocks are constructed based on the hexagonal grid. By varying a design parameter used in the generation of these blocks, we study its influence on the structural performance of the entire assembly. The results improve our understanding of the link between the block parameters and the mechanical performance. This enhances the ability to custom design blocks for certain mechanical requirements of the topological interlocking assemblies....

---

### 4. Evaluation of Foundational Machine Learned Interatomic Potentials for Migration Barrier Predictions

**Authors:** Achinthya Krishna Bheemaguli, Penghao Xiao, Gopalakrishnan Sai Gautam

**Published:** 2025-12-03

**Category:** cond-mat.mtrl-sci

**ID:** 2512.03642v1

**Link:** [http://arxiv.org/abs/2512.03642v1](http://arxiv.org/abs/2512.03642v1)

**Summary:** Fast, and accurate prediction of ionic migration barriers ($E_m$) is crucial for designing next-generation battery materials that combine high energy density with facile ion transport. Given the computational costs associated with estimating $E_m$ using conventional density functional theory (DFT) based nudged elastic band (NEB) calculations, we benchmark the accuracy in $E_m$ and geometry predictions of five foundational machine learned interatomic potentials (MLIPs), which can potentially accelerate predictions of ionic transport. Specifically, we assess the accuracy of MACE-MP-0, Orb-v3, SevenNet, CHGNet, and M3GNet models, coupled with the NEB framework, against DFT-NEB-calculated $E_m$ across a diverse set of battery-relevant chemistries and structures. Notably, MACE-MP-0 and Orb-v3 exhibit the lowest mean absolute errors in $E_m$ predictions across the entire dataset and over data points that are not outliers, respectively. Importantly, Orb-v3 and SevenNet classify `good' versus `bad' ionic conductors with an accuracy of $>$82\%, based on a threshold $E_m$ of 500~meV, indicating their utility in high-throughput screening approaches. Notably, intermediate images generated by MACE-MP-0 and SevenNet provide better initial guesses relative to conventional interpolation techniques in $>$71\% of structures, offering a practical route to accelerate subsequent DFT-NEB relaxations. Finally, we observe that accurate $E_m$ predictions by MLIPs are not correlated with accurate (local) geometry predictions. Our work establishes the use-cases, accuracies, and limitations of foundational MLIPs in estimating $E_m$ and should serve as a base for accelerating the discovery of novel ionic conductors for batteries and beyond....

---

### 5. Orbital Current-Driven Magnetization Switching in a Magnetic Tunnel Junction

**Authors:** Jingkai Xu, Dongxing Zheng, Meng Tang, Chen Liu, Bin He, Man Yang, Hao Li, Yan Li, Aitian Chen, Senfu Zhang, Ziqiang Qiu, Xixiang Zhang

**Published:** 2025-04-08

**Category:** cond-mat.mtrl-sci

**ID:** 2504.05780v2

**Link:** [http://arxiv.org/abs/2504.05780v2](http://arxiv.org/abs/2504.05780v2)

**Summary:** Spin-orbitronics, based on both spin and orbital angular momentum, presents a promising pathway for energy-efficient memory and logic devices. Recent studies have demonstrated the emergence of orbital currents in light transition metals such as Ti, Cr, and Zr, broadening the scope of spin-orbit torque (SOT). In particular, the orbital Hall effect, which arises independently of spin-obit coupling, has shown potential for enhancing torque efficiency in spintronic devices. However, the direct integration of orbital current into magnetic random-access memory (MRAM) remains unexplored. In this work, we design a light metal/heavy metal/ferromagnet multilayer structure and experimentally demonstrate magnetization switching by orbital current. Furthermore, we have realized a robust SOT-MRAM cell by incorporating a reference layer that is pinned by a synthetic antiferromagnetic structure. We observed a tunnel magnetoresistance of 66%, evident in both magnetic field and current-driven switching processes. Our findings underscore the potential for employing orbital current in designing next-generation spintronic devices....

---

### 6. Physics-Driven Learning Framework for Tomographic Tactile Sensing

**Authors:** Xuanxuan Yang, Xiuyang Zhang, Haofeng Chen, Gang Ma, Xiaojie Wang

**Published:** 2025-12-03

**Category:** cs.LG

**ID:** 2512.03512v1

**Link:** [http://arxiv.org/abs/2512.03512v1](http://arxiv.org/abs/2512.03512v1)

**Summary:** Electrical impedance tomography (EIT) provides an attractive solution for large-area tactile sensing due to its minimal wiring and shape flexibility, but its nonlinear inverse problem often leads to severe artifacts and inaccurate contact reconstruction. This work presents PhyDNN, a physics-driven deep reconstruction framework that embeds the EIT forward model directly into the learning objective. By jointly minimizing the discrepancy between predicted and ground-truth conductivity maps and enforcing consistency with the forward PDE, PhyDNN reduces the black-box nature of deep networks and improves both physical plausibility and generalization. To enable efficient backpropagation, we design a differentiable forward-operator network that accurately approximates the nonlinear EIT response, allowing fast physics-guided training. Extensive simulations and real tactile experiments on a 16-electrode soft sensor show that PhyDNN consistently outperforms NOSER, TV, and standard DNNs in reconstructing contact shape, location, and pressure distribution. PhyDNN yields fewer artifacts, sharper boundaries, and higher metric scores, demonstrating its effectiveness for high-quality tomographic tactile sensing....

---

### 7. MACS: Measurement-Aware Consistency Sampling for Inverse Problems

**Authors:** Amirreza Tanevardi, Pooria Abbas Rad Moghadam, Seyed Mohammad Eshtehardian, Sajjad Amini, Babak Khalaj

**Published:** 2025-10-02

**Category:** eess.IV

**ID:** 2510.02208v2

**Link:** [http://arxiv.org/abs/2510.02208v2](http://arxiv.org/abs/2510.02208v2)

**Summary:** Diffusion models have emerged as powerful generative priors for solving inverse imaging problems. However, their practical deployment is hindered by the substantial computational cost of slow, multi-step sampling. Although Consistency Models (CMs) address this limitation by enabling high-quality generation in only one or a few steps, their direct application to inverse problems has remained largely unexplored. This paper introduces a modified consistency sampling framework specifically designed for inverse problems. The proposed approach regulates the sampler's stochasticity through a measurement-consistency mechanism that leverages the degradation operator, thereby enforcing fidelity to the observed data while preserving the computational efficiency of consistency-based generation. Comprehensive experiments on the Fashion-MNIST and LSUN Bedroom datasets demonstrate consistent improvements across both perceptual and pixel-level metrics, including the Fréchet Inception Distance (FID), Kernel Inception Distance (KID), peak signal-to-noise ratio (PSNR), and structural similarity index measure (SSIM), compared with baseline consistency and diffusion-based sampling methods. The proposed method achieves competitive or superior reconstruction quality with only a small number of sampling steps....

---

### 8. Hierarchical Deep Research with Local-Web RAG: Toward Automated System-Level Materials Discovery

**Authors:** Rui Ding, Rodrigo Pires Ferreira, Yuxin Chen, Junhong Chen

**Published:** 2025-11-23

**Category:** cs.LG

**ID:** 2511.18303v2

**Link:** [http://arxiv.org/abs/2511.18303v2](http://arxiv.org/abs/2511.18303v2)

**Summary:** We present a long-horizon, hierarchical deep research (DR) agent designed for complex materials and device discovery problems that exceed the scope of existing Machine Learning (ML) surrogates and closed-source commercial agents. Our framework instantiates a locally deployable DR instance that integrates local retrieval-augmented generation with large language model reasoners, enhanced by a Deep Tree of Research (DToR) mechanism that adaptively expands and prunes research branches to maximize coverage, depth, and coherence. We systematically evaluate across 27 nanomaterials/device topics using a large language model (LLM)-as-judge rubric with five web-enabled state-of-the-art models as jurors. In addition, we conduct dry-lab validations on five representative tasks, where human experts use domain simulations (e.g., density functional theory, DFT) to verify whether DR-agent proposals are actionable. Results show that our DR agent produces reports with quality comparable to--and often exceeding--those of commercial systems (ChatGPT-5-thinking/o3/o4-mini-high Deep Research) at a substantially lower cost, while enabling on-prem integration with local data and tools....

---

### 9. Physics-Informed Machine Learning for Steel Development: A Computational Framework and CCT Diagram Modelling

**Authors:** Peter Hedström, Victor Lamelas Cubero, Jón Sigurdsson, Viktor Österberg, Satish Kolli, Joakim Odqvist, Ziyong Hou, Wangzhong Mu, Viswanadh Gowtham Arigela

**Published:** 2025-11-21

**Category:** cs.LG

**ID:** 2512.03050v1

**Link:** [http://arxiv.org/abs/2512.03050v1](http://arxiv.org/abs/2512.03050v1)

**Summary:** Machine learning (ML) has emerged as a powerful tool for accelerating the computational design and production of materials. In materials science, ML has primarily supported large-scale discovery of novel compounds using first-principles data and digital twin applications for optimizing manufacturing processes. However, applying general-purpose ML frameworks to complex industrial materials such as steel remains a challenge. A key obstacle is accurately capturing the intricate relationship between chemical composition, processing parameters, and the resulting microstructure and properties. To address this, we introduce a computational framework that combines physical insights with ML to develop a physics-informed continuous cooling transformation (CCT) model for steels. Our model, trained on a dataset of 4,100 diagrams, is validated against literature and experimental data. It demonstrates high computational efficiency, generating complete CCT diagrams with 100 cooling curves in under 5 seconds. It also shows strong generalizability across alloy steels, achieving phase classification F1 scores above 88% for all phases. For phase transition temperature regression, it attains mean absolute errors (MAE) below 20 °C across all phases except bainite, which shows a slightly higher MAE of 27 °C. This framework can be extended with additional generic and customized ML models to establish a universal digital twin platform for heat treatment. Integration with complementary simulation tools and targeted experiments will further support accelerated materials design workflows....

---


<!-- ARXIV_PAPERS_END -->