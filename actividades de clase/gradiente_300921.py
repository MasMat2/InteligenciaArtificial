import random, math
import numpy as np
from fractions import Fraction

# Funcion a minimizar
f = lambda x,y,z: (x*x+y*y+z*z)

# Funcion para obtener el gradiente
gradiente = lambda : np.array([derivada(f, p, i) for i in range(3)])

# Elegimos un punto incial al azar
p = np.random.rand(3,1).transpose()

# Calcular derivada numericamente
def derivada (f, p, basis, h=0.00001): 
    p_h = p+h*np.eye(1,3,basis)
    f_h = f(*(p_h[0]))
    return (f_h-f(*(p[0])))/h

# Actualizar el vector, hasta que el nuevo valor de la funcion sea mayor o igual al anterior
old_v = math.inf
while old_v>(old_v:=f(*(p[0]))):
    p = p+gradiente()*-math.pow(2, -10)

# Equivalente a print(p), pero con reglas de formato
fmt = lambda x : str(x.round(3))
with np.printoptions(formatter={'float': lambda s: f'{fmt(s)}'}):
    print(f"Minimo de la funcion f: {fmt(f(*(p[0])))}, en el punto {p}")