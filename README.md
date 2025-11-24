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

*Last updated: 2025-11-25 06:17:07 (SGT)*

### 1. Model Inversion Attack Against Deep Hashing

**Authors:** Dongdong Zhao, Qiben Xu, Ranxin Fang, Baogang Song

**Published:** 2025-11-15

**Category:** cs.CV

**ID:** 2511.12233v2

**Link:** [http://arxiv.org/abs/2511.12233v2](http://arxiv.org/abs/2511.12233v2)

**Summary:** Deep hashing improves retrieval efficiency through compact binary codes, yet it introduces severe and often overlooked privacy risks. The ability to reconstruct original training data from hash codes could lead to serious threats such as biometric forgery and privacy breaches. However, model inversion attacks specifically targeting deep hashing models remain unexplored, leaving their security implications unexamined. This research gap stems from the inaccessibility of genuine training hash codes and the highly discrete Hamming space, which prevents existing methods from adapting to deep hashing. To address these challenges, we propose DHMI, the first diffusion-based model inversion framework designed for deep hashing. DHMI first clusters an auxiliary dataset to derive semantic hash centers as surrogate anchors. It then introduces a surrogate-guided denoising optimization method that leverages a novel attack metric (fusing classification consistency and hash proximity) to dynamically select candidate samples. A cluster of surrogate models guides the refinement of these candidates, ensuring the generation of high-fidelity and semantically consistent images. Experiments on multiple datasets demonstrate that DHMI successfully reconstructs high-resolution, high-quality images even under the most challenging black-box setting, where no training hash codes are available. Our method outperforms the existing state-of-the-art model inversion attacks in black-box scenarios, confirming both its practical efficacy and the critical privacy risks inherent in deep hashing systems....

---

### 2. RTMol: Rethinking Molecule-text Alignment in a Round-trip View

**Authors:** Letian Chen, Runhan Shi, Gufeng Yu, Yang Yang

**Published:** 2025-11-15

**Category:** cs.AI

**ID:** 2511.12135v2

**Link:** [http://arxiv.org/abs/2511.12135v2](http://arxiv.org/abs/2511.12135v2)

**Summary:** Aligning molecular sequence representations (e.g., SMILES notations) with textual descriptions is critical for applications spanning drug discovery, materials design, and automated chemical literature analysis. Existing methodologies typically treat molecular captioning (molecule-to-text) and text-based molecular design (text-to-molecule) as separate tasks, relying on supervised fine-tuning or contrastive learning pipelines. These approaches face three key limitations: (i) conventional metrics like BLEU prioritize linguistic fluency over chemical accuracy, (ii) training datasets frequently contain chemically ambiguous narratives with incomplete specifications, and (iii) independent optimization of generation directions leads to bidirectional inconsistency. To address these issues, we propose RTMol, a bidirectional alignment framework that unifies molecular captioning and text-to-SMILES generation through self-supervised round-trip learning. The framework introduces novel round-trip evaluation metrics and enables unsupervised training for molecular captioning without requiring paired molecule-text corpora. Experiments demonstrate that RTMol enhances bidirectional alignment performance by up to 47% across various LLMs, establishing an effective paradigm for joint molecule-text understanding and generation....

---

### 3. Quasiparticle states of hexagonal BN: A van der Waals density functional study

**Authors:** Raul Quintero-Monsebaiz, Per Hyldgaard

**Published:** 2025-11-20

**Category:** cond-mat.mtrl-sci

**ID:** 2511.16313v2

**Link:** [http://arxiv.org/abs/2511.16313v2](http://arxiv.org/abs/2511.16313v2)

**Summary:** We compute and track the impact of truly nonlocal-correlation effects on the quasi-particle (QP) band-structure of hexagonal boron-nitride (h-BN) systems. To that end, we start with the consistent-exchange vdW-DF-cx version [PRB 89, 035412 (2014)] of the van der Waals density functional (vdW-DF) method [JPCM 39, 390001 (2020)] for exchange-correlation (XC) functional design and enforce piece-wise linearity in the energy changes with partial charging, using the Koopmans-integer (KI) DFT framework [JCTC 19, 7079 (2023)]. Our approach and results (denoted KI-CX) extends present-standard use of KI DFT (denoted KI-PBE as it is based on the semilocal PBE [PRL 77, 3865 (1996)] XC functional) to capture, for example, the impact of the interlayer coupling on the QPs. We contrast KI-CX and KI-PBE results for the QP band-structure and compare with both $GW$ calculations and experimental observations of the (direct and indirect) QP gaps. We find that KI-CX brings improvements in the h-BN QP energy description and generally agrees with $GW$ studies....

---

### 4. MRI Super-Resolution with Deep Learning: A Comprehensive Survey

**Authors:** Mohammad Khateri, Serge Vasylechko, Morteza Ghahremani, Liam Timms, Deniz Kocanaogullari, Simon K. Warfield, Camilo Jaimes, Davood Karimi, Alejandra Sierra, Jussi Tohka, Sila Kurugol, Onur Afacan

**Published:** 2025-11-20

**Category:** eess.IV

**ID:** 2511.16854v1

**Link:** [http://arxiv.org/abs/2511.16854v1](http://arxiv.org/abs/2511.16854v1)

**Summary:** High-resolution (HR) magnetic resonance imaging (MRI) is crucial for many clinical and research applications. However, achieving it remains costly and constrained by technical trade-offs and experimental limitations. Super-resolution (SR) presents a promising computational approach to overcome these challenges by generating HR images from more affordable low-resolution (LR) scans, potentially improving diagnostic accuracy and efficiency without requiring additional hardware. This survey reviews recent advances in MRI SR techniques, with a focus on deep learning (DL) approaches. It examines DL-based MRI SR methods from the perspectives of computer vision, computational imaging, inverse problems, and MR physics, covering theoretical foundations, architectural designs, learning strategies, benchmark datasets, and performance metrics. We propose a systematic taxonomy to categorize these methods and present an in-depth study of both established and emerging SR techniques applicable to MRI, considering unique challenges in clinical and research contexts. We also highlight open challenges and directions that the community needs to address. Additionally, we provide a collection of essential open-access resources, tools, and tutorials, available on our GitHub: https://github.com/mkhateri/Awesome-MRI-Super-Resolution.
  IEEE keywords: MRI, Super-Resolution, Deep Learning, Computational Imaging, Inverse Problem, Survey....

---


<!-- ARXIV_PAPERS_END -->