def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def product(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

a = float(input('Please enter the value of a: '))
b = float(input('Please enter the value of b: '))
c = float(input('Please enter the value of c: '))
d = float(input('Please enter the value of d: '))

#Please enter your code here for computing and displaying the result of the expression.
A = divide(d,4)
B = divide(power(a,b),2.1)
C = power(divide(c,(add(d,product(a, 4)))),divide(2,c))
D = product(B,C)
E = subtract(A, D)
print(E)
