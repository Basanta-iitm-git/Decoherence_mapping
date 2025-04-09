#Impoting all the libraries
from qutip import tensor,qeye
import numpy as np
from tqdm.notebook import trange
from joblib import Parallel, delayed
from plotly import graph_objs as go
from plotly.subplots import make_subplots
from decoherence_mapping_parameters import nuclear, electronic

def generalized_operators(electron, nuclei):
    """
    Generate spin operators for composite system using tensor products
    
    Args:
        electron: Central spin system with Sx, Sy, Sz attributes
        nuclei: List of nuclear spin systems with Ix, Iy, Iz attributes
    
    Returns:
        Tuple: (S_operators, [I_operators_list])
    """
    # Central spin operators
    S_op = [
        tensor(electron.Sx, *[qeye(n.dimension) for n in nuclei]),
        tensor(electron.Sy, *[qeye(n.dimension) for n in nuclei]),
        tensor(electron.Sz, *[qeye(n.dimension) for n in nuclei])
        ]
    
    # Nuclear spin operators
    I_ops = []
    for i, nuc in enumerate(nuclei):
        Ix = tensor(qeye(electron.dimension), *[qeye(n.dimension) if j != i else nuc.Ix for j, n in enumerate(nuclei)])
        Iy = tensor(qeye(electron.dimension), *[qeye(n.dimension) if j != i else nuc.Iy for j, n in enumerate(nuclei)])
        Iz = tensor(qeye(electron.dimension), *[qeye(n.dimension) if j != i else nuc.Iz for j, n in enumerate(nuclei)])
        I_ops.append((Ix, Iy, Iz))
    
    return S_op, I_ops

def generalized_hamiltonian(electron, nuclei, Bx, By, Bz):
    """
    Build complete Hamiltonian for central spin + multiple nuclei
    
    Args:
        electron: Central spin system with parameters
        nuclei: List of nuclear spin systems with parameters
        B: Magnetic field vector (Bx, By, Bz)
    
    Returns:
        Qobj: Full system Hamiltonian
    """
    S, I_list = generalized_operators(electron, nuclei)
    
    # Central spin terms
    H = (electron.D * (S[2]**2 - 2/3) + electron.E * (S[1]**2 - S[0]**2) -electron.g * (S[0]*Bx + S[1]*By + S[2]*Bz))
    
    # Add nuclear terms
    for i, (nuc, (Ix, Iy, Iz)) in enumerate(zip(nuclei, I_list)):
        # Hyperfine interaction
        H += nuc.A_xx * S[0] * Ix + nuc.A_yy * S[1] * Iy + nuc.A_zz * S[2] * Iz
        
        # Nuclear Zeeman
        H -= nuc.g * (Ix*Bx + Iy*By + Iz*Bz)
        
        # Quadrupole interaction
        H += nuc.Q_xx * Ix**2 + nuc.Q_yy * Iy**2 + nuc.Q_zz * Iz**2
        
    return H

def compute_eigenvalues_for_point(system, i, B_arr, neighbour_arr, generalized_hamiltonian):
    
    # Compute eigenvalues for central point
    # Central Hamiltonians
    H = generalized_hamiltonian(system[0], system[1], B_arr[0, i], B_arr[1, i], B_arr[2, i])
    H_0 = generalized_hamiltonian(system[0], system[1], 0, 0, 0)
    eigenvalues_point = np.zeros((neighbour_arr.shape[0] + 1, H.shape[0]))
    eigenvalues_point[0, :] = (np.sort(H.eigenstates()[0]) - np.sort(H_0.eigenstates()[0])[0])
    
    # Compute eigenvalues for neighbor points
    for k in range(neighbour_arr.shape[0]):
        H = generalized_hamiltonian(system[0], system[1], neighbour_arr[k, 0, i], neighbour_arr[k, 1, i], neighbour_arr[k, 2, i])
        eigenvalues_point[k + 1, :] = (np.sort(H.eigenstates()[0]) - np.sort(H_0.eigenstates()[0])[0])
    
    return eigenvalues_point


