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

*Last updated: 2026-04-22 06:36:46 (SGT)*

### 1. SWORD: Symmetry and Wyckoff-sequence of Ordered and Disordered crystals

**Authors:** Yuyao Huang, Wei Nong, Shuya Yamazaki, Martin Hoffmann Petersen, Jianghai Wang, Ruiming Zhu, Kedar Hippalgaonkar

**Published:** 2026-04-20

**Category:** cond-mat.mtrl-sci

**ID:** 2604.17994v1

**Link:** [http://arxiv.org/abs/2604.17994v1](http://arxiv.org/abs/2604.17994v1)

**Summary:** Novelty in materials discovery requires candidates to be distinct, non-redundant, and thermodynamically plausible. While crystallographic databases continue to expand in both size and complexity, making efficient and reliable novelty assessment has become increasingly difficult. This becomes particularly acute when crystallographic disorder is involved, as partial occupancies greatly enlarge the structure-composition space and obscure the identification of genuinely distinct structures. Here, we introduce SWORD, a symmetry-aware, Wyckoff-based string representation compatible with both ordered and disordered crystals. SWORD provides (i) standardization of symmetry-equivalent structural descriptions into a consistent label, (ii) explicitly represents co-occupying species on partially occupied sites, and (iii) quantifies complex disorder through a degree of mixing descriptor that captures continuous variation in site stoichiometry. These features enable efficient structure grouping, duplicate identification, and finer refinement of disordered structures. Benchmarking against existing fingerprint and structure-matching methods shows that SWORD remains invariant under identity-preserving transformations while retaining interpretable sensitivity to structural perturbations. In addition, SWORD shows competitive performance in associating unrelaxed and intermediate configurations with their final relaxed states along relaxation trajectories. This feature could enable more reliable novelty assessment directly from partially relaxed or even unrelaxed generated structures. Finally, SWORD was used to showcase its capability of disorder-aware database-scale deduplication and curation for the Inorganic Crystal Structure Database (ICSD). The curated ICSD would serve as the basis for the materials informatics and data-driven materials design in the era of artificial intelligence....

---

### 2. EGMOF: Efficient Generation of Metal-Organic Frameworks Using a Hybrid Diffusion-Transformer Architecture

**Authors:** Seunghee Han, Yeonghun Kang, Taeun Bae, Junho Kim, Younghun Kim, Varinia Bernales, Alan Aspuru-Guzik, Jihan Kim

**Published:** 2025-11-05

**Category:** cond-mat.mtrl-sci

**ID:** 2511.03122v3

**Link:** [http://arxiv.org/abs/2511.03122v3](http://arxiv.org/abs/2511.03122v3)

**Summary:** Designing materials with targeted properties remains challenging due to the vastness of chemical space and the scarcity of property-labeled data. While recent advances in generative models offer a promising way for inverse design, most approaches require large datasets and must be retrained for every new target property. Here, we introduce the EGMOF (Efficient Generation of MOFs), a hybrid diffusion-transformer framework that overcomes these limitations through a modular, descriptor-mediated workflow. EGMOF decomposes inverse design into two steps: (1) a one-dimensional diffusion model (Prop2Desc) that maps desired properties to chemically meaningful descriptors followed by (2) a transformer model (Desc2MOF) that generates structures from these descriptors. This modular hybrid design enables minimal retraining and maintains high accuracy even under small-data conditions. On a hydrogen uptake dataset, EGMOF achieved over 94% validity and 91% hit rate, representing significant improvements of up to 39% in validity and 29% in hit rate compared to existing methods, while remaining effective with only 1,000 training samples. Moreover, our model successfully performed conditional generation across 29 diverse property datasets, including CoREMOF, QMOF, and text-mined experimental datasets, whereas previous models have not. This work presents a data-efficient, generalizable approach to the inverse design of diverse MOFs and highlights the potential of modular inverse design workflows for broader materials discovery....

---

### 3. Offline Materials Optimization with CliqueFlowmer

**Authors:** Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine, Pieter Abbeel

**Published:** 2026-03-06

**Category:** cs.AI

**ID:** 2603.06082v4

**Link:** [http://arxiv.org/abs/2603.06082v4](http://arxiv.org/abs/2603.06082v4)

**Summary:** Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate this model's optimization abilities and show that materials it produces strongly outperform those from generative baselines. To support specialized materials discovery applications and broader interdisciplinary research, we release our code, model weights, and additional project resources at https://github.com/znowu/CliqueFlowmer, https://colab.research.google.com/drive/1usUg7zezFkcYHlm2MdYwZUNJXf_YkWnY?usp=sharing, and https://x.com/kuba_AI/status/2033382617442345321....

---


<!-- ARXIV_PAPERS_END -->