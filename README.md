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

*Last updated: 2025-09-30 06:14:30 (SGT)*

### 1. Challenges in Non-Polymeric Crystal Structure Prediction: Why a Geometric, Permutation-Invariant Loss is Needed

**Authors:** Emmanuel Jehanno, Romain Menegaux, Julien Mairal, Sergei Grudinin

**Published:** 2025-08-31

**Category:** cs.LG

**ID:** 2509.00832v3

**Link:** [http://arxiv.org/abs/2509.00832v3](http://arxiv.org/abs/2509.00832v3)

**Summary:** Crystalline structure prediction is an essential prerequisite for designing
materials with targeted properties. Yet, it is still an open challenge in
materials design and drug discovery. Despite recent advances in computational
materials science, accurately predicting three-dimensional non-polymeric
crystal structures remains elusive. In this work, we focus on the molecular
assembly problem, where a set $\mathcal{S}$ of identical rigid molecules is
packed to form a crystalline structure. Such a simplified formulation provides
a useful approximation to the actual problem. However, while recent
state-of-the-art methods have increasingly adopted sophisticated techniques,
the underlying learning objective remains ill-posed. We propose a better
formulation that introduces a loss function capturing key geometric molecular
properties while ensuring permutation invariance over $\mathcal{S}$.
Remarkably, we demonstrate that within this framework, a simple regression
model already outperforms prior approaches, including flow matching techniques,
on the COD-Cluster17 benchmark, a curated non-polymeric subset of the
Crystallography Open Database (COD)....

---

### 2. Interpretable Spectral Features Predict Conductivity in Self-Driving Doped Conjugated Polymer Labs

**Authors:** Ankush Kumar Mishra, Jacob P. Mauthe, Nicholas Luke, Aram Amassian, Baskar Ganapathysubramanian

**Published:** 2025-09-06

**Category:** cond-mat.mtrl-sci

**ID:** 2509.21330v1

**Link:** [http://arxiv.org/abs/2509.21330v1](http://arxiv.org/abs/2509.21330v1)

**Summary:** Self-driving labs (SDLs) promise faster materials discovery by coupling
automation with machine learning, but a central challenge is predicting costly,
slow-to-measure properties from inexpensive, automatable readouts. We address
this for doped conjugated polymers by learning interpretable spectral
fingerprints from optical spectroscopy to predict electrical conductivity.
Optical spectra are fast, non-destructive, and sensitive to aggregation and
charge generation; we automate their featurization by combining a genetic
algorithm (GA) with area-under-the-curve (AUC) computations over adaptively
selected spectral windows. These data-driven spectral features, together with
processing parameters, are used to train a quantitative structure-property
relationship (QSPR) linking optical response and processing to conductivity. To
improve accuracy and interpretability in the small-data regime, we add
domain-knowledge-based feature expansions and apply SHAP-guided selection to
retain a compact, physically meaningful feature set. The pipeline is evaluated
under a leak-free train/test protocol, and GA is repeated to assess feature
stability. The data-driven model matches the performance of a baseline built
from expert-curated descriptors while reducing experimental effort (about 33%)
by limiting direct conductivity measurements. Combining data-driven and expert
features yields a hybrid QSPR with superior predictive performance,
highlighting productive human-ML collaboration. The learned features recover
known descriptors in pBTTT (0-0/0-1 vibronic intensity ratio) and reveal a
tail-state region correlated with polymer bleaching during successful doping.
This approach delivers interpretable, noise-robust, small-data-friendly
features that convert rapid measurements into reliable predictions of costly
properties and readily extends to other spectral modalities (e.g., XANES,
Raman, FTIR)....

---


<!-- ARXIV_PAPERS_END -->