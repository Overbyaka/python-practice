import math

def f11(x, y): #Задача 1.1
    return "{0:.2e}".format(((y + y**2 - 46)/(x**2-y)-(x**3+math.tan(y))/(x**3+x**4)-(x**5+y**8)/(73*y**2-y/11-8)))

def f12(x): #Задача 1.2
    if x < 53:
        return "{0:.2e}".format(x**5/82-18*x**6-39)
    elif x < 138:
        return "{0:.2e}".format(76*x**5+x**6-10)
    elif x < 233:
        return "{0:.2e}".format(x**3-3*x**5+math.fabs(x))
    elif x < 296:
        return "{0:.2e}".format(71*(x**2-math.exp(x)+36)**7-math.fabs(x))
    else:
        return "{0:.2e}".format(x**5-x**6+27)

def f13(n, m): #Задача 1.3
    answer = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            answer += (j**5/82-18*i**6-39)
    answer = answer * 87
    for i in range(1, n+1):
        answer -= (math.log(i)+math.sin(i))
    return "{0:.2e}".format(answer)

def f14(n): #Задача 1.4
    if n == 0:
        return "{0:.2e}".format(4)
    else:
        return "{0:.2e}".format(1/61*float(f14(n-1))**2+1/66*float(f14(n-1)))

print(f11(-15, -85))
print(f11(30, 80))
print(f12(383))
print(f12(360))
print(f13(27, 19))
print(f13(12, 40))
print(f14(3))
print(f14(15))