# Causality Testing Overview

## Idea:
- We have no way of computationally determining whether a signal is a leading or lagging indicator of another.
- We have no way of measuring if events **cause** changes in a continuous time series.
- **Current Best:** Pearson's Correlation
  - Not a good metric for causality. Why?
  - **Correlation doesn't imply causation.**
  - Key difference: Symmetry.

## Key Overviews of Causality Testing:
- **Granger:** 
  - Create two models - one with a variable and one without. Check if the error on the model without the variable increases.
- **Transfer Entropy:** 
  - Information theoretic-based but relatively unfamiliar.
- **Convergent Cross Mapping:** 
  - Similar to Anavi's TDA pitch except less weird. Due to some arbitrary theorem in topology, we can essentially create "manifolds" of our two time series, and if the points in the manifold that are physically close are also temporally close, we can claim causality.

## Pitch Tasks:
- **Explain two or three of the causality measures**
  - **High-level Overview of the Causality Tests**
  - **ASSUMPTIONS AND CONDITIONS**
  - **Potential Downfalls on Different Types of Data**
- **Testing on Simulated Data**
  - Lorenz attractor
  - Lotka Volterra system
- **Testing on Polygon Data**
  - Paper linked on how to correctly deal with financial time series data with TE and CCM: [Read more](https://arxiv.org/html/2312.16185v1)
  - Brainstorm which stocks/options are causal
  - TRIAL ON NEWS EVENTS/OTHER BERNOULLI EVENT
- **Well-documented code**
  - Create lasting API that can be used on future stock pitches
