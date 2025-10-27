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

*Last updated: 2025-10-28 06:16:11 (SGT)*

### 1. Space Group Equivariant Crystal Diffusion

**Authors:** Rees Chang, Angela Pak, Alex Guerra, Ni Zhan, Nick Richardson, Elif Ertekin, Ryan P. Adams

**Published:** 2025-05-16

**Category:** cond-mat.mtrl-sci

**ID:** 2505.10994v3

**Link:** [http://arxiv.org/abs/2505.10994v3](http://arxiv.org/abs/2505.10994v3)

**Summary:** Accelerating inverse design of crystalline materials with generative models
has significant implications for a range of technologies. Unlike other atomic
systems, 3D crystals are invariant to discrete groups of isometries called the
space groups. Crucially, these space group symmetries are known to heavily
influence materials properties. We propose SGEquiDiff, a crystal generative
model which naturally handles space group constraints with space group
invariant likelihoods. SGEquiD-iff consists of an SE(3)-invariant, telescoping
discrete sampler of crystal lattices; permutation-invariant, transformer-based
autoregressive sampling of Wyckoff positions, elements, and numbers of
symmetrically unique atoms; and space group equivariant diffusion of atomic
coordinates. We show that space group equivariant vector fields automatically
live in the tangent spaces of the Wyckoff positions. SGEquiDiff achieves
state-of-the-art performance on standard benchmark datasets as assessed by
quantitative proxy metrics and quantum mechanical calculations. Our code is
available at https://github.com/rees-c/sgequidiff....

---

### 2. L^2M^3OF: A Large Language Multimodal Model for Metal-Organic Frameworks

**Authors:** Jiyu Cui, Fang Wu, Haokai Zhao, Minggao Feng, Xenophon Evangelopoulos, Andrew I. Cooper, Yejin Choi

**Published:** 2025-10-23

**Category:** cs.LG

**ID:** 2510.20976v1

**Link:** [http://arxiv.org/abs/2510.20976v1](http://arxiv.org/abs/2510.20976v1)

**Summary:** Large language models have demonstrated remarkable reasoning capabilities
across diverse natural language tasks. However, comparable breakthroughs in
scientific discovery are more limited, because understanding complex physical
phenomena demands multifaceted representations far beyond language alone. A
compelling example is the design of functional materials such as MOFs-critical
for a range of impactful applications like carbon capture and hydrogen storage.
Navigating their vast and intricate design space in language-based
representations interpretable by LLMs is challenging due to the numerous
possible three-dimensional atomic arrangements and strict reticular rules of
coordination geometry and topology. Despite promising early results in
LLM-assisted discovery for simpler materials systems, MOF design remains
heavily reliant on tacit human expertise rarely codified in textual information
alone. To overcome this barrier, we introduce L2M3OF, the first multimodal LLM
for MOFs. L2M3OF integrates crystal representation learning with language
understanding to process structural, textual, and knowledge modalities jointly.
L2M3OF employs a pre-trained crystal encoder with a lightweight projection
layer to compress structural information into a token space, enabling efficient
alignment with language instructions. To facilitate training and evaluation, we
curate a structure-property-knowledge database of crystalline materials and
benchmark L2M3OF against state-of-the-art closed-source LLMs such as GPT-5,
Gemini-2.5-Pro and DeepSeek-R1. Experiments show that L2M3OF outperforms
leading text-based closed-source LLMs in property prediction and knowledge
generation tasks, despite using far fewer parameters. These results highlight
the importance of multimodal approaches for porous material understanding and
establish L2M3OF as a foundation for next-generation AI systems in materials
discovery....

---


<!-- ARXIV_PAPERS_END -->