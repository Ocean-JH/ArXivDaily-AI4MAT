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

*Last updated: 2025-04-30 16:30:05 (SGT)*

### 1. 3D variational autoencoder for fingerprinting microstructure volume elements

**Authors:** Michael D. White, Michael D. Atkinson, Adam J. Plowman, Pratheek Shanthraj

**Published:** 2025-03-21

**Category:** cond-mat.mtrl-sci

**ID:** 2503.17427v2

**Link:** [http://arxiv.org/abs/2503.17427v2](http://arxiv.org/abs/2503.17427v2)

**Summary:** Microstructure quantification is an important step towards establishing
structure-property relationships in materials. Machine learning-based image
processing methods have been shown to outperform conventional image processing
techniques and are increasingly applied to microstructure quantification tasks.
In this work, we present a 3D variational autoencoder (VAE) for encoding
microstructure volume elements (VEs) comprising voxelated crystallographic
orientation data. Crystal symmetries in the orientation space are accounted for
by mapping to the crystallographic fundamental zone as a preprocessing step,
which allows for a continuous loss function to be used and improves the
training convergence rate. The VAE is then used to encode a training set of VEs
with an equiaxed polycrystalline microstructure with random texture. Accurate
reconstructions are achieved with a relative average misorientation error of
9x10-3 on the test dataset, for a continuous latent space with dimension 256.
We show that the model generalises well to microstructures with textures, grain
sizes and aspect ratios outside the training distribution. Structure-property
relationships are explored through using the training set of VEs as initial
configurations in various crystal plasticity (CP) simulations. Microstructural
fingerprints extracted from the VAE, which parameterise the VEs in a
low-dimensional latent space, are stored alongside the volume-averaged stress
response, at each strain increment, to uniaxial tensile deformation from CP
simulations. This is then used to train a fully connected neural network
mapping the input fingerprint to the resulting stress response, which acts as a
surrogate model for the CP simulation. The fingerprint-based surrogate model is
shown to accurately predict the microstructural dependence in the CP stress
response, with a relative mean-squared error of 8.9x10-4 on unseen test data....

---


<!-- ARXIV_PAPERS_END -->