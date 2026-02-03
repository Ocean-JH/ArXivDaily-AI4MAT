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

*Last updated: 2026-02-04 06:27:36 (SGT)*

### 1. Physics Informed Generative AI Enabling Labour Free Segmentation For Microscopy Analysis

**Authors:** Salma Zahran, Zhou Ao, Zhengyang Zhang, Chen Chi, Chenchen Yuan, Yanming Wang

**Published:** 2026-02-02

**Category:** cs.CV

**ID:** 2602.01710v1

**Link:** [http://arxiv.org/abs/2602.01710v1](http://arxiv.org/abs/2602.01710v1)

**Summary:** Semantic segmentation of microscopy images is a critical task for high-throughput materials characterisation, yet its automation is severely constrained by the prohibitive cost, subjectivity, and scarcity of expert-annotated data. While physics-based simulations offer a scalable alternative to manual labelling, models trained on such data historically fail to generalise due to a significant domain gap, lacking the complex textures, noise patterns, and imaging artefacts inherent to experimental data. This paper introduces a novel framework for labour-free segmentation that successfully bridges this simulation-to-reality gap. Our pipeline leverages phase-field simulations to generate an abundant source of microstructural morphologies with perfect, intrinsically-derived ground-truth masks. We then employ a Cycle-Consistent Generative Adversarial Network (CycleGAN) for unpaired image-to-image translation, transforming the clean simulations into a large-scale dataset of high-fidelity, realistic SEM images. A U-Net model, trained exclusively on this synthetic data, demonstrated remarkable generalisation when deployed on unseen experimental images, achieving a mean Boundary F1-Score of 0.90 and an Intersection over Union (IOU) of 0.88. Comprehensive validation using t-SNE feature-space projection and Shannon entropy analysis confirms that our synthetic images are statistically and featurally indistinguishable from the real data manifold. By completely decoupling model training from manual annotation, our generative framework transforms a data-scarce problem into one of data abundance, providing a robust and fully automated solution to accelerate materials discovery and analysis....

---

### 2. Are diffusion models ready for materials discovery in unexplored chemical space?

**Authors:** Sanghyun Kim, Gihyeon Jeon, Seungwoo Hwang, Jiho Lee, Jisu Jung, Seungwu Han, Sungwoo Kang

**Published:** 2025-10-10

**Category:** cond-mat.mtrl-sci

**ID:** 2510.09406v3

**Link:** [http://arxiv.org/abs/2510.09406v3](http://arxiv.org/abs/2510.09406v3)

**Summary:** While diffusion models are attracting increasing attention for the design of novel materials, their ability to generate low-energy structures in unexplored chemical spaces has not been systematically assessed. Here, we evaluate the performance of two diffusion models, MatterGen and DiffCSP, against three databases: a ternary oxide set (constructed by a genetic algorithm), a ternary nitride set (constructed by template informatics), and the GNoME database (constructed by a combination of both). We find that diffusion models generally perform stably in well-sampled chemical spaces (oxides and nitrides), but are less effective in uncommon ones (GNoME), which contains many compositions involving rare-earth elements and unconventional stoichiometry. Finally, we assess their size-extrapolation capability and observe a significant drop in performance when the number of atoms exceeds the trained range. This is attributed to the limitations imposed by periodic boundary conditions, which we refer to as the curse of periodicity. This study paves the way for future developments in materials design by highlighting both the strength and the limitations of diffusion models....

---

### 3. Data-driven active learning approaches for accelerating materials discovery

**Authors:** Jiaxin Chen, Tianjiao Wan, Hui Geng, Liang Xiong, Guohong Wang, Yihan Zhao, Longxiang Deng, Zijian Gao, Susu Fang, Zheng Luo, Huaimin Wang, Shanshan Wang, Kele Xu

**Published:** 2026-01-11

**Category:** cond-mat.mtrl-sci

**ID:** 2601.06971v3

**Link:** [http://arxiv.org/abs/2601.06971v3](http://arxiv.org/abs/2601.06971v3)

**Summary:** Materials discovery is a cornerstone of modern technological advancement, yet it remains constrained by traditional trial-and-error paradigms and the inherent bias of human intuition. Artificial intelligence (AI) has emerged as a transformative tool in materials science by effectively modeling structure-property relationships. Despite substantial efforts to enhance model expressiveness, data efficiency remains an equally critical challenge, given the limited availability of experimental and computational resources. Active learning (AL), as a data-driven machine learning paradigm, has shown great promise for discovering novel materials and enabling the efficient navigation of vast materials spaces. In this review, we follow the evolution of sampling strategy design techniques in AL, from Bayesian optimization to advanced deep learning-based strategies. We then highlight how AL enhances data efficiency across various data regimes, ranging from task-specific settings with limited data to the development of general-purpose datasets and large-scale models. We further provide a systematic overview of AL applications throughout the materials research pipeline, including computational simulation, composition and structural design, process optimization, and self-driving laboratory systems. Finally, we pinpoint key challenges and future perspectives of AL in materials discovery....

---

### 4. Robust Machine Learning Framework for Reliable Discovery of High-Performance Half-Heusler Thermoelectrics

**Authors:** Shoeb Athar, Adrien Mecibah, Philippe Jund

**Published:** 2026-02-01

**Category:** cond-mat.mtrl-sci

**ID:** 2602.01149v1

**Link:** [http://arxiv.org/abs/2602.01149v1](http://arxiv.org/abs/2602.01149v1)

**Summary:** Machine learning (ML) can facilitate efficient thermoelectric (TE) material discovery essential to address the environmental crisis. However, ML models often suffer from poor experimental generalizability despite high metrics. This study presents a robust workflow, applied to the half-Heusler (hH) structural prototype, for figure of merit (zT) prediction, to improve the generalizability of ML models. To resolve challenges in dataset handling and feature filtering, we first introduce a rigorous PCA-based splitting method that ensures training and test sets are unbiased and representative of the full chemical space. We then integrate Bayesian hyperparameter optimization with k-best feature filtering across three architectures-Random Forest, XGBoost, and Neural Networks - while employing SISSO symbolic regression for physical insight and comparison. Using SHAP and SISSO analysis, we identify A-site dopant concentration (xA'), and A-site Heat of Vaporization (HVA) as the primary drivers of zT besides Temperature (T). Finally, a high-throughput screening of approximately 6.6x10^8 potential compositions, filtered by stability constraints, yielded several novel high-zT candidates. Breaking from the traditional focus of improving test RMSE/R^2 values of the models, this work shifts the attention on establishing the test set a true proxy for model generalizability and strengthening the often neglected modules of the existing ML workflows for the data-driven design of next-generation thermoelectric materials....

---

### 5. Open Materials Generation with Inference-Time Reinforcement Learning

**Authors:** Philipp Hoellmer, Stefano Martiniani

**Published:** 2026-01-31

**Category:** cs.LG

**ID:** 2602.00424v1

**Link:** [http://arxiv.org/abs/2602.00424v1](http://arxiv.org/abs/2602.00424v1)

**Summary:** Continuous-time generative models for crystalline materials enable inverse materials design by learning to predict stable crystal structures, but incorporating explicit target properties into the generative process remains challenging. Policy-gradient reinforcement learning (RL) provides a principled mechanism for aligning generative models with downstream objectives but typically requires access to the score, which has prevented its application to flow-based models that learn only velocity fields. We introduce Open Materials Generation with Inference-time Reinforcement Learning (OMatG-IRL), a policy-gradient RL framework that operates directly on the learned velocity fields and eliminates the need for the explicit computation of the score. OMatG-IRL leverages stochastic perturbations of the underlying generation dynamics preserving the baseline performance of the pretrained generative model while enabling exploration and policy-gradient estimation at inference time. Using OMatG-IRL, we present the first application of RL to crystal structure prediction (CSP). Our method enables effective reinforcement of an energy-based objective while preserving diversity through composition conditioning, and it achieves performance competitive with score-based RL approaches. Finally, we show that OMatG-IRL can learn time-dependent velocity-annealing schedules, enabling accurate CSP with order-of-magnitude improvements in sampling efficiency and, correspondingly, reduction in generation time....

---

### 6. Exploring the Limitations of kNN Noisy Feature Detection and Recovery for Self-Driving Labs

**Authors:** Qiuyu Shi, Kangming Li, Yao Fehlis, Runze Zhang, Daniel Persaud, Robert Black, Jason Hattrick-Simpers

**Published:** 2025-07-15

**Category:** cs.LG

**ID:** 2507.16833v2

**Link:** [http://arxiv.org/abs/2507.16833v2](http://arxiv.org/abs/2507.16833v2)

**Summary:** Self-driving laboratories (SDLs) have shown promise to accelerate materials discovery by integrating machine learning with automated experimental platforms. However, errors in the capture of input parameters may corrupt the features used to model system performance, compromising current and future campaigns. This study develops an automated workflow to systematically detect noisy features, determine sample-feature pairings that can be corrected, and finally recover the correct feature values. A systematic study is then performed to examine how dataset size, noise intensity, noise type, and feature value distribution affect both the detectability and recoverability of noisy features on both Density Functional Theory (DFT) and SDL datasets. In general, high-intensity noise and large training datasets are conducive to the detection and correction of noisy features. Low-intensity noise reduces detection and recovery but can be compensated for by larger clean training data sets. Detection and correction results vary between features, with continuous and dispersed feature distributions showing greater recoverability compared to features with discrete or narrow distributions. This systematic study not only demonstrates a model agnostic framework for rational data recovery in the presence of noise, limited data, and differing feature distributions but also provides a tangible benchmark of kNN imputation in materials datasets. Ultimately, it aims to enhance data quality and experimental precision in automated materials discovery....

---

### 7. How well do generative models solve inverse problems? A benchmark study

**Authors:** Patrick Krüger, Patrick Materne, Werner Krebs, Hanno Gottschalk

**Published:** 2026-01-30

**Category:** cs.LG

**ID:** 2601.23238v1

**Link:** [http://arxiv.org/abs/2601.23238v1](http://arxiv.org/abs/2601.23238v1)

**Summary:** Generative learning generates high dimensional data based on low dimensional conditions, also called prompts. Therefore, generative learning algorithms are eligible for solving (Bayesian) inverse problems. In this article we compare a traditional Bayesian inverse approach based on a forward regression model and a prior sampled with the Markov Chain Monte Carlo method with three state of the art generative learning models, namely conditional Generative Adversarial Networks, Invertible Neural Networks and Conditional Flow Matching. We apply them to a problem of gas turbine combustor design where we map six independent design parameters to three performance labels. We propose several metrics for the evaluation of this inverse design approaches and measure the accuracy of the labels of the generated designs along with the diversity. We also study the performance as a function of the training dataset size. Our benchmark has a clear winner, as Conditional Flow Matching consistently outperforms all competing approaches....

---


<!-- ARXIV_PAPERS_END -->