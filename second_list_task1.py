import numpy
from math import log
import pandas as pd
from numerical_tools import (function_function_inner_product,
                             function_vector_inner_product,
                             )

df = pd.read_csv("data.csv")

x_vector = [10.4, 11.7, 12.8, 13, 15.7, 16.3, 18, 18.7, 20.7, 22.1, 
            22.4, 24.4, 25.8, 32.5, 33.6, 36.8, 37.8, 36.9, 42.2, 47,
            47.1, 48.4, 49.4, 49.5, 59.2, 60.1, 61.7, 62.4, 69.3, 73.6,
            74.4, 78.5, 82.9, 87.7, 88.1, 90.4, 90.6, 97.7, 103.7]
y_vector = [19.5, 24.9, 36.1, 40.9, 26.5, 32.2, 55.3, 36.8, 54.4, 41.5,
            27.8, 29.0, 53.6, 69.8, 43.1, 52.7, 50.7, 47.4, 50.4, 45.1,
            53.5, 48.0, 55.4, 54.7, 45.2, 52.7, 46.9, 49.7, 44.9, 51.6,
            49.5, 48.5, 52.1, 47.3, 45.6, 48.9, 53.8, 48.0, 47.8]

# We are enumerating the functions according to the exercise:

def f_1(x: float) -> float:
    return 1

def f_2(x: float) -> float: 
    return x

def f_3(x: float) -> float:
    return x ** 2

def f_4(x: float) -> float:
    return log(x)

vector_of_functions = [f_1, f_2, f_3, f_4]


# Mounting matrix of functions and vectors inner products:

matrix_of_coefficients = []
for i in range(len(vector_of_functions)):
    matrix_of_coefficients.append([])
    for j in range(len(vector_of_functions)):
        matrix_of_coefficients[i].append(
            function_function_inner_product(vector_of_functions[i], 
                                            vector_of_functions[j], x_vector))

print(len(x_vector), matrix_of_coefficients)
