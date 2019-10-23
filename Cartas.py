import random
from fcartas import *

bar=[]
jugador=[]
casa=[]
for v in ['A','2','3','4','5','6','7','8','9','J','Q','K']:
   for p in ['C','D','P','T']:
        bar.append(v+p)

#print(bar)


for i in (0,1):
  casa.append(bar[random.randint(0,47)])
for j in (0,1):
  jugador.append(bar[random.randint(0,47)])
print("Casa: " + str(casa))
print("Jugador: " + str(jugador))

sumacartas(casa)

