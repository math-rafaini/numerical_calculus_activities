import numpy as np
from math import log, exp
import pandas as pd
import matplotlib.pyplot as plt
from numerical_tools import (calculate_integral_trapezium_method_based_on_h,
                             calculate_divided_difference_terms,
                             calculate_interpolating_polynomial
                             )

# Defining functions and constants
def f(x:float)->float:
    return exp(x)

s = list(range(3,11))
k = 2
a = 0
b = 1
h_ks_list = []

# Item 1:
# Sub-item 1:
trapezium_approximation_list = []
trapezium_matrix = []
for j in range(len(s)):
    m = s[j] * 2 ** k
    h_ks = (b - a) / m
    s_list = []
    h_ks_list.append(h_ks)

    for i in range(k+1):
        current_h = (2**i) * h_ks
        s_list.append(calculate_integral_trapezium_method_based_on_h(f, current_h, a, b)) 
    trapezium_matrix.append(s_list)
    trapezium_approximation_list.append(s_list[0])

for j in range(len(s)):
    print("Trapezium rule matrix [", j,"] for s =", s[j],":")
    for i in range(k+1):
        print(trapezium_matrix[j][i], end=" ")
    print("\n")

# Sub-item 2:
x_Romberg_method = []

for j in range(len(s)):
    m = s[j] * 2 ** k
    h_ks = (b - a) / m
    s_list = [] 

    for i in range(k+1):
        s_list.append(((2**i) * h_ks) ** 2)
    x_Romberg_method.append(s_list)

romberg_integral_list = []

for j in range(len(s)):
    newton_coefficients_interpolating_polynomial = calculate_divided_difference_terms(x_Romberg_method[j], trapezium_matrix[j])
    print("Coefficients for Newton's interpolating polynomial: ", newton_coefficients_interpolating_polynomial)

    # Finding interpolating polynomial based on the coefficients found before
    interpolating_polynomial = calculate_interpolating_polynomial(newton_coefficients_interpolating_polynomial, x_Romberg_method[j])
    romberg_integral_list.append(interpolating_polynomial(0))    
    print("Result for the Romberg integral: ", interpolating_polynomial(0), "\n\n")

real_integral_val = 1.718281828459045

error_list_1 = []
error_list_2 = []

for j in range(len(s)):
    error_1 = abs(real_integral_val - trapezium_approximation_list[j])
    error_list_1.append(error_1)

for j in range(len(s)):
    error_2 = abs(real_integral_val - romberg_integral_list[j])
    error_list_2.append(error_2)

# Declaring dataframe
df = pd.DataFrame({'s_value': s,'Trapezium Rule Error': error_list_1, 'Romberg Error': error_list_2})

# Printing table of error values
print(df)


# Item 2:

def calculate_x_val(h_list: list[float]) -> list[float]:
    log_x_val = []
    
    for j in range(len(s)):
        log_x_val.append(log(h_list[j]))
    return log_x_val

def calculate_y_val(integral_error_list: list[float]) -> list[float]:
    log_y_val = []

    for j in range(len(s)):
        log_y_val.append(log(integral_error_list[j]))
    return log_y_val

# Mounting matrix from Trapezium method:





# Item 3:
# Ploting dataframe following the respective method:

x_vector = calculate_x_val(h_ks_list)

# - Trapezium method

y_vector = calculate_y_val(error_list_1)
plt.scatter(x_vector, y_vector, color="red", label="Dados fornecidos")
plt.legend(loc="upper right")

plt.title("Erro de integração em função do comprimento da partição h")
plt.xlabel("Comprimento da partição h")
plt.ylabel("Erro de integração - Método dos trapézios")

# - Romberg method
y_vector = calculate_y_val(error_list_2)
plt.scatter(x_vector, y_vector, color="red", label="Dados fornecidos")
plt.legend(loc="upper right")

plt.title("Erro de integração em função do comprimento da partição h")
plt.xlabel("Comprimento da partição h")
plt.ylabel("Erro de integração - Método de Romberg")

# Note that if you are using a linux distribution to run this script
# it is important to have a GUI package for the python to plot the graph.
# To do so, use the command: sudo apt-get install python3-tk
plt.show()

