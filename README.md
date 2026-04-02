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

## New Papers (3)

*Last updated: 2026-04-03 06:29:51 (SGT)*

### 1. Inverse Design of Optical Multilayer Thin Films using Robust Masked Diffusion Models

**Authors:** Jonas Schaible, Asena Karolin Özdemir, Charlotte Debus, Sven Burger, Achim Streit, Christiane Becker, Klaus Jäger, Markus Götz

**Published:** 2026-04-01

**Category:** physics.optics

**ID:** 2604.01106v1

**Link:** [http://arxiv.org/abs/2604.01106v1](http://arxiv.org/abs/2604.01106v1)

**Summary:** Inverse design of optical multilayer stacks seeks to infer layer materials, thicknesses, and ordering from a desired target spectrum. It is a long-standing challenge due to the large design space and non-unique solutions. We introduce \texttt{OptoLlama}, a masked diffusion language model for inverse thin-film design from optical spectra. Representing multilayer stacks as sequences of material-thickness tokens, \texttt{OptoLlama} conditions generation on reflectance, absorptance, and transmittance spectra and learns a probabilistic mapping from optical response to structure. Evaluated on a representative test set of 3,000 targets, \texttt{OptoLlama} reduces the mean absolute spectral error by 2.9-fold relative to a nearest-neighbor template baseline and by 3.45-fold relative to the state-of-the-art data-driven baseline, called \texttt{OptoGPT}. Case studies on designed and expert-defined targets show that the model reproduces characteristic spectral features and recovers physically meaningful stack motifs, including distributed Bragg reflectors. These results establish diffusion-based sequence modeling as a powerful framework for inverse photonic design....

---

### 2. Learning Inter-Atomic Potentials without Explicit Equivariance

**Authors:** Ahmed A. Elhag, Arun Raja, Alex Morehead, Samuel M. Blau, Hongtao Zhao, Christian Tyrchan, Eva Nittinger, Garrett M. Morris, Michael M. Bronstein

**Published:** 2025-09-25

**Category:** cs.LG

**ID:** 2510.00027v3

**Link:** [http://arxiv.org/abs/2510.00027v3](http://arxiv.org/abs/2510.00027v3)

**Summary:** Accurate and scalable machine-learned inter-atomic potentials (MLIPs) are essential for molecular simulations ranging from drug discovery to new material design. Current state-of-the-art models enforce roto-translational symmetries through equivariant neural network architectures, a hard-wired inductive bias that can often lead to reduced flexibility, computational efficiency, and scalability. In this work, we introduce TransIP: Transformer-based Inter-Atomic Potentials, a novel training paradigm for interatomic potentials achieving symmetry compliance without explicit architectural constraints. Our approach guides a generic non-equivariant Transformer-based model to learn SO(3)-equivariance by optimizing its representations in the embedding space. Trained on the recent Open Molecules (OMol25) collection, a large and diverse molecular dataset built specifically for MLIPs and covering different types of molecules (including small organics, biomolecular fragments, and electrolyte-like species), TransIP attains comparable performance in machine-learning force fields versus state-of-the-art equivariant baselines. Further, compared to a data augmentation baseline, TransIP achieves 40% to 60% improvement in performance across varying OMol25 dataset sizes. More broadly, our work shows that learned equivariance can be a powerful and efficient alternative to equivariant or augmentation-based MLIP models. Our code is available at: https://github.com/Ahmed-A-A-Elhag/TransIP....

---

### 3. AMShortcut: An Inference- and Training-Efficient Inverse Design Model for Amorphous Materials

**Authors:** Yan Lin, Jonas A. Finkler, Tao Du, Jilin Hu, Morten M. Smedskjaer

**Published:** 2026-03-31

**Category:** cs.LG

**ID:** 2603.29812v1

**Link:** [http://arxiv.org/abs/2603.29812v1](http://arxiv.org/abs/2603.29812v1)

**Summary:** Amorphous materials are solids that lack long-range atomic order but possess complex short- and medium-range order. Unlike crystalline materials that can be described by unit cells containing few up to hundreds of atoms, amorphous materials require larger simulation cells with at least hundreds or often thousands of atoms. Inverse design of amorphous materials with probabilistic generative models aims to generate the atomic positions and elements of amorphous materials given a set of desired properties. It has emerged as a promising approach for facilitating the application of amorphous materials in domains such as energy storage and thermal management. In this paper, we introduce AMShortcut, an inference- and training-efficient probabilistic generative model for amorphous materials. AMShortcut enables accurate inference of diverse short- and medium-range structures in amorphous materials with only a few sampling steps, mitigating the need for an excessive number of sampling steps that hinders inference efficiency. AMShortcut can be trained once with all relevant properties and perform inference conditioned on arbitrary combinations of desired properties, mitigating the need for training one model for each combination. Experiments on three amorphous materials datasets with diverse structures and properties demonstrate that AMShortcut achieves its design goals....

---


<!-- ARXIV_PAPERS_END -->