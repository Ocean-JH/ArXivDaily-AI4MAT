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

*Last updated: 2026-03-11 06:26:55 (SGT)*

### 1. Symmetry Classification of Magnetic Orders using Oriented Spin Space Groups

**Authors:** Yuntian Liu, Xiaobing Chen, Yutong Yu, Jesús Etxebarria, J. Manuel Perez-Mato, Qihang Liu

**Published:** 2025-06-25

**Category:** cond-mat.mtrl-sci

**ID:** 2506.20739v2

**Link:** [http://arxiv.org/abs/2506.20739v2](http://arxiv.org/abs/2506.20739v2)

**Summary:** Magnetism has witnessed remarkable progress in recent decades, largely driven by its potential for next-generation storage devices. However, the classification of magnetic orders, even for fundamental concepts such as ferromagnetism and antiferromagnetism, remains a topic of active evolution, particularly with the discovery of unconventional magnetic materials and advances in antiferromagnetic spintronics. Here, we present a unified classification of magnetic order utilizing the state-of-the-art spin space group (SSG) theory. Based on whether the net spin magnetization is constrained to zero by SSG, we systematically categorize magnetic orders into ferromagnetism (including ferrimagnetism) and antiferromagnetism. We further introduce an oriented SSG description, i.e., an SSG with a fixed magnetic orientation, thereby unifying the SSG and magnetic space group frameworks. This approach clearly reveals the symmetry-breaking pathway induced by spin-orbit coupling. The proposed group framework completes the intrinsic logic of magnetic symmetry and identifies a distinct magnetic phase, termed spin-orbit magnetism, in which the net spin magnetization is induced by spin-orbit coupling. Our work provides a comprehensive symmetry-based perspective for classifying magnetic order, offering fresh insights into unconventional magnets and broad applicability in spintronics and quantum material design....

---

### 2. Symmetry-Driven Generation of Crystal Structures from Composition

**Authors:** Shi Yin, Jinming Mu, Xudong Zhu, Linxin He

**Published:** 2026-02-19

**Category:** cond-mat.mtrl-sci

**ID:** 2602.17176v3

**Link:** [http://arxiv.org/abs/2602.17176v3](http://arxiv.org/abs/2602.17176v3)

**Summary:** Crystal structure prediction (CSP), which aims to predict the three-dimensional atomic arrangement of a crystal from its composition, is central to materials discovery and mechanistic understanding. However, given the composition in a unit cell, existing methods struggle with the NP-hard combinatorial challenge of rigorous symmetry enforcement or rely on retrieving known templates, which inherently limits both physical fidelity and the ability to discover genuinely new materials. To solve this, we propose a symmetry-driven generative framework. Our approach leverages large language models to encode chemical semantics and directly generate fine-grained Wyckoff patterns from atomic stoichiometry, effectively circumventing the limitations inherent to database lookups. Crucially, to overcome the exponentially complex problem of combinatorial site assignments, we incorporate domain knowledge through an efficient, linear-complexity heuristic beam search algorithm that rigorously enforces algebraic consistency between site multiplicities and atomic stoichiometry. By integrating this symmetry-consistent template into a diffusion backbone, our approach constrains the stochastic generative trajectory to a physically valid geometric manifold. This framework achieves state-of-the-art performance across stability, uniqueness, and novelty (SUN) benchmarks, alongside superior matching performance, thereby establishing a new paradigm for the rigorous exploration of targeted crystallographic space which can be previously uncharted, with no reliance on a priori structural knowledge....

---

### 3. One step further with Monte-Carlo sampler to guide diffusion better

**Authors:** Minsi Ren, Wenhao Deng, Ruiqi Feng, Tailin Wu

**Published:** 2026-03-04

**Category:** cs.LG

**ID:** 2603.06685v1

**Link:** [http://arxiv.org/abs/2603.06685v1](http://arxiv.org/abs/2603.06685v1)

**Summary:** Stochastic differential equation (SDE)-based generative models have achieved substantial progress in conditional generation via training-free differentiable loss-guided approaches. However, existing methodologies utilizing posterior sam- pling typically confront a substantial estimation error, which results in inaccu- rate gradients for guidance and leading to inconsistent generation results. To mitigate this issue, we propose that performing an additional backward denois- ing step and Monte-Carlo sampling (ABMS) can achieve better guided diffu- sion, which is a plug-and-play adjustment strategy. To verify the effectiveness of our method, we provide theoretical analysis and propose the adoption of a dual-focus evaluation framework, which further serves to highlight the critical problem of cross-condition interference prevalent in existing approaches. We conduct experiments across various task settings and data types, mainly includ- ing conditional online handwritten trajectory generation, image inverse problems (inpainting, super resolution and gaussian deblurring) molecular inverse design and so on. Experimental results demonstrate that our approach can be effec- tively used with higher order samplers and consistently improves the quality of generation samples across all the different scenarios....

---


<!-- ARXIV_PAPERS_END -->