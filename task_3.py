import numpy as np


# -----------------------------
# item number 1
# -----------------------------

# function f asked:
def f(x, k):
    return x**((2*k)-1)

# function to calculate integral:
def trapezoidal_rule(f, a, b, h, k):
    n = int((b-a)/h)
    x = np.linspace(a, b, n+1)
    y = f(x, k)
    T = (h/2) * (y[0] + 2*np.sum(y[1:n]) + y[n])
    return T

a = 0
b = 1
s = 5

# printing values:
for k in range(3, 10):
    m = s*(2**(k-1))
    h = (b-a)/m
    for i in range(0,k):
      v = (2**i)
      Th = trapezoidal_rule(f, a, b, v*h, k)
      print(f"k = {k}: T({v:}h) = {Th:}")
    print("-------------")