import math
def suma(a,b):
    suma_R = a[0] + b[0]
    suma_i = a[1] + b[1]
    return(suma_R,suma_i)
def producto(a,b):
    producto_R = ( a[0] * b[0] ) -(a[1]*b[1])
    producto_i = ( a[0] * b[1] ) +(a[1]*b[0])
    return(producto_R,producto_i)
def resta(a,b):
    resta_R = a[0] - b[0]
    resta_i = a[1] - b[1]
    return(resta_R,resta_i)
def division(a,b):
    division_R = ((a[0]*b[0])+(a[1]*b[1]))/((b[0]**2)+(b[1]**2))
    division_i = ((b[1]*a[1])-(a[0]*b[1]))/((b[0]**2)+(b[1]**2))
    return(division_R,division_i)
def modulo(a):
    mod = (((a[0])**2)+((a[1])**2))**(1/2)
    return(mod)
def conjugado(a):
    part_R = a[0]
    parte:i = a[1]*-1
    return(parte_R,parte_i)
def fase(a):
    angulo_rad = math.atan2(a[1] ,a[0])
    angulo_G = math.degrees(angulo_rad)
    return(angulo_G)
def cartesiana(a):
    modulo = modulo(a)
    angulo = fase(a)
    return (modulo,angulo)    
#[]><
