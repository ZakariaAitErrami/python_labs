from pickle import TRUE



Tas = (1,2,3,4,5,6)
Allumettes = [1,2,3, 4 ,5 ,6]


    


def print_game_state():
    for i in range(0,len(Allumettes)):
        print("Tas %d => %d" %(Tas[i] ,Allumettes[i]))
        


def game_over():
    a = True
    for i in range(0, len(Allumettes)):
        if Allumettes[i]!=0:
            a = False
    return a

def validate_tas_allumette_number(ntas, nallum):
    a = True
    if(ntas>6 or ntas<0):
        print("Invalid numbre of tas")
        a=False
    elif(Allumettes[ntas-1] < nallum):
        print("Sorry you can't remove %d of allumette, in this tas there is %d" %(nallum,Allumettes[ntas-1]))
        a=False
    return a


player1 = input("Enter your name (Player1): ")
player2 = input("Enter your name (Player2): ")
print("Welcome to the game ",player1, " and ", player2)

while True:
    print_game_state()
    print("------------------ Player 1: %s ------------------ " %(player1))
    tasa = int(input("Enter the tas number: "))
    alum = int(input("Enter the number of allumette you want to remove: "))
    if validate_tas_allumette_number(tasa,alum)==False:
        print("**Try Again**")
        continue
    else:
        Allumettes[tasa-1]-=alum
        if game_over()==True:
            print(player1," (player1) you have lost")
            print("The winner is ", player2)
            break
    print_game_state()
    print("------------------ Player 2: %s ------------------ " %(player2))
    tasa = int(input("Enter the tas number: "))
    alum = int(input("Enter the number of allumette you want to remove: "))
    if validate_tas_allumette_number(tasa,alum)==False:
        print("**Try Again**")
        continue
    else:
        Allumettes[tasa-1]-=alum
        if game_over()==True:
            print(player2," (player2) you have lost")
            print("The winner is ", player1)
            break
