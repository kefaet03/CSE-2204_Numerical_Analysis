a=float(input())
b=float(input())
h=float(input())
n=int((b-a)/h)
x_values = [a+i*h for i in range (n+1)]
y_values = [1 / (x + 1) if (x + 1) != 0 else None for x in x_values]
def trapezoidal_rule(x_values, y_values, h):
    result = y_values[0] + 2 * sum(y_values[1:-1]) + y_values[-1]
    result = result * 0.5 * h
    return result
def simson_rule_1(x_values, y_values, h):
    odd_sum = sum(y_values[1:-1:2])  
    even_sum = sum(y_values[2:-1:2]) 

    result = y_values[0] + 4*odd_sum + 2*even_sum + y_values[-1]
    result *= h / 3  
    return result
def simson_rule_2(x_values,y_values,h):
    div_3 = 0
    div_not_3  = 0
    for i in range(1,len(y_values)):
        if i % 3 == 0:
            div_3 += y_values[i]
        else:
            div_not_3 += y_values[i]

    result = y_values[0]+ 3*div_not_3 + 2*div_3 + y_values[-1]
    result = result * (3/8) * h
    return result

way_1 = trapezoidal_rule(x_values, y_values,h)
way_2 = simson_rule_1(x_values, y_values,h)
way_3 = simson_rule_2(x_values, y_values,h)

print(way_1)
print(way_2)
print(way_3)