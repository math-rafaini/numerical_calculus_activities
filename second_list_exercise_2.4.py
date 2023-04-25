import numpy as np
from math import log, sqrt
import pandas as pd
import matplotlib.pyplot as plt
from numerical_tools import (calculate_integral_trapezium_method_based_on_h,
                             calculate_divided_difference_terms,
                             calculate_interpolating_polynomial
                             )

# Defining functions and constants

def f_1(x:float) -> float:
    return x**20

def f_2(x:float) -> float:
    if (x == 0):
        return 0
    else:
        return sqrt(x)*log(x)

def calculate_h_ks(k:list[int], s: float, begin: float, end: float) -> list[float]:
    h_ks = []
    for i in range(len(k)):
        m = s * 2 ** k[i]
        h_ks.append((end - begin) / m)
    return h_ks

s = 3
k = list(range(1,7)) 
a = 0
b = 1
h_ks_list = calculate_h_ks(k, s, a, b)

# Item 1:
# Calculating trapezium integral method for f_1

trapezium_matrix = []
trapezium_approximation_val = []

for j in range(len(k)):
    trapezium_val = []
    for i in range(k[j]+1):
        current_h = (2**i) * h_ks_list[j]
        trapezium_val.append(calculate_integral_trapezium_method_based_on_h(f_1, current_h, a, b)) 
    trapezium_matrix.append(trapezium_val)
    trapezium_approximation_val.append(trapezium_val[0])

#for j in range(len(k)):
#    print("Trapezium rule matrix [", j,"] for k =", k[j],":")
#    for i in range(k[j]+1):
#        print(trapezium_matrix[j][i], end=" ")
#    print("\n")

# Calculating Romberg integral method for f_1

x_Romberg_method = []

for j in range(len(k)):
    romberg_val = [] 
    for i in range(k[j]+1):
        romberg_val.append(((2**i) * h_ks_list[j]) ** 2)
    x_Romberg_method.append(romberg_val)

romberg_integral_list = []

for j in range(len(k)):
    newton_coefficients_interpolating_polynomial = calculate_divided_difference_terms(x_Romberg_method[j], trapezium_matrix[j])
    #print("Coefficients for Newton's interpolating polynomial: ", newton_coefficients_interpolating_polynomial)

    # Finding interpolating polynomial based on the coefficients found before
    interpolating_polynomial = calculate_interpolating_polynomial(newton_coefficients_interpolating_polynomial, x_Romberg_method[j])
    romberg_integral_list.append(interpolating_polynomial(0))    

real_integral_val = 0.04761904761904761904761904761905

error_list_1 = []
error_list_2 = []
ratio_list = []
aux = []

for j in range(len(k)):
    error_1 = abs(real_integral_val - trapezium_approximation_val[j])
    error_list_1.append(error_1)

for j in range(len(k)):
    error_2 = abs(real_integral_val - romberg_integral_list[j])
    error_list_2.append(error_2)

for j in range(len(k)):
    ratio = (abs(error_list_2[j]) / (abs(error_list_1[j])))
    ratio_list.append(ratio)

for j in range(len(k)):
    if(j == 0):
        aux.append("x^20")
    else:
        aux.append("----")

# Declaring dataframe
df = pd.DataFrame({'k_value': k,'Ratio between Trapezium method x Romberg method': ratio_list, 'Function': aux})

# Printing table of ratio values
print(df, "\n\n")


# Item 1:
# Calculating trapezium integral method for f_2

trapezium_matrix = []
trapezium_approximation_val = []
for j in range(len(k)):

    trapezium_val = []
    for i in range(k[j]+1):
        current_h = (2**i) * h_ks_list[j]
        trapezium_val.append(calculate_integral_trapezium_method_based_on_h(f_2, current_h, a, b)) 
    trapezium_matrix.append(trapezium_val)
    trapezium_approximation_val.append(trapezium_val[0])

# Calculating Romberg integral method for f_2

x_Romberg_method = []

for j in range(len(k)):
    romberg_val = [] 
    for i in range(k[j]+1):
        romberg_val.append(((2**i) * h_ks_list[j]) ** 2)
    x_Romberg_method.append(romberg_val)

romberg_integral_list = []

for j in range(len(k)):
    newton_coefficients_interpolating_polynomial = calculate_divided_difference_terms(x_Romberg_method[j], trapezium_matrix[j])
    interpolating_polynomial = calculate_interpolating_polynomial(newton_coefficients_interpolating_polynomial, x_Romberg_method[j])
    romberg_integral_list.append(interpolating_polynomial(0))    

real_integral_val = - 0.44444444444444444444444444444444 

error_list_1 = []
error_list_2 = []
ratio_list = []
aux = []

for j in range(len(k)):
    error_1 = abs(real_integral_val - trapezium_approximation_val[j])
    error_list_1.append(error_1)

for j in range(len(k)):
    error_2 = abs(real_integral_val - romberg_integral_list[j])
    error_list_2.append(error_2)

for j in range(len(k)):
    ratio = (abs(error_list_2[j]) / (abs(error_list_1[j])))
    ratio_list.append(ratio)

for j in range(len(k)):
    if(j == 0):
        aux.append("sqrt(x)*log(x) or 0")
    else:
        aux.append("-------------------")

# Declaring dataframe
df = pd.DataFrame({'k_value': k,'Ratio between Trapezium method x Romberg method': ratio_list, 'Function': aux})

# Printing table of ratio values
print(df)
