---
Title: PyData Berlin 2018: On Laplacian Eigenmaps for Dimensionality Reduction
Date: 2018-07-08
Category: Geometry, Visualization
Tags: mathematics, geometry, visualization
slug: laplacian_eigenmaps_dim_red
Authors: Juan Camilo Orduz
Summary: This post contains the slides and material from a talk I gave at PyData Berlin 2018.
---

This summer I had the great oportunity to attend an give a talk at [Pydata Berlin 2018](https://pydata.org/berlin2018/). The topic of my talk was [On Laplacian Eigenmaps for Dimensionality Reduction](https://pydata.org/berlin2018/schedule/presentation/33/). 

---

**Abstract**

The aim of this talk is to describe a non-linear dimensionality reduction algorithm based on spectral techniques introduced in [BN2003](http://web.cse.ohio-state.edu/~belkin.8/papers/LEM_NC_03.pdf). The goal of non-linear dimensionality reduction algorithms, so called {\em manifold learning algorithms}, is to construct a representation of data on a low dimensional manifold embedded in a high dimensional space. The particular case we are going to present exploits various relations of geometric and spectral methods (discrete and continuous). Spectral methods are sometimes motivated by Marc Kac's question  *Can One Hear the Shape of a Drum?* which makes reference to the idea of recovering geometrical properties from the eigenvalues (spectrum) of a matrix (linear operator). Concretely, the approach followed in [BN2003](http://web.cse.ohio-state.edu/~belkin.8/papers/LEM_NC_03.pdf) has its foundation on the spectral analysis of the graph Laplacian of the adjacency graph constructed from the data. The motivation of the construction relies on the continuous limit analogue, the Laplace-Beltrami operator, in providing an optimal embedding for manifolds. We will also indicate the relation with the associated heat kernel operator. Instead of following a pure formal approach we will present the main geometric and computational ideas of the algorithm. Hence, with basic knowledge of linear algebra (eigenvalues) and differential calculus you will be able to follow the talk. Finally we will show a concrete example in Python using scikit-learn.

---

**Slides**

[Here]({filename}/documents/orduz_pydata2018.pdf) you can find the slides of the talk. 

Suggestions and comments are always welcome!

---

**Notebook**

{% notebook spectral_embedding.ipynb %}


