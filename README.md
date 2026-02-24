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

*Last updated: 2026-02-25 06:31:37 (SGT)*

### 1. Exact Discrete Stochastic Simulation with Deep-Learning-Scale Gradient Optimization

**Authors:** Jose M. G. Vilar, Leonor Saiz

**Published:** 2026-02-23

**Category:** q-bio.QM

**ID:** 2602.19775v1

**Link:** [http://arxiv.org/abs/2602.19775v1](http://arxiv.org/abs/2602.19775v1)

**Summary:** Exact stochastic simulation of continuous-time Markov chains (CTMCs) is essential when discreteness and noise drive system behavior, but the hard categorical event selection in Gillespie-type algorithms blocks gradient-based learning. We eliminate this constraint by decoupling forward simulation from backward differentiation, with hard categorical sampling generating exact trajectories and gradients propagating through a continuous massively-parallel Gumbel-Softmax straight-through surrogate. Our approach enables accurate optimization at parameter scales over four orders of magnitude beyond existing simulators. We validate for accuracy, scalability, and reliability on a reversible dimerization model (0.09% error), a genetic oscillator (1.2% error), a 203,796-parameter gene regulatory network achieving 98.4% MNIST accuracy (a prototypical deep-learning multilayer perceptron benchmark), and experimental patch-clamp recordings of ion channel gating (R^2 = 0.987) in the single-channel regime. Our GPU implementation delivers 1.9 billion steps per second, matching the scale of non-differentiable simulators. By making exact stochastic simulation massively parallel and autodiff-compatible, our results enable high-dimensional parameter inference and inverse design across systems biology, chemical kinetics, physics, and related CTMC-governed domains....

---


<!-- ARXIV_PAPERS_END -->