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

*Last updated: 2025-07-29 06:19:12 (SGT)*

### 1. Stability and Symmetry-Assured Crystal Structure Generation for Inverse Design of Photocatalysts in Water Splitting

**Authors:** Zhilong Song, Chongyi Ling, Qiang Li, Qionghua Zhou, Jinlan Wang

**Published:** 2025-07-25

**Category:** cond-mat.mtrl-sci

**ID:** 2507.19307v1

**Link:** [http://arxiv.org/abs/2507.19307v1](http://arxiv.org/abs/2507.19307v1)

**Summary:** Generative models are revolutionizing materials discovery by enabling inverse
design-direct generation of structures from desired properties. However,
existing approaches often struggle to ensure inherent stability and symmetry
while precisely generating structures with target compositions, space groups,
and lattices without fine-tuning. Here, we present SSAGEN (Stability and
Symmetry-Assured GENerative framework), which overcomes these limitations by
decoupling structure generation into two distinct stages: crystal information
(lattice, composition, and space group) generation and coordinate optimization.
SSAGEN first generates diverse yet physically plausible crystal information,
then derives stable and metastable atomic positions through universal machine
learning potentials, combined global and local optimization with symmetry and
Wyckoff position constraints, and dynamically refined search spaces. Compared
to prior generative models such as CDVAE, SSAGEN improves the thermodynamic and
kinetic stability of generated structures by 148% and 180%, respectively, while
inherently satisfying target compositions, space groups, and lattices. Applied
to photocatalytic water splitting (PWS), SSAGEN generates 200,000
structures-81.2% novel-with 3,318 meeting all stability and band gap criteria.
Density functional theory (DFT) validation confirms 95.6% structures satisfy
PWS requirements, with 24 optimal candidates identified through comprehensive
screening based on electronic structure, thermodynamic, kinetic, and aqueous
stability criteria. SSAGEN not only precisely generates materials with desired
crystal information but also ensures inherent stability and symmetry,
establishing a new paradigm for targeted inverse design of functional
materials....

---

### 2. T2MAT (text-to-materials): A universal agent for generating material structures with goal properties from a single sentence

**Authors:** Zhilong Song, Shuaihua Lu, Qionghua Zhou, Jinlan Wang

**Published:** 2024-07-09

**Category:** cond-mat.mtrl-sci

**ID:** 2407.06489v2

**Link:** [http://arxiv.org/abs/2407.06489v2](http://arxiv.org/abs/2407.06489v2)

**Summary:** Artificial Intelligence-Generated Content (AIGC)-content autonomously
produced by AI systems without human intervention-has significantly boosted
efficiency across various fields. However, AIGC in material science faces
challenges in efficiently discovering novel materials that surpass existing
databases, while simultaneously addressing the invariance and stability of
crystal structures. To address these challenges, we develop T2MAT
(text-to-material), a comprehensive agent processing from a user-input sentence
to inverse design material structures with goal properties beyond the existing
database via globally exploring chemical space, followed by an entirely
automated workflow of first-principles validation. Furthermore, we propose
CGTNet (Crystal Graph Transformer NETwork), a graph neural network model that
captures long-range interactions, to enhance the accuracy and data utilization
efficiency of property prediction and thereby strengthen the reliability of
inverse design. Through these contributions, T2MAT minimizes the dependency on
human expertise and significantly improves the efficiency of discovering novel,
high-performance functional materials, offering a robust way toward more
autonomous materials design....

---

### 3. A High-Quality Thermoelectric Material Database with Self-Consistent ZT Filtering

**Authors:** Byungki Ryu, Ji Hui Son, Sungjin Park, Jaywan Chung, Hye-Jin Lim, SuJi Park, Yujeong Do, SuDong Park

**Published:** 2025-05-25

**Category:** cond-mat.mtrl-sci

**ID:** 2505.19150v3

**Link:** [http://arxiv.org/abs/2505.19150v3](http://arxiv.org/abs/2505.19150v3)

**Summary:** This study presents a curated thermoelectric material database, teMatDb,
constructed by digitizing literature-reported data. It includes
temperature-dependent thermoelectric properties (TEPs), Seebeck coefficient,
electrical resistivity, thermal conductivity, and figure of merit (ZT), along
with metadata on materials and their corresponding publications. A
self-consistent ZT (Sc-ZT) filter set was developed to measure ZT errors by
comparing reported ZT's from figures with ZT's recalculated from digitized
TEPs. Using this Sc-ZT protocol, we generated tMatDb272, comprising 14,717
temperature-property pairs from 272 high-quality TEP sets across 262
publications. The method identifies various types of ZT errors, such as
resolution error, publication bias, ZT overestimation, interpolation and
extrapolation error, and digitization noise, and excludes inconsistent samples
from the dataset. teMatDb272 and the Sc-ZT filtering framework offer a robust
dataset for data-driven and machine-learning-based materials design, device
modeling, and future thermoelectric research....

---


<!-- ARXIV_PAPERS_END -->