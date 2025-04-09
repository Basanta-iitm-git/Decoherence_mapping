# Objective: 
The objective of this repository is to explore decoherence free subspaces in varied spin defect systems. The code performs following tasks:

- **Hamiltonian Diagonalization**
- Calculation of **Oscillator Strengths** pertaining to all posible transitions
- Evaluation of **Gradient**, and **Curvature** associated with various transition energies as a function of applied magnetic field with an arbitrary orientation.
- **3D Visualization** of the computed parameters

# Hamiltonian Structure:

The code is design to accommodate following interactions:

- Crystal field
- Electron Zeeman
- Nuclear Zeeman
- Nuclear Quadrupolar
- Electron-Nuclear Hyperfine

The generic Hamiltonian would look something like this:
$H = D\left(S_z^2-\frac{2}{3}\right) + \gamma_e  \vec{B}.\vec{S} + \vec{S}.\vec{A}.\vec{I} +  \gamma_{n} \vec{B}.\vec{I} + \vec{I}.\vec{Q}.\vec{I}$

Here, $\vec{S}$, $\vec{I}$ are electron and nuclear spin operators, respectively. D is the zero field splitting term, $\epsilon$ is the strain term, $\gamma_e$, $\gamma_n$ are the electron and nuclear gyromagnetic ratio, $\vec{A}$ is the hyperfine interaction tensor, $\vec{Q}$ is the quadrupole interaction tensor.

# Parameters:

The electronic and nuclear parameters required for Hamiltonian diagonalization are provided in this file. The current set of parameters allows for calculations pertaining to the two defect systems: 

- 


