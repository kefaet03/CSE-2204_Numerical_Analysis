import sympy as sp

def newton_raphson(f_x, tol=1e-3, max_iter=100):
    x0 = float(input("Enter the initial guess: "))

    x = sp.symbols('x')

    f = sp.lambdify(x, f_x)
    
    df_expr = sp.diff(f_x, x)
    df = sp.lambdify(x, df_expr)
    
    x_r = x0
    print(f"Iteration | x_r")
    
    for i in range(max_iter):
        x_new = x_r - f(x_r) / df(x_r)
        print(f"{i+1}  {x_r:.6f}")

        if abs(x_new - x_r) < tol:
            return x_new
        
        x_r = x_new

    return x_r

def ramanujan(f_x,tol=1e-3,max_iter=100):
    x=sp.symbols('x')

    coeff = sp.Poly(f_x, x).all_coeffs()

    coeff = [float(coef) for coef in coeff]
    # print(coeff)

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

x = sp.symbols('x')
f_x = x**3 - 6*x**2 + 11*x - 6

print("The form of the equation\nax^(n) + bx^(n-1) + ..... + ex + z = 0\nEnter the co-efficients")

    
while 1:
    print("The method you want\n1.Newton Raphson\n2.Ramanujan\n3.Exit")
    choice = int(input())
    if choice==1:
        # Run Newton-Raphson method
        root = newton_raphson(f_x)
        print(f"\nRoot is approximately: {root:.6f}")
    elif choice == 2:
        root =  ramanujan(f_x)
        print(f"\nRoot is approximately: {root:.6f}")
    else:
        break    


