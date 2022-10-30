def isAlternate(l):
    for i in range(0, len(l)):
        if(i!=len(l)-1): 
            if (l[i] * l[i+1] > 0): return False
        
        if(i%2==0) and (l[i]!=i): return False
        if(i%2!=0) and (l[i]!=-i): return False
    return True

lst = [0, -1, 2, -3, 4, -5]


print(isAlternate(lst))