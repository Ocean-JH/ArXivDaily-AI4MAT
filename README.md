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

## New Papers (1)

*Last updated: 2025-09-12 06:15:16 (SGT)*

### 1. Facet: highly efficient E(3)-equivariant networks for interatomic potentials

**Authors:** Nicholas Miklaucic, Lai Wei, Rongzhi Dong, Nihang Fu, Sadman Sadeed Omee, Qingyang Li, Sourin Dey, Victor Fung, Jianjun Hu

**Published:** 2025-09-10

**Category:** cond-mat.mtrl-sci

**ID:** 2509.08418v1

**Link:** [http://arxiv.org/abs/2509.08418v1](http://arxiv.org/abs/2509.08418v1)

**Summary:** Computational materials discovery is limited by the high cost of
first-principles calculations. Machine learning (ML) potentials that predict
energies from crystal structures are promising, but existing methods face
computational bottlenecks. Steerable graph neural networks (GNNs) encode
geometry with spherical harmonics, respecting atomic symmetries -- permutation,
rotation, and translation -- for physically realistic predictions. Yet
maintaining equivariance is difficult: activation functions must be modified,
and each layer must handle multiple data types for different harmonic orders.
We present Facet, a GNN architecture for efficient ML potentials, developed
through systematic analysis of steerable GNNs. Our innovations include
replacing expensive multi-layer perceptrons (MLPs) for interatomic distances
with splines, which match performance while cutting computational and memory
demands. We also introduce a general-purpose equivariant layer that mixes node
information via spherical grid projection followed by standard MLPs -- faster
than tensor products and more expressive than linear or gate layers. On the
MPTrj dataset, Facet matches leading models with far fewer parameters and under
10% of their training compute. On a crystal relaxation task, it runs twice as
fast as MACE models. We further show SevenNet-0's parameters can be reduced by
over 25% with no accuracy loss. These techniques enable more than 10x faster
training of large-scale foundation models for ML potentials, potentially
reshaping computational materials discovery....

---


<!-- ARXIV_PAPERS_END -->