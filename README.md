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

*Last updated: 2025-12-12 06:18:22 (SGT)*

### 1. Partial Inverse Design of High-Performance Concrete Using Cooperative Neural Networks for Constraint-Aware Mix Generation

**Authors:** Agung Nugraha, Heungjun Im, Jihwan Lee

**Published:** 2025-12-07

**Category:** cs.LG

**ID:** 2512.06813v2

**Link:** [http://arxiv.org/abs/2512.06813v2](http://arxiv.org/abs/2512.06813v2)

**Summary:** High-performance concrete requires complex mix design decisions involving interdependent variables and practical constraints. While data-driven methods have improved predictive modeling for forward design in concrete engineering, inverse design remains limited, especially when some variables are fixed and only the remaining ones must be inferred. This study proposes a cooperative neural network framework for the partial inverse design of high-performance concrete. The framework integrates an imputation model with a surrogate strength predictor and learns through cooperative training. Once trained, it generates valid and performance-consistent mix designs in a single forward pass without retraining for different constraint scenarios. Compared with baseline models, including autoencoder models and Bayesian inference with Gaussian process surrogates, the proposed method achieves R-squared values of 0.87 to 0.92 and substantially reduces mean squared error by approximately 50% and 70%, respectively. The results show that the framework provides an accurate and computationally efficient foundation for constraint-aware, data-driven mix proportioning....

---

### 2. Transport Novelty Distance: A Distributional Metric for Evaluating Material Generative Models

**Authors:** Paul Hagemann, Simon Müller, Janine George, Philipp Benner

**Published:** 2025-12-10

**Category:** cond-mat.mtrl-sci

**ID:** 2512.09514v1

**Link:** [http://arxiv.org/abs/2512.09514v1](http://arxiv.org/abs/2512.09514v1)

**Summary:** Recent advances in generative machine learning have opened new possibilities for the discovery and design of novel materials. However, as these models become more sophisticated, the need for rigorous and meaningful evaluation metrics has grown. Existing evaluation approaches often fail to capture both the quality and novelty of generated structures, limiting our ability to assess true generative performance. In this paper, we introduce the Transport Novelty Distance (TNovD) to judge generative models used for materials discovery jointly by the quality and novelty of the generated materials. Based on ideas from Optimal Transport theory, TNovD uses a coupling between the features of the training and generated sets, which is refined into a quality and memorization regime by a threshold. The features are generated from crystal structures using a graph neural network that is trained to distinguish between materials, their augmented counterparts, and differently sized supercells using contrastive learning. We evaluate our proposed metric on typical toy experiments relevant for crystal structure prediction, including memorization, noise injection and lattice deformations. Additionally, we validate the TNovD on the MP20 validation set and the WBM substitution dataset, demonstrating that it is capable of detecting both memorized and low-quality material data. We also benchmark the performance of several popular material generative models. While introduced for materials, our TNovD framework is domain-agnostic and can be adapted for other areas, such as images and molecules....

---

### 3. exa-AMD: An Exascale-Ready Framework for Accelerating the Discovery and Design of Functional Materials

**Authors:** Weiyi Xia, Maxim Moraru, Ying Wai Li, Cai-Zhuang Wang

**Published:** 2025-10-01

**Category:** cond-mat.mtrl-sci

**ID:** 2510.01170v2

**Link:** [http://arxiv.org/abs/2510.01170v2](http://arxiv.org/abs/2510.01170v2)

**Summary:** We present exa-AMD, an open-source, high-performance framework designed for accelerated materials discovery on modern supercomputers. exa-AMD overcomes key computational bottlenecks in large-scale structure prediction through task-based parallelization, adaptive load balancing, and optimized data management for CPU and GPU architectures. The framework automates the end-to-end workflow, from generating candidate structures to evaluating formation energies and updating phase diagrams. Its modular design allows users to easily replace or extend components with custom machine learning models, alternative initial structure templates, and future structure generators, enabling flexible integration with emerging AI approaches. We demonstrate strong scaling across high-performance computing platforms and highlight applications to Na-B-C, Ce-Co-B, and Fe-Co-Zr systems, establishing exa-AMD as a robust and exascale-ready tool for accelerating the discovery and design of functional materials. exa-AMD is publicly available on GitHub, with detailed documentation and reproducible test cases to support community engagement and collaborative research....

---

### 4. AI-Driven Expansion and Application of the Alexandria Database

**Authors:** Théo Cavignac, Jonathan Schmidt, Pierre-Paul De Breuck, Antoine Loew, Tiago F. T. Cerqueira, Hai-Chen Wang, Anton Bochkarev, Yury Lysogorskiy, Aldo H. Romero, Ralf Drautz, Silvana Botti, Miguel A. L. Marques

**Published:** 2025-12-09

**Category:** cond-mat.mtrl-sci

**ID:** 2512.09169v1

**Link:** [http://arxiv.org/abs/2512.09169v1](http://arxiv.org/abs/2512.09169v1)

**Summary:** We present a novel multi-stage workflow for computational materials discovery that achieves a 99% success rate in identifying compounds within 100 meV/atom of thermodynamic stability, with a threefold improvement over previous approaches. By combining the Matra-Genoa generative model, Orb-v2 universal machine learning interatomic potential, and ALIGNN graph neural network for energy prediction, we generated 119 million candidate structures and added 1.3 million DFT-validated compounds to the ALEXANDRIA database, including 74 thousand new stable materials. The expanded ALEXANDRIA database now contains 5.8 million structures with 175 thousand compounds on the convex hull. Predicted structural disorder rates (37-43%) match experimental databases, unlike other recent AI-generated datasets. Analysis reveals fundamental patterns in space group distributions, coordination environments, and phase stability networks, including sub-linear scaling of convex hull connectivity. We release the complete dataset, including sAlex25 with 14 million out-of-equilibrium structures containing forces and stresses for training universal force fields. We demonstrate that fine-tuning a GRACE model on this data improves benchmark accuracy. All data, models, and workflows are freely available under Creative Commons licenses....

---

### 5. 3DID: Direct 3D Inverse Design for Aerodynamics with Physics-Aware Optimization

**Authors:** Yuze Hao, Linchao Zhu, Yi Yang

**Published:** 2025-12-06

**Category:** cs.CV

**ID:** 2512.08987v1

**Link:** [http://arxiv.org/abs/2512.08987v1](http://arxiv.org/abs/2512.08987v1)

**Summary:** Inverse design aims to design the input variables of a physical system to optimize a specified objective function, typically formulated as a search or optimization problem. However, in 3D domains, the design space grows exponentially, rendering exhaustive grid-based searches infeasible. Recent advances in deep learning have accelerated inverse design by providing powerful generative priors and differentiable surrogate models. Nevertheless, current methods tend to approximate the 3D design space using 2D projections or fine-tune existing 3D shapes. These approaches sacrifice volumetric detail and constrain design exploration, preventing true 3D design from scratch. In this paper, we propose a 3D Inverse Design (3DID) framework that directly navigates the 3D design space by coupling a continuous latent representation with a physics-aware optimization strategy. We first learn a unified physics-geometry embedding that compactly captures shape and physical field data in a continuous latent space. Then, we introduce a two-stage strategy to perform physics-aware optimization. In the first stage, a gradient-guided diffusion sampler explores the global latent manifold. In the second stage, an objective-driven, topology-preserving refinement further sculpts each candidate toward the target objective. This enables 3DID to generate high-fidelity 3D geometries, outperforming existing methods in both solution quality and design versatility....

---


<!-- ARXIV_PAPERS_END -->