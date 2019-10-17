import random
numero =[]

cifra=int(input("Digite cifra de número a jugar: "))

while len(numero) < cifra :
    digito =random.randint(0,9)
    if digito not in numero:
        numero.append(digito)

print(" El numero a adivinar es: "+str(numero))

while True:
    intento=input("Ingrese número: ")

    usuario = []
    for i in intento:
        if  int (i) not in usuario:
            usuario.append(int(i))

    if len(usuario) != len(numero):
        print("intento no valido")
    else:
        break

print(usuario,numero)
picas=0
fijas=0

    for i in range (len(numero)):
        for j in range (len(usuario)):
            if numero[i]==usuario[j] and i!=j:
               picas=picas+1

print(picas)
print(fijas)
