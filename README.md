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

## New Papers (16)

*Last updated: 2025-11-19 06:18:15 (SGT)*

### 1. Artificial Intelligence-driven Intelligent Wearable Systems: A full-stack Integration from Material Design to Personalized Interaction

**Authors:** Jingyi Zhao, Daqian Shi, Zhengda Wang, Xiongfeng Tang, Yanguo Qin

**Published:** 2025-11-17

**Category:** cs.AI

**ID:** 2511.13565v1

**Link:** [http://arxiv.org/abs/2511.13565v1](http://arxiv.org/abs/2511.13565v1)

**Summary:** Intelligent wearable systems are at the forefront of precision medicine and play a crucial role in enhancing human-machine interaction. Traditional devices often encounter limitations due to their dependence on empirical material design and basic signal processing techniques. To overcome these issues, we introduce the concept of Human-Symbiotic Health Intelligence (HSHI), which is a framework that integrates multi-modal sensor networks with edge-cloud collaborative computing and a hybrid approach to data and knowledge modeling. HSHI is designed to adapt dynamically to both inter-individual and intra-individual variability, transitioning health management from passive monitoring to an active collaborative evolution. The framework incorporates AI-driven optimization of materials and micro-structures, provides robust interpretation of multi-modal signals, and utilizes a dual mechanism that merges population-level insights with personalized adaptations. Moreover, the integration of closed-loop optimization through reinforcement learning and digital twins facilitates customized interventions and feedback. In general, HSHI represents a significant shift in healthcare, moving towards a model that emphasizes prevention, adaptability, and a harmonious relationship between technology and health management....

---

### 2. CDFlow: Building Invertible Layers with Circulant and Diagonal Matrices

**Authors:** Xuchen Feng, Siyu Liao

**Published:** 2025-10-29

**Category:** cs.LG

**ID:** 2510.25323v3

**Link:** [http://arxiv.org/abs/2510.25323v3](http://arxiv.org/abs/2510.25323v3)

**Summary:** Normalizing flows are deep generative models that enable efficient likelihood estimation and sampling through invertible transformations. A key challenge is to design linear layers that enhance expressiveness while maintaining efficient computation of the Jacobian determinant and inverse. We introduce a novel invertible linear layer based on the product of circulant and diagonal matrices. This decomposition reduces parameter complexity from $\mathcal{O}(n^2)$ to $\mathcal{O}(mn)$ using $m$ diagonal matrices and $m-1$ circulant matrices while still approximating general linear transformations. By leveraging the Fast Fourier Transform, our approach reduces the time complexity of matrix inversion from $\mathcal{O}(n^3)$ to $\mathcal{O}(mn\log n)$ and that of computing the log-determinant from $\mathcal{O}(n^3)$ to $\mathcal{O}(mn)$, where $n$ is the input dimension. We build upon this layer to develop Circulant-Diagonal Flow (CDFlow), which achieves strong density estimation on natural image datasets and effectively models data with inherent periodic structure. Furthermore, CDFlow significantly accelerates key operations in normalizing flows, providing practical benefits for scalable generative modeling....

---

### 3. NuBench: An Open Benchmark for Deep Learning-Based Event Reconstruction in Neutrino Telescopes

**Authors:** Rasmus F. Orsoe, Stephan Meighen-Berger, Jeffrey Lazar, Jorge Prado, Ivan Mozun-Mateo, Aske Rosted, Philip Weigel, Arturo Llorente Anaya

**Published:** 2025-11-17

**Category:** hep-ex

**ID:** 2511.13111v1

**Link:** [http://arxiv.org/abs/2511.13111v1](http://arxiv.org/abs/2511.13111v1)

**Summary:** Neutrino telescopes are large-scale detectors designed to observe Cherenkov radiation produced from neutrino interactions in water or ice. They exist to identify extraterrestrial neutrino sources and to probe fundamental questions pertaining to the elusive neutrino itself. A central challenge common across neutrino telescopes is to solve a series of inverse problems known as event reconstruction, which seeks to resolve properties of the incident neutrino, based on the detected Cherenkov light. In recent times, significant efforts have been made in adapting advances from deep learning research to event reconstruction, as such techniques provide several benefits over traditional methods. While a large degree of similarity in reconstruction needs and low-level data exists, cross-experimental collaboration has been hindered by a lack of diverse open-source datasets for comparing methods.
  We present NuBench, an open benchmark for deep learning-based event reconstruction in neutrino telescopes. NuBench comprises seven large-scale simulated datasets containing nearly 130 million charged- and neutral-current muon-neutrino interactions spanning 10 GeV to 100 TeV, generated across six detector geometries inspired by existing and proposed experiments. These datasets provide pulse- and event-level information suitable for developing and comparing machine-learning reconstruction methods in both water and ice environments. Using NuBench, we evaluate four reconstruction algorithms - ParticleNeT and DynEdge, both actively used within the KM3NeT and IceCube collaborations, respectively, along with GRIT and DeepIce - on up to five core tasks: energy and direction reconstruction, topology classification, interaction vertex prediction, and inelasticity estimation....

---

### 4. On Geometric Structures for Policy Parameterization in Continuous Control

**Authors:** Zhihao Lin

**Published:** 2025-11-11

**Category:** cs.AI

**ID:** 2511.08234v2

**Link:** [http://arxiv.org/abs/2511.08234v2](http://arxiv.org/abs/2511.08234v2)

**Summary:** Standard stochastic policies for continuous control often rely on ad-hoc boundary-enforcing transformations (e.g., tanh) which can distort the underlying optimization landscape and introduce gradient pathologies. While alternative parameterizations on the unit manifold (e.g., directional distributions) are theoretically appealing, their computational complexity (often requiring special functions or rejection sampling) has limited their practical use. We propose a novel, computationally efficient action generation paradigm that preserves the structural benefits of operating on a unit manifold. Our method decomposes the action into a deterministic directional vector and a learnable concentration scalar, enabling efficient interpolation between the target direction and uniform noise on the unit manifold. This design can reduce policy head parameters by nearly 50\% (from $2d$ to $d+1$) and maintains a simple $O(d)$ sampling complexity, avoiding costly sampling procedures. Empirically, our method matches or exceeds state-of-the-art methods on standard continuous control benchmarks, with significant improvements (e.g., +37.6\% and +112\%) on high-dimensional locomotion tasks. Ablation studies confirm that both the unit-norm normalization and the adaptive concentration mechanism are essential to the method's success. These findings suggest that robust, efficient control can be achieved by explicitly respecting the structure of bounded action spaces, rather than relying on complex, unbounded distributions. Code is available in supplementary materials....

---

### 5. MolEdit: Knowledge Editing for Multimodal Molecule Language Models

**Authors:** Zhenyu Lei, Patrick Soga, Yaochen Zhu, Yinhan He, Yushun Dong, Jundong Li

**Published:** 2025-11-16

**Category:** cs.LG

**ID:** 2511.12770v1

**Link:** [http://arxiv.org/abs/2511.12770v1](http://arxiv.org/abs/2511.12770v1)

**Summary:** Understanding and continuously refining multimodal molecular knowledge is crucial for advancing biomedicine, chemistry, and materials science. Molecule language models (MoLMs) have become powerful tools in these domains, integrating structural representations (e.g., SMILES strings, molecular graphs) with rich contextual descriptions (e.g., physicochemical properties). However, MoLMs can encode and propagate inaccuracies due to outdated web-mined training corpora or malicious manipulation, jeopardizing downstream discovery pipelines. While knowledge editing has been explored for general-domain AI, its application to MoLMs remains uncharted, presenting unique challenges due to the multifaceted and interdependent nature of molecular knowledge. In this paper, we take the first step toward MoLM editing for two critical tasks: molecule-to-caption generation and caption-to-molecule generation. To address molecule-specific challenges, we propose MolEdit, a powerful framework that enables targeted modifications while preserving unrelated molecular knowledge. MolEdit combines a Multi-Expert Knowledge Adapter that routes edits to specialized experts for different molecular facets with an Expertise-Aware Editing Switcher that activates the adapters only when input closely matches the stored edits across all expertise, minimizing interference with unrelated knowledge. To systematically evaluate editing performance, we introduce MEBench, a comprehensive benchmark assessing multiple dimensions, including Reliability (accuracy of the editing), Locality (preservation of irrelevant knowledge), and Generality (robustness to reformed queries). Across extensive experiments on two popular MoLM backbones, MolEdit delivers up to 18.8% higher Reliability and 12.0% better Locality than baselines while maintaining efficiency. The code is available at: https://github.com/LzyFischer/MolEdit....

---

### 6. AI Bill of Materials and Beyond: Systematizing Security Assurance through the AI Risk Scanning (AIRS) Framework

**Authors:** Samuel Nathanson, Alexander Lee, Catherine Chen Kieffer, Jared Junkin, Jessica Ye, Amir Saeed, Melanie Lockhart, Russ Fink, Elisha Peterson, Lanier Watkins

**Published:** 2025-11-16

**Category:** cs.CR

**ID:** 2511.12668v1

**Link:** [http://arxiv.org/abs/2511.12668v1](http://arxiv.org/abs/2511.12668v1)

**Summary:** Assurance for artificial intelligence (AI) systems remains fragmented across software supply-chain security, adversarial machine learning, and governance documentation. Existing transparency mechanisms - including Model Cards, Datasheets, and Software Bills of Materials (SBOMs) - advance provenance reporting but rarely provide verifiable, machine-readable evidence of model security. This paper introduces the AI Risk Scanning (AIRS) Framework, a threat-model-based, evidence-generating framework designed to operationalize AI assurance. The AIRS Framework evolved through three progressive pilot studies - Smurf (AIBOM schema design), OPAL (operational validation), and Pilot C (AIRS) - that reframed AI documentation from descriptive disclosure toward measurable, evidence-bound verification. The framework aligns its assurance fields to the MITRE ATLAS adversarial ML taxonomy and automatically produces structured artifacts capturing model integrity, packaging and serialization safety, structural adapters, and runtime behaviors. Currently, the AIRS Framework is scoped to provide model-level assurances for LLMs, but it could be expanded to include other modalities and cover system-level threats (e.g. application-layer abuses, tool-calling). A proof-of-concept on a quantized GPT-OSS-20B model demonstrates enforcement of safe loader policies, per-shard hash verification, and contamination and backdoor probes executed under controlled runtime conditions. Comparative analysis with SBOM standards of SPDX 3.0 and CycloneDX 1.6 reveals alignment on identity and evaluation metadata, but identifies critical gaps in representing AI-specific assurance fields. The AIRS Framework thus extends SBOM practice to the AI domain by coupling threat modeling with automated, auditable evidence generation, providing a principled foundation for standardized, trustworthy, and machine-verifiable AI risk documentation....

---

### 7. Small Models, Big Support: A Local LLM Framework for Educator-Centric Content Creation and Assessment with RAG and CAG

**Authors:** Zarreen Reza, Alexander Mazur, Michael T. Dugdale, Robin Ray-Chaudhuri

**Published:** 2025-06-06

**Category:** cs.CY

**ID:** 2506.05925v2

**Link:** [http://arxiv.org/abs/2506.05925v2](http://arxiv.org/abs/2506.05925v2)

**Summary:** While Large Language Models (LLMs) are increasingly applied in student-facing educational tools, their potential to directly support educators through locally deployable and customizable solutions remains underexplored. Many existing approaches rely on proprietary, cloud-based systems that raise significant cost, privacy, and control concerns for educational institutions. To address these barriers, we introduce an end-to-end, open-source framework that empowers educators using small (3B-7B parameter), locally deployable LLMs. Our system is designed for comprehensive teacher support, including customized teaching material generation and AI-assisted assessment. The framework synergistically combines Retrieval-Augmented Generation (RAG) and Context-Augmented Generation (CAG) to produce factually accurate, pedagogically-styled content. A core feature is an interactive refinement loop, a teacher-in-the-loop mechanism that ensures educator agency and precise alignment of the final output. To enhance reliability and safety, an auxiliary verifier LLM inspects all generated content. We validate our framework through a rigorous evaluation of its content generation capabilities and report on a successful technical deployment in a college physics course, which confirms its feasibility on standard institutional hardware. Our findings demonstrate that carefully engineered, self-hosted systems built on small LLMs can provide robust, affordable, and private support for educators, achieving practical utility comparable to much larger models for targeted instructional tasks. This work presents a practical blueprint for the development of sovereign AI tools tailored to the real-world needs of educational institutions....

---

### 8. Parameter-aware high-fidelity microstructure generation using stable diffusion

**Authors:** Hoang Cuong Phan, Minh Tien Tran, Chihun Lee, Hoheok Kim, Sehyeok Oh, Dong-Kyu Kim, Ho Won Lee

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00459v2

**Link:** [http://arxiv.org/abs/2507.00459v2](http://arxiv.org/abs/2507.00459v2)

**Summary:** Synthesizing realistic microstructure images conditioned on processing parameters is crucial for understanding process-structure relationships in materials design. However, this task remains challenging due to limited training micrographs and the continuous nature of processing variables. To overcome these challenges, we present a novel process-aware generative modeling approach based on Stable Diffusion 3.5 Large (SD3.5-Large), a state-of-the-art text-to-image diffusion model adapted for microstructure generation. Our method introduces numeric-aware embeddings that encode continuous variables (annealing temperature, time, and magnification) directly into the model's conditioning, enabling controlled image generation under specified process conditions and capturing process-driven microstructural variations. To address data scarcity and computational constraints, we fine-tune only a small fraction of the model's weights via DreamBooth and Low-Rank Adaptation (LoRA), efficiently transferring the pre-trained model to the materials domain. We validate realism using a semantic segmentation model based on a fine-tuned U-Net with a VGG16 encoder on 24 labeled micrographs. It achieves 97.1% accuracy and 85.7% mean IoU, outperforming previous methods. Quantitative analyses using physical descriptors and spatial statistics show strong agreement between synthetic and real microstructures. Specifically, two-point correlation and lineal-path errors remain below 2.1% and 0.6%, respectively. Our method represents the first adaptation of SD3.5-Large for process-aware microstructure generation, offering a scalable approach for data-driven materials design....

---

### 9. Chemical-space completeness: a new strategy for crystalline materials exploration

**Authors:** Fengyu Xie, Ruoyu Wang, Taoyuze Lv, Yuxiang Gao, Hongyu Wu, Zhicheng Zhong

**Published:** 2025-11-16

**Category:** cond-mat.mtrl-sci

**ID:** 2511.12420v1

**Link:** [http://arxiv.org/abs/2511.12420v1](http://arxiv.org/abs/2511.12420v1)

**Summary:** The emergence of deep learning has brought the long-standing goal of comprehensively understanding and exploring crystalline materials closer to reality. Yet, universal exploration across all elements remains hindered by the combinatorial explosion of possible chemical environments, making it difficult to balance accuracy and efficiency. Crucially, within any finite set of elements, the diversity of short-range bonding types and local geometric motifs is inherently limited. Guided by this chemical intuition, we propose a chemical-system-centric strategy for crystalline materials exploration. In this framework, generative models are coupled with machine-learned force fields as fast energy evaluators, and both are iteratively refined in a closed-loop cycle of generation, evaluation, and fine-tuning. Using the Li-P-S ternary system as a case study, we show that this approach captures the diversity of local environments with minimal additional first-principles data while maintaining structural creativity, achieving closed-loop convergence toward chemical completeness within a bounded chemical space. We further demonstrate downstream applications, including phase-diagram construction, ionic-diffusivity screening, and electronic-structure prediction. Together, this strategy provides a systematic and data-efficient framework for modeling both atomistic and electronic structures within defined chemical spaces, bridging accuracy and efficiency, and paving the way toward scalable, AI-driven discovery of crystalline materials with human-level creativity and first-principles fidelity....

---

### 10. Model Inversion Attack Against Deep Hashing

**Authors:** Dongdong Zhao, Qiben Xu, Ranxin Fang, Baogang Song

**Published:** 2025-11-15

**Category:** cs.CV

**ID:** 2511.12233v1

**Link:** [http://arxiv.org/abs/2511.12233v1](http://arxiv.org/abs/2511.12233v1)

**Summary:** Deep hashing improves retrieval efficiency through compact binary codes, yet it introduces severe and often overlooked privacy risks. The ability to reconstruct original training data from hash codes could lead to serious threats such as biometric forgery and privacy breaches. However, model inversion attacks specifically targeting deep hashing models remain unexplored, leaving their security implications unexamined. This research gap stems from the inaccessibility of genuine training hash codes and the highly discrete Hamming space, which prevents existing methods from adapting to deep hashing. To address these challenges, we propose DHMI, the first diffusion-based model inversion framework designed for deep hashing. DHMI first clusters an auxiliary dataset to derive semantic hash centers as surrogate anchors. It then introduces a surrogate-guided denoising optimization method that leverages a novel attack metric (fusing classification consistency and hash proximity) to dynamically select candidate samples. A cluster of surrogate models guides the refinement of these candidates, ensuring the generation of high-fidelity and semantically consistent images. Experiments on multiple datasets demonstrate that DHMI successfully reconstructs high-resolution, high-quality images even under the most challenging black-box setting, where no training hash codes are available. Our method outperforms the existing state-of-the-art model inversion attacks in black-box scenarios, confirming both its practical efficacy and the critical privacy risks inherent in deep hashing systems....

---

### 11. FGM optimization in complex domains using Gaussian process regression based profile generation algorithm

**Authors:** Chaitanya Kumar Konda, Piyush Agrawal, Shivansh Srivastava, Manish Agrawal

**Published:** 2025-11-15

**Category:** cs.LG

**ID:** 2511.12171v1

**Link:** [http://arxiv.org/abs/2511.12171v1](http://arxiv.org/abs/2511.12171v1)

**Summary:** This manuscript addresses the challenge of designing functionally graded materials (FGMs) for arbitrary-shaped domains. Towards this goal, the present work proposes a generic volume fraction profile generation algorithm based on Gaussian Process Regression (GPR). The proposed algorithm can handle complex-shaped domains and generate smooth FGM profiles while adhering to the specified volume fraction values at boundaries/part of boundaries. The resulting design space from GPR comprises diverse profiles, enhancing the potential for discovering optimal configurations. Further, the algorithm allows the user to control the smoothness of the underlying profiles and the size of the design space through a length scale parameter. Further, the proposed profile generation scheme is coupled with the genetic algorithm to find the optimum FGM profiles for a given application. To make the genetic algorithm consistent with the GPR profile generation scheme, the standard simulated binary crossover operator in the genetic algorithm has been modified with a projection operator. We present numerous thermoelastic optimization examples to demonstrate the efficacy of the proposed profile generation algorithm and optimization framework....

---

### 12. RTMol: Rethinking Molecule-text Alignment in a Round-trip View

**Authors:** Letian Chen, Runhan Shi, Gufeng Yu, Yang Yang

**Published:** 2025-11-15

**Category:** cs.AI

**ID:** 2511.12135v1

**Link:** [http://arxiv.org/abs/2511.12135v1](http://arxiv.org/abs/2511.12135v1)

**Summary:** Aligning molecular sequence representations (e.g., SMILES notations) with textual descriptions is critical for applications spanning drug discovery, materials design, and automated chemical literature analysis. Existing methodologies typically treat molecular captioning (molecule-to-text) and text-based molecular design (text-to-molecule) as separate tasks, relying on supervised fine-tuning or contrastive learning pipelines. These approaches face three key limitations: (i) conventional metrics like BLEU prioritize linguistic fluency over chemical accuracy, (ii) training datasets frequently contain chemically ambiguous narratives with incomplete specifications, and (iii) independent optimization of generation directions leads to bidirectional inconsistency. To address these issues, we propose RTMol, a bidirectional alignment framework that unifies molecular captioning and text-to-SMILES generation through self-supervised round-trip learning. The framework introduces novel round-trip evaluation metrics and enables unsupervised training for molecular captioning without requiring paired molecule-text corpora. Experiments demonstrate that RTMol enhances bidirectional alignment performance by up to 47% across various LLMs, establishing an effective paradigm for joint molecule-text understanding and generation....

---

### 13. Preference Learning from Physics-Based Feedback: Tuning Language Models to Design BCC/B2 Superalloys

**Authors:** Satanu Ghosh, Collin Holgate, Neal R. Brodnik, Doug Downey, Samantha Daly, Tresa M. Pollock, Samuel Carton

**Published:** 2025-11-15

**Category:** cs.CE

**ID:** 2511.12036v1

**Link:** [http://arxiv.org/abs/2511.12036v1](http://arxiv.org/abs/2511.12036v1)

**Summary:** We apply preference learning to the task of language model-guided design of novel structural alloys. In contrast to prior work that focuses on generating stable inorganic crystals, our approach targets the synthesizeability of a specific structural class: BCC/B2 superalloys, an underexplored family of materials with potential applications in extreme environments. Using three open-weight models (LLaMA-3.1, Gemma-2, and OLMo-2), we demonstrate that language models can be optimized for multiple design objectives using a single, unified reward signal through Direct Preference Optimization (DPO). Unlike prior approaches that rely on heuristic or human-in-the-loop feedback (costly), our reward signal is derived from thermodynamic phase calculations, offering a scientifically grounded criterion for model tuning. To our knowledge, this is the first demonstration of preference-tuning a language model using physics-grounded feedback for structural alloy design. The resulting framework is general and extensible, providing a path forward for intelligent design-space exploration across a range of physical science domains....

---

### 14. Language Model Distillation: A Temporal Difference Imitation Learning Perspective

**Authors:** Zishun Yu, Shangzhe Li, Xinhua Zhang

**Published:** 2025-05-24

**Category:** cs.CL

**ID:** 2505.20335v3

**Link:** [http://arxiv.org/abs/2505.20335v3](http://arxiv.org/abs/2505.20335v3)

**Summary:** Large language models have led to significant progress across many NLP tasks, although their massive sizes often incur substantial computational costs. Distillation has become a common practice to compress these large and highly capable models into smaller, more efficient ones. Many existing language model distillation methods can be viewed as behavior cloning from the perspective of imitation learning or inverse reinforcement learning. This viewpoint has inspired subsequent studies that leverage (inverse) reinforcement learning techniques, including variations of behavior cloning and temporal difference learning methods. Rather than proposing yet another specific temporal difference method, we introduce a general framework for temporal difference-based distillation by exploiting the distributional sparsity of the teacher model. Specifically, it is often observed that language models assign most probability mass to a small subset of tokens. Motivated by this observation, we design a temporal difference learning framework that operates on a reduced action space (a subset of vocabulary), and demonstrate how practical algorithms can be derived and the resulting performance improvements....

---

### 15. Regularized Schrödinger: Alleviating Distortion and Exposure Bias in Solving Inverse Problems

**Authors:** Qing Yao, Lijian Gao, Qirong Mao, Dong Ming

**Published:** 2025-11-12

**Category:** cs.LG

**ID:** 2511.11686v1

**Link:** [http://arxiv.org/abs/2511.11686v1](http://arxiv.org/abs/2511.11686v1)

**Summary:** Diffusion models serve as a powerful generative framework for solving inverse problems. However, they still face two key challenges: 1) the distortion-perception tradeoff, where improving perceptual quality often degrades reconstruction fidelity, and 2) the exposure bias problem, where the training-inference input mismatch leads to prediction error accumulation and reduced reconstruction quality. In this work, we propose the Regularized Schrödinger Bridge (RSB), an adaptation of Schrödinger Bridge tailored for inverse problems that addresses the above limitations. RSB employs a novel regularized training strategy that perturbs both the input states and targets, effectively mitigating exposure bias by exposing the model to simulated prediction errors and also alleviating distortion by well-designed interpolation via the posterior mean. Extensive experiments on two typical inverse problems for speech enhancement demonstrate that RSB outperforms state-of-the-art methods, significantly improving distortion metrics and effectively reducing exposure bias....

---

### 16. Transition from MOS to Ideal Capacitor Behavior Triggered by Tunneling in the Inversion Population Regime

**Authors:** Pedro Pereyra

**Published:** 2025-11-08

**Category:** cond-mat.mtrl-sci

**ID:** 2511.11637v1

**Link:** [http://arxiv.org/abs/2511.11637v1](http://arxiv.org/abs/2511.11637v1)

**Summary:** An analytical solution to the nonlinear Poisson equation governing the inversion layer in metal-oxide-semiconductor (MOS) structures has recently been obtained, resolving a fundamental challenge in semiconductor theory first identified in 1955. This breakthrough enables the derivation of explicit expressions for relevant physical quantities, such as the inversion-layer width, electric potential, and charge distribution, as functions of gate voltage $V_G$, distance from oxide-semiconductor interface and impurity concentration. These quantities exhibit rapid variation during early-stage inversion but saturate once the gate voltage exceeds the threshold voltage by a few tenths of a volt signaling a transition in the MOS response to $V_G$. The onset of tunneling through the Esaki barrier leads to increased charge accumulation near the interface, reshaping the charge distribution into a two-dimensional profile and shifting the potential drop from the semiconductor to the oxide layer. This reconfiguration resembles the behavior of an ideal parallel-plate capacitor, with charge confined at the interface and the voltage drop localized across the oxide. We analyze this mechanism in detail and demonstrate, through explicit calculations, that the tunneling current through the Esaki-like barrier formed during inversion becomes dominant, effectively superseding classical inversion behavior. These results offer a new analytical foundation for quantum-aware device modeling and inform the design of next-generation MOSFET and tunneling FET architectures....

---


<!-- ARXIV_PAPERS_END -->