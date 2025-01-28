import random
import math
import numpy as np

n = int(input("Enter the size of the lists: "))

x = [random.uniform(1, 50) for _ in range(n)]
y = [random.uniform(1, 50) for _ in range(n)]

x_sum = sum(x)
y_sum = sum(y)

x_square = [i**2 for i in x]
x_square_sum = sum(x_square)

x_y = [x[i]*y[i] for i in range(n)]
x_y_sum = sum(x_y)

a1=n
b1=x_sum
c1=y_sum
a2=x_sum
b2=x_square_sum
c2=x_y_sum

A = np.array([[a1, b1], [a2, b2]])
C = np.array([c1, c2])

if np.linalg.det(A) != 0:
    solution = np.linalg.solve(A, C)
    p, q = solution
    print(f"y = {p} + ({q})x")
else:
    print("No Solution.")

y2 = [math.log(i) for i in y]
sum_y2 = sum(y2)
avg_y = sum_y2/n
avg_x = x_sum/n

a_1 = ((n*x_y_sum)-(x_sum*avg_y))/(n*x_square_sum-x_sum**2)
a_0 = avg_y - a_1*avg_x
a = math.exp(a_0)
print(f"y = {a}e^{a_1}x")

