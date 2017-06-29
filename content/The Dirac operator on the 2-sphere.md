---
Title: The Dirac operator on the 2-sphere
Date: 2017-06-29
Category: Geometry
Tags: mathematics, geometry 
slug: dirac_sphere
Authors: Juan Camilo Orduz
Summary: summary
---


The objective of this post is to explore [MathJax](http://docs.mathjax.org/en/latest/index.html), a JavaScript display engine for LaTeX. Being my first post writen with this tool, I want to present a short but fun example: I will give a description of the explicit computation of the [spin-Dirac](https://en.wikipedia.org/wiki/Dirac_operator) operator (of the unique complex spinor bundle!) on the 2-sphere \\(S^2\\) equipped with the standar round metric. A more detailed treatment can be found in my expository [paper](https://arxiv.org).

## The Levi-Civita connection

Let us consider a 2-sphere of radius $r>0$,

\begin{equation*}
S^{2}(r):= \{(x_1,x_2,x_3) \: | \: x_1^2+x_2^2+x_3^2=r^{2}\}\subset\mathbb{R}^3
\end{equation*}

equipped with the induced Riemanian metric from \\(\mathbb{R}^3\\). With respect to a local parametrization given by polar coordinates

\begin{align*}
x_1(r,\theta,\phi)=&\cos\phi\sin\theta,\\
x_2(r,\theta,\phi)=&\sin\phi\sin\theta,\\
x_3(r,\theta,\phi)=&\cos\theta,
\end{align*}


where $0<\theta<\pi$ and $0<\phi<2\pi$, the metric can be written as 

\begin{align*}
g^{TS^2(r)}=r^2d\theta^2+r^2\sin^{2}\theta d\phi^2.
\end{align*}

A straight forward computation shows that for the Levi-Civita connection we have 

\begin{align*}
\nabla_{\partial_\theta}\partial_{\theta}=&0,\\
\nabla_{\partial_\phi}\partial_\phi=&-\sin\theta\cos\theta\partial_\theta,\\
\nabla_{\partial_\theta}\partial_\phi=&\cot\theta\partial_\phi,\\
\nabla_{\partial_\phi}\partial_\theta=&\cot\theta\partial_\phi.
\end{align*}

Indeed, the Christoffel symbols are

\begin{align*}
\Gamma_{\phi\phi}^{\theta}=&\frac{1}{2r^2}(-\partial_\theta (r^2\sin^2\theta))=-\sin\theta\cos\theta,\\
\Gamma_{\theta\phi}^{\phi}=&\frac{1}{2r^2\sin^2\theta}(\partial_\theta (r^2\sin^2\theta))=\cot\theta.
\end{align*}

## The curvature form

Let us consider the following local orthonotmal basis for $TS^2(r)$,

\begin{align*}
e_1:=&\frac{\partial_\theta}{r},\\
e_2:=&\frac{\partial_\phi}{r\sin\theta},
\end{align*}


with associated dual basis 

\begin{align*}
e^1:=&rd\theta,\\
e^2:=&r\sin\theta d\theta.
\end{align*}

With respect to this basis the volume form is \\(vol_{S^2(r)}=e^1\wedge e^2\\). To be precise we consider the orientation such that 
$vol_{\mathbb{R}^3}=rdr\wedge vol_{S^2(r)}$. For further reference we compute the exterior derivative 

\begin{align*}
de^1=&0,\\
de^2=& d(r\sin\theta d\phi)=r\cos\theta d\theta\wedge d\phi=\frac{\cot\theta}{r} e^1\wedge e^2. 
\end{align*}

We now calculate the components $\omega_{ij}$ of the connection $1$-form associated with this basis, which are defined by the relations

\begin{align*}
\nabla  e_j=:\omega_{ij}\otimes e_i, 
\end{align*}

where the sum over repeated indices is understood. From the expression of the [Levi-Civita connection](https://en.wikipedia.org/wiki/Levi-Civita_connection) we verify

\begin{align*}
\nabla_{e_1}e_1=&0,\\
\nabla_{e_1}e_2=&\partial_\theta\left(\frac{1}{r^2\sin\theta}\right)\partial_\phi+\left(\frac{1}{r^2\sin\theta}\right)\nabla_{\partial_\theta}\partial_\phi=-\frac{\cos\theta}{r^2}\partial_\phi+\frac{\cos\theta}{r^2}\partial_\phi =0,\\
\nabla_{e_2}e_1=&\left(\frac{1}{r^2\sin\theta}\right)\nabla_{\partial_\phi}\partial_\theta=\left(\frac{1}{r^2\sin\theta}\right)\cot\theta\partial_\phi=\frac{\cot\theta}{r}e_2,\\
\nabla_{e_2}e_2=&\left(\frac{1}{r\sin\theta}\right)^2\nabla_{\partial_\phi}\partial_\phi=-\left(\frac{1}{r\sin\theta}\right)^2\sin\theta\cos\theta\partial_\theta=-\frac{\cot\theta}{r} e_1.\\
\end{align*}


Thus

\begin{align*}
\omega_{12}=-\omega_{21}=-\frac{\cot\theta}{r} e^2. 
\end{align*}

Since the Levi-Civita connection is compatible with metric then $\omega_{ij}=-\omega_{ji}$. In addition, since it is also torsion-free then the components satisfy the structure equations 

\begin{align*}
de^i+\omega_{ij}\wedge e^j=0. 
\end{align*}

Note for example for $i=2$,

\begin{align*}
de^2+\omega_{21}\wedge e^1=\frac{\cot\theta}{r}e^1\wedge e^2+\frac{\cot\theta}{r}e^2\wedge e^1=0. 
\end{align*}

From the components of the connection 1-form we can compute the components \\(\Omega_{ij}\\) of the curvature using the relation 

\begin{align*}
\Omega_{ij}=d\omega_{ij}+\omega_{ik}\wedge\omega_{kj}. 
\end{align*}


In this particular case we have

\begin{align*}
\Omega_{12}=&d\omega_{12}=\frac{\csc^2\theta}{r^2} e^1\wedge e^2-\frac{\cot\theta}{r} de^2=\frac{\csc^2\theta}{r^2} e^1\wedge e^2-\frac{\cot^2\theta}{r^2} e^1\wedge e^2=\frac{1}{r^2}e^1\wedge e^2.
\end{align*}

### The Gauß-Bonnet Theorem

If we integrate the 2-form \\(\Omega_{12}/2\pi\\) over \\(S^2(r)\\) we obtain

\begin{equation}\label{Eq:GB}
\int_{S^{2}(r)}\frac{\Omega_{12}}{2\pi}=\frac{1}{2\pi r^2}\int_{S^{2}(r)}e^1\wedge e^2=\frac{4\pi r^2}{2\pi r^2}=2,
\end{equation}

which verifies the [Gauß-Bonnet theorem](https://en.wikipedia.org/wiki/Gauss–Bonnet_theorem) since the [Euler characteristic](https://en.wikipedia.org/wiki/Euler_characteristic) \\(\chi(S^{2}(r))=2\\) for any $r>0$. 

## Spin strucrure

A topological condition for the existence of [spin structures](https://en.wikipedia.org/wiki/Spin_structure) is the vanishing of the second 
[Stiefel-Whitney](https://en.wikipedia.org/wiki/Stiefel–Whitney_class) class $w_2(TS^2)\in H^2(S^2;\mathbb{Z}/2\mathbb{Z})$. This characteristic class is the $\mathbb{Z}/2\mathbb{Z}$-reduction of the Euler class of $TS^2$. By the Gauß-Bonnet theorem (see \eqref{Eq:GB})we know that the integral of this Euler class equals the Euler characteristic $\chi(S^2)=2$, which modulo $\mathbb{Z}/2\mathbb{Z}$ is zero. This shows that $S^2$ is a spin manifold. Moreover, the spin structures are classified by the group $H^1(S^2;\mathbb{Z}/2\mathbb{Z})=0$, so we conclude that $S^2$ has only one spin structure. This result is actually valid for all spheres.

## The spinor bundle

Now we construct the [spinor bundle](https://en.wikipedia.org/wiki/Spinor_bundle) $\Sigma(S^2)$ as an associated bundle $\Sigma(S^2)=Spin(S^2)\times_{\rho_2}\Sigma_2$ where, $Spin(S^2)$ the principal $Spin$-bundle correspinding to the unique spin structure, $\rho_2:S^1\longrightarrow \text{Aut}(\Sigma_2)$ is the [spin representation](https://en.wikipedia.org/wiki/Spin_representation) and $\Sigma_2=\mathbb{C}^2$ is the spinor space. 

To begin with we describe the spin representation of the Clifford algebra $Cl(2)$ on the spinor vector space $\Sigma_2=\mathbb{C}^{2}$. To to so its enough to describe the action on basis elements. Recall the definition of the [Pauli matrices](https://en.wikipedia.org/wiki/Pauli_matrices),

\begin{align*}
\sigma_1:=\left(
\begin{array}{cc}
0 & 1\\
1 & 0
\end{array}
\right),\quad\quad
\sigma_2:=\left(
\begin{array}{cc}
0 & -i\\
i & 0
\end{array}
\right),\quad\quad
\sigma_3:=\left(
\begin{array}{cc}
1 & 0\\
0 & -1
\end{array}
\right).
\end{align*}

These matrices satisfy the relations

\begin{align*}
\sigma_j^\dagger=&\sigma_j,\\
\sigma_j^2=&1,\\
\sigma_1\sigma_2=&i\sigma_3,\\
\sigma_j\sigma_k+\sigma_k\sigma_j=&2\delta_{jk}\quad\text{for $j=1,2,3$}.
\end{align*}

Let $\{v_1,v_2\}$ be the standard orthonormal basis of $\mathbb{R}^2$, we define the Clifford action $\rho_2(v_j):=-i\sigma_j$ for $j=1,2$. It then follows 

\begin{align*}
\rho_2(v_j)\rho_2(v_k)+\rho_2(v_k)\rho_2(v_j)=-2\delta_{jk}.
\end{align*}

We now want to study the restriction of this representation to $Spin(2)\subset Cl(2)$. Note that every element of $Spin(2)$ can be written as 

\begin{align*}
\cos t+\sin t v_1v_2=-(\sin(t/2)v_1+\cos(t/2)v_2)(\cos(t/2)v_1+\sin(t/2)v_2),
\end{align*}

for $t\in[0,2\pi]$, so

\begin{align*}
\rho_2(\cos t+\sin t v_1v_2)=&
\left(
\begin{array}{cc}
1 & 0\\
0 & 1
\end{array}
\right)\cos t
+\left(
\begin{array}{cc}
-i & 0\\
0 & i
\end{array}
\right)\sin t=
\left(
\begin{array}{cc}
e^{-it} & 0\\
0 & e^{it}
\end{array}
\right).
\end{align*}


This shows that the spin representation restricted to $Spin(2)=S^1$ is given by

\begin{align*}
\rho_2(z)
=
\left(
\begin{array}{cc}
\bar{z} & 0\\
0 & z
\end{array}
\right).
\end{align*}


We now compute the transition functions of the spinor bundle $\Sigma(S^2)=Spin(S^2)\times_{\rho_2}\Sigma_2$. These are obtained by composing the transition functions of the [Hopf bundle](https://en.wikipedia.org/wiki/Hopf_fibration) $\pi:S^3\subset\mathbb{C}^2\longrightarrow S^2$ (which defines the Spin structure on $S^2$) with $\rho_2$, i.e. for $\pi(z_0,z_1)\in U_N\cap U_S=S^1$ we have

\begin{equation*}
\rho_2(\pi(z_0,z_1))=\rho_2\left(\frac{z_0}{z_1}\right)=
\left(
\begin{array}{cc}
z_0/z_1 & 0\\
0 & \bar{z}_0/\bar{z}_1
\end{array}
\right).
\end{equation*}

Here $U_N$ and $U_S$ denote the north and south hemisphere of $S^2$ respectively. 

We now sketch the proof to show that the spinor bundle $\Sigma(S^2)$ is trivial. The argument goes into the direction of clutching functions in [K-theory](https://en.wikipedia.org/wiki/K-theory). Let  $\text{Vect}_\mathbb{C}^k(S^2)$ denote the monoid of isomorphims classes of complex vector bundles of rank $k$ over $S^2$. An important result in the context of classification of vector bundles states that the map $\Phi:[S^1,GL(k,\mathbb{C})]\longrightarrow \text{Vect}_\mathbb{C}^k(S^2)$ defined by the transition functions (clutching functions) is a bijection. Here $[S^1,GL(k,\mathbb{C})]$ denotes the space of maps up to homotopy. Moreover, as groups we have an isomorphism  $[S^1,GL(k,\mathbb{C})]\cong [S^1,U(k,\mathbb{C})]\cong\mathbb{Z}$, the first one given by the  Gram-Schmidt orthogonalization process and the second one because of the known computation of the fundamental group for the unitary group. One also verifies that the determinant $det:[S^1,U(k,\mathbb{C})]\longrightarrow S^1$ is well defined and the degree of it $deg\circ det:[S^1,U(k,\mathbb{C})] \longrightarrow\mathbb{Z}$ is actually an isomorphism. This means that the degree of the determinant of the clutching functions characterizes the isomorphism class of the associated vector bundle. This argument shows, in view of 

\begin{align*}
\det\left(
\begin{array}{cc}
\bar{z} & 0\\
0 & z
\end{array}
\right)=\bar{z}z=1,
\end{align*}

for $z\in S^1$, that the associated bundle of this clutching function must be isomorphic to the trivial bundle. One can actually define an explicit homotopy for $t\in[0,\pi/2]$,

\begin{align*}
\gamma(t):=\left(
\begin{array}{cc}
\bar{z} & 0\\
0 & 1
\end{array}
\right)
\left(
\begin{array}{cc}
\cos t & \sin t\\
-\sin t & \cos t
\end{array}
\right)
\left(
\begin{array}{cc}
1 & 0\\
0 & z
\end{array}
\right)
\left(
\begin{array}{cc}
\cos t & -\sin t\\
\sin t & \cos t
\end{array}
\right).
\end{align*}

Observe that $det(\gamma(t))=1$ for all $$t\in[0,\pi/2]$ and 

\begin{align*}
\gamma(0)=
\left(
\begin{array}{cc}
\bar{z} & 0\\
0 & z
\end{array}
\right)
\quad\text{and}\quad
\gamma(\pi/2)=\left(
\begin{array}{cc}
1& 0\\
0 & 1
\end{array}
\right). 
\end{align*}

As a consequence, the sections of $\Sigma(S^2)$, called *spinors*, can be regarded as functions $\psi:S^2\longrightarrow \mathbb{C}^2$.

## The Dirac operator

We now want to construct the Dirac operator ${D}_{S^2(r)}$ associated to the Clifford bundle $\Sigma(S^2)$. This operator is defined by the formula 

\begin{align*}
{D}_{S^2(r)}:=\rho_2(e_1)\nabla^\Sigma_{e_{1}}+\rho_2(e_2)\nabla^\Sigma_{e_{2}}, 
\end{align*}


where $\{e_1,e_2\}$ is the orthonormal basis defined above and $\nabla^\Sigma$ is the [spin connection](https://en.wikipedia.org/wiki/Spin_connection) induced by the Levi-Civita connection and the spin representation. This connection can be computed using the component of the connection $1$-form as 

\begin{align*}
\nabla^{\Sigma}=\frac{1}{2}\omega_{21}\otimes\rho_2(e_1)\rho_2(e_2)=-\frac{1}{2}\omega_{12}\otimes\sigma_2\sigma_1=-\frac{i}{2}\frac{\cot\theta}{r}e^2\otimes\sigma_3.
\end{align*}

Applying the Clifford action we get 

\begin{align*}
-i\sigma_1\nabla^\Sigma_{e_1}=&-i\sigma_1e_1,\\
-i\sigma_2\nabla^\Sigma_{e_2}=&-i\sigma_2e_2-\frac{1}{2}\frac{\cot\theta}{r}\sigma_2\sigma_3=-i\sigma_2e_2-\frac{i}{2}\frac{\cot\theta}{r}\sigma_1,
\end{align*}

so we obtain 

\begin{align*}
{D}_{S^2(r)}=-i\sigma_1\nabla^\Sigma_{e_1}-i\sigma_2\nabla^\Sigma_{e_2}=-i\sigma_1\left(e_1+\frac{1}{2}\frac{\cot\theta}{r}\right)-i\sigma_2e_2.
\end{align*}

*Remark*: Note that as $r\longrightarrow +\infty$, the Dirac operator becomes $-i\sigma_1 e_1 - i\sigma_2 e_2$, which is the spin-Dirac operator on $\mathbb{R}^2$.

In terms of the coordinate vector fields we can write 

\begin{align*}
{D}_{S^2(r)}=-i\sigma_1\left(\frac{1}{r}\partial_\theta+\frac{1}{2}\frac{\cot\theta}{r}\right)-\frac{i\sigma_2}{r\sin\theta}\partial_\phi.
\end{align*}

## Lichnerowicz formula

Let $\Delta^{\Sigma} := (\nabla^{\Sigma})^{*}\nabla^{\Sigma}$ be the spinor Laplacian, then the [Lichnerowicz formula](https://en.wikipedia.org/wiki/Lichnerowicz_formula) takes the form

$$
D^2_{S^2(r)} = \Delta^{\Sigma} + \frac{scal}{4} = \Delta^{\Sigma} + \frac{1}{2r^2}, 
$$

where $scal$ is the the [scalar curvature](https://en.wikipedia.org/wiki/Scalar_curvature) and equals $scal=2/r^2$ for the sphere.

## The spectrum

The spin-Dirac operator is a first order, self-adjoint elliptic operator, which implies (as $S^2$ is compact) that it has a discrete spectrum. The eigenvalues of $D_{S^2}$ are given by $\pm(k+1)$, for $k\geq 0$, with multiplicities 

\begin{equation*}
2\left(
\begin{array}{c}
k+1\\
k
\end{array}
\right).
\end{equation*}

This can be deduced from the work of [Christian Bär](https://www.math.uni-potsdam.de/fileadmin/user_upload/Prof-Geometrie/Dokumente/Publikationen/sphere.pdf).
 

## The Fredholm index

The chirality operator of associated to the spinor bundle $\Sigma(S^2)$ is 

\begin{align*}
\Gamma=i(-i\sigma_1)(-i\sigma_2)=\sigma_3. 
\end{align*}

Since the dimension of $S^2$ is even we can verify that ${D}_{S^2(r)}\sigma_3+\sigma_3{D}_{S^2(r)}=0$. With respect to $$\Gamma$$ we can therefore decompose 

\begin{equation*}
D_{S^2(r)} =
\left(
\begin{array}{cc}
0 & D_{S^2(r)}^{-}\\
D_{S^2(r)}^{+} & 0
\end{array}
\right). 
\end{equation*}

Finally, by the [Atiyah-Singer Index Theorem](https://en.wikipedia.org/wiki/Atiyah–Singer_index_theorem), we have $\text{ind}(D_{S^2(r)}^{+})=0$ as the $\widehat{A}$-polynomial is a polynomial in the [Pontryagin classes](https://en.wikipedia.org/wiki/Pontryagin_class) which are of degree $4j$, for $j\in\mathbb{N}_0$.

