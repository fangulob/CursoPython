def sumacartas (lista):
    k=0
    for i in range(len(lista)):
       t=lista[i]
       n=t[0]
       if (n=='J')or(n=='Q')or(n=='K')or(n=='A'):
           print("letra: " + str(n))
       else:
           #k=int(n)
           k = k + int (n)
           print k
