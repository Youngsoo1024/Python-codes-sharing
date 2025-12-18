print("hello world")
print("nice to replace python to python3")
import numpy as np
import matplotlib.pyplot as plt

def Diagonalization(EJ, ECC, ng, N1, N2):
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