from collections.abc import Callable
import pandas as pd

init_alpha = 0.7
precision = 10**(-10)
num_iterations = 1000

pd.set_option("display.precision", 45)


def newton(function:Callable[[float], float], derivative:Callable[[float], float], approximation: float, max_iterations: int, tolerance: float) -> float:
    i = 0
    stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
    approximations_list = []
    while(i <= max_iterations):
        if(function(approximation) == 0.0):
            return approximations_list
            
        elif(stop_criteria < 0):
            return approximations_list

        print(approximation)
        approximation = approximation - (function(approximation)/derivative(approximation))
        stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
        i+=1
        approximations_list.append(approximation)

def function_expression(x:float) -> float:
    return ((12600*x - 25200)*x + 15120)*x-2520 # nested polynomial

def derivative_expression(x:float) -> float:
    return (37800*x - 50400)*x+15120

approximations_list = newton(function_expression, derivative_expression, init_alpha, num_iterations, precision)
row_label = ["alpha_i"]
dataset = {}

for index, item in enumerate(approximations_list):
    column_label = str(index + 1)
    dataset[column_label] = [item]
    
df = pd.DataFrame(dataset)
df.index = row_label
print(df.T.to_latex())

