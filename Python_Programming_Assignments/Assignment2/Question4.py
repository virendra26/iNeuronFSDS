#solve quadratic equation


import math

def sqaureroot(a, b, c):

    val = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(val))

    if val > 0:
        print(" Roots of quadratic equation are real and distinct ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif val == 0:
        print("Roots of given equation are real and same roots")
        print(-b / (2 * a))


    else:
        print("Roots of given equation are Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

a=int(input('Coefficient of x^2 '))
b=int(input('Coefficient of x '))
c=int(input('Constant term '))

while a==0:
    print('Wrong input')
    a = int(input('Coefficient of x^2 '))
    b = int(input('Coefficient of x '))
    c = int(input('Constant term '))

else:
    sqaureroot(a,b,c)