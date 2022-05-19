# -*- Nuha Alghamdi -*-
# -*- nuhaalghamdi92@gmail.com -*-
# -*- Oct 18 2019 -*-

#import random library to generate random numbers
import random


#to draw the dice
ledge="[-----------]"
dice=[ledge,"[]","[]","[]",ledge]
zero="[           ]"
one="[     0     ]"
two="[   0   0   ]"

repeat="y"
while (repeat == "y"):

    #generate a random integer from 1 to 6
    number=random.randint(1,6)

    #draw the face based on the generated number
    if number == 1:
        dice[1]=zero
        dice[2]=one
        dice[3]=zero
    elif number ==2:
        dice[1]=zero
        dice[2]=two
        dice[3]=zero
    elif number==3:
        dice[1]=one
        dice[2]=one
        dice[3]=one
    elif number==4:
        dice[1]=two
        dice[2]=zero
        dice[3]=two
    elif number==5:
        dice[1]=two
        dice[2]=one
        dice[3]=two
    else:
        dice[1]=two
        dice[2]=two
        dice[3]=two
    for item in dice:
        print(item)
        
    #if user wants to roll again
    repeat=input("Chcesz powtórzyć rzut? Naciśij Y aby rzucić ponownie, naciśnij N, aby zakończyć")
    if repeat != "n" and repeat != "y":
        repeat=input("Nie wybrałeś żadnej opcji! Naciśnij y aby rzucić kością albo n jeżeli chcesz zakończyć grę")
