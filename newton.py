from collections.abc import Callable
import pandas as pd

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

        print("Approximation for Newton's method:",  approximation)
        approximation = approximation - (function(approximation)/derivative(approximation))
        stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
        i+=1
        approximations_list.append(approximation)
