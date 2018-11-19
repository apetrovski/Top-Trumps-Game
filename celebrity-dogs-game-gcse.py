#Celebrity Dogs Game
#Anton Petrovski
#Computer Science
import random
from random import shuffle, randint
from pprint import pprint
import json
def Compare(player, Computer):
    PlGo,CompG0=1,0
    player=player
    computer=Computer
    i,j=0,0
    while len(player)>0 and len(computer)>0:
        while PlGo==1 and len(computer)!=0 and len(player)!=0:
            choice=input("what atribute do you want to use:\n\t Exercise\n\t Intelligence\n\t Friendliness\n\t Drool\n\t")
            print(choice)
            if choice in ["Exercise","Intelligence","Friendliness"]:
                print("This was the Computers card:\n",json.dumps(computer[j], indent = 4))
                if player[i][choice]>computer[j][choice]:
                    PlGo,CompG0=1,0
                    player.extend([player.pop(0),computer.pop(0)])
                    print("you won the round\n",json.dumps(player, indent = 4))
                else:
                    computer.extend([computer.pop(0),player.pop(0)])
                    PlGo,CompG0=0,1
                    print("computer won the round\n",json.dumps(player, indent = 4))
                    break
            elif choice == "Drool":
                print("This was the Computers card:\n",json.dumps(computer[j], indent = 4))
                if player[i][choice]<computer[j][choice]:
                    PlGo,CompG0=1,0
                    player.extend([player.pop(0),computer.pop(0)])
                    print("you won the round",json.dumps(player, indent = 4))
                else:
                    computer.extend([computer.pop(0),player.pop(0)])
                    PlGo,CompG0=0,1
                    print("computer won the round\n",json.dumps(player, indent = 4))
                    break
        while CompG0==1 and len(computer)!=0 and len(player)!=0:
            choice2=random.choice(["Exercise","Intelligence","Friendliness","Drool"])
            print("Computers choice is:\t",choice2)
            if choice in ["Exercise","Intelligence","Friendliness"]:
                print("This was the Computers card:\n",json.dumps(computer[j], indent = 4))
                if player[i][choice2]>computer[j][choice2]:
                    PlGo,CompG0=1,0
                    player.extend([player.pop(0),computer.pop(0)])
                    print("you won the round\n",json.dumps(player, indent = 4))
                    break
                else:
                    computer.extend([computer.pop(0),player.pop(0)])
                    PlGo,CompG0=0,1
                    print("computer won the round\n",json.dumps(player, indent = 4))
            elif choice == "Drool":
                print("This was the Computers card:\n",json.dumps(computer[j], indent = 4))
                if player[i][choice2]<computer[j][choice2]:
                    PlGo,CompG0=1,0
                    player.extend([player.pop(0),computer.pop(0)])
                    print("you won the round\n",json.dumps(player, indent = 4))
                    break
                else:
                    computer.extend([computer.pop(0),player.pop(0)])
                    PlGo,CompG0=0,1
                    print("computer won the round\n",json.dumps(player, indent = 4))
        if len(computer)==0:
            print("\t\tPlayer Wins\n\t\tThe End\n\n")
            break
        elif len(player)==0:
            print("\t\tComputer Wins\n\t\tThe End\n\n")
            break
def Players(FinCards):
    player=[FinCards[i] for i in range(0,len(FinCards),2)]
    Computer=[each for each in FinCards if each not in player]
    print("These are your cards:\t\n",json.dumps(player, indent = 4))
    Compare(player, Computer)
def Cards(CardNum):
    with open("dogs.txt","r") as f:
        for i in range(0,len(CardNum)):
            lines=(f.read().splitlines()[:int(CardNum)])
            shuffle(lines)
            FinCards=[]
            for dog in lines:
                FinCards.append({"Name":dog,
                                "Exercise":randint(1,6),
                                "Intelligence":randint(1,101),
                                "Friendliness":randint(1,11),
                                "Drool":randint(1,11)})
            Players(FinCards)
def Start():
        CardNum=(input("Type the number of cards you want (4:30) only even numbers please:\t"))
        if CardNum in ["4","6","8","10","12","14","16","18","20","22","24","26","28","30"]:
            Cards(CardNum)
        else:
            print("Try again")
while True:
    start=input("Do you want to play:\t").upper()
    if start in ["YES","NO"]:
        if start=="NO":
            print("Goodbye")
            break
        elif start=="YES":
            Start()


        
