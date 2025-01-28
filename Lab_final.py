import math

def poly(coeff, x):
    result = 0.0
    for i in range (0,len(coeff)):
        result += coeff[i] * pow(x, len(coeff) - i - 1)
    return result

def bisection(coeff):
    print("Approxitmation: ")

    for i in range(1,50):
        a = float(input("a: "))
        b = float(input("b: "))

        if poly(coeff,a) * poly(coeff, b) < 0:
            break
        else:
            print("Invalid")

    xr = 0
    count = 0
    error = 0
    max_iterations = 100

    for i in range (0,max_iterations):
        temp = xr
        xr = (a + b) / 2

        if count > 0 :
            error = abs(xr - temp)

        print(f"{count} {a} {b} {xr} {error}")
        count+=1

        f_xr = poly(coeff,xr)

        if f_xr == 0 or (error <= 0.001 and count > 1) :
            break

        if poly(coeff, a) * f_xr < 0:
            b = xr
        else:
            a = xr
    return xr

def diff(coeff,x):
    return sum(((len(coeff)-1-i)*c*pow(x,len(coeff)-1-i-1)) for i,c in enumerate(coeff))

def newton(coeff):
    x0 = float(input("Enter the initial guess: "))
    x_r = x0

    print(f"Iteration | x_r")
    max_iter=100
    tol=1e-5

    for i in range(max_iter):
        x_new = x_r - poly(coeff,x_r) / diff(coeff,x_r)
        print(f"{i+1}  {x_r:.6f}")

        if abs(x_new - x_r) < tol:
            return x_new
        
        x_r = x_new

    return x_r


order = int(input("Order: "))
c = input("Enter the co-efficients: ")
coeff = []
coeff = [float(i) for i in c.split()]

while(1):
    print("1.Bisection\n2.Newton Raphson\n")
    choose = int(input("Select: "))
    if choose == 1:
        root1 = bisection(coeff)
        print(root1)
    elif choose == 2:
        root2 = newton(coeff)
        print(root2)
    else:
        break;        






























































