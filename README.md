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

*Last updated: 2026-02-19 06:30:44 (SGT)*

### 1. Guided Diffusion by Optimized Loss Functions on Relaxed Parameters for Inverse Material Design

**Authors:** Jens U. Kreber, Christian Weißenfels, Joerg Stueckler

**Published:** 2026-02-17

**Category:** cs.LG

**ID:** 2602.15648v1

**Link:** [http://arxiv.org/abs/2602.15648v1](http://arxiv.org/abs/2602.15648v1)

**Summary:** Inverse design problems are common in engineering and materials science. The forward direction, i.e., computing output quantities from design parameters, typically requires running a numerical simulation, such as a FEM, as an intermediate step, which is an optimization problem by itself. In many scenarios, several design parameters can lead to the same or similar output values. For such cases, multi-modal probabilistic approaches are advantageous to obtain diverse solutions. A major difficulty in inverse design stems from the structure of the design space, since discrete parameters or further constraints disallow the direct use of gradient-based optimization. To tackle this problem, we propose a novel inverse design method based on diffusion models. Our approach relaxes the original design space into a continuous grid representation, where gradients can be computed by implicit differentiation in the forward simulation. A diffusion model is trained on this relaxed parameter space in order to serve as a prior for plausible relaxed designs. Parameters are sampled by guided diffusion using gradients that are propagated from an objective function specified at inference time through the differentiable simulation. A design sample is obtained by backprojection into the original parameter space. We develop our approach for a composite material design problem where the forward process is modeled as a linear FEM problem. We evaluate the performance of our approach in finding designs that match a specified bulk modulus. We demonstrate that our method can propose diverse designs within 1% relative error margin from medium to high target bulk moduli in 2D and 3D settings. We also demonstrate that the material density of generated samples can be minimized simultaneously by using a multi-objective loss function....

---


<!-- ARXIV_PAPERS_END -->