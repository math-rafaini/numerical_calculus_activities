import numpy as np
from math import log, exp
import pandas as pd
import matplotlib.pyplot as plt
from numerical_tools import (calculate_integral_trapezium_method_based_on_h,
                             calculate_divided_difference_terms,
                             calculate_interpolating_polynomial
                             )

pd.set_option("display.precision", 30)
pd.set_option("display.float_format", lambda x: '%.30f' % x)

# Defining functions and constants
def f(x: float) -> float: 
    return exp(x)
    # To test the algorithm, use the following return instead of the above:
    # return x ** 10
    # the result of the Romberg's integral must be 0.0909289894775222

s = 3
k = 2
m = s * 2 ** k
a = 0
b = 1
h_ks = (b - a) / m

# Item 1:
trapezium_list = []
for i in range(k+1):
    current_h = (2**i) * h_ks
    trapezium_list.append(calculate_integral_trapezium_method_based_on_h(f, current_h, a, b))
    
print("Trapezium rule list for different values of h: ", trapezium_list, "\n\n")

# Item 2: 
x_Romberg_method = []
for i in range(k+1):
    x_Romberg_method.append(((2**i) * h_ks) ** 2)

newton_coefficients_interpolating_polynomial = calculate_divided_difference_terms(x_Romberg_method, trapezium_list)

print("Coefficients for Newton's interpolating polynomial: ", newton_coefficients_interpolating_polynomial, "\n\n")

# Finding interpolating polynomial based on the coefficients found before
interpolating_polynomial = calculate_interpolating_polynomial(newton_coefficients_interpolating_polynomial, x_Romberg_method)

print("Result for the Romberg integral: ", interpolating_polynomial(0))
