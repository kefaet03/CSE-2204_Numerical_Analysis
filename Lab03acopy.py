import sympy as sp

def poly(coeff,x):
    return sum((c*pow(x,len(coeff)-1-i)) for i,c in enumerate(coeff))

def diff(coeff,x):
    return sum(((len(coeff)-1-i)*c*pow(x,len(coeff)-1-i-1)) for i,c in enumerate(coeff))

def newton_raphson(coeff, tol=1e-3, max_iter=100):
    x0 = float(input("Enter the initial guess: "))
    x_r = x0

    print(f"Iteration | x_r")
    
    for i in range(max_iter):
        x_new = x_r - poly(coeff,x_r) / diff(coeff,x_r)
        print(f"{i+1}  {x_r:.6f}")

        if abs(x_new - x_r) < tol:
            return x_new
        
        x_r = x_new

    return x_r

def ramanujan(coeff,tol=1e-3,max_iter=100):
    c = coeff[-1]

    a = [float(coef/c*-1) for coef in coeff]

    partial_a = a[:-1]

    reverse_partial_a = partial_a[::-1]

    b = [1.0]
    ratio_list = [0.0]

    # print(reverse_partial_a)

    i=1
    while i <= max_iter:
        new_b = 0
        for j in range(i):
            if i - j - 1 < len(reverse_partial_a):
                new_b += reverse_partial_a[i - j - 1] * b[j]
           
        b.append(new_b)

        ratio = b[i-1] / b[i]
        ratio_list.append(ratio)
    
        print(f"{i}  {ratio:.6f}")

        if abs(ratio_list[i]-ratio_list[i-1]) < tol :
            return ratio
    
        i += 1
    

order = int(input("Order :"))

print("The form of the equation\nax^(n) + bx^(n-1) + ..... + ex + z = 0\nEnter the co-efficients")

coeff = []
c = input()
coeff = [float(i) for i in c.split()]
    
while 1:
    print("The method you want\n1.Newton Raphson\n2.Ramanujan\n3.Exit")
    choice = int(input())
    if choice==1:
        # Run Newton-Raphson method
        root = newton_raphson(coeff)
        print(f"Root is approximately: {root:.6f}")
    elif choice == 2:
        root =  ramanujan(coeff)
        print(f"Root is approximately: {root:.6f}")
    else:
        break    


