from module_ex6 import *

lstParfait = list()
lstChanceux = list()

for n in range(2, 1001):
    if(estParfait(n)):
        lstParfait.append(n)
    if(estChanceu(n)): lstChanceux.append(n)

print("Parfait: \n", lstParfait)
print("Chancaux: \n", lstChanceux)