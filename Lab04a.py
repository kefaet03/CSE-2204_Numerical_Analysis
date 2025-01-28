import numpy as np
import math

def difference_table(y_values):
    n = len(y_values)
    table = np.zeros((n, n))
    table[:, 0] = y_values

    for j in range(1, n):
        for i in range(n - j):
            table[i, j] = table[i + 1, j - 1] - table[i, j - 1]

    return table

def compute_u_product(u, x):
    result = 1
    for i in range(x):
        result *= (u - i)
    return result

def compute_v_product(v, x):
    result = 1
    for i in range(x):
        result *= (v + i)
    return result

def compute_u_g_f(p,x):
    temp = p
    for i in range (1,x):
        if i%2==0:
            temp *= (p-i) 
        else:
            temp *= (p+1)    
    return temp

def compute_v_g_b(p,x):
    temp = p
    for i in range (1,x):
        if i%2==0:
            temp *= (p+i) 
        else:
            temp *= (p-i)    
    return temp            

def newton_forward(table,u):
    result  = 0.0
    for i in range (table.shape[1]):
        result += (compute_u_product(u,i)/math.factorial(i))*table[0][i]
    return result    

def newton_backward(table,v):
    result  = 0.0
    for i, j in zip(range(0, table.shape[1]-1), range(table.shape[0]-1, -1, -1)):
        result += (compute_u_product(v,i)/math.factorial(i))*table[j][i]
    return result

def gauss_forward(table,a_index,p):
    result=table[a_index,0]
    p=1
    sign = 1

    for i in range (1,table.shape[0]):
        result += (compute_u_g_f(p,i) * table[(table.shape[1]-i)//2, i]) / math.factorial(i)

    return result    

def gauss_backward(table,a_index,p):
    result=table[a_index,0]
    p=1
    sign = 1

    for i in range (1,table.shape[0]):
        result += (compute_u_g_f(p,i) * table[(table.shape[1]-i)//2, i]) / math.factorial(i)

    return result

x = [1.0, 1.05,1.10,1.15,1.20,1.25,1.30]
y = [2.7183,2.8577,3.0042,3.1582,3.3201,3.4903,3.6693]

table = difference_table(y)

x0 = float(input("X = "))

choose = int(input("Method: 1.Newton's Forward 2.Newton's Backward 3.Gauss Forward 4.Gauss Backward\n"))

while(1):
    if choose==1:
        u = (x0-x[0])/(x[1]-x[0])
        answer1 = newton_forward(table,u)
        print(answer1)
    if choose==2:
        v = (x[-1]-x0)/(x[1]-x[0])
        answer2 = newton_backward(table,v)
        print(answer2)
    if choose==3:
        a_index = len(x)//2
        a = x[a_index]
        p = (x0-a)/(x[1]-x[0])
        answer3= gauss_forward(table,a_index,p)
        print(answer3)
    if choose==4:
        a_index = len(x)//2
        a = x[a_index]
        p = (x0-a)/(x[1]-x[0])
        answer4= gauss_backward(table,a_index,p)
        print(answer4)    
    break


