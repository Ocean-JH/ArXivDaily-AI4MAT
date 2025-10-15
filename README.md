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

*Last updated: 2025-10-16 06:14:36 (SGT)*

### 1. Inverse Design in Nanophotonics via Representation Learning

**Authors:** Reza Marzban, Ali Adibi, Raphael Pestourie

**Published:** 2025-07-01

**Category:** physics.app-ph

**ID:** 2507.00546v2

**Link:** [http://arxiv.org/abs/2507.00546v2](http://arxiv.org/abs/2507.00546v2)

**Summary:** Inverse design in nanophotonics, the computational discovery of structures
achieving targeted electromagnetic (EM) responses, has become a key tool for
recent optical advances. Traditional intuition-driven or iterative optimization
methods struggle with the inherently high-dimensional, non-convex design spaces
and the substantial computational demands of EM simulations. Recently, machine
learning (ML) has emerged to address these bottlenecks effectively. This review
frames ML-enhanced inverse design methodologies through the lens of
representation learning, classifying them into two categories: output-side and
input-side approaches. Output-side methods use ML to learn a representation in
the solution space to create a differentiable solver that accelerates
optimization. Conversely, input-side techniques employ ML to learn compact,
latent-space representations of feasible device geometries, enabling efficient
global exploration through generative models. Each strategy presents unique
trade-offs in data requirements, generalization capacity, and novel design
discovery potentials. Hybrid frameworks that combine physics-based optimization
with data-driven representations help escape poor local optima, improve
scalability, and facilitate knowledge transfer. We conclude by highlighting
open challenges and opportunities, emphasizing complexity management,
geometry-independent representations, integration of fabrication constraints,
and advancements in multiphysics co-designs....

---

### 2. Generative Diffusion Model DiffCrysGen Discovers Rare Earth-Free Magnetic Materials

**Authors:** Sourav Mal, Nehad Ahmed, Subhankar Mishra, Prasenjit Sen

**Published:** 2025-10-14

**Category:** cond-mat.mtrl-sci

**ID:** 2510.12329v1

**Link:** [http://arxiv.org/abs/2510.12329v1](http://arxiv.org/abs/2510.12329v1)

**Summary:** Efficient exploration of the vast chemical space is a fundamental challenge
in materials discovery, particularly for designing functional inorganic
crystalline materials with targeted properties. Diffusion-based generative
models have emerged as a powerful route, but most existing approaches require
domain-specific constraints and separate diffusion processes for atom types,
atomic positions, and lattice parameters, adding complexity and limiting
efficiency. Here, we present DiffCrysGen, a fully data-driven, score-based
diffusion model that generates complete crystal structures in a single,
end-to-end diffusion process. This unified framework simplifies the model
architecture and accelerates sampling by two to three orders of magnitude
compared to existing methods without compromising chemical and structural
diversity of the generated materials. In order to demonstrate the efficacy of
DiffCrysGen in generating valid and useful materials, using density functional
theory (DFT), we validate a number of newly generated rare earth-free magnetic
materials that are energetically and dynamically stable, and are potentially
synthesizable. These include ferromagnets with high saturation magnetization
and large magnetocrystalline anisotropy, as also metallic antiferromagnets.
These results establish DiffCrysGen as a general platform for accelerated
functional materials discovery....

---

### 3. ToPolyAgent: AI Agents for Coarse-Grained Topological Polymer Simulations

**Authors:** Lijie Ding, Jan-Michael Carrillo, Changwoo Do

**Published:** 2025-10-14

**Category:** cs.AI

**ID:** 2510.12091v1

**Link:** [http://arxiv.org/abs/2510.12091v1](http://arxiv.org/abs/2510.12091v1)

**Summary:** We introduce ToPolyAgent, a multi-agent AI framework for performing
coarse-grained molecular dynamics (MD) simulations of topological polymers
through natural language instructions. By integrating large language models
(LLMs) with domain-specific computational tools, ToPolyAgent supports both
interactive and autonomous simulation workflows across diverse polymer
architectures, including linear, ring, brush, and star polymers, as well as
dendrimers. The system consists of four LLM-powered agents: a Config Agent for
generating initial polymer-solvent configurations, a Simulation Agent for
executing LAMMPS-based MD simulations and conformational analyses, a Report
Agent for compiling markdown reports, and a Workflow Agent for streamlined
autonomous operations. Interactive mode incorporates user feedback loops for
iterative refinements, while autonomous mode enables end-to-end task execution
from detailed prompts. We demonstrate ToPolyAgent's versatility through case
studies involving diverse polymer architectures under varying solvent
condition, thermostats, and simulation lengths. Furthermore, we highlight its
potential as a research assistant by directing it to investigate the effect of
interaction parameters on the linear polymer conformation, and the influence of
grafting density on the persistence length of the brush polymer. By coupling
natural language interfaces with rigorous simulation tools, ToPolyAgent lowers
barriers to complex computational workflows and advances AI-driven materials
discovery in polymer science. It lays the foundation for autonomous and
extensible multi-agent scientific research ecosystems....

---

### 4. Generative Deep Learning Framework for Inverse Design of Fuels

**Authors:** Kiran K. Yalamanchi, Pinaki Pal, Balaji Mohan, Abdullah S. AlRamadan, Jihad A. Badra, Yuanjiang Pei

**Published:** 2025-04-16

**Category:** cs.LG

**ID:** 2504.12075v3

**Link:** [http://arxiv.org/abs/2504.12075v3](http://arxiv.org/abs/2504.12075v3)

**Summary:** In the present work, a generative deep learning framework combining a
Co-optimized Variational Autoencoder (Co-VAE) architecture with quantitative
structure-property relationship (QSPR) techniques is developed to enable
accelerated inverse design of fuels. The Co-VAE integrates a property
prediction component coupled with the VAE latent space, enhancing molecular
reconstruction and accurate estimation of Research Octane Number (RON) (chosen
as the fuel property of interest). A subset of the GDB-13 database, enriched
with a curated RON database, is used for model training. Hyperparameter tuning
is further utilized to optimize the balance among reconstruction fidelity,
chemical validity, and RON prediction. An independent regression model is then
used to refine RON prediction, while a differential evolution algorithm is
employed to efficiently navigate the VAE latent space and identify promising
fuel molecule candidates with high RON. This methodology addresses the
limitations of traditional fuel screening approaches by capturing complex
structure-property relationships within a comprehensive latent representation.
The generative model can be adapted to different target properties, enabling
systematic exploration of large chemical spaces relevant to fuel design
applications. Furthermore, the demonstrated framework can be readily extended
by incorporating additional synthesizability criteria to improve applicability
and reliability for de novo design of new fuels....

---


<!-- ARXIV_PAPERS_END -->