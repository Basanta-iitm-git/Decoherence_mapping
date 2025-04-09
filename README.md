# Decoherence_mapping
The objective of this repository is to explore decoherence free subspaces in varied spin defect systems. The code performs following tasks:

- **Hamiltonian Diagonalization**
- Calculation of **Oscillator Strengths** pertaining to all posible transitions
- Evaluation of **Gradient**, and **Curvature** associated with various transition energies as a function of applied magnetic field with an arbitrary orientation.
- **3D Visualization** of the computed parameters

# Generic Hamiltonian
$
H = D\left(S_z^2-\frac{2}{3}\right) + \epsilon \left(S_y^2 - S_x^2\right) + \gamma_e  \mathbf{B}.\mathbf{S} + \sum_{i=1}^{3} \mathbf{S}.\mathbf{A}^i.\mathbf{I}^i +  \sum_{i=1}^{3} \gamma_{n}^i \mathbf{B}.\mathbf{I}^i + \sum_{i=1}^{3} \mathbf{I}^i.\mathbf{Q}^i.\mathbf{I}^i.
$

