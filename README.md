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

*Last updated: 2025-10-09 06:16:05 (SGT)*

### 1. MatLLMSearch: Crystal Structure Discovery with Evolution-Guided Large Language Models

**Authors:** Jingru Gan, Peichen Zhong, Yuanqi Du, Yanqiao Zhu, Chenru Duan, Haorui Wang, Daniel Schwalbe-Koda, Carla P. Gomes, Kristin A. Persson, Wei Wang

**Published:** 2025-02-28

**Category:** cond-mat.mtrl-sci

**ID:** 2502.20933v2

**Link:** [http://arxiv.org/abs/2502.20933v2](http://arxiv.org/abs/2502.20933v2)

**Summary:** Crystal structure generation is fundamental to materials science, enabling
the discovery of novel materials with desired properties. While existing
approaches leverage Large Language Models (LLMs) through extensive fine-tuning
on materials databases, we show that pre-trained LLMs can inherently generate
novel and stable crystal structures without additional fine-tuning. Our
framework employs LLMs as intelligent proposal agents within an evolutionary
pipeline that guides them to perform implicit crossover and mutation operations
while maintaining chemical validity. We demonstrate that MatLLMSearch achieves
a 78.38% metastable rate validated by machine learning interatomic potentials
and 31.7% DFT-verified stability, outperforming specialized models such as
CrystalTextLLM. Beyond crystal structure generation, we further demonstrate
that our framework adapts to diverse materials design tasks, including crystal
structure prediction and multi-objective optimization of properties such as
deformation energy and bulk modulus, all without fine-tuning. These results
establish our framework as a versatile and effective framework for consistent
high-quality materials discovery, offering training-free generation of novel
stable structures with reduced overhead and broader accessibility....

---

### 2. Generative Inverse Design: From Single Point Optimization to a Diverse Design Portfolio via Conditional Variational Autoencoders

**Authors:** Muhammad Arif Hakimi Zamrai

**Published:** 2025-10-03

**Category:** cs.LG

**ID:** 2510.05160v1

**Link:** [http://arxiv.org/abs/2510.05160v1](http://arxiv.org/abs/2510.05160v1)

**Summary:** Inverse design, which seeks to find optimal parameters for a target output,
is a central challenge in engineering. Surrogate-based optimization (SBO) has
become a standard approach, yet it is fundamentally structured to converge to a
single-point solution, thereby limiting design space exploration and ignoring
potentially valuable alternative topologies. This paper presents a paradigm
shift from single-point optimization to generative inverse design. We introduce
a framework based on a Conditional Variational Autoencoder (CVAE) that learns a
probabilistic mapping between a system's design parameters and its performance,
enabling the generation of a diverse portfolio of high-performing candidates
conditioned on a specific performance objective. We apply this methodology to
the complex, non-linear problem of minimizing airfoil self-noise, using a
high-performing SBO method from a prior benchmark study as a rigorous baseline.
The CVAE framework successfully generated 256 novel designs with a 94.1\%
validity rate. A subsequent surrogate-based evaluation revealed that 77.2\% of
these valid designs achieved superior performance compared to the single
optimal design found by the SBO baseline. This work demonstrates that the
generative approach not only discovers higher-quality solutions but also
provides a rich portfolio of diverse candidates, fundamentally enhancing the
engineering design process by enabling multi-criteria decision-making....

---

### 3. Reliable End-to-End Material Information Extraction from the Literature with Source-Tracked Multi-Stage Large Language Models

**Authors:** Xin Wang, Anshu Raj, Matthew Luebbe, Haiming Wen, Shuozhi Xu, Kun Lu

**Published:** 2025-10-01

**Category:** cs.CL

**ID:** 2510.05142v1

**Link:** [http://arxiv.org/abs/2510.05142v1](http://arxiv.org/abs/2510.05142v1)

**Summary:** Data-driven materials discovery requires large-scale experimental datasets,
yet most of the information remains trapped in unstructured literature.
Existing extraction efforts often focus on a limited set of features and have
not addressed the integrated composition-processing-microstructure-property
relationships essential for understanding materials behavior, thereby posing
challenges for building comprehensive databases. To address this gap, we
propose a multi-stage information extraction pipeline powered by large language
models, which captures 47 features spanning composition, processing,
microstructure, and properties exclusively from experimentally reported
materials. The pipeline integrates iterative extraction with source tracking to
enhance both accuracy and reliability. Evaluations at the feature level
(independent attributes) and tuple level (interdependent features) yielded F1
scores around 0.96. Compared with single-pass extraction without source
tracking, our approach improved F1 scores of microstructure category by 10.0%
(feature level) and 13.7% (tuple level), and reduced missed materials from 49
to 13 out of 396 materials in 100 articles on precipitate-containing
multi-principal element alloys (miss rate reduced from 12.4% to 3.3%). The
pipeline enables scalable and efficient literature mining, producing databases
with high precision, minimal omissions, and zero false positives. These
datasets provide trustworthy inputs for machine learning and materials
informatics, while the modular design generalizes to diverse material classes,
enabling comprehensive materials information extraction....

---


<!-- ARXIV_PAPERS_END -->