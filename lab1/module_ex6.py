def somDiv(n):
    s=1
    for i in range(2,n//2+1):
        if(n%i==0): s+=i
    return s

def estParfait(n):
    return somDiv(n)==n

def estPremier(n):
    return somDiv(n)==1

# 0<=a <=n-1 =>il faut que n+a+pow(a,2) premier
def estChanceu(n):
    for a in range(0,n-1):
        if not estPremier(n+a+a*a): return False
    return True
