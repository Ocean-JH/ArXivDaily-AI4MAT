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

*Last updated: 2026-04-12 06:30:33 (SGT)*

### 1. Information-Theoretic Requirements for Gradient-Based Task Affinity Estimation in Multi-Task Learning

**Authors:** Jasper Zhang, Bryan Cheng

**Published:** 2026-04-09

**Category:** cs.LG

**ID:** 2604.07848v1

**Link:** [http://arxiv.org/abs/2604.07848v1](http://arxiv.org/abs/2604.07848v1)

**Summary:** Multi-task learning shows strikingly inconsistent results -- sometimes joint training helps substantially, sometimes it actively harms performance -- yet the field lacks a principled framework for predicting these outcomes. We identify a fundamental but unstated assumption underlying gradient-based task analysis: tasks must share training instances for gradient conflicts to reveal genuine relationships. When tasks are measured on the same inputs, gradient alignment reflects shared mechanistic structure; when measured on disjoint inputs, any apparent signal conflates task relationships with distributional shift. We discover this sample overlap requirement exhibits a sharp phase transition: below 30% overlap, gradient-task correlations are statistically indistinguishable from noise; above 40%, they reliably recover known biological structure. Comprehensive validation across multiple datasets achieves strong correlations and recovers biological pathway organization. Standard benchmarks systematically violate this requirement -- MoleculeNet operates at <5% overlap, TDC at 8-14% -- far below the threshold where gradient analysis becomes meaningful. This provides the first principled explanation for seven years of inconsistent MTL results....

---

### 2. Rhizome OS-1: Rhizome's Semi-Autonomous Operating System for Small Molecule Drug Discovery

**Authors:** Yiwen Wang, Gregory Sinenka, Xhuliano Brace

**Published:** 2026-04-08

**Category:** cs.AI

**ID:** 2604.07512v1

**Link:** [http://arxiv.org/abs/2604.07512v1](http://arxiv.org/abs/2604.07512v1)

**Summary:** We introduce a semi-autonomous discovery system in which multi-modal AI agents function as a multi-disciplinary discovery team, acting as computational chemists, medicinal chemists, and patent agents, writing and executing analysis code, visually evaluating molecular candidates, assessing patentability, and adapting generation strategy from empirical screening feedback, while r1, a 246M-parameter Graph Neural Network (GNN) trained on 800M molecules, generates novel chemical matter directly on molecular graphs. Agents executed two campaigns in oncology (BCL6, EZH2), formulating medicinal chemistry hypotheses across three strategy tiers and generating libraries of 2,355-2,876 novel molecules per target. Across both targets, 91.9% of generated Murcko scaffolds are absent from ChEMBL for their respective targets, with Tanimoto distances of 0.56-0.69 to the nearest known active, confirming that the engine produces structurally distinct chemical matter rather than recapitulating known compounds. Binding affinity predictions using Boltz-2 were calibrated against ChEMBL experimental data, achieving Spearman correlations of -0.53 to -0.64 and ROC AUC values of 0.88 to 0.93. These results demonstrate that semi-autonomous agent systems, equipped with graph-native generative tools and physics-informed scoring, provide a foundation for a modern operating system for small molecule discovery. We show that Rhizome OS-1 enables a new paradigm for early-stage drug discovery by supporting scaled, rapid, and adaptive inverse design....

---


<!-- ARXIV_PAPERS_END -->