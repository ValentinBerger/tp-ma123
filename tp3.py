from math import sin , log, tan , cos , exp, acos
from math import log as ln
def PointFixe (f,fder,x0,epsilon,Nitermax):
    
    xold= x0
    xnew = xold - f(xold)/fder(xold)
    n= 1
    
    while abs(xnew-xold) > epsilon and n < Nitermax :
        xold=xnew
        xnew = xold - f(xold)/fder(xold)
        n+=1
          
    return xnew ,n

def f1(x):
    return  (x**4)+3*x-9
def fder1(x):
    return 4*x**3 +3

def f2(x):
    return 3*cos(x)-2-x
def fder2(x):
    return -3*sin(x)-1

def f3(x):
    return x*(exp(x))-7
def fder3(x):
    return x*exp(x)+exp(x)

def f4(x):
    return exp(x)-x-10
def fder4(x):
    return exp(x)-1

def f5(x):
    return 2*tan(x)-x-5
def fder5(x):
    return 2/(cos(x)**2)-1 

def f6(x):
    return exp(x)-x**2-3
def fder6(x):
    return exp(x)-2*x

def f7(x):
    return 3*x+4*ln(x)-7
def fder7(x):
    return 3 + 4/x

def f8(x):
    return x**4 -2*x**2+4*x-17
def fder8(x):
    return 4*x**3-4*x+4

def f9(x): 
    return  exp(x)-2*sin(x) -7
def fder9(x):
    return exp(x) -2*cos(x)

def f10(x):
    return ln(x**2+4)*exp(x)-10
def fder10(x):
    return (2*exp(x)*x)/(x**2+4) +exp(x)*ln(x**2+4)


'''
print(PointFixe(f1,fder1,3/2,1e-10,5e4)) #solution 1 pour f1
print(PointFixe(f1,fder1,-2,1e-10,5e4)) #solution 2 pour f1

print(PointFixe(f2,fder2,0.4,1e-10,5e4)) #solution 1 pour f2
print(PointFixe(f2,fder2,-3/2,1e-10,5e4))#solution 2 pour f2

print(PointFixe(f3,fder3,2,1e-10,5e4))#solution 1 pour f3

print(PointFixe(f4,fder4,3,1e-10,5e4)) #solution 1 pour f4
print(PointFixe(f4,fder4,-10,1e-10,5e4)) #solution 2 pour f4


print(PointFixe(f5,fder5,1.2,1e-10,5e4))#solution 1 pour f5

print(PointFixe(f6,fder6,1.2,1e-10,5e4))#solution 1 pour f6


print(PointFixe(f7,fder7,3/2,1e-10,5e4)) #solution 1 pour f7

print(PointFixe(f8,fder8,3/2,1e-10,5e4))#solution 1 pour f8
print(PointFixe(f8,fder8,-2.8,1e-10,5e4))#solution 2 pour f8


print(PointFixe(f9,fder9,3.14/2,1e-10,5e4))#solution 1 pour f8

print(PointFixe(f10,fder10,3/2,1e-10,5e4)) #solution 1 pour f10

'''

