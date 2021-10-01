from functools import partial, reduce

def suma_cuadrados(v):
    return sum(i*i for i in v)

def limite_gradiente(f,v,i,h):
    v2 = [v_j + (h if j==i else 0) for j, v_j in enumerate(v)]
    return (f(v2)-f(v))/h

def estimacion_gradiente(f, v, h):
    return [limite_gradiente(f,v,i,h) for i in range(len(v))]

gradiente = partial(estimacion_gradiente, suma_cuadrados, h=0.0001)

v = [1,1,1]
g=gradiente(v)
while any([i>0.0001 for i in g]):
    v = [i+j*-0.0001 for i, j in zip(v,g)]
    g=gradiente(v)

fmt = lambda x: round(x, 4)
print(f"Minimo de la funcion f: {fmt(suma_cuadrados(v))}, en el punto {[fmt(i) for i in v]}")