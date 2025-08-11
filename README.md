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

## New Papers (1)

*Last updated: 2025-08-12 06:17:26 (SGT)*

### 1. Leveraging transfer learning for accurate estimation of ionic migration barriers in solids

**Authors:** Reshma Devi, Keith T. Butler, Gopalakrishnan Sai Gautam

**Published:** 2025-08-08

**Category:** cond-mat.mtrl-sci

**ID:** 2508.06436v1

**Link:** [http://arxiv.org/abs/2508.06436v1](http://arxiv.org/abs/2508.06436v1)

**Summary:** Ionic mobility determines the rate performance of several applications, such
as batteries, fuel cells, and electrochemical sensors and is exponentially
dependent on the migration barrier ($E_m$), a difficult to measure/calculate
quantity. Previous approaches to identify materials with high ionic mobility
have relied on imprecise descriptors given the lack of generalizable models to
predict $E_m$. Here, we present a graph neural network based architecture that
leverages principles of transfer learning to efficiently and accurately predict
$E_m$ across a diverse set of materials. We use a model pre-trained
simultaneously on seven distinct bulk properties (labeled MPT), modify the MPT
model to classify different migration pathways in a structure, and fine-tune
(FT) on a manually-curated literature-derived dataset of 619 $E_m$ data points
calculated with density functional theory. Importantly, our best-performing FT
model (labeled MODEL-3) demonstrates substantial improvements in prediction
accuracy compared to classical machine learning methods, graph models trained
from scratch, and a universal machine learned interatomic potential, with a
R$^2$ score of 0.703 and a mean absolute error of 0.261 eV on the test set.
Notably, MODEL-3 is able to distinguish different migration pathways within a
structure and also demonstrates excellent ability to generalize across
intercalant compositions and chemistries. As a classifier, MODEL-3 exhibits
80\% accuracy and 82.8\% precision in identifying materials that are `good'
ionic conductors (i.e., structures with $E_m <$0.65~eV). Thus, our work
demonstrates the effective use of FT strategies and architectural modifications
necessary for making swift and accurate $E_m$ predictions, which will be useful
for materials discovery in batteries and for predicting other data-scarce
material properties....

---


<!-- ARXIV_PAPERS_END -->