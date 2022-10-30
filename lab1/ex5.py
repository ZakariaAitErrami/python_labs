from math import *
def heron (a, eps=0.000001):
    ua = a
    while (True):
        up = ua
        ua = (up + a / up) /2
        if(up-ua <=eps): break
    return ua

a = float(input("A = "))


print("Racine ( %f ) = Math %f et Heron %f" %(a,sqrt(a) ,heron(a)))