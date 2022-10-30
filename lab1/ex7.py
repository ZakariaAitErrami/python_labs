from module_ex6 import *


def jumeau(n):
    l = list()
    i = n+1
    while len(l)!=2:
        if (estPremier(i) and estPremier(i+2)):
            l.append(i)
            l.append(i+2)
        else:
            i=i+1
    return l

def lesJummeaux(n):
    blist = list()
    slist = list()
    i=1
    while i<=n:
        if(estPremier(i) and estPremier(i+2) and i+2<=n):
            slist.append(i)
            slist.append(i+2)
            blist.append(slist)
            slist = list() #Initialize the list another time to remove all its elements 
        i+=1
    return blist
 
l = jumeau(5)
b = lesJummeaux(18)
print(l)
print(b)
