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

*Last updated: 2026-03-07 06:29:27 (SGT)*

### 1. LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery

**Authors:** Nikhil Abhyankar, Sanchit Kabra, Saaketh Desai, Chandan K. Reddy

**Published:** 2025-10-26

**Category:** cs.LG

**ID:** 2510.22503v2

**Link:** [http://arxiv.org/abs/2510.22503v2](http://arxiv.org/abs/2510.22503v2)

**Summary:** Materials discovery requires navigating vast chemical and structural spaces while satisfying multiple, often conflicting, objectives. We present LLM-guided Evolution for MAterials discovery (LLEMA), a unified framework that couples the scientific knowledge embedded in large language models with chemistry-informed evolutionary rules and memory-based refinement. At each iteration, an LLM proposes crystallographically specified candidates under explicit property constraints; a surrogate-augmented oracle estimates physicochemical properties; and a multi-objective scorer updates success/failure memories to guide subsequent generations. Evaluated on 14 realistic tasks that span electronics, energy, coatings, optics, and aerospace, LLEMA discovers candidates that are chemically plausible, thermodynamically stable, and property-aligned, achieving higher hit rates and improved Pareto front quality relative to generative and LLM-only baselines. Ablation studies confirm the importance of rule-guided generation, memory-based refinement, and surrogate prediction. By enforcing synthesizability and multi-objective trade-offs, LLEMA provides a principled approach to accelerating practical materials discovery. Project website: https://scientific-discovery.github.io/llema-project/...

---

### 2. Inverse-design of two-dimensional magnonic crystals via topology optimization with frequency-domain micromagnetics

**Authors:** Ryunosuke Nagaoka, Takahiro Yamazaki, Chiharu Mitsumata, Yuma Iwasaki, Masato Kotsugi

**Published:** 2026-03-05

**Category:** cond-mat.mtrl-sci

**ID:** 2603.05132v1

**Link:** [http://arxiv.org/abs/2603.05132v1](http://arxiv.org/abs/2603.05132v1)

**Summary:** Magnonic crystals (MCs) are emerging spintronic metamaterials capable of manipulating transmission properties of magnons, the quanta of spin waves. Due to the complex relationship between lattice geometry and magnonic band dispersion, it remains challenging to establish general design strategies for optimizing targeted properties in MCs. In this study, we demonstrated an inverse-design framework for two-dimensional MCs to explore unconventional lattice structures with large magnonic band gaps. We employed genetic algorithms to enable global exploration of structures with a complete band gap as the objective property, and used frequency-domain micromagnetic simulations for computationally efficient band gap evaluation. Our established inverse-design method successfully discovered several previously unreported designs of MCs, whose performance was validated using time-domain micromagnetic simulations. Furthermore, we observed that the design landscape becomes increasingly non-convex at high-order bands, suggesting the existence of multiple design solutions. The overall inverse-design framework is expected to be broadly applicable to experimentally accessible material systems and device dimensions, facilitating the formulation of design rules for MCs....

---

### 3. Overcoming the Combinatorial Bottleneck in Symmetry-Driven Crystal Structure Prediction

**Authors:** Shi Yin, Jinming Mu, Xudong Zhu, Lixin He

**Published:** 2026-02-19

**Category:** cond-mat.mtrl-sci

**ID:** 2602.17176v2

**Link:** [http://arxiv.org/abs/2602.17176v2](http://arxiv.org/abs/2602.17176v2)

**Summary:** Crystal structure prediction (CSP), which aims to predict the three-dimensional atomic arrangement of a crystal from its composition, is central to materials discovery and mechanistic understanding. However, given the composition and atomic counts in a unit cell, existing methods struggle with the NP-hard combinatorial challenge of rigorous symmetry enforcement or rely on retrieving known templates, which inherently limits both physical fidelity and the ability to discover genuinely new materials. To solve this, we propose a symmetry-driven generative framework. Our approach leverages large language models to encode chemical semantics and directly generate fine-grained Wyckoff patterns from atomic stoichiometry and counts, effectively circumventing the limitations inherent to database lookups. Crucially, to overcome the exponentially complex problem of combinatorial site assignments, we incorporate domain knowledge through an efficient, linear-complexity heuristic beam search algorithm that rigorously enforces algebraic consistency between site multiplicities and atomic stoichiometry and counts. By integrating this symmetry-consistent template into a diffusion backbone, our approach constrains the stochastic generative trajectory to a physically valid geometric manifold. This framework achieves state-of-the-art performance across stability, uniqueness, and novelty (SUN) benchmarks, alongside superior matching performance, thereby establishing a new paradigm for the rigorous exploration of targeted crystallographic space which can be previously uncharted, with no reliance on existing databases or a priori structural knowledge....

---

### 4. Lang2Str: Two-Stage Crystal Structure Generation with LLMs and Continuous Flow Models

**Authors:** Cong Liu, Chengyue Gong, Zhenyu Liu, Jiale Zhao, Yuxuan Zhang

**Published:** 2026-03-04

**Category:** cs.LG

**ID:** 2603.03946v1

**Link:** [http://arxiv.org/abs/2603.03946v1](http://arxiv.org/abs/2603.03946v1)

**Summary:** Generative models hold great promise for accelerating material discovery but are often limited by their inflexible single-stage generative process in designing valid and diverse materials. To address this, we propose a two-stage generative framework, Lang2Str, that combines the strengths of large language models (LLMs) and flow-based models for flexible and precise material generation. Our method frames the generative process as a conditional generative task, where an LLM provides high-level conditions by generating descriptions of material unit cells' geometric layouts and properties. These descriptions, informed by the LLM's extensive background knowledge, ensure reasonable structure designs. A conditioned flow model then decodes these textual conditions into precise continuous coordinates and unit cell parameters. This staged approach combines the structured reasoning of LLMs and the distribution modeling capabilities of flow models. Experimental results show that our method achieves competitive performance on \textit{ab initio} material generation and crystal structure prediction tasks, with generated structures exhibiting closer alignment to ground truth in both geometry and energy levels, surpassing state-of-the-art models. The flexibility and modularity of our framework further enable fine-grained control over the generation process, potentially leading to more efficient and customizable material design....

---

### 5. Crystal-GFN: sampling crystals with desirable properties and constraints

**Authors:** Mila AI4Science, :, Alex Hernandez-Garcia, Alexandre Duval, Alexandra Volokhova, Yoshua Bengio, Divya Sharma, Pierre Luc Carrier, Yasmine Benabed, Michał Koziarski, Victor Schmidt, Gian-Marco Rignanese, Pierre-Paul De Breuck, Paulette Clancy

**Published:** 2023-10-07

**Category:** cs.LG

**ID:** 2310.04925v3

**Link:** [http://arxiv.org/abs/2310.04925v3](http://arxiv.org/abs/2310.04925v3)

**Summary:** The discovery of novel solid-state materials, such as electrocatalysts, super-ionic conductors, or photovoltaic materials, plays a critical role in addressing various global challenges. It has, for instance, the potential to significantly improve the efficiency of renewable energy production and storage, thereby making substantial contributions to climate crisis mitigation strategies. In this paper, we introduce Crystal-GFN, a generative model of crystal structures possessing desirable properties and constraints. Operating as a multi-environment, continuous-discrete GFlowNet, it sequentially samples structural attributes of crystalline materials, namely space group, composition and lattice parameters. This domain-inspired approach enables the flexible incorporation of physicochemical and geometric hard constraints. We demonstrate the capabilities of Crystal-GFN to efficiently discover diverse and valid crystals with various properties: low predicted formation energy (median -3.2 eV/atom), band gap close to a target value and high density. Overall, Crystal-GFN is a crystal generation method that addresses several existing challenges in the literature and opens promising paths for accelerating materials discovery with machine learning....

---


<!-- ARXIV_PAPERS_END -->