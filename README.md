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

*Last updated: 2026-03-19 06:30:39 (SGT)*

### 1. Controllable Graph Generation with Diffusion Models via Inference-Time Tree Search Guidance

**Authors:** Jiachi Zhao, Zehong Wang, Yamei Liao, Chuxu Zhang, Yanfang Ye

**Published:** 2025-10-12

**Category:** cs.LG

**ID:** 2510.10402v2

**Link:** [http://arxiv.org/abs/2510.10402v2](http://arxiv.org/abs/2510.10402v2)

**Summary:** Graph generation is a fundamental problem in graph learning with broad applications across Web-scale systems, knowledge graphs, and scientific domains such as drug and material discovery. Recent approaches leverage diffusion models for step-by-step generation, yet unconditional diffusion offers little control over desired properties, often leading to unstable quality and difficulty in incorporating new objectives. Inference-time guidance methods mitigate these issues by adjusting the sampling process without retraining, but they remain inherently local, heuristic, and limited in controllability. To overcome these limitations, we propose TreeDiff, a Monte Carlo Tree Search (MCTS) guided dual-space diffusion framework for controllable graph generation. TreeDiff is a plug-and-play inference-time method that expands the search space while keeping computation tractable. Specifically, TreeDiff introduces three key designs to make it practical and scalable: (1) a macro-step expansion strategy that groups multiple denoising updates into a single transition, reducing tree depth and enabling long-horizon exploration; (2) a dual-space denoising mechanism that couples efficient latent-space denoising with lightweight discrete correction in graph space, ensuring both scalability and structural fidelity; and (3) a dual-space verifier that predicts long-term rewards from partially denoised graphs, enabling early value estimation and removing the need for full rollouts. Extensive experiments on 2D and 3D molecular generation benchmarks, under both unconditional and conditional settings, demonstrate that TreeDiff achieves state-of-the-art performance. Notably, TreeDiff exhibits favorable inference-time scaling: it continues to improve with additional computation, while existing inference-time methods plateau early under limited resources....

---

### 2. Generative Inverse Design with Abstention via Diagonal Flow Matching

**Authors:** Miguel de Campos, Werner Krebs, Hanno Gottschalk

**Published:** 2026-03-16

**Category:** cs.LG

**ID:** 2603.15925v1

**Link:** [http://arxiv.org/abs/2603.15925v1](http://arxiv.org/abs/2603.15925v1)

**Summary:** Inverse design aims to find design parameters $x$ achieving target performance $y^*$. Generative approaches learn bidirectional mappings between designs and labels, enabling diverse solution sampling. However, standard conditional flow matching (CFM), when adapted to inverse problems by pairing labels with design parameters, exhibits strong sensitivity to their arbitrary ordering and scaling, leading to unstable training. We introduce Diagonal Flow Matching (Diag-CFM), which resolves this through a zero-anchoring strategy that pairs design coordinates with noise and labels with zero, making the learning problem provably invariant to coordinate permutations. This yields order-of-magnitude improvements in round-trip accuracy over CFM and invertible neural network baselines across design dimensions up to $P{=}100$. We develop two architecture-intrinsic uncertainty metrics, Zero-Deviation and Self-Consistency, that enable three practical capabilities: selecting the best candidate among multiple generations, abstaining from unreliable predictions, and detecting out-of-distribution targets; consistently outperforming ensemble and general-purpose alternatives across all tasks. We validate on airfoil, gas turbine combustor, and an analytical benchmark with scalable design dimension....

---

### 3. LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation

**Authors:** AI Scientists, Xinyi Lin, Danqing Yin, Ying Guo

**Published:** 2026-03-16

**Category:** cond-mat.mtrl-sci

**ID:** 2603.15712v1

**Link:** [http://arxiv.org/abs/2603.15712v1](http://arxiv.org/abs/2603.15712v1)

**Summary:** CO2 reduction requires efficient catalysts, yet materials discovery remains bottlenecked by 10-20 year development cycles requiring deep domain expertise. This paper demonstrates how large language models can assist the catalyst discovery process by helping researchers explore chemical spaces and interpret results when augmented with retrieval-based grounding. We introduce a retrieval-augmented generation framework that enables GPT-4 to navigate chemical space by accessing a database of 50,000+ known materials, adapting general-purpose language understanding for high-throughput materials design. Our approach generated over 250 catalyst candidates with an 82% thermodynamic stability rate while addressing multi-objective constraints: 68% achieved <$100/kg cost with metallic conductivity (band gap<0.1eV) and mechanical stability (B/G>1.75). The best-performing Fe0.2Co0.2Ni0.2Ir0.1Ru0.3 achieves 0.285V limiting potential (25% improvement over IrO2), while Cr0.2Fe0.2Co0.3Ni0.2Mo0.1 optimally balances performance-cost trade-offs at $18/kg. Volcano plot analysis confirms that 78% of LLM-generated catalysts cluster near the theoretical activity optimum, while our system achieves 200x computational efficiency compared to traditional high-throughput screening. By demonstrating that retrieval-augmented generation can ground AI creativity in physical constraints without sacrificing exploration, this work demonstrates an approach where natural language interfaces can streamline materials discovery workflows, enabling researchers to explore chemical spaces more efficiently while the LLM assists in result interpretation and hypothesis generation....

---


<!-- ARXIV_PAPERS_END -->