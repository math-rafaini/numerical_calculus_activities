import pandas as pd
from collections.abc import Callable
from newton import newton
import warnings

# Settings for python and pandas
warnings.filterwarnings('ignore')
pd.set_option("display.precision", 45)

# -----------------------------
# item number 1
# -----------------------------
print("item number 1")
columns = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
rows = ["g(x)", "g'(x)", "g''(x)"]
def g(x):
    return 2520 * (5 * x**3 - 10 * x**2 + 6 * x - 1)
def deriv_g(x):
    return 2520 * (15 * x**2 - 20 * x + 6)
def deriv_2_g(x):
    return 2520 * (30 * x - 20)

data_frame = {}
for i in columns:
    column_label = str(i)
    item_1 = g(i)
    item_2 = deriv_g(i)
    item_3 = deriv_2_g(i)
    # patch to make sure it will fit in the hbox size
    
    data_frame[column_label] = [item_1, item_2, item_3]


df = pd.DataFrame(data_frame)
df.index = rows

new_df = df.T

# The following lines will be commented out to avoid poluting
# the output of the rest of the first task
# It represents the 3 first tables displayed in the first item of 
# the first task.
# print(new_df["g(x)"].to_latex())
# print(new_df["g'(x)"].to_latex())
# print(new_df["g''(x)"].to_latex())

# -----------------------------
# item number 3
# -----------------------------
print("\n\n\nitem number 3")

# Function definitions
def function_expression_for_item_3(x:float) -> float:
    return ((12600*x - 25200)*x + 15120)*x-2520 # nested polynomial

def derivative_expression_for_item_3(x:float) -> float:
    return (37800*x - 50400)*x+15120

# You can set the initial value for the approximation
# for the equation we are studying it could be 0.3 or 0.7
init_alpha = 0.7
precision = 10**(-10)
num_iterations = 1000

approximations_list = newton(function_expression_for_item_3, derivative_expression_for_item_3, init_alpha, num_iterations, precision)
row_label = ["alpha_i"]
dataset = {}

for index, item in enumerate(approximations_list):
    column_label = str(index + 1)
    dataset[column_label] = [item]
    
df = pd.DataFrame(dataset)
df.index = row_label
print(df.T.to_latex())


# -----------------------------
# item number 4
# -----------------------------
print("\n\n\nitem number 4")

def f_second_derivative(x):
    return 840*(1 - x)*(3*x**2 - 6*x + 1)

x1 = 0.276393202250021119414924442025949247181415558
x2 = 0.723606797749774321992788372881477698683738708
print("Second derivative in x=0: ", abs(f_second_derivative(0)))
print("Second derivative in x=x1: ", abs(f_second_derivative(x1)))
print("Second derivative in x=x2: ", abs(f_second_derivative(x2)))
print("Second derivative in x=1: ", abs(f_second_derivative(1)))

h = (12/840)**(1/2) * 10E-4
print("h = ", h)
print("1/h = ", 1/h)

def f(x):
    return 105*x*x*(1-x)**4
    
def calculate_integral_trapezium_method(f, m, a, b):
    h = (b-a)/m
    
    sum = (1/2)*f(a) + (1/2)*f(b) 
    x_i = a
    for i in range(1, m):
        x_i = x_i + h
        sum += f(x_i)
    return sum*h


# Process to discover the value of the minimum m to satisfy the integral inequation:
m_minimum = 1
integral_i = integral = calculate_integral_trapezium_method(f, m_minimum, 0, 1)
while abs(integral_i - 1) >= 10E-8:
    m_minimum = m_minimum + 1
    integral_i = calculate_integral_trapezium_method(f, m_minimum, 0, 1)

print(integral_i, m_minimum)
