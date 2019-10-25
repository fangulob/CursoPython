from punto import *
from math import pi

class Figura:

    
       def __init__(self,p1,p2):
           self.origen=p1
           self.destino=p2
           self.area=0
           self.perimetro=0

class Cuadrado(Figura):

     def calcular_area(self):
         lado=self.origen.calcular_distancia(self.destino)
         self.area=lado*lado
         

     def calcular_perimetro(self):
         lado=self.origen.calcular_distancia(self.destino)
         self.perimetro=lado*4

class Circulo(Figura):

    def calcular_area(self):
        radio=self.origen.calcular_distancia(self.destino)
        self.area=pi*(radio**2)

    def calcular_perimetro(self):
         radio=self.origen.calcular_distancia(self.destino)
         self.perimetro=(2*pi)*radio

class Triangulo(Figura):

    def calcular_area(self):
        temp=Punto(self.origen.x,self.destino.y)
        base=temp.calcular_distancia(self.destino)
        altura=temp.calcular_distancia(self.origen)
        hipotenusa=self.origen.calcular_distancia(self.destino)
        self.area=(base*altura)/2

    def calcular_perimetro(self):
        temp=Punto(self.origen.x,self.destino.y)
        base=temp.calcular_distancia(self.destino)
        altura=temp.calcular_distancia(self.origen)
        hipotenusa=self.origen.calcular_distancia(self.destino)
        self.perimetro=base+altura+hipotenusa
    
