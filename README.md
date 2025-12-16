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

*Last updated: 2025-12-17 06:18:30 (SGT)*

### 1. Meta-GPT: Decoding the Metasurface Genome with Generative Artificial Intelligence

**Authors:** David Dang, Stuart Love, Meena Salib, Quynh Dang, Samuel Rothfarb, Mysk Alnatour, Andrew Salij, Hou-Tong Chen, Ho Wai, Lee, Wilton J. M. Kort-Kamp

**Published:** 2025-12-15

**Category:** physics.optics

**ID:** 2512.12888v1

**Link:** [http://arxiv.org/abs/2512.12888v1](http://arxiv.org/abs/2512.12888v1)

**Summary:** Advancing artificial intelligence for physical sciences requires representations that are both interpretable and compatible with the underlying laws of nature. We introduce METASTRINGS, a symbolic language for photonics that expresses nanostructures as textual sequences encoding materials, geometries, and lattice configurations. Analogous to molecular textual representations in chemistry, METASTRINGS provides a framework connecting human interpretability with computational design by capturing the structural hierarchy of photonic metasurfaces. Building on this representation, we develop Meta-GPT, a foundation transformer model trained on METASTRINGS and finetuned with physics-informed supervised, reinforcement, and chain-of-thought learning. Across various design tasks, the model achieves <3% mean-squared spectral error and maintains >98% syntactic validity, generating diverse metasurface prototypes whose experimentally measured optical responses match their target spectra. These results demonstrate that Meta-GPT can learn the compositional rules of light-matter interactions through METASTRINGS, laying a rigorous foundation for AI-driven photonics and representing an important step toward a metasurface genome project....

---

### 2. Quantum-Aware Generative AI for Materials Discovery: A Framework for Robust Exploration Beyond DFT Biases

**Authors:** Mahule Roy, Guillaume Lambard

**Published:** 2025-12-13

**Category:** cs.AI

**ID:** 2512.12288v1

**Link:** [http://arxiv.org/abs/2512.12288v1](http://arxiv.org/abs/2512.12288v1)

**Summary:** Conventional generative models for materials discovery are predominantly trained and validated using data from Density Functional Theory (DFT) with approximate exchange-correlation functionals. This creates a fundamental bottleneck: these models inherit DFT's systematic failures for strongly correlated systems, leading to exploration biases and an inability to discover materials where DFT predictions are qualitatively incorrect. We introduce a quantum-aware generative AI framework that systematically addresses this limitation through tight integration of multi-fidelity learning and active validation. Our approach employs a diffusion-based generator conditioned on quantum-mechanical descriptors and a validator using an equivariant neural network potential trained on a hierarchical dataset spanning multiple levels of theory (PBE, SCAN, HSE06, CCSD(T)). Crucially, we implement a robust active learning loop that quantifies and targets the divergence between low- and high-fidelity predictions. We conduct comprehensive ablation studies to deconstruct the contribution of each component, perform detailed failure mode analysis, and benchmark our framework against state-of-the-art generative models (CDVAE, GNoME, DiffCSP) across several challenging material classes. Our results demonstrate significant practical gains: a 3-5x improvement in successfully identifying potentially stable candidates in high-divergence regions (e.g., correlated oxides) compared to DFT-only baselines, while maintaining computational feasibility. This work provides a rigorous, transparent framework for extending the effective search space of computational materials discovery beyond the limitations of single-fidelity models....

---

### 3. Random Combinatorial Libraries and Automated Nanoindentation for High-Throughput Structural Materials Discovery

**Authors:** Vivek Chawla, Dayakar Penumadu, Sergei Kalinin

**Published:** 2025-12-13

**Category:** cond-mat.mtrl-sci

**ID:** 2512.12164v1

**Link:** [http://arxiv.org/abs/2512.12164v1](http://arxiv.org/abs/2512.12164v1)

**Summary:** Accelerating the discovery of structural materials is essential for applications in hard and refractory alloys, hypersonic platforms, nuclear systems, and other extreme environment technologies. Progress is often constrained by slow synthesis and characterization cycles and the need for extensive mechanical testing across large compositional spaces. Here, we propose a rapid screening strategy based on random material libraries, in which thousands of distinct compositions are embedded within a single specimen, mapped by EDS, and subsequently characterized. Using nanoindentation as a representative case, we show that such libraries enable dense composition property mapping while reducing the number of samples required to explore high dimensional composition spaces compared to traditional synthesis and test workflows. An experimentally calibrated Monte Carlo framework is developed to quantify practical limits, including particle size, EDS noise and resolution, positional accuracy, and nanoindenter motion costs. The simulations identify regimes where random libraries provide orders of magnitude acceleration over classical workflows. Finally, we demonstrate experimental navigation of these libraries using automated indentation. Together, these results establish random libraries as a general route to high throughput characterization in structurally critical material systems....

---


<!-- ARXIV_PAPERS_END -->