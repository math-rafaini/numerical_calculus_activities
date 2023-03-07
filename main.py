import pandas as pd

columns = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
rows = ["g(x)", "g'(x)", "g''(x)"]
def g(x):
    return 2520 * (5 * x**3 - 10 * x**2 + 6 * x - 1)
def deriv_g(x):
    return 2520 * (15 * x**2 - 20 * x + 6)
def deriv_2_g(x):
    return 2520 * (30 * x - 20)

data_frame_1 = {}
data_frame_2 = {}
for i in columns:
    column_label = str(i)
    item_1 = g(i)
    item_2 = deriv_g(i)
    item_3 = deriv_2_g(i)
    # patch to make sure it will fit in the hbox size
    if i <= 0.4:
        data_frame_1[column_label] = [item_1, item_2, item_3]
    else:
        data_frame_2[column_label] = [item_1, item_2, item_3]

df_1 = pd.DataFrame(data_frame_1)
df_1.index = rows

df_2 = pd.DataFrame(data_frame_2)
df_2.index = rows

print(df_1.to_latex())
print(df_2.to_latex())

