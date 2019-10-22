import random
numero =[]

cifra=int(input("Digite cifra de número a jugar: "))

while len(numero) < cifra :
    digito =random.randint(0,9)
    if digito not in numero:
        numero.append(digito)

print(" El numero a adivinar es: "+str(numero))

repetir=True

while repetir:

   while True:
     intento=input("Ingrese número: ")

     usuario = []
     for i in intento:
        if  int (i) not in usuario:
            usuario.append(int(i))

     if len(usuario) != len(numero):
        print("intento no valido: Favor digite un número de "+str(len(numero))+" cifras")
     else:
          break

   print("Numero generado al azar es: "+str(numero)+" y el numero digitado por el usuario es :"+str(usuario))
   picas=0
   fijas=0

   for i in range (len(numero)):
     for j in range (len(usuario)):
        if numero[i]==usuario[j] and i!=j:
           picas=picas+1
        if numero[i]==usuario[j] and i==j:
           fijas=fijas+1
         
   print("La cantidad de picas es:"+str(picas))
   print("La cantidad de fijas es:"+str(fijas))
   intento =[]
   seguir=input("Desea seguir intentando ? Digite (y) para si,Digite (n) para finalizar: ")

   if (seguir=="y"):
        repetir=True
   else:
        repetir=False
