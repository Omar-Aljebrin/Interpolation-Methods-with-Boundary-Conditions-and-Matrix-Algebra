"""
===============================================================================
-What you are doing: 

Interpolating or approximating the values between given data 
xi, xf, yi, yf, PhiT, PhiB, PhiL, PhiR. By finding the average of the 
adjacent points of any Phi[i,j] within the boundaries of given data. 


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


# -----------------------------------------------------------------------------
# END FUNCTIONS
# =============================================================================

# =============================================================================
# MAIN SCRIPT
# -----------------------------------------------------------------------------



# Inputs:

for u in range(2):
    if u == 0:     # For inputs of a 
        
        n = 20 # Number of points 

        kmax = 100000  # If it doesn't reach desired accuracy, end at kmax iteration

        eps = 1.0e-4   # Desired accuracy to the decimal places

        # Initial and final given positions
        xi = 0
        xf = 1 
        yi = 0
        yf = 1

        # Boundary conditions
        phiT = 100.0
        phiL = 0.0
        phiR = 0.0
        phiB = 0.0
        phinewa = np.zeros((n,n))  # Matrix with inputs a
        xa = np.zeros(n)
        ya = np.zeros(n)
       
        
    if u == 1:   # For inputs of b 
    
        n = 30  # Number of points 

        kmax = 100000

        eps = 1.0e-6  # Desired accuracy of decimal places
        
        # Initial and final given positions
        xi = 0
        xf = 1
        yi = 0
        yf = 1

        # Boundary conditions
        phiT = -100.0
        phiL = -50.0
        phiR = 10.0
        phiB = 10.0
        phinewb = np.zeros((n,n))  # Matrix with inputs b
        xb = np.zeros(n)
        yb = np.zeros(n)
    


   
    # Variables
    
    # x and y positions evenly spaced n times from xi to xf and yi to yf
    x = np.linspace(xi, xf, num=n)
    y = np.linspace(yi, yf, num=n)
    
    phiold = np.zeros((n,n))
    phinew = np.zeros((n,n))
    
    x[0] = xi
    x[n - 1] = xf
              
    y[0] = yi
    y[n - 1] = yf
    
    # Boundary condition for k
    phiold[:,0] = phiL
    phiold[:,n - 1] = phiR
    phiold[0,:] = phiB
    phiold[n - 1,:] = phiT
    
    # Boundary condition for k+1
    phinew[:,0] = phiL
    phinew[:,n - 1] = phiR
    phinew[0,:] = phiB
    phinew[n - 1,:] = phiT
    
    #------------------------------------------------------------
    
    # Computing phinew by finding the average with each iteration if phinew-phiold !< eps
    for k in range(kmax): 
      
      for j in range(1,n - 1):
            
            for i in range(1,n - 1):
    # Computing the average of the adjacent positions for the desired position
                
                phinew[j,i] = (phiold[j + 1,i] + phiold[j - 1,i] + phiold[j,i + 1] + phiold[j,i - 1]) / 4
    
    # Check for convergence
        
      s = 0
    
      for j in range(n):
          for i in range(n):
                 s += (phinew[j,i] - phiold[j,i]) ** 2
    
      s = np.sqrt(s)
    
      if s < eps:
            break
        
      for j in range(n):
            for i in range(n):
    # Update phiold to newer values from phinew to be used again in the iterations
    
                phiold[j,i] = phinew[j,i] 
  
# Storing process:

# For each iteration of u the inputs will vary so this saves the values of 
# each depending on the corresponding u
    if u == 0:
       
        ka = k
        for j in range(n):
              for i in range(n):
      
                  phinewa[j,i] = phinew[j,i] 
                  xa[i] = x[i]
                  ya[i] = y[i]
        print('k(a)={}'  .format(ka))  # Prints number of iteration for inputs a
    if u == 1:
        kb = k
        for j in range(n):
              for i in range(n):
      
                  phinewb[j,i] = phinew[j,i] 
                  xb[i] = x[i]
                  yb[i] = y[i]
        
        print('k(b)={}'  .format(kb))  # Prints number of iteration of inputs b


 #--------------------------------------------------------------------------
  
# Plot: 

xxa,yya = np.meshgrid(xa, ya)   
xxb,yyb = np.meshgrid(xb, yb)  
    
    
# Plot contour surface:
    
fig, ax = plt.subplots(2,1)    
cs = ax[0].contourf(xxa, yya, phinewa,  
                      levels=20,)
cbar = fig.colorbar(cs,
                      orientation='vertical').set_label(label='V{a}', size=16)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
cs = ax[1].contourf(xxb, yyb, phinewb,  
                      levels=20,)
                      
cbar = fig.colorbar(cs,
                      orientation='vertical').set_label(label='V{b}', size=16)
plt.xlabel('x', fontsize=16)
plt.ylabel('y', fontsize=16)
plt.savefig('fig_mid(3).png', dpi=250)
plt.show()


