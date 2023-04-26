import time
from collections.abc import Callable
from math import log, exp
import pandas as pd
import matplotlib.pyplot as plt
from numerical_tools import (calculate_integral_trapezium_method_based_on_h,
                             calculate_divided_difference_terms,
                             calculate_interpolating_polynomial,
                             simpson_integral,
                             )

pd.set_option("display.precision", 30)
pd.set_option("display.float_format", lambda x: '%.30f' % x)

# Defining functions and constants
def f(x: float) -> float: 
    return exp(x)
    # To test the algorithm, use the following return instead of the above:
    # return x ** 10
    # the result of the Romberg's integral must be 0.0909289894775222

def primitive_f(x: float) -> float:
    return exp(x)

def exact_defined_integral(primitive_function: Callable[[float], float], a: float, b: float) -> float:
    return primitive_function(b) - primitive_function(a)

def vary_parameters_for_integral_comparison(s, k, a, b):
    
    m = s * 2 ** k
    h_ks = (b - a) / m
    
    t_0_romberg_integral = round(time.time() * 1000)
    trapezium_list = []
    # Trapezium rule list for different values of h
    for i in range(k+1):
        current_h = (2**i) * h_ks
        trapezium_list.append(calculate_integral_trapezium_method_based_on_h(f, current_h, a, b))
        
    x_Romberg_method = []
    for i in range(k+1):
        x_Romberg_method.append(((2**i) * h_ks) ** 2)

    # Coefficients for Newton's interpolating polynomial
    newton_coefficients_interpolating_polynomial = calculate_divided_difference_terms(x_Romberg_method, trapezium_list)

    # Finding interpolating polynomial based on the coefficients found before
    interpolating_polynomial = calculate_interpolating_polynomial(newton_coefficients_interpolating_polynomial, x_Romberg_method)

    # Result for the Romberg integral
    romberg_integral = interpolating_polynomial(0)
    dt_romberg_integral = round(time.time() * 1000) - t_0_romberg_integral

    # Calculating Simpson's integral
      
    t_0_simpson_integral = round(time.time() * 1000)    
    simpson_integral_result = simpson_integral(f, a, b, h_ks, m)
    dt_simpson_integral = round(time.time() * 1000) - t_0_simpson_integral    
    

    # Calculating exact solution
    exact_integral = exact_defined_integral(primitive_f, a, b)
    print("Result for the exact integral: ", exact_integral, "\n\n")

    print("Delta t for Simpson: ", dt_simpson_integral)
    print("Delta t for Romberg: ", dt_romberg_integral)
    simpson_error = abs(simpson_integral_result - exact_integral)
    romberg_error = abs(romberg_integral - exact_integral)

    return [simpson_error, romberg_error]

# Item 1:
# We are going to repeat mostly the same process
# as the first and the second task just varying some 
# parameters:
k = 1
a = 0
b = 1

list_of_errors = []
for s in range (3, 11):
    print("\n\n\nVarying parameters ---> s = ", s, "\n")
    list_of_errors.append(vary_parameters_for_integral_comparison(s, k, a, b))

df_romberg = pd.DataFrame([list_of_errors[i][1] for i in range(len(list_of_errors))])
df_simpson = pd.DataFrame([list_of_errors[i][0] for i in range(len(list_of_errors))])
df_simpson.columns =  ["Erro para o método Simpson"]
df_romberg.columns =  ["Erro para o método Roberg"]
print(df_romberg.to_latex())
print(df_simpson.to_latex())


# Item 2:

# Item 3: 

# Just pure mathematics
