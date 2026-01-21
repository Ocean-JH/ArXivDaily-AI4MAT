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

*Last updated: 2026-01-22 06:23:16 (SGT)*

### 1. Generative Adversarial Networks for Resource State Generation

**Authors:** Shahbaz Shaik, Sourav Chatterjee, Sayantan Pramanik, Indranil Chakrabarty

**Published:** 2026-01-20

**Category:** quant-ph

**ID:** 2601.13708v1

**Link:** [http://arxiv.org/abs/2601.13708v1](http://arxiv.org/abs/2601.13708v1)

**Summary:** We introduce a physics-informed Generative Adversarial Network framework that recasts quantum resource-state generation as an inverse-design task. By embedding task-specific utility functions into training, the model learns to generate valid two-qubit states optimized for teleportation and entanglement broadcasting. Comparing decomposition-based and direct-generation architectures reveals that structural enforcement of Hermiticity, trace-one, and positivity yields higher fidelity and training stability than loss-only approaches. The framework reproduces theoretical resource boundaries for Werner-like and Bell-diagonal states with fidelities exceeding ~98%, establishing adversarial learning as a lightweight yet effective method for constraint-driven quantum-state discovery. This approach provides a scalable foundation for automated design of tailored quantum resources for information-processing applications, exemplified with teleportation and broadcasting of entanglement, and it opens up the possibility of using such states in efficient quantum network design....

---

### 2. Multi-objective fluorescent molecule design with a data-physics dual-driven generative framework

**Authors:** Yanheng Li, Zhichen Pu, Lijiang Yang, Zehao Zhou, Yi Qin Gao

**Published:** 2026-01-20

**Category:** cs.LG

**ID:** 2601.13564v1

**Link:** [http://arxiv.org/abs/2601.13564v1](http://arxiv.org/abs/2601.13564v1)

**Summary:** Designing fluorescent small molecules with tailored optical and physicochemical properties requires navigating vast, underexplored chemical space while satisfying multiple objectives and constraints. Conventional generate-score-screen approaches become impractical under such realistic design specifications, owing to their low search efficiency, unreliable generalizability of machine-learning prediction, and the prohibitive cost of quantum chemical calculation. Here we present LUMOS, a data-and-physics driven framework for inverse design of fluorescent molecules. LUMOS couples generator and predictor within a shared latent representation, enabling direct specification-to-molecule design and efficient exploration. Moreover, LUMOS combines neural networks with a fast time-dependent density functional theory (TD-DFT) calculation workflow to build a suite of complementary predictors spanning different trade-offs in speed, accuracy, and generalizability, enabling reliable property prediction across diverse scenarios. Finally, LUMOS employs a property-guided diffusion model integrated with multi-objective evolutionary algorithms, enabling de novo design and molecular optimization under multiple objectives and constraints. Across comprehensive benchmarks, LUMOS consistently outperforms baseline models in terms of accuracy, generalizability and physical plausibility for fluorescence property prediction, and demonstrates superior performance in multi-objective scaffold- and fragment-level molecular optimization. Further validation using TD-DFT and molecular dynamics (MD) simulations demonstrates that LUMOS can generate valid fluorophores that meet various target specifications. Overall, these results establish LUMOS as a data-physics dual-driven framework for general fluorophore inverse design....

---

### 3. RAG: A Random-Forest-Based Generative Design Framework for Uncertainty-Aware Design of Metamaterials with Complex Functional Response Requirements

**Authors:** Bolin Chen, Dex Doksoo Lee, Wei "Wayne'' Chen, Wei Chen

**Published:** 2026-01-19

**Category:** cs.AI

**ID:** 2601.13233v1

**Link:** [http://arxiv.org/abs/2601.13233v1](http://arxiv.org/abs/2601.13233v1)

**Summary:** Metamaterials design for advanced functionality often entails the inverse design on nonlinear and condition-dependent responses (e.g., stress-strain relation and dispersion relation), which are described by continuous functions. Most existing design methods focus on vector-valued responses (e.g., Young's modulus and bandgap width), while the inverse design of functional responses remains challenging due to their high-dimensionality, the complexity of accommodating design requirements in inverse-design frameworks, and non-existence or non-uniqueness of feasible solutions. Although generative design approaches have shown promise, they are often data-hungry, handle design requirements heuristically, and may generate infeasible designs without uncertainty quantification. To address these challenges, we introduce a RAndom-forest-based Generative approach (RAG). By leveraging the small-data compatibility of random forests, RAG enables data-efficient predictions of high-dimensional functional responses. During the inverse design, the framework estimates the likelihood through the ensemble which quantifies the trustworthiness of generated designs while reflecting the relative difficulty across different requirements. The one-to-many mapping is addressed through single-shot design generation by sampling from the conditional likelihood. We demonstrate RAG on: 1) acoustic metamaterials with prescribed partial passbands/stopbands, and 2) mechanical metamaterials with targeted snap-through responses, using 500 and 1057 samples, respectively. Its data-efficiency is benchmarked against neural networks on a public mechanical metamaterial dataset with nonlinear stress-strain relations. Our framework provides a lightweight, trustworthy pathway to inverse design involving functional responses, expensive simulations, and complex design requirements, beyond metamaterials....

---

### 4. Artificial Intelligence in Materials Science and Engineering: Current Landscape, Key Challenges, and Future Trajectorie

**Authors:** Iman Peivaste, Salim Belouettar, Francesco Mercuri, Nicholas Fantuzzi, Hamidreza Dehghani, Razieh Izadi, Halliru Ibrahim, Jakub Lengiewicz, Maël Belouettar-Mathis, Kouider Bendine, Ahmed Makradi, Martin Hörsch, Peter Klein, Mohamed El Hachemi, Heinz A. Preisig, Yacine Rezgui, Natalia Konchakova, Ali Daouadji

**Published:** 2026-01-18

**Category:** cond-mat.mtrl-sci

**ID:** 2601.12554v1

**Link:** [http://arxiv.org/abs/2601.12554v1](http://arxiv.org/abs/2601.12554v1)

**Summary:** Artificial Intelligence is rapidly transforming materials science and engineering, offering powerful tools to navigate complexity, accelerate discovery, and optimize material design in ways previously unattainable. Driven by the accelerating pace of algorithmic advancements and increasing data availability, AI is becoming an essential competency for materials researchers. This review provides a comprehensive and structured overview of the current landscape, synthesizing recent advancements and methodologies for materials scientists seeking to effectively leverage these data-driven techniques. We survey the spectrum of machine learning approaches, from traditional algorithms to advanced deep learning architectures, including CNNs, GNNs, and Transformers, alongside emerging generative AI and probabilistic models such as Gaussian Processes for uncertainty quantification. The review also examines the pivotal role of data in this field, emphasizing how effective representation and featurization strategies, spanning compositional, structural, image-based, and language-inspired approaches, combined with appropriate preprocessing, fundamentally underpin the performance of machine learning models in materials research. Persistent challenges related to data quality, quantity, and standardization, which critically impact model development and application in materials science and engineering, are also addressed....

---


<!-- ARXIV_PAPERS_END -->