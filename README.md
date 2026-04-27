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

*Last updated: 2026-04-28 06:50:23 (SGT)*

### 1. Algebraic Language Models for Inverse Design of Metamaterials via Diffusion Transformers

**Authors:** Li Zheng, Siddhant Kumar, Dennis M. Kochmann

**Published:** 2025-07-21

**Category:** cs.CE

**ID:** 2507.15753v3

**Link:** [http://arxiv.org/abs/2507.15753v3](http://arxiv.org/abs/2507.15753v3)

**Summary:** Generative machine learning models have revolutionized material discovery by capturing complex structure-property relationships, yet extending these approaches to the inverse design of three-dimensional metamaterials remains limited by computational complexity and underexplored design spaces due to the lack of expressive representations. Here we present DiffuMeta, a generative framework integrating diffusion transformers with an algebraic language representation, encoding three-dimensional geometries as mathematical sentences. This compact, unified parameterization spans diverse topologies, enabling the direct application of transformers to structural design. DiffuMeta leverages diffusion models to generate new shell structures with precisely targeted stress-strain responses under large deformations, accounting for buckling and contact while addressing the inherent one-to-many mapping by producing diverse solutions. Uniquely, our approach enables simultaneous control over multiple mechanical objectives, including linear and nonlinear responses beyond training domains. Experimental validation of fabricated structures further confirms the efficacy of our approach for accelerated design of metamaterials and structures with tailored properties....

---

### 2. Parameter-Efficient Conditioning for Material Generalization in Graph-Based Simulators

**Authors:** Naveen Raj Manoharan, Hassan Iqbal, Krishna Kumar

**Published:** 2025-11-07

**Category:** cs.LG

**ID:** 2511.05456v2

**Link:** [http://arxiv.org/abs/2511.05456v2](http://arxiv.org/abs/2511.05456v2)

**Summary:** Graph network-based simulators (GNS) have demonstrated strong potential for learning particle-based physics (such as fluids, deformable solids, and granular flows) while generalizing to unseen geometries due to their inherent inductive biases. However, existing models are typically trained for a single material type and fail to generalize across distinct constitutive behaviors, limiting their applicability in real-world engineering settings. Using granular flows as a running example, we propose a parameter-efficient conditioning mechanism that makes the GNS model adaptive to material parameters. We identify that sensitivity to material properties is concentrated in the early message-passing (MP) layers, a finding we link to the local nature of constitutive models (e.g., Mohr-Coulomb) and their effects on information propagation. We empirically validate this by showing that fine-tuning only the first few (1-5) of 10 MP layers of a pretrained model achieves comparable test performance as compared to fine-tuning the entire network. Building on this insight, we propose a parameter-efficient Feature-wise Linear Modulation (FiLM) conditioning mechanism designed to specifically target these early layers. This approach produces accurate long-term rollouts on unseen, interpolated, or moderately extrapolated values (e.g., up to 2.5 degrees for friction angle and 0.25 kPa for cohesion) when trained exclusively on as few as 12 short simulation trajectories from new materials, representing a 5-fold data reduction compared to a baseline multi-task learning method. Finally, we validate the model's utility by applying it to an inverse problem, successfully identifying unknown cohesion parameters from trajectory data. This approach enables the use of GNS in inverse design and closed-loop control tasks where material properties are treated as design variables....

---


<!-- ARXIV_PAPERS_END -->