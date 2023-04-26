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

def calculate_integral_trapezium_method_based_on_h(function: Callable[[float], float], 
                                        h: float, a: float, b: float) -> float:
    m = (b - a) / h
    return calculate_integral_trapezium_method(function, m, a, b)

def calculate_integral_trapezium_method(function: Callable[[float], float], 
                                        m: float, a: float, b: float) -> float:
    h = (b-a)/m
    sum = (1/2)*function(a) + (1/2)*function(b) 
    x_i = a
    m = int(m)
    for i in range(1, m):
        x_i = x_i + h
        sum += function(x_i)
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

def resolve_triangular_matrix(A_triangular: list[list[float]], 
                              y_triangular: list[float], m: int) -> list[float]:
    x = [0] * m
    for i in range(m-1, -1, -1):
        x_i = y_triangular[i]
        for j in range(i+1, m):
            x_i -= A_triangular[i][j] * x[j]
        x_i = x_i / A_triangular[i][i]
        x[i] = x_i
    return x

def gauss_elimination_method(A: list[list[float]], y: list[float], m: int):
    A_triangular, y_triangular = triangularize(A, y, m)
    return resolve_triangular_matrix(A_triangular, y_triangular, m)

def function_function_inner_product(first_function: Callable[[float], float], second_function: Callable[[float], float], 
                           data_x: list) -> float:
    total_sum = 0.0
    for x_k in data_x:
        total_sum += first_function(x_k) * second_function(x_k)
    return total_sum

def function_vector_inner_product(function: Callable[[float], float], 
                                  independent_terms_vector: list, data_x: list) -> float:
    total_sum = 0.0
    for index, x_k in enumerate(data_x):
        total_sum += function(x_k) * independent_terms_vector[index]
    return total_sum

def calculate_max_and_min_of_array(vector: list[float]) -> list[float]:
    max = min = vector[0]
    for vector_item in vector:
        if vector_item > max:
            max = vector_item
        if vector_item < min:
            min = vector_item
    return [min, max]

def calculate_divided_difference_terms(x_vector: list[float], y_vector: list[float]) -> list[float]:
    #creating matrix
    matrix = []
    for i in range(len(x_vector)):
        matrix.append([])
        for j in range(len(y_vector)):
            matrix[i].append(0)
    
    for i in range(len(x_vector)):
        matrix[i][0] = y_vector[i]
    
    for i in range(1, len(x_vector)):
        for j in range(1, i + 1):
            matrix[i][j] = (matrix[i][j - 1] - matrix[i - 1][j - 1]) / (x_vector[i] - x_vector[i - j])

    # Return the main diagonal of the matrix
    return [matrix[i][i] for i in range(len(x_vector))]
        
def calculate_interpolating_polynomial(interpolating_polynomial_coefficients: list[float], x_vector_data: list[float]) -> Callable[[float], float]:
    def interpolating_polynomial(x: float) -> float:
        sum = 0.0
        for index, item in enumerate(interpolating_polynomial_coefficients):
            prod_result = 1
            for prod_index in range(index):
                prod_result *= (x - x_vector_data[prod_index]) 
            sum += item * prod_result
        return sum
    return interpolating_polynomial

def simpson_integral(function_to_integrate: Callable[[float], float], 
                      a: float, b: float, h: float, m: int) -> float:
    sum = function_to_integrate(a) + function_to_integrate(b)
    for i in range(1, m):
        item = a + h*i
        if i % 2 == 0:
            sum += function_to_integrate(item) * 2
        else:
            sum += function_to_integrate(item) * 4
    
    return sum * h / 3


def calculate_romberg_lagrange_interpolating_plynomial() -> Callable[[float], float]:
    def interpolating_polynomial(x: float) -> float:
        sum = 0.0
        for index, item in enumerate(interpolating_polynomial_coefficients):
            prod_result = 1
            for prod_index in range(index):
                prod_result *= (x - x_vector_data[prod_index]) 
            sum += item * prod_result
        return sum
    return interpolating_polynomial
    