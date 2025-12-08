import matplotlib.pyplot as plt
import numpy as np
import scienceplots # Assuming you have scienceplots installed

plt.style.use(['science', 'ieee']) # Apply scientific and IEEE styles
x = np.linspace(0, 10, 100)
y = np.exp(-x/2) * np.cos(2*np.pi*x)

plt.plot(x, y)
plt.xlabel(r'$t$ (s)') # Using LaTeX for labels
plt.ylabel(r'$V$ (V)')
plt.title("Damped Oscillations")
plt.show()