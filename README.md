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

## New Papers (200)

*Last updated: 2025-07-16 12:36:30 (SGT)*

### 1. On Equivariant Model Selection through the Lens of Uncertainty

**Authors:** Putri A. van der Linden, Alexander Timans, Dharmesh Tailor, Erik J. Bekkers

**Published:** 2025-06-23

**Category:** cs.LG

**ID:** 2506.18629v2

**Link:** [http://arxiv.org/abs/2506.18629v2](http://arxiv.org/abs/2506.18629v2)

**Summary:** Equivariant models leverage prior knowledge on symmetries to improve
predictive performance, but misspecified architectural constraints can harm it
instead. While work has explored learning or relaxing constraints, selecting
among pretrained models with varying symmetry biases remains challenging. We
examine this model selection task from an uncertainty-aware perspective,
comparing frequentist (via Conformal Prediction), Bayesian (via the marginal
likelihood), and calibration-based measures to naive error-based evaluation. We
find that uncertainty metrics generally align with predictive performance, but
Bayesian model evidence does so inconsistently. We attribute this to a mismatch
in Bayesian and geometric notions of model complexity for the employed
last-layer Laplace approximation, and discuss possible remedies. Our findings
point towards the potential of uncertainty in guiding symmetry-aware model
selection....

---

### 2. Spin ordering-induced fully-compensated ferrimagnetism

**Authors:** San-Dong Guo, Shaobo Chen, Guangzhao Wang

**Published:** 2025-07-14

**Category:** cond-mat.mtrl-sci

**ID:** 2507.10848v1

**Link:** [http://arxiv.org/abs/2507.10848v1](http://arxiv.org/abs/2507.10848v1)

**Summary:** Fully-compensated ferrimagnets exhibit zero net magnetic moment yet display
non-relativistic global spin splitting, making them highly advantageous for
constructing high-performance spintronic devices. The general strategy is to
break the inversion symmetry of conventional antiferromagnets or the
rotational/mirror symmetry of altermagnets to achieve fully-compensated
ferrimagnets. Here, we propose to induce fully-compensated ferrimagnetism by
engineering the spin ordering rather than modifying the lattice structure.
Bilayer stacking engineering offers a convenient platform to verify our
proposal and readily enables switching between two distinct electronic states
by tuning the $\mathrm{N\acute{e}el}$ vector of one layer. By the
first-principles calculations, a bilayer system is constructed with monolayer
$\mathrm{Cr_2C_2S_6}$ as the elementary building block to corroborate our
proposal. This strategy can also be extended to inducing altermagnetism via
spin ordering engineering. Our work offers an alternative route to realize
non-relativistic spin splitting in zero-net-magnetization magnets, paving the
way for the advancement and construction of low-power spintronic device....

---

### 3. Spin dynamics of triple-Q magnetic orderings in a triangular lattice: Implications for multi-Q orderings in general two-dimensional lattices

**Authors:** Pyeongjae Park, Woonghee Cho, Chaebin Kim, Yeochan An, Kazuki Iida, Ryoichi Kajimoto, Sakib Matin, Shang-Shun Zhang, Cristian D. Batista, Je-Geun Park

**Published:** 2024-10-03

**Category:** cond-mat.str-el

**ID:** 2410.02180v3

**Link:** [http://arxiv.org/abs/2410.02180v3](http://arxiv.org/abs/2410.02180v3)

**Summary:** Multi-Q magnetic structures on two-dimensional (2D) lattices provide a key
route to realizing topological physics in 2D magnetism. A major experimental
challenge is to unambiguously confirm their formation by excluding the
possibility of topologically trivial multi-domain single- or double-Q magnetic
orders, which cannot be distinguished using conventional diffraction
techniques. Here, we propose that long-wavelength spin dynamics offers a
universal diagnostic for triangular lattices: triple-Q orders that preserve
rotational symmetry and single- or double-Q orders that break it exhibit
qualitatively distinct anisotropies in their Goldstone mode velocities,
stemming from fundamental differences in their underlying spin configurations.
We validate this concept using the metallic triangular lattice antiferromagnet
Co$_{0.325}$TaS$_{2}$, which hosts both a stripe-type single-Q state and a
triple-Q tetrahedral ordering at different temperatures. Using inelastic
neutron scattering (INS) and spin dynamics simulations, we first refine the
spin Hamiltonian by fitting the paramagnetic excitation spectra, allowing us to
develop an unbiased model independent of magnetic ordering. We then show that
the observed velocity profiles of the Goldstone modes agree with the
high-temperature model's predictions: markedly anisotropic for the single-Q
phase and near isotropic for the triple-Q phase. Importantly, this contrast
persists across various exchange parameters, highlighting its model-independent
nature and suggesting potential applicability to other 2D lattice systems. This
work provides universal insight into the dynamical properties of topological
multi-Q magnetic orderings in 2D lattice structures, offering a broadly
applicable diagnostic to distinguishing them from topologically trivial single-
or double-Q counterparts. (For the full abstract, please refer to the
manuscript)...

---

### 4. A Group Theoretic Analysis of the Symmetries Underlying Base Addition and Their Learnability by Neural Networks

**Authors:** Cutter Dawes, Simon Segert, Kamesh Krishnamurthy, Jonathan D. Cohen

**Published:** 2025-07-14

**Category:** cs.LG

**ID:** 2507.10678v1

**Link:** [http://arxiv.org/abs/2507.10678v1](http://arxiv.org/abs/2507.10678v1)

**Summary:** A major challenge in the use of neural networks both for modeling human
cognitive function and for artificial intelligence is the design of systems
with the capacity to efficiently learn functions that support radical
generalization. At the roots of this is the capacity to discover and implement
symmetry functions. In this paper, we investigate a paradigmatic example of
radical generalization through the use of symmetry: base addition. We present a
group theoretic analysis of base addition, a fundamental and defining
characteristic of which is the carry function -- the transfer of the remainder,
when a sum exceeds the base modulus, to the next significant place. Our
analysis exposes a range of alternative carry functions for a given base, and
we introduce quantitative measures to characterize these. We then exploit
differences in carry functions to probe the inductive biases of neural networks
in symmetry learning, by training neural networks to carry out base addition
using different carries, and comparing efficacy and rate of learning as a
function of their structure. We find that even simple neural networks can
achieve radical generalization with the right input format and carry function,
and that learning speed is closely correlated with carry function structure. We
then discuss the relevance this has for cognitive science and machine learning....

---

### 5. Quantum-Annealing Enhanced Machine Learning for Interpretable Phase Classification of High-Entropy Alloys

**Authors:** Diego Ibarra Hoyos, Gia-Wei Chern, Israel Klich, Joseph Poon

**Published:** 2025-07-14

**Category:** cond-mat.mtrl-sci

**ID:** 2507.10237v1

**Link:** [http://arxiv.org/abs/2507.10237v1](http://arxiv.org/abs/2507.10237v1)

**Summary:** High entropy alloys (HEAs) offer unprecedented compositional flexibility for
designing advanced materials, yet predicting their crystallographic phases
remains a key bottleneck due to limited data and complex phase formation
behavior. Here, we present a quantum-enhanced machine learning framework that
leverages quantum annealing to enhance phase classification in HEAs. Our
pipeline integrates Quantum Boosting (QBoost) for interpretable feature
selection and classification, with Quantum Support Vector Machines (QSVM) that
use quantum-enhanced kernels to capture nonlinear relationships between
physical descriptors. By reformulating both models as Quadratic Unconstrained
Binary Optimization (QUBO) problems, we exploit the efficient sampling
capabilities of quantum annealers to achieve rapid training and robust
generalization, demonstrating notable runtime reductions relative to classical
baselines in our setup. We target six key phases: FCC, BCC, Sigma, Laves,
Heusler, and AlXY B2, and benchmark model performance using both
cross-validation and a rigorously curated test set of prior experimentally
synthesized HEAs. The results confirm strong alignment between predicted and
measured phases. Our findings demonstrate that quantum-enhanced classifiers
match or exceed classical models in accuracy and offer insights grounded in
interpretable physical descriptors. This work constitutes an important step
toward practical quantum acceleration in materials discovery pipelines....

---

### 6. Sliding ferroelectric control of unconventional magnetism in stacked bilayers

**Authors:** Yongqian Zhu, Mingqiang Gu, Yuntian Liu, Xiaobing Chen, Yuhui Li, Shixuan Du, Qihang Liu

**Published:** 2025-02-24

**Category:** cond-mat.mtrl-sci

**ID:** 2502.17095v2

**Link:** [http://arxiv.org/abs/2502.17095v2](http://arxiv.org/abs/2502.17095v2)

**Summary:** The control of unconventional magnetism, which displays ferromagnetism-like
properties with compensated magnetization, has drawn intense attention for
advancing antiferromagnetic spintronics. Here, through symmetry analysis, we
propose a general stacking rule, characterized by a connection operator linking
two stacked bilayers, for controlling unconventional magnetism via sliding
ferroelectricity. Such rule enables the simultaneous switching of both electric
polarization and nonrelativistic spin splitting or anomalous Hall effect in
altermagnets, a class of collinear unconventional magnets. By comprehensively
surveying the 80 layer groups, we identify all the stacking orders that allow
for such two types of simultaneous switching. Furthermore, we extend the
stacking rule to collinear compensated ferrimagnets, where the opposite-spin
sublattices are not connected by any symmetry operator, yet the net
magnetization remains zero. Combined with first-principles calculations, we
demonstrate the sliding ferroelectric control of spin polarization and
anomalous Hall effect in the altermagnetic AgF2 and Fe2MoSe4 bilayers. Our work
provides a symmetry strategy for achieving ferroelectric control of
unconventional magnetism in bilayer systems and opens avenues for exploring new
types of magnetoelectric coupling....

---

### 7. Spin current generation driven by skyrmion dynamics under magnetic anisotropy and polarized microwaves

**Authors:** Seno Aji, Muhammad Anin Nabail Azhiim, Nur Ika Puji Ayu, Adam Badra Cahaya, Koichi Kusakabe, Muhammad Aziz Majidi

**Published:** 2025-07-12

**Category:** cond-mat.mtrl-sci

**ID:** 2507.09126v1

**Link:** [http://arxiv.org/abs/2507.09126v1](http://arxiv.org/abs/2507.09126v1)

**Summary:** We have investigated the spin-current pumped by the skyrmion-host material
with the lack of inversion symmetry through the microwave resonance process.
The effects of magnetic anisotropy and polarized microwaves are examined by
micromagnetic simulations. Our results reveal two distinct skyrmion phases,
designated as SkX type-I and II, which emerge at low ($K_z<0.1$ meV) and high
($K_z>0.1$ meV) magnetic anisotropy constants, respectively, having different
characteristics of spin excitations. The SkX type-I exhibits spin dynamics
where the resonant frequency of the breathing mode is lying in between the
clockwise and counterclockwise gyration modes of Bloch-type skyrmion at a very
low anisotropy, and is crossing over the counterclockwise mode at $K_z \sim
0.04$ meV. Meanwhile, the SkX type-II exhibits distinct spin excitations in
which the clockwise mode is notably absent, while the counterclockwise modes
exist at both low and high resonant frequencies. This suggests that the
magnetic anisotropy plays an essential role in the spin dynamics. Furthermore,
the resulting spin excitations induce spin currents with exotic features under
the polarized microwaves. The spin currents induced, for instance, by low-lying
in-plane excitations are strongly enhanced under the left-handed circularly
polarized microwaves, but quenched by the right-handed circularly polarized
microwaves regardless of the sign of the Dzyaloshinskii-Moriya interaction.
These results may pave the way for understanding the non-trivial interplay
between magnetic anisotropy and polarized microwaves in the generation of spin
currents by a resonant process....

---

### 8. A General, Automated Method for Building Structural Tensors of Arbitrary Order for Anisotropic Function Representations

**Authors:** Ravi G. Patel, Reese E. Jones, D. Thomas Seidl, Brian N. Granzow, Jan N. Fuhg

**Published:** 2025-07-12

**Category:** math-ph

**ID:** 2507.09088v1

**Link:** [http://arxiv.org/abs/2507.09088v1](http://arxiv.org/abs/2507.09088v1)

**Summary:** We present a general, constructive procedure to find the basis for tensors of
arbitrary order subject to linear constraints by transforming the problem to
that of finding the nullspace of a linear operator. The proposed method
utilizes standard numerical linear algebra techniques that are highly optimized
and well-behaved. Our primary applications are in mechanics where modulus
tensors and so-called structure tensors can be used to characterize anisotropy
of functional dependencies on other inputs such as strain. Like modulus
tensors, structure tensors are defined by their invariance to transformations
by symmetry group generators but have more general applicability. The fully
automated method is an alternative to classical, more intuition-reliant methods
such as the Pipkin-Rivlin polynomial integrity basis construction. We
demonstrate the utility of the procedure by: (a) enumerating elastic modulus
tensors for common symmetries, and (b) finding the lowest-order structure
tensors that can represent all common point groups/crystal classes.
Furthermore, we employ these results in two calibration problems using neural
network models following classical function representation theory: (a) learning
the symmetry class and orientation of a hyperelastic material given
stress-strain data, and (b) representing strain-dependent anisotropy of the
stress response of a soft matrix-stiff fiber composite in a sequence of
uniaxial loadings. These two examples demonstrate the utility of the method in
model selection and calibration by: (a) determining structural tensors of a
selected order across multiple symmetry groups, and (b) determining a basis for
a given group that allows the characterization of all subgroups. Using a common
order in both cases allows sparse regression to operate on a common function
representation to select the best-fit symmetry group for the data....

---

### 9. Elastic tensor-derived properties of composition-dependent disordered refractory binary alloys using DFPT

**Authors:** Surya T. Bijjala, Susan R. Atlas, Pankaj Kumar

**Published:** 2024-12-30

**Category:** cond-mat.mtrl-sci

**ID:** 2501.00127v3

**Link:** [http://arxiv.org/abs/2501.00127v3](http://arxiv.org/abs/2501.00127v3)

**Summary:** The elastic tensor provides valuable insight into the mechanical behavior of
a material with lattice strain, such as disordered binary alloys. Traditional
stress-strain methods have made it possible to compute elastic constants for
ordered structures and individually tailored alloy compositions. However, this
approach depends on predetermined or iteratively-chosen strain tensors. This
poses a significant challenge for systematic, composition-dependent studies of
disordered materials with low symmetry. DFPT provides a compelling alternative
to stress-strain methods: it allows for an unbiased determination of the
elastic tensor, as well as access to local field data derived from the
underlying general response function framework. Despite its intrinsic
flexibility and efficiency, DFPT has seen limited application to the study of
disordered systems. At the same time, there is a growing need for expanded
quantum mechanical data to improve predictive modeling of complex disordered
material properties. Here we present results for the rigid-ion and relaxed-ion
elastic tensors computed using DFPT, for a comprehensive set of structural
refractory BCC binary alloys of Mo, Nb, Ta, and W. We map the quantum-driven
heterogeneity in elastic constants and shear modulus, and associated relaxation
fields at each disordered structure lattice site, by computing the force
response internal strain tensor and displacement response internal strain
tensors. Derived properties -- the bulk modulus ($B$), shear modulus ($G$),
Young's modulus ($E$), Poisson's ratio ($\nu$), Pugh's ratio ($B/G$), Cauchy
pressure and elastic anisotropy -- are reported as a function of composition
for all refractory binaries. The DFPT-computed mechanical properties data for
the refractory binary alloys at systematically-varied Mo, Nb, Ta, and W
compositions are in excellent agreement with available experimental data....

---

### 10. Open Materials Generation with Stochastic Interpolants

**Authors:** Philipp Hoellmer, Thomas Egg, Maya M. Martirossyan, Eric Fuemmeler, Zeren Shui, Amit Gupta, Pawan Prakash, Adrian Roitberg, Mingjie Liu, George Karypis, Mark Transtrum, Richard G. Hennig, Ellad B. Tadmor, Stefano Martiniani

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.02582v2

**Link:** [http://arxiv.org/abs/2502.02582v2](http://arxiv.org/abs/2502.02582v2)

**Summary:** The discovery of new materials is essential for enabling technological
advancements. Computational approaches for predicting novel materials must
effectively learn the manifold of stable crystal structures within an infinite
design space. We introduce Open Materials Generation (OMatG), a unifying
framework for the generative design and discovery of inorganic crystalline
materials. OMatG employs stochastic interpolants (SI) to bridge an arbitrary
base distribution to the target distribution of inorganic crystals via a broad
class of tunable stochastic processes, encompassing both diffusion models and
flow matching as special cases. In this work, we adapt the SI framework by
integrating an equivariant graph representation of crystal structures and
extending it to account for periodic boundary conditions in unit cell
representations. Additionally, we couple the SI flow over spatial coordinates
and lattice vectors with discrete flow matching for atomic species. We
benchmark OMatG's performance on two tasks: Crystal Structure Prediction (CSP)
for specified compositions, and 'de novo' generation (DNG) aimed at discovering
stable, novel, and unique structures. In our ground-up implementation of OMatG,
we refine and extend both CSP and DNG metrics compared to previous works. OMatG
establishes a new state of the art in generative modeling for materials
discovery, outperforming purely flow-based and diffusion-based implementations.
These results underscore the importance of designing flexible deep learning
frameworks to accelerate progress in materials science. The OMatG code is
available at https://github.com/FERMat-ML/OMatG....

---

### 11. Unconventional Magnetism, Sliding Ferroelectricity, and Magneto-Optical Kerr Effects in a Multiferroic Bilayer

**Authors:** Chen Xinfeng, Ding Ning, Paolo Barone, Carlo Rizza, Shuai Dong, Wei Ren, Paolo G. Radaelli, Gaoyang Gou, Alessandro Stroppa

**Published:** 2025-07-09

**Category:** cond-mat.mtrl-sci

**ID:** 2507.06638v1

**Link:** [http://arxiv.org/abs/2507.06638v1](http://arxiv.org/abs/2507.06638v1)

**Summary:** Antiferromagnetic (AFM) materials offer a promising platform for exploring
novel couplings between altermagnetic (AM) spin-splitting and magneto-optical
Kerr effect (MOKE), with potential applications in next-generation quantum
technologies. In this work, first-principles calculations, symmetry analysis,
and kp modeling are employed to demonstrate how interlayer sliding in AFM
multiferroic bilayers enables engineering of the electronic, magnetic, and
magneto-optical properties. This study reveals an unprecedented
dimension-driven AM crossover, where the 2D paraelectric (PE) bilayer exhibits
spin-degenerate bands protected by the [C2||Mc] spin-space symmetry, while the
3D counterpart manifests AM spin-splitting along kz not equal to 0 paths.
Furthermore, interlayer sliding breaks the Mc symmetry and stabilizes a
ferroelectric (FE) state characterized by compensated ferrimagnetism and a
Zeeman effect, which produces non-relativistic spin-split bands. In the FE
phase, the inclusion of spin-orbit coupling (SOC) lifts accidental
degeneracies, creating `alternating' spin-polarized bands due to the interplay
of Zeeman and Rashba effects. Crucially, the spin polarization, ferro-valley
polarization, and Kerr angle are simultaneously reversible by switching either
interlayer sliding or the Neel vector. These findings highlight the rich
coupling between electronic, magnetic, and optical orders in sliding
multiferroics, thereby paving the way for ultra-low-power spintronics and
optoelectronic devices....

---

### 12. Two-color laser control of photocurrent and high harmonics in graphene

**Authors:** Minoru Kanega, Masahiro Sato

**Published:** 2024-10-10

**Category:** cond-mat.mes-hall

**ID:** 2410.07767v2

**Link:** [http://arxiv.org/abs/2410.07767v2](http://arxiv.org/abs/2410.07767v2)

**Summary:** We comprehensively investigate two-color-laser-driven photocurrent and high
harmonic generation (HHG) in graphene models. By numerically solving the
quantum master equation, we uniformly explore a broad parameter regime
including both the weak (perturbative) and intense-laser (nonperturbative)
cases while considering the dissipation effects. We demonstrate that the HHG
spectra can be drastically altered by tuning the real-space path traced by the
laser electric field. This controllability is explained by the dynamical
symmetry argument. We also show that both the magnitude and the direction of
photocurrent (zeroth order harmonics) can be controlled by varying the
frequency, intensity, ellipticity, and relative phase of the two-color laser.
Furthermore, the nature of photocurrent is shown to be classified into shift-
or injection-current types, depending on the phase of two-color laser. Our
findings indicate that even in centrosymmetric electron systems, photocurrent
and HHG can be quantitatively controlled by adjusting various external
parameters if we utilize multicolor laser with a lower spatial or temporal
symmetry....

---

### 13. Nonlinear denoising score matching for enhanced learning of structured distributions

**Authors:** Jeremiah Birrell, Markos A. Katsoulakis, Luc Rey-Bellet, Benjamin J. Zhang, Wei Zhu

**Published:** 2024-05-24

**Category:** stat.ML

**ID:** 2405.15625v2

**Link:** [http://arxiv.org/abs/2405.15625v2](http://arxiv.org/abs/2405.15625v2)

**Summary:** We present a novel method for training score-based generative models which
uses nonlinear noising dynamics to improve learning of structured
distributions. Generalizing to a nonlinear drift allows for additional
structure to be incorporated into the dynamics, thus making the training better
adapted to the data, e.g., in the case of multimodality or (approximate)
symmetries. Such structure can be obtained from the data by an inexpensive
preprocessing step. The nonlinear dynamics introduces new challenges into
training which we address in two ways: 1) we develop a new nonlinear denoising
score matching (NDSM) method, 2) we introduce neural control variates in order
to reduce the variance of the NDSM training objective. We demonstrate the
effectiveness of this method on several examples: a) a collection of
low-dimensional examples, motivated by clustering in latent space, b)
high-dimensional images, addressing issues with mode imbalance, small training
sets, and approximate symmetries, the latter being a challenge for methods
based on equivariant neural networks, which require exact symmetries, c) latent
space representation of high-dimensional data, demonstrating improved
performance with greatly reduced computational cost. Our method learns
score-based generative models with less data by flexibly incorporating
structure arising in the dataset....

---

### 14. Tailored-light photocurrent spectroscopy for probing time-reversal symmetry-broken phases

**Authors:** Daniel M. B. Lesko, Tobias Weitz, Simon Wittigschlager, Selina Nöcker, Weizhe Li, Peter Hommelhoff, Ofer Neufeld

**Published:** 2025-07-08

**Category:** physics.optics

**ID:** 2507.05768v1

**Link:** [http://arxiv.org/abs/2507.05768v1](http://arxiv.org/abs/2507.05768v1)

**Summary:** Light-field-driven photocurrents represent a powerful tool for generating
photocurrents without external bias in light-matter systems that lack inversion
symmetry. While these photocurrents are used in electronic applications, such
as current sources, switches, and photovoltaics, their presence can also be
used to probe material properties in and out of equilibrium, such as
topology.Here we advance this path of light-field-driven photocurrent
spectroscopy by utilizing tailored laser fields for ultrafast photocurrent
generation. We employ combinations of bichromatic linearly-polarized laser
beams that individually respect mirror and time-reversal symmetry (TRS). Hence
they do not lead to a field-driven photocurrent individually, but when
superposed can break individual symmetries and generate photocurrents. For
unique choices of the relative polarization angle and two-color phase the
tailored light exhibits TRS while breaking all other crystal symmetries, which
imposes a forbidden photocurrent selection rule in TRS-invariant systems as we
show both theoretically and experimentally. We employ state-of-the-art
\textit{ab-initio} simulations to validate this physical mechanism, and,
crucially, predict its breaking in materials with intrinsically-broken TRS,
creating a background free signal for magnetism and Chern physics. Our work
paves way for probing TRS-broken phases of matter in an ultrafast time-resolved
manner, not requiring the application of external magnetic fields or even
circularly-polarized electric fields....

---

### 15. Competing phases of HfO$_2$ from unstable flat phonon bands of an unconventional high-symmetry structure

**Authors:** Yubo Qi, Karin M. Rabe

**Published:** 2024-12-21

**Category:** cond-mat.mtrl-sci

**ID:** 2412.16792v2

**Link:** [http://arxiv.org/abs/2412.16792v2](http://arxiv.org/abs/2412.16792v2)

**Summary:** We carry out first-principles calculations to demonstrate that the complex
energy landscape and competing phases of HfO$_2$ can be understood from the
four unstable flat phonon bands of an unconventional high-symmetry structure of
HfO$_2$ with the space group $Cmma$. We consider structures generated from the
$Cmma$ reference structure by all possible combinations of the zone center and
zone boundary modes belonging to the unstable flat phonon branches. We find 12
distinct locally-stable structures, of which 5 correspond to well-known phases.
We also show that 8 of these 12 structures can be described as period-2
superlattices of the ferroelectric $Pca2_1$ (oIII), ferroelectric $Pnm2_1$
(oIV), monoclinic $P2_1/c$ (m) and distorted monoclinic $P2_1/c$ (dm)
structures. We demonstrate how the unstable flat phonon bands can explain the
atomically thin grain boundaries in the various types of superlattices.
Finally, we point out that arbitrary-period HfO$_2$ superlattices derived from
the 6 different types of period-2 superlattices are expected to form based on
the flatness of the unstable phonon branches. The organizing principle provided
by this work deepens our understanding of the underlying physics in the phase
stability of HfO$_2$ and provides guidance for functional phase stabilization....

---

### 16. Special-Unitary Parameterization for Trainable Variational Quantum Circuits

**Authors:** Kuan-Cheng Chen, Huan-Hsin Tseng, Samuel Yen-Chi Chen, Chen-Yu Liu, Kin K. Leung

**Published:** 2025-07-07

**Category:** quant-ph

**ID:** 2507.05535v1

**Link:** [http://arxiv.org/abs/2507.05535v1](http://arxiv.org/abs/2507.05535v1)

**Summary:** We propose SUN-VQC, a variational-circuit architecture whose elementary
layers are single exponentials of a symmetry-restricted Lie subgroup,
$\mathrm{SU}(2^{k}) \subset \mathrm{SU}(2^{n})$ with $k \ll n$. Confining the
evolution to this compact subspace reduces the dynamical Lie-algebra dimension
from $\mathcal{O}(4^{n})$ to $\mathcal{O}(4^{k})$, ensuring only polynomial
suppression of gradient variance and circumventing barren plateaus that plague
hardware-efficient ans\"atze. Exact, hardware-compatible gradients are obtained
using a generalized parameter-shift rule, avoiding ancillary qubits and
finite-difference bias. Numerical experiments on quantum auto-encoding and
classification show that SUN-VQCs sustain order-of-magnitude larger gradient
signals, converge 2--3$\times$ faster, and reach higher final fidelities than
depth-matched Pauli-rotation or hardware-efficient circuits. These results
demonstrate that Lie-subalgebra engineering provides a principled, scalable
route to barren-plateau-resilient VQAs compatible with near-term quantum
processors....

---

### 17. MBFormer: A General Transformer-based Learning Paradigm for Many-body Interactions in Real Materials

**Authors:** Bowen Hou, Xian Xu, Jinyuan Wu, Diana Y. Qiu

**Published:** 2025-07-07

**Category:** cond-mat.mtrl-sci

**ID:** 2507.05480v1

**Link:** [http://arxiv.org/abs/2507.05480v1](http://arxiv.org/abs/2507.05480v1)

**Summary:** Recently, radical progress in machine learning (ML) has revolutionized
computational materials science, enabling unprecedentedly rapid materials
discovery and property prediction, but the quantum many-body problem -- which
is the key to understanding excited-state properties, ranging from transport to
optics -- remains challenging due to the complexity of the nonlocal and
energy-dependent interactions. Here, we propose a symmetry-aware, grid-free,
transformer-based model, MBFormer, that is designed to learn the entire
many-body hierarchy directly from mean-field inputs, exploiting the attention
mechanism to accurately capture many-body correlations between mean-field
states. As proof of principle, we demonstrate the capability of MBFormer in
predicting results based on the GW plus Bethe Salpeter equation (GW-BSE)
formalism, including quasiparticle energies, exciton energies, exciton
oscillator strengths, and exciton wavefunction distribution. Our model is
trained on a dataset of 721 two-dimensional materials from the C2DB database,
achieving state-of-the-art performance with a low prediction mean absolute
error (MAE) on the order of 0.1-0.2 eV for state-level quasiparticle and
exciton energies across different materials. Moreover, we show explicitly that
the attention mechanism plays a crucial role in capturing many-body
correlations. Our framework provides an end-to-end platform from ground states
to general many-body prediction in real materials, which could serve as a
foundation model for computational materials science....

---

### 18. $\varphi$-Adapt: A Physics-Informed Adaptation Learning Approach to 2D Quantum Material Discovery

**Authors:** Hoang-Quan Nguyen, Xuan Bac Nguyen, Sankalp Pandey, Tim Faltermeier, Nicholas Borys, Hugh Churchill, Khoa Luu

**Published:** 2025-07-07

**Category:** cs.CV

**ID:** 2507.05184v1

**Link:** [http://arxiv.org/abs/2507.05184v1](http://arxiv.org/abs/2507.05184v1)

**Summary:** Characterizing quantum flakes is a critical step in quantum hardware
engineering because the quality of these flakes directly influences qubit
performance. Although computer vision methods for identifying two-dimensional
quantum flakes have emerged, they still face significant challenges in
estimating flake thickness. These challenges include limited data, poor
generalization, sensitivity to domain shifts, and a lack of physical
interpretability. In this paper, we introduce one of the first Physics-informed
Adaptation Learning approaches to overcome these obstacles. We focus on two
main issues, i.e., data scarcity and generalization. First, we propose a new
synthetic data generation framework that produces diverse quantum flake samples
across various materials and configurations, reducing the need for
time-consuming manual collection. Second, we present $\varphi$-Adapt, a
physics-informed adaptation method that bridges the performance gap between
models trained on synthetic data and those deployed in real-world settings.
Experimental results show that our approach achieves state-of-the-art
performance on multiple benchmarks, outperforming existing methods. Our
proposed approach advances the integration of physics-based modeling and domain
adaptation. It also addresses a critical gap in leveraging synthesized data for
real-world 2D material analysis, offering impactful tools for deep learning and
materials science communities....

---

### 19. BaZrS$_\text{3}$ Lights Up: The Interplay of Electrons, Photons, and Phonons in Strongly Luminescent Single Crystals

**Authors:** Rasmus Svejstrup Nielsen, Ángel Labordet Álvarez, Yvonne Tomm, Galina Gurieva, Andres Ortega-Guerrero, Joachim Breternitz, Lorenzo Bastonero, Nicola Marzari, Carlo Antonio Pignedoli, Susan Schorr, Mirjana Dimitrievska

**Published:** 2025-03-20

**Category:** cond-mat.mtrl-sci

**ID:** 2503.16180v4

**Link:** [http://arxiv.org/abs/2503.16180v4](http://arxiv.org/abs/2503.16180v4)

**Summary:** Chalcogenide perovskites have emerged as a promising class of materials for
the next generation of optoelectronic applications, with BaZrS$_\text{3}$
attracting significant attention due to its wide bandgap, earth-abundant
composition, and thermal and chemical stability. However, previous studies have
consistently reported weak and ambiguous photoluminescence (PL), regardless of
synthesis method, raising questions about the intrinsic optoelectronic quality
of this compound. In this work, we demonstrate strong, band-to-band-dominated
PL at room temperature in high-quality BaZrS$_\text{3}$ single crystals, with a
PL quantum yield of $\sim$0.005\%. Despite the narrow, single-component PL
emission band, time-resolved PL measurements reveal a carrier lifetime of
$1.0\pm0.2$ ns. To understand the origin of the strong PL and short carrier
lifetime, we perform multiwavelength excitation and polarization-dependent
Raman measurements, supported by first-principles lattice dynamics
calculations. We identify all 23 theoretically predicted Raman-active modes and
their symmetries, providing a comprehensive reference for future studies. Our
results indicate that phonon-assisted carrier decay and nontrivial
electron-phonon interactions contribute to the short carrier lifetimes, as
evidenced by Raman spectroscopy and DFT calculations. Further studies on
compositional variations or partial cation/anion substitutions could mitigate
electron-phonon coupling and enhance carrier lifetimes. By establishing a
detailed reference for the intrinsic vibrational and optoelectronic properties
of BaZrS$_\text{3}$, this work paves the way for further advancements in
chalcogenide perovskites for energy and optoelectronic technologies....

---

### 20. The Neural Networks with Tensor Weights and the Corresponding Fermionic Quantum Field Theory

**Authors:** Guojun Huang, Kai Zhou

**Published:** 2025-07-07

**Category:** hep-th

**ID:** 2507.05303v1

**Link:** [http://arxiv.org/abs/2507.05303v1](http://arxiv.org/abs/2507.05303v1)

**Summary:** In this paper, we establish a theoretical connection between complex-valued
neural networks (CVNNs) and fermionic quantum field theory (QFT), bridging a
fundamental gap in the emerging framework of neural network quantum field
theory (NN-QFT). While prior NN-QFT works have linked real-valued architectures
to bosonic fields, we demonstrate that CVNNs equipped with tensor-valued
weights intrinsically generate fermionic quantum fields. By promoting
hidden-to-output weights to Clifford algebra-valued tensors, we induce
anticommutation relations essential for fermionic statistics. Through
analytical study of the generating functional, we obtain the exact quantum
state in the infinite-width limit, revealing that the parameters between the
input layer and the last hidden layer correspond to the eigenvalues of the
quantum system, and the tensor weighting parameters in the hidden-to-output
layer map to dynamical fermionic fields. The continuum limit reproduces free
fermion correlators, with diagrammatic expansions confirming anticommutation.
The work provides the first explicit mapping from neural architectures to
fermionic QFT at the level of correlation functions and generating functional.
It extends NN-QFT beyond bosonic theories and opens avenues for encoding
fermionic symmetries into machine learning models, with potential applications
in quantum simulation and lattice field theory....

---

### 21. Thousand-Brains Systems: Sensorimotor Intelligence for Rapid, Robust Learning and Inference

**Authors:** Niels Leadholm, Viviane Clay, Scott Knudstrup, Hojae Lee, Jeff Hawkins

**Published:** 2025-07-06

**Category:** cs.AI

**ID:** 2507.04494v1

**Link:** [http://arxiv.org/abs/2507.04494v1](http://arxiv.org/abs/2507.04494v1)

**Summary:** Current AI systems achieve impressive performance on many tasks, yet they
lack core attributes of biological intelligence, including rapid, continual
learning, representations grounded in sensorimotor interactions, and structured
knowledge that enables efficient generalization. Neuroscience theory suggests
that mammals evolved flexible intelligence through the replication of a
semi-independent, sensorimotor module, a functional unit known as a cortical
column. To address the disparity between biological and artificial
intelligence, thousand-brains systems were proposed as a means of mirroring the
architecture of cortical columns and their interactions.
  In the current work, we evaluate the unique properties of Monty, the first
implementation of a thousand-brains system. We focus on 3D object perception,
and in particular, the combined task of object recognition and pose estimation.
Utilizing the YCB dataset of household objects, we first assess Monty's use of
sensorimotor learning to build structured representations, finding that these
enable robust generalization. These representations include an emphasis on
classifying objects by their global shape, as well as a natural ability to
detect object symmetries. We then explore Monty's use of model-free and
model-based policies to enable rapid inference by supporting principled
movements. We find that such policies complement Monty's modular architecture,
a design that can accommodate communication between modules to further
accelerate inference speed via a novel `voting' algorithm. Finally, we examine
Monty's use of associative, Hebbian-like binding to enable rapid, continual,
and computationally efficient learning, properties that compare favorably to
current deep learning architectures. While Monty is still in a nascent stage of
development, these findings support thousand-brains systems as a powerful and
promising new approach to AI....

---

### 22. Machine Learning-Based Prediction of Metal-Organic Framework Materials: A Comparative Analysis of Multiple Models

**Authors:** Zhuo Zheng, Keyan Liu, Xiyuan Zhu

**Published:** 2025-07-06

**Category:** cs.LG

**ID:** 2507.04493v1

**Link:** [http://arxiv.org/abs/2507.04493v1](http://arxiv.org/abs/2507.04493v1)

**Summary:** Metal-organic frameworks (MOFs) have emerged as promising materials for
various applications due to their unique structural properties and versatile
functionalities. This study presents a comprehensive investigation of machine
learning approaches for predicting MOF material properties. We employed five
different machine learning models: Random Forest, XGBoost, LightGBM, Support
Vector Machine, and Neural Network, to analyze and predict MOF characteristics
using a dataset from the Kaggle platform. The models were evaluated using
multiple performance metrics, including RMSE, R^2, MAE, and cross-validation
scores. Results demonstrated that the Random Forest model achieved superior
performance with an R^2 value of 0.891 and RMSE of 0.152, significantly
outperforming other models. LightGBM showed remarkable computational
efficiency, completing training in 25.7 seconds while maintaining high
accuracy. Our comparative analysis revealed that ensemble learning methods
generally exhibited better performance than traditional single models in MOF
property prediction. This research provides valuable insights into the
application of machine learning in materials science and establishes a robust
framework for future MOF material design and property prediction....

---

### 23. Music102: An $D_{12}$-equivariant transformer for chord progression accompaniment

**Authors:** Weiliang Luo

**Published:** 2024-10-23

**Category:** cs.SD

**ID:** 2410.18151v2

**Link:** [http://arxiv.org/abs/2410.18151v2](http://arxiv.org/abs/2410.18151v2)

**Summary:** We present Music102, an advanced model aimed at enhancing chord progression
accompaniment through a $D_{12}$-equivariant transformer. Inspired by group
theory and symbolic music structures, Music102 leverages musical symmetry--such
as transposition and reflection operations--integrating these properties into
the transformer architecture. By encoding prior music knowledge, the model
maintains equivariance across both melody and chord sequences. The POP909
dataset was employed to train and evaluate Music102, revealing significant
improvements over the non-equivariant Music101 prototype Music101 in both
weighted loss and exact accuracy metrics, despite using fewer parameters. This
work showcases the adaptability of self-attention mechanisms and layer
normalization to the discrete musical domain, addressing challenges in
computational music analysis. With its stable and flexible neural framework,
Music102 sets the stage for further exploration in equivariant music generation
and computational composition tools, bridging mathematical theory with
practical music performance....

---

### 24. TopoMAS: Large Language Model Driven Topological Materials Multiagent System

**Authors:** Baohua Zhang, Xin Li, Huangchao Xu, Zhong Jin, Quansheng Wu, Ce Li

**Published:** 2025-07-05

**Category:** cond-mat.mtrl-sci

**ID:** 2507.04053v1

**Link:** [http://arxiv.org/abs/2507.04053v1](http://arxiv.org/abs/2507.04053v1)

**Summary:** Topological materials occupy a frontier in condensed-matter physics thanks to
their remarkable electronic and quantum properties, yet their cross-scale
design remains bottlenecked by inefficient discovery workflows. Here, we
introduce TopoMAS (Topological materials Multi-Agent System), an interactive
human-AI framework that seamlessly orchestrates the entire materials-discovery
pipeline: from user-defined queries and multi-source data retrieval, through
theoretical inference and crystal-structure generation, to first-principles
validation. Crucially, TopoMAS closes the loop by autonomously integrating
computational outcomes into a dynamic knowledge graph, enabling continuous
knowledge refinement. In collaboration with human experts, it has already
guided the identification of novel topological phases SrSbO3, confirmed by
first-principles calculations. Comprehensive benchmarks demonstrate robust
adaptability across base Large Language Model, with the lightweight Qwen2.5-72B
model achieving 94.55% accuracy while consuming only 74.3-78.4% of tokens
required by Qwen3-235B and 83.0% of DeepSeek-V3's usage--delivering responses
twice as fast as Qwen3-235B. This efficiency establishes TopoMAS as an
accelerator for computation-driven discovery pipelines. By harmonizing rational
agent orchestration with a self-evolving knowledge graph, our framework not
only delivers immediate advances in topological materials but also establishes
a transferable, extensible paradigm for materials-science domain....

---

### 25. Ferroelectrically Switchable Half-Quantized Hall Effect

**Authors:** M. U. Muzaffar, Kai-Zhi Bai, Wei Qin, Guohua Cao, Bo Fu, Ping Cui, Shun-Qing Shen, Zhenyu Zhang

**Published:** 2025-07-05

**Category:** cond-mat.mes-hall

**ID:** 2507.03985v1

**Link:** [http://arxiv.org/abs/2507.03985v1](http://arxiv.org/abs/2507.03985v1)

**Summary:** Integrating ferroelectricity, antiferromagnetism, and topological quantum
transport within a single material is rare, but crucial for developing
next-generation quantum devices. Here, we propose a multiferroic
heterostructure consisting of an antiferromagnetic MnBi$_2$Te$_4$ bilayer and
an Sb$_2$Te$_3$ film is able to harbor the half-quantized Hall (HQH) effect
with a ferroelectrically switchable Hall conductivity of $e^2/2h$. We first
show that, in the energetically stable configuration, the antiferromagnetic
MnBi$_2$Te$_4$ bilayer opens a gap in the top surface bands of Sb$_2$Te$_3$
through proximity effect, while its bottom surface bands remain gapless;
consequently, HQH conductivity of $e^2/2h$ can be sustained clockwise or
counterclockwise depending on antiferromagnetic configuration of the
MnBi$_2$Te$_4$. Remarkably, when applying interlayer sliding within the
MnBi$_2$Te$_4$ bilayer, its electric polarization direction associated with
parity-time reversal symmetry breaking is reversed, accompanied by a reversal
of the HQH conductivity. The proposed approach offers a powerful route to
control topological quantum transport in antiferromagnetic materials by
ferroelectricity....

---

### 26. Symmetry-Robust 3D Orientation Estimation

**Authors:** Christopher Scarvelis, David Benhaim, Paul Zhang

**Published:** 2024-10-02

**Category:** cs.CV

**ID:** 2410.02101v4

**Link:** [http://arxiv.org/abs/2410.02101v4](http://arxiv.org/abs/2410.02101v4)

**Summary:** Orientation estimation is a fundamental task in 3D shape analysis which
consists of estimating a shape's orientation axes: its side-, up-, and
front-axes. Using this data, one can rotate a shape into canonical orientation,
where its orientation axes are aligned with the coordinate axes. Developing an
orientation algorithm that reliably estimates complete orientations of general
shapes remains an open problem. We introduce a two-stage orientation pipeline
that achieves state of the art performance on up-axis estimation and further
demonstrate its efficacy on full-orientation estimation, where one seeks all
three orientation axes. Unlike previous work, we train and evaluate our method
on all of Shapenet rather than a subset of classes. We motivate our engineering
contributions by theory describing fundamental obstacles to orientation
estimation for rotationally-symmetric shapes, and show how our method avoids
these obstacles....

---

### 27. CosmoBench: A Multiscale, Multiview, Multitask Cosmology Benchmark for Geometric Deep Learning

**Authors:** Ningyuan Huang, Richard Stiskalek, Jun-Young Lee, Adrian E. Bayer, Charles C. Margossian, Christian Kragh Jespersen, Lucia A. Perez, Lawrence K. Saul, Francisco Villaescusa-Navarro

**Published:** 2025-07-04

**Category:** cs.LG

**ID:** 2507.03707v1

**Link:** [http://arxiv.org/abs/2507.03707v1](http://arxiv.org/abs/2507.03707v1)

**Summary:** Cosmological simulations provide a wealth of data in the form of point clouds
and directed trees. A crucial goal is to extract insights from this data that
shed light on the nature and composition of the Universe. In this paper we
introduce CosmoBench, a benchmark dataset curated from state-of-the-art
cosmological simulations whose runs required more than 41 million core-hours
and generated over two petabytes of data. CosmoBench is the largest dataset of
its kind: it contains 34 thousand point clouds from simulations of dark matter
halos and galaxies at three different length scales, as well as 25 thousand
directed trees that record the formation history of halos on two different time
scales. The data in CosmoBench can be used for multiple tasks -- to predict
cosmological parameters from point clouds and merger trees, to predict the
velocities of individual halos and galaxies from their collective positions,
and to reconstruct merger trees on finer time scales from those on coarser time
scales. We provide several baselines on these tasks, some based on established
approaches from cosmological modeling and others rooted in machine learning.
For the latter, we study different approaches -- from simple linear models that
are minimally constrained by symmetries to much larger and more
computationally-demanding models in deep learning, such as graph neural
networks. We find that least-squares fits with a handful of invariant features
sometimes outperform deep architectures with many more parameters and far
longer training times. Still there remains tremendous potential to improve
these baselines by combining machine learning and cosmology to fully exploit
the data. CosmoBench sets the stage for bridging cosmology and geometric deep
learning at scale. We invite the community to push the frontier of scientific
discovery by engaging with this dataset, available at
https://cosmobench.streamlit.app...

---

### 28. SymmetryLens: Unsupervised Symmetry Learning via Locality and Density Preservation

**Authors:** Onur Efe, Arkadas Ozakin

**Published:** 2024-10-07

**Category:** cs.LG

**ID:** 2410.05232v2

**Link:** [http://arxiv.org/abs/2410.05232v2](http://arxiv.org/abs/2410.05232v2)

**Summary:** We develop a new unsupervised symmetry learning method that starts with raw
data and provides the minimal generator of an underlying Lie group of
symmetries, together with a symmetry-equivariant representation of the data,
which turns the hidden symmetry into an explicit one. The method is able to
learn the pixel translation operator from a dataset with only an approximate
translation symmetry and can learn quite different types of symmetries that are
not apparent to the naked eye. The method is based on the formulation of an
information-theoretic loss function that measures both the degree of symmetry
of a dataset under a candidate symmetry generator and a proposed notion of
locality of the samples, which is coupled to symmetry. We demonstrate that this
coupling between symmetry and locality, together with an optimization technique
developed for entropy estimation, results in a stable system that provides
reproducible results....

---

### 29. Kinetic Langevin Diffusion for Crystalline Materials Generation

**Authors:** François Cornet, Federico Bergamin, Arghya Bhowmik, Juan Maria Garcia Lastra, Jes Frellsen, Mikkel N. Schmidt

**Published:** 2025-07-04

**Category:** cs.LG

**ID:** 2507.03602v1

**Link:** [http://arxiv.org/abs/2507.03602v1](http://arxiv.org/abs/2507.03602v1)

**Summary:** Generative modeling of crystalline materials using diffusion models presents
a series of challenges: the data distribution is characterized by inherent
symmetries and involves multiple modalities, with some defined on specific
manifolds. Notably, the treatment of fractional coordinates representing atomic
positions in the unit cell requires careful consideration, as they lie on a
hypertorus. In this work, we introduce Kinetic Langevin Diffusion for Materials
(KLDM), a novel diffusion model for crystalline materials generation, where the
key innovation resides in the modeling of the coordinates. Instead of resorting
to Riemannian diffusion on the hypertorus directly, we generalize Trivialized
Diffusion Model (TDM) to account for the symmetries inherent to crystals. By
coupling coordinates with auxiliary Euclidean variables representing
velocities, the diffusion process is now offset to a flat space. This allows us
to effectively perform diffusion on the hypertorus while providing a training
objective that accounts for the periodic translation symmetry of the true data
distribution. We evaluate KLDM on both Crystal Structure Prediction (CSP) and
De-novo Generation (DNG) tasks, demonstrating its competitive performance with
current state-of-the-art models....

---

### 30. Magnetocrystalline anisotropy of FeNi and FeCo along the Bain path

**Authors:** Nica Jane B. Ferrer, Gregory A. Fiete

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.01120v2

**Link:** [http://arxiv.org/abs/2507.01120v2](http://arxiv.org/abs/2507.01120v2)

**Summary:** We theoretically investigate magnetic anisotropy in materials with
non-critical elements to determine which symmetry conditions and atomic shell
filling favor enhanced magnetic anisotropy. We study the magnetocrystalline
anisotropies (MCA) of the equiatomic ferrous compounds FeCo and FeNi using ab
initio calculations and analytical approaches via the diatomic pair model. We
find that when these materials undergo a Bain transformation, that is, the
variation of the a and c lattice parameters adjust to interpolate between the
B2 and L10 structural phases while keeping the unit cell volume constant, the
MCA versus r = c/a ratio varies differently for FeCo and FeNi despite Co and Ni
differing only by one valence electron. To uncover the physics governing these
trends, we use a diatomic pair model to perform a theoretical analysis of the
ab initio results. We find that the MCA variation along the Bain path is
correlated with the structural phase of the material as well as the occupation
of (l, m)-resolved states for each equiatomic ferrous compound. Accordingly,
the MCA was found to differ depending on the element paired with Fe to form the
Fe-X compound (X = Co, Ni). Our work could help guide the scientific community
in solving the supply crisis of hard/strong permanent magnets that are crucial
for various technological applications such as those depending on motors and
generators for energy conversion and clean energy applications....

---

### 31. Synthesizable by Design: A Retrosynthesis-Guided Framework for Molecular Analog Generation

**Authors:** Shuan Chen, Gunwook Nam, Yousung Jung

**Published:** 2025-07-03

**Category:** physics.chem-ph

**ID:** 2507.02752v1

**Link:** [http://arxiv.org/abs/2507.02752v1](http://arxiv.org/abs/2507.02752v1)

**Summary:** The disconnect between AI-generated molecules with desirable properties and
their synthetic feasibility remains a critical bottleneck in computational drug
and material discovery. While generative AI has accelerated the proposal of
candidate molecules, many of these structures prove challenging or impossible
to synthesize using established chemical reactions. Here, we introduce
SynTwins, a novel retrosynthesis-guided molecular analog design framework that
designs synthetically accessible molecular analogs by emulating expert chemist
strategies through a three-step process: retrosynthesis, similar building block
searching, and virtual synthesis. In comparative evaluations, SynTwins
demonstrates superior performance in generating synthetically accessible
analogs compared to state-of-the-art machine learning models while maintaining
high structural similarity to original target molecules. Furthermore, when
integrated with existing molecule optimization frameworks, our hybrid approach
produces synthetically feasible molecules with property profiles comparable to
unconstrained molecule generators, yet its synthesizability ensured. Our
comprehensive benchmarking across diverse molecular datasets demonstrates that
SynTwins effectively bridges the gap between computational design and
experimental synthesis, providing a practical solution for accelerating the
discovery of synthesizable molecules with desired properties for a wide range
of applications....

---

### 32. Identifying Systems with Symmetries using Equivariant Autoregressive Reservoir Computers

**Authors:** Fredy Vides, Idelfonso B. R. Nogueira, Gabriela Lopez Gutierrez, Lendy Banegas, Evelyn Flores

**Published:** 2023-11-16

**Category:** eess.SY

**ID:** 2311.09511v4

**Link:** [http://arxiv.org/abs/2311.09511v4](http://arxiv.org/abs/2311.09511v4)

**Summary:** The investigation reported in this document focuses on identifying systems
with symmetries using equivariant autoregressive reservoir computers. General
results in structured matrix approximation theory are presented, exploring a
two-fold approach. Firstly, a comprehensive examination of generic
symmetry-preserving nonlinear time delay embedding is conducted. This involves
analyzing time series data sampled from an equivariant system under study.
Secondly, sparse least-squares methods are applied to discern approximate
representations of the output coupling matrices. These matrices play a critical
role in determining the nonlinear autoregressive representation of an
equivariant system. The structural characteristics of these matrices are
dictated by the set of symmetries inherent in the system. The document outlines
prototypical algorithms derived from the described techniques, offering insight
into their practical applications. Emphasis is placed on the significant
improvement on structured identification precision when compared to classical
reservoir computing methods for the simulation of equivariant dynamical
systems....

---

### 33. Unconventional Spintronics from Chiral Perovskites

**Authors:** Yuntian Liu, Reshna Shrestha, Konstantin Denisov, Denzel Ayala, Mark van Schilfgaarde, Wanyi Nie, Igor Žutić

**Published:** 2025-07-02

**Category:** cond-mat.mtrl-sci

**ID:** 2507.02060v1

**Link:** [http://arxiv.org/abs/2507.02060v1](http://arxiv.org/abs/2507.02060v1)

**Summary:** Spintronic devices typically employ heterostructures with ferromagnets which
break time-reversal symmetry and have non-vanishing magnetization. With the
growing class of materials that support spin-polarized carriers, current, and
excitations,it is possible to envision emerging spintronic applications that
are not limited to magnetoresistance. Here we focus on chiral perovskites with
no net magnetization where the space-inversion and mirror symmetries are broken
to induce chiral structure. The known importance of these perovskites is
further expanded by the demonstration of the chiral-induced spin selectivity
(CISS). However, the generation of the spin-polarized carriers across the
interface with these chiral perovskites remains to be fully understood. Our
first-principles studies for two-dimensional PbBr$_4$-based chiral perovskites
provide their electronic structure and an orbital-based symmetry analysis,
which allows us to establish an effective Hamiltonian to elucidate the
underlying origin of their chirality. We also use this analysis for the
Edelstein effect, responsible for electrical generation of the nonequilibrium
spin polarization in many materials, which in chiral perovskites could be a
mechanism contributing to CISS. Furthermore, by examining optical properties of
chiral perovskites and the opportunity to use them to realize tunable
altermagnets, another class of zero-magnetization spintronic materials, we put
forth a versatile materials platform for unconventional spintronics....

---

### 34. Advancing Magnetic Materials Discovery -- A structure-based machine learning approach for magnetic ordering and magnetic moment prediction

**Authors:** Apoorv Verma, Junaid Jami, Amrita Bhattacharya

**Published:** 2025-07-02

**Category:** cond-mat.mtrl-sci

**ID:** 2507.01913v1

**Link:** [http://arxiv.org/abs/2507.01913v1](http://arxiv.org/abs/2507.01913v1)

**Summary:** Accurately predicting magnetic behavior across diverse materials systems
remains a longstanding challenge due to the complex interplay of structural and
electronic factors and is pivotal for the accelerated discovery and design of
next-generation magnetic materials. In this work, a refined descriptor is
proposed that significantly improves the prediction of two critical magnetic
properties -- magnetic ordering (Ferromagnetic vs. Ferrimagnetic) and magnetic
moment per atom -- using only the structural information of materials. Unlike
previous models limited to Mn-based or lanthanide-transition metal compounds,
the present approach generalizes across a diverse dataset of 5741 stable,
binary and ternary, ferromagnetic and ferrimagnetic compounds sourced from the
Materials Project. Leveraging an enriched elemental vector representation and
advanced feature engineering, including nonlinear terms and reduced matrix
sparsity, the LightGBM-based model achieves an accuracy of 82.4% for magnetic
ordering classification and balanced recall across FM and FiM classes,
addressing a key limitation in prior studies. The model predicts magnetic
moment per atom with a correlation coefficient of 0.93, surpassing the Hund's
matrix and orbital field matrix descriptors. Additionally, it accurately
estimates formation energy per atom, enabling assessment of both magnetic
behavior and material stability. This generalized and computationally efficient
framework offers a robust tool for high-throughput screening of magnetic
materials with tailored properties....

---

### 35. Quasi-symmetry Constrained Spin Ferromagnetism in Altermagnets

**Authors:** Mercè Roig, Yue Yu, Rune C. Ekman, Andreas Kreisel, Brian M. Andersen, Daniel F. Agterberg

**Published:** 2024-12-12

**Category:** cond-mat.str-el

**ID:** 2412.09338v2

**Link:** [http://arxiv.org/abs/2412.09338v2](http://arxiv.org/abs/2412.09338v2)

**Summary:** Altermagnets break time-reversal symmetry and their spin-orbit coupling (SOC)
allow for an anomalous Hall effect (AHE) that depends on the direction of the
N\'eel ordering vector. The AHE and the ferromagnetic spin moment share the
same symmetry and hence are usually proportional. However, density functional
theory (DFT) calculations find that the AHE exists with negligible
ferromagnetic spin moment for some compounds, whereas it reaches sizable values
for other altermagnets. By examining realistic minimal models for
altermagnetism in which the DFT phenomenology is captured, we uncover a general
SOC-enabled quasi-symmetry, the uniaxial spin space-group, that provides a
natural explanation for the amplitude of the ferromagnetic spin moment across
the vast range of different altermagnetic materials. Additionally, we derive
analytic expressions for the magnetic anisotropy energy, providing a simple
means to identify the preferred N\'eel vector orientation for altermagnets....

---

### 36. Hybrid antiferroelectric-ferroelectric domain walls in noncollinear antipolar oxides

**Authors:** Ivan N. Ushakov, Mats Topstad, Muhammad Z. Khalid, Niyorjyoti Sharma, Christoph Grams, Ursula Ludacka, Jiali He, Kasper A. Hunnestad, Mohsen Sadeqi-Moqadam, Julia Glaum, Sverre M. Selbach, Joachim Hemberger, Petra Becker, Ladislav Bohatý, Amit Kumar, Jorge Íñiguez-González, Antonius T. J. van Helvoort, Dennis Meier

**Published:** 2025-07-02

**Category:** cond-mat.mtrl-sci

**ID:** 2507.01622v1

**Link:** [http://arxiv.org/abs/2507.01622v1](http://arxiv.org/abs/2507.01622v1)

**Summary:** Antiferroelectrics are emerging as advanced functional materials and are
fertile ground for unusual electric effects. For example, they enhance the
recoverable energy density in energy storage applications and give rise to
large electromechanical responses. Here, we demonstrate noncollinearity in
dipolar order as an additional degree of freedom, unlocking physical properties
that are symmetry-forbidden in classical antiferroelectrics. We show that
noncollinear order of electric dipole moments in
K$_3$[Nb$_3$O$_6$|(BO$_3$)$_2$] leads to a coexistence of antiferroelectric and
ferroelectric behaviors. Besides the double-hysteresis loop observed in
antiferroelectrics, a pronounced piezoresponse and electrically switchable
domains are observed, separated by atomically sharp and micrometer-long charged
domain walls. Hybrid antiferroelectric-ferroelectric responses are expected in
a wide range of noncollinear systems, giving a new dimension to the research on
antiferroelectrics and multifunctional oxides in general....

---

### 37. Text to Band Gap: Pre-trained Language Models as Encoders for Semiconductor Band Gap Prediction

**Authors:** Ying-Ting Yeh, Janghoon Ock, Shagun Maheshwari, Amir Barati Farimani

**Published:** 2025-01-07

**Category:** cs.CL

**ID:** 2501.03456v2

**Link:** [http://arxiv.org/abs/2501.03456v2](http://arxiv.org/abs/2501.03456v2)

**Summary:** We investigate the use of transformer-based language models, RoBERTa, T5, and
LLaMA, for predicting the band gaps of semiconductor materials directly from
textual representations that encode key material features such as chemical
composition, crystal system, space group, number of atoms per unit cell,
valence electron count, and other relevant electronic and structural
properties. Quantum chemistry simulations such as DFT provide accurate
predictions but are computationally intensive, limiting their feasibility for
large-scale materials screening. Shallow ML models offer faster alternatives
but typically require extensive data preprocessing to convert non-numerical
material features into structured numerical inputs, often at the cost of losing
critical descriptive information. In contrast, our approach leverages
pretrained language models to process textual data directly, eliminating the
need for manual feature engineering. We construct material descriptions in two
formats: structured strings that combine key features in a consistent template,
and natural language narratives generated using the ChatGPT API. For each
model, we append a custom regression head and perform task-specific finetuning
on a curated dataset of inorganic compounds. Our results show that finetuned
language models, particularly the decoder-only LLaMA-3 architecture, can
outperform conventional approaches in prediction accuracy and flexibility,
achieving an MAE of 0.25 eV and R2 of 0.89, compared to the best shallow ML
baseline, which achieved an MAE of 0.32 eV and R2 of 0.84. Notably, LLaMA-3
achieves competitive accuracy with minimal finetuning, suggesting its
architecture enables more transferable representations for scientific tasks.
This work demonstrates the effectiveness of finetuned language models for
scientific property prediction and provides a scalable, language-native
framework for materials informatics....

---

### 38. TABASCO: A Fast, Simplified Model for Molecular Generation with Improved Physical Quality

**Authors:** Carlos Vonessen, Charles Harris, Miruna Cretu, Pietro Liò

**Published:** 2025-07-01

**Category:** cs.LG

**ID:** 2507.00899v1

**Link:** [http://arxiv.org/abs/2507.00899v1](http://arxiv.org/abs/2507.00899v1)

**Summary:** State-of-the-art models for 3D molecular generation are based on significant
inductive biases, SE(3), permutation equivariance to respect symmetry and graph
message-passing networks to capture local chemistry, yet the generated
molecules still struggle with physical plausibility. We introduce TABASCO which
relaxes these assumptions: The model has a standard non-equivariant transformer
architecture, treats atoms in a molecule as sequences and reconstructs bonds
deterministically after generation. The absence of equivariant layers and
message passing allows us to significantly simplify the model architecture and
scale data throughput. On the GEOM-Drugs benchmark TABASCO achieves
state-of-the-art PoseBusters validity and delivers inference roughly 10x faster
than the strongest baseline, while exhibiting emergent rotational equivariance
despite symmetry not being hard-coded. Our work offers a blueprint for training
minimalist, high-throughput generative models suited to specialised tasks such
as structure- and pharmacophore-based drug design. We provide a link to our
implementation at github.com/carlosinator/tabasco....

---

### 39. Monolayer Two-dimensional Materials Database (ML2DDB) and Applications

**Authors:** Zhongwei Liu, Zhimin Zhang, Xuwei Liu, Mingjia Yao, Xin He, Yuanhui Sun, Xin Chen, Lijun Zhang

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00584v1

**Link:** [http://arxiv.org/abs/2507.00584v1](http://arxiv.org/abs/2507.00584v1)

**Summary:** The discovery of two-dimensional (2D) materials with tailored properties is
critical to meet the increasing demands of high-performance applications across
flexible electronics, optoelectronics, catalysis, and energy storage. However,
current 2D material databases are constrained by limited scale and
compositional diversity. In this study, we introduce a scalable active learning
workflow that integrates deep neural networks with density functional theory
(DFT) calculations to efficiently explore a vast set of candidate structures.
These structures are generated through physics-informed elemental substitution
strategies, enabling broad and systematic discovery of stable 2D materials.
Through six iterative screening cycles, we established the creation of the
Monolayer 2D Materials Database (ML2DDB), which contains 242,546 DFT-validated
stable structures-an order-of-magnitude increase over the largest known 2D
materials databases. In particular, the number of ternary and quaternary
compounds showed the most significant increase. Combining this database with a
generative diffusion model, we demonstrated effective structure generation
under specified chemistry and symmetry constraints. This work accomplished an
organically interconnected loop of 2D material data expansion and application,
which provides a new paradigm for the discovery of new materials....

---

### 40. Rotational Sampling: A Plug-and-Play Encoder for Rotation-Invariant 3D Molecular GNNs

**Authors:** Dian Jin

**Published:** 2025-07-01

**Category:** cs.LG

**ID:** 2507.01073v1

**Link:** [http://arxiv.org/abs/2507.01073v1](http://arxiv.org/abs/2507.01073v1)

**Summary:** Graph neural networks (GNNs) have achieved remarkable success in molecular
property prediction. However, traditional graph representations struggle to
effectively encode the inherent 3D spatial structures of molecules, as
molecular orientations in 3D space introduce significant variability, severely
limiting model generalization and robustness. Existing approaches primarily
focus on rotation-invariant and rotation-equivariant methods. Invariant methods
often rely heavily on prior knowledge and lack sufficient generalizability,
while equivariant methods suffer from high computational costs. To address
these limitations, this paper proposes a novel plug-and-play 3D encoding module
leveraging rotational sampling. By computing the expectation over the SO(3)
rotational group, the method naturally achieves approximate rotational
invariance. Furthermore, by introducing a carefully designed post-alignment
strategy, strict invariance can be achieved without compromising performance.
Experimental evaluations on the QM9 and C10 Datasets demonstrate superior
predictive accuracy, robustness, and generalization performance compared to
existing methods. Moreover, the proposed approach maintains low computational
complexity and enhanced interpretability, providing a promising direction for
efficient and effective handling of 3D molecular information in drug discovery
and material design....

---

### 41. Process-aware and high-fidelity microstructure generation using stable diffusion

**Authors:** Hoang Cuong Phan, Minh Tien Tran, Chihun Lee, Hoheok Kim, Sehyok Oh, Dong-Kyu Kim, Ho Won Lee

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00459v1

**Link:** [http://arxiv.org/abs/2507.00459v1](http://arxiv.org/abs/2507.00459v1)

**Summary:** Synthesizing realistic microstructure images conditioned on processing
parameters is crucial for understanding process-structure relationships in
materials design. However, this task remains challenging due to limited
training micrographs and the continuous nature of processing variables. To
overcome these challenges, we present a novel process-aware generative modeling
approach based on Stable Diffusion 3.5 Large (SD3.5-Large), a state-of-the-art
text-to-image diffusion model adapted for microstructure generation. Our method
introduces numeric-aware embeddings that encode continuous variables (annealing
temperature, time, and magnification) directly into the model's conditioning,
enabling controlled image generation under specified process conditions and
capturing process-driven microstructural variations. To address data scarcity
and computational constraints, we fine-tune only a small fraction of the
model's weights via DreamBooth and Low-Rank Adaptation (LoRA), efficiently
transferring the pre-trained model to the materials domain. We validate realism
using a semantic segmentation model based on a fine-tuned U-Net with a VGG16
encoder on 24 labeled micrographs. It achieves 97.1% accuracy and 85.7% mean
IoU, outperforming previous methods. Quantitative analyses using physical
descriptors and spatial statistics show strong agreement between synthetic and
real microstructures. Specifically, two-point correlation and lineal-path
errors remain below 2.1% and 0.6%, respectively. Our method represents the
first adaptation of SD3.5-Large for process-aware microstructure generation,
offering a scalable approach for data-driven materials design....

---

### 42. Second-order microscopic nonlinear susceptibility in a centrosymmetric material: application to imaging valence electron motion

**Authors:** Chance Ornelas-Skarin, Tatiana Bezriadina, Matthias Fuchs, Shambhu Ghimire, J. B. Hastings, Quynh L Nguyen, Gilberto de la Peña, Takahiro Sato, Sharon Shwartz, Mariano Trigo, Diling Zhu, Daria Popova-Gorelova, David A. Reis

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00441v1

**Link:** [http://arxiv.org/abs/2507.00441v1](http://arxiv.org/abs/2507.00441v1)

**Summary:** We report measurements of phase-matched nonlinear x-ray and optical
sum-frequency generation from single-crystal silicon using sub-resonant 0.95 eV
laser pulses and 9.5 keV hard x-ray pulses from the LCLS free-electron laser.
The sum-frequency signal appears as energy and momentum sidebands to the
elastic Bragg peak. It is proportional to the magnitude squared of the relevant
temporal and spatial Fourier components of the optically induced microscopic
charges/currents. We measure the first- and second-order sideband to the 220
Bragg peak and find that the efficiency is maximized when the applied field is
along the reciprocal lattice vector. For an optical intensity of $\sim10^{12}
\text{W}/\text{cm}^2$, we measure peak efficiencies of $3\times 10^{-7}$ and
$3\times 10^{-10}$ for the first and second-order sideband respectively
(relative to the elastic Bragg peak). The first-order sideband is consistent
with induced microscopic currents along the applied electric field (consistent
with an isotropic response). The second-order sideband depends nontrivially on
the optical field orientation and is consistent with an anisotropic response
originating from induced charges along the bonds with C$_{3v}$ site symmetry.
The results agree well with first-principles Bloch-Floquet calculations....

---

### 43. Generation of Pure Spin Current with Insulating Antiferromagnetic Materials

**Authors:** Yingwei Chen, Junyi Ji, Liangliang Hong, Xiangang Wan, Hongjun Xiang

**Published:** 2025-07-01

**Category:** cond-mat.mtrl-sci

**ID:** 2507.00369v1

**Link:** [http://arxiv.org/abs/2507.00369v1](http://arxiv.org/abs/2507.00369v1)

**Summary:** The generation of pure spin currents is critical for low-dissipation
spintronic applications, yet existing methods relying on spin-orbit coupling or
ferromagnetic interfaces face challenges in material compatibility and
operational robustness. We propose a paradigm-shifting approach to generate
symmetry-protected pure spin currents by applying mechanical stress on
insulating antiferromagnetic materials, i.e., the pure piezospintronic effect.
We first classify magnetic point groups enabling pure piezospintronic effects.
A novel first-principles method is developed to compute the spin dipole moments
and coefficients of the piezospintronic effect. Integrating these methodologies
with high-throughput screening, we identify FeOOH, Cr2O3 and NaMnX (X=As, Bi,
P, Sb) with significant pure piezospintronic effects. Interestingly, we reveal
that the ionic displacement contribution dominates the piezospintronic effect,
in contrast to the piezoelectric effect. Our study not only provides
first-principles approach for investigating spin dipole moment related
phenomena (e.g., ferrotoroidicity, fractional quantum spin dipole moment,
piezospintronics), but also provide promising piezospintronic materials for
experimental verification and industrial applications....

---

### 44. Establishing baselines for generative discovery of inorganic crystals

**Authors:** Nathan J. Szymanski, Christopher J. Bartel

**Published:** 2025-01-04

**Category:** cond-mat.mtrl-sci

**ID:** 2501.02144v2

**Link:** [http://arxiv.org/abs/2501.02144v2](http://arxiv.org/abs/2501.02144v2)

**Summary:** Generative artificial intelligence offers a promising avenue for materials
discovery, yet its advantages over traditional methods remain unclear. In this
work, we introduce and benchmark two baseline approaches - random enumeration
of charge-balanced prototypes and data-driven ion exchange of known compounds -
against four generative techniques based on diffusion models, variational
autoencoders, and large language models. Our results show that established
methods such as ion exchange are better at generating novel materials that are
stable, although many of these closely resemble known compounds. In contrast,
generative models excel at proposing novel structural frameworks and, when
sufficient training data is available, can more effectively target properties
such as electronic band gap and bulk modulus. To enhance the performance of
both the baseline and generative approaches, we implement a post-generation
screening step in which all proposed structures are passed through stability
and property filters from pre-trained machine learning models including
universal interatomic potentials. This low-cost filtering step leads to
substantial improvement in the success rates of all methods, remains
computationally efficient, and ultimately provides a practical pathway toward
more effective generative strategies for materials discovery. By establishing
baselines for comparison, this work highlights opportunities for continued
advancement of generative models, especially for the targeted generation of
novel materials that are thermodynamically stable....

---

### 45. Squeezing Quantum States in Three-Dimensional Twisted Crystals

**Authors:** Vo Tien Phong, Kason Kunkelmann, Christophe De Beule, Mohammed M. Al Ezzi, Robert-Jan Slager, Shaffique Adam, E. J. Mele

**Published:** 2024-09-25

**Category:** cond-mat.mes-hall

**ID:** 2409.16602v2

**Link:** [http://arxiv.org/abs/2409.16602v2](http://arxiv.org/abs/2409.16602v2)

**Summary:** A fundamental idea in wave mechanics is that propagation in a periodic medium
can be described by Bloch waves whose conserved crystal momenta define their
transformations when displaced by the set of discrete lattice translations. In
ordered materials where incommensurate spatial periods compete, this general
principle is rendered ineffective, often with dramatic consequences. Examples
are crystals with broken symmetries from charge or spin density waves,
quasiperiodic lattices that produce diffraction patterns with
crystallographically forbidden point symmetries, and stacks of two-dimensional
lattices with a relative rotation (twist) between layers. In special cases when
there is a small difference between the competing periods, a useful work-around
is a continuum description where a periodic long-wavelength field produces
Bragg scattering that coherently mixes short-wavelength carrier waves. In this
work, we advocate an alternative approach to study three-dimensional twisted
crystals that replaces their spectrally congested momentum-space Bloch band
structures with a representation using squeezed coherent states in a Fock space
of free-particle vortex states. This reorganization of the Hilbert space
highlights the crucial role of the Coriolis force in the equations of motion
that leads to unconventional phase space dynamics and edge state structure
generic to a family of complex crystals....

---

### 46. Quantum decoherence by magnetic fluctuations in a magnetic topological insulator

**Authors:** Ruben Saatjian, Simon Dovrén, Kohtaro Yamakawa, Ryan S. Russell, James G. Analytis, John W. Harter

**Published:** 2024-07-03

**Category:** cond-mat.mtrl-sci

**ID:** 2407.03459v2

**Link:** [http://arxiv.org/abs/2407.03459v2](http://arxiv.org/abs/2407.03459v2)

**Summary:** In magnetic topological insulators, spontaneous time-reversal symmetry
breaking by intrinsic magnetic order can gap the topological surface spectrum,
resulting in exotic properties like axion electrodynamics, the quantum
anomalous Hall effect, and other topological magnetoelectric responses.
Understanding the magnetic order and its coupling to topological states is
essential to harness these properties. Here, we leverage near-resonant magnetic
dipole optical second harmonic generation to probe magnetic fluctuations in the
candidate axion insulator EuSn$_2$(As,P)$_2$ across its antiferromagnetic phase
boundary. We observe a pronounced dimensional crossover in the quantum
decoherence induced by magnetic fluctuations, whereby two-dimensional in-plane
ferromagnetic correlations at high temperatures give way to three-dimensional
long-range order at the N\'eel temperature. We also observe the breaking of
rotational symmetry within the long-range-ordered antiferromagnetic state and
map out the resulting spatial domain structure. More generally, we demonstrate
the unique capabilities of nonlinear optical spectroscopy to study quantum
coherence and fluctuations in magnetic quantum materials....

---

### 47. A unified framework on the universal approximation of transformer-type architectures

**Authors:** Jingpu Cheng, Qianxiao Li, Ting Lin, Zuowei Shen

**Published:** 2025-06-30

**Category:** cs.LG

**ID:** 2506.23551v1

**Link:** [http://arxiv.org/abs/2506.23551v1](http://arxiv.org/abs/2506.23551v1)

**Summary:** We investigate the universal approximation property (UAP) of transformer-type
architectures, providing a unified theoretical framework that extends prior
results on residual networks to models incorporating attention mechanisms. Our
work identifies token distinguishability as a fundamental requirement for UAP
and introduces a general sufficient condition that applies to a broad class of
architectures. Leveraging an analyticity assumption on the attention layer, we
can significantly simplify the verification of this condition, providing a
non-constructive approach in establishing UAP for such architectures. We
demonstrate the applicability of our framework by proving UAP for transformers
with various attention mechanisms, including kernel-based and sparse attention
mechanisms. The corollaries of our results either generalize prior works or
establish UAP for architectures not previously covered. Furthermore, our
framework offers a principled foundation for designing novel transformer
architectures with inherent UAP guarantees, including those with specific
functional symmetries. We propose examples to illustrate these insights....

---

### 48. Equivariance Everywhere All At Once: A Recipe for Graph Foundation Models

**Authors:** Ben Finkelshtein, İsmail İlkan Ceylan, Michael Bronstein, Ron Levie

**Published:** 2025-06-17

**Category:** cs.LG

**ID:** 2506.14291v2

**Link:** [http://arxiv.org/abs/2506.14291v2](http://arxiv.org/abs/2506.14291v2)

**Summary:** Graph machine learning architectures are typically tailored to specific tasks
on specific datasets, which hinders their broader applicability. This has led
to a new quest in graph machine learning: how to build graph foundation models
capable of generalizing across arbitrary graphs and features? In this work, we
present a recipe for designing graph foundation models for node-level tasks
from first principles. The key ingredient underpinning our study is a
systematic investigation of the symmetries that a graph foundation model must
respect. In a nutshell, we argue that label permutation-equivariance alongside
feature permutation-invariance are necessary in addition to the common node
permutation-equivariance on each local neighborhood of the graph. To this end,
we first characterize the space of linear transformations that are equivariant
to permutations of nodes and labels, and invariant to permutations of features.
We then prove that the resulting network is a universal approximator on
multisets that respect the aforementioned symmetries. Our recipe uses such
layers on the multiset of features induced by the local neighborhood of the
graph to obtain a class of graph foundation models for node property
prediction. We validate our approach through extensive experiments on 29
real-world node classification datasets, demonstrating both strong zero-shot
empirical performance and consistent improvement as the number of training
graphs increases....

---

### 49. Scalable Non-Equivariant 3D Molecule Generation via Rotational Alignment

**Authors:** Yuhui Ding, Thomas Hofmann

**Published:** 2025-06-11

**Category:** cs.LG

**ID:** 2506.10186v2

**Link:** [http://arxiv.org/abs/2506.10186v2](http://arxiv.org/abs/2506.10186v2)

**Summary:** Equivariant diffusion models have achieved impressive performance in 3D
molecule generation. These models incorporate Euclidean symmetries of 3D
molecules by utilizing an SE(3)-equivariant denoising network. However,
specialized equivariant architectures limit the scalability and efficiency of
diffusion models. In this paper, we propose an approach that relaxes such
equivariance constraints. Specifically, our approach learns a sample-dependent
SO(3) transformation for each molecule to construct an aligned latent space. A
non-equivariant diffusion model is then trained over the aligned
representations. Experimental results demonstrate that our approach performs
significantly better than previously reported non-equivariant models. It yields
sample quality comparable to state-of-the-art equivariant diffusion models and
offers improved training and sampling efficiency. Our code is available at
https://github.com/skeletondyh/RADM...

---

### 50. Segment as You Wish -- Free-Form Language-Based Segmentation for Medical Images

**Authors:** Longchao Da, Rui Wang, Xiaojian Xu, Parminder Bhatia, Taha Kass-Hout, Hua Wei, Cao Xiao

**Published:** 2024-10-02

**Category:** eess.IV

**ID:** 2410.12831v2

**Link:** [http://arxiv.org/abs/2410.12831v2](http://arxiv.org/abs/2410.12831v2)

**Summary:** Medical imaging is crucial for diagnosing a patient's health condition, and
accurate segmentation of these images is essential for isolating regions of
interest to ensure precise diagnosis and treatment planning. Existing methods
primarily rely on bounding boxes or point-based prompts, while few have
explored text-related prompts, despite clinicians often describing their
observations and instructions in natural language. To address this gap, we
first propose a RAG-based free-form text prompt generator, that leverages the
domain corpus to generate diverse and realistic descriptions. Then, we
introduce FLanS, a novel medical image segmentation model that handles various
free-form text prompts, including professional anatomy-informed queries,
anatomy-agnostic position-driven queries, and anatomy-agnostic size-driven
queries. Additionally, our model also incorporates a symmetry-aware
canonicalization module to ensure consistent, accurate segmentations across
varying scan orientations and reduce confusion between the anatomical position
of an organ and its appearance in the scan. FLanS is trained on a large-scale
dataset of over 100k medical images from 7 public datasets. Comprehensive
experiments demonstrate the model's superior language understanding and
segmentation precision, along with a deep comprehension of the relationship
between them, outperforming SOTA baselines on both in-domain and out-of-domain
datasets....

---

### 51. Generalized Linear Mode Connectivity for Transformers

**Authors:** Alexander Theus, Alessandro Cabodi, Sotiris Anagnostidis, Antonio Orvieto, Sidak Pal Singh, Valentina Boeva

**Published:** 2025-06-28

**Category:** cs.LG

**ID:** 2506.22712v1

**Link:** [http://arxiv.org/abs/2506.22712v1](http://arxiv.org/abs/2506.22712v1)

**Summary:** Understanding the geometry of neural network loss landscapes is a central
question in deep learning, with implications for generalization and
optimization. A striking phenomenon is linear mode connectivity (LMC), where
independently trained models can be connected by low- or zero-loss paths,
despite appearing to lie in separate loss basins. However, this is often
obscured by symmetries in parameter space -- such as neuron permutations --
which make functionally equivalent models appear dissimilar. Prior work has
predominantly focused on neuron re-ordering through permutations, but such
approaches are limited in scope and fail to capture the richer symmetries
exhibited by modern architectures such as Transformers. In this work, we
introduce a unified framework that captures four symmetry classes:
permutations, semi-permutations, orthogonal transformations, and general
invertible maps -- broadening the set of valid reparameterizations and
subsuming many previous approaches as special cases. Crucially, this
generalization enables, for the first time, the discovery of low- and
zero-barrier linear interpolation paths between independently trained Vision
Transformers and GPT-2 models. These results reveal deeper structure in the
loss landscape and underscore the importance of symmetry-aware analysis for
understanding model space geometry....

---

### 52. deCIFer: Crystal Structure Prediction from Powder Diffraction Data using Autoregressive Language Models

**Authors:** Frederik Lizak Johansen, Ulrik Friis-Jensen, Erik Bjørnager Dam, Kirsten Marie Ørnsbjerg Jensen, Rocío Mercado, Raghavendra Selvan

**Published:** 2025-02-04

**Category:** cs.LG

**ID:** 2502.02189v3

**Link:** [http://arxiv.org/abs/2502.02189v3](http://arxiv.org/abs/2502.02189v3)

**Summary:** Novel materials drive progress across applications from energy storage to
electronics. Automated characterization of material structures with machine
learning methods offers a promising strategy for accelerating this key step in
material design. In this work, we introduce an autoregressive language model
that performs crystal structure prediction (CSP) from powder diffraction data.
The presented model, deCIFer, generates crystal structures in the widely used
Crystallographic Information File (CIF) format and can be conditioned on powder
X-ray diffraction (PXRD) data. Unlike earlier works that primarily rely on
high-level descriptors like composition, deCIFer is also able to use
diffraction data to perform CSP. We train deCIFer on nearly 2.3M crystal
structures and validate on diverse sets of PXRD patterns for characterizing
challenging inorganic crystal systems. Qualitative checks and quantitative
assessments using the residual weighted profile show that deCIFer produces
structures that more accurately match the target diffraction data. Notably,
deCIFer can achieve a 94% match rate on test data. deCIFer bridges experimental
diffraction data with computational CSP, lending itself as a powerful tool for
crystal structure characterization....

---

### 53. Mic-hackathon 2024: Hackathon on Machine Learning for Electron and Scanning Probe Microscopy

**Authors:** Utkarsh Pratiush, Austin Houston, Kamyar Barakati, Aditya Raghavan, Dasol Yoon, Harikrishnan KP, Zhaslan Baraissov, Desheng Ma, Samuel S. Welborn, Mikolaj Jakowski, Shawn-Patrick Barhorst, Alexander J. Pattison, Panayotis Manganaris, Sita Sirisha Madugula, Sai Venkata Gayathri Ayyagari, Vishal Kennedy, Ralph Bulanadi, Michelle Wang, Kieran J. Pang, Ian Addison-Smith, Willy Menacho, Horacio V. Guzman, Alexander Kiefer, Nicholas Furth, Nikola L. Kolev, Mikhail Petrov, Viktoriia Liu, Sergey Ilyev, Srikar Rairao, Tommaso Rodani, Ivan Pinto-Huguet, Xuli Chen, Josep Cruañes, Marta Torrens, Jovan Pomar, Fanzhi Su, Pawan Vedanti, Zhiheng Lyu, Xingzhi Wang, Lehan Yao, Amir Taqieddin, Forrest Laskowski, Xiangyu Yin, Yu-Tsun Shao, Benjamin Fein-Ashley, Yi Jiang, Vineet Kumar, Himanshu Mishra, Yogesh Paul, Adib Bazgir, Rama chandra Praneeth Madugula, Yuwen Zhang, Pravan Omprakash, Jian Huang, Eric Montufar-Morales, Vivek Chawla, Harshit Sethi, Jie Huang, Lauri Kurki, Grace Guinan, Addison Salvador, Arman Ter-Petrosyan, Madeline Van Winkle, Steven R. Spurgeon, Ganesh Narasimha, Zijie Wu, Richard Liu, Yongtao Liu, Boris Slautin, Andrew R Lupini, Rama Vasudevan, Gerd Duscher, Sergei V. Kalinin

**Published:** 2025-06-10

**Category:** cond-mat.mtrl-sci

**ID:** 2506.08423v2

**Link:** [http://arxiv.org/abs/2506.08423v2](http://arxiv.org/abs/2506.08423v2)

**Summary:** Microscopy is a primary source of information on materials structure and
functionality at nanometer and atomic scales. The data generated is often
well-structured, enriched with metadata and sample histories, though not always
consistent in detail or format. The adoption of Data Management Plans (DMPs) by
major funding agencies promotes preservation and access. However, deriving
insights remains difficult due to the lack of standardized code ecosystems,
benchmarks, and integration strategies. As a result, data usage is inefficient
and analysis time is extensive. In addition to post-acquisition analysis, new
APIs from major microscope manufacturers enable real-time, ML-based analytics
for automated decision-making and ML-agent-controlled microscope operation.
Yet, a gap remains between the ML and microscopy communities, limiting the
impact of these methods on physics, materials discovery, and optimization.
Hackathons help bridge this divide by fostering collaboration between ML
researchers and microscopy experts. They encourage the development of novel
solutions that apply ML to microscopy, while preparing a future workforce for
instrumentation, materials science, and applied ML. This hackathon produced
benchmark datasets and digital twins of microscopes to support community growth
and standardized workflows. All related code is available at GitHub:
https://github.com/KalininGroup/Mic-hackathon-2024-codes-publication/tree/1.0.0.1...

---

### 54. Exploring the Capabilities of the Frontier Large Language Models for Nuclear Energy Research

**Authors:** Ahmed Almeldein, Mohammed Alnaggar, Rick Archibald, Tom Beck, Arpan Biswas, Rike Bostelmann, Wes Brewer, Chris Bryan, Christopher Calle, Cihangir Celik, Rajni Chahal, Jong Youl Choi, Arindam Chowdhury, Mark Cianciosa, Franklin Curtis, Gregory Davidson, Sebastian De Pascuale, Lisa Fassino, Ana Gainaru, Yashika Ghai, Luke Gibson, Qian Gong, Christopher Greulich, Scott Greenwood, Cory Hauck, Ehab Hassan, Rinkle Juneja, Soyoung Kang, Scott Klasky, Atul Kumar, Vineet Kumar, Paul Laiu, Calvin Lear, Yan-Ru Lin, Jono McConnell, Furkan Oz, Rishi Pillai, Anant Raj, Pradeep Ramuhalli, Marie Romedenne, Samantha Sabatino, José Salcedo-Pérez, Nathan D. See, Arpan Sircar, Punam Thankur, Tim Younkin, Xiao-Ying Yu, Prashant Jain, Tom Evans, Prasanna Balaprakash

**Published:** 2025-06-10

**Category:** physics.comp-ph

**ID:** 2506.19863v2

**Link:** [http://arxiv.org/abs/2506.19863v2](http://arxiv.org/abs/2506.19863v2)

**Summary:** The AI for Nuclear Energy workshop at Oak Ridge National Laboratory evaluated
the potential of Large Language Models (LLMs) to accelerate fusion and fission
research. Fourteen interdisciplinary teams explored diverse nuclear science
challenges using ChatGPT, Gemini, Claude, and other AI models over a single
day. Applications ranged from developing foundation models for fusion reactor
control to automating Monte Carlo simulations, predicting material degradation,
and designing experimental programs for advanced reactors. Teams employed
structured workflows combining prompt engineering, deep research capabilities,
and iterative refinement to generate hypotheses, prototype code, and research
strategies. Key findings demonstrate that LLMs excel at early-stage
exploration, literature synthesis, and workflow design, successfully
identifying research gaps and generating plausible experimental frameworks.
However, significant limitations emerged, including difficulties with novel
materials designs, advanced code generation for modeling and simulation, and
domain-specific details requiring expert validation. The successful outcomes
resulted from expert-driven prompt engineering and treating AI as a
complementary tool rather than a replacement for physics-based methods. The
workshop validated AI's potential to accelerate nuclear energy research through
rapid iteration and cross-disciplinary synthesis while highlighting the need
for curated nuclear-specific datasets, workflow automation, and specialized
model development. These results provide a roadmap for integrating AI tools
into nuclear science workflows, potentially reducing development cycles for
safer, more efficient nuclear energy systems while maintaining rigorous
scientific standards....

---

### 55. On the Ability of Deep Networks to Learn Symmetries from Data: A Neural Kernel Theory

**Authors:** Andrea Perin, Stephane Deny

**Published:** 2024-12-16

**Category:** cs.LG

**ID:** 2412.11521v2

**Link:** [http://arxiv.org/abs/2412.11521v2](http://arxiv.org/abs/2412.11521v2)

**Summary:** Symmetries (transformations by group actions) are present in many datasets,
and leveraging them holds considerable promise for improving predictions in
machine learning. In this work, we aim to understand when and how deep networks
-- with standard architectures trained in a standard, supervised way -- learn
symmetries from data. Inspired by real-world scenarios, we study a
classification paradigm where data symmetries are only partially observed
during training: some classes include all transformations of a cyclic group,
while others -- only a subset. In the infinite-width limit, where kernel
analogies apply, we derive a neural kernel theory of symmetry learning. The
group-cyclic nature of the dataset allows us to analyze the Gram matrix of
neural kernels in the Fourier domain; here we find a simple characterization of
the generalization error as a function of class separation (signal) and
class-orbit density (noise). This characterization reveals that generalization
can only be successful when the local structure of the data prevails over its
non-local, symmetry-induced structure, in the kernel space defined by the
architecture. We extend our theoretical treatment to any finite group,
including non-abelian groups. Our framework also applies to equivariant
architectures (e.g., CNNs), and recovers their success in the special case
where the architecture matches the inherent symmetry of the data. Empirically,
our theory reproduces the generalization failure of finite-width networks (MLP,
CNN, ViT) trained on partially observed versions of rotated-MNIST. We conclude
that conventional deep networks lack a mechanism to learn symmetries that have
not been explicitly embedded in their architecture a priori. Our framework
could be extended to guide the design of architectures and training procedures
able to learn symmetries from data....

---

### 56. Efficient Band Structure Unfolding with Atomic-centered Orbitals: General Theory and Application

**Authors:** Jingkai Quan, Nikita Rybin, Matthias Scheffler, Christian Carbogno

**Published:** 2025-06-26

**Category:** cond-mat.mtrl-sci

**ID:** 2506.21089v1

**Link:** [http://arxiv.org/abs/2506.21089v1](http://arxiv.org/abs/2506.21089v1)

**Summary:** Band structure unfolding is a key technique for analyzing and simplifying the
electronic band structure of large, internally distorted supercells that break
the primitive cell's translational symmetry. In this work, we present an
efficient band unfolding method for atomic orbital (AO) basis sets that
explicitly accounts for both the non-orthogonality of atomic orbitals and their
atom-centered nature. Unlike existing approaches that typically rely on a
plane-wave representation of the (semi-)valence states, we here derive
analytical expressions that recasts the primitive cell translational operator
and the associated Bloch-functions in the supercell AO basis. In turn, this
enables the accurate and efficient unfolding of conduction, valence, and core
states in all-electron codes, as demonstrated by our implementation in the
all-electron ab initio simulation package FHI-aims, which employs numeric
atom-centered orbitals. We explicitly demonstrate the capability of running
large-scale unfolding calculations for systems with thousands of atoms and
showcase the importance of this technique for computing temperature-dependent
spectral functions in strongly anharmonic materials using CuI as example....

---

### 57. Antibody Design and Optimization with Multi-scale Equivariant Graph Diffusion Models for Accurate Complex Antigen Binding

**Authors:** Jiameng Chen, Xiantao Cai, Jia Wu, Wenbin Hu

**Published:** 2025-06-26

**Category:** cs.LG

**ID:** 2506.20957v1

**Link:** [http://arxiv.org/abs/2506.20957v1](http://arxiv.org/abs/2506.20957v1)

**Summary:** Antibody design remains a critical challenge in therapeutic and diagnostic
development, particularly for complex antigens with diverse binding interfaces.
Current computational methods face two main limitations: (1) capturing
geometric features while preserving symmetries, and (2) generalizing novel
antigen interfaces. Despite recent advancements, these methods often fail to
accurately capture molecular interactions and maintain structural integrity. To
address these challenges, we propose \textbf{AbMEGD}, an end-to-end framework
integrating \textbf{M}ulti-scale \textbf{E}quivariant \textbf{G}raph
\textbf{D}iffusion for antibody sequence and structure co-design. Leveraging
advanced geometric deep learning, AbMEGD combines atomic-level geometric
features with residue-level embeddings, capturing local atomic details and
global sequence-structure interactions. Its E(3)-equivariant diffusion method
ensures geometric precision, computational efficiency, and robust
generalizability for complex antigens. Furthermore, experiments using the
SAbDab database demonstrate a 10.13\% increase in amino acid recovery, 3.32\%
rise in improvement percentage, and a 0.062~\AA\ reduction in root mean square
deviation within the critical CDR-H3 region compared to DiffAb, a leading
antibody design model. These results highlight AbMEGD's ability to balance
structural integrity with improved functionality, establishing a new benchmark
for sequence-structure co-design and affinity optimization. The code is
available at: https://github.com/Patrick221215/AbMEGD....

---

### 58. Symmetry Classification of Magnetic Orders and Emergence of Spin-Orbit Magnetism

**Authors:** Yuntian Liu, Xiaobing Chen, Yutong Yu, Qihang Liu

**Published:** 2025-06-25

**Category:** cond-mat.mtrl-sci

**ID:** 2506.20739v1

**Link:** [http://arxiv.org/abs/2506.20739v1](http://arxiv.org/abs/2506.20739v1)

**Summary:** Magnetism, a fundamental concept predating condensed matter physics, has
achieved significant advancements in recent decades, driven by its potential
for next-generation storage devices. Meanwhile, the classification of magnetic
orders, even for the most fundamental concepts like ferromagnetism (FM) and
antiferromagnetism (AFM), has encountered unprecedented challenges since the
discovery of unconventional magnets and advancements in antiferromagnetic
spintronics. Here, we present a rigorous classification of magnetic order using
state-of-the-art spin space group (SSG) theory. Based on whether the net
magnetic moment is constrained to zero by SSG, magnetic order is unambiguously
dichotomized into FM (including ferrimagnetism) and AFM. Additionally, we
classify AFM geometries into four categories -- primary, bi-color, spiral, and
multi-axial -- based on periodic spin propagation beyond the symmetry
operations of magnetic space groups. We then introduce a distinct magnetic
phase, dubbed spin-orbit magnetism, characterized by its unique behavior
involving the spin-orbit coupling (SOC) order parameter and SOC-driven phase
transition. We further create an oriented SSG description, i.e., SSG with a
fixed magnetic configuration, apply the framework to 2,065 experimentally
validated magnetic materials in MAGNDATA database, and identify over 220
spin-orbit magnets with distinct spin and orbital magnetization mechanisms.
Implemented by the online program FINDSPINGROUP, our work establishes a
universal symmetry standard for magnetic order classification, offering new
understandings of unconventional magnets and broad applicability in spintronics
and quantum material design....

---

### 59. WyckoffDiff -- A Generative Diffusion Model for Crystal Symmetry

**Authors:** Filip Ekström Kelvinius, Oskar B. Andersson, Abhijith S. Parackal, Dong Qian, Rickard Armiento, Fredrik Lindsten

**Published:** 2025-02-10

**Category:** cond-mat.mtrl-sci

**ID:** 2502.06485v3

**Link:** [http://arxiv.org/abs/2502.06485v3](http://arxiv.org/abs/2502.06485v3)

**Summary:** Crystalline materials often exhibit a high level of symmetry. However, most
generative models do not account for symmetry, but rather model each atom
without any constraints on its position or element. We propose a generative
model, Wyckoff Diffusion (WyckoffDiff), which generates symmetry-based
descriptions of crystals. This is enabled by considering a crystal structure
representation that encodes all symmetry, and we design a novel neural network
architecture which enables using this representation inside a discrete
generative model framework. In addition to respecting symmetry by construction,
the discrete nature of our model enables fast generation. We additionally
present a new metric, Fr\'echet Wrenformer Distance, which captures the
symmetry aspects of the materials generated, and we benchmark WyckoffDiff
against recently proposed generative models for crystal generation. As a
proof-of-concept study, we use WyckoffDiff to find new materials below the
convex hull of thermodynamical stability....

---

### 60. Staggered nonlinear spin generations in centrosymmetric altermagnets under electric current

**Authors:** Jie Zhang, Ruijing Fang, Zhichao Zhou, Xiao Li

**Published:** 2025-06-25

**Category:** cond-mat.mes-hall

**ID:** 2506.20298v1

**Link:** [http://arxiv.org/abs/2506.20298v1](http://arxiv.org/abs/2506.20298v1)

**Summary:** Current-induced spin generations are of significant importance for
electrically controllable magnetization. Due to symmetry constraints, linear
spin generation is absent in centrosymmetric magnets and nonlinear
contributions become crucial. However, nonlinear spin generations have few
examples in centrosymmetric compensated magnets with opposite-spin sublattices,
which hinders electric control of associated magnetization. Here, we study
nonlinear spin generations in altermagnets with opposite-spin sublattices. In a
square altermagnetic model, both staggered and uniform nonlinear spin
generations appear at opposite-spin sublattices. They vary as the magnetization
direction rotates, with emerging out-of-plane components that can be utilized
in perpendicular magnetization switching of high-density storage devices. By
first-principles calculations, out-of-plane, staggered nonlinear spin
generations are found to be considerable in a typical altermagnet,
Fe$_2$Se$_2$O monolayer. Our findings provide opportunities for electrically
manipulating magnetization and designing energy-efficient magnetic devices
based on compensated magnets....

---

### 61. Standard model of electromagnetism and chirality in crystals

**Authors:** R. Winkler, U. Zülicke

**Published:** 2024-05-31

**Category:** cond-mat.mtrl-sci

**ID:** 2405.20940v2

**Link:** [http://arxiv.org/abs/2405.20940v2](http://arxiv.org/abs/2405.20940v2)

**Summary:** We present a general, systematic theory of electromagnetism and chirality in
crystalline solids. Symmetry is its basic guiding principle, enabling us to
consider macroscopic multipole densities without reference to any specific
microscopic configurations. We use a formal analogy between space inversion $i$
and time inversion $\theta$ to identify two complementary, comprehensive
classifications of crystals, based on five categories of electric and magnetic
multipole order--called polarizations--and five categories of chirality. The
five categories of polarizations (parapolar, electropolar, magnetopolar,
antimagnetopolar, and multipolar) embody the ways in which electromagnetic
multipole order can be realized in solids, thus expanding the familiar notion
of electric dipolarization in ferroelectrics and magnetization in ferromagnets
to higher-order multipole densities. The five categories of chirality
(parachiral, electrochiral, magnetochiral, antimagnetochiral, and multichiral)
extend the notion of enantiomorphism--conventionally associated with the lack
of spatial mirror symmetries--to include all possibilities for creating
non-superposable images by applying the inversions $i$, $\theta$, and
$i\theta$. In particular, multichiral systems lack all inversion symmetries and
thus have four different enantiomorphs. Each category of chirality arises from
particular superpositions of electric and magnetic multipole densities.
Jointly, the categories of polarizations and chirality yield a classification
of all 122 magnetic point groups into 12 types that exhibit distinct physical
properties and are identifiable by characteristic features in the electronic
band structure that we elucidate in detail. The classification makes the formal
equivalence of $i$, $\theta$, and $i\theta$ explicit and reveals striking
correspondences between apparently dissimilar systems and their physical
properties....

---

### 62. Massive Atomic Diversity: a compact universal dataset for atomistic machine learning

**Authors:** Arslan Mazitov, Sofiia Chorna, Guillaume Fraux, Marnik Bercx, Giovanni Pizzi, Sandip De, Michele Ceriotti

**Published:** 2025-06-24

**Category:** cond-mat.mtrl-sci

**ID:** 2506.19674v1

**Link:** [http://arxiv.org/abs/2506.19674v1](http://arxiv.org/abs/2506.19674v1)

**Summary:** The development of machine-learning models for atomic-scale simulations has
benefited tremendously from the large databases of materials and molecular
properties computed in the past two decades using electronic-structure
calculations. More recently, these databases have made it possible to train
universal models that aim at making accurate predictions for arbitrary atomic
geometries and compositions. The construction of many of these databases was
however in itself aimed at materials discovery, and therefore targeted
primarily to sample stable, or at least plausible, structures and to make the
most accurate predictions for each compound - e.g. adjusting the calculation
details to the material at hand. Here we introduce a dataset designed
specifically to train machine learning models that can provide reasonable
predictions for arbitrary structures, and that therefore follows a different
philosophy. Starting from relatively small sets of stable structures, the
dataset is built to contain massive atomic diversity (MAD) by aggressively
distorting these configurations, with near-complete disregard for the stability
of the resulting configurations. The electronic structure details, on the other
hand, are chosen to maximize consistency rather than to obtain the most
accurate prediction for a given structure, or to minimize computational effort.
The MAD dataset we present here, despite containing fewer than 100k structures,
has already been shown to enable training universal interatomic potentials that
are competitive with models trained on traditional datasets with two to three
orders of magnitude more structures. We describe in detail the philosophy and
details of the construction of the MAD dataset. We also introduce a
low-dimensional structural latent space that allows us to compare it with other
popular datasets and that can be used as a general-purpose materials
cartography tool....

---

### 63. Discovering Symmetries of ODEs by Symbolic Regression

**Authors:** Paul Kahlmeyer, Niklas Merk, Joachim Giesen

**Published:** 2025-06-24

**Category:** cs.LG

**ID:** 2506.19550v1

**Link:** [http://arxiv.org/abs/2506.19550v1](http://arxiv.org/abs/2506.19550v1)

**Summary:** Solving systems of ordinary differential equations (ODEs) is essential when
it comes to understanding the behavior of dynamical systems. Yet, automated
solving remains challenging, in particular for nonlinear systems. Computer
algebra systems (CASs) provide support for solving ODEs by first simplifying
them, in particular through the use of Lie point symmetries. Finding these
symmetries is, however, itself a difficult problem for CASs. Recent works in
symbolic regression have shown promising results for recovering symbolic
expressions from data. Here, we adapt search-based symbolic regression to the
task of finding generators of Lie point symmetries. With this approach, we can
find symmetries of ODEs that existing CASs cannot find....

---

### 64. Machine Learning-Driven Insights into Excitonic Effects in 2D Materials

**Authors:** Ahsan Javed, Sajid Ali

**Published:** 2025-01-02

**Category:** cond-mat.mtrl-sci

**ID:** 2501.01092v2

**Link:** [http://arxiv.org/abs/2501.01092v2](http://arxiv.org/abs/2501.01092v2)

**Summary:** Understanding excitonic effects in two-dimensional (2D) materials is critical
for advancing their potential in next-generation electronic and photonic
devices. In this study, we introduce a machine learning (ML)-based framework to
predict exciton binding energies in 2D materials, offering a computationally
efficient alternative to traditional methods such as many-body perturbation
theory (GW) and the Bethe-Salpeter equation. Leveraging data from the
Computational 2D Materials Database (C2DB), our ML models establish connections
between cheaply available material descriptors and complex excitonic
properties, significantly accelerating the screening process for materials with
pronounced excitonic effects. Additionally, Bayesian optimization with Gaussian
process regression was employed to efficiently filter materials with largest
exciton binding energies, further enhancing the discovery process. Although
developed for 2D systems, this approach is versatile and can be extended to
three-dimensional materials, broadening its applicability in materials
discovery....

---

### 65. Exchange-correlation torques from gauge symmetries

**Authors:** Jacques K. Desmarais, Kamel Bencheikh, Giovanni Vignale, Stefano Pittalis

**Published:** 2025-06-24

**Category:** cond-mat.mtrl-sci

**ID:** 2506.19458v1

**Link:** [http://arxiv.org/abs/2506.19458v1](http://arxiv.org/abs/2506.19458v1)

**Summary:** The problem of predicting accurate exchange-correlation (xc) spin-torques in
non-collinear magnetic systems has dominated the scene of spin-density
functional theory (SDFT) in the last two decades. Progress has been hindered by
the fact that the spin torque is directly connected to the divergence of the
spin current, a quantity that is extraneous to SDFT. Furthermore, SDFT does not
apply in the presence of vector potentials and spin-orbit couplings. Here, we
propose a solution that exploits the physical implications of the U(1)xSU(2)
gauge invariance of the xc energy in SpinCurrent-DFT. We derive explicit xc
torque expressions based on meta-generalized-gradient approximations in the
framework of the generalized Kohn-Sham (GKS) formulation. One key term
represents an xc-torque involving the GKS spin-kinetic energy density; and
another term resembles the phenomenological spin current of the Landau-Lifshitz
equations: both are derived from first-principles. We also show that the
functional form ensures that the GKS particle- and spin-currents are identical,
in form, to their interacting counterparts. Non-collinear equilibrium
conditions and adiabatic dynamics are thus derived that resolve longstanding
issues....

---

### 66. Efficient Crystal Structure Prediction Using Genetic Algorithm and Universal Neural Network Potential

**Authors:** Takuya Shibayama, Hideaki Imamura, Katsuhiko Nishimra, Kohei Shinohara, Chikashi Shinagawa, So Takamoto, Ju Li

**Published:** 2025-03-27

**Category:** cond-mat.mtrl-sci

**ID:** 2503.21201v2

**Link:** [http://arxiv.org/abs/2503.21201v2](http://arxiv.org/abs/2503.21201v2)

**Summary:** Crystal structure prediction (CSP) is crucial for identifying stable crystal
structures in given systems and is a prerequisite for computational atomistic
simulations. Recent advances in neural network potentials (NNPs) have reduced
the computational cost of CSP. However, searching for stable crystal structures
across the entire composition space in multicomponent systems remains a
significant challenge. Here, we propose a novel genetic algorithm (GA) -based
CSP method using a universal NNP. Our GA-based methods are designed to
efficiently expand convex hull volumes while preserving the diversity of
crystal structures. This approach draws inspiration from the similarity between
convex hull updates and Pareto front evolution in multi-objective optimization.
Our evaluation shows that the present method outperforms the symmetry-aware
random structure generation, achieving a larger convex hull with fewer trials.
We demonstrated that our approach, combined with the developed universal NNP
(PFP), can accurately reproduce and explore phase diagrams obtained through DFT
calculations; this indicates the validity of PFP across a wide range of crystal
structures and element combinations. This study, which integrates a universal
NNP with a GA-based CSP method, highlights the promise of these methods in
materials discovery....

---

### 67. TrajTok: Technical Report for 2025 Waymo Open Sim Agents Challenge

**Authors:** Zhiyuan Zhang, Xiaosong Jia, Guanyu Chen, Qifeng Li, Junchi Yan

**Published:** 2025-06-23

**Category:** cs.CL

**ID:** 2506.21618v1

**Link:** [http://arxiv.org/abs/2506.21618v1](http://arxiv.org/abs/2506.21618v1)

**Summary:** In this technical report, we introduce TrajTok, a trajectory tokenizer for
discrete next-token-prediction based behavior generation models, which combines
data-driven and rule-based methods with better coverage, symmetry and
robustness, along with a spatial-aware label smoothing method for cross-entropy
loss. We adopt the tokenizer and loss for the SMART model and reach a superior
performance with realism score of 0.7852 on the Waymo Open Sim Agents Challenge
2025. We will open-source the code in the future....

---

### 68. First-principles prediction of altermagnetism in transition metal graphite intercalation compounds

**Authors:** Weida Fu, Guo-Dong Zhao, Tao Hu, Wencai Yi, Hui Zhang, Alessandro Stroppa, Wei Ren, Zhongming Ren

**Published:** 2025-06-23

**Category:** cond-mat.mtrl-sci

**ID:** 2506.18353v1

**Link:** [http://arxiv.org/abs/2506.18353v1](http://arxiv.org/abs/2506.18353v1)

**Summary:** We report the emergence of altermagnetism, a magnetic phase characterized by
the coexistence of compensated spin ordering and momentum-dependent spin
splitting, in graphite intercalation compounds (GICs), a prototypical material
system long investigated for its tunable electronic and structural properties.
Through first-principles calculations, we demonstrate that
vanadium-intercalated stage-1 graphite compounds, exhibit inherent
altermagnetic properties. The hexagonal crystal system and antiferromagnetic
ordering of V atoms generate a magnetic space group that enforces alternating
spin polarization in momentum space while maintaining zero net magnetization.
The calculated band structure reveals robust altermagnetic signatures: along
the high-symmetry direction, we observe a pronounced spin splitting of ~270 meV
with alternating spin polarization. Crucially, the spin splitting exhibits
minimal sensitivity to spin-orbit coupling (SOC) effect, highlighting the
dominance of exchange interactions over relativistic effects. From Monte Carlo
simulations, we predict a magnetic transition temperature ($T_m$ ) of ~228 K,
indicating stable magnetic ordering above liquid nitrogen temperatures. The
combination of symmetry-protected spin textures, SOC-independent splitting, and
elevated $T_m$ temperature makes V-GICs as a promising candidate for spintronic
applications, particularly for zero-field spin-polarized current generation and
topologically robust spin transport. As the first demonstration of carbon-based
alternating magnetic systems, this work offers a design paradigm for
engineering spin-polarized quantum states governed by crystalline symmetry
constraints....

---

### 69. Controlled Generation with Equivariant Variational Flow Matching

**Authors:** Floor Eijkelboom, Heiko Zimmermann, Sharvaree Vadgama, Erik J Bekkers, Max Welling, Christian A. Naesseth, Jan-Willem van de Meent

**Published:** 2025-06-23

**Category:** cs.LG

**ID:** 2506.18340v1

**Link:** [http://arxiv.org/abs/2506.18340v1](http://arxiv.org/abs/2506.18340v1)

**Summary:** We derive a controlled generation objective within the framework of
Variational Flow Matching (VFM), which casts flow matching as a variational
inference problem. We demonstrate that controlled generation can be implemented
two ways: (1) by way of end-to-end training of conditional generative models,
or (2) as a Bayesian inference problem, enabling post hoc control of
unconditional models without retraining. Furthermore, we establish the
conditions required for equivariant generation and provide an equivariant
formulation of VFM tailored for molecular generation, ensuring invariance to
rotations, translations, and permutations. We evaluate our approach on both
uncontrolled and controlled molecular generation, achieving state-of-the-art
performance on uncontrolled generation and outperforming state-of-the-art
models in controlled generation, both with end-to-end training and in the
Bayesian inference setting. This work strengthens the connection between
flow-based generative modeling and Bayesian inference, offering a scalable and
principled framework for constraint-driven and symmetry-aware generation....

---

### 70. Doping-induced Polyamorphic Transitions in Fluorite Oxides

**Authors:** Hao Yang, Qiaotong Luan, Qing Zhang, Yuhao Yue, Yawen Xu, Xiaohui Liu, Zheng Wen, Zhaoru Sun

**Published:** 2025-06-23

**Category:** cond-mat.mtrl-sci

**ID:** 2506.18333v1

**Link:** [http://arxiv.org/abs/2506.18333v1](http://arxiv.org/abs/2506.18333v1)

**Summary:** Fluorite oxides such as HfO$_2$ exhibit rich and tunable phase behavior,
making them promising candidates for next generation electronic devices. A key
challenge is to design amorphous HfO$_2$-based high-$k$ materials with both
structural and performance stability. Here, using molecular dynamics
simulations supported by experimental measurements, we reveal that Ba doping
stimulates a polyamorphic transition in HfO$_2$, yielding a semi-ordered
amorphous (SA) phase characterized by disordered oxygens embedded within an
ordered metal sublattice. We find that this phase arises from degenerate
short-range symmetry breaking modes, consistent with Pauling's parsimony rule.
Notably, the SA structure is thermodynamically stable and displays a wider
bandgap and higher dielectric constant than conventional random-packing
amorphous structure, owing to suppressed subgap states and increased Born
effective charges. We further demonstrate that this structural motif
generalizes to Ba-, Sr-, and Ca-doped HfO$_2$ and ZrO$_2$, establishing a
broadly applicable strategy for designing high-performance amorphous
dielectrics....

---

### 71. Theory of Photocurrent and High-Harmonic Generation with Chiral Fermions

**Authors:** Yuya Ominato, Masahito Mochizuki

**Published:** 2025-03-04

**Category:** cond-mat.mtrl-sci

**ID:** 2503.02469v2

**Link:** [http://arxiv.org/abs/2503.02469v2](http://arxiv.org/abs/2503.02469v2)

**Summary:** We theoretically discover possible dc-current induction and high-harmonic
generation from photodriven chiral fermions in B20-type semimetals irradiated
with circularly polarized light as nonlinear optical responses with several
unconventional properties. First, we find multiple sign changes of the induced
bulk dc photocurrent as a function of light parameters, which is ascribed to
the nature of asymmetric photon-dressed bands in chiral systems. Moreover, we
observe a parity-dependent directivity of high-harmonic generation where the
odd- and even-order harmonics have intensities only in directions perpendicular
and parallel to the polarization plane, respectively, which can be understood
from dynamical symmetry of the present photodriven chiral systems....

---

### 72. Single crystalline orthorhombic GdAlGe as a rare earth magnetic Dirac nodal-line metal

**Authors:** Antu Laha, Juntao Yao, Asish K. Kundu, Niraj Aryal, Anil Rajapitamahuni, Elio Vescovo, Fernando Camino, Kim Kisslinger, Lihua Zhang, Dmytro Nykypanchuk, J. Sears, J. M. Tranquada, Weiguo Yin, Qiang Li

**Published:** 2025-06-20

**Category:** cond-mat.mtrl-sci

**ID:** 2506.17502v1

**Link:** [http://arxiv.org/abs/2506.17502v1](http://arxiv.org/abs/2506.17502v1)

**Summary:** Crystal engineering is a method for discovering new quantum materials and
phases, which may be achieved by external pressure or strain. Chemical pressure
is unique in that it generates internal pressure perpetually to the lattice. As
an example, GdAlSi from the rare-earth ($R$) $R$Al$X$ ($X =$ Si or Ge) family
of Weyl semimetals is considered. Replacing Si with the larger isovalent
element Ge creates sufficiently large chemical pressure to induce a structural
transition from the tetragonal structure of GdAlSi, compatible with a Weyl
semimetallic state, to an orthorhombic phase in GdAlGe, resulting in an
inversion-symmetry-protected nodal-line metal. We find that GdAlGe hosts an
antiferromagnetic ground state with two successive orderings, at
$T_\mathrm{N1}$ = 35 K and $T_\mathrm{N2}$ = 30 K. In-plane isothermal
magnetization shows a magnetic field induced metamagnetic transition at 6.2 T
for 2 K. Furthermore, electron-hole compensation gives rise to a large
magnetoresistance of $\sim 100\%$ at 2 K and 14 T. Angle-resolved photoemission
spectroscopy measurements and density functional theory calculations reveal a
Dirac-like linear band dispersion over an exceptionally large energy range of
$\sim$ 1.5 eV with a high Fermi velocity of $\sim 10^6$ m/s, a rare feature not
observed in any magnetic topological materials....

---

### 73. Quantum Geometric Origin of the Intrinsic Nonlinear Hall Effect

**Authors:** Yannis Ulrich, Johannes Mitscherling, Laura Classen, Andreas P. Schnyder

**Published:** 2025-06-20

**Category:** cond-mat.mes-hall

**ID:** 2506.17386v1

**Link:** [http://arxiv.org/abs/2506.17386v1](http://arxiv.org/abs/2506.17386v1)

**Summary:** We analyze the quantum geometric contribution to the intrinsic second-order
nonlinear Hall effect (NLHE) for a general multiband Hamiltonian. The nonlinear
conductivity, obtained in Green's function formalism, is decomposed into its
quantum geometric constituents using a projector-based approach. In addition to
the previously identified Berry curvature and interband quantum metric dipoles,
we obtain a third term of quantum geometric origin, given by the momentum
derivative of the $intraband$ quantum metric. This contribution, which we term
the intraband quantum metric dipole, provides substantial corrections to the
NLHE in topological magnets and becomes the dominant geometric term in
topological antiferromagnets with gapped Dirac cones. Considering generalized
2D and 3D Weyl/Dirac Hamiltonians, describing a large class of topological band
crossings with sizable quantum geometry, we derive analytical expressions of
the NLHE, thereby revealing the individual contributions of the three quantum
geometric terms. Combined with an exhaustive symmetry classification of all
magnetic space groups, this analysis leads to the identification of several
candidate materials expected to exhibit large intrinsic NLHE, including the
antiferromagnets $\text{Yb}_3\text{Pt}_4$, $\text{CuMnAs}$, and
$\text{CoNb}_3\text{S}_6$, as well as the nodal-plane material
$\text{MnNb}_3\text{S}_6$. Finally, our projector-based approach yields a
compact expression for the NLHE in terms of momentum derivatives of the Bloch
Hamiltonian matrix alone, enabling efficient numerical evaluation of each
contribution in the aforementioned materials....

---

### 74. Nature Language Model: Deciphering the Language of Nature for Scientific Discovery

**Authors:** Yingce Xia, Peiran Jin, Shufang Xie, Liang He, Chuan Cao, Renqian Luo, Guoqing Liu, Yue Wang, Zequn Liu, Yuan-Jyue Chen, Zekun Guo, Yeqi Bai, Pan Deng, Yaosen Min, Ziheng Lu, Hongxia Hao, Han Yang, Jielan Li, Chang Liu, Jia Zhang, Jianwei Zhu, Ran Bi, Kehan Wu, Wei Zhang, Kaiyuan Gao, Qizhi Pei, Qian Wang, Xixian Liu, Yanting Li, Houtian Zhu, Yeqing Lu, Mingqian Ma, Zun Wang, Tian Xie, Krzysztof Maziarz, Marwin Segler, Zhao Yang, Zilong Chen, Yu Shi, Shuxin Zheng, Lijun Wu, Chen Hu, Peggy Dai, Tie-Yan Liu, Haiguang Liu, Tao Qin

**Published:** 2025-02-11

**Category:** cs.AI

**ID:** 2502.07527v3

**Link:** [http://arxiv.org/abs/2502.07527v3](http://arxiv.org/abs/2502.07527v3)

**Summary:** Foundation models have revolutionized natural language processing and
artificial intelligence, significantly enhancing how machines comprehend and
generate human languages. Inspired by the success of these foundation models,
researchers have developed foundation models for individual scientific domains,
including small molecules, materials, proteins, DNA, RNA and even cells.
However, these models are typically trained in isolation, lacking the ability
to integrate across different scientific domains. Recognizing that entities
within these domains can all be represented as sequences, which together form
the "language of nature", we introduce Nature Language Model (NatureLM), a
sequence-based science foundation model designed for scientific discovery.
Pre-trained with data from multiple scientific domains, NatureLM offers a
unified, versatile model that enables various applications including: (i)
generating and optimizing small molecules, proteins, RNA, and materials using
text instructions; (ii) cross-domain generation/design, such as
protein-to-molecule and protein-to-RNA generation; and (iii) top performance
across different domains, matching or surpassing state-of-the-art specialist
models. NatureLM offers a promising generalist approach for various scientific
tasks, including drug discovery (hit generation/optimization, ADMET
optimization, synthesis), novel material design, and the development of
therapeutic proteins or nucleotides. We have developed NatureLM models in
different sizes (1 billion, 8 billion, and 46.7 billion parameters) and
observed a clear improvement in performance as the model size increases....

---

### 75. Sampling 3D Molecular Conformers with Diffusion Transformers

**Authors:** J. Thorben Frank, Winfried Ripken, Gregor Lied, Klaus-Robert Müller, Oliver T. Unke, Stefan Chmiela

**Published:** 2025-06-18

**Category:** cs.LG

**ID:** 2506.15378v1

**Link:** [http://arxiv.org/abs/2506.15378v1](http://arxiv.org/abs/2506.15378v1)

**Summary:** Diffusion Transformers (DiTs) have demonstrated strong performance in
generative modeling, particularly in image synthesis, making them a compelling
choice for molecular conformer generation. However, applying DiTs to molecules
introduces novel challenges, such as integrating discrete molecular graph
information with continuous 3D geometry, handling Euclidean symmetries, and
designing conditioning mechanisms that generalize across molecules of varying
sizes and structures. We propose DiTMC, a framework that adapts DiTs to address
these challenges through a modular architecture that separates the processing
of 3D coordinates from conditioning on atomic connectivity. To this end, we
introduce two complementary graph-based conditioning strategies that integrate
seamlessly with the DiT architecture. These are combined with different
attention mechanisms, including both standard non-equivariant and
SO(3)-equivariant formulations, enabling flexible control over the trade-off
between between accuracy and computational efficiency. Experiments on standard
conformer generation benchmarks (GEOM-QM9, -DRUGS, -XL) demonstrate that DiTMC
achieves state-of-the-art precision and physical validity. Our results
highlight how architectural choices and symmetry priors affect sample quality
and efficiency, suggesting promising directions for large-scale generative
modeling of molecular structures. Code available at
https://github.com/ML4MolSim/dit_mc....

---

### 76. Rao-Blackwell Gradient Estimators for Equivariant Denoising Diffusion

**Authors:** Vinh Tong, Trung-Dung Hoang, Anji Liu, Guy Van den Broeck, Mathias Niepert

**Published:** 2025-02-14

**Category:** cs.LG

**ID:** 2502.09890v3

**Link:** [http://arxiv.org/abs/2502.09890v3](http://arxiv.org/abs/2502.09890v3)

**Summary:** In domains such as molecular and protein generation, physical systems exhibit
inherent symmetries that are critical to model. Two main strategies have
emerged for learning invariant distributions: designing equivariant network
architectures and using data augmentation to approximate equivariance. While
equivariant architectures preserve symmetry by design, they often involve
greater complexity and pose optimization challenges. Data augmentation, on the
other hand, offers flexibility but may fall short in fully capturing
symmetries. Our framework enhances both approaches by reducing training
variance and providing a provably lower-variance gradient estimator. We achieve
this by interpreting data augmentation as a Monte Carlo estimator of the
training gradient and applying Rao-Blackwellization. This leads to more stable
optimization, faster convergence, and reduced variance, all while requiring
only a single forward and backward pass per sample. We also present a practical
implementation of this estimator incorporating the loss and sampling procedure
through a method we call Orbit Diffusion. Theoretically, we guarantee that our
loss admits equivariant minimizers. Empirically, Orbit Diffusion achieves
state-of-the-art results on GEOM-QM9 for molecular conformation generation,
improves crystal structure prediction, and advances text-guided crystal
generation on the Perov-5 and MP-20 benchmarks. Additionally, it enhances
protein designability in protein structure generation....

---

### 77. Photomagnetic-Chiral Anisotropy mediated by Chirality-Driven Asymmetric Spin Splitting

**Authors:** Tianwei Ouyang, Hang Su, Wanning Zhang, Yingying Duan, Yuxi Fang, Shunai Che, Yizhou Liu

**Published:** 2025-06-16

**Category:** cond-mat.mtrl-sci

**ID:** 2506.13696v1

**Link:** [http://arxiv.org/abs/2506.13696v1](http://arxiv.org/abs/2506.13696v1)

**Summary:** Photo-magnetic effects (PMEs), intrinsic to transition metals, arises from
the interaction between light-induced angu-lar momentum and electronic spin.
These effects are suppressed in noble metals with high symmetry and electron
density. Introducing chiral structures can induce photomagnetic-chiral
anisotropy (PM-ChA) of metals by linking chirality and spin dynamics. However,
a theoretical explain remains elusive. Here, we investigated the mechanism of
PM-ChA in tetrahelix-stacked chiral nanostructured gold chains (CNACs) using
first-principles calculations. Non-equilibrium Green's function calculations
reveal that chiral potentials enhance spin channel asymmetry by amplify-ing
spin-orbit coupling (SOC)-induced spin splitting. Real-time time-dependent
density functional theory simulations further identify SOC as the bridge
connecting chiral spintronics to PME, where chirality-driven spin flips from
asymmetric geometries generate opposing photomagnetic fields in materials of
different handedness. These findings are consistent with experimental
observations in chiral nanostructured gold films and provide a theoretical
instruction for design metallic spintronic devices....

---

### 78. Geometric Kolmogorov-Arnold Superposition Theorem

**Authors:** Francesco Alesiani, Takashi Maruyama, Henrik Christiansen, Viktor Zaverkin

**Published:** 2025-02-23

**Category:** cs.LG

**ID:** 2502.16664v2

**Link:** [http://arxiv.org/abs/2502.16664v2](http://arxiv.org/abs/2502.16664v2)

**Summary:** The Kolmogorov-Arnold Theorem (KAT), or more generally, the Kolmogorov
Superposition Theorem (KST), establishes that any non-linear multivariate
function can be exactly represented as a finite superposition of non-linear
univariate functions. Unlike the universal approximation theorem, which
provides only an approximate representation without guaranteeing a fixed
network size, KST offers a theoretically exact decomposition. The
Kolmogorov-Arnold Network (KAN) was introduced as a trainable model to
implement KAT, and recent advancements have adapted KAN using concepts from
modern neural networks. However, KAN struggles to effectively model physical
systems that require inherent equivariance or invariance geometric symmetries
as $E(3)$ transformations, a key property for many scientific and engineering
applications. In this work, we propose a novel extension of KAT and KAN to
incorporate equivariance and invariance over various group actions, including
$O(n)$, $O(1,n)$, $S_n$, and general $GL$, enabling accurate and efficient
modeling of these systems. Our approach provides a unified approach that
bridges the gap between mathematical theory and practical architectures for
physical systems, expanding the applicability of KAN to a broader class of
problems. We provide experimental validation on molecular dynamical systems and
particle physics....

---

### 79. On the Completeness of Invariant Geometric Deep Learning Models

**Authors:** Zian Li, Xiyuan Wang, Shijia Kang, Muhan Zhang

**Published:** 2024-02-07

**Category:** cs.LG

**ID:** 2402.04836v4

**Link:** [http://arxiv.org/abs/2402.04836v4](http://arxiv.org/abs/2402.04836v4)

**Summary:** Invariant models, one important class of geometric deep learning models, are
capable of generating meaningful geometric representations by leveraging
informative geometric features in point clouds. These models are characterized
by their simplicity, good experimental results and computational efficiency.
However, their theoretical expressive power still remains unclear, restricting
a deeper understanding of the potential of such models. In this work, we
concentrate on characterizing the theoretical expressiveness of a wide range of
invariant models under fully-connected conditions. We first rigorously
characterize the expressiveness of the most classic invariant model,
message-passing neural networks incorporating distance (DisGNN), restricting
its unidentifiable cases to be only highly symmetric point clouds. We then
prove that GeoNGNN, the geometric counterpart of one of the simplest subgraph
graph neural networks, can effectively break these corner cases' symmetry and
thus achieve E(3)-completeness. By leveraging GeoNGNN as a theoretical tool, we
further prove that: 1) most subgraph GNNs developed in traditional graph
learning can be seamlessly extended to geometric scenarios with
E(3)-completeness; 2) DimeNet, GemNet and SphereNet, three well-established
invariant models, are also all capable of achieving E(3)-completeness. Our
theoretical results fill the gap in the expressive power of invariant models,
contributing to a rigorous and comprehensive understanding of their
capabilities....

---

### 80. Stress-Testing Multimodal Foundation Models for Crystallographic Reasoning

**Authors:** Can Polat, Hasan Kurban, Erchin Serpedin, Mustafa Kurban

**Published:** 2025-06-16

**Category:** cs.CV

**ID:** 2506.13051v1

**Link:** [http://arxiv.org/abs/2506.13051v1](http://arxiv.org/abs/2506.13051v1)

**Summary:** Evaluating foundation models for crystallographic reasoning requires
benchmarks that isolate generalization behavior while enforcing physical
constraints. This work introduces a multiscale multicrystal dataset with two
physically grounded evaluation protocols to stress-test multimodal generative
models. The Spatial-Exclusion benchmark withholds all supercells of a given
radius from a diverse dataset, enabling controlled assessments of spatial
interpolation and extrapolation. The Compositional-Exclusion benchmark omits
all samples of a specific chemical composition, probing generalization across
stoichiometries. Nine vision--language foundation models are prompted with
crystallographic images and textual context to generate structural annotations.
Responses are evaluated via (i) relative errors in lattice parameters and
density, (ii) a physics-consistency index penalizing volumetric violations, and
(iii) a hallucination score capturing geometric outliers and invalid
space-group predictions. These benchmarks establish a reproducible, physically
informed framework for assessing generalization, consistency, and reliability
in large-scale multimodal models. Dataset and code are available at
https://github.com/KurbanIntelligenceLab/StressTestingMMFMinCR....

---

### 81. Symmetry in Neural Network Parameter Spaces

**Authors:** Bo Zhao, Robin Walters, Rose Yu

**Published:** 2025-06-16

**Category:** cs.LG

**ID:** 2506.13018v1

**Link:** [http://arxiv.org/abs/2506.13018v1](http://arxiv.org/abs/2506.13018v1)

**Summary:** Modern deep learning models are highly overparameterized, resulting in large
sets of parameter configurations that yield the same outputs. A significant
portion of this redundancy is explained by symmetries in the parameter
space--transformations that leave the network function unchanged. These
symmetries shape the loss landscape and constrain learning dynamics, offering a
new lens for understanding optimization, generalization, and model complexity
that complements existing theory of deep learning. This survey provides an
overview of parameter space symmetry. We summarize existing literature, uncover
connections between symmetry and learning theory, and identify gaps and
opportunities in this emerging field....

---

### 82. DeFoG: Discrete Flow Matching for Graph Generation

**Authors:** Yiming Qin, Manuel Madeira, Dorina Thanou, Pascal Frossard

**Published:** 2024-10-05

**Category:** cs.LG

**ID:** 2410.04263v3

**Link:** [http://arxiv.org/abs/2410.04263v3](http://arxiv.org/abs/2410.04263v3)

**Summary:** Graph generative models are essential across diverse scientific domains by
capturing complex distributions over relational data. Among them, graph
diffusion models achieve superior performance but face inefficient sampling and
limited flexibility due to the tight coupling between training and sampling
stages. We introduce DeFoG, a novel graph generative framework that
disentangles sampling from training, enabling a broader design space for more
effective and efficient model optimization. DeFoG employs a discrete
flow-matching formulation that respects the inherent symmetries of graphs. We
theoretically ground this disentangled formulation by explicitly relating the
training loss to the sampling algorithm and showing that DeFoG faithfully
replicates the ground truth graph distribution. Building on these foundations,
we thoroughly investigate DeFoG's design space and propose novel sampling
methods that significantly enhance performance and reduce the required number
of refinement steps. Extensive experiments demonstrate state-of-the-art
performance across synthetic, molecular, and digital pathology datasets,
covering both unconditional and conditional generation settings. It also
outperforms most diffusion-based models with just 5-10% of their sampling
steps....

---

### 83. Symmetry-preserving neural networks in lattice field theories

**Authors:** Matteo Favoni

**Published:** 2025-06-14

**Category:** hep-lat

**ID:** 2506.12493v1

**Link:** [http://arxiv.org/abs/2506.12493v1](http://arxiv.org/abs/2506.12493v1)

**Summary:** This thesis deals with neural networks that respect symmetries and presents
the advantages in applying them to lattice field theory problems. The concept
of equivariance is explained, together with the reason why such a property is
crucial for the network to preserve the desired symmetry. The benefits of
choosing equivariant networks are first illustrated for translational symmetry
on a complex scalar field toy model. The discussion is then extended to gauge
theories, for which Lattice Gauge Equivariant Convolutional Neural Networks
(L-CNNs) are specifically designed ad hoc. Regressions of physical observables
such as Wilson loops are successfully solved by L-CNNs, whereas traditional
architectures which are not gauge symmetric perform significantly worse.
Finally, we introduce the technique of neural gradient flow, which is an
ordinary differential equation solved by neural networks, and propose it as a
method to generate lattice gauge configurations....

---

### 84. SplashNet: Split-and-Share Encoders for Accurate and Efficient Typing with Surface Electromyography

**Authors:** Nima Hadidi, Jason Chan, Ebrahim Feghhi, Jonathan Kao

**Published:** 2025-06-14

**Category:** cs.HC

**ID:** 2506.12356v1

**Link:** [http://arxiv.org/abs/2506.12356v1](http://arxiv.org/abs/2506.12356v1)

**Summary:** Surface electromyography (sEMG) at the wrists could enable natural,
keyboard-free text entry, yet the state-of-the-art emg2qwerty baseline still
misrecognizes $51.8\%$ of characters in the zero-shot setting on unseen users
and $7.0\%$ after user-specific fine-tuning. We trace many of these errors to
mismatched cross-user signal statistics, fragile reliance on high-order feature
dependencies, and the absence of architectural inductive biases aligned with
the bilateral nature of typing. To address these issues, we introduce three
simple modifications: (i) Rolling Time Normalization, which adaptively aligns
input distributions across users; (ii) Aggressive Channel Masking, which
encourages reliance on low-order feature combinations more likely to generalize
across users; and (iii) a Split-and-Share encoder that processes each hand
independently with weight-shared streams to reflect the bilateral symmetry of
the neuromuscular system. Combined with a five-fold reduction in spectral
resolution ($33\!\rightarrow\!6$ frequency bands), these components yield a
compact Split-and-Share model, SplashNet-mini, which uses only $\tfrac14$ the
parameters and $0.6\times$ the FLOPs of the baseline while reducing
character-error rate (CER) to $36.4\%$ zero-shot and $5.9\%$ after fine-tuning.
An upscaled variant, SplashNet ($\tfrac12$ the parameters, $1.15\times$ the
FLOPs of the baseline), further lowers error to $35.7\%$ and $5.5\%$,
representing relative improvements of $31\%$ and $21\%$ in the zero-shot and
fine-tuned settings, respectively. SplashNet therefore establishes a new state
of the art without requiring additional data....

---

### 85. Fundamentals and Advances in Transverse Thermoelectrics

**Authors:** Hiroto Adachi, Fuyuki Ando, Takamasa Hirai, Rajkumar Modak, Matthew Grayson, Ken-ichi Uchida

**Published:** 2025-06-14

**Category:** cond-mat.mtrl-sci

**ID:** 2506.12319v1

**Link:** [http://arxiv.org/abs/2506.12319v1](http://arxiv.org/abs/2506.12319v1)

**Summary:** Transverse thermoelectric effects interconvert charge and heat currents in
orthogonal directions due to the breaking of either time-reversal symmetry or
structural symmetry, enabling simple and versatile thermal energy harvesting
and solid-state cooling within single materials. In comparison to the complex
module structures required for the conventional Seebeck and Peltier effects,
the transverse thermoelectric effects provide the complete device structures,
potentially resolving the fundamental issue of multi-module degradation of
thermoelectric conversion performance. This review article provides an overview
of all currently known transverse thermoelectric conversion phenomena and
principles, as well as their characteristics, and reclassifies them in a
unified manner. The performance of the transverse thermoelectric generator,
refrigerator, and active cooler is formulated, showing that thermal boundary
conditions play an essential role to discuss their behaviors. Examples of
recent application research and material development in transverse
thermoelectrics are also introduced, followed by a discussion of future
prospects....

---

### 86. Piezoelectric truss metamaterials: data-driven design and additive manufacturing

**Authors:** Saurav Sharma, Satya K. Ammu, Prakash Thakolkaran, Jovana Jovanova, Kunal Masania, Siddhant Kumar

**Published:** 2025-06-13

**Category:** physics.app-ph

**ID:** 2506.22451v1

**Link:** [http://arxiv.org/abs/2506.22451v1](http://arxiv.org/abs/2506.22451v1)

**Summary:** In the development of active animate materials, electromechanical coupling is
highly attractive to realize mechanoresponsive functionality. Piezoelectricity
is the most utilized electromechanical phenomenon due to the wide availability
of materials that display precise and reliable coupling. However, the inherent
directionality of these materials is constrained by the symmetry of their
crystal structure, which limits the choice of available properties in natural
piezoelectric materials. A solution to alleviate this limitation could be to
leverage geometry or architecture at the mesoscale. Here, we present an
integrated framework to design and 3D-print piezoelectric truss metamaterials
with customizable anisotropic responses. To explore the vast design space of
truss metamaterials, we employ generative machine learning to optimize the
topology and geometry of truss lattices and achieve target piezoelectricity.
Then, we develop an in-gel-3D printing method to fabricate polymer-ceramic
piezoelectric truss metamaterial structures using a composite slurry of
photo-curable resin and lead-free piezoelectric particles. The ML framework
discovers designs exhibiting unconventional behaviors, including auxetic,
unidirectional, and omnidirectional piezoelectricity, while the additive
manufacturing technique ensures shaping freedom and precision in fabricating
these metamaterials at small scales. Our results show an improvement of over
48% in the specific hydrostatic piezoelectric coefficient in optimized
metamaterials over bulk lead zirconate titanate (PZT). We successfully achieved
metamaterials with higher transverse piezoelectric coupling coefficient than
its longitudinal coefficient, which is a phenomenon that is rare in bulk
materials. Our approach enables customizable piezoelectric responses and paves
the way towards the development of a new generation of electro-active animate
materials....

---

### 87. A Rescaling-Invariant Lipschitz Bound Based on Path-Metrics for Modern ReLU Network Parameterizations

**Authors:** Antoine Gonon, Nicolas Brisebarre, Elisa Riccietti, Rémi Gribonval

**Published:** 2024-05-23

**Category:** cs.LG

**ID:** 2405.15006v3

**Link:** [http://arxiv.org/abs/2405.15006v3](http://arxiv.org/abs/2405.15006v3)

**Summary:** Robustness with respect to weight perturbations underpins guarantees for
generalization, pruning and quantization. Existing guarantees rely on Lipschitz
bounds in parameter space, cover only plain feed-forward MLPs, and break under
the ubiquitous neuron-wise rescaling symmetry of ReLU networks. We prove a new
Lipschitz inequality expressed through the $\ell^1$-path-metric of the weights.
The bound is (i) rescaling-invariant by construction and (ii) applies to any
ReLU-DAG architecture with any combination of convolutions, skip connections,
pooling, and frozen (inference-time) batch-normalization -- thus encompassing
ResNets, U-Nets, VGG-style CNNs, and more. By respecting the network's natural
symmetries, the new bound strictly sharpens prior parameter-space bounds and
can be computed in two forward passes. To illustrate its utility, we derive
from it a symmetry-aware pruning criterion and show -- through a
proof-of-concept experiment on a ResNet-18 trained on ImageNet -- that its
pruning performance matches that of classical magnitude pruning, while becoming
totally immune to arbitrary neuron-wise rescalings....

---

### 88. Polymorphism Crystal Structure Prediction with Adaptive Space Group Diversity Control

**Authors:** Sadman Sadeed Omee, Lai Wei, Sourin Dey, Jianjun Hu

**Published:** 2025-06-12

**Category:** cond-mat.mtrl-sci

**ID:** 2506.11332v1

**Link:** [http://arxiv.org/abs/2506.11332v1](http://arxiv.org/abs/2506.11332v1)

**Summary:** Crystalline materials can form different structural arrangements (i.e.
polymorphs) with the same chemical composition, exhibiting distinct physical
properties depending on how they were synthesized or the conditions under which
they operate. For example, carbon can exist as graphite (soft, conductive) or
diamond (hard, insulating). Computational methods that can predict these
polymorphs are vital in materials science, which help understand stability
relationships, guide synthesis efforts, and discover new materials with desired
properties without extensive trial-and-error experimentation. However,
effective crystal structure prediction (CSP) algorithms for inorganic polymorph
structures remain limited. We propose ParetoCSP2, a multi-objective genetic
algorithm for polymorphism CSP that incorporates an adaptive space group
diversity control technique, preventing over-representation of any single space
group in the population guided by a neural network interatomic potential. Using
an improved population initialization method and performing iterative structure
relaxation, ParetoCSP2 not only alleviates premature convergence but also
achieves improved convergence speed. Our results show that ParetoCSP2 achieves
excellent performance in polymorphism prediction, including a nearly perfect
space group and structural similarity accuracy for formulas with two polymorphs
but with the same number of unit cell atoms. Evaluated on a benchmark dataset,
it outperforms baseline algorithms by factors of 2.46-8.62 for these accuracies
and improves by 44.8\%-87.04\% across key performance metrics for regular CSP.
Our source code is freely available at
https://github.com/usccolumbia/ParetoCSP2....

---

### 89. Deterministic Switching of the Néel Vector by Asymmetric Spin Torque

**Authors:** Shui-Sen Zhang, Zi-An Wang, Bo Li, Wen-Jian Lu, Mingliang Tian, Yu-Ping Sun, Haifeng Du, Ding-Fu Shao

**Published:** 2025-06-12

**Category:** cond-mat.mtrl-sci

**ID:** 2506.10786v1

**Link:** [http://arxiv.org/abs/2506.10786v1](http://arxiv.org/abs/2506.10786v1)

**Summary:** N\'{e}el vector, the order parameter of collinear antiferromagnets, serves as
a state variable in associated antiferromagnetic (AFM) spintronic devices to
encode information. A deterministic switching of N\'{e}el vector is crucial for
the write-in operation, which, however, remains a challenging problem in AFM
spintronics. Here we demonstrate, based on analytical derivation and macro-spin
simulations, that N\'{e}el vector switching can be generally achieved via a
current-induced spin torque, provided the spin accumulations responsible for
this torque are non-identical between opposite sublattices. This condition
occurs widely in AFM films, as symmetry equivalence between
sublattice-dependent spin accumulations is usually absent, allowing unequal
spin accumulations induced by Edelstein effect or a spin current. The
consequent asymmetric spin torque leads to N\'{e}el vector dynamics
fundamentally different from previous expectations. The switching conditions
derived analytically agree well with simulation results and suggest various
directions for further optimization. Our work establishes a general mechanism
for current-induced N\'{e}el vector switching, which is in principle feasible
for all collinear antiferromagnets, and thus paves the route to realize
efficient writing in antiferromagnetic spintronics....

---

### 90. Field-free perpendicular magnetization switching by altermagnet with collinear spin current

**Authors:** M. Q. Dong, Zhi-Xin Guo, Xin-Gao Gong

**Published:** 2025-06-12

**Category:** cond-mat.mtrl-sci

**ID:** 2506.10336v1

**Link:** [http://arxiv.org/abs/2506.10336v1](http://arxiv.org/abs/2506.10336v1)

**Summary:** The generation of collinear spin current (CSC), where both the propagation
direction and spin-polarized direction aligned perpendicularly to the applied
charge current, is crucial for efficiently manipulating systems with
perpendicular magnetic anisotropy used in high-density magnetic recording.
However, the efficient generation of CSC remains a challenge. In this work,
based on the symmetry analysis, we propose that CSC can be effectively
generated using altermagnets when the charge current is aligned along specific
directions, due to spin-dependent symmetry breaking. This proposal is supported
by density functional theory (DFT) and Boltzmann transport equation (BTE)
calculations on a series of altermagnetic materials, including RuO2, Mn5Si3,
KRu4O8 and CuF2, where unusually large CSC is produced by the charge current
along certain orientations. Furthermore, we introduce a physical quantity, the
spin-splitting angle, to quantify the efficiency of CSC generated by the charge
current. We find that the spin-splitting angle ranges from 0.24 to 0.57 in
these altermagnets, which is significantly larger than the spin-Hall angle
typically observed in the anomalous spin-Hall effect, where the spin-Hall angle
is generally less than 0.1. Our findings provide an effective method for
manipulating spin currents, which is advantageous for the exploration of
altermagnetic spintronic devices with field-free perpendicular magnetization
switching....

---

### 91. DUN-SRE: Deep Unrolling Network with Spatiotemporal Rotation Equivariance for Dynamic MRI Reconstruction

**Authors:** Yuliang Zhu, Jing Cheng, Qi Xie, Zhuo-Xu Cui, Qingyong Zhu, Yuanyuan Liu, Xin Liu, Jianfeng Ren, Chengbo Wang, Dong Liang

**Published:** 2025-06-12

**Category:** eess.IV

**ID:** 2506.10309v1

**Link:** [http://arxiv.org/abs/2506.10309v1](http://arxiv.org/abs/2506.10309v1)

**Summary:** Dynamic Magnetic Resonance Imaging (MRI) exhibits transformation symmetries,
including spatial rotation symmetry within individual frames and temporal
symmetry along the time dimension. Explicit incorporation of these symmetry
priors in the reconstruction model can significantly improve image quality,
especially under aggressive undersampling scenarios. Recently, Equivariant
convolutional neural network (ECNN) has shown great promise in exploiting
spatial symmetry priors. However, existing ECNNs critically fail to model
temporal symmetry, arguably the most universal and informative structural prior
in dynamic MRI reconstruction. To tackle this issue, we propose a novel Deep
Unrolling Network with Spatiotemporal Rotation Equivariance (DUN-SRE) for
Dynamic MRI Reconstruction. The DUN-SRE establishes spatiotemporal equivariance
through a (2+1)D equivariant convolutional architecture. In particular, it
integrates both the data consistency and proximal mapping module into a unified
deep unrolling framework. This architecture ensures rigorous propagation of
spatiotemporal rotation symmetry constraints throughout the reconstruction
process, enabling more physically accurate modeling of cardiac motion dynamics
in cine MRI. In addition, a high-fidelity group filter parameterization
mechanism is developed to maintain representation precision while enforcing
symmetry constraints. Comprehensive experiments on Cardiac CINE MRI datasets
demonstrate that DUN-SRE achieves state-of-the-art performance, particularly in
preserving rotation-symmetric structures, offering strong generalization
capability to a broad range of dynamic MRI reconstruction tasks....

---

### 92. Learning single-index models via harmonic decomposition

**Authors:** Nirmit Joshi, Hugo Koubbi, Theodor Misiakiewicz, Nathan Srebro

**Published:** 2025-06-11

**Category:** cs.LG

**ID:** 2506.09887v1

**Link:** [http://arxiv.org/abs/2506.09887v1](http://arxiv.org/abs/2506.09887v1)

**Summary:** We study the problem of learning single-index models, where the label $y \in
\mathbb{R}$ depends on the input $\boldsymbol{x} \in \mathbb{R}^d$ only through
an unknown one-dimensional projection $\langle
\boldsymbol{w}_*,\boldsymbol{x}\rangle$. Prior work has shown that under
Gaussian inputs, the statistical and computational complexity of recovering
$\boldsymbol{w}_*$ is governed by the Hermite expansion of the link function.
In this paper, we propose a new perspective: we argue that "spherical
harmonics" -- rather than "Hermite polynomials" -- provide the natural basis
for this problem, as they capture its intrinsic "rotational symmetry". Building
on this insight, we characterize the complexity of learning single-index models
under arbitrary spherically symmetric input distributions. We introduce two
families of estimators -- based on tensor unfolding and online SGD -- that
respectively achieve either optimal sample complexity or optimal runtime, and
argue that estimators achieving both may not exist in general. When specialized
to Gaussian inputs, our theory not only recovers and clarifies existing results
but also reveals new phenomena that had previously been overlooked....

---

### 93. Type III Valley Polarization and Anomalous Valley Hall Effect in Two-Dimensional Non-Janus and Janus Altermagnet Fe2WS2Se2

**Authors:** Yanchao She, Yiding Wang, Hanbo Sun, Chao Wu, Weixi Zhang, Ping Li

**Published:** 2025-06-11

**Category:** cond-mat.mtrl-sci

**ID:** 2506.09675v1

**Link:** [http://arxiv.org/abs/2506.09675v1](http://arxiv.org/abs/2506.09675v1)

**Summary:** Exploiting the valley degree of freedom introduces a novel paradigm for
advancing quantum information technology. Currently, the investigation on
spontaneous valley polarization mainly focuses on two major types of systems.
One type magnetic systems by breaking the time-reversal symmetry, the other is
ferroelectric materials through breaking the inversion symmetry. Might there be
additional scenarios? Here, we propose to realize spontaneous valley
polarization by breaking the mirror symmetry in the altermagnets, named type
III valley polarization. Through symmetry analysis and first-principles
calculations, we confirm that this mechanism is feasible in Non-Janus
Fe2WS2Se2. Monolayer Non-Janus and Janus Fe2WS2Se2 are stable Neel-type
antiferromagnetic state with the direct band gap semiconductor. More
interestingly, their magnetic anisotropy energy exhibits the rare biaxial
anisotropy and a four-leaf clover shape in the xy plane, while the xz and yz
planes show the common uniaxial anisotropy. This originated from the
fourth-order single ion interactions. More importantly, the valley splitting is
spontaneously generated in the Non-Janus Fe2WS2Se2 due to the Mxy symmetry
breaking, without requiring the SOC effect. Both the Non-Janus and Janus
Fe2WS2Se2 exhibit diverse valley polarization and anomalous valley Hall effect
properties. In addition, the magnitude and direction of valley polarization can
be effectively tuned by the biaxial strain and magnetic field. Our findings not
only expand the realization system of spontaneous valley polarization, but also
provide a theoretical basis for the high-density storage of valley degrees of
freedom....

---

### 94. Efficient Prediction of SO(3)-Equivariant Hamiltonian Matrices via SO(2) Local Frames

**Authors:** Haiyang Yu, Yuchao Lin, Xuan Zhang, Xiaofeng Qian, Shuiwang Ji

**Published:** 2025-06-11

**Category:** cs.LG

**ID:** 2506.09398v1

**Link:** [http://arxiv.org/abs/2506.09398v1](http://arxiv.org/abs/2506.09398v1)

**Summary:** We consider the task of predicting Hamiltonian matrices to accelerate
electronic structure calculations, which plays an important role in physics,
chemistry, and materials science. Motivated by the inherent relationship
between the off-diagonal blocks of the Hamiltonian matrix and the SO(2) local
frame, we propose a novel and efficient network, called QHNetV2, that achieves
global SO(3) equivariance without the costly SO(3) Clebsch-Gordan tensor
products. This is achieved by introducing a set of new efficient and powerful
SO(2)-equivariant operations and performing all off-diagonal feature updates
and message passing within SO(2) local frames, thereby eliminating the need of
SO(3) tensor products. Moreover, a continuous SO(2) tensor product is performed
within the SO(2) local frame at each node to fuse node features, mimicking the
symmetric contraction operation. Extensive experiments on the large QH9 and
MD17 datasets demonstrate that our model achieves superior performance across a
wide range of molecular structures and trajectories, highlighting its strong
generalization capability. The proposed SO(2) operations on SO(2) local frames
offer a promising direction for scalable and symmetry-aware learning of
electronic structures. Our code will be released as part of the AIRS library
https://github.com/divelab/AIRS....

---

### 95. Generalized Lie Symmetries in Physics-Informed Neural Operators

**Authors:** Amy Xiang Wang, Zakhar Shumaylov, Peter Zaika, Ferdia Sherry, Carola-Bibiane Schönlieb

**Published:** 2025-02-01

**Category:** cs.LG

**ID:** 2502.00373v2

**Link:** [http://arxiv.org/abs/2502.00373v2](http://arxiv.org/abs/2502.00373v2)

**Summary:** Physics-informed neural operators (PINOs) have emerged as powerful tools for
learning solution operators of partial differential equations (PDEs). Recent
research has demonstrated that incorporating Lie point symmetry information can
significantly enhance the training efficiency of PINOs, primarily through
techniques like data, architecture, and loss augmentation. In this work, we
focus on the latter, highlighting that point symmetries oftentimes result in no
training signal, limiting their effectiveness in many problems. To address
this, we propose a novel loss augmentation strategy that leverages evolutionary
representatives of point symmetries, a specific class of generalized symmetries
of the underlying PDE. These generalized symmetries provide a richer set of
generators compared to standard symmetries, leading to a more informative
training signal. We demonstrate that leveraging evolutionary representatives
enhances the performance of neural operators, resulting in improved data
efficiency and accuracy during training....

---

### 96. Artificial Intelligence for Science in Quantum, Atomistic, and Continuum Systems

**Authors:** Xuan Zhang, Limei Wang, Jacob Helwig, Youzhi Luo, Cong Fu, Yaochen Xie, Meng Liu, Yuchao Lin, Zhao Xu, Keqiang Yan, Keir Adams, Maurice Weiler, Xiner Li, Tianfan Fu, Yucheng Wang, Alex Strasser, Haiyang Yu, YuQing Xie, Xiang Fu, Shenglong Xu, Yi Liu, Yuanqi Du, Alexandra Saxton, Hongyi Ling, Hannah Lawrence, Hannes Stärk, Shurui Gui, Carl Edwards, Nicholas Gao, Adriana Ladera, Tailin Wu, Elyssa F. Hofgard, Aria Mansouri Tehrani, Rui Wang, Ameya Daigavane, Montgomery Bohde, Jerry Kurtin, Qian Huang, Tuong Phung, Minkai Xu, Chaitanya K. Joshi, Simon V. Mathis, Kamyar Azizzadenesheli, Ada Fang, Alán Aspuru-Guzik, Erik Bekkers, Michael Bronstein, Marinka Zitnik, Anima Anandkumar, Stefano Ermon, Pietro Liò, Rose Yu, Stephan Günnemann, Jure Leskovec, Heng Ji, Jimeng Sun, Regina Barzilay, Tommi Jaakkola, Connor W. Coley, Xiaoning Qian, Xiaofeng Qian, Tess Smidt, Shuiwang Ji

**Published:** 2023-07-17

**Category:** cs.LG

**ID:** 2307.08423v5

**Link:** [http://arxiv.org/abs/2307.08423v5](http://arxiv.org/abs/2307.08423v5)

**Summary:** Advances in artificial intelligence (AI) are fueling a new paradigm of
discoveries in natural sciences. Today, AI has started to advance natural
sciences by improving, accelerating, and enabling our understanding of natural
phenomena at a wide range of spatial and temporal scales, giving rise to a new
area of research known as AI for science (AI4Science). Being an emerging
research paradigm, AI4Science is unique in that it is an enormous and highly
interdisciplinary area. Thus, a unified and technical treatment of this field
is needed yet challenging. This work aims to provide a technically thorough
account of a subarea of AI4Science; namely, AI for quantum, atomistic, and
continuum systems. These areas aim at understanding the physical world from the
subatomic (wavefunctions and electron density), atomic (molecules, proteins,
materials, and interactions), to macro (fluids, climate, and subsurface) scales
and form an important subarea of AI4Science. A unique advantage of focusing on
these areas is that they largely share a common set of challenges, thereby
allowing a unified and foundational treatment. A key common challenge is how to
capture physics first principles, especially symmetries, in natural systems by
deep learning methods. We provide an in-depth yet intuitive account of
techniques to achieve equivariance to symmetry transformations. We also discuss
other common technical challenges, including explainability,
out-of-distribution generalization, knowledge transfer with foundation and
large language models, and uncertainty quantification. To facilitate learning
and education, we provide categorized lists of resources that we found to be
useful. We strive to be thorough and unified and hope this initial effort may
trigger more community interests and efforts to further advance AI4Science....

---

### 97. Spectral invariance and maximality properties of the frequency spectrum of quantum neural networks

**Authors:** Patrick Holzer, Ivica Turkalj

**Published:** 2024-02-22

**Category:** quant-ph

**ID:** 2402.14515v3

**Link:** [http://arxiv.org/abs/2402.14515v3](http://arxiv.org/abs/2402.14515v3)

**Summary:** Quantum Neural Networks (QNNs) are a popular approach in Quantum Machine
Learning.
  We analyze this frequency spectrum using the Minkowski sum for sets and the
set of differences, which makes it particularly easy to express and calculate
the frequency spectrum algebraically, and prove different maximality results
for a large class of models.
  Furthermore, we prove that under some mild conditions there exists a
bijection between classes of models with the same area $A:=R\cdot L$ that
preserves the frequency spectrum, where $R$ denotes the number of qubits and
$L$ the number of layers, which we consequently call spectral invariance under
area-preserving transformations. With this we explain the symmetry in $R$ and
$L$ in the results often observed in the literature and show that the maximal
frequency spectrum depends only on the area $A=RL$ and not on the individual
values of $R$ and $L$. Moreover, we collect and extend existing results and
specify the maximum possible frequency spectrum of a QNN with arbitrarily many
layers as a function of the spectrum of its generators. In the case of
arbitrary dimensional generators, where our two introduces notions of
maximality differ, we extend existing results based on the so-called Golomb
ruler and introduce a second novel approach based on a variation of the
turnpike problem, which we call the relaxed turnpike problem....

---

### 98. Orbital Hall effect assisted field-free perpendicular magnetization switching

**Authors:** Zelalem Abebe Bekele, Yuan-Yuan Jiang, Kun Lei, Xiukai Lan, Xiangyu Liu, Hui Wen, Ding-Fu Shao, Kaiyou Wang

**Published:** 2024-04-20

**Category:** cond-mat.mes-hall

**ID:** 2404.13405v2

**Link:** [http://arxiv.org/abs/2404.13405v2](http://arxiv.org/abs/2404.13405v2)

**Summary:** Spin-orbit torques (SOTs) generated through the conventional spin Hall effect
(SHE) and/or Rashba-Edelstein effect offer potential for magnetization
manipulation. However, deterministic switching of perpendicular ferromagnets
via SOTs requires a strong symmetry-breaking perturbation, typically an
external magnetic field. Here, we demonstrate that field-free SOT switching of
perpendicular magnetization can be facilitated with the assistance of the
orbital Hall effect (OHE). Using a representative Co/PtGd bilayer SOT device,
we find that while the planar Hall effect (PHE) generates a finite out-of-plane
damping-like torque, representing a lateral symmetry breaking, the SHE-induced
torque achievable at practical current density is insufficient to switch the
perpendicular magnetization. Incorporating a Mo underlayer and exploiting its
strong OHE can amplify the in-plane damping-like torque via orbital-to-spin
conversion, enabling efficient field-free deterministic switching without
complex device geometries or low symmetric spin sources, providing a
straightforward and scalable strategy for achieving high-speed and low-power
spintronics....

---

### 99. Sharper Convergence Rates for Nonconvex Optimisation via Reduction Mappings

**Authors:** Evan Markou, Thalaiyasingam Ajanthan, Stephen Gould

**Published:** 2025-06-10

**Category:** math.OC

**ID:** 2506.08428v1

**Link:** [http://arxiv.org/abs/2506.08428v1](http://arxiv.org/abs/2506.08428v1)

**Summary:** Many high-dimensional optimisation problems exhibit rich geometric structures
in their set of minimisers, often forming smooth manifolds due to
over-parametrisation or symmetries. When this structure is known, at least
locally, it can be exploited through reduction mappings that reparametrise part
of the parameter space to lie on the solution manifold. These reductions
naturally arise from inner optimisation problems and effectively remove
redundant directions, yielding a lower-dimensional objective. In this work, we
introduce a general framework to understand how such reductions influence the
optimisation landscape. We show that well-designed reduction mappings improve
curvature properties of the objective, leading to better-conditioned problems
and theoretically faster convergence for gradient-based methods. Our analysis
unifies a range of scenarios where structural information at optimality is
leveraged to accelerate convergence, offering a principled explanation for the
empirical gains observed in such optimisation algorithms....

---

### 100. Sparse Training from Random Initialization: Aligning Lottery Ticket Masks using Weight Symmetry

**Authors:** Mohammed Adnan, Rohan Jain, Ekansh Sharma, Rahul Krishnan, Yani Ioannou

**Published:** 2025-05-08

**Category:** cs.LG

**ID:** 2505.05143v2

**Link:** [http://arxiv.org/abs/2505.05143v2](http://arxiv.org/abs/2505.05143v2)

**Summary:** The Lottery Ticket Hypothesis (LTH) suggests there exists a sparse LTH mask
and weights that achieve the same generalization performance as the dense model
while using significantly fewer parameters. However, finding a LTH solution is
computationally expensive, and a LTH sparsity mask does not generalize to other
random weight initializations. Recent work has suggested that neural networks
trained from random initialization find solutions within the same basin modulo
permutation, and proposes a method to align trained models within the same loss
basin. We hypothesize that misalignment of basins is the reason why LTH masks
do not generalize to new random initializations and propose permuting the LTH
mask to align with the new optimization basin when performing sparse training
from a different random init. We empirically show a significant increase in
generalization when sparse training from random initialization with the
permuted mask as compared to using the non-permuted LTH mask, on multiple
datasets (CIFAR-10, CIFAR-100 and ImageNet) and models (VGG11, ResNet20 and
ResNet50)....

---

### 101. AI-Assisted Rapid Crystal Structure Generation Towards a Target Local Environment

**Authors:** Osman Goni Ridwan, Sylvain Pitié, Monish Soundar Raj, Dong Dai, Gilles Frapper, Hongfei Xue, Qiang Zhu

**Published:** 2025-06-09

**Category:** cond-mat.mtrl-sci

**ID:** 2506.08224v1

**Link:** [http://arxiv.org/abs/2506.08224v1](http://arxiv.org/abs/2506.08224v1)

**Summary:** In the field of material design, traditional crystal structure prediction
approaches require extensive structural sampling through computationally
expensive energy minimization methods using either force fields or quantum
mechanical simulations. While emerging artificial intelligence (AI) generative
models have shown great promise in generating realistic crystal structures more
rapidly, most existing models fail to account for the unique symmetries and
periodicity of crystalline materials, and they are limited to handling
structures with only a few tens of atoms per unit cell. Here, we present a
symmetry-informed AI generative approach called Local Environment
Geometry-Oriented Crystal Generator (LEGO-xtal) that overcomes these
limitations. Our method generates initial structures using AI models trained on
an augmented small dataset, and then optimizes them using machine learning
structure descriptors rather than traditional energy-based optimization. We
demonstrate the effectiveness of LEGO-xtal by expanding from 25 known
low-energy sp2 carbon allotropes to over 1,700, all within 0.5 eV/atom of the
ground-state energy of graphite. This framework offers a generalizable strategy
for the targeted design of materials with modular building blocks, such as
metal-organic frameworks and next-generation battery materials....

---

### 102. Toward Greater Autonomy in Materials Discovery Agents: Unifying Planning, Physics, and Scientists

**Authors:** Lianhao Zhou, Hongyi Ling, Keqiang Yan, Kaiji Zhao, Xiaoning Qian, Raymundo Arróyave, Xiaofeng Qian, Shuiwang Ji

**Published:** 2025-06-05

**Category:** cs.AI

**ID:** 2506.05616v2

**Link:** [http://arxiv.org/abs/2506.05616v2](http://arxiv.org/abs/2506.05616v2)

**Summary:** We aim at designing language agents with greater autonomy for crystal
materials discovery. While most of existing studies restrict the agents to
perform specific tasks within predefined workflows, we aim to automate workflow
planning given high-level goals and scientist intuition. To this end, we
propose Materials Agent unifying Planning, Physics, and Scientists, known as
MAPPS. MAPPS consists of a Workflow Planner, a Tool Code Generator, and a
Scientific Mediator. The Workflow Planner uses large language models (LLMs) to
generate structured and multi-step workflows. The Tool Code Generator
synthesizes executable Python code for various tasks, including invoking a
force field foundation model that encodes physics. The Scientific Mediator
coordinates communications, facilitates scientist feedback, and ensures
robustness through error reflection and recovery. By unifying planning,
physics, and scientists, MAPPS enables flexible and reliable materials
discovery with greater autonomy, achieving a five-fold improvement in
stability, uniqueness, and novelty rates compared with prior generative models
when evaluated on the MP-20 data. We provide extensive experiments across
diverse tasks to show that MAPPS is a promising framework for autonomous
materials discovery....

---

### 103. Neural networks for the prediction of peel force for skin adhesive interface using FEM simulation

**Authors:** Ashish Masarkar, Rakesh Gupta, Naga Neehar Dingari, Beena Rai

**Published:** 2025-06-09

**Category:** physics.med-ph

**ID:** 2506.19855v1

**Link:** [http://arxiv.org/abs/2506.19855v1](http://arxiv.org/abs/2506.19855v1)

**Summary:** Studying the peeling behaviour of adhesives on skin is vital for advancing
biomedical applications such as medical adhesives and transdermal patches.
Traditional methods like experimental testing and finite element method (FEM),
though considered gold standards, are resource-intensive, computationally
expensive and time-consuming, particularly when analysing a wide material
parameter space. In this study, we present a neural network-based approach to
predict the minimum peel force (F_min) required for adhesive detachment from
skin tissue, limiting the need for repeated FEM simulations and significantly
reducing the computational cost. Leveraging a dataset generated from FEM
simulations of 90 degree peel test with varying adhesive and fracture mechanics
parameters, our neural network model achieved high accuracy, validated through
rigorous 5-fold cross-validation. The final architecture was able to predict a
wide variety of skin-adhesive peeling behaviour, exhibiting a mean squared
error (MSE) of 3.66*10^-7 and a R^2 score of 0.94 on test set, demonstrating
robust performance. This work introduces a reliable, computationally efficient
method for predicting adhesive behaviour, significantly reducing simulation
time while maintaining accuracy. This integration of machine learning with
high-fidelity biomechanical simulations enables efficient design and
optimization of skin-adhesive systems, providing a scalable framework for
future research in computational dermato-mechanics and bio-adhesive material
design....

---

### 104. Orbital Hall Effect Enables Field-Free Magnetization Reversal in Ferrimagnets without Additional Conversion Layer

**Authors:** Zelalem Abebe Bekele, Kun Lei, Xiukai Lan, Xiangyu Liu, Hui Wen, Weihao Li, Yongcheng Deng, Wenkai Zhu, Kaiming Cai, Kaiyou Wang

**Published:** 2025-06-09

**Category:** cond-mat.mtrl-sci

**ID:** 2506.07608v1

**Link:** [http://arxiv.org/abs/2506.07608v1](http://arxiv.org/abs/2506.07608v1)

**Summary:** The spin Hall effect (SHE) enables efficient electrical manipulation of
magnetization through the spin Hall current
\left(\mathbit{J}_{\mathbit{SHE}}\right), advancing energy-efficient
spintronics. In parallel, the orbital Hall effect (OHE) offers an alternative
pathway to SHE for converting charge current into an angular momentum flow. In
this study, we demonstrate field-free current-induced perpendicular
ferrimagnetic deterministic switching within a Mo/CoGd device without an
additional orbital-to-spin conversion layer. This is achieved by harnessing
localized orbital Hall currents \left(\mathbit{J}_{\mathbit{OHE}}\right)
generated in the Mo layer. The in-plane symmetry breaking at the Mo/CoGd
surface-interface layer, validated by a pronounced planar Hall effect, gives
rise to a substantial unconventional z-polarized damping-like torque. The CoGd
serves a dual role: not only as a converter that transforms the significant
\mathbit{J}_{\mathbit{OHE}} into \mathbit{J}_{\mathbit{SHE}} but also as a
ferrimagnetic self-switching mechanism. This dual functionality enables highly
efficient field-free current-induced magnetization switching with a critical
current density as low as \mathbf{2}.\mathbf{51}\
\times{\mathbf{10}}^\mathbf{6} A cm-2. Our work highlights the potential of
orbital Hall currents for energy-efficient magnetization switching, making a
notable contribution to the burgeoning field of orbitronics....

---

### 105. Circumventing Backdoor Space via Weight Symmetry

**Authors:** Jie Peng, Hongwei Yang, Jing Zhao, Hengji Dong, Hui He, Weizhe Zhang, Haoyu He

**Published:** 2025-06-09

**Category:** cs.LG

**ID:** 2506.07467v1

**Link:** [http://arxiv.org/abs/2506.07467v1](http://arxiv.org/abs/2506.07467v1)

**Summary:** Deep neural networks are vulnerable to backdoor attacks, where malicious
behaviors are implanted during training. While existing defenses can
effectively purify compromised models, they typically require labeled data or
specific training procedures, making them difficult to apply beyond supervised
learning settings. Notably, recent studies have shown successful backdoor
attacks across various learning paradigms, highlighting a critical security
concern. To address this gap, we propose Two-stage Symmetry Connectivity (TSC),
a novel backdoor purification defense that operates independently of data
format and requires only a small fraction of clean samples. Through theoretical
analysis, we prove that by leveraging permutation invariance in neural networks
and quadratic mode connectivity, TSC amplifies the loss on poisoned samples
while maintaining bounded clean accuracy. Experiments demonstrate that TSC
achieves robust performance comparable to state-of-the-art methods in
supervised learning scenarios. Furthermore, TSC generalizes to self-supervised
learning frameworks, such as SimCLR and CLIP, maintaining its strong defense
capabilities. Our code is available at https://github.com/JiePeng104/TSC....

---

### 106. Audio synthesizer inversion in symmetric parameter spaces with approximately equivariant flow matching

**Authors:** Ben Hayes, Charalampos Saitis, György Fazekas

**Published:** 2025-06-08

**Category:** cs.SD

**ID:** 2506.07199v1

**Link:** [http://arxiv.org/abs/2506.07199v1](http://arxiv.org/abs/2506.07199v1)

**Summary:** Many audio synthesizers can produce the same signal given different parameter
configurations, meaning the inversion from sound to parameters is an inherently
ill-posed problem. We show that this is largely due to intrinsic symmetries of
the synthesizer, and focus in particular on permutation invariance. First, we
demonstrate on a synthetic task that regressing point estimates under
permutation symmetry degrades performance, even when using a
permutation-invariant loss function or symmetry-breaking heuristics. Then,
viewing equivalent solutions as modes of a probability distribution, we show
that a conditional generative model substantially improves performance.
Further, acknowledging the invariance of the implicit parameter distribution,
we find that performance is further improved by using a permutation equivariant
continuous normalizing flow. To accommodate intricate symmetries in real
synthesizers, we also propose a relaxed equivariance strategy that adaptively
discovers relevant symmetries from data. Applying our method to Surge XT, a
full-featured open source synthesizer used in real world audio production, we
find our method outperforms regression and generative baselines across audio
reconstruction metrics....

---

### 107. Equivariant Denoisers Cannot Copy Graphs: Align Your Graph Diffusion Models

**Authors:** Najwa Laabid, Severi Rissanen, Markus Heinonen, Arno Solin, Vikas Garg

**Published:** 2024-05-27

**Category:** cs.LG

**ID:** 2405.17656v2

**Link:** [http://arxiv.org/abs/2405.17656v2](http://arxiv.org/abs/2405.17656v2)

**Summary:** Graph diffusion models, dominant in graph generative modeling, remain
underexplored for graph-to-graph translation tasks like chemical reaction
prediction. We demonstrate that standard permutation equivariant denoisers face
fundamental limitations in these tasks due to their inability to break
symmetries in noisy inputs. To address this, we propose aligning input and
target graphs to break input symmetries while preserving permutation
equivariance in non-matching graph portions. Using retrosynthesis (i.e., the
task of predicting precursors for synthesis of a given target molecule) as our
application domain, we show how alignment dramatically improves discrete
diffusion model performance from 5% to a SOTA-matching 54.7% top-1 accuracy.
Code is available at https://github.com/Aalto-QuML/DiffAlign....

---

### 108. Dimensionless Hierarchical Topological Phononic States

**Authors:** Joel R. Pyfrom, Kai Sun, Jihong A. Ma

**Published:** 2025-06-08

**Category:** cond-mat.mes-hall

**ID:** 2506.07048v1

**Link:** [http://arxiv.org/abs/2506.07048v1](http://arxiv.org/abs/2506.07048v1)

**Summary:** Topological insulators exhibit unique boundary states that are protected by
the topology of the bulk bands, a phenomenon that has now been extended to
classical systems such as phononics and mechanics. Typically, nontrivial
topology in an $n$-dimensional bulk leads to the emergence of
$(n-1)$-dimensional topologically protected boundary states. However, these
states can often be gapped out by breaking the symmetry that protects them,
resulting in the possible creation of new in-gap higher-order topological
modes. A notable example of this is the higher-order topological insulator
(HOTI), where gapping out surface states leads to the formation of
lower-dimensional topological modes, such as hinge or corner states. This
process reduces the spatial dimensionality of the protected modes from $(n-1)$
to $(n-2)$ or even lower. In this work, we propose an alternative method to
achieve higher-order topological modes using a one-dimensional
Su-Schrieffer-Heeger model. Instead of relying on dimensional reduction, we
manipulate the positions of domain walls to gap out the originally
topologically protected domain-wall states, thereby inducing new higher-order
topological states. These new higher-order topological states can be
characterized using a generalized winding number calculation. This approach
allows for the realization of multiple (and even infinite) topological orders
within simple 1D lattices while maintaining the principle of bulk-boundary
correspondence. Our study reveals a new mechanism that enriches topological
hierarchies beyond conventional classifications. Such a mechanism could also be
extended to higher dimensions, potentially creating intricate networks of
topological states and advancing our control over wave phenomena....

---

### 109. Imprinting electrically switchable scalar spin chirality by anisotropic strain in a Kagome antiferromagnet

**Authors:** Debjoty Paul, Shivesh Yadav, Shikhar Gupta, Bikash Patra, Nilesh Kulkarni, Debashis Mondal, Kaushal Gavankar, Sourav K. Sahu, Biswarup Satpati, Bahadur Singh, Owen Benton, Shouvik Chatterjee

**Published:** 2024-11-04

**Category:** cond-mat.mtrl-sci

**ID:** 2411.01824v2

**Link:** [http://arxiv.org/abs/2411.01824v2](http://arxiv.org/abs/2411.01824v2)

**Summary:** Topological chiral antiferromagnets, such as Mn$_{3}$Sn, are emerging as
promising materials for next-generation spintronic devices due to their
intrinsic transport properties linked to exotic magnetic configurations. Here,
we demonstrate that anisotropic strain in Mn$_{3}$Sn thin films offers a novel
approach to manipulate the magnetic ground state, unlocking new functionalities
in this material. Anisotropic strain reduces the point group symmetry of the
manganese (Mn) Kagome triangles from $C_{3v}$ to $C_{1}$, significantly
altering the energy landscape of the magnetic states in Mn$_{3}$Sn. This
symmetry reduction enables even a tiny in-plane Dzyaloshinskii-Moriya (DM)
interaction to induce canting of the Mn spins out of the Kagome plane. The
modified magnetic ground state introduces a finite scalar spin chirality and
results in a significant Berry phase in momentum space. Consequently, a large
anomalous Hall effect emerges in the Kagome plane at room temperature - an
effect that is absent in the bulk material. Moreover, this two-fold degenerate
magnetic state enables the creation of multiple-stable, non-volatile anomalous
Hall resistance (AHR) memory states. These states are field-stable and can be
controlled by thermal assisted current-induced magnetization switching
requiring modest current densities and small bias fields, thereby offering a
compelling new functionality in Mn$_{3}$Sn for spintronic applications....

---

### 110. Accounting for plasticity: An extension of inelastic Constitutive Artificial Neural Networks

**Authors:** Birte Boes, Jaan-Willem Simon, Hagen Holthusen

**Published:** 2024-07-27

**Category:** cs.LG

**ID:** 2407.19326v2

**Link:** [http://arxiv.org/abs/2407.19326v2](http://arxiv.org/abs/2407.19326v2)

**Summary:** In this work, we extend the existing framework of inelastic constitutive
artificial neural networks (iCANNs) by incorporating plasticity to increase
their applicability to model more complex material behavior. The proposed
approach ensures objectivity, material symmetry, and thermodynamic consistency,
providing a robust basis for automatic model discovery of constitutive
equations at finite strains. These are predicted by discovering formulations
for the Helmholtz free energy and plastic potentials for the yield function and
evolution equations in terms of feed-forward networks. Our framework captures
both linear and nonlinear kinematic hardening behavior. Investigation of our
model's prediction showed that the extended iCANNs successfully predict both
linear and nonlinear kinematic hardening behavior based on experimental and
artificially generated datasets, showcasing promising capabilities of this
framework. Nonetheless, challenges remain in discovering more complex yield
criteria with tension-compression asymmetry and addressing deviations in
experimental data at larger strains. Despite these limitations, the proposed
framework provides a promising basis for incorporating plasticity into iCANNs,
offering a platform for advancing in the field of automated model discovery....

---

### 111. Rapid training of Hamiltonian graph networks without gradient descent

**Authors:** Atamert Rahma, Chinmay Datar, Ana Cukarska, Felix Dietrich

**Published:** 2025-06-06

**Category:** cs.LG

**ID:** 2506.06558v1

**Link:** [http://arxiv.org/abs/2506.06558v1](http://arxiv.org/abs/2506.06558v1)

**Summary:** Learning dynamical systems that respect physical symmetries and constraints
remains a fundamental challenge in data-driven modeling. Integrating physical
laws with graph neural networks facilitates principled modeling of complex
N-body dynamics and yields accurate and permutation-invariant models. However,
training graph neural networks with iterative, gradient-based optimization
algorithms (e.g., Adam, RMSProp, LBFGS) often leads to slow training,
especially for large, complex systems. In comparison to 15 different
optimizers, we demonstrate that Hamiltonian Graph Networks (HGN) can be trained
up to 600x faster--but with comparable accuracy--by replacing iterative
optimization with random feature-based parameter construction. We show robust
performance in diverse simulations, including N-body mass-spring systems in up
to 3 dimensions with different geometries, while retaining essential physical
invariances with respect to permutation, rotation, and translation. We reveal
that even when trained on minimal 8-node systems, the model can generalize in a
zero-shot manner to systems as large as 4096 nodes without retraining. Our work
challenges the dominance of iterative gradient-descent-based optimization
algorithms for training neural network models for physical systems....

---

### 112. Training-Free Constrained Generation With Stable Diffusion Models

**Authors:** Stefano Zampini, Jacob K. Christopher, Luca Oneto, Davide Anguita, Ferdinando Fioretto

**Published:** 2025-02-08

**Category:** cs.LG

**ID:** 2502.05625v3

**Link:** [http://arxiv.org/abs/2502.05625v3](http://arxiv.org/abs/2502.05625v3)

**Summary:** Stable diffusion models represent the state-of-the-art in data synthesis
across diverse domains and hold transformative potential for applications in
science and engineering, e.g., by facilitating the discovery of novel solutions
and simulating systems that are computationally intractable to model
explicitly. While there is increasing effort to incorporate physics-based
constraints into generative models, existing techniques are either limited in
their applicability to latent diffusion frameworks or lack the capability to
strictly enforce domain-specific constraints. To address this limitation this
paper proposes a novel integration of stable diffusion models with constrained
optimization frameworks, enabling the generation of outputs satisfying
stringent physical and functional requirements. The effectiveness of this
approach is demonstrated through material design experiments requiring
adherence to precise morphometric properties, challenging inverse design tasks
involving the generation of materials inducing specific stress-strain
responses, and copyright-constrained content generation tasks....

---

### 113. Clone-Robust Weights in Metric Spaces: Handling Redundancy Bias for Benchmark Aggregation

**Authors:** Damien Berriaud, Roger Wattenhofer

**Published:** 2025-02-05

**Category:** cs.LG

**ID:** 2502.03576v2

**Link:** [http://arxiv.org/abs/2502.03576v2](http://arxiv.org/abs/2502.03576v2)

**Summary:** We are given a set of elements in a metric space. The distribution of the
elements is arbitrary, possibly adversarial. Can we weigh the elements in a way
that is resistant to such (adversarial) manipulations? This problem arises in
various contexts. For instance, the elements could represent data points,
requiring robust domain adaptation. Alternatively, they might represent tasks
to be aggregated into a benchmark; or questions about personal political
opinions in voting advice applications. This article introduces a theoretical
framework for dealing with such problems. We propose clone-proof weighting
functions as a solution concept. These functions distribute importance across
elements of a set such that similar objects (``clones'') share (some of) their
weights, thus avoiding a potential bias introduced by their multiplicity. Our
framework extends the maximum uncertainty principle to accommodate general
metric spaces and includes a set of axioms -- symmetry, continuity, and
clone-proofness -- that guide the construction of weighting functions. Finally,
we address the existence of weighting functions satisfying our axioms in the
significant case of Euclidean spaces and propose a general method for their
construction....

---

### 114. EqCollide: Equivariant and Collision-Aware Deformable Objects Neural Simulator

**Authors:** Qianyi Chen, Tianrun Gao, Chenbo Jiang, Tailin Wu

**Published:** 2025-06-06

**Category:** cs.LG

**ID:** 2506.05797v1

**Link:** [http://arxiv.org/abs/2506.05797v1](http://arxiv.org/abs/2506.05797v1)

**Summary:** Simulating collisions of deformable objects is a fundamental yet challenging
task due to the complexity of modeling solid mechanics and multi-body
interactions. Existing data-driven methods often suffer from lack of
equivariance to physical symmetries, inadequate handling of collisions, and
limited scalability. Here we introduce EqCollide, the first end-to-end
equivariant neural fields simulator for deformable objects and their
collisions. We propose an equivariant encoder to map object geometry and
velocity into latent control points. A subsequent equivariant Graph Neural
Network-based Neural Ordinary Differential Equation models the interactions
among control points via collision-aware message passing. To reconstruct
velocity fields, we query a neural field conditioned on control point features,
enabling continuous and resolution-independent motion predictions. Experimental
results show that EqCollide achieves accurate, stable, and scalable simulations
across diverse object configurations, and our model achieves 24.34% to 35.82%
lower rollout MSE even compared with the best-performing baseline model.
Furthermore, our model could generalize to more colliding objects and extended
temporal horizons, and stay robust to input transformed with group action....

---

### 115. Phonon angular momentum induced by Terahertz electric field

**Authors:** Hong Sun, Xiaozhe Li, Lifa Zhang

**Published:** 2025-06-06

**Category:** cond-mat.mtrl-sci

**ID:** 2506.05715v1

**Link:** [http://arxiv.org/abs/2506.05715v1](http://arxiv.org/abs/2506.05715v1)

**Summary:** Despite the growing interest in phonon angular momentum (AM) in recent years,
current studies remain limited to a few materials due to the constraints
imposed by time reversal symmetry on macroscopic phonon AM. In this work, we
theoretically investigate the generation of total phonon AM through alternating
terahertz electric fields in polarized materials. In contrast to previous
studies on phonon AM, here the off-diagonal elements of the phonon AM operator
play an essential role. According to our formula, the large AM is generated
when the energy of incident electric fields matches the frequency of optical
phonons at {\Gamma} point. Furthermore, a specific resonance on the imaginary
part of the response coefficient, as well as periodic regulation of the phonon
AM by the phase difference of the driving field, is observed. In polar material
GaN, the oscillation maximum is observed as \hbar per unit cell which can be
experimentally measured through orbital magnetization induced by phonon AM. Our
work offers a promising approach to generate observable phonon AM in a wider
range of materials, advancing both the understanding of phonon fundamental
physics and potential applications in phononic devices....

---

### 116. Learning Design-Score Manifold to Guide Diffusion Models for Offline Optimization

**Authors:** Tailin Zhou, Zhilin Chen, Wenlong Lyu, Zhitang Chen, Danny H. K. Tsang, Jun Zhang

**Published:** 2025-06-06

**Category:** cs.LG

**ID:** 2506.05680v1

**Link:** [http://arxiv.org/abs/2506.05680v1](http://arxiv.org/abs/2506.05680v1)

**Summary:** Optimizing complex systems, from discovering therapeutic drugs to designing
high-performance materials, remains a fundamental challenge across science and
engineering, as the underlying rules are often unknown and costly to evaluate.
Offline optimization aims to optimize designs for target scores using
pre-collected datasets without system interaction. However, conventional
approaches may fail beyond training data, predicting inaccurate scores and
generating inferior designs. This paper introduces ManGO, a diffusion-based
framework that learns the design-score manifold, capturing the design-score
interdependencies holistically. Unlike existing methods that treat design and
score spaces in isolation, ManGO unifies forward prediction and backward
generation, attaining generalization beyond training data. Key to this is its
derivative-free guidance for conditional generation, coupled with adaptive
inference-time scaling that dynamically optimizes denoising paths. Extensive
evaluations demonstrate that ManGO outperforms 24 single- and 10
multi-objective optimization methods across diverse domains, including
synthetic tasks, robot control, material design, DNA sequence, and real-world
engineering optimization....

---

### 117. Geometric and Physical Constraints Synergistically Enhance Neural PDE Surrogates

**Authors:** Yunfei Huang, David S. Greenberg

**Published:** 2025-06-05

**Category:** cs.LG

**ID:** 2506.05513v1

**Link:** [http://arxiv.org/abs/2506.05513v1](http://arxiv.org/abs/2506.05513v1)

**Summary:** Neural PDE surrogates can improve the cost-accuracy tradeoff of classical
solvers, but often generalize poorly to new initial conditions and accumulate
errors over time. Physical and symmetry constraints have shown promise in
closing this performance gap, but existing techniques for imposing these
inductive biases are incompatible with the staggered grids commonly used in
computational fluid dynamics. Here we introduce novel input and output layers
that respect physical laws and symmetries on the staggered grids, and for the
first time systematically investigate how these constraints, individually and
in combination, affect the accuracy of PDE surrogates. We focus on two
challenging problems: shallow water equations with closed boundaries and
decaying incompressible turbulence. Compared to strong baselines, symmetries
and physical constraints consistently improve performance across tasks,
architectures, autoregressive prediction steps, accuracy measures, and network
sizes. Symmetries are more effective than physical constraints, but surrogates
with both performed best, even compared to baselines with data augmentation or
pushforward training, while themselves benefiting from the pushforward trick.
Doubly-constrained surrogates also generalize better to initial conditions and
durations beyond the range of the training data, and more accurately predict
real-world ocean currents....

---

### 118. Rectified Point Flow: Generic Point Cloud Pose Estimation

**Authors:** Tao Sun, Liyuan Zhu, Shengyu Huang, Shuran Song, Iro Armeni

**Published:** 2025-06-05

**Category:** cs.CV

**ID:** 2506.05282v1

**Link:** [http://arxiv.org/abs/2506.05282v1](http://arxiv.org/abs/2506.05282v1)

**Summary:** We introduce Rectified Point Flow, a unified parameterization that formulates
pairwise point cloud registration and multi-part shape assembly as a single
conditional generative problem. Given unposed point clouds, our method learns a
continuous point-wise velocity field that transports noisy points toward their
target positions, from which part poses are recovered. In contrast to prior
work that regresses part-wise poses with ad-hoc symmetry handling, our method
intrinsically learns assembly symmetries without symmetry labels. Together with
a self-supervised encoder focused on overlapping points, our method achieves a
new state-of-the-art performance on six benchmarks spanning pairwise
registration and shape assembly. Notably, our unified formulation enables
effective joint training on diverse datasets, facilitating the learning of
shared geometric priors and consequently boosting accuracy. Project page:
https://rectified-pointflow.github.io/....

---

### 119. Learning long range dependencies through time reversal symmetry breaking

**Authors:** Guillaume Pourcel, Maxence Ernoult

**Published:** 2025-06-05

**Category:** cs.LG

**ID:** 2506.05259v1

**Link:** [http://arxiv.org/abs/2506.05259v1](http://arxiv.org/abs/2506.05259v1)

**Summary:** Deep State Space Models (SSMs) reignite physics-grounded compute paradigms,
as RNNs could natively be embodied into dynamical systems. This calls for
dedicated learning algorithms obeying to core physical principles, with
efficient techniques to simulate these systems and guide their design. We
propose Recurrent Hamiltonian Echo Learning (RHEL), an algorithm which provably
computes loss gradients as finite differences of physical trajectories of
non-dissipative, Hamiltonian systems. In ML terms, RHEL only requires three
"forward passes" irrespective of model size, without explicit Jacobian
computation, nor incurring any variance in the gradient estimation. Motivated
by the physical realization of our algorithm, we first introduce RHEL in
continuous time and demonstrate its formal equivalence with the continuous
adjoint state method. To facilitate the simulation of Hamiltonian systems
trained by RHEL, we propose a discrete-time version of RHEL which is equivalent
to Backpropagation Through Time (BPTT) when applied to a class of recurrent
modules which we call Hamiltonian Recurrent Units (HRUs). This setting allows
us to demonstrate the scalability of RHEL by generalizing these results to
hierarchies of HRUs, which we call Hamiltonian SSMs (HSSMs). We apply RHEL to
train HSSMs with linear and nonlinear dynamics on a variety of time-series
tasks ranging from mid-range to long-range classification and regression with
sequence length reaching $\sim 50k$. We show that RHEL consistently matches the
performance of BPTT across all models and tasks. This work opens new doors for
the design of scalable, energy-efficient physical systems endowed with
self-learning capabilities for sequence modelling....

---

### 120. SESaMo: Symmetry-Enforcing Stochastic Modulation for Normalizing Flows

**Authors:** Janik Kreit, Dominic Schuh, Kim A. Nicoli, Lena Funcke

**Published:** 2025-05-26

**Category:** cs.LG

**ID:** 2505.19619v2

**Link:** [http://arxiv.org/abs/2505.19619v2](http://arxiv.org/abs/2505.19619v2)

**Summary:** Deep generative models have recently garnered significant attention across
various fields, from physics to chemistry, where sampling from unnormalized
Boltzmann-like distributions represents a fundamental challenge. In particular,
autoregressive models and normalizing flows have become prominent due to their
appealing ability to yield closed-form probability densities. Moreover, it is
well-established that incorporating prior knowledge - such as symmetries - into
deep neural networks can substantially improve training performances. In this
context, recent advances have focused on developing symmetry-equivariant
generative models, achieving remarkable results. Building upon these
foundations, this paper introduces Symmetry-Enforcing Stochastic Modulation
(SESaMo). Similar to equivariant normalizing flows, SESaMo enables the
incorporation of inductive biases (e.g., symmetries) into normalizing flows
through a novel technique called stochastic modulation. This approach enhances
the flexibility of the generative model, allowing to effectively learn a
variety of exact and broken symmetries. Our numerical experiments benchmark
SESaMo in different scenarios, including an 8-Gaussian mixture model and
physically relevant field theories, such as the $\phi^4$ theory and the Hubbard
model....

---

### 121. Tip-induced nitrene generation

**Authors:** Leonard-Alexander Lieske, Aaron H. Oechsle, Igor Rončević, Ilias Gazizullin, Florian Albrecht, Matthias Krinninger, Leonhard Grill, Friedrich Esch, Leo Gross

**Published:** 2025-06-05

**Category:** cond-mat.mtrl-sci

**ID:** 2506.04741v1

**Link:** [http://arxiv.org/abs/2506.04741v1](http://arxiv.org/abs/2506.04741v1)

**Summary:** We generated trinitreno-s-heptazine, a small molecule featuring three nitrene
centers, by tip-induced chemistry from the precursor 2,5,8-triazido-s-heptazine
on bilayer NaCl on Au(111). The precursor's azide groups were dissociated to
form mono-, di- and trinitreno-s-heptazine, yielding molecules with one to
three nitrene centers. The precursor and its products are characterized by
atomic force microscopy and scanning tunnelling microscopy. Broken-symmetry DFT
and configuration interaction calculations of inter- and intra-nitrene exchange
couplings suggest a ferromagnetic coupling of the S = 1 nitrene centers,
resulting in a high-spin septet ground state for neutral trinitreno-s-heptazine
in the gas phase. On bilayer NaCl on Au(111), the combined results of
experiments and theory suggest trinitreno-s-heptazine to be an anion with a
sextet ground state....

---

### 122. Wyckoff Transformer: Generation of Symmetric Crystals

**Authors:** Nikita Kazeev, Wei Nong, Ignat Romanov, Ruiming Zhu, Andrey Ustyuzhanin, Shuya Yamazaki, Kedar Hippalgaonkar

**Published:** 2025-03-04

**Category:** cond-mat.mtrl-sci

**ID:** 2503.02407v4

**Link:** [http://arxiv.org/abs/2503.02407v4](http://arxiv.org/abs/2503.02407v4)

**Summary:** Crystal symmetry plays a fundamental role in determining its physical,
chemical, and electronic properties such as electrical and thermal
conductivity, optical and polarization behavior, and mechanical strength.
Almost all known crystalline materials have internal symmetry. However, this is
often inadequately addressed by existing generative models, making the
consistent generation of stable and symmetrically valid crystal structures a
significant challenge. We introduce WyFormer, a generative model that directly
tackles this by formally conditioning on space group symmetry. It achieves this
by using Wyckoff positions as the basis for an elegant, compressed, and
discrete structure representation. To model the distribution, we develop a
permutation-invariant autoregressive model based on the Transformer encoder and
an absence of positional encoding. Extensive experimentation demonstrates
WyFormer's compelling combination of attributes: it achieves best-in-class
symmetry-conditioned generation, incorporates a physics-motivated inductive
bias, produces structures with competitive stability, predicts material
properties with competitive accuracy even without atomic coordinates, and
exhibits unparalleled inference speed....

---

### 123. Large Berry curvature effects induced by extended nodal structures: Rational design strategy and high-throughput materials predictions

**Authors:** Wencheng Wang, Minxue Yang, Wei Chen, Xiangang Wan, Feng Tang

**Published:** 2025-06-04

**Category:** cond-mat.mtrl-sci

**ID:** 2506.03871v1

**Link:** [http://arxiv.org/abs/2506.03871v1](http://arxiv.org/abs/2506.03871v1)

**Summary:** Berry curvature can drastically modify the electron dynamics, thereby
offering an effective pathway for electron manipulation and novel device
applications. Compared to zero-dimensional nodal points in Weyl/Dirac
semimetals, higher-dimensional extended nodal structures, such as nodal lines
and nodal surfaces, are more likely to intersect the Fermi surface, leading to
large Berry curvature effects without fine-tuning the chemical potential. In
this work, we propose a strategy that utilizes straight nodal lines (SNLs) and
flat nodal surfaces (FNSs) to design large Berry curvature effects, and we
exhaustively tabulate SNLs and FNSs within the 1651 magnetic space groups
(MSGs). We demonstrate that SNLs and FNSs can generate large Berry curvature
widely distributed in the Brillouin zone. As an application, we identify 158
MSGs that host FNSs, SNLs, or both and allow for nonvanishing anomalous Hall
conductivity (AHC). Based on these 158 MSGs, we screen materials from the
MAGNDATA magnetic material database for high-throughput calculations,
identifying 60 materials with AHC values exceeding $500\,\Omega^{-1}{\rm
cm}^{-1}$. We select the candidate materials $\rm SrRuO_3$ and $\rm
Ca_2NiOsO_6$ to demonstrate the contributions of FNSs and SNLs to one and two
nonvanishing AHC components, respectively. We also investigate the tuning of
AHC through symmetry breaking, outlining all possible symmetry-breaking
pathways, and select the candidate material HoNi to demonstrate this approach
by applying an external magnetic field. Additionally, we identify Berry
curvature quadrupoles in the candidate materials, indicating that our strategy
can be generalized to Berry curvature multipole effects. Our work will guide
both the theoretical and experimental design of materials with large Berry
curvature effects, with significant implications for a wide range of device
applications....

---

### 124. Understanding Stability Mechanisms in Single-Atom Alloys with Theory-infused Deep Learning

**Authors:** Yang Huang, Shih-Han Wang, Shuyi Cao, Luke E. K. Achenie, Hongliang Xin

**Published:** 2025-06-03

**Category:** cond-mat.mtrl-sci

**ID:** 2506.03031v1

**Link:** [http://arxiv.org/abs/2506.03031v1](http://arxiv.org/abs/2506.03031v1)

**Summary:** We present an interpretable deep learning model that enhances the prediction
of cohesive energy in transition metal alloys (TMAs) by incorporating cohesion
theory into a graph neural network (GNN) framework. The model not only predicts
the total cohesive energy-an indicator of crystal stability-but also
disentangles its various contributing factors and underlying physical
parameters. The physics insights extracted from the model clarify the stability
trends of transition metal surfaces across the periodic table. Furthermore, by
applying the model to single-atom alloys (SAAs), a class of catalytically
significant next-generation TMAs, we analyze and explain the relative stability
of monomer/dimer (in-plane symmetry breaking) and top-/sub-layer (out-of-plane
symmetry breaking) configurations. These two types of symmetry breaking lead to
distinct thermodynamic preferences in SAAs, governed by localized effects (e.g.
d-orbital coupling) and delocalized effects (e.g. wavefunction
renormalization). The model is thus positioned as a powerful tool for
understanding and strategically designing TMAs, enabling the tailored
development of materials with improved stability for advanced applications in
catalysis and materials science....

---

### 125. How does ion temperature gradient turbulence depend on magnetic geometry? Insights from data and machine learning

**Authors:** Matt Landreman, Jong Youl Choi, Caio Alves, Prasanna Balaprakash, R. Michael Churchill, Rory Conlin, Gareth Roberg-Clark

**Published:** 2025-02-17

**Category:** physics.plasm-ph

**ID:** 2502.11657v2

**Link:** [http://arxiv.org/abs/2502.11657v2](http://arxiv.org/abs/2502.11657v2)

**Summary:** Magnetic geometry has a significant effect on the level of turbulent
transport in fusion plasmas. Here, we model and analyze this dependence using
multiple machine learning methods and a dataset of > 200,000 nonlinear
simulations of ion-temperature-gradient turbulence in diverse non-axisymmetric
geometries. The dataset is generated using a large collection of both optimized
and randomly generated stellarator equilibria. At fixed gradients, the
turbulent heat flux varies between geometries by several orders of magnitude.
Trends are apparent among the configurations with particularly high or low heat
flux. Regression and classification techniques from machine learning are then
applied to extract patterns in the dataset. Due to a symmetry of the
gyrokinetic equation, the heat flux and regressions thereof should be invariant
to translations of the raw features in the parallel coordinate, similar to
translation invariance in computer vision applications. Multiple regression
models including convolutional neural networks (CNNs) and decision trees can
achieve reasonable predictive power for the heat flux in held-out test
configurations, with highest accuracy for the CNNs. Using Spearman correlation,
sequential feature selection, and Shapley values to measure feature importance,
it is consistently found that the most important geometric lever on the heat
flux is the flux surface compression in regions of bad curvature. The second
most important feature relates to the magnitude of geodesic curvature. These
two features align remarkably with surrogates that have been proposed based on
theory, while the methods here allow a natural extension to more features for
increased accuracy. The dataset, released with this publication, may also be
used to test other proposed surrogates, and we find many previously published
proxies do correlate well with both the heat flux and stability boundary....

---

### 126. Symmetry-Aware GFlowNets

**Authors:** Hohyun Kim, Seunggeun Lee, Min-hwan Oh

**Published:** 2025-06-03

**Category:** stat.ML

**ID:** 2506.02685v1

**Link:** [http://arxiv.org/abs/2506.02685v1](http://arxiv.org/abs/2506.02685v1)

**Summary:** Generative Flow Networks (GFlowNets) offer a powerful framework for sampling
graphs in proportion to their rewards. However, existing approaches suffer from
systematic biases due to inaccuracies in state transition probability
computations. These biases, rooted in the inherent symmetries of graphs, impact
both atom-based and fragment-based generation schemes. To address this
challenge, we introduce Symmetry-Aware GFlowNets (SA-GFN), a method that
incorporates symmetry corrections into the learning process through reward
scaling. By integrating bias correction directly into the reward structure,
SA-GFN eliminates the need for explicit state transition computations.
Empirical results show that SA-GFN enables unbiased sampling while enhancing
diversity and consistently generating high-reward graphs that closely match the
target distribution....

---

### 127. eGAD! double descent is explained by Generalized Aliasing Decomposition

**Authors:** Mark K. Transtrum, Gus L. W. Hart, Tyler J. Jarvis, Jared P. Whitehead

**Published:** 2024-08-15

**Category:** math.ST

**ID:** 2408.08294v4

**Link:** [http://arxiv.org/abs/2408.08294v4](http://arxiv.org/abs/2408.08294v4)

**Summary:** A central problem in data science is to use potentially noisy samples of an
unknown function to predict values for unseen inputs. In classical statistics,
predictive error is understood as a trade-off between the bias and the variance
that balances model simplicity with its ability to fit complex functions.
However, over-parameterized models exhibit counterintuitive behaviors, such as
"double descent" in which models of increasing complexity exhibit decreasing
generalization error. Others may exhibit more complicated patterns of
predictive error with multiple peaks and valleys. Neither double descent nor
multiple descent phenomena are well explained by the bias-variance
decomposition.
  We introduce a novel decomposition that we call the generalized aliasing
decomposition (GAD) to explain the relationship between predictive performance
and model complexity. The GAD decomposes the predictive error into three parts:
1) model insufficiency, which dominates when the number of parameters is much
smaller than the number of data points, 2) data insufficiency, which dominates
when the number of parameters is much greater than the number of data points,
and 3) generalized aliasing, which dominates between these two extremes.
  We demonstrate the applicability of the GAD to diverse applications,
including random feature models from machine learning, Fourier transforms from
signal processing, solution methods for differential equations, and predictive
formation enthalpy in materials discovery. Because key components of the GAD
can be explicitly calculated from the relationship between model class and
samples without seeing any data labels, it can answer questions related to
experimental design and model selection before collecting data or performing
experiments. We further demonstrate this approach on several examples and
discuss implications for predictive modeling and data science....

---

### 128. On Universality Classes of Equivariant Networks

**Authors:** Marco Pacini, Gabriele Santin, Bruno Lepri, Shubhendu Trivedi

**Published:** 2025-06-02

**Category:** cs.LG

**ID:** 2506.02293v1

**Link:** [http://arxiv.org/abs/2506.02293v1](http://arxiv.org/abs/2506.02293v1)

**Summary:** Equivariant neural networks provide a principled framework for incorporating
symmetry into learning architectures and have been extensively analyzed through
the lens of their separation power, that is, the ability to distinguish inputs
modulo symmetry. This notion plays a central role in settings such as graph
learning, where it is often formalized via the Weisfeiler-Leman hierarchy. In
contrast, the universality of equivariant models-their capacity to approximate
target functions-remains comparatively underexplored. In this work, we
investigate the approximation power of equivariant neural networks beyond
separation constraints. We show that separation power does not fully capture
expressivity: models with identical separation power may differ in their
approximation ability. To demonstrate this, we characterize the universality
classes of shallow invariant networks, providing a general framework for
understanding which functions these architectures can approximate. Since
equivariant models reduce to invariant ones under projection, this analysis
yields sufficient conditions under which shallow equivariant networks fail to
be universal. Conversely, we identify settings where shallow models do achieve
separation-constrained universality. These positive results, however, depend
critically on structural properties of the symmetry group, such as the
existence of adequate normal subgroups, which may not hold in important cases
like permutation symmetry....

---

### 129. Exchangeability in Neural Network Architectures and its Application to Dynamic Pruning

**Authors:** Pu, Yi, Tianlang Chen, Yifan Yang, Sara Achour

**Published:** 2025-06-02

**Category:** cs.LG

**ID:** 2506.02210v1

**Link:** [http://arxiv.org/abs/2506.02210v1](http://arxiv.org/abs/2506.02210v1)

**Summary:** Neural networks (NNs) are equipped with increasingly many parameters and
require more and more resource for deployment. Researchers have explored
various ways to improve the efficiency of NNs by identifying and reducing the
redundancy, such as pruning or quantizing unimportant weights. Symmetry in the
NN architectures has been identified by prior work as a possible type of
redundancy, but exploiting it for efficient inference is not yet explored. In
this work, we formalize the symmetry of parameters and intermediate values in
NNs using the statistical property of exchangeablility. We identify that
exchangeable values in NN computation may contain overlapping information,
leading to redundancy. Exploiting the insight, we derive a principled general
dynamic pruning algorithm ExPrune to remove symmetry-induced redundancy on a
per-input basis. We also provide an instantiation of ExPrune that performs
neuron-level dynamic pruning by predicting negative inputs to ReLU activations.
We evaluate ExPrune on two computer vision models, one graph model and one
language model. ExPrune provides 10.98--26.3% reduction in FLOPs with
negligible accuracy drop and 21.01--39.05% reduction in FLOPs with at most 1%
accuracy drop. We also demonstrate that ExPrune composes with static pruning.
On models that have been aggressively pruned statically, ExPrune provides
additional 10.24--11.11% reduction in FLOPs with negligible accuracy drop and
13.91--14.39% reduction in FLOPs with at most 1% accuracy drop....

---

### 130. Strain-Induced Modulation of Spin Splitting and Persistent Spin Textures in Low-Symmetry 2D Hybrid Perovskites: A case study of RP phase

**Authors:** Shantanu Pathak, Saswata Bhattacharya

**Published:** 2025-06-02

**Category:** cond-mat.mtrl-sci

**ID:** 2506.01697v1

**Link:** [http://arxiv.org/abs/2506.01697v1](http://arxiv.org/abs/2506.01697v1)

**Summary:** We report the observation of a persistent spin texture (PST) in pseudo-2D
hybrid perovskite, characterized by significant spin splitting strength on the
order of \(3 \, \text{eV} \cdot \text{\AA}\). Using first-principles density
functional theory (DFT) calculations, complemented by a \(\mathbf{k} \cdot
\mathbf{p}\) model analysis, we validate the presence of PST and its robustness
under various conditions. The material's non-centrosymmetric nature and strong
spin-orbit coupling ensure uniform spin orientation in momentum space, enabling
long spin lifetimes and promising spintronic applications. Furthermore, we
demonstrate the tunability of the spin splitting via the application of
external strain and stress, offering a versatile approach to control spin
configurations. Our results highlight the potential of this perovskite system
for next-generation spintronic devices, where external perturbations can be
used to precisely modulate electronic properties....

---

### 131. Dynamic Modulation of Electronic and Optical Properties in GaN Bilayers by Interlayer Sliding

**Authors:** Heeju Kim, Gunn Kim

**Published:** 2025-01-25

**Category:** cond-mat.mes-hall

**ID:** 2501.15088v2

**Link:** [http://arxiv.org/abs/2501.15088v2](http://arxiv.org/abs/2501.15088v2)

**Summary:** In this study, we present a first-principles investigation of the electronic
and optical properties of gallium nitride (GaN) bilayers, focusing on the
influence of interlayer sliding and spacing. In contrast to the earlier studies
on discrete stacking configurations, we explore the dynamic evolution of the
properties during transitions between stable stacking arrangements. Using
density functional theory calculations, we systematically analyze the impact of
these structural variations on the electronic band structure and optical
absorption spectra of GaN bilayers. The analysis includes both high-symmetry
stacking configurations (AA', AB', and AC') and intermediate states generated
by controlled in-plane atomic displacements, thereby providing a comprehensive
understanding of the property changes associated with interlayer sliding. The
findings of this study provide valuable insights into the potential for tuning
the electronic and optical response of two-dimensional GaN for applications in
nanoscale photonic and electronic devices, where precise control over
interlayer interactions and stacking is crucial....

---

### 132. Learning Abstract World Models with a Group-Structured Latent Space

**Authors:** Thomas Delliaux, Nguyen-Khanh Vu, Vincent François-Lavet, Elise van der Pol, Emmanuel Rachelson

**Published:** 2025-06-02

**Category:** cs.LG

**ID:** 2506.01529v1

**Link:** [http://arxiv.org/abs/2506.01529v1](http://arxiv.org/abs/2506.01529v1)

**Summary:** Learning meaningful abstract models of Markov Decision Processes (MDPs) is
crucial for improving generalization from limited data. In this work, we show
how geometric priors can be imposed on the low-dimensional representation
manifold of a learned transition model. We incorporate known symmetric
structures via appropriate choices of the latent space and the associated group
actions, which encode prior knowledge about invariances in the environment. In
addition, our framework allows the embedding of additional unstructured
information alongside these symmetries. We show experimentally that this leads
to better predictions of the latent transition model than fully unstructured
approaches, as well as better learning on downstream RL tasks, in environments
with rotational and translational features, including in first-person views of
3D environments. Additionally, our experiments show that this leads to simpler
and more disentangled representations. The full code is available on GitHub to
ensure reproducibility....

---

### 133. Generalized many-body exciton g-factors: magnetic hybridization and non-monotonic Rydberg series in monolayer WSe$_2$

**Authors:** Paulo E. Faria Junior, Daniel Hernangómez-Pérez, Tomer Amit, Jaroslav Fabian, Sivan Refaely-Abramson

**Published:** 2025-05-24

**Category:** cond-mat.mes-hall

**ID:** 2505.18468v2

**Link:** [http://arxiv.org/abs/2505.18468v2](http://arxiv.org/abs/2505.18468v2)

**Summary:** Magneto-optics of low dimensional semiconductors, such as monolayer
transition metal dichalcogenides, offers a vast playground for exploring
complex quantum phenomena. However, current ab initio approaches fail to
capture important experimental observations related to brightening of excitonic
levels and their g-factor dependence. Here, we develop a robust and general
first principles framework for many-body exciton g-factors by incorporating
off-diagonal terms for the spin and orbital angular momenta of single-particle
bands and many-body states for magnetic fields pointing in arbitrary spatial
directions. We implement our framework using many-body perturbation theory via
the GW-Bethe-Salpeter equation (BSE) and supplement our analysis with robust
symmetry-based models, establishing a fruitful synergy between many-body GW-BSE
and group theory. Focusing on the archetypal monolayer WSe$_2$, we accurately
reproduce the known results of the low-energy excitons including the Zeeman
splitting and the dark/grey exciton brightening. Furthermore, our theory
naturally reveals fundamental physical mechanisms of magnetic-field
hybridization of higher-energy excitons (s- and p-like) and resolves the
long-standing puzzle of the experimentally measured non-monotonic Rydberg
series (1s-4s) of exciton g-factors. Our framework offers a comprehensive
approach to investigate, rationalize, and predict the non-trivial interplay
between magnetic fields, angular momenta, and many-body exciton physics in van
der Waals systems....

---

### 134. Time inversion symmetry in the Dirac and Schrödinger-Pauli theories

**Authors:** R. Winkler, U. Zülicke

**Published:** 2025-06-02

**Category:** cond-mat.mtrl-sci

**ID:** 2506.01292v1

**Link:** [http://arxiv.org/abs/2506.01292v1](http://arxiv.org/abs/2506.01292v1)

**Summary:** The Schr\"odinger-Pauli theory is generally believed to give a faithful
representation of the nonrelativistic and weakly relativistic limit of the
Dirac theory. However, the Schr\"odinger-Pauli theory is fundamentally
incomplete in its account of broken time inversion symmetry, e.g., in
magnetically ordered systems. In the Dirac theory of the electron, magnetic
order breaks time inversion symmetry even in the nonrelativistic limit, whereas
time inversion symmetry is effectively preserved in the Schr\"odinger-Pauli
theory in the absence of spin-orbit coupling. In the Dirac theory, the Berry
curvature $1/(2m^2c^2)$ is thus an intrinsic property of nonrelativistic
electrons similar to the well-known spin magnetic moment $e\hbar/(2m)$, while
this result is missed by the nonrelativistic or weakly relativistic
Schr\"odinger-Pauli equation. In ferromagnetically ordered systems, the
intrinsic Berry curvature yields a contribution to the anomalous Hall
conductivity independent of spin-orbit coupling....

---

### 135. Probing Equivariance and Symmetry Breaking in Convolutional Networks

**Authors:** Sharvaree Vadgama, Mohammad Mohaiminul Islam, Domas Buracas, Christian Shewmake, Artem Moskalev, Erik Bekkers

**Published:** 2025-01-01

**Category:** cs.CV

**ID:** 2501.01999v3

**Link:** [http://arxiv.org/abs/2501.01999v3](http://arxiv.org/abs/2501.01999v3)

**Summary:** In this work, we explore the trade-offs of explicit structural priors,
particularly group equivariance. We address this through theoretical analysis
and a comprehensive empirical study. To enable controlled and fair comparisons,
we introduce \texttt{Rapidash}, a unified group convolutional architecture that
allows for different variants of equivariant and non-equivariant models. Our
results suggest that more constrained equivariant models outperform less
constrained alternatives when aligned with the geometry of the task, and
increasing representation capacity does not fully eliminate performance gaps.
We see improved performance of models with equivariance and symmetry-breaking
through tasks like segmentation, regression, and generation across diverse
datasets. Explicit \textit{symmetry breaking} via geometric reference frames
consistently improves performance, while \textit{breaking equivariance} through
geometric input features can be helpful when aligned with task geometry. Our
results provide task-specific performance trends that offer a more nuanced way
for model selection....

---

### 136. Probing the Limit of Heat Transfer in Inorganic Crystals with Deep Learning

**Authors:** Jielan Li, Zekun Chen, Qian Wang, Han Yang, Ziheng Lu, Guanzhi Li, Shuizhou Chen, Yu Zhu, Xixian Liu, Junfu Tan, Mingfa Tang, Yichi Zhou, Claudio Zeni, Andrew Fowler, Daniel Zügner, Robert Pinsler, Matthew Horton, Tian Xie, Tie-Yan Liu, Haiguang Liu, Tao Qin, Bing Lv, Davide Donadio, Hongxia Hao

**Published:** 2025-03-14

**Category:** cond-mat.mtrl-sci

**ID:** 2503.11568v2

**Link:** [http://arxiv.org/abs/2503.11568v2](http://arxiv.org/abs/2503.11568v2)

**Summary:** Heat transfer is a fundamental property of matter. Research spanning decades
has attempted to discover materials with exceptional thermal conductivity, yet
the upper limit remains unknown. Using deep learning accelerated crystal
structure prediction and first-principles calculation, we systematically
explore the thermal conductivity landscape of inorganic crystals. We
brute-force over half a million ordered crystalline structures, encompassing an
extensive coverage of local energy minima in binary compounds with up to four
atoms per primitive cell. We confirm diamond sets the upper bound of thermal
conductivity within our search space, very likely also among all stable
crystalline solids at ambient conditions. We also identify over 20 novel
crystals surpassing silicon in thermal conductivity, validated by density
functional theory. These include a semiconductor TaN with ultrahigh thermal
conductivity (~900 $\mathrm{W\cdot m^{-1}\cdot K^{-1}}$), and metallic
compounds such as MnV that exhibit high lattice and electronic thermal
conductivity simultaneously, a distinctive feature not observed before. These
results as well as the deep learning-driven screening method, redefine the
landscape of thermal transport and establish a large open-access database for
future materials discovery....

---

### 137. MOFGPT: Generative Design of Metal-Organic Frameworks using Language Models

**Authors:** Srivathsan Badrinarayanan, Rishikesh Magar, Akshay Antony, Radheesh Sharma Meda, Amir Barati Farimani

**Published:** 2025-05-30

**Category:** cs.LG

**ID:** 2506.00198v1

**Link:** [http://arxiv.org/abs/2506.00198v1](http://arxiv.org/abs/2506.00198v1)

**Summary:** The discovery of Metal-Organic Frameworks (MOFs) with application-specific
properties remains a central challenge in materials chemistry, owing to the
immense size and complexity of their structural design space. Conventional
computational screening techniques such as molecular simulations and density
functional theory (DFT), while accurate, are computationally prohibitive at
scale. Machine learning offers an exciting alternative by leveraging
data-driven approaches to accelerate materials discovery. The complexity of
MOFs, with their extended periodic structures and diverse topologies, creates
both opportunities and challenges for generative modeling approaches. To
address these challenges, we present a reinforcement learning-enhanced,
transformer-based framework for the de novo design of MOFs. Central to our
approach is MOFid, a chemically-informed string representation encoding both
connectivity and topology, enabling scalable generative modeling. Our pipeline
comprises three components: (1) a generative GPT model trained on MOFid
sequences, (2) MOFormer, a transformer-based property predictor, and (3) a
reinforcement learning (RL) module that optimizes generated candidates via
property-guided reward functions. By integrating property feedback into
sequence generation, our method drives the model toward synthesizable,
topologically valid MOFs with desired functional attributes. This work
demonstrates the potential of large language models, when coupled with
reinforcement learning, to accelerate inverse design in reticular chemistry and
unlock new frontiers in computational MOF discovery....

---

### 138. Minimax Rates for the Estimation of Eigenpairs of Weighted Laplace-Beltrami Operators on Manifolds

**Authors:** Nicolás García Trillos, Chenghui Li, Raghavendra Venkatraman

**Published:** 2025-05-30

**Category:** stat.ML

**ID:** 2506.00171v1

**Link:** [http://arxiv.org/abs/2506.00171v1](http://arxiv.org/abs/2506.00171v1)

**Summary:** We study the problem of estimating eigenpairs of elliptic differential
operators from samples of a distribution $\rho$ supported on a manifold $M$.
The operators discussed in the paper are relevant in unsupervised learning and
in particular are obtained by taking suitable scaling limits of widely used
graph Laplacians over data clouds. We study the minimax risk for this eigenpair
estimation problem and explore the rates of approximation that can be achieved
by commonly used graph Laplacians built from random data. More concretely,
assuming that $\rho$ belongs to a certain family of distributions with
controlled second derivatives, and assuming that the $d$-dimensional manifold
$M$ where $\rho$ is supported has bounded geometry, we prove that the
statistical minimax rate for approximating eigenvalues and eigenvectors in the
$H^1(M)$-sense is $n^{-2/(d+4)}$, a rate that matches the minimax rate for a
closely related density estimation problem. We then revisit the literature
studying Laplacians over proximity graphs in the large data limit and prove
that, under slightly stronger regularity assumptions on the data generating
model, eigenpairs of graph Laplacians induce manifold agnostic estimators with
an error of approximation that, up to logarithmic corrections, matches our
lower bounds. Our analysis allows us to expand the existing literature on
graph-based learning in at least two significant ways: 1) we consider stronger
norms to measure the error of approximation than the ones that had been
analyzed in the past; 2) our rates of convergence are uniform over a family of
smooth distributions and do not just apply to densities with special
symmetries, and, as a consequence of our lower bounds, are essentially sharp
when the connectivity of the graph is sufficiently high....

---

### 139. Accurate grain boundary plane distributions for textured microstructures from stereological analysis of orthogonal two-dimensional electron backscatter diffraction orientation maps

**Authors:** Martin Folwarczny, Ao Li, Rushvi Shah, Aaron Chote, Alexandra C. Austin, Yimin Zhu, Gregory S. Rohrer, Michael A. Jackson, Souhardh Kotakadi, Katharina Marquardt

**Published:** 2025-05-30

**Category:** cond-mat.mtrl-sci

**ID:** 2505.24798v1

**Link:** [http://arxiv.org/abs/2505.24798v1](http://arxiv.org/abs/2505.24798v1)

**Summary:** We present a method for obtaining qualitatively accurate grain boundary plane
distributions (GBPD) for textured microstructures using a stereological
calculation applied to two-dimensional electron backscatter diffraction (EBSD)
orientation maps. Stereology, applied to 2D EBSD orientation maps, is currently
the fastest method of obtaining GBPDs. Existing stereological methods are not
directly applicable to textured microstructures because of the biased viewing
perspectives for different grain boundary types supplied from a single planar
orientation map. The method presented in this work successfully removes part of
this bias by combining data from three orthogonal EBSD orientation maps for
stereology. This is shown here to produce qualitatively correct GBPDs for
heavily textured synthetic microstructures with hexagonal and tetragonal
crystal symmetries. Synthetic microstructures were generated to compare the
stereological GBPD to a known ground truth, as the true GBPD could be obtained
from a triangular mesh of the full grain boundary network in 3D. The triangle
mesh data contained all five macroscopic parameters to fully describe the grain
boundary structure. It was observed that our stereological method overestimated
the GBPD anisotropy. However, qualitative analysis of the GBPD remains useful.
Furthermore, it was found that combining data from three orthogonal sections
gives reliable results when sectioning the texture's primary axes....

---

### 140. Modelling bounded rational decision-making through Wasserstein constraints

**Authors:** Benjamin Patrick Evans, Leo Ardon, Sumitra Ganesh

**Published:** 2025-04-01

**Category:** cs.LG

**ID:** 2504.03743v2

**Link:** [http://arxiv.org/abs/2504.03743v2](http://arxiv.org/abs/2504.03743v2)

**Summary:** Modelling bounded rational decision-making through information constrained
processing provides a principled approach for representing departures from
rationality within a reinforcement learning framework, while still treating
decision-making as an optimization process. However, existing approaches are
generally based on Entropy, Kullback-Leibler divergence, or Mutual Information.
In this work, we highlight issues with these approaches when dealing with
ordinal action spaces. Specifically, entropy assumes uniform prior beliefs,
missing the impact of a priori biases on decision-makings. KL-Divergence
addresses this, however, has no notion of "nearness" of actions, and
additionally, has several well known potentially undesirable properties such as
the lack of symmetry, and furthermore, requires the distributions to have the
same support (e.g. positive probability for all actions). Mutual information is
often difficult to estimate. Here, we propose an alternative approach for
modeling bounded rational RL agents utilising Wasserstein distances. This
approach overcomes the aforementioned issues. Crucially, this approach accounts
for the nearness of ordinal actions, modeling "stickiness" in agent decisions
and unlikeliness of rapidly switching to far away actions, while also
supporting low probability actions, zero-support prior distributions, and is
simple to calculate directly....

---

### 141. Epitaxial growth and transport properties of a metallic altermagnet CrSb on a GaAs (001) substrate

**Authors:** Seiji Aota, Masaaki Tanaka

**Published:** 2025-02-12

**Category:** cond-mat.mtrl-sci

**ID:** 2502.08117v2

**Link:** [http://arxiv.org/abs/2502.08117v2](http://arxiv.org/abs/2502.08117v2)

**Summary:** A newly identified class of magnetic materials called altermagnets has
attracted much attention due to the practical properties of spin-splitting
bands akin to ferromagnets and small compensated magnetization akin to
antiferromagnets. These features make them promising candidates for
applications in spintronics devices. Among candidate materials, CrSb is
promising because of its high ordering temperature (~705 K) and large
spin-splitting energy; however, it is predicted that tuning the N\'eel vector
requires additional symmetry breaking or a change in the easy magnetization
axis. While applying epitaxial strain can modulate the symmetry, the selection
of substrates with closely matched lattice constants for heteroepitaxial growth
is limited for altermagnets, which generally have low crystal symmetry.
Therefore, exploring the heteroepitaxial growth of altermagnet thin films on
well-established, dissimilar crystal systems is valuable. (001)-oriented III-V
semiconductors, which share group-V elements with the overgrown CrSb, offer an
ideal platform because they are expected to have material compatibility with
stable interfaces, as well as tunability of the buffer layer's bandgap and
lattice constant by varying the atomic composition of their group-III and
group-V atoms. In this study, we have achieved the molecular beam epitaxial
growth of a CrSb ($\bar{1}10$) thin film on a GaAs (001) substrate by inserting
thin FeSb ($\bar{1}10$) / AlAs (001) buffer layers. The in-plane epitaxial
relationship is found to be CrSb [110] $\|$ GaAs [110] and CrSb [001] $\|$ GaAs
[$\bar{1}10$], and epitaxial strain is also confirmed. We also characterized
the magneto-transport properties of the grown CrSb thin film. Although the
obtained conductivity tensors are mainly explained by a two-carrier model, not
by an anomalous Hall effect, this model reveals the presence of high-mobility
electron and hole carriers....

---

### 142. A Survey of Geometric Graph Neural Networks: Data Structures, Models and Applications

**Authors:** Jiaqi Han, Jiacheng Cen, Liming Wu, Zongzhao Li, Xiangzhe Kong, Rui Jiao, Ziyang Yu, Tingyang Xu, Fandi Wu, Zihe Wang, Hongteng Xu, Zhewei Wei, Deli Zhao, Yang Liu, Yu Rong, Wenbing Huang

**Published:** 2024-03-01

**Category:** cs.LG

**ID:** 2403.00485v3

**Link:** [http://arxiv.org/abs/2403.00485v3](http://arxiv.org/abs/2403.00485v3)

**Summary:** Geometric graphs are a special kind of graph with geometric features, which
are vital to model many scientific problems. Unlike generic graphs, geometric
graphs often exhibit physical symmetries of translations, rotations, and
reflections, making them ineffectively processed by current Graph Neural
Networks (GNNs). To address this issue, researchers proposed a variety of
geometric GNNs equipped with invariant/equivariant properties to better
characterize the geometry and topology of geometric graphs. Given the current
progress in this field, it is imperative to conduct a comprehensive survey of
data structures, models, and applications related to geometric GNNs. In this
paper, based on the necessary but concise mathematical preliminaries, we
formalize geometric graph as the data structure, on top of which we provide a
unified view of existing models from the geometric message passing perspective.
Additionally, we summarize the applications as well as the related datasets to
facilitate later research for methodology development and experimental
evaluation. We also discuss the challenges and future potential directions of
geometric GNNs at the end of this survey....

---

### 143. Line and Planar Defects with Zero Formation Free Energy: Applications of the Phase Rule toward Ripening-Immune Microstructures

**Authors:** Ju Li, Yuri Mishin

**Published:** 2025-05-30

**Category:** cond-mat.mtrl-sci

**ID:** 2505.24092v1

**Link:** [http://arxiv.org/abs/2505.24092v1](http://arxiv.org/abs/2505.24092v1)

**Summary:** Extended one- and two-dimensional defects in crystalline materials are
usually metastable. The thermodynamic ground state of the material is presumed
to be defect-free. Here, we investigate the conditions under which extended
defects, such as grain boundaries, can exist in a multicomponent alloy when the
latter reaches the thermodynamic ground state allowed by the Gibbs phase rule.
We treat all extended defects as low-dimensional phases on the same footing as
the conventional bulk phases. Thermodynamic analysis shows that, in the ground
state, the formation free energies of all extended defects must be zero, and
the system must follow a generalized phase rule. The latter predicts that only
a finite number of symmetry-related defect types can coexist in the material in
the ground state. Guided by the phase rule, we discuss finite-size
polycrystalline and/or polyphase microstructures that are fully immune to
coarsening and their possible transformations....

---

### 144. Recurrent Self-Attention Dynamics: An Energy-Agnostic Perspective from Jacobians

**Authors:** Akiyoshi Tomihari, Ryo Karakida

**Published:** 2025-05-26

**Category:** cs.LG

**ID:** 2505.19458v2

**Link:** [http://arxiv.org/abs/2505.19458v2](http://arxiv.org/abs/2505.19458v2)

**Summary:** The theoretical understanding of self-attention (SA) has been steadily
progressing. A prominent line of work studies a class of SA layers that admit
an energy function decreased by state updates. While it provides valuable
insights into inherent biases in signal propagation, it often relies on
idealized assumptions or additional constraints not necessarily present in
standard SA. Thus, to broaden our understanding, this work aims to relax these
energy constraints and provide an energy-agnostic characterization of inference
dynamics by dynamical systems analysis. In more detail, we first consider
relaxing the symmetry and single-head constraints traditionally required in
energy-based formulations. Next, to investigate more general SA architectures
capable of oscillatory dynamics without necessarily admitting an energy
function, we analyze the Jacobian matrix of the state. We reveal that
normalization layers effectively normalize the Jacobian's complex eigenvalues,
forcing the dynamics close to a critical state. This significantly enhances
inference performance. Furthermore, we utilize the Jacobian perspective to
develop regularization methods for training and a pseudo-energy for monitoring
inference dynamics....

---

### 145. A Flexible, Equivariant Framework for Subgraph GNNs via Graph Products and Graph Coarsening

**Authors:** Guy Bar-Shalom, Yam Eitan, Fabrizio Frasca, Haggai Maron

**Published:** 2024-06-13

**Category:** cs.LG

**ID:** 2406.09291v4

**Link:** [http://arxiv.org/abs/2406.09291v4](http://arxiv.org/abs/2406.09291v4)

**Summary:** Subgraph GNNs enhance message-passing GNNs expressivity by representing
graphs as sets of subgraphs, demonstrating impressive performance across
various tasks. However, their scalability is hindered by the need to process
large numbers of subgraphs. While previous approaches attempted to generate
smaller subsets of subgraphs through random or learnable sampling, these
methods often yielded suboptimal selections or were limited to small subset
sizes, ultimately compromising their effectiveness. This paper introduces a new
Subgraph GNN framework to address these issues. Our approach diverges from most
previous methods by associating subgraphs with node clusters rather than with
individual nodes. We show that the resulting collection of subgraphs can be
viewed as the product of coarsened and original graphs, unveiling a new
connectivity structure on which we perform generalized message passing.
  Crucially, controlling the coarsening function enables meaningful selection
of any number of subgraphs. In addition, we reveal novel permutation symmetries
in the resulting node feature tensor, characterize associated linear
equivariant layers, and integrate them into our Subgraph GNN. We also introduce
novel node marking strategies and provide a theoretical analysis of their
expressive power and other key aspects of our approach. Extensive experiments
on multiple graph learning benchmarks demonstrate that our method is
significantly more flexible than previous approaches, as it can seamlessly
handle any number of subgraphs, while consistently outperforming baseline
approaches. Our code is available at
https://github.com/BarSGuy/Efficient-Subgraph-GNNs....

---

### 146. A Straightforward Gradient-Based Approach for High-Tc Superconductor Design: Leveraging Domain Knowledge via Adaptive Constraints

**Authors:** Akihiro Fujii, Anh Khoa Augustin Lu, Koji Shimizu, Satoshi Watanabe

**Published:** 2024-03-20

**Category:** cond-mat.supr-con

**ID:** 2403.13627v2

**Link:** [http://arxiv.org/abs/2403.13627v2](http://arxiv.org/abs/2403.13627v2)

**Summary:** Materials design aims to discover novel compounds with desired properties.
However, prevailing strategies face critical trade-offs. Conventional
element-substitution approaches readily and adaptively incorporate various
domain knowledge but remain confined to a narrow search space. In contrast,
deep generative models efficiently explore vast compositional landscapes, yet
they struggle to flexibly integrate domain knowledge. To address these
trade-offs, we propose a gradient-based material design framework that combines
these strengths, offering both efficiency and adaptability. In our method,
chemical compositions are optimised to achieve target properties by using
property prediction models and their gradients. In order to seamlessly enforce
diverse constraints, including those reflecting domain insights such as
oxidation states, discretised compositional ratios, types of elements, and
their abundance, we apply masks and employ a special loss function, namely the
integer loss. Furthermore, we initialise the optimisation using promising
candidates from existing dataset, effectively guiding the search away from
unfavourable regions and thus helping to avoid poor solutions. Our approach
demonstrates a more efficient exploration of superconductor candidates,
uncovering candidate materials with higher critical temperature than
conventional element-substitution and generative models. Importantly, it could
propose new compositions beyond those found in existing databases, including
new hydride superconductors absent from the training dataset but which share
compositional similarities with materials found in literature. This synergy of
domain knowledge and machine-learning-based scalability provides a robust
foundation for rapid, adaptive, and comprehensive materials design for
superconductors and beyond....

---

### 147. Rethinking Gradient-Based Methods: Multi-Property Materials Design Beyond Differentiable Targets

**Authors:** Akihiro Fujii, Yoshitaka Ushiku, Koji Shimizu, Anh Khoa Augustin Lu, Satoshi Watanabe

**Published:** 2024-10-11

**Category:** cond-mat.mtrl-sci

**ID:** 2410.08562v4

**Link:** [http://arxiv.org/abs/2410.08562v4](http://arxiv.org/abs/2410.08562v4)

**Summary:** Gradient-based methods offer a simple, efficient strategy for materials
design by directly optimizing candidates using gradients from pretrained
property predictors. However, their use in crystal structure optimization is
hindered by two key challenges: handling non-differentiable constraints, such
as charge neutrality and structural fidelity, and susceptibility to poor local
minima. We revisit and extend the gradient-based methods to address these
issues. We propose Simultaneous Multi-property Optimization using Adaptive
Crystal Synthesizer (SMOACS), which integrates oxidation-number masks and
template-based initialization to enforce non-differentiable constraints, avoid
poor local minima, and flexibly incorporate additional constraints without
retraining. SMOACS enables multi-property optimization. including exceptional
targets such as high-temperature superconductivity, and scales to large crystal
systems, both persistent challenges for generative models, even those enhanced
with gradient-based guidance from property predictors. In experiments on five
target properties and three datasets, SMOACS outperforms generative models and
Bayesian optimization methods, successfully designing 135-atom perovskite
structures that satisfy multiple property targets and constraints, a task at
which the other methods fail entirely....

---

### 148. Nanoscale quantum imaging of field-free deterministic switching of a chiral antiferromagnet

**Authors:** Jingcheng Zhou, Senlei Li, Chuangtang Wang, Hanshang Jin, Stelo Xu, Zelong Xiong, Carson Jacobsen, Kenji Watanabe, Takashi Taniguchi, Valentin Taufour, Liuyan Zhao, Hua Chen, Chunhui Rita Du, Hailong Wang

**Published:** 2025-05-28

**Category:** cond-mat.mtrl-sci

**ID:** 2505.22856v1

**Link:** [http://arxiv.org/abs/2505.22856v1](http://arxiv.org/abs/2505.22856v1)

**Summary:** Recently, unconventional spin-orbit torques (SOTs) with tunable spin
generation open new pathways for designing novel magnetization control for
cutting-edge spintronics innovations. A leading research thrust is to develop
field-free deterministic magnetization switching for implementing scalable and
energy favorable magnetic recording and storage applications, which have been
demonstrated in conventional ferromagnetic and antiferromagnetic material
systems. Here we extend this advanced magnetization control strategy to chiral
antiferromagnet Mn3Sn using spin currents with out-of-plane canted polarization
generated from low-symmetry van der Waals (vdW) material WTe2. Numerical
calculations suggest that damping-like SOT of spins injected perpendicular to
the kagome plane of Mn3Sn serves as a driving force to rotate the chiral
magnetic order, while the field-like SOT of spin currents with polarization
parallel to the kagome plane provides the bipolar deterministicity to the
magnetic switching. We further introduce scanning quantum microscopy to
visualize nanoscale evolutions of Mn3Sn magnetic domains during the field-free
switching process, corroborating the exceptionally large magnetic switching
ratio up to 90%. Our results highlight the opportunities provided by hybrid SOT
material platforms consisting of noncollinear antiferromagnets and low-symmetry
vdW spin source materials for developing next-generation, transformative
spintronic logic devices....

---

### 149. Beyond the Permutation Symmetry of Transformers: The Role of Rotation for Model Fusion

**Authors:** Binchi Zhang, Zaiyi Zheng, Zhengzhang Chen, Jundong Li

**Published:** 2025-02-01

**Category:** cs.LG

**ID:** 2502.00264v2

**Link:** [http://arxiv.org/abs/2502.00264v2](http://arxiv.org/abs/2502.00264v2)

**Summary:** Symmetry in the parameter space of deep neural networks (DNNs) has proven
beneficial for various deep learning applications. A well-known example is the
permutation symmetry in Multi-Layer Perceptrons (MLPs), where permuting the
rows of weight matrices in one layer and applying the inverse permutation to
adjacent layers yields a functionally equivalent model. While permutation
symmetry fully characterizes the equivalence set for MLPs, its discrete nature
limits its utility for transformers. In this paper, we introduce rotation
symmetry, a novel form of parameter space symmetry for transformers that
generalizes permutation symmetry by rotating parameter matrices in
self-attention layers. Unlike permutation symmetry, rotation symmetry operates
in a continuous domain, thereby significantly expanding the equivalence set for
transformers. Based on this property, we propose a theoretically optimal
parameter matching algorithm as a plug-and-play module to enhance model fusion.
We evaluate our approach using pre-trained transformers across diverse natural
language and vision tasks. Experimental results demonstrate that our rotation
symmetry-based matching algorithm substantially improves model fusion,
highlighting the potential of parameter space symmetry to facilitate model
fusion. Our code is available on
https://github.com/zhengzaiyi/RotationSymmetry....

---

### 150. Improper flexoelectricity in hexagonal rare-earth ferrites

**Authors:** Xin Li, Guodong Ren, Yu Yun, Arashdeep Singh Thind, Amit Kumar Shah, Abbey Bowers, Rohan Mishra, Xiaoshan Xu

**Published:** 2024-09-25

**Category:** cond-mat.mtrl-sci

**ID:** 2409.17022v2

**Link:** [http://arxiv.org/abs/2409.17022v2](http://arxiv.org/abs/2409.17022v2)

**Summary:** Flexoelectricity is a universal effect that generates electric polarization
due to broken inversion symmetry caused by local strain gradient. The large
strain gradient at nanoscale makes flexo-electric effects, especially in
nanoscopic ferroelectric materials, promising in sensors, actuator, energy
harvesting, and memory applications. In this work, we studied flexoelectricity
in hexagonal ferrites h-YbFeO3, an improper ferroelectric expected to have weak
piezoelectricity and low sensitivity to depolarization field, which are
advantageous for studying flexoelectric effects. We show that in h-YbFeO3
epitaxial thin films, strain gradient on the order of 10^6 m-1 occurs near
grain boundaries and edge dislocation, which has a significant impact on the
non-polar K3 structural distortion that induces spontaneous polarization. The
phenomenological model based on the Landau theory of improper ferroelectricity
suggests an indirect flexoelectric effect on the order of 10 nC/m in h-YbFeO3,
which is substantially larger than the expectation from Kogan mechanism. These
results reveal a novel microscopic mechanism of coupling between strain
gradient and polarization mediated by structural distortion, which we call
improper flexoelectricity....

---

### 151. Lattice Compatibility and Energy Barriers in Intercalation Compounds

**Authors:** Delin Zhang, Ananya Renuka Balakrishna

**Published:** 2025-05-28

**Category:** cond-mat.mtrl-sci

**ID:** 2505.22628v1

**Link:** [http://arxiv.org/abs/2505.22628v1](http://arxiv.org/abs/2505.22628v1)

**Summary:** We present a continuum model for symmetry-breaking phase transformations in
intercalation compounds, based on Ericksen's multi-well energy formulation. The
model predicts the nucleation and growth of crystallographic microstructures in
Li$_{2}$Mn$_{2}$O$_{4}$ -- a representative intercalation compound -- with twin
boundary orientations and volume fractions that closely match experimental
observations. Our chemo-mechanically coupled model not only generates
geometrically accurate microstructures through energy minimization, but also
reveals a subtle interplay between twinned domains and electro-chemo-mechanical
behavior. A key finding is that intercalation compounds satisfying specific
compatibility conditions (e.g., $\lambda_{2} = 1$ or $|\det \mathbf{U} - 1| =
0)$ show lower elastic energy barriers, require smaller driving forces, and
display narrower voltage hysteresis loops. Furthermore, we show that twinned
domains act as conduits for fast Li-diffusion. These results establish
quantitative design guidelines for intercalation compounds, which focuses on
tailoring lattice deformations (rather than suppressing them) and reducing
energy barriers to mitigate structural degradation and enhance the
electrochemical performance of battery electrodes....

---

### 152. Adjoint Sampling: Highly Scalable Diffusion Samplers via Adjoint Matching

**Authors:** Aaron Havens, Benjamin Kurt Miller, Bing Yan, Carles Domingo-Enrich, Anuroop Sriram, Brandon Wood, Daniel Levine, Bin Hu, Brandon Amos, Brian Karrer, Xiang Fu, Guan-Horng Liu, Ricky T. Q. Chen

**Published:** 2025-04-16

**Category:** cs.LG

**ID:** 2504.11713v3

**Link:** [http://arxiv.org/abs/2504.11713v3](http://arxiv.org/abs/2504.11713v3)

**Summary:** We introduce Adjoint Sampling, a highly scalable and efficient algorithm for
learning diffusion processes that sample from unnormalized densities, or energy
functions. It is the first on-policy approach that allows significantly more
gradient updates than the number of energy evaluations and model samples,
allowing us to scale to much larger problem settings than previously explored
by similar methods. Our framework is theoretically grounded in stochastic
optimal control and shares the same theoretical guarantees as Adjoint Matching,
being able to train without the need for corrective measures that push samples
towards the target distribution. We show how to incorporate key symmetries, as
well as periodic boundary conditions, for modeling molecules in both cartesian
and torsional coordinates. We demonstrate the effectiveness of our approach
through extensive experiments on classical energy functions, and further scale
up to neural network-based energy models where we perform amortized conformer
generation across many molecular systems. To encourage further research in
developing highly scalable sampling methods, we plan to open source these
challenging benchmarks, where successful methods can directly impact progress
in computational chemistry....

---

### 153. Direct ab initio calculation of magnons in altermagnets: method, spin-space symmetry aspects, and application to MnTe

**Authors:** L. M. Sandratskii, K. Carva, V. M. Silkin

**Published:** 2025-01-20

**Category:** cond-mat.mtrl-sci

**ID:** 2501.11327v2

**Link:** [http://arxiv.org/abs/2501.11327v2](http://arxiv.org/abs/2501.11327v2)

**Summary:** We suggest the method for direct ab initio calculation of magnons in complex
collinear magnets. The method is based on the density-functional-theory
calculation under two different constraints: one constraint governs the change
of the magnetization with respect to the ground state, and the other is the
symmetry constraint responsible for the value of the magnon wave vector. The
performance of the method is demonstrated by the application to an altermagnet
MnTe. An important role in both the formulation and the application of the
method play the aspects of generalized symmetry described by the spin-space
groups. The symmetry analysis connects in one coherent picture the following
three parts of the consideration: (i) the generalized translational symmetry of
the magnons as a crucial condition for their efficient ab-initio calculation,
(ii) altermagnetic spin-splitting of the electron states in the ground magnetic
state, and (iii) chirality splitting of the magnon excitations. It is
demonstrated that both the spin splitting of the electron states and the
chirality splitting of the magnons have identical patterns in the corresponding
wave vector spaces. Since the altermagnetism of MnTe is the consequence of the
presence of the Te atoms, an adequate attention is devoted to the symmetry
analysis and calculation results for the Te moments induced in the magnon
states. The knowledge of the symmetry properties of the Te moments allows to
accelerate the numerical convergence of the magnon states and serves as a test
for the accuracy of the calculations. To expose the connection between electron
band structures of the magnon states of the system and the chirality properties
of these states we investigate the transformation of the electron structure in
the transition from the collinear ground state to a noncollinear magnon state....

---

### 154. Systematic generation of electron models for Second-Principles Density Functional Theory Methods

**Authors:** Nayara Carral-Sainz, Toraya Fernández-Ruiz, Jorge Íñiguez, Javier Junquera, Pablo Garcia-Fernandez

**Published:** 2025-05-28

**Category:** cond-mat.mtrl-sci

**ID:** 2505.22056v1

**Link:** [http://arxiv.org/abs/2505.22056v1](http://arxiv.org/abs/2505.22056v1)

**Summary:** We present a systematic, quasi-automated methodology for generating
electronic models in the framework of second-principles density functional
theory (SPDFT). This approach enables the construction of accurate and
computationally efficient models by deriving all necessary parameters from
first-principles calculations on a carefully designed training set. A key
feature of our method is the enforcement of space group symmetries, which
reduces both the number of independent parameters and the required
computational effort. The formalism includes improved treatments of
one-electron Hamiltonians, electron-lattice coupling-through both linear and
quadratic terms-and electron-electron interactions, enabling accurate modeling
of structural and electronic responses. We apply the methodology to SrTiO$_{3}$
and LiF, materials representative of transition-metal perovskites and
wide-band-gap insulators, respectively. In both cases, the resulting models
reproduce DFT reference data with high fidelity across various atomic
configurations and charge states. Our results validate the robustness of the
approach and highlight its potential for simulating complex phenomena such as
polarons and excitons. This work lays the foundation for extending SPDFT to
real-time simulations of optoelectronic properties and further integration with
machine-learning methods....

---

### 155. Efficient Diffusion Models for Symmetric Manifolds

**Authors:** Oren Mangoubi, Neil He, Nisheeth K. Vishnoi

**Published:** 2025-05-27

**Category:** cs.LG

**ID:** 2505.21640v1

**Link:** [http://arxiv.org/abs/2505.21640v1](http://arxiv.org/abs/2505.21640v1)

**Summary:** We introduce a framework for designing efficient diffusion models for
$d$-dimensional symmetric-space Riemannian manifolds, including the torus,
sphere, special orthogonal group and unitary group. Existing manifold diffusion
models often depend on heat kernels, which lack closed-form expressions and
require either $d$ gradient evaluations or exponential-in-$d$ arithmetic
operations per training step. We introduce a new diffusion model for symmetric
manifolds with a spatially-varying covariance, allowing us to leverage a
projection of Euclidean Brownian motion to bypass heat kernel computations. Our
training algorithm minimizes a novel efficient objective derived via Ito's
Lemma, allowing each step to run in $O(1)$ gradient evaluations and
nearly-linear-in-$d$ ($O(d^{1.19})$) arithmetic operations, reducing the gap
between diffusions on symmetric manifolds and Euclidean space. Manifold
symmetries ensure the diffusion satisfies an "average-case" Lipschitz
condition, enabling accurate and efficient sample generation. Empirically, our
model outperforms prior methods in training speed and improves sample quality
on synthetic datasets on the torus, special orthogonal group, and unitary
group....

---

### 156. Equivariant Representation Learning for Symmetry-Aware Inference with Guarantees

**Authors:** Daniel Ordoñez-Apraez, Vladimir Kostić, Alek Fröhlich, Vivien Brandt, Karim Lounici, Massimiliano Pontil

**Published:** 2025-05-26

**Category:** cs.LG

**ID:** 2505.19809v2

**Link:** [http://arxiv.org/abs/2505.19809v2](http://arxiv.org/abs/2505.19809v2)

**Summary:** In many real-world applications of regression, conditional probability
estimation, and uncertainty quantification, exploiting symmetries rooted in
physics or geometry can dramatically improve generalization and sample
efficiency. While geometric deep learning has made significant empirical
advances by incorporating group-theoretic structure, less attention has been
given to statistical learning guarantees. In this paper, we introduce an
equivariant representation learning framework that simultaneously addresses
regression, conditional probability estimation, and uncertainty quantification
while providing first-of-its-kind non-asymptotic statistical learning
guarantees. Grounded in operator and group representation theory, our framework
approximates the spectral decomposition of the conditional expectation
operator, building representations that are both equivariant and disentangled
along independent symmetry subgroups. Empirical evaluations on synthetic
datasets and real-world robotics applications confirm the potential of our
approach, matching or outperforming existing equivariant baselines in
regression while additionally providing well-calibrated parametric uncertainty
estimates....

---

### 157. One-Time Soft Alignment Enables Resilient Learning without Weight Transport

**Authors:** Jeonghwan Cheon, Jaehyuk Bae, Se-Bum Paik

**Published:** 2025-05-27

**Category:** cs.LG

**ID:** 2505.20892v1

**Link:** [http://arxiv.org/abs/2505.20892v1](http://arxiv.org/abs/2505.20892v1)

**Summary:** Backpropagation is the cornerstone of deep learning, but its reliance on
symmetric weight transport and global synchronization makes it computationally
expensive and biologically implausible. Feedback alignment offers a promising
alternative by approximating error gradients through fixed random feedback,
thereby avoiding symmetric weight transport. However, this approach often
struggles with poor learning performance and instability, especially in deep
networks. Here, we show that a one-time soft alignment between forward and
feedback weights at initialization enables deep networks to achieve performance
comparable to backpropagation, without requiring weight transport during
learning. This simple initialization condition guides stable error minimization
in the loss landscape, improving network trainability. Spectral analyses
further reveal that initial alignment promotes smoother gradient flow and
convergence to flatter minima, resulting in better generalization and
robustness. Notably, we also find that allowing moderate deviations from exact
weight symmetry can improve adversarial robustness compared to standard
backpropagation. These findings demonstrate that a simple initialization
strategy can enable effective learning in deep networks in a biologically
plausible and resource-efficient manner....

---

### 158. Machine Learning - Driven Materials Discovery: Unlocking Next-Generation Functional Materials -- A minireview

**Authors:** Dilshod Nematov, Mirabbos Hojamberdiev

**Published:** 2025-03-22

**Category:** cond-mat.mtrl-sci

**ID:** 2503.18975v2

**Link:** [http://arxiv.org/abs/2503.18975v2](http://arxiv.org/abs/2503.18975v2)

**Summary:** The rapid advancement of machine learning and artificial intelligence
(AI)-driven techniques is revolutionizing materials discovery, property
prediction, and material design by minimizing human intervention and
accelerating scientific progress. This review provides a comprehensive overview
of smart, machine learning (ML)-driven approaches, emphasizing their role in
predicting material properties, discovering novel compounds, and optimizing
material structures. Key methodologies ranging from deep learning, graph neural
networks, and Bayesian optimization to automated generative models, such as
generative adversarial networks (GANs) and variational autoencoders (VAEs)
enable the autonomous design of materials with tailored functionalities. By
leveraging AutoML frameworks (e.g., AutoGluon, TPOT, and H2O.ai), researchers
can automate the model selection, hyperparameter tuning, and feature
engineering, significantly improving the efficiency of materials informatics.
Furthermore, the integration of AI-driven robotic laboratories and
high-throughput computing has established a fully automated pipeline for rapid
synthesis and experimental validation, drastically reducing the time and cost
of material discovery. This review highlights real-world applications of
automated ML-driven approaches in predicting mechanical, thermal, electrical,
and optical properties of materials, demonstrating successful cases in
superconductors, catalysts, photovoltaics, and energy storage systems. We also
address key challenges, such as data quality, interpretability, and the
integration of AutoML with quantum computing, which are essential for future
advancements. Ultimately, the synergy between AI, automated experimentation,
and computational modeling transforms the way the materials are discovered,
optimized, and designed, paving the way for next-generation innovations in
energy, electronics, and nanotechnology....

---

### 159. A Generation Framework with Strict Constraints for Crystal Materials Design

**Authors:** Chao Huang, Jiahui Chen, Chen Chen, Chunyan Chen, Renjie Su, Shiyu Du, ChenChen, Hongrui Liang, Daojing Lin

**Published:** 2024-11-13

**Category:** cs.AI

**ID:** 2411.08464v2

**Link:** [http://arxiv.org/abs/2411.08464v2](http://arxiv.org/abs/2411.08464v2)

**Summary:** The design of crystal materials plays a critical role in areas such as new
energy development, biomedical engineering, and semiconductors. Recent advances
in data-driven methods have enabled the generation of diverse crystal
structures. However, most existing approaches still rely on random sampling
without strict constraints, requiring multiple post-processing steps to
identify stable candidates with the desired physical and chemical properties.
In this work, we present a new constrained generation framework that takes
multiple constraints as input and enables the generation of crystal structures
with specific chemical and properties. In this framework, intermediate
constraints, such as symmetry information and composition ratio, are generated
by a constraint generator based on large language models (LLMs), which
considers the target properties. These constraints are then used by a
subsequent crystal structure generator to ensure that the structure generation
process is under control. Our method generates crystal structures with a
probability of meeting the target properties that is more than twice that of
existing approaches. Furthermore, nearly 100% of the generated crystals
strictly adhere to predefined chemical composition, eliminating the risks of
supply chain during production....

---

### 160. teMatDb: A High-Quality Thermoelectric Material Database with Self-Consistent ZT Filtering

**Authors:** Byungki Ryu, Ji Hui Son, Sungjin Park, Jaywan Chung, Hye-Jin Lim, SuJi Park, Yujeong Do, SuDong Park

**Published:** 2025-05-25

**Category:** cond-mat.mtrl-sci

**ID:** 2505.19150v2

**Link:** [http://arxiv.org/abs/2505.19150v2](http://arxiv.org/abs/2505.19150v2)

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

### 161. Nonlinear Transport Signatures of Hidden Symmetry Breaking in a Weyl Altermagnet

**Authors:** Yufei Zhao, Zhiqiang Mao, Binghai Yan

**Published:** 2025-05-27

**Category:** cond-mat.mtrl-sci

**ID:** 2505.20603v1

**Link:** [http://arxiv.org/abs/2505.20603v1](http://arxiv.org/abs/2505.20603v1)

**Summary:** Phase transitions in solids are often accompanied by structural changes, but
subtle lattice distortions can remain hidden from conventional crystallographic
probes, hindering the identification of the correct order parameters. A case in
point is Ca$_3$Ru$_2$O$_7$, a correlated polar ruthenate with
well-characterized phase transitions, whose ground state structure has recently
become a subject of debate. This uncertainty stems from extremely small atomic
displacements ($\sim$0.001 \AA) between competing phases, beyond the resolution
of X-ray diffraction, neutron scattering, or optical second-harmonic
generation. In this work, we propose a method to detect hidden symmetry
breaking by leveraging nonlinear transport induced by quantum geometry. We show
that Ca$_3$Ru$_2$O$_7$ is a Weyl chain semimetal in both phases. The
low-symmetry phase, classified as an altermagnet by symmetry, features
distorted topological surface states that are asymmetric along the polar ($b$)
axis. However, the nonrelativistic spin splitting is too weak ($\sim$0.1 meV)
to be resolved directly, regarding the altermagnetism. In contrast, Weyl chains
generate a large quantum metric at the Fermi surface, leading to nonlinear
conductivities that are orders of magnitude stronger in the low-symmetry phase.
A longitudinal nonlinear conductivity along the polar axis emerges exclusively
in this phase, providing a sensitive probe to qualitatively distinguish it from
the high-symmetry structure and demonstrate the emergence of altermangetism,
which is confirmed by a recent experiment. Our work establishes a route for
identifying hidden symmetry breaking in complex quantum materials through the
interplay of crystal symmetry, topology and nonlinear quantum transport....

---

### 162. Symmetry constrained neural networks for detection and localization of damage in metal plates

**Authors:** James Amarel, Christopher Rudolf, Athanasios Iliopoulos, John Michopoulos, Leslie N. Smith

**Published:** 2024-09-09

**Category:** cs.LG

**ID:** 2409.06084v3

**Link:** [http://arxiv.org/abs/2409.06084v3](http://arxiv.org/abs/2409.06084v3)

**Summary:** The present paper is concerned with deep learning techniques applied to
detection and localization of damage in a thin aluminum plate. We used data
collected on a tabletop apparatus by mounting to the plate four piezoelectric
transducers, each of which took turn to generate a Lamb wave that then
traversed the region of interest before being received by the remaining three
sensors. On training a neural network to analyze time-series data of the
material response, which displayed damage-reflective features whenever the
plate guided waves interacted with a contact load, we achieved a model that
detected with greater than $99\%$ accuracy in addition to a model that
localized with $2.58 \pm 0.12$ mm mean distance error. For each task, the
best-performing model was designed according to the inductive bias that our
transducers were both similar and arranged in a square pattern on a nearly
uniform plate....

---

### 163. Symmetries in Overparametrized Neural Networks: A Mean-Field View

**Authors:** Javier Maass, Joaquin Fontbona

**Published:** 2024-05-30

**Category:** stat.ML

**ID:** 2405.19995v3

**Link:** [http://arxiv.org/abs/2405.19995v3](http://arxiv.org/abs/2405.19995v3)

**Summary:** We develop a Mean-Field (MF) view of the learning dynamics of
overparametrized Artificial Neural Networks (NN) under data symmetric in law
wrt the action of a general compact group $G$. We consider for this a class of
generalized shallow NNs given by an ensemble of $N$ multi-layer units, jointly
trained using stochastic gradient descent (SGD) and possibly
symmetry-leveraging (SL) techniques, such as Data Augmentation (DA), Feature
Averaging (FA) or Equivariant Architectures (EA). We introduce the notions of
weakly and strongly invariant laws (WI and SI) on the parameter space of each
single unit, corresponding, respectively, to $G$-invariant distributions, and
to distributions supported on parameters fixed by the group action (which
encode EA). This allows us to define symmetric models compatible with taking
$N\to\infty$ and give an interpretation of the asymptotic dynamics of DA, FA
and EA in terms of Wasserstein Gradient Flows describing their MF limits. When
activations respect the group action, we show that, for symmetric data, DA, FA
and freely-trained models obey the exact same MF dynamic, which stays in the
space of WI laws and minimizes therein the population risk. We also give a
counterexample to the general attainability of an optimum over SI laws. Despite
this, quite remarkably, we show that the set of SI laws is also preserved by
the MF dynamics even when freely trained. This sharply contrasts the finite-$N$
setting, in which EAs are generally not preserved by unconstrained SGD. We
illustrate the validity of our findings as $N$ gets larger in a teacher-student
experimental setting, training a student NN to learn from a WI, SI or arbitrary
teacher model through various SL schemes. We last deduce a data-driven
heuristic to discover the largest subspace of parameters supporting SI
distributions for a problem, that could be used for designing EA with minimal
generalization error....

---

### 164. PointOBB-v3: Expanding Performance Boundaries of Single Point-Supervised Oriented Object Detection

**Authors:** Peiyuan Zhang, Junwei Luo, Xue Yang, Yi Yu, Qingyun Li, Yue Zhou, Xiaosong Jia, Xudong Lu, Jingdong Chen, Xiang Li, Junchi Yan, Yansheng Li

**Published:** 2025-01-23

**Category:** cs.CV

**ID:** 2501.13898v2

**Link:** [http://arxiv.org/abs/2501.13898v2](http://arxiv.org/abs/2501.13898v2)

**Summary:** With the growing demand for oriented object detection (OOD), recent studies
on point-supervised OOD have attracted significant interest. In this paper, we
propose PointOBB-v3, a stronger single point-supervised OOD framework. Compared
to existing methods, it generates pseudo rotated boxes without additional
priors and incorporates support for the end-to-end paradigm. PointOBB-v3
functions by integrating three unique image views: the original view, a resized
view, and a rotated/flipped (rot/flp) view. Based on the views, a scale
augmentation module and an angle acquisition module are constructed. In the
first module, a Scale-Sensitive Consistency (SSC) loss and a Scale-Sensitive
Feature Fusion (SSFF) module are introduced to improve the model's ability to
estimate object scale. To achieve precise angle predictions, the second module
employs symmetry-based self-supervised learning. Additionally, we introduce an
end-to-end version that eliminates the pseudo-label generation process by
integrating a detector branch and introduces an Instance-Aware Weighting (IAW)
strategy to focus on high-quality predictions. We conducted extensive
experiments on the DIOR-R, DOTA-v1.0/v1.5/v2.0, FAIR1M, STAR, and RSAR
datasets. Across all these datasets, our method achieves an average improvement
in accuracy of 3.56% in comparison to previous state-of-the-art methods. The
code will be available at https://github.com/ZpyWHU/PointOBB-v3....

---

### 165. G-type Antiferromagnetic BiFeO$_3$ is a Multiferroic $g$-wave Altermagnet

**Authors:** Andrea Urru, Daniel Seleznev, Yujia Teng, Se Young Park, Sebastian E. Reyes-Lillo, Karin M. Rabe

**Published:** 2025-05-25

**Category:** cond-mat.mtrl-sci

**ID:** 2505.18965v1

**Link:** [http://arxiv.org/abs/2505.18965v1](http://arxiv.org/abs/2505.18965v1)

**Summary:** G-type antiferromagnetic BiFeO$_3$ is shown to be an altermagnet. We present
the band structure using an unconventional scheme designed to highlight the
distinctive spin splitting which is characteristic of altermagnets. We define
and show plots of the spin-splitting function in reciprocal space. We show that
the nodal surfaces of the spin-splitting function that follow from symmetry can
be classified into two types, which we call symmetry-enforced and
continuity-enforced. We describe the spin-splitting function with a simple
parametrization in a basis of symmetry-adapted plane waves. Using group-theory
analysis based on irreducible representations of the crystallographic Laue
group, we confirm that the altermagnetism of G-type BiFeO$_3$ is $g$-wave and
present a complete classification table for the general three-dimensional case.
Finally, we discuss the effect of ferroelectric switching on the altermagnetic
order, and identify three classes of ferroelectric altermagnets....

---

### 166. High-order Equivariant Flow Matching for Density Functional Theory Hamiltonian Prediction

**Authors:** Seongsu Kim, Nayoung Kim, Dongwoo Kim, Sungsoo Ahn

**Published:** 2025-05-24

**Category:** physics.comp-ph

**ID:** 2505.18817v1

**Link:** [http://arxiv.org/abs/2505.18817v1](http://arxiv.org/abs/2505.18817v1)

**Summary:** Density functional theory (DFT) is a fundamental method for simulating
quantum chemical properties, but it remains expensive due to the iterative
self-consistent field (SCF) process required to solve the Kohn-Sham equations.
Recently, deep learning methods are gaining attention as a way to bypass this
step by directly predicting the Hamiltonian. However, they rely on
deterministic regression and do not consider the highly structured nature of
Hamiltonians. In this work, we propose QHFlow, a high-order equivariant flow
matching framework that generates Hamiltonian matrices conditioned on molecular
geometry. Flow matching models continuous-time trajectories between simple
priors and complex targets, learning the structured distributions over
Hamiltonians instead of direct regression. To further incorporate symmetry, we
use a neural architecture that predicts SE(3)-equivariant vector fields,
improving accuracy and generalization across diverse geometries. To further
enhance physical fidelity, we additionally introduce a fine-tuning scheme to
align predicted orbital energies with the target. QHFlow achieves
state-of-the-art performance, reducing Hamiltonian error by 71% on MD17 and 53%
on QH9. Moreover, we further show that QHFlow accelerates the DFT process
without trading off the solution quality when initializing SCF iterations with
the predicted Hamiltonian, significantly reducing the number of iterations and
runtime....

---

### 167. Governing Equation Discovery from Data Based on Differential Invariants

**Authors:** Lexiang Hu, Yikang Li, Zhouchen Lin

**Published:** 2025-05-24

**Category:** cs.LG

**ID:** 2505.18798v1

**Link:** [http://arxiv.org/abs/2505.18798v1](http://arxiv.org/abs/2505.18798v1)

**Summary:** The explicit governing equation is one of the simplest and most intuitive
forms for characterizing physical laws. However, directly discovering partial
differential equations (PDEs) from data poses significant challenges, primarily
in determining relevant terms from a vast search space. Symmetry, as a crucial
prior knowledge in scientific fields, has been widely applied in tasks such as
designing equivariant networks and guiding neural PDE solvers. In this paper,
we propose a pipeline for governing equation discovery based on differential
invariants, which can losslessly reduce the search space of existing equation
discovery methods while strictly adhering to symmetry. Specifically, we compute
the set of differential invariants corresponding to the infinitesimal
generators of the symmetry group and select them as the relevant terms for
equation discovery. Taking DI-SINDy (SINDy based on Differential Invariants) as
an example, we demonstrate that its success rate and accuracy in PDE discovery
surpass those of other symmetry-informed governing equation discovery methods
across a series of PDEs....

---

### 168. Flow Matching for Geometric Trajectory Simulation

**Authors:** Kiet Bennema ten Brinke, Koen Minartz, Vlado Menkovski

**Published:** 2025-05-24

**Category:** cs.LG

**ID:** 2505.18647v1

**Link:** [http://arxiv.org/abs/2505.18647v1](http://arxiv.org/abs/2505.18647v1)

**Summary:** The simulation of N-body systems is a fundamental problem with applications
in a wide range of fields, such as molecular dynamics, biochemistry, and
pedestrian dynamics. Machine learning has become an invaluable tool for scaling
physics-based simulators and developing models directly from experimental data.
In particular, recent advances based on deep generative modeling and geometric
deep learning have enabled probabilistic simulation by modeling complex
distributions over trajectories while respecting the permutation symmetry that
is fundamental to N-body systems. However, to generate realistic trajectories,
existing methods must learn complex transformations starting from uninformed
noise and do not allow for the exploitation of domain-informed priors. In this
work, we propose STFlow to address this limitation. By leveraging flow matching
and data-dependent couplings, STFlow facilitates physics-informed simulation of
geometric trajectories without sacrificing model expressivity or scalability.
Our evaluation on N-body dynamical systems, molecular dynamics, and pedestrian
dynamics benchmarks shows that STFlow produces significantly lower prediction
errors while enabling more efficient inference, highlighting the benefits of
employing physics-informed prior distributions in probabilistic geometric
trajectory modeling....

---

### 169. AI-predicted PT-symmetric magnets

**Authors:** Hao Wu, Daniel F. Agterberg

**Published:** 2025-05-24

**Category:** cond-mat.mtrl-sci

**ID:** 2505.18620v1

**Link:** [http://arxiv.org/abs/2505.18620v1](http://arxiv.org/abs/2505.18620v1)

**Summary:** Parity-time-reversal-symmetric odd-parity antiferromagnetic (AFM1) materials
are of interest for their symmetry-enabled quantum transport and optical
effects. These materials host odd-parity terms in their band dispersion,
leading to asymmetric energy bands and enabling responses such as the
magnetopiezoelectric effect, nonreciprocal conductivity, and photocurrent
generation. In addition, they may support a nonlinear spin Hall effect without
spin-orbit coupling, offering an efficient route to spin current generation. We
identify 23 candidate AFM1 materials by combining artificial intelligence,
density functional theory (DFT), and symmetry analysis. Using a graph neural
network model and incorporating AFM1-specific symmetry constraints, we screen
Materials Project compounds for high-probability AFM1 candidates. DFT
calculations show that AFM1 has the lowest energy among the tested magnetic
configurations in 23 candidate materials. These include 3 experimentally
verified AFM1 materials, 10 synthesized compounds with unknown magnetic
structures, and 10 that are not yet synthesized....

---

### 170. MolMiner: Towards Controllable, 3D-Aware, Fragment-Based Molecular Design

**Authors:** Raul Ortega-Ochoa, Tejs Vegge, Jes Frellsen

**Published:** 2024-11-10

**Category:** cs.LG

**ID:** 2411.06608v2

**Link:** [http://arxiv.org/abs/2411.06608v2](http://arxiv.org/abs/2411.06608v2)

**Summary:** We introduce MolMiner, a fragment-based, geometry-aware, and order-agnostic
autoregressive model for molecular design. MolMiner supports conditional
generation of molecules over twelve properties, enabling flexible control
across physicochemical and structural targets. Molecules are built via
symmetry-aware fragment attachments, with 3D geometry dynamically updated
during generation using forcefields. A probabilistic conditioning mechanism
allows users to specify any subset of target properties while sampling the
rest. MolMiner achieves calibrated conditional generation across most
properties and offers competitive unconditional performance. We also propose
improved benchmarking methods for both unconditional and conditional
generation, including distributional comparisons via Wasserstein distance and
calibration plots for property control. To our knowledge, this is the first
model to unify dynamic geometry, symmetry handling, order-agnostic
fragment-based generation, and high-dimensional multi-property conditioning....

---

### 171. SymmCD: Symmetry-Preserving Crystal Generation with Diffusion Models

**Authors:** Daniel Levy, Siba Smarak Panigrahi, Sékou-Oumar Kaba, Qiang Zhu, Kin Long Kelvin Lee, Mikhail Galkin, Santiago Miret, Siamak Ravanbakhsh

**Published:** 2025-02-05

**Category:** cond-mat.mtrl-sci

**ID:** 2502.03638v3

**Link:** [http://arxiv.org/abs/2502.03638v3](http://arxiv.org/abs/2502.03638v3)

**Summary:** Generating novel crystalline materials has the potential to lead to
advancements in fields such as electronics, energy storage, and catalysis. The
defining characteristic of crystals is their symmetry, which plays a central
role in determining their physical properties. However, existing crystal
generation methods either fail to generate materials that display the
symmetries of real-world crystals, or simply replicate the symmetry information
from examples in a database. To address this limitation, we propose SymmCD, a
novel diffusion-based generative model that explicitly incorporates
crystallographic symmetry into the generative process. We decompose crystals
into two components and learn their joint distribution through diffusion: 1)
the asymmetric unit, the smallest subset of the crystal which can generate the
whole crystal through symmetry transformations, and; 2) the symmetry
transformations needed to be applied to each atom in the asymmetric unit. We
also use a novel and interpretable representation for these transformations,
enabling generalization across different crystallographic symmetry groups. We
showcase the competitive performance of SymmCD on a subset of the Materials
Project, obtaining diverse and valid crystals with realistic symmetries and
predicted properties....

---

### 172. Light-induced inverse spin Hall effect and field-induced circular photogalvanic effect in GaAs revealed by two-dimensional terahertz Fourier analysis

**Authors:** Tomohiro Fujimoto, Yuta Murotani, Tomohiro Tamaya, Takayuki Kurihara, Natsuki Kanda, Changsu Kim, Jun Yoshinobu, Hidefumi Akiyama, Takeo Kato, Ryusuke Matsunaga

**Published:** 2024-11-01

**Category:** cond-mat.mtrl-sci

**ID:** 2411.00528v2

**Link:** [http://arxiv.org/abs/2411.00528v2](http://arxiv.org/abs/2411.00528v2)

**Summary:** The electromotive force transverse to a bias field under irradiation of
circularly polarized light, namely the photovoltaic Hall response or
light-induced anomalous Hall effect, has attracted considerable attention to
investigate the topologically nontrivial states in Floquet engineering and the
inverse spin Hall effect of spin-polarized carriers in spintronics. However,
taking into account inversion symmetry breaking by the bias field, the
circularly polarized light can excite photocarriers with asymmetric momentum
distribution, which generates injection current transverse to the bias field.
Therefore, the field-induced circular photogalvanic effect (FI-CPGE) should
also emerge in the very same experimental configuration for light-induced
anomalous Hall effect but has been overlooked in literature. In this work,
using terahertz pulses as a bias field for a semiconductor GaAs, we conduct
two-dimensional Fourier analysis and demonstrate that FI-CPGE can play a major
role in the photovoltaic Hall response. Counterintuitively, FI-CPGE is
significantly enhanced when the photocarriers are excited near the bandgap with
small density of states and low group velocity, which can be explained by a
three-level resonant nonlinear interaction near the band degeneracy point. We
also clarified that FI-CPGE would be further largely detected in the
contact-type measurement using electrodes because of the absence of a filtering
effect inherent to terahertz pulses. This work provides a comprehensive,
generalized view of the photovoltaic Hall response in biased materials, paving
a new avenue for detecting topological monopoles in momentum space hidden in
equilibrium using third-order nonlinear responses....

---

### 173. Separation and Collapse of Equilibria Inequalities on AND-OR Trees without Shape Constraints

**Authors:** Fuki Ito, Toshio Suzuki

**Published:** 2024-05-30

**Category:** cs.AI

**ID:** 2405.20138v3

**Link:** [http://arxiv.org/abs/2405.20138v3](http://arxiv.org/abs/2405.20138v3)

**Summary:** Herein, we investigate the zero-error randomized complexity, which is the
least cost against the worst input, of AND-OR tree computation by imposing
various restrictions on the algorithm to find the Boolean value of the root of
that tree and no restrictions on the tree shape. When a tree satisfies a
certain condition regarding its symmetry, directional algorithms proposed by
Saks and Wigderson (1986), special randomized algorithms, are known to achieve
the randomized complexity. Furthermore, there is a known example of a tree that
is so unbalanced that no directional algorithm achieves the randomized
complexity (Vereshchagin 1998). In this study, we aim to identify where
deviations arise between the general randomized Boolean decision tree and its
special case, directional algorithms. We show that for any AND-OR tree,
randomized depth-first algorithms, which form a broader class compared with
directional algorithms, have the same equilibrium as that of the directional
algorithms. Thus, we get the collapse result on equilibria inequalities that
holds for an arbitrary AND-OR tree. This implies that there exists a case where
even depth-first algorithms cannot be the fastest, leading to the separation
result on equilibria inequality. Additionally, a new algorithm is introduced as
a key concept for proof of the separation result....

---

### 174. The Hamiltonian of Poly-matrix Zero-sum Games

**Authors:** Toshihiro Ota, Yuma Fujimoto

**Published:** 2025-05-19

**Category:** cs.GT

**ID:** 2505.12609v2

**Link:** [http://arxiv.org/abs/2505.12609v2](http://arxiv.org/abs/2505.12609v2)

**Summary:** Understanding a dynamical system fundamentally relies on establishing an
appropriate Hamiltonian function and elucidating its symmetries. By formulating
agents' strategies and cumulative payoffs as canonically conjugate variables,
we identify the Hamiltonian function that generates the dynamics of poly-matrix
zero-sum games. We reveal the symmetries of our Hamiltonian and derive the
associated conserved quantities, showing how the conservation of probability
and the invariance of the Fenchel coupling are intrinsically encoded within the
system. Furthermore, we propose the dissipation FTRL (DFTRL) dynamics by
introducing a perturbation that dissipates the Fenchel coupling, proving
convergence to the Nash equilibrium and linking DFTRL to last-iterate
convergent algorithms. Our results highlight the potential of Hamiltonian
dynamics in uncovering the structural properties of learning dynamics in games,
and pave the way for broader applications of Hamiltonian dynamics in game
theory and machine learning....

---

### 175. Defect-induced spin textures in magnetic solids

**Authors:** M. E. Zhitomirsky, Vijay B. Shenoy, Roderich Moessner

**Published:** 2024-12-02

**Category:** cond-mat.str-el

**ID:** 2412.01662v2

**Link:** [http://arxiv.org/abs/2412.01662v2](http://arxiv.org/abs/2412.01662v2)

**Summary:** Vacancy defects in isotropic noncollinear antiferromagnets produce long-range
spin textures. By developing a "magnetic elasticity theory", we demonstrate
that a vacancy-induced readjustment in the spin configuration decays
algebraically with distance. The power law exponent depends on the multipole
moment of a local spin deformation, which in turn is determined by the lattice
symmetry and an equilibrium spin configuration in the absence of defects. The
role of these two factors is highlighted for the J1-J2 Heisenberg model on a
kagome lattice. A vacancy in this model generates spin deformations that decay
as 1/r^2 for the q=0 ground state and as a 1/r for the sqrt{3} x sqrt{3}
magnetic structure. The analytic conclusions are confirmed by extensive
numerical simulations. We also compute the fractional magnetic moments
associated with vacancies and other lattice defects. Our results shed light on
relative fragility of different magnetic structures with respect to spin glass
formation at higher doping levels....

---

### 176. Materials Generation in the Era of Artificial Intelligence: A Comprehensive Survey

**Authors:** Zhixun Li, Bin Cao, Rui Jiao, Liang Wang, Ding Wang, Yang Liu, Dingshuo Chen, Jia Li, Qiang Liu, Yu Rong, Liang Wang, Tong-yi Zhang, Jeffrey Xu Yu

**Published:** 2025-05-22

**Category:** cond-mat.mtrl-sci

**ID:** 2505.16379v1

**Link:** [http://arxiv.org/abs/2505.16379v1](http://arxiv.org/abs/2505.16379v1)

**Summary:** Materials are the foundation of modern society, underpinning advancements in
energy, electronics, healthcare, transportation, and infrastructure. The
ability to discover and design new materials with tailored properties is
critical to solving some of the most pressing global challenges. In recent
years, the growing availability of high-quality materials data combined with
rapid advances in Artificial Intelligence (AI) has opened new opportunities for
accelerating materials discovery. Data-driven generative models provide a
powerful tool for materials design by directly create novel materials that
satisfy predefined property requirements. Despite the proliferation of related
work, there remains a notable lack of up-to-date and systematic surveys in this
area. To fill this gap, this paper provides a comprehensive overview of recent
progress in AI-driven materials generation. We first organize various types of
materials and illustrate multiple representations of crystalline materials. We
then provide a detailed summary and taxonomy of current AI-driven materials
generation approaches. Furthermore, we discuss the common evaluation metrics
and summarize open-source codes and benchmark datasets. Finally, we conclude
with potential future directions and challenges in this fast-growing field. The
related sources can be found at
https://github.com/ZhixunLEE/Awesome-AI-for-Materials-Generation....

---

### 177. Transforming the Hybrid Cloud for Emerging AI Workloads

**Authors:** Deming Chen, Alaa Youssef, Ruchi Pendse, André Schleife, Bryan K. Clark, Hendrik Hamann, Jingrui He, Teodoro Laino, Lav Varshney, Yuxiong Wang, Avirup Sil, Reyhaneh Jabbarvand, Tianyin Xu, Volodymyr Kindratenko, Carlos Costa, Sarita Adve, Charith Mendis, Minjia Zhang, Santiago Núñez-Corrales, Raghu Ganti, Mudhakar Srivatsa, Nam Sung Kim, Josep Torrellas, Jian Huang, Seetharami Seelam, Klara Nahrstedt, Tarek Abdelzaher, Tamar Eilam, Huimin Zhao, Matteo Manica, Ravishankar Iyer, Martin Hirzel, Vikram Adve, Darko Marinov, Hubertus Franke, Hanghang Tong, Elizabeth Ainsworth, Han Zhao, Deepak Vasisht, Minh Do, Sahil Suneja, Fabio Oliveira, Giovanni Pacifici, Ruchir Puri, Priya Nagpurkar

**Published:** 2024-11-20

**Category:** cs.DC

**ID:** 2411.13239v2

**Link:** [http://arxiv.org/abs/2411.13239v2](http://arxiv.org/abs/2411.13239v2)

**Summary:** This white paper, developed through close collaboration between IBM Research
and UIUC researchers within the IIDAI Institute, envisions transforming hybrid
cloud systems to meet the growing complexity of AI workloads through
innovative, full-stack co-design approaches, emphasizing usability,
manageability, affordability, adaptability, efficiency, and scalability. By
integrating cutting-edge technologies such as generative and agentic AI,
cross-layer automation and optimization, unified control plane, and composable
and adaptive system architecture, the proposed framework addresses critical
challenges in energy efficiency, performance, and cost-effectiveness.
Incorporating quantum computing as it matures will enable quantum-accelerated
simulations for materials science, climate modeling, and other high-impact
domains. Collaborative efforts between academia and industry are central to
this vision, driving advancements in foundation models for material design and
climate solutions, scalable multimodal data processing, and enhanced
physics-based AI emulators for applications like weather forecasting and carbon
sequestration. Research priorities include advancing AI agentic systems, LLM as
an Abstraction (LLMaaA), AI model optimization and unified abstractions across
heterogeneous infrastructure, end-to-end edge-cloud transformation, efficient
programming model, middleware and platform, secure infrastructure,
application-adaptive cloud systems, and new quantum-classical collaborative
workflows. These ideas and solutions encompass both theoretical and practical
research questions, requiring coordinated input and support from the research
community. This joint initiative aims to establish hybrid clouds as secure,
efficient, and sustainable platforms, fostering breakthroughs in AI-driven
applications and scientific discovery across academia, industry, and society....

---

### 178. Activation of anomalous Hall effect and orbital magnetization by domain walls in altermagnets

**Authors:** Sopheak Sorn, Yuriy Mokrousov

**Published:** 2025-05-21

**Category:** cond-mat.mes-hall

**ID:** 2505.15894v1

**Link:** [http://arxiv.org/abs/2505.15894v1](http://arxiv.org/abs/2505.15894v1)

**Summary:** Altermagnets are an emerging class of unconventional antiferromagnets,
characterized by a N\'eel ordering that does not break the translation symmetry
of the underlying lattice. Depending on the orientation of the N\'eel vector,
the anomalous Hall effect (AHE) may or may not exist. In the so-called pure
altermagnets, AHE is forbidden by the magnetic symmetry. Here, we demonstrate
that in pure altermagnets, the domain walls can lift the symmetry constraints,
thereby activating the AHE and orbital magnetization. Taking a representative
example of a rutile-lattice tight-binding minimal model in slab geometry, we
use the linear response theory to demonstrate the emergence of the domain wall
AHE, finding that it is closely related with the orbital magnetization, while
the spin magnetization does not play a significant role. Using Landau theory,
we argue that while for a random arrangement of $\pi$ domain walls, the
contributions from the individual domain walls will cancel one another, an
external magnetic field will favor domain-wall arrangements with specific
chirality giving rise to a net AHE signal. Using group theory, we discuss how
these findings can be generalized straightforwardly to certain other classes of
altermagnets. Our work reveals a crucial role of the domain walls in the
understanding of the Hall transport and orbital magnetism of altermagnets....

---

### 179. Chemical design of monolayer altermagnets

**Authors:** Runzhang Xu, Yifan Gao, Junwei Liu

**Published:** 2025-05-21

**Category:** cond-mat.mtrl-sci

**ID:** 2505.15484v1

**Link:** [http://arxiv.org/abs/2505.15484v1](http://arxiv.org/abs/2505.15484v1)

**Summary:** The crystal-symmetry-paired spin-momentum locking (CSML) arisen from the
intrinsic crystal symmetry connecting different magnetic sublattices in
altermagnets enables many exotic spintronics properties such as unconventional
piezomagnetism and noncollinear spin current. However, the shortage of
monolayer altermagnets restricts further exploration of dimensionally confined
phenomena and applications of nanostructured devices. Here, we propose general
chemical design principles inspired by sublattice symmetry of layered
altermagnet V$_2$(Se,Te)$_2$O through symmetry-preserving structural
modification and valence-adaptive chemical substitutions. In total, we
construct 2600 candidates across four structural frameworks,
M$_2$A$_2$B$_{1,0}$ and their Janus derivatives. High-throughput calculations
identify 670 potential altermagnets with N\'eel-ordered ground states, among
which 91 ones exhibiting CSML Dirac cones that enable spin-polarized ultra-fast
transport. These materials also feature different ground-state magnetic
orderings and demonstrate diverse electronic behaviors, ranging from
semiconductors, metals, half-metals, to Dirac semimetals. This work not only
reveals abundant monolayer altermagnets, but also establishes a rational
principle for their design, opening gates for exploration of confined magnetism
and spintronics in atomically thin systems....

---

### 180. Inverse Design of Metal-Organic Frameworks Using Quantum Natural Language Processing

**Authors:** Shinyoung Kang, Jihan Kim

**Published:** 2024-05-20

**Category:** cs.LG

**ID:** 2405.11783v2

**Link:** [http://arxiv.org/abs/2405.11783v2](http://arxiv.org/abs/2405.11783v2)

**Summary:** In this study, we explore the potential of using quantum natural language
processing (QNLP) to inverse design metal-organic frameworks (MOFs) with
targeted properties. Specifically, by analyzing 450 hypothetical MOF structures
consisting of 3 topologies, 10 metal nodes and 15 organic ligands, we
categorize these structures into four distinct classes for pore volume and
$CO_{2}$ Henry's constant values. We then compare various QNLP models (i.e. the
bag-of-words, DisCoCat (Distributional Compositional Categorical), and
sequence-based models) to identify the most effective approach to process the
MOF dataset. Using a classical simulator provided by the IBM Qiskit, the
bag-of-words model is identified to be the optimum model, achieving validation
accuracies of 88.6% and 78.0% for binary classification tasks on pore volume
and $CO_{2}$ Henry's constant, respectively. Further, we developed multi-class
classification models tailored to the probabilistic nature of quantum circuits,
with average test accuracies of 92% and 80% across different classes for pore
volume and $CO_{2}$ Henry's constant datasets. Finally, the performance of
generating MOF with target properties showed accuracies of 93.5% for pore
volume and 87% for $CO_{2}$ Henry's constant, respectively. Although our
investigation covers only a fraction of the vast MOF search space, it marks a
promising first step towards using quantum computing for materials design,
offering a new perspective through which to explore the complex landscape of
MOFs....

---

### 181. Neural Collapse is Globally Optimal in Deep Regularized ResNets and Transformers

**Authors:** Peter Súkeník, Christoph H. Lampert, Marco Mondelli

**Published:** 2025-05-21

**Category:** cs.LG

**ID:** 2505.15239v1

**Link:** [http://arxiv.org/abs/2505.15239v1](http://arxiv.org/abs/2505.15239v1)

**Summary:** The empirical emergence of neural collapse -- a surprising symmetry in the
feature representations of the training data in the penultimate layer of deep
neural networks -- has spurred a line of theoretical research aimed at its
understanding. However, existing work focuses on data-agnostic models or, when
data structure is taken into account, it remains limited to multi-layer
perceptrons. Our paper fills both these gaps by analyzing modern architectures
in a data-aware regime: we prove that global optima of deep regularized
transformers and residual networks (ResNets) with LayerNorm trained with cross
entropy or mean squared error loss are approximately collapsed, and the
approximation gets tighter as the depth grows. More generally, we formally
reduce any end-to-end large-depth ResNet or transformer training into an
equivalent unconstrained features model, thus justifying its wide use in the
literature even beyond data-agnostic settings. Our theoretical results are
supported by experiments on computer vision and language datasets showing that,
as the depth grows, neural collapse indeed becomes more prominent....

---

### 182. Time Reversal Symmetry for Efficient Robotic Manipulations in Deep Reinforcement Learning

**Authors:** Yunpeng Jiang, Jianshu Hu, Paul Weng, Yutong Ban

**Published:** 2025-05-20

**Category:** cs.RO

**ID:** 2505.13925v1

**Link:** [http://arxiv.org/abs/2505.13925v1](http://arxiv.org/abs/2505.13925v1)

**Summary:** Symmetry is pervasive in robotics and has been widely exploited to improve
sample efficiency in deep reinforcement learning (DRL). However, existing
approaches primarily focus on spatial symmetries, such as reflection, rotation,
and translation, while largely neglecting temporal symmetries. To address this
gap, we explore time reversal symmetry, a form of temporal symmetry commonly
found in robotics tasks such as door opening and closing. We propose Time
Reversal symmetry enhanced Deep Reinforcement Learning (TR-DRL), a framework
that combines trajectory reversal augmentation and time reversal guided reward
shaping to efficiently solve temporally symmetric tasks. Our method generates
reversed transitions from fully reversible transitions, identified by a
proposed dynamics-consistent filter, to augment the training data. For
partially reversible transitions, we apply reward shaping to guide learning,
according to successful trajectories from the reversed task. Extensive
experiments on the Robosuite and MetaWorld benchmarks demonstrate that TR-DRL
is effective in both single-task and multi-task settings, achieving higher
sample efficiency and stronger final performance compared to baseline methods....

---

### 183. RoCoDA: Counterfactual Data Augmentation for Data-Efficient Robot Learning from Demonstrations

**Authors:** Ezra Ameperosa, Jeremy A. Collins, Mrinal Jain, Animesh Garg

**Published:** 2024-11-25

**Category:** cs.RO

**ID:** 2411.16959v2

**Link:** [http://arxiv.org/abs/2411.16959v2](http://arxiv.org/abs/2411.16959v2)

**Summary:** Imitation learning in robotics faces significant challenges in generalization
due to the complexity of robotic environments and the high cost of data
collection. We introduce RoCoDA, a novel method that unifies the concepts of
invariance, equivariance, and causality within a single framework to enhance
data augmentation for imitation learning. RoCoDA leverages causal invariance by
modifying task-irrelevant subsets of the environment state without affecting
the policy's output. Simultaneously, we exploit SE(3) equivariance by applying
rigid body transformations to object poses and adjusting corresponding actions
to generate synthetic demonstrations. We validate RoCoDA through extensive
experiments on five robotic manipulation tasks, demonstrating improvements in
policy performance, generalization, and sample efficiency compared to
state-of-the-art data augmentation methods. Our policies exhibit robust
generalization to unseen object poses, textures, and the presence of
distractors. Furthermore, we observe emergent behavior such as re-grasping,
indicating policies trained with RoCoDA possess a deeper understanding of task
dynamics. By leveraging invariance, equivariance, and causality, RoCoDA
provides a principled approach to data augmentation in imitation learning,
bridging the gap between geometric symmetries and causal reasoning. Project
Page: https://rocoda.github.io...

---

### 184. Symmetry-Driven Trimer Formation in Kagome Correlated Electron Materials

**Authors:** Varsha Kumari, Julia Bauer, Alexandru B. Georgescu

**Published:** 2025-05-19

**Category:** cond-mat.mtrl-sci

**ID:** 2505.13659v1

**Link:** [http://arxiv.org/abs/2505.13659v1](http://arxiv.org/abs/2505.13659v1)

**Summary:** Correlated electron materials with molecular orbital states extending over
transition metal clusters can host multiferroicity, spin frustration, and
unconventional insulating phases. However, the fundamental criteria that govern
cluster formation and stability remain unclear. Here, we identify a symmetry,
correlation, and electron filling driven criteria that stabilize triangular
metal trimers in materials displaying transition metal kagome patterns. Using
density functional theory and chemical bonding analysis, we show that trimer
formation emerges when 6 to 8 electrons occupy molecular orbitals derived from
transition metal d-states, achieving near complete filling of bonding states
while avoiding antibonding occupation, and correlations are of intermediate
strength. This principle explains the stability of Nb$_3$X$_8$ (X = Cl, Br, I),
and more broadly, our findings offer a general design rule to obtain quantum
materials with quantum states extended across transition metal clusters....

---

### 185. TopoTune : A Framework for Generalized Combinatorial Complex Neural Networks

**Authors:** Mathilde Papillon, Guillermo Bernárdez, Claudio Battiloro, Nina Miolane

**Published:** 2024-10-09

**Category:** cs.LG

**ID:** 2410.06530v4

**Link:** [http://arxiv.org/abs/2410.06530v4](http://arxiv.org/abs/2410.06530v4)

**Summary:** Graph Neural Networks (GNNs) excel in learning from relational datasets as
they preserve the symmetries of the graph domain. However, many complex systems
-- such as biological or social networks -- involve multiway complex
interactions that are more naturally represented by higher-order topological
domains. The emerging field of Topological Deep Learning (TDL) aims to
accommodate and leverage these higher-order structures. Combinatorial Complex
Neural Networks (CCNNs), fairly general TDL models, have been shown to be more
expressive and better performing than GNNs. However, differently from the GNN
ecosystem, TDL lacks a principled and standardized framework for easily
defining new architectures, restricting its accessibility and applicability. To
address this issue, we introduce Generalized CCNNs (GCCNs), a simple yet
powerful family of TDL models that can be used to systematically transform any
(graph) neural network into its TDL counterpart. We prove that GCCNs generalize
and subsume CCNNs, while extensive experiments on a diverse class of GCCNs show
that these architectures consistently match or outperform CCNNs, often with
less model complexity. In an effort to accelerate and democratize TDL, we
introduce TopoTune, a lightweight software for defining, building, and training
GCCNs with unprecedented flexibility and ease....

---

### 186. Learning (Approximately) Equivariant Networks via Constrained Optimization

**Authors:** Andrei Manolache, Luiz F. O. Chamon, Mathias Niepert

**Published:** 2025-05-19

**Category:** cs.LG

**ID:** 2505.13631v1

**Link:** [http://arxiv.org/abs/2505.13631v1](http://arxiv.org/abs/2505.13631v1)

**Summary:** Equivariant neural networks are designed to respect symmetries through their
architecture, boosting generalization and sample efficiency when those
symmetries are present in the data distribution. Real-world data, however,
often departs from perfect symmetry because of noise, structural variation,
measurement bias, or other symmetry-breaking effects. Strictly equivariant
models may struggle to fit the data, while unconstrained models lack a
principled way to leverage partial symmetries. Even when the data is fully
symmetric, enforcing equivariance can hurt training by limiting the model to a
restricted region of the parameter space. Guided by homotopy principles, where
an optimization problem is solved by gradually transforming a simpler problem
into a complex one, we introduce Adaptive Constrained Equivariance (ACE), a
constrained optimization approach that starts with a flexible, non-equivariant
model and gradually reduces its deviation from equivariance. This gradual
tightening smooths training early on and settles the model at a data-driven
equilibrium, balancing between equivariance and non-equivariance. Across
multiple architectures and tasks, our method consistently improves performance
metrics, sample efficiency, and robustness to input perturbations compared with
strictly equivariant models and heuristic equivariance relaxations....

---

### 187. Symmetry-Breaking Descent for Invariant Cost Functionals

**Authors:** Mikhail Osipov

**Published:** 2025-05-19

**Category:** cs.LG

**ID:** 2505.13578v1

**Link:** [http://arxiv.org/abs/2505.13578v1](http://arxiv.org/abs/2505.13578v1)

**Summary:** We study the problem of reducing a task cost functional $W(S)$, defined over
Sobolev-class signals $S$, when the cost is invariant under a global symmetry
group $G \subset \mathrm{Diff}(M)$ and accessible only as a black-box. Such
scenarios arise in machine learning, imaging, and inverse problems, where cost
metrics reflect model outputs or performance scores but are non-differentiable
and model-internal. We propose a variational method that exploits the symmetry
structure to construct explicit, symmetry-breaking deformations of the input
signal. A gauge field $\phi$, obtained by minimizing an auxiliary energy
functional, induces a deformation $h = A_\phi[S]$ that generically lies
transverse to the $G$-orbit of $S$. We prove that, under mild regularity, the
cost $W$ strictly decreases along this direction -- either via Clarke
subdifferential descent or by escaping locally flat plateaus. The exceptional
set of degeneracies has zero Gaussian measure. Our approach requires no access
to model gradients or labels and operates entirely at test time. It provides a
principled tool for optimizing invariant cost functionals via Lie-algebraic
variational flows, with applications to black-box models and
symmetry-constrained tasks....

---

### 188. Ultrafast Laser Induces Macroscopic Symmetry-Breaking of Diamond Color Centers

**Authors:** Yang Gao, Qi-Zheng Ji, Chao-Bo Liu, Qi Xiao, Chao Lian

**Published:** 2025-05-19

**Category:** cond-mat.mtrl-sci

**ID:** 2505.12989v1

**Link:** [http://arxiv.org/abs/2505.12989v1](http://arxiv.org/abs/2505.12989v1)

**Summary:** We employ real-time time-dependent density functional theory (RT-TDDFT) to
investigate the electron-phonon-spin correlated dynamics in negatively charged
nitrogen-vacancy centers (NV$^{-}$) and construct a comprehensive dynamical
picture. Laser excitation promotes minority-spin electrons within 100~fs,
establishing a three-fold rotation symmetry breaking (3RSB) charge ordering.
Subsequently, ionic motion on the potential energy surface of the excited
electrons generates two distinct dynamical modes: (1) symmetric oscillations of
carbon-nitrogen bonds and (2) dynamic Jahn-Teller distortions (DJT) with 3RSB.
These distortions induce nonlocal coherent phonons in the diamond lattice,
which propagate with 3RSB at the sound velocity ($\sim$2~\AA/fs). Furthermore,
the NV$^{-}$ spin state remains preserved during photoexcitation but undergoes
rapid reorientation within 100~fs via enhanced spin-orbit-phonon coupling. Our
RT-TDDFT simulations provide direct time-resolved visualization of these
processes, offering novel insights into the microscopic interplay of electrons,
phonons, and spins in NV$^{-}$ centers. These results advance the fundamental
understanding of dynamical mechanisms in solid-state quantum systems, with
implications for optimizing NV$^{-}$-based quantum sensing technologies....

---

### 189. AdS-GNN -- a Conformally Equivariant Graph Neural Network

**Authors:** Maksim Zhdanov, Nabil Iqbal, Erik Bekkers, Patrick Forré

**Published:** 2025-05-19

**Category:** cs.LG

**ID:** 2505.12880v1

**Link:** [http://arxiv.org/abs/2505.12880v1](http://arxiv.org/abs/2505.12880v1)

**Summary:** Conformal symmetries, i.e.\ coordinate transformations that preserve angles,
play a key role in many fields, including physics, mathematics, computer vision
and (geometric) machine learning. Here we build a neural network that is
equivariant under general conformal transformations. To achieve this, we lift
data from flat Euclidean space to Anti de Sitter (AdS) space. This allows us to
exploit a known correspondence between conformal transformations of flat space
and isometric transformations on the AdS space. We then build upon the fact
that such isometric transformations have been extensively studied on general
geometries in the geometric deep learning literature. We employ message-passing
layers conditioned on the proper distance, yielding a computationally efficient
framework. We validate our model on tasks from computer vision and statistical
physics, demonstrating strong performance, improved generalization capacities,
and the ability to extract conformal data such as scaling dimensions from the
trained network....

---

### 190. Giant Nonvolatile Multistate Resistance with Fully Magnetically Controlled van der Waals Multiferroic Tunnel Junctions

**Authors:** Zhi Yan, Xujin Zhang, Jianhua Xiao, Cheng Fang, Xiaohong Xu

**Published:** 2025-01-01

**Category:** cond-mat.mtrl-sci

**ID:** 2501.00761v4

**Link:** [http://arxiv.org/abs/2501.00761v4](http://arxiv.org/abs/2501.00761v4)

**Summary:** Ferroelectric polarization switching in electrically controlled van der Waals
multiferroic tunnel junctions (vdW-MFTJs) causes atomic migration, compromising
device stability and fatigue resistance. Here we propose a fully magnetically
controlled vdW-MFTJ based on a \(\mathrm{CrBr_3/MnPSe_3/CrBr_3}\) vertical
heterostructure, which achieves ferroelectric polarization reversal without
relying on atomic migration driven by inversion symmetry breaking. Using
first-principles calculations, we investigate the spin-polarized quantum
transport properties of the proposed structure. By integrating asymmetric
PtTe$_2$/alkali-metal (Li/Na/K)-doped/intercalated CrBr$_3$ electrodes, the
device demonstrates exceptional performance, with a maximum tunneling
magnetoresistance (TMR) exceeding $8.1\times10^5$\% and tunneling
electroresistance (TER) reaching 2499\%, while the spin-filtering channels can
be flexibly controlled by the magnetization direction of the magnetic free
layer, achieving perfect spin-filtering over a broad bias voltage range.
Applying an external bias voltage further enhances these metrics, increasing
TMR to $3.6\times 10^7$\% and TER to 9990\%. Notably, a pronounced negative
differential resistance (NDR) effect is observed, yielding an unprecedented
peak-to-valley ratio (PVR) of $9.55\times10^9$\%, representing the highest
value reported for vertical tunnel junctions. These extraordinary
characteristics highlight the potential of vdW-MFTJs for ultra-efficient
electronic switching, a key feature for next-generation spintronic devices. Our
findings provide a solid theoretical foundation for designing and developing
high-performance magnetic storage and logic technologies....

---

### 191. Re-experiment Smart: a Novel Method to Enhance Data-driven Prediction of Mechanical Properties of Epoxy Polymers

**Authors:** Wanshan Cui, Yejin Jeong, Inwook Song, Gyuri Kim, Minsang Kwon, Donghun Lee

**Published:** 2025-05-19

**Category:** cond-mat.soft

**ID:** 2506.01994v1

**Link:** [http://arxiv.org/abs/2506.01994v1](http://arxiv.org/abs/2506.01994v1)

**Summary:** Accurate prediction of polymer material properties through data-driven
approaches greatly accelerates novel material development by reducing redundant
experiments and trial-and-error processes. However, inevitable outliers in
empirical measurements can severely skew machine learning results, leading to
erroneous prediction models and suboptimal material designs. To address this
limitation, we propose a novel approach to enhance dataset quality efficiently
by integrating multi-algorithm outlier detection with selective
re-experimentation of unreliable outlier cases. To validate the empirical
effectiveness of the approach, we systematically construct a new dataset
containing 701 measurements of three key mechanical properties: glass
transition temperature ($T_g$), tan $\delta$ peak, and crosslinking density
($v_{c}$). To demonstrate its general applicability, we report the performance
improvements across multiple machine learning models, including Elastic Net,
SVR, Random Forest, and TPOT, to predict the three key properties. Our method
reliably reduces prediction error (RMSE) and significantly improves accuracy
with minimal additional experimental work, requiring only about 5% of the
dataset to be re-measured. These findings highlight the importance of data
quality enhancement in achieving reliable machine learning applications in
polymer science and present a scalable strategy for improving predictive
reliability in materials science....

---

### 192. Spontaneous Enhancement of Dzyaloshinskii-Moriya Interaction via Field-Cooling-Induced Interface Engineering in 2D van der Waals Ferromagnetic ternary Tellurides

**Authors:** Shian Xia, Yan Luo, Iftikhar Ahmed Malik, Xinyi Zhou, Keying Han, Yue Sun, Haoyun Lin, Hanqing Shi, Yingchun Cheng, Vanessa Li Zhang, Yi Du, Sheng Liu, Chao Zhu, Ting Yu

**Published:** 2025-05-11

**Category:** cond-mat.mtrl-sci

**ID:** 2505.06924v2

**Link:** [http://arxiv.org/abs/2505.06924v2](http://arxiv.org/abs/2505.06924v2)

**Summary:** The emergence of two-dimensional (2D) van der Waals (vdW) ferromagnets has
opened new avenues for exploring topological spin textures and their
applications in next-generation spintronics. Among these materials, Fe3GaTe2
(FGaT) emerges as a model system due to its room-temperature skyrmion phases,
which are stabilized by strong Dzyaloshinskii-Moriya interaction (DMI).
However, the atomistic origins of DMI in centrosymmetric vdW lattices remain
elusive. Here, we report a spontaneous DMI enhancement mechanism driven by FC
in FGaT and its analog Fe3GeTe2 (FGeT). Combining Raman spectroscopy and
scanning transmission electron microscopy (STEM), we have observed the
irreversible precipitation of FeTe2 in annealed FGaT. The resulting FeTe2/FGaT
heterostructure is considered to break the symmetry and significantly enhance
the DMI. Furthermore, similar phenomenon has been observed in the family
ferromagnetic material FGeT as well. Additionally, the precipitation of FeTe2
varies significantly with different thicknesses of FGaT, aligning closely with
the reported behavior of skyrmions. This discovery provides new insights into
the mechanisms behind the origin of the DMI in ternary tellurides, paving the
way for advanced spintronic applications....

---

### 193. Observation of optical vortex generation via magnon-induced Brillouin light scattering

**Authors:** Ryusuke Hisatomi, Alto Osada, Kotaro Taga, Haruka Komiyama, Takuya Takahashi, Shutaro Karube, Yoichi Shiota, Teruo Ono

**Published:** 2025-05-06

**Category:** physics.optics

**ID:** 2505.03152v2

**Link:** [http://arxiv.org/abs/2505.03152v2](http://arxiv.org/abs/2505.03152v2)

**Summary:** Exploration of physics involving orbital angular momentum (OAM) of light,
first recognized in 1992, is essential for deepening our understanding of the
interaction between light and matter and that opens up new applications. In
systems with rotational symmetry, it is known that OAM can be exchanged between
light and matter. One of the most common applications of such a phenomenon is
manipulating the optical OAM through the exchange of OAM between light and a
nematic liquid crystal-based spatial light modulator (SLM). It is already being
used as a tool in many studies related to the optical OAM. However, the
operation bandwidth is limited by the response speed 100 Hz of the liquid
crystal, which hinders the applications of the optical OAM to spatial division
multiplexing, quantum communication, and optical microscopy. The generation of
optical vortex beams with the optical OAM in inelastic scattering by elementary
excitations with gigahertz-order resonance may solve this problem, although it
has not been studied so far. Here, we demonstrate the generation of the optical
vortex beams using Brillouin light scattering by magnons without phase
singularities. We observe scattering rules in the Brillouin light scattering
which can be explained by conservation of total angular momentum including
spins and orbits with photons and magnons. This work serves as a starting point
for research into the interaction between optical vertices and magnons. It
opens up devices with the novel mechanism of optical OAM generation together
with high operation bandwidth....

---

### 194. Anisotropic magnetic phase diagrams, tricriticality, and spin-reorientation in high-pressure grown SmCrO$_3$ single crystals

**Authors:** Ning Yuan, Erik Walendy, Nour Maraytta, Waldemar Hergett, Luca Bischof, Michael Merz, Rüdiger Klingeler

**Published:** 2025-05-16

**Category:** cond-mat.str-el

**ID:** 2505.11256v1

**Link:** [http://arxiv.org/abs/2505.11256v1](http://arxiv.org/abs/2505.11256v1)

**Summary:** SmCrO$_3$ single crystals were successfully grown utilizing the high-pressure
optical floating-zone method and their crystal structure, magnetization
behavior, and magnetic phase diagrams were thoroughly investigated. Magnetic
studies were conducted for fields applied along all principal crystallographic
directions, with measurements taken at temperatures as low as 0.4 K and
magnetic fields up to 14 T. The single crystal growth parameters are reported
and the orthorhombic structure with the centrosymmetric space group $Pbnm$ is
confirmed. Long-range order of the Cr$^{3+}$ and Sm$^{3+}$ magnetic sublattices
evolves at $T_{\rm N}$ = 192 K and $T_{\rm N2}$=3 K, respectively. In contrast
to previous studies on polycrystals our single crystal data imply a
discontinuous and one-step spin-reorientation (SR) of net magnetic moments
$\tilde{M}$ from the $c$ axis into the $ab$ plane at zero magnetic field at
$T_{\rm SR}$=33 K. Its discontinuous nature is maintained if $B$ is applied
$||c$ axis but tricritical behavior and a triple point is found for $B||a$
axis. While our data are consistent with the magnetic representation $\Gamma_4$
for $T > T_{\mathrm {SR}}$, the size and in-plane direction of the observed net
magnetic moment disagree to previously proposed spin configurations, i.e.,
$\Gamma_1$ and $\Gamma_2$, for the spin-reoriented phases. In general, our
high-quality single crystals enable us to revisit the phase diagram and to
clarify the complex magnetism in SmCrO3 arising from the interplay of
anisotropic 3$d$ and 4$f$ magnetic sublattices....

---

### 195. Attention on the Sphere

**Authors:** Boris Bonev, Max Rietmann, Andrea Paris, Alberto Carpentieri, Thorsten Kurth

**Published:** 2025-05-16

**Category:** cs.LG

**ID:** 2505.11157v1

**Link:** [http://arxiv.org/abs/2505.11157v1](http://arxiv.org/abs/2505.11157v1)

**Summary:** We introduce a generalized attention mechanism for spherical domains,
enabling Transformer architectures to natively process data defined on the
two-dimensional sphere - a critical need in fields such as atmospheric physics,
cosmology, and robotics, where preserving spherical symmetries and topology is
essential for physical accuracy. By integrating numerical quadrature weights
into the attention mechanism, we obtain a geometrically faithful spherical
attention that is approximately rotationally equivariant, providing strong
inductive biases and leading to better performance than Cartesian approaches.
To further enhance both scalability and model performance, we propose
neighborhood attention on the sphere, which confines interactions to geodesic
neighborhoods. This approach reduces computational complexity and introduces
the additional inductive bias for locality, while retaining the symmetry
properties of our method. We provide optimized CUDA kernels and
memory-efficient implementations to ensure practical applicability. The method
is validated on three diverse tasks: simulating shallow water equations on the
rotating sphere, spherical image segmentation, and spherical depth estimation.
Across all tasks, our spherical Transformers consistently outperform their
planar counterparts, highlighting the advantage of geometric priors for
learning on spherical domains....

---

### 196. Assessing the Performance of Analog Training for Transfer Learning

**Authors:** Omobayode Fagbohungbe, Corey Lammie, Malte J. Rasch, Takashi Ando, Tayfun Gokmen, Vijay Narayanan

**Published:** 2025-05-16

**Category:** cs.LG

**ID:** 2505.11067v1

**Link:** [http://arxiv.org/abs/2505.11067v1](http://arxiv.org/abs/2505.11067v1)

**Summary:** Analog in-memory computing is a next-generation computing paradigm that
promises fast, parallel, and energy-efficient deep learning training and
transfer learning (TL). However, achieving this promise has remained elusive
due to a lack of suitable training algorithms. Analog memory devices exhibit
asymmetric and non-linear switching behavior in addition to device-to-device
variation, meaning that most, if not all, of the current off-the-shelf training
algorithms cannot achieve good training outcomes. Also, recently introduced
algorithms have enjoyed limited attention, as they require bi-directionally
switching devices of unrealistically high symmetry and precision and are highly
sensitive. A new algorithm chopped TTv2 (c-TTv2), has been introduced, which
leverages the chopped technique to address many of the challenges mentioned
above. In this paper, we assess the performance of the c-TTv2 algorithm for
analog TL using a Swin-ViT model on a subset of the CIFAR100 dataset. We also
investigate the robustness of our algorithm to changes in some device
specifications, including weight transfer noise, symmetry point skew, and
symmetry point variability...

---

### 197. Space Group Equivariant Crystal Diffusion

**Authors:** Rees Chang, Angela Pak, Alex Guerra, Ni Zhan, Nick Richardson, Elif Ertekin, Ryan P. Adams

**Published:** 2025-05-16

**Category:** cond-mat.mtrl-sci

**ID:** 2505.10994v1

**Link:** [http://arxiv.org/abs/2505.10994v1](http://arxiv.org/abs/2505.10994v1)

**Summary:** Accelerating inverse design of crystalline materials with generative models
has significant implications for a range of technologies. Unlike other atomic
systems, 3D crystals are invariant to discrete groups of isometries called the
space groups. Crucially, these space group symmetries are known to heavily
influence materials properties. We propose SGEquiDiff, a crystal generative
model which naturally handles space group constraints with space group
invariant likelihoods. SGEquiDiff consists of an SE(3)-invariant, telescoping
discrete sampler of crystal lattices; permutation-invariant, transformer-based
autoregressive sampling of Wyckoff positions, elements, and numbers of
symmetrically unique atoms; and space group equivariant diffusion of atomic
coordinates. We show that space group equivariant vector fields automatically
live in the tangent spaces of the Wyckoff positions. SGEquiDiff achieves
state-of-the-art performance on standard benchmark datasets as assessed by
quantitative proxy metrics and quantum mechanical calculations....

---

### 198. Texture- and Stress-Dependent Electromechanical Response in Ferroelectric PZT: Insights from a Micromechanical Model

**Authors:** Saujatya Mandal, Debashish Das

**Published:** 2025-03-15

**Category:** cond-mat.mtrl-sci

**ID:** 2503.12057v2

**Link:** [http://arxiv.org/abs/2503.12057v2](http://arxiv.org/abs/2503.12057v2)

**Summary:** The electromechanical response of PbZr0.52Ti0.48O3 (PZT) near the
morphotropic phase boundary (MPB) is strongly influenced by crystallographic
texture and residual stress, both of which affect domain switching behavior.
While these effects are critical for optimizing sensors, actuators, and MEMS
devices, their combined influence remains poorly understood. We present a
computational micromechanical model that captures texture- and stress-dependent
polarization switching in MPB PZT. The framework incorporates both tetragonal
and rhombohedral domain switching, along with interphase transformations,
enabling accurate simulation of nonlinear electromechanical behavior. The model
reproduces key experimental trends, including enhanced piezoelectric response
in (001)-textured ceramics, and degradation under high in-plane stress. The
implementation, provided as open-source MATLAB code, offers an accessible
platform for experimentalists and materials designers to explore and interpret
electromechanical behavior. By linking microstructural orientation and stress
state to macroscopic response, this work provides a practical tool for
understanding and designing next-generation piezoelectric materials....

---

### 199. MatTools: Benchmarking Large Language Models for Materials Science Tools

**Authors:** Siyu Liu, Jiamin Xu, Beilin Ye, Bo Hu, David J. Srolovitz, Tongqi Wen

**Published:** 2025-05-16

**Category:** cond-mat.mtrl-sci

**ID:** 2505.10852v1

**Link:** [http://arxiv.org/abs/2505.10852v1](http://arxiv.org/abs/2505.10852v1)

**Summary:** Large language models (LLMs) are increasingly applied to materials science
questions, including literature comprehension, property prediction, materials
discovery and alloy design. At the same time, a wide range of physics-based
computational approaches have been developed in which materials properties can
be calculated. Here, we propose a benchmark application to evaluate the
proficiency of LLMs to answer materials science questions through the
generation and safe execution of codes based on such physics-based
computational materials science packages. MatTools is built on two
complementary components: a materials simulation tool question-answer (QA)
benchmark and a real-world tool-usage benchmark. We designed an automated
methodology to efficiently collect real-world materials science tool-use
examples. The QA benchmark, derived from the pymatgen (Python Materials
Genomics) codebase and documentation, comprises 69,225 QA pairs that assess the
ability of an LLM to understand materials science tools. The real-world
benchmark contains 49 tasks (138 subtasks) requiring the generation of
functional Python code for materials property calculations. Our evaluation of
diverse LLMs yields three key insights: (1)Generalists outshine
specialists;(2)AI knows AI; and (3)Simpler is better. MatTools provides a
standardized framework for assessing and improving LLM capabilities for
materials science tool applications, facilitating the development of more
effective AI systems for materials science and general scientific research....

---

### 200. 34 Examples of LLM Applications in Materials Science and Chemistry: Towards Automation, Assistants, Agents, and Accelerated Scientific Discovery

**Authors:** Yoel Zimmermann, Adib Bazgir, Alexander Al-Feghali, Mehrad Ansari, Joshua Bocarsly, L. Catherine Brinson, Yuan Chiang, Defne Circi, Min-Hsueh Chiu, Nathan Daelman, Matthew L. Evans, Abhijeet S. Gangan, Janine George, Hassan Harb, Ghazal Khalighinejad, Sartaaj Takrim Khan, Sascha Klawohn, Magdalena Lederbauer, Soroush Mahjoubi, Bernadette Mohr, Seyed Mohamad Moosavi, Aakash Naik, Aleyna Beste Ozhan, Dieter Plessers, Aritra Roy, Fabian Schöppach, Philippe Schwaller, Carla Terboven, Katharina Ueltzen, Yue Wu, Shang Zhu, Jan Janssen, Calvin Li, Ian Foster, Ben Blaiszik

**Published:** 2025-05-05

**Category:** cs.LG

**ID:** 2505.03049v2

**Link:** [http://arxiv.org/abs/2505.03049v2](http://arxiv.org/abs/2505.03049v2)

**Summary:** Large Language Models (LLMs) are reshaping many aspects of materials science
and chemistry research, enabling advances in molecular property prediction,
materials design, scientific automation, knowledge extraction, and more. Recent
developments demonstrate that the latest class of models are able to integrate
structured and unstructured data, assist in hypothesis generation, and
streamline research workflows. To explore the frontier of LLM capabilities
across the research lifecycle, we review applications of LLMs through 34 total
projects developed during the second annual Large Language Model Hackathon for
Applications in Materials Science and Chemistry, a global hybrid event. These
projects spanned seven key research areas: (1) molecular and material property
prediction, (2) molecular and material design, (3) automation and novel
interfaces, (4) scientific communication and education, (5) research data
management and automation, (6) hypothesis generation and evaluation, and (7)
knowledge extraction and reasoning from the scientific literature.
Collectively, these applications illustrate how LLMs serve as versatile
predictive models, platforms for rapid prototyping of domain-specific tools,
and much more. In particular, improvements in both open source and proprietary
LLM performance through the addition of reasoning, additional training data,
and new techniques have expanded effectiveness, particularly in low-data
environments and interdisciplinary research. As LLMs continue to improve, their
integration into scientific workflows presents both new opportunities and new
challenges, requiring ongoing exploration, continued refinement, and further
research to address reliability, interpretability, and reproducibility....

---


<!-- ARXIV_PAPERS_END -->