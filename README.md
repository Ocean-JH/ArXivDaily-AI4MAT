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

*Last updated: 2025-07-24 06:18:40 (SGT)*

### 1. Perovskite-R1: A Domain-Specialized LLM for Intelligent Discovery of Precursor Additives and Experimental Design

**Authors:** Xin-De Wang, Zhi-Rui Chen, Peng-Jie Guo, Ze-Feng Gao, Cheng Mu, Zhong-Yi Lu

**Published:** 2025-07-22

**Category:** cs.LG

**ID:** 2507.16307v1

**Link:** [http://arxiv.org/abs/2507.16307v1](http://arxiv.org/abs/2507.16307v1)

**Summary:** Perovskite solar cells (PSCs) have rapidly emerged as a leading contender in
next-generation photovoltaic technologies, owing to their exceptional power
conversion efficiencies and advantageous material properties. Despite these
advances, challenges such as long-term stability, environmental sustainability,
and scalable manufacturing continue to hinder their commercialization.
Precursor additive engineering has shown promise in addressing these issues by
enhancing both the performance and durability of PSCs. However, the explosive
growth of scientific literature and the complex interplay of materials,
processes, and device architectures make it increasingly difficult for
researchers to efficiently access, organize, and utilize domain knowledge in
this rapidly evolving field. To address this gap, we introduce Perovskite-R1, a
specialized large language model (LLM) with advanced reasoning capabilities
tailored for the discovery and design of PSC precursor additives. By
systematically mining and curating 1,232 high-quality scientific publications
and integrating a comprehensive library of 33,269 candidate materials, we
constructed a domain-specific instruction-tuning dataset using automated
question-answer generation and chain-of-thought reasoning. Fine-tuning the
QwQ-32B model on this dataset resulted in Perovskite-R1, which can
intelligently synthesize literature insights and generate innovative and
practical solutions for defect passivation and the selection of precursor
additives. Experimental validation of several model-proposed strategies
confirms their effectiveness in improving material stability and performance.
Our work demonstrates the potential of domain-adapted LLMs in accelerating
materials discovery and provides a closed-loop framework for intelligent,
data-driven advancements in perovskite photovoltaic research....

---

### 2. DiffuMeta: Algebraic Language Models for Inverse Design of Metamaterials via Diffusion Transformers

**Authors:** Li Zheng, Siddhant Kumar, Dennis M. Kochmann

**Published:** 2025-07-21

**Category:** cs.CE

**ID:** 2507.15753v1

**Link:** [http://arxiv.org/abs/2507.15753v1](http://arxiv.org/abs/2507.15753v1)

**Summary:** Generative machine learning models have revolutionized material discovery by
capturing complex structure-property relationships, yet extending these
approaches to the inverse design of three-dimensional metamaterials remains
limited by computational complexity and underexplored design spaces due to the
lack of expressive representations. Here, we present DiffuMeta, a generative
framework integrating diffusion transformers with a novel algebraic language
representation, encoding 3D geometries as mathematical sentences. This compact,
unified parameterization spans diverse topologies while enabling direct
application of transformers to structural design. DiffuMeta leverages diffusion
models to generate novel shell structures with precisely targeted stress-strain
responses under large deformations, accounting for buckling and contact while
addressing the inherent one-to-many mapping by producing diverse solutions.
Uniquely, our approach enables simultaneous control over multiple mechanical
objectives, including linear and nonlinear responses beyond training domains.
Experimental validation of fabricated structures further confirms the efficacy
of our approach for accelerated design of metamaterials and structures with
tailored properties....

---

### 3. DREAMS: Density Functional Theory Based Research Engine for Agentic Materials Simulation

**Authors:** Ziqi Wang, Hongshuo Huang, Hancheng Zhao, Changwen Xu, Shang Zhu, Jan Janssen, Venkatasubramanian Viswanathan

**Published:** 2025-07-18

**Category:** cs.AI

**ID:** 2507.14267v1

**Link:** [http://arxiv.org/abs/2507.14267v1](http://arxiv.org/abs/2507.14267v1)

**Summary:** Materials discovery relies on high-throughput, high-fidelity simulation
techniques such as Density Functional Theory (DFT), which require years of
training, extensive parameter fine-tuning and systematic error handling. To
address these challenges, we introduce the DFT-based Research Engine for
Agentic Materials Screening (DREAMS), a hierarchical, multi-agent framework for
DFT simulation that combines a central Large Language Model (LLM) planner agent
with domain-specific LLM agents for atomistic structure generation, systematic
DFT convergence testing, High-Performance Computing (HPC) scheduling, and error
handling. In addition, a shared canvas helps the LLM agents to structure their
discussions, preserve context and prevent hallucination. We validate DREAMS
capabilities on the Sol27LC lattice-constant benchmark, achieving average
errors below 1\% compared to the results of human DFT experts. Furthermore, we
apply DREAMS to the long-standing CO/Pt(111) adsorption puzzle, demonstrating
its long-term and complex problem-solving capabilities. The framework again
reproduces expert-level literature adsorption-energy differences. Finally,
DREAMS is employed to quantify functional-driven uncertainties with Bayesian
ensemble sampling, confirming the Face Centered Cubic (FCC)-site preference at
the Generalized Gradient Approximation (GGA) DFT level. In conclusion, DREAMS
approaches L3-level automation - autonomous exploration of a defined design
space - and significantly reduces the reliance on human expertise and
intervention, offering a scalable path toward democratized, high-throughput,
high-fidelity computational materials discovery....

---


<!-- ARXIV_PAPERS_END -->