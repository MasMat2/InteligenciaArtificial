import random, math
f = lambda x: x*x*x*(x-2)
derivada = lambda f, x, h=0.00001: (f(x+h)-f(x))/h

sign = lambda x: bool(x > 0) - bool(x < 0)
x=-1
d=derivada(f, x)
signo0 = sign(d)

while signo0*sign(d) != -1:
    x = x+sign(d)*-math.pow(2, -10)
    d=derivada(f, x)
    

print(x)