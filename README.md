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

*Last updated: 2025-09-11 06:15:07 (SGT)*

### 1. PLaID++: A Preference Aligned Language Model for Targeted Inorganic Materials Design

**Authors:** Andy Xu, Rohan Desai, Larry Wang, Gabriel Hope, Ethan Ritz

**Published:** 2025-09-08

**Category:** cs.LG

**ID:** 2509.07150v1

**Link:** [http://arxiv.org/abs/2509.07150v1](http://arxiv.org/abs/2509.07150v1)

**Summary:** Discovering novel materials is critical for technological advancements such
as solar cells, batteries, and carbon capture. However, the development of new
materials is constrained by a slow and expensive trial-and-error process. To
accelerate this pipeline, we introduce PLaID++, a Large Language Model (LLM)
fine-tuned for stable and property-guided crystal generation. We fine-tune
Qwen-2.5 7B to generate crystal structures using a novel Wyckoff-based text
representation. We show that generation can be effectively guided with a
reinforcement learning technique based on Direct Preference Optimization (DPO),
with sampled structures categorized by their stability, novelty, and space
group. By encoding symmetry constraints directly into text and guiding model
outputs towards desirable chemical space, PLaID++ generates structures that are
thermodynamically stable, unique, and novel at a $\sim$50\% greater rate than
prior methods and conditionally generates structures with desired space group
properties. Our experiments highlight the effectiveness of iterative DPO,
achieving $\sim$115\% and $\sim$50\% improvements in unconditional and space
group conditioned generation, respectively, compared to fine-tuning alone. Our
work demonstrates the potential of adapting post-training techniques from
natural language processing to materials design, paving the way for targeted
and efficient discovery of novel materials....

---

### 2. Language Native Lightly Structured Databases for Large Language Model Driven Composite Materials Research

**Authors:** Yuze Liu, Zhaoyuan Zhang, Xiangsheng Zeng, Yihe Zhang, Leping Yu, Lejia Wang, Xi Yu

**Published:** 2025-09-07

**Category:** cs.DB

**ID:** 2509.06093v1

**Link:** [http://arxiv.org/abs/2509.06093v1](http://arxiv.org/abs/2509.06093v1)

**Summary:** Chemical and materials research has traditionally relied heavily on knowledge
narrative, with progress often driven by language-based descriptions of
principles, mechanisms, and experimental experiences, rather than tables,
limiting what conventional databases and ML can exploit. We present a
language-native database for boron nitride nanosheet (BNNS) polymer thermally
conductive composites that captures lightly structured information from papers
across preparation, characterization, theory-computation, and mechanistic
reasoning, with evidence-linked snippets. Records are organized in a
heterogeneous database and queried via composite retrieval with semantics, key
words and value filters. The system can synthesizes literature into accurate,
verifiable, and expert style guidance. This substrate enables high fidelity
efficient Retrieval Augmented Generation (RAG) and tool augmented agents to
interleave retrieval with reasoning and deliver actionable SOP. The framework
supplies the language rich foundation required for LLM-driven materials
discovery....

---

### 3. Meta-training of diffractive meta-neural networks for super-resolution direction of arrival estimation

**Authors:** Songtao Yang, Sheng Gao, Chu Wu, Zejia Zhao, Haiou Zhang, Xing Lin

**Published:** 2025-09-07

**Category:** physics.optics

**ID:** 2509.05926v1

**Link:** [http://arxiv.org/abs/2509.05926v1](http://arxiv.org/abs/2509.05926v1)

**Summary:** Diffractive neural networks leverage the high-dimensional characteristics of
electromagnetic (EM) fields for high-throughput computing. However, the
existing architectures face challenges in integrating large-scale
multidimensional metasurfaces with precise network training and haven't
utilized multidimensional EM field coding scheme for super-resolution sensing.
Here, we propose diffractive meta-neural networks (DMNNs) for accurate EM field
modulation through metasurfaces, which enable multidimensional multiplexing and
coding for multi-task learning and high-throughput super-resolution direction
of arrival estimation. DMNN integrates pre-trained mini-metanets to
characterize the amplitude and phase responses of meta-atoms across different
polarizations and frequencies, with structure parameters inversely designed
using the gradient-based meta-training. For wide-field super-resolution angle
estimation, the system simultaneously resolves azimuthal and elevational angles
through x and y-polarization channels, while the interleaving of
frequency-multiplexed angular intervals generates spectral-encoded optical
super-oscillations to achieve full-angle high-resolution estimation.
Post-processing lightweight electronic neural networks further enhance the
performance. Experimental results validate that a three-layer DMNN operating at
27 GHz, 29 GHz, and 31 GHz achieves $\sim7\times$ Rayleigh diffraction-limited
angular resolution (0.5$^\circ$), a mean absolute error of 0.048$^\circ$ for
two incoherent targets within a $\pm 11.5^\circ$ field of view, and an angular
estimation throughput an order of magnitude higher (1917) than that of existing
methods. The proposed architecture advances high-dimensional photonic computing
systems by utilizing inherent high-parallelism and all-optical coding methods
for ultra-high-resolution, high-throughput applications....

---

### 4. Crystal structure prediction with host-guided inpainting generation and foundation potentials

**Authors:** Peichen Zhong, Xinzhe Dai, Bowen Deng, Gerbrand Ceder, Kristin A. Persson

**Published:** 2025-04-23

**Category:** cond-mat.mtrl-sci

**ID:** 2504.16893v2

**Link:** [http://arxiv.org/abs/2504.16893v2](http://arxiv.org/abs/2504.16893v2)

**Summary:** Unconditional crystal structure generation with diffusion models faces
challenges in identifying symmetric crystals as the unit cell size increases.
We present the Crystal Host-Guided Generation (CHGGen) framework to address
this challenge through conditional generation using an inpainting method, which
optimizes a fraction of atomic positions within a predefined and symmetrized
host structure to improve the success rate for symmetric structure generation.
By integrating inpainting structure generation with a foundation potential for
structure optimization, we demonstrate the method on the ZnS-P$_2$S$_5$ and
Li-Si chemical systems, where the inpainting method generates a higher fraction
of symmetric structures than unconditional generation. The practical
significance of CHGGen extends to enabling the structural modification of
crystal structures, particularly for systems with partial occupancy or
intercalation chemistry. The inpainting method also allows for seamless
integration with other generative models, providing a versatile framework for
accelerating materials discovery....

---

### 5. Physically Interpretable Descriptors Drive the Materials Design of Metal Hydrides for Hydrogen Storage

**Authors:** Seong-Hoon Jang, Di Zhang, Hung Ba Tran, Xue Jia, Kiyoe Konno, Ryuhei Sato, Shin-ichi Orimo, Hao Li

**Published:** 2025-09-04

**Category:** cond-mat.mtrl-sci

**ID:** 2509.04039v2

**Link:** [http://arxiv.org/abs/2509.04039v2](http://arxiv.org/abs/2509.04039v2)

**Summary:** Designing metal hydrides for hydrogen storage remains a longstanding
challenge due to the vast compositional space and complex structure-property
relationships. Herein, for the first time, we present physically interpretable
models for predicting two key performance metrics, gravimetric hydrogen density
$w$ and equilibrium pressure $P_{\rm eq,RT}$ at room temperature, based on a
minimal set of chemically meaningful descriptors. Using a rigorously curated
dataset of $5,089$ metal hydride compositions from our recently developed
Digital Hydrogen Platform (\it{DigHyd}) based on large-scale data mining from
available experimental literature of solid-state hydrogen storage materials, we
systematically constructed over $1.6$ million candidate models using
combinations of scalar transformations and nonlinear link functions. The final
closed-form models, derived from $2$-$3$ descriptors each, achieve predictive
accuracies on par with state-of-the-art machine learning methods, while
maintaining full physical transparency. Strikingly, descriptor-based design
maps generated from these models reveal a fundamental trade-off between $w$ and
$P_{\rm eq,RT}$: saline-type hydrides, composed of light electropositive
elements, offer high $w$ but low $P_{\rm eq,RT}$, whereas interstitial-type
hydrides based on heavier electronegative transition metals show the opposite
trend. Notably, Be-based systems, such as Be-Na alloys, emerge as rare
candidates that simultaneously satisfy both performance metrics, attributed to
the unique combination of light mass and high molar density for Be. Our models
indicate that Be-based systems may offer renewed prospects for approaching
these benchmarks. These results provide chemically intuitive guidelines for
materials design and establish a scalable framework for the rational discovery
of materials in complex chemical spaces....

---

### 6. Unveiling the critical factors in crystal structure graph representation: a comparative analysis using streamlined MLPSets frameworks

**Authors:** Hongwei Du, Hong Wang

**Published:** 2025-09-06

**Category:** cond-mat.mtrl-sci

**ID:** 2509.05712v1

**Link:** [http://arxiv.org/abs/2509.05712v1](http://arxiv.org/abs/2509.05712v1)

**Summary:** Graph Neural Networks have rapidly advanced in materials science and
chemistry,with their performance critically dependent on comprehensive
representations of crystal or molecular structures across five dimensions:
elemental information, geometric topology, electronic interactions, symmetry,
and long-range interactions. Existing models still exhibit limitations in
representing electronic interactions, symmetry, and long-range information.
This study compares physics-based site feature calculators with data-driven
graph representation strategies. We find that the latter achieve superior
performance in representation completeness, convergence speed, and
extrapolation capability by incorporating electronic structure generation
models-such as variational autoencoders (VAEs) that compress Kohn-Sham wave
functions and leveraging multi-task learning. Notably, the CHGNet-V1/V2
strategies, when integrated into the DenseGNN model,significantly outperform
state-of-the-art models across 35 datasets from Matbench and JARVIS-DFT,
yielding predictions with accuracy close to that of DFT calculations.
Furthermore, applying a pre-training and fine-tuning strategy substantially
reduces the prediction error for band gaps of complex disordered materials,
demonstrating the superiority and potential of data-driven graph
representations in accelerating materials discovery....

---


<!-- ARXIV_PAPERS_END -->