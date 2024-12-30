# README for Python Scripts

## Overview

This repository contains three distinct Python scripts that approximate values based on different numerical methods, including interpolation, boundary condition handling, and linear system solution. Each script employs various techniques for solving problems related to temperature distribution, matrix operations, and iterative methods for boundary value problems. Below is a description of each script and its respective method.

---

### 1. **linear_system_temperature_interpolation.py**
#### **Title**: Linear System Temperature Interpolation
#### **Method**:
This script approximates the temperature values (`T`) between two boundary temperatures (`T0` and `Tf`) using a linear system approach. The method solves for intermediate temperatures between given boundary values using finite differences and matrix equations. It compares the numerical solution with the exact solution derived from a simple linear function (`Ta`).

#### **Key Components**:
- **Matrix Creation**: A system of linear equations is set up with boundary conditions.
- **Solution**: The system is solved using `scipy.linalg.solve`.
- **Comparison**: The results are compared with the analytical solution for validation.

#### **Functionality**:
- Generates `n` temperature values between `T0` and `Tf`.
- Solves a linear system based on finite differences for the unknown values of `T`.
- Plots the results against the exact temperature distribution (`Ta`).
  
---

### 2. **iterative_averaging_boundary_conditions.py**
#### **Title**: Iterative Averaging with Boundary Conditions
#### **Method**:
This script implements an iterative method to approximate the temperature distribution in a two-dimensional grid. The method is based on averaging the adjacent points within a grid while respecting boundary conditions (`phiT`, `phiB`, `phiL`, `phiR`). It iterates until the difference between consecutive approximations is less than a specified threshold (`eps`).

#### **Key Components**:
- **Boundary Conditions**: The script uses specific boundary conditions for the grid edges (e.g., `phiT`, `phiB`, etc.).
- **Iterative Process**: The approximation is updated iteratively using the average of neighboring points.
- **Convergence**: The script checks for convergence based on a defined tolerance (`eps`).

#### **Functionality**:
- Solves for the temperature values within the grid by averaging neighboring values iteratively.
- Applies two different sets of boundary conditions to demonstrate the effect of different configurations on the solution.
- Visualizes the results using contour plots of the temperature distribution.

---

### 3. **linear_system_temperature_interpolation.py** (First Script in the README)
#### **Title**: Linear System Temperature Interpolation (Revisited)
#### **Method**:
Similar to the second script, this script also interpolates or approximates temperature values between given boundary temperatures (`T0`, `Tf`). However, it focuses on solving the system iteratively, comparing approximations for different tolerances (`eps`).

#### **Key Components**:
- **Exact Value Function (`Ta`)**: This function computes the exact value of temperature as a linear function between the initial and final values.
- **Comparison**: The script compares the numerically calculated temperature distribution (`Tnew1`, `Tnew2`) with the exact analytical solution (`Ta`).

#### **Functionality**:
- Implements iterative computation for temperature distribution.
- Prints and plots results for different precision levels (defined by `eps1` and `eps2`).
- Compares the results of the iterative method with the exact solution (`Ta`).

---

## How to Use

1. **Ensure Dependencies**: Each script requires `numpy`, `scipy`, and `matplotlib`. Install them via pip if not already installed:
   ```bash
   pip install numpy scipy matplotlib
