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

*Last updated: 2026-05-02 06:48:16 (SGT)*

### 1. Hyper-Dimensional Fingerprints as Molecular Representations

**Authors:** Jonas Teufel, Luca Torresi, André Eberhard, Pascal Friederich

**Published:** 2026-04-30

**Category:** cs.LG

**ID:** 2604.27810v1

**Link:** [http://arxiv.org/abs/2604.27810v1](http://arxiv.org/abs/2604.27810v1)

**Summary:** Computational molecular representations underpin virtual screening, property prediction, and materials discovery. Conventional fingerprints are efficient and deterministic but lose structural information through hash-based compression, particularly at low dimensionalities. Learned representations from graph neural networks recover this expressiveness but require task-specific training and substantial computational resources. Here we introduce hyperdimensional fingerprints (HDF), which replace the learned transformations of message-passing neural networks with algebraic operations on high-dimensional vectors, producing deterministic molecular representations without any training. Across diverse property prediction benchmarks, HDF outperforms conventional fingerprints in the majority of tasks while exhibiting greater consistency across datasets and models. Crucially, HDF embeddings preserve molecular similarity faithfully: at 32 dimensions, distances in HDF space achieve a 0.9 Pearson correlation with graph edit distance, compared to 0.55 for Morgan fingerprints at equivalent size. This structural fidelity persists at low dimensions where hash-based methods degrade, allowing simple nearest-neighbor regression to remain predictive with as few as 64 components. We further demonstrate the practical impact in Bayesian molecular optimization, where HDF-based surrogate models achieve substantially improved sample efficiency in regimes where Morgan fingerprints perform comparably to random search. HDF thus provides a general-purpose, training-free alternative to conventional molecular fingerprints, suggesting that the information loss long accepted as inherent to fixed-length fingerprints is a limitation of the hash-based encoding scheme rather than the fingerprint paradigm itself....

---

### 2. Generative structure search for efficient and diverse discovery of molecular and crystal structures

**Authors:** Yifang Qin, Yu Shi, Junfu Tan, Chang Liu, Ming Zhang, Ziheng Lu

**Published:** 2026-04-30

**Category:** cs.AI

**ID:** 2604.27636v1

**Link:** [http://arxiv.org/abs/2604.27636v1](http://arxiv.org/abs/2604.27636v1)

**Summary:** Predicting stable and metastable structures is central to molecular and materials discovery, but remains limited by the cost of searching high-dimensional energy landscapes. Deep generative models offer efficient structure sampling, yet their outputs remain shaped by training data and can underexplore minima that are rare but physically relevant. We introduce generative structure search (GSS), a unified framework that formulates diffusion-based generation and random structure search (RSS) as limiting regimes of a common sampling process driven by learned score fields and physical forces. Coupling these drivers lets GSS use data priors to accelerate sampling while retaining energy-guided exploration of local minima. Across molecular and crystalline systems, GSS recovers diverse metastable structures with more than tenfold lower sampling cost than RSS for broad coverage and remains effective for compositions outside the training distribution. The results establish a physically grounded generative search strategy for discovering structures beyond the reach of data-driven sampling alone....

---

### 3. AMGenC: Generating Charge Balanced Amorphous Materials

**Authors:** Yan Lin, Jilin Hu, N. M. Anoop Krishnan, Morten M. Smedskjaer

**Published:** 2026-04-30

**Category:** cs.LG

**ID:** 2604.27613v1

**Link:** [http://arxiv.org/abs/2604.27613v1](http://arxiv.org/abs/2604.27613v1)

**Summary:** Amorphous (disordered) materials are solids that have shown great potential in various domains, including energy storage, thermal management, and advanced materials. Unlike crystalline materials that can be described by unit cells containing a few to hundreds of atoms, amorphous materials require larger simulation cells with at least hundreds to thousands of atoms. To advance the design of amorphous materials with desired properties and facilitate the exploration of their vast design space, generative inverse design has emerged as a promising approach. It aims to directly output materials with properties closely aligned with the desired ones using probabilistic generative models conditioned on desired properties, which can be more resource efficient than the traditional trial-and-error approach. However, due to the inherent stochasticity of probabilistic generative models, when element assignments are unconstrained, a large portion of generated materials may be charge unbalanced, and no existing methods can effectively mitigate this limitation. In this work, we propose AMGenC, a new generative inverse design method for amorphous materials that can guarantee the generation of charge balanced samples, with minimal additional computational overhead and without sacrificing inverse design accuracy. AMGenC achieves this through an element noise that gives the generation process a starting point centered around charge balance, and the combination of a per-step soft projection and a final discrete projection for steering the elements toward exact charge balance throughout the generation. We perform extensive experiments on two amorphous materials datasets. Experimental results provide evidence that AMGenC achieves its design goal....

---

### 4. METASYMBO: Multi-Agent Language-Guided Metamaterial Discovery via Symbolic Latent Evolution

**Authors:** Jianpeng Chen, Wangzhi Zhan, Dongqi Fu, Junkai Zhang, Zian Jia, Ling Li, Wei Wang, Dawei Zhou

**Published:** 2026-04-30

**Category:** cs.AI

**ID:** 2604.27300v1

**Link:** [http://arxiv.org/abs/2604.27300v1](http://arxiv.org/abs/2604.27300v1)

**Summary:** Metamaterial discovery seeks microstructured materials whose geometry induces targeted mechanical behavior. Existing inverse-design methods can efficiently generate candidates, but they typically require explicit numerical property targets and are less suitable for early-stage exploration, where researchers often begin with incomplete constraints and qualitative intents expressed in natural language. Large language models can interpret such intents, but they lack geometric awareness and physical property validity. To address this gap, we propose MetaSymbO, a multi-agent framework for language-guided Metamaterial discovery via Symbolic-driven latent evOlution. Specifically, MetaSymbO contains three agents: a Designer that interprets free-form design intents and retrieves a semantically consistent scaffold, a Generator that synthesizes candidate microstructures in a disentangled latent space, and a Supervisor that provides fast property-aware feedback for iterative refinement. To move beyond the limitations of reproducing known samples from literature and training data, we further introduce symbolic-driven latent evolution, which applies programmable operators over disentangled latent factors to compose, modify, and refine structures at inference time. Extensive experiments demonstrate that (i) MetaSymbO improves structural validity by up to 34% in symmetry and nearly 98% in periodicity compared to state-of-the-art baselines; (ii) MetaSymbO achieves about 6-7% higher language-guidance scores while maintaining superior structure novelty compared to advanced reasoning LLMs; (iii) qualitative analyses confirm the effectiveness of symbolic logic operators in enabling programmable semantic alignment; and (iv) realworld case studies on auxetic, high-stiffness metamaterial design further validate its practical capability....

---


<!-- ARXIV_PAPERS_END -->