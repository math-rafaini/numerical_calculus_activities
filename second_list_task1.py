import numpy as np
from math import log
import pandas as pd
import matplotlib.pyplot as plt
from numerical_tools import (function_function_inner_product,
                             function_vector_inner_product,
                             gauss_elimination_method,
                             calculate_max_and_min_of_array
                             )

pd.set_option("display.precision", 30)
pd.set_option("display.float_format", lambda x: '%.30f' % x)

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

function_vector = [f_1, f_2, f_3, f_4]


# Mounting matrix of functions and vectors inner products:

coefficients_matrix = []
for i in range(len(function_vector)):
    coefficients_matrix.append([])
    for j in range(len(function_vector)):
        coefficients_matrix[i].append(
            function_function_inner_product(function_vector[i], 
                                            function_vector[j], x_vector))

independent_terms_vector = []
for i in range(len(function_vector)):
    independent_terms_vector.append(function_vector_inner_product(function_vector[i], y_vector, x_vector))

print("Size of the dataset: ", len(x_vector), "\n\n", "Coefficient matrix: ",  
      coefficients_matrix, "\n\n", "Independent terms vector: ", independent_terms_vector)

# Exhibiting the coefficients matrix in latex format:
# This part is commented to avoid polluting the output
# index = []
# data_to_data_frame = []
# for i in range(len(coefficients_matrix)):
#     for j in range(len(coefficients_matrix)):
#         index.append("\langle f_"+ str(i+1) +" , \; f_" + str(j+1) + " \rangle")
#         data_to_data_frame.append([coefficients_matrix[i][j]])
# df = pd.DataFrame(data_to_data_frame)
# df.index = index
# df.columns = ["Valor"]
# print("Data frame: \n\n", df.to_latex())


# Calculating system results to determine the functions coefficients
system_result = gauss_elimination_method(coefficients_matrix, independent_terms_vector, 
                                         len(independent_terms_vector))

print("Final system result: ", system_result)

# Defining final function to plot the graph:
def final_function(x: float) -> float: 
    total_sum = 0.0
    for i in range(len(system_result)):
        total_sum += system_result[i] * function_vector[i](x)
    return total_sum

interval = calculate_max_and_min_of_array(x_vector)
graph_grid = np.arange(interval[0], interval[1], 0.01)
final_function_plot = []
for i in graph_grid:
    final_function_plot.append(final_function(i))

plt.plot(graph_grid, final_function_plot, "-b", label="Função ajustada")
plt.scatter(x_vector, y_vector, color="red", label="Dados fornecidos")
plt.legend(loc="upper right")

plt.title("Concentração de iodo em profundidade de lago")
plt.xlabel("Profundidade do lago (m)")
plt.ylabel("Concentração de iodo (%)")


# Note that if you are using a linux distribution to run this script
# it is important to have a GUI package for the python to plot the graph.
# To do so, use the command: sudo apt-get install python3-tk
plt.show()
