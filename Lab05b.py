import numpy as np













coeff=[]
order = int(input("Oder: "))
c = input("Enter the co-efficients: ")
coeff= [float(i) for i in c.split()]
arr = np.zeros((order+1,order+1))

for i in range (0,order+1):
    for j in range(i,order+i+1):
        
