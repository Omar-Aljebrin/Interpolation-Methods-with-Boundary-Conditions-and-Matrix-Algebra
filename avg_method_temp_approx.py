"""
===============================================================================
-What you are doing: 

Interpolating or approximating the values between given data xi, xf, Ti, Tf
and comparing that to the exact value computed by the function Ta.

-References:
    
"Midterm Project" PDF provided by Professor Camelli
-------------------------------------------------------------------------------
-Date: 3/5/2024
-Name: Omar Aljebrin
===============================================================================
"""
# =============================================================================
# GLOBAL VAR - GLOBAL MODS
# -----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
# -----------------------------------------------------------------------------
# END GLOBAL VAR - GLOBAL MODS
# =============================================================================

# =============================================================================
# FUNCTIONS
# -----------------------------------------------------------------------------
# Function for the exact value to compare with approximation
def Ta(x, xi, xf, yi, yf):
    T = (yf - yi) / (xf - xi) * (x - xi) + yi  
    return T
# -----------------------------------------------------------------------------
# END FUNCTIONS
# =============================================================================

# =============================================================================
# MAIN SCRIPT
# -----------------------------------------------------------------------------

# Inputs:

xi = 3.4 # Initial point to start from

xf = 12.1 # Final point 

n = 20  # Number of points

Tnew1 = np.zeros(n) # Space to store all the values of T when eps=1.e-4=eps1

Tnew2 = np.zeros(n) # Space to store all the values of T when eps=1.e-6=eps2

Ti = 121 # Initial regulating point from xi, which is given

Tf = 38.2 # Final value resulting from xf which is given 

# Maximum number of iterations of computation
kmax = 100000  

# The desired accuracy to the decimal point 
eps1 = 1.0e-4
eps2 = 1.0e-6

# Variables:

x = np.linspace(xi, xf, num=n)  # Position along the rod evenly spaced n times

Told = np.random.rand(n)  # Array to place Tnew for k+1
Tnew = np.zeros(n)  # A space to place the calculated values from Told at k

# Boundary conditions
Told[0] = Ti  
Told[n - 1] = Tf 
               
Tnew[0] = Ti
Tnew[n - 1] = Tf

# Computing Tnew:
    
# Loop to run through both inputs of eps to compare
for u in range(0, 2):
    
    # Number of times it will do the calculation
    
    for k in range(kmax):  
        
        # The computing process
        for i in range(1, n - 1):
            Tnew[i] = (Told[i - 1] + Told[i + 1]) / 2  # The average 
#----------------------------------------------------------------------------
 
        # Checking for convergence:
        s = 0
        for i in range(n):
            s += (Tnew[i] - Told[i]) ** 2
        
        s = np.sqrt(s)
        
        # Depending on which u it will use eps that corresponds to that u value
        if u == 0:
            if s < eps1:
                break
        if u == 1:
            if s < eps2:
                break

        # If both if statements aren't fulfilled for both u values, it will renew
        # the value of Told with Tnew for use to compute Tnew at k+1
        for i in range(n):
            Told[i] = Tnew[i]
            
# Storing all that information with the correspondent u iteration 
    if u == 0:
        s1 = s
        k1 = k
        for i in range(n):
            Tnew1[i] = Tnew[i]
    if u == 1:
        s2 = s
        k2 = k
        for i in range(n):
            Tnew2[i] = Tnew[i]
        

# The function that will give us the exact value of T 
Ta = Ta(x, xi, xf, Ti, Tf) 

print('k = {}  when eps={:.1e}, |Told-Tnew| = {}'.format(k1, eps1, s1))
print('k = {}  when eps={:.1e}, |Told-Tnew| = {}'.format(k2, eps2, s2))
#-----------------------------------------------------------------------

# Plots:
plt.figure()
plt.plot(x, Ta,
         label='Ta',
         color='k',
         ms=5,
         )
plt.plot(x, Tnew2, 
         label= (r'$T^{{({})}}$' ', ''eps={:.1e}'.format(k2, eps2)),
         marker='.' ,
         color='b',
         ls='',
         ms=14,
         )
plt.plot(x, Tnew1, 
         label= (r'$T^{{({})}}$' ', ' 'eps={:.1e}'.format(k1, eps1)),
         marker='+' ,
         color='red',
         ls='',
         ms=12,
         )
plt.legend(fontsize=13)
plt.grid()
plt.xlabel('x', fontsize=20)
plt.ylabel('T', fontsize=20)
plt.savefig('fig_mid(1).png', dpi=250)
plt.show()


#inputs wrong and not printed is that okay or can i re sumbit 
# # -----------------------------------------------------------------------------
# END MAIN SCRIPT
# ======================================================

