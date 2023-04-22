import pandas as pd
from collections.abc import Callable
from numerical_tools import newton_method, calculate_integral_trapezium_method
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

# The following lines will be commented out to avoid polluting
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

approximations_list = newton_method(function_expression_for_item_3, derivative_expression_for_item_3, init_alpha, num_iterations, precision)
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
    return 210*((1-x)**2)*(15*x**2 - 10*x + 1)

x1 = 0.276393202250021119414924442025949247181415558
x2 = 0.723606797749774321992788372881477698683738708
print("Second derivative in x=0: ", abs(f_second_derivative(0)))
print("Second derivative in x=x1: ", abs(f_second_derivative(x1)))
print("Second derivative in x=x2: ", abs(f_second_derivative(x2)))
print("Second derivative in x=1: ", abs(f_second_derivative(1)))

h = (12/210)**(1/2) * 10E-4
print("h = ", h)
print("1/h = ", 1/h)

# This is simply the function initially given by the exercise
# without any further derivatives.
def f(x):
    return 105*x*x*(1-x)**4

m_star = 4184

integral_result = calculate_integral_trapezium_method(f, m_star, 0, 1)

print("integral_result = ", integral_result) 

error_calculation = abs(1 - integral_result)
print("error_calculation = ", error_calculation)
