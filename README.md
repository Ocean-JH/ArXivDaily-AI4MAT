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

## New Papers (4)

*Last updated: 2026-05-01 06:52:12 (SGT)*

### 1. Inverting Foundation Models of Brain Function with Simulation-Based Inference

**Authors:** Niels Bracher, Xavier Intes, Stefan T. Radev

**Published:** 2026-04-26

**Category:** cs.LG

**ID:** 2604.23865v2

**Link:** [http://arxiv.org/abs/2604.23865v2](http://arxiv.org/abs/2604.23865v2)

**Summary:** Foundation models of brain activity promise a new frontier for in silico neuroscience by emulating neural responses to complex stimuli across tasks and modalities. A natural next step is to ask whether these models can also be used in reverse. Can we recover a stimulus or its properties from synthetic brain activity? We study this question in a proof-of-concept setting using TRIBEv2. We pair the brain emulator with large language models (LLMs) that generate news headlines from linguistic parameters such as valence, arousal, and dominance. We then use simulation-based inference to learn a probabilistic mapping from brain maps to latent stimulus parameters. Our results show that these parameters can be recovered from predicted brain maps, validating the quality of neural encodings. They also show that LLMs can serve as controllable stimulus generators for simulated experiments. Together, these findings provide a step toward decoding and inverse design with foundation brain models....

---

### 2. Generative design of inorganic materials

**Authors:** Jose Recatala-Gomez, Haiwen Dai, Zhu Ruiming, Nikita Kazeev, Nong Wei, Gang Wu, Maciej Koperski, Tan Teck Leong, Andrey Ustyuzhanin, Gerbrand Ceder, Kostya Novoselov, Kedar Hippalgaonkar

**Published:** 2026-04-15

**Category:** cond-mat.mtrl-sci

**ID:** 2604.14082v4

**Link:** [http://arxiv.org/abs/2604.14082v4](http://arxiv.org/abs/2604.14082v4)

**Summary:** Materials discovery is fundamental to advance next-generation technologies as well as for sustainable and circular economy. Beyond computational screening, generative models are efficient at finding materials with desired properties, via multi-modal learning using multiscale data. This perspective examines the landscape of generative design for inorganic materials and discusses the integration of multi-modal learning with high-throughput experimental validation. We contextualize these challenges through the lens of a generative design framework as a unified approach to address the data-driven inverse design of functional materials. The central idea of the framework is constructed around a foundation AI model for inorganic materials interlinked deeply with various property databases and high-throughput experiments via a machine learning driven closed loop, which enables the framework to solve key challenges in functional materials. We argue that domain-specific implementations of such integrated workflows represent a promising pathway toward the unresolved challenge of data-driven inverse design for atom-engineered inorganic functional materials....

---

### 3. Agentic Fusion of Large Atomic and Language Models to Accelerate Superconductors Discovery

**Authors:** Mingze Li, Yu Rong, Songyou Li, Lihong Wang, Jiacheng Cen, Liming Wu, Anyi Li, Zongzhao Li, Qiuliang Liu, Rui Jiao, Tian Bian, Pengju Wang, Hao Sun, Jianfeng Zhang, Ji-Rong Wen, Deli Zhao, Shifeng Jin, Tingyang Xu, Wenbing Huang

**Published:** 2026-04-26

**Category:** cs.LG

**ID:** 2604.23758v2

**Link:** [http://arxiv.org/abs/2604.23758v2](http://arxiv.org/abs/2604.23758v2)

**Summary:** The discovery of novel materials is critical for global energy and quantum technology transitions. While deep learning has fundamentally reshaped this landscape, existing predictive or generative models typically operate in isolation, lacking the autonomous orchestration required to execute the full discovery process. Here we present ElementsClaw, an agentic framework for materials discovery that synergizes Large Atomic Models (LAMs) with Large Language Models (LLMs). In response to varied human queries, ElementsClaw orchestrates a suite of LAM tools finetuned from our proposed 1-billion-parameter model Elements for atomic-scale numerical computation, while leveraging LLMs for high-level semantic reasoning. This shift moves AI-driven materials science from isolated processes toward integrated and human interactive discovery. Applied to superconductors, ElementsClaw screens 2.4 million crystals in just 28 GPU hours to identify 68,000 high-confidence candidates (The complete dataset of screened superconductors is available at https://developer.damo-academy.com/material), expanding known superconducting space by orders of magnitude compared to datasets curated over decades. Critically, ElementsClaw achieves a high success rate in identifying superconductors hidden in literature and discovers four novel experimentally verified superconductors, exemplified by Zr3ScRe8 with a transition temperature of 6.8 K and HfZrRe4 at 6.7 K. Together, our results establish a knowledge integrated, autonomously orchestrated, and experimentally grounded paradigm for materials discovery....

---

### 4. A Category-Theoretic Framework from Biological Mechanics to Engineered Stimulus-Response Systems

**Authors:** Lee Marom, Skylar Tibbits, Gioele Zardini, Markus J. Buehler

**Published:** 2026-04-29

**Category:** cond-mat.soft

**ID:** 2604.26367v1

**Link:** [http://arxiv.org/abs/2604.26367v1](http://arxiv.org/abs/2604.26367v1)

**Summary:** Natural materials achieve adaptive behavior through hierarchical organization and coupled mechanisms across scales. Their translation into engineering, however, remains largely heuristic. What is missing is a formal translation framework that carries biological design logic into engineered realization while preserving physical consistency across levels of abstraction. Here we present a category theoretic compositional framework for verified nature-derived design. The framework defines a category of stimulus response dynamical systems with natural and artificial subcategories. It introduces a structure preserving implementation functor from biological mechanics to engineered systems. It also formalizes a machine agnostic specification layer that links behavioral intent to executable fabrication programs. We instantiate the framework on the hygromorphic pinecone hierarchy as a representative biological case. We implement the full pipeline in Grasshopper, where formal specifications are translated into modular parametric scripts that preserve the compositional structure of the model. The resulting designs are fabricated by fused filament fabrication, evaluated experimentally, and tested against model predictions derived from the pipeline. The current implementation generates four actuator classes spanning two stimulus types and two kinematic responses. One actuator arises purely through composition from previously validated components, without additional manual derivation. The results show that compositionality can function not just as a descriptive language, but as a generative and system level verifiable method for mechanical material design. More broadly, the work provides a concrete route for embedding formal multiscale reasoning within increasingly computational, generative, and physics-driven design workflows....

---


<!-- ARXIV_PAPERS_END -->