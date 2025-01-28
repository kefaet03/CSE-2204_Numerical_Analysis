import numpy as np


def forward_difference_table(y_values):
    n = len(y_values)
    table = np.zeros((n, n))
    table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    return table

def newton_forward_derivative(x_values, y_values, x,target_index):
    h = x_values[1] - x_values[0]
    table = forward_difference_table(y_values)
    # print(table)

    derivative = 0.0

    for i in range (1,table.shape[1]-target_index):
        if i%2!=0:
            derivative+= (1/i) * table[target_index][i]
        else:
            derivative += (-1/i) * table[target_index][i]   
    
    derivative *= (1/h)
    second_diff_coeff = [1,-1,11/12,-5/6,137/180,-7/10,363/560]
    second_derivative = 0.0
    i=0
    for j in range (2,table.shape[1]-target_index):
        second_derivative += second_diff_coeff[i]*table[target_index][j]
        i+=1
    second_derivative *= 1/(h**2)
    result = [derivative,second_derivative]
    return result


x = [1, 1.2, 1.4, 1.6, 1.8,2.0,2.2]
y = [2.7183, 3.3201, 4.0552, 4.9530, 6.0496,7.3891,9.0250]

x_target = 1.2
target_index = x.index(1.2)

derivatives = newton_forward_derivative(x, y, x_target,target_index)

print(derivatives)