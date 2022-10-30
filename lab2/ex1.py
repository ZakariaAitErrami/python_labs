from calendar import monthrange
from sys import exit

zellerdays = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def nbJour(month, year):
    return monthrange(year, month)[1] #numdays

def give_day(date):
    
    datel = date.split('-')
    j=int(datel[0])
    m=int(datel[1])
    s=(int(datel[2])//100)
    a = int(datel[2])%100
    if(nbJour(m,int(datel[2]))<j):
        print("Date invalide")
        exit()
    zeller = ( (j+ ((26*(m+1))/10) +a +a/4 + s/4 + 5*s) ) %7
    return int(zeller)

strDate = input("Enter a date (dd-mm-yyyy): ")

q =give_day(strDate)
print(q)
print("The day is: %s" %(zellerdays[q]))