# MATLAB-Style Matrix to LaTeX Converter

## Overview

This project is a simple tool for converting matrices written in MATLAB-style formatting into LaTeX-friendly syntax. It doesn't require MATLAB itself and is designed for scenarios where you want to take advantage of the concise MATLAB matrix syntax in LaTeX documents.
> Formating a matrix in MATLAB is faster than formating it in LaTeX.
> – Sun Tzu, *the art of formating*

## Usage

### How to Use

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ImStian/MATLAB_TO_LATEX_MATRIX.git
   ``` 

2. Navigate to the project directory:

   ```bash
   cd MATLAB_TO_LATEX_MATRIX
   ``` 

3. Run the conversion script:

   ```bash
   python main.py
   ```
4. **OR** Execute the provided executable file:

    ```bash
    ./latex_matrix_generator.exe
    ``` 
     

5. Enter the matrix which should be converted, and click confirm.

### Example

Type the matrix as you would in MATLAB with commas (,) separating row elements and semicolons (;) separating rows to get proper LATEX formating.

 **Input:**
   ```matlab
    "[1,2;3,4]"
```

 **Output:**
  ```latex
  $\begin{bmatrix} 
  1 & 2\\
  3 & 4\\
  \end{bmatrix}$
  ```
