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

*Last updated: 2025-10-23 06:14:10 (SGT)*

### 1. Uncovering critical temperature dependence in Heusler magnets via explicit machine learning

**Authors:** Jean-Baptiste Morée, Juba Bouaziz, Ryotaro Arita

**Published:** 2025-10-21

**Category:** cond-mat.mtrl-sci

**ID:** 2510.18469v1

**Link:** [http://arxiv.org/abs/2510.18469v1](http://arxiv.org/abs/2510.18469v1)

**Summary:** We employ interpretable explicit machine learning to analyze the material
dependence of the magnetic transition temperature $T_c$ in ferromagnetic and
ferrimagnetic Heusler compounds. For around 200 compounds, we consider both
experimental $T_c$ and calculated $T_c$ using \textit{ab initio} determination
of magnetic interactions together with a Monte-Carlo solution. We use the
hierarchical dependence extraction (HDE) procedure [Mor\'ee and Arita, Phys.
Rev. B 110, 014502 (2024)] to extract the dependencies of $T_c$ on chemical
proportions and magnetic moments from the main order to the higher order, and
construct an explicit expression of $T_c$ from these dependencies. The main
results are: (a) $T_c$ is mainly controlled by the proportions of Fe, Co, and
Mn, and increases with these proportions, consistent with previous machine
learning analyses of ferromagnetic materials. (b) The HDE describes $T_c$ with
an accuracy that is comparable to that of other machine learning procedures.
(c) The HDE expression of $T_c$ can be interpreted as a generalized order
parameter that increases with increasing magnetization amplitude, in
qualitative agreement with various theories of phase transitions. These results
strengthen our understanding of the material dependence of $T_c$ in collinear
Heusler magnets and motivate the further use of HDE in material design....

---

### 2. Enabling Automatic Differentiation with Mollified Graph Neural Operators

**Authors:** Ryan Y. Lin, Julius Berner, Valentin Duruisseaux, David Pitt, Daniel Leibovici, Jean Kossaifi, Kamyar Azizzadenesheli, Anima Anandkumar

**Published:** 2025-04-11

**Category:** cs.LG

**ID:** 2504.08277v2

**Link:** [http://arxiv.org/abs/2504.08277v2](http://arxiv.org/abs/2504.08277v2)

**Summary:** Physics-informed neural operators offer a powerful framework for learning
solution operators of partial differential equations (PDEs) by combining data
and physics losses. However, these physics losses rely on derivatives.
Computing these derivatives remains challenging, with spectral and finite
difference methods introducing approximation errors due to finite resolution.
Here, we propose the mollified graph neural operator ($m$GNO), the first method
to leverage automatic differentiation and compute exact gradients on arbitrary
geometries. This enhancement enables efficient training on irregular grids and
varying geometries while allowing seamless evaluation of physics losses at
randomly sampled points for improved generalization. For a PDE example on
regular grids, $m$GNO paired with autograd reduced the L2 relative data error
by 20x compared to finite differences, although training was slower. It can
also solve PDEs on unstructured point clouds seamlessly, using physics losses
only, at resolutions vastly lower than those needed for finite differences to
be accurate enough. On these unstructured point clouds, $m$GNO leads to errors
that are consistently 2 orders of magnitude lower than machine learning
baselines (Meta-PDE, which accelerates PINNs) for comparable runtimes, and also
delivers speedups from 1 to 3 orders of magnitude compared to the numerical
solver for similar accuracy. $m$GNOs can also be used to solve inverse design
and shape optimization problems on complex geometries....

---


<!-- ARXIV_PAPERS_END -->