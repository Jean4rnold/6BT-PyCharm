#se requiere obtener la distancia de dos puntos
from math import sqrt
print("ingrese los valores del primer punto (P1)")
x1 = float(input("Ingresar valor de x1: "))
y1 = float(input("Ingrese el valor de y1: "))
z1 = float(input("Ingrese el valor de z1: "))
m1 = float(input("Ingrese el valor de m1: "))
n1 = float(input("Ingrese el valor de n1: "))
print("ingrese los valores del segundo punto (P2): ")
x2 = float(input("Ingresar valor de x2: "))
y2 = float(input("Ingresar valor de y2: "))
z2 = float(input("Ingresar valor de z2: "))
m2 = float(input("Ingrese el valor de m2: "))
n2 = float(input("Ingrese el valor de n2: "))

distacia = sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2+(m2-m1)**2+(n2-n1)**2)

print("la distancia entre los puntos es: ",distacia)


