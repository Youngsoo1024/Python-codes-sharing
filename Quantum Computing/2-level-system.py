import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
def Diagonalization(EJ, ECC, ng, N1, N2):    
    """
    Definitions of arguments
    EJ=1
    #Charging energy (normalized)
    ECC = 0.000000001
    # Offset Charge
    ng = 0.3
    #Lowest Charge Basis
    N1 = 0
    #Highest Charge Basis
    N2 = 1
    """
    # The matrix will be indexed from 0 to N
    N = N2-N1+1
    # Initialize the Hamiltonian
    H_dash = np.zeros((N)*(N)).reshape((N,N))
    # Calculate Eav for shifting
    Eav = ECC*ng*ng-ECC*ng+ECC/2

    for i in range(N):
        for j in range(N):
          if(i==j):
            H_dash[i,j]=ECC*((i+N1)-ng)*((i+N1)-ng)-Eav
          if((i==j+1)):
            H_dash[i,j]=-EJ/2 
          if((i==j-1)):
            H_dash[i,j]=-EJ/2  
    # The returned i-th eigenvector is in eigenvectors[:,i]
    eigenvalues, eigenvectors = np.linalg.eig(H_dash)
    # Sort from low eigenvalues to high values
    idx = eigenvalues.argsort()
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:,idx]
    # return with tranpose
    return eigenvalues, np.transpose(eigenvectors)
#def Diagonalization(EJ, ECC, ng, N1, N2):
# Definitions of arguments
EJ = 1
#Charging energy (normalized)
ECC = 0.02
#Lowest Charge Basis
N1 = -100
#Highest Charge Basis
N2 = 100
# ng range (extend to -value value)
ng_range = 1
# discretization points in the postive size (so double overall)
discretization = 100

# Initialize eigenenergy arrays
E0=[]
E1=[]
E2=[]
for i in range(0, 2*discretization+1, 1):
            eigenvalues, eigenvectors = Diagonalization\
            (EJ, ECC, -ng_range+2*ng_range*i/2/discretization, N1, N2)
E0.append(eigenvalues[0])
E1.append(eigenvalues[1])
    #E2.append(eigenvalues[2])
    #this is n_g location
if i==150: 
        print(eigenvectors[0][99],eigenvectors[0][100],eigenvectors[0][101])
        #print(eigenvectors[2][99],eigenvectors[2][100],eigenvectors[2][101])
        #print(eigenvectors[0])
        #print(eigenvectors[1])
    
#print desired qubit freqency
print(E1[150]-E0[150])


plt.figure(figsize=[3,5])
#Plot each level
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), E0)
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), E1)
plt.legend(["E0","E1"],fontsize=13)


"""
#Plot spacing
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), \
    np.array(E1)-np.array(E0))
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), \
    np.array(E2)-np.array(E1))
plt.legend(["E10","E21"],fontsize=13)
"""

"""
#Plot each level offset to E0
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), \
         np.array(E0)-np.array(E0))
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), \
         np.array(E1)-np.array(E0))
plt.plot(np.linspace(-ng_range,ng_range,2*discretization+1), \
         np.array(E2)-np.array(E0))
plt.legend(["E00","E10","E20"],fontsize=13)
"""

plt.grid()
plt.xlabel('$n_g$', fontsize=20)
plt.ylabel('Energy (a.u.)', fontsize=20)
plt.xlim(0,1)
plt.ylim(-1,2)
plt.tick_params(labelsize=16)