# Dice game
import random
list1 = [1, 2, 3, 4, 5, 6]

PlayersGrade = {"Player1":0, "Player2":0}

while True:
    if(PlayersGrade["Player1"]>=50 or PlayersGrade["Player1"]>=50 ):
        break
    player1Number = random.choice(list1)
    print("Player1 => ",player1Number)
    if player1Number%2==0:
        PlayersGrade["Player1"]+=player1Number
    elif player1Number==3:
        PlayersGrade["Player1"]*=2
    elif player1Number==5:
        PlayersGrade["Player1"]-=2
    else:
        pass
    print(PlayersGrade)
    #Player2 turn
    player2Number = random.choice(list1)
    print("Player2 => ",player2Number)
    if player2Number%2==0:
        PlayersGrade["Player2"]+=player2Number
    elif player2Number==3:
        PlayersGrade["Player2"]*=2
    elif player2Number==5:
        PlayersGrade["Player2"]-=2
    else:
        pass 
    print(PlayersGrade)

print(PlayersGrade)

winner = "Player1" if PlayersGrade["Player1"]>PlayersGrade["Player2"] else "Player2"

print("The winner is %s" %(winner))