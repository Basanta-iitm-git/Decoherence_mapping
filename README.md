# Reference:

The repository is based on the work presented in the following manuscript:

[*Identifying optimal magnetic field configurations for decoherence mitigation of boron vacancies in hexagonal boron nitride* - Basanta Mistri, Saksham Mahajan, Felix Donaldson, Rama K. Kamineni, and Siddharth Dhomkar, arXiv:2505.06574](https://arxiv.org/abs/2505.06574)

![Figure](https://github.com/Basanta-iitm-git/Decoherence_mapping/blob/main/figure.png?raw=true)

# Objective: 
The objective of this repository is to explore decoherence free subspaces in varied spin defect systems. The code performs following tasks:

- **Hamiltonian Diagonalization**
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

Here, $\vec{S}$, $\vec{I}$ are electron and nuclear spin operators, respectively. D is the zero field splitting term, $\gamma_e$, $\gamma_n$ are the electron and nuclear gyromagnetic ratio, $\vec{A}$ is the hyperfine interaction tensor, $\vec{Q}$ is the quadrupole interaction tensor.

# Methodology:

Assuming that $T_2(B)$ is inversely proportional to the frequency broadening caused by the magnetic field perturbations, its dependence on energy gradients and curvatures can be expressed as: 

$\frac{1}{T_2(B)} \approx \sqrt{\left( \frac{df}{dB} \sigma_B \right)^2 + \frac{1}{2}\left( \frac{d^2f}{dB^2} \sigma_B^2 \right)^2}$

where, $f$ is the transition frequency, $\sigma_B$ is the standard deviation of the external field noise (assuming the normal distribution), and $T_{2'}$ is related to the decoherence mechanisms due to the non-magnetic noise. 

The functions required for evaluating gradients and curvatures are presented in [decoherence_mapping_functions.py](decoherence_mapping_functions.py). **Qutip** and **Numpy** are the main libraries which have been used in the script.

# Parameters:

The electronic and nuclear parameters required for Hamiltonian diagonalization are provided in [decoherence_mapping_parameters.py](https://github.com/Basanta-iitm-git/Decoherence_mapping/blob/main/decoherence_mapping_parameters.py). The current set of parameters allows for calculations pertaining to the two defect systems: 

- Negatively charged **Nitrogen Vacancy Centers in Diamond** interacting with the host nuclear spin $\left( ^{14}N, ^{15}N \right)$ and the nuclear spins in the bath $\left(^{13}C\right)$
- Negatively charged **Boron Vacancy Centers in Hexagonal Boron Nitride** interacting with the nearest $^{14}N$ nuclear spins

In case the user wishes to work with another material system, the parameters in the file can be easily updated.

# Visualization:

Plotly based visualization example has been provided in [decoherence_mapping_example.ipynb](https://github.com/Basanta-iitm-git/Decoherence_mapping/blob/main/decoherence_mapping_example.ipynb). The example consider a negatively charged boron vacancy center in hexagonal boron nitride interacting with three nearest $^{14}N$ nuclear spins.
