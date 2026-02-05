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

## New Papers (2)

*Last updated: 2026-02-06 06:25:07 (SGT)*

### 1. Robust inverse material design with physical guarantees using the Voigt-Reuss Net

**Authors:** Sanath Keshav, Felix Fritzen

**Published:** 2025-11-14

**Category:** cs.LG

**ID:** 2511.11388v2

**Link:** [http://arxiv.org/abs/2511.11388v2](http://arxiv.org/abs/2511.11388v2)

**Summary:** We propose a spectrally normalized surrogate for forward and inverse mechanical homogenization with hard physical guarantees. Leveraging the Voigt-Reuss bounds, we factor their difference via a Cholesky-like operator and learn a dimensionless, symmetric positive semi-definite representation with eigenvalues in $[0,1]$; the inverse map returns symmetric positive-definite predictions that lie between the bounds in the Löwner sense. In 3D linear elasticity on an open dataset of stochastic biphasic microstructures, a fully connected Voigt-Reuss net trained on $>\!7.5\times 10^{5}$ FFT-based labels with 236 isotropy-invariant descriptors and three contrast parameters recovers the isotropic projection with near-perfect fidelity (isotropy-related entries: $R^2 \ge 0.998$), while anisotropy-revealing couplings are unidentifiable from $SO(3)$-invariant inputs. Tensor-level relative Frobenius errors have median $\approx 1.7\%$ and mean $\approx 3.4\%$ across splits. For 2D plane strain on thresholded trigonometric microstructures, coupling spectral normalization with a differentiable renderer and a CNN yields $R^2>0.99$ on all components, subpercent normalized losses, accurate tracking of percolation-induced eigenvalue jumps, and robust generalization to out-of-distribution images. Treating the parametric microstructure as design variables, batched first-order optimization with a single surrogate matches target tensors within a few percent and returns diverse near-optimal designs. Overall, the Voigt-Reuss net unifies accurate, physically admissible forward prediction with large-batch, constraint-consistent inverse design, and is generic to elliptic operators and coupled-physics settings....

---

### 2. Automated Extraction of Multicomponent Alloy Data Using Large Language Models for Sustainable Design

**Authors:** Aravindan Kamatchi Sundaram, Mohit Chakraborty, Sai Mani Kumar Devathi, B. Pabitramohan Prusty, Rohit Batra

**Published:** 2026-02-04

**Category:** cond-mat.mtrl-sci

**ID:** 2602.04602v1

**Link:** [http://arxiv.org/abs/2602.04602v1](http://arxiv.org/abs/2602.04602v1)

**Summary:** The design of sustainable materials requires access to materials performance and sustainability data from literature corpus in an organized, structured and automated manner. Natural language processing approaches, particularly large language models (LLMs), have been explored for materials data extraction from the literature, yet often suffer from limited accuracy or narrow scope. In this work, an LLM-based pipeline is developed to accurately extract alloy-related information from both textual descriptions and tabular data across the literature on high-entropy (or multicomponent) alloys (HEA). Specifically two databases with 37,711 and 148,069 entries respectively are retrieved; one from the literature text, consisting of alloy composition, processing conditions, characterization methods, and reported properties, and other from the literature tables, consisting of property names, values, and units. The pipeline enhances materials-domain sensitivity through prompt engineering and retrieval-augmented generation and achieves F1-scores of 0.83 for textual extraction and 0.88 for tabular extraction, surpassing or matching existing approaches. Application of the pipeline to over 10,000 articles yields the largest publicly available multicomponent alloy database and reveals compositional and processing-property trends. The database is further employed for sustainability-aware materials selection in three application domains, i.e., lightweighting, soft magnetic, and corrosion-resistant, identifying multicomponent alloy candidates with more sustainable production while maintaining or exceeding benchmark performance. The pipeline developed can be easily generalized to other class of materials, and assist in development of comprehensive, accurate and usable databases for sustainable materials design....

---


<!-- ARXIV_PAPERS_END -->