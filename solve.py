import math
import cmath
 
def solve(a, b, c):
    if a == 0 and b == 0 and c == 0:
        print("X is any number!")
    else:
        if a == 0 and b == 0:
            print("There are no solutions!")
        else:
            if a == 0 and c == 0:
                print("x =", 0)
            else:
                if a == 0:
                    x = (-c / b)
                    print("x =", x)
                else:
                    d = b * b - 4 * a * c
                    if d > 0:
                        x1 = (-b + math.sqrt(d)) / (2 * a)
                        x2 = (-b - math.sqrt(d)) / (2 * a)
                        if x1 == x2:
                            print("x1 =", x1)
                        else:
                            print("x1 =", x1)
                            print("x2 =", x2)
                    else:
                        x1 = (-b + cmath.sqrt(d)) / (2 * a)
                        x2 = (-b - cmath.sqrt(d)) / (2 * a)
                        if x1 == x2:
                            print("x1 =", x1)
                        else:
                            print("x1 =", x1)
                            print("x2 =", x2)
                        
def get_coef():
    print('ax^2+bx+c, write a, b and c:')
    a = int(input('a: '))
    b = int(input('b: '))
    c = int(input('c: '))
    solve(a, b, c)
    
get_coef()