def energy_curvature(system, B_arr, neighbour_arr, generalized_hamiltonian, n_jobs=-1):
    # Use joblib to parallelize the outer loop
    results = Parallel(n_jobs=n_jobs)(delayed(compute_eigenvalues_for_point)(system, i, B_arr, neighbour_arr, generalized_hamiltonian)
                                      for i in trange(neighbour_arr.shape[2]))
    
    # Stack results into a single array
    eigenvalues = np.stack(results)
    return eigenvalues

# mean curvature
def curvature_transition_energy(system, B_arr, neighbour_arr, generalized_hamiltonian):
    Energies = energy_curvature(system, B_arr, neighbour_arr, generalized_hamiltonian, n_jobs=-1)
    # Extract field step sizes from arr (predefined bias fields)
    delta_Bx, delta_By, delta_Bz = 0.1e-3, 0.1e-3, 0.1e-3  # 0.1e-3
    
    # Initialize arrays with proper dimensions
    array_size = int(Energies.shape[2]/3)
    Trans_Eng_1 = np.zeros((neighbour_arr.shape[2], array_size, array_size), dtype=np.float32)
    Trans_Eng_2 = np.zeros((neighbour_arr.shape[2], array_size, array_size), dtype=np.float32)
    Trans_Eng_3 = np.zeros((neighbour_arr.shape[2], array_size, array_size), dtype=np.float32)
    gradient1 = np.zeros_like(Trans_Eng_1)
    gradient2 = np.zeros_like(Trans_Eng_2)
    gradient3 = np.zeros_like(Trans_Eng_3)
    curvature1 = np.zeros_like(Trans_Eng_1)
    curvature2 = np.zeros_like(Trans_Eng_2)
    curvature3 = np.zeros_like(Trans_Eng_3)
    # Initialize arrays with proper dimensions
    array_size = Energies.shape[2] // 3  # Ensuring integer division
    m = Energies.shape[-1] // 3  # Integer division for valid indexing
    
    for k in range(array_size):
        for l in range(array_size): 
            # First derivatives (central differences)
            #for ms=0 to ms=-1 transition
            df_dBx_1 = ((Energies[:,1,m+l] - Energies[:,2,m+l]) - (Energies[:,1,k] - Energies[:,2,k])) / (2*delta_Bx)
            df_dBy_1 = ((Energies[:,3,m+l] - Energies[:,4,m+l]) - (Energies[:,3,k] - Energies[:,4,k])) / (2*delta_By)           
            df_dBz_1 = ((Energies[:,5,m+l] - Energies[:,6,m+l]) - (Energies[:,5,k] - Energies[:,6,k])) / (2*delta_Bz)
            #for ms=0 to ms=1 transition
            df_dBx_2 = ((Energies[:,1,(2*m)+l]-Energies[:,1,k])-(Energies[:,2,(2*m)+l]-Energies[:,2,k])) / (2*delta_Bx)
            df_dBy_2 = ((Energies[:,3,(2*m)+l]-Energies[:,3,k])-(Energies[:,4,(2*m)+l]-Energies[:,4,k])) / (2*delta_By)
            df_dBz_2 = ((Energies[:,5,(2*m)+l]-Energies[:,5,k])-(Energies[:,6,(2*m)+l]-Energies[:,6,k])) / (2*delta_Bz)
            #for ms=-1 to ms=1 transition
            df_dBx_3 = ((Energies[:,1,(2*m)+l]-Energies[:,1,m+k])-(Energies[:,2,(2*m)+l]-Energies[:,2,m+k])) / (2*delta_Bx)
            df_dBy_3 = ((Energies[:,3,(2*m)+l]-Energies[:,3,m+k])-(Energies[:,4,(2*m)+l]-Energies[:,4,m+k])) / (2*delta_By)
            df_dBz_3 = ((Energies[:,5,(2*m)+l]-Energies[:,5,m+k])-(Energies[:,6,(2*m)+l]-Energies[:,6,m+k])) / (2*delta_Bz)
            
            # Second derivatives (central differences)
            #for ms=0 to ms=-1 transition
            d2f_dBx2_1 = ((Energies[:,1,m+l] - 2*Energies[:,0,m+l] + Energies[:,2,m+l]) - (Energies[:,1,k] - 2*Energies[:,0,k] + Energies[:,2,k])) / delta_Bx**2           
            d2f_dBy2_1 = ((Energies[:,3,m+l] - 2*Energies[:,0,m+l] + Energies[:,4,m+l]) - (Energies[:,3,k] - 2*Energies[:,0,k] + Energies[:,4,k])) / delta_By**2            
            d2f_dBz2_1 = ((Energies[:,5,m+l] - 2*Energies[:,0,m+l] + Energies[:,6,m+l]) - (Energies[:,5,k] - 2*Energies[:,0,k] + Energies[:,6,k])) / delta_Bz**2
            #for ms=0 to ms=1 transition
            d2f_dBx2_2 = ((Energies[:,1,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,2,(2*m)+l]) - (Energies[:,1,k] - 2*Energies[:,0,k] + Energies[:,2,k])) / delta_Bx**2           
            d2f_dBy2_2 = ((Energies[:,3,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,4,(2*m)+l]) - (Energies[:,3,k] - 2*Energies[:,0,k] + Energies[:,4,k])) / delta_By**2            
            d2f_dBz2_2 = ((Energies[:,5,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,6,(2*m)+l]) - (Energies[:,5,k] - 2*Energies[:,0,k] + Energies[:,6,k])) / delta_Bz**2
            #for ms=-1 to ms=1 transition
            d2f_dBx2_3 = ((Energies[:,1,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,2,(2*m)+l]) - (Energies[:,1,m+k] - 2*Energies[:,0,m+k] + Energies[:,2,m+k])) / delta_Bx**2           
            d2f_dBy2_3 = ((Energies[:,3,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,4,(2*m)+l]) - (Energies[:,3,m+k] - 2*Energies[:,0,m+k] + Energies[:,4,m+k])) / delta_By**2            
            d2f_dBz2_3 = ((Energies[:,5,(2*m)+l] - 2*Energies[:,0,(2*m)+l] + Energies[:,6,(2*m)+l]) - (Energies[:,5,m+k] - 2*Energies[:,0,m+k] + Energies[:,6,m+k])) / delta_Bz**2
            
            # Cross derivatives (mixed derivatives)
            #for ms=0 to ms=-1 transition
            d2f_dBxdBy_1 = ((Energies[:,7,m+l] -  Energies[:,8,m+l] -  Energies[:,9,m+l] +  Energies[:,10,m+l]) - (Energies[:,7,k] -  Energies[:,8,k] -  Energies[:,9,k] +  Energies[:,10,k])) / (4*delta_Bx*delta_By)
            d2f_dBxdBz_1 = ((Energies[:,11,m+l] - Energies[:,12,m+l] - Energies[:,13,m+l] + Energies[:,14,m+l]) - (Energies[:,11,k] - Energies[:,12,k] - Energies[:,13,k] + Energies[:,14,k])) / (4*delta_Bx*delta_Bz)
            d2f_dBydBz_1 = ((Energies[:,15,m+l] - Energies[:,16,m+l] - Energies[:,17,m+l] + Energies[:,18,m+l]) - (Energies[:,15,k] - Energies[:,16,k] - Energies[:,17,k] + Energies[:,18,k])) / (4*delta_By*delta_Bz)
            #for ms=0 to ms=1 transition
            d2f_dBxdBy_2 = ((Energies[:,7,(2*m)+l] -  Energies[:,8,(2*m)+l] -  Energies[:,9,(2*m)+l] +  Energies[:,10,(2*m)+l]) - (Energies[:,7,k] -  Energies[:,8,k] -  Energies[:,9,k] +  Energies[:,10,k])) / (4*delta_Bx*delta_By)
            d2f_dBxdBz_2 = ((Energies[:,11,(2*m)+l] - Energies[:,12,(2*m)+l] - Energies[:,13,(2*m)+l] + Energies[:,14,(2*m)+l]) - (Energies[:,11,k] - Energies[:,12,k] - Energies[:,13,k] + Energies[:,14,k])) / (4*delta_Bx*delta_Bz)
            d2f_dBydBz_2 = ((Energies[:,15,(2*m)+l] - Energies[:,16,(2*m)+l] - Energies[:,17,(2*m)+l] + Energies[:,18,(2*m)+l]) - (Energies[:,15,k] - Energies[:,16,k] - Energies[:,17,k] + Energies[:,18,k])) / (4*delta_By*delta_Bz)
            #for ms=-1 to ms=1 transition
            d2f_dBxdBy_3 = ((Energies[:,1,(2*m)+l] - Energies[:,2,(2*m)+l] - Energies[:,3,(2*m)+l] + Energies[:,4,(2*m)+l]) - (Energies[:,1,m+k] - Energies[:,2,m+k] - Energies[:,3,m+k] + Energies[:,4,m+k])) / (4*delta_Bx*delta_By)
            d2f_dBxdBz_3 = ((Energies[:,1,(2*m)+l] - Energies[:,2,(2*m)+l] - Energies[:,5,(2*m)+l] + Energies[:,6,(2*m)+l]) - (Energies[:,1,m+k] - Energies[:,2,m+k] - Energies[:,5,m+k] + Energies[:,6,m+k])) / (4*delta_Bx*delta_Bz)
            d2f_dBydBz_3 = ((Energies[:,3,(2*m)+l] - Energies[:,4,(2*m)+l] - Energies[:,5,(2*m)+l] + Energies[:,6,(2*m)+l]) - (Energies[:,3,m+k] - Energies[:,4,m+k] - Energies[:,5,m+k] + Energies[:,6,m+k])) / (4*delta_By*delta_Bz)

            # Curvature calculation
            numerator1   = (df_dBy_1**2 + df_dBz_1**2) * d2f_dBx2_1 + (df_dBx_1**2 + df_dBz_1**2) * d2f_dBy2_1 + (df_dBx_1**2 + df_dBy_1**2) * d2f_dBz2_1 + 2 * df_dBx_1 * df_dBy_1 * d2f_dBxdBy_1 + 2 * df_dBx_1 * df_dBz_1 * d2f_dBxdBz_1 + 2 * df_dBy_1 * df_dBz_1 * d2f_dBydBz_1
            denominator1 = 2 * (df_dBx_1**2 + df_dBy_1**2 + df_dBz_1**2)**(1.5)
            numerator2   = (df_dBy_2**2 + df_dBz_2**2) * d2f_dBx2_2 + (df_dBx_2**2 + df_dBz_2**2) * d2f_dBy2_2 + (df_dBx_2**2 + df_dBy_2**2) * d2f_dBz2_2 + 2 * df_dBx_1 * df_dBy_2 * d2f_dBxdBy_2 + 2 * df_dBx_2 * df_dBz_2 * d2f_dBxdBz_2 + 2 * df_dBy_2 * df_dBz_2 * d2f_dBydBz_2
            denominator2 = 2 * (df_dBx_2**2 + df_dBy_2**2 + df_dBz_2**2)**(1.5)
            numerator3   = (df_dBy_3**2 + df_dBz_3**2) * d2f_dBx2_3 + (df_dBx_3**2 + df_dBz_3**2) * d2f_dBy2_3 + (df_dBx_3**2 + df_dBy_3**2) * d2f_dBz2_3 + 2 * df_dBx_3 * df_dBy_3 * d2f_dBxdBy_3 + 2 * df_dBx_3 * df_dBz_3 * d2f_dBxdBz_3 + 2 * df_dBy_3 * df_dBz_3 * d2f_dBydBz_3
            denominator3 = 2 * (df_dBx_3**2 + df_dBy_3**2 + df_dBz_3**2)**(1.5)
            
            # Store results
            Trans_Eng_1[:,k,l] = Energies[:,0,m+l] - Energies[:,0,k]
            Trans_Eng_2[:,k,l] = Energies[:,0,(2*m)+l] - Energies[:,0,k]
            Trans_Eng_3[:,k,l] = Energies[:,0,(2*m)+l] - Energies[:,0,m+k]
            gradient1[:,k,l] = (np.sqrt(df_dBx_1**2 + df_dBy_1**2 + df_dBz_1**2))
            gradient2[:,k,l] = (np.sqrt(df_dBx_2**2 + df_dBy_2**2 + df_dBz_2**2))
            gradient3[:,k,l] = (np.sqrt(df_dBx_3**2 + df_dBy_3**2 + df_dBz_3**2))
            curvature1[:,k,l] = np.abs(numerator1 / denominator1)
            curvature2[:,k,l] = np.abs(numerator2 / denominator2)
            curvature3[:,k,l] = np.abs(numerator3 / denominator3)

    return Trans_Eng_1,gradient1,curvature1,Trans_Eng_2,gradient2,curvature2,Trans_Eng_3,gradient3,curvature3