import random
bar=[]

def cargarb(l):
    for b in ("A","2","3","4","5","6","7","8","9","10","J","Q","K"):
        for p in ("C","D","T","P"):
          bar.append(b+p)
    return bar

def gst(g):
    cini=[]
    for h in(0,1):
       cini.append(bar[random.randint(0,51)])
    return cini
 

def sumcar(lista):
    r=0
    for i in range (len(lista)):
        k=lista[i]
        t = k[0]
       
        if (t == "K")or(t == "Q")or(t == "J")or (k[1]=='0'):
           r=r+10
        elif (t == "A"):
           r=r+1
        else:
           r = r + int(t)
    return r

def nuevacarta(lista):
    n=0
    lista.append(bar[random.randint(0,51)])
    n=sumcar(lista)          
    return lista,n
