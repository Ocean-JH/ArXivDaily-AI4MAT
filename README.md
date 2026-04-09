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

*Last updated: 2026-04-10 06:38:42 (SGT)*

### 1. When Does Context Help? A Systematic Study of Target-Conditional Molecular Property Prediction

**Authors:** Bryan Cheng, Jasper Zhang

**Published:** 2026-04-08

**Category:** cs.LG

**ID:** 2604.06558v1

**Link:** [http://arxiv.org/abs/2604.06558v1](http://arxiv.org/abs/2604.06558v1)

**Summary:** We present the first systematic study of when target context helps molecular property prediction, evaluating context conditioning across 10 diverse protein families, 4 fusion architectures, data regimes spanning 67-9,409 training compounds, and both temporal and random evaluation splits. Using NestDrug, a FiLM-based architecture that conditions molecular representations on target identity, we characterize both success and failure modes with three principal findings. First, fusion architecture dominates: FiLM outperforms concatenation by 24.2 percentage points and additive conditioning by 8.6 pp; how you incorporate context matters more than whether you include it. Second, context enables otherwise impossible predictions: on data-scarce CYP3A4 (67 training compounds), multi-task transfer achieves 0.686 AUC where per-target Random Forest collapses to 0.238. Third, context can systematically hurt: distribution mismatch causes 10.2 pp degradation on BACE1; few-shot adaptation consistently underperforms zero-shot. Beyond methodology, we expose fundamental flaws in standard benchmarking: 1-nearest-neighbor Tanimoto achieves 0.991 AUC on DUD-E without any learning, and 50% of actives leak from training data, rendering absolute performance metrics meaningless. Our temporal split evaluation (train up to 2020, test 2021-2024) achieves stable 0.843 AUC with no degradation, providing the first rigorous evidence that context-conditional molecular representations generalize to future chemical space....

---


<!-- ARXIV_PAPERS_END -->