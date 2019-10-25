from figuras import *


p1=Punto(5,5)
p2=Punto(10,10)


cuadrado=Cuadrado(p1,p2)
circulo=Circulo(p1,p2)
triangulo=Triangulo(p1,p2)

cuadrado.calcular_area()
cuadrado.calcular_perimetro()
circulo.calcular_area()
circulo.calcular_perimetro()
triangulo.calcular_area()
triangulo.calcular_perimetro()


print("El área de un cuadrado es:"+str(cuadrado.area))
print("El perímetro de un cuadrado es:"+str(cuadrado.perimetro))
print("El área de un circulo es:"+str(circulo.area))
print("El perímetro de un circulo:"+str(circulo.perimetro))
print("El área de un triangulo:"+str(triangulo.area))
print("El perímetro de un triangulo:"+str(triangulo.perimetro))
