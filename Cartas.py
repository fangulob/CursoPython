from fcartas import *

baraja=[]
player=[]
house=[]

baraja=cargarb(baraja)

#print(baraja)

player=gst(player)
print("Sus cartas son: " + str(player))
print("Su Score es de: " + str(sumcar(player)))

house=gst(house)
print("La carta de la casa es: " + str(house[0]))

ciclo=True
while ciclo:

      seguir=input("Desea seguir jugando (y/n): ")

      if(seguir=='y'):
         player,sc=nuevacarta(player)
         print(player,sc)
         if(sc>21):
            print("Perdiste")
            break

      else:
           while True:
                 if(sumcar(house)>= sumcar(player)and sumcar(house)<= 21):
                    print("Perdiste,el score de la casa fue: "+str(sumcar(house)))
                    print(house)
                    ciclo=False
                    break
                 else:
                      house,sh=nuevacarta(house)
                      if(sh>21):
                          print("Ganaste")
                          print("El score de la casa fue: "+str(sh))
                          print(house)
                          ciclo=False
                          break
                          
                  

           
     
