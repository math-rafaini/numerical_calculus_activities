from collections.abc import Callable
import pandas as pd

pd.set_option("display.precision", 45)


def newton_method(function:Callable[[float], float], derivative:Callable[[float], float], approximation: float, max_iterations: int, tolerance: float) -> list:
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

def bisection_method(function:Callable[[float], float], max_iterations: int, tolerance: float, 
                     lower_bound: float, upper_bound: float):
    minimal_i = lower_bound
    maximal_i = upper_bound
    alpha_next = (minimal_i + maximal_i) / 2
    approximations_list = [alpha_next]
    i = 0
    while function(alpha_next - tolerance) * function(alpha_next + tolerance) >= 0 and i < max_iterations:
        if function(alpha_next)*function(minimal_i) < 0:
            maximal_i = alpha_next
        elif function(alpha_next)*function(minimal_i) == 0:
            if function(alpha_next) == 0:
                return approximations_list
            else: 
                approximations_list.append(minimal_i)
                return approximations_list
        elif function(alpha_next)*function(minimal_i) > 0:
            minimal_i = alpha_next
        alpha_next = (minimal_i + maximal_i) / 2
        approximations_list.append(alpha_next)
        i += 1
    
    return approximations_list

def newton_method_performance_focused(function:Callable[[float], float], derivative:Callable[[float], float], approximation: float, max_iterations: int, tolerance: float) -> float:
    i = 0
    stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
    while(i <= max_iterations):
        if(function(approximation) == 0.0):
            return approximation
            
        elif(stop_criteria < 0):
            return approximation

        approximation = approximation - (function(approximation)/derivative(approximation))
        stop_criteria = function(approximation + tolerance) * function(approximation - tolerance)
        i+=1

def bisection_method_performance_focused(function:Callable[[float], float], max_iterations: int, tolerance: float, 
                     lower_bound: float, upper_bound: float):
    minimal_i = lower_bound
    maximal_i = upper_bound
    alpha_next = (minimal_i + maximal_i) / 2
    i = 0
    while function(alpha_next - tolerance) * function(alpha_next + tolerance) >= 0 and i < max_iterations:
        if function(alpha_next)*function(minimal_i) < 0:
            maximal_i = alpha_next
        elif function(alpha_next)*function(minimal_i) == 0:
            if function(alpha_next) == 0:
                return alpha_next
            else: 
                return minimal_i
        elif function(alpha_next)*function(minimal_i) > 0:
            minimal_i = alpha_next
        alpha_next = (minimal_i + maximal_i) / 2
        i += 1
    
    return alpha_next

def calculate_integral_trapezium_method(f, m, a, b):
    h = (b-a)/m
    
    sum = (1/2)*f(a) + (1/2)*f(b) 
    x_i = a
    m = int(m)
    for i in range(1, m):
        x_i = x_i + h
        sum += f(x_i)
    return sum*h

def print_matrix(Matrix, m):
    
    for j in range(m):
        
        for i in range(m):
            print(f'{Matrix[j][i]}   ', end= "")
        print("\n")

def triangularize(A, y, m):

    for j in range(m):
        if A[j][j] == 0:
            new_j = None
            for k in range(m):
                if A[k][j] != 0:
                    new_j = k
                if k == m:
                    print("Error: Matrix is singular.")
                    return None
            if not new_j:
                A[j], A[new_j] = A[new_j], A[j]
                y[j], y[new_j] = y[new_j], y[j]
                    
            # print_matrix(A, m)

    for j in range(m):
        # Eliminates all elements underneath the main diagonal's
        for i in range(j+1, m):
            mu = -A[i][j] / A[j][j]
            for k in range(j, m):
                
                # This line is necessary only to debug the code:
                # print(f'{A[i][k]} += {mu} * {A[j][k]}       value of j = {j}  valor de k = {k}\n')
                
                A[i][k] += mu * A[j][k]
            
            y[i] += mu * y[j]

    return A, y

def resolve_triangular_matrix(A_triangular, y_triangular, m):
    for i in range(m-1, -1, -1):
        print(i)
        
for i in range(4, -1, -1):
        print(i)
