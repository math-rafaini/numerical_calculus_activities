from collections.abc import Callable

# INPUT
init_alpha = 0.15
precision = 10**(-10)
num_iterations = 1000

#FUNCTION
def newton(function:Callable[[float], float], derivative:Callable[[float], float], approximation: float, max_iterations: int, tolerance: float) -> float:
    i = 0
    stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
    while(i <= max_iterations):
        if(function(approximation) == 0.0):
            return approximation
            
        elif(stop_criteria < 0):
            return approximation

        print(approximation)
        approximation = approximation - (function(approximation)/derivative(approximation))
        stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
        i+=1

def function_expression(x:float) -> float:
    return ((12600*x - 25200)*x + 15120)*x-2520 # nested polynomial

def derivative_expression(x:float) -> float:
    return (37800*x - 50400)*x+15120

print(newton(function_expression, derivative_expression, init_alpha, num_iterations, precision))