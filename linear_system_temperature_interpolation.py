#===============================================================================
'''
-What you are doing 

Interpolating or approximating the values of T between given boundary values 
T0 and Tf and comparing the values to the exact values provided by the 
analytical solution Ta.

#-References
#"Midterm Project" PDF provided by Professor Camelli.
#-------------------------------------------------------------------------------
#-Date: 3/5/2024
-Name: Omar Aljebrin'
#===============================================================================
'''
# =============================================================================
# GLOBAL VARIABLES - GLOBAL MODULES
# -----------------------------------------------------------------------------
import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# END GLOBAL VARIABLES - GLOBAL MODULES
# =============================================================================

# =============================================================================
# FUNCTIONS
# -----------------------------------------------------------------------------
def ya(x, xi, xf, yi, yf):  # Random letters, no reason behind them
    
    T = (yf - yi) / (xf - xi) * (x - xi) + yi
    
    return T
# -----------------------------------------------------------------------------
# END FUNCTIONS
# =============================================================================

# =============================================================================
# MAIN SCRIPT
# -----------------------------------------------------------------------------
  
# Inputs
n = 23

T0 = -5.0

Tf = 25.5


xi = 5.0

xf = 35.0

# Variables
L = np.zeros((n, n))

x = np.linspace(xi, xf, num=n) # Space to store x values 

x[0] = xi  # Given x initial assigned to first position of array

x[n - 1] = xf  # Given last value in array

L[0, 0] = 1

L[n - 1, n - 1] = 1

#-----------------------------------------------
# Filling in matrix L

# Since it is a square matrix, j and i are the same so no nested loop

for i in range(1, n - 1): 
    
    L[i, i + 1] = -1
    
    L[i, i] = 2 
    
    L[i, i - 1] = -1
    

# Independent vector 
b = np.zeros(n)  # Space for given array or one solved from average equation

# Assigning given initial and final conditions to do the computing

b[0] = T0

b[n - 1] = Tf

TL = la.solve(L, b) 
# TL is an array of Ti to Tn-1 approximation (except for Ti and Tn-1 because they are given)  

Ta = ya(x, xi, xf, T0, Tf)  # Exact values (analytical solution)
#---------------------------------------------------------------------------
# Plot

plt.figure()  # A space to place plots in

plt.plot(x, Ta,
         label='Ta',   # The label on the legend
         color='k',  # Color black
         lw=2    # Line width
        )
plt.plot(x, TL, 
         label= 'TL',   # Label in the legend
         marker='.' ,  # Type of marker
         color='b',    # Color blue
         ls='',        # Line type ('') means no line
         ms=12,
         )

plt.grid()  
plt.xlabel('x', fontsize=20)  
plt.ylabel('T', fontsize=20)
plt.legend(fontsize=14)
plt.savefig('fig_mid(2).png', dpi=250)   
plt.show()

print(Ta)
print(TL)
# -----------------------------------------------------------------------------
# END MAIN SCRIPT
# =============================================================================


