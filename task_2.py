from numerical_tools import newton_method, calculate_integral_trapezium_method

def f(x):
    return 105*x**2*(1-x)**4

def F(tau):
    m = 10E4
    return calculate_integral_trapezium_method(f, m, 0, tau) - 0.5

def derivative_of_F(tau):
    return f(tau)

list_of_approximations_newton_method = newton_method(F, derivative_of_F, 0.5, 1000, 10E-10)
print(len(list_of_approximations_newton_method), list_of_approximations_newton_method[-1])

list_of_approximations_bisection_method = newton_method(F, derivative_of_F, 0.5, 1000, 10E-10)
print(len(list_of_approximations_bisection_method), list_of_approximations_bisection_method[-1])
