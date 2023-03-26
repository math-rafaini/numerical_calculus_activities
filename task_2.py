from time import time

from numerical_tools import (calculate_integral_trapezium_method,
                             newton_method_performance_focused,
                             bisection_method_performance_focused)

def f(x):
    return 105*x**2*(1-x)**4

def F(tau):
    m = 10E4
    return calculate_integral_trapezium_method(f, m, 0, tau) - 0.5

def derivative_of_F(tau):
    return f(tau)

# The folowing lines are commented to avoid poluting the task's output
# print("---------------------")
# print("Newton's method")
# list_of_approximations_newton_method = newton_method(F, derivative_of_F, 0.5, 1000, 10E-10)
# print(len(list_of_approximations_newton_method), list_of_approximations_newton_method[-1])

# print("---------------------")
# print("Bisection method")
# list_of_approximations_bisection_method = bisection_method(F, 1000, 10E-10, 0, 1)
# print(len(list_of_approximations_bisection_method), list_of_approximations_bisection_method[-1])

# -----------------------------
# item number 1
# -----------------------------

print("---------------------")
print("Newton's method")
before_timestamp = time()
newton = newton_method_performance_focused(F, derivative_of_F, 0.5, 1000, 10E-10)
print("Time spent in newton's method: ", time() - before_timestamp)
print("Result from newton's method: ", newton)

print("---------------------")
print("Bisection method")
before_timestamp = time()
bisection = bisection_method_performance_focused(F, 1000, 10E-10, 0, 1)
print("Time spent in bisection method: ",  time() - before_timestamp)
print("Result from bisection method: ", bisection)
