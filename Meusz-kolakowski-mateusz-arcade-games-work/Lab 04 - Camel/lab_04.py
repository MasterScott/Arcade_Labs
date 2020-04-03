from functions import *
import random

get_started()
done = False
natives_dis = -20
camel_tiredness = 0
thirst = 0
player_dis = 0
drinks_in_canteen = 3

while not done:
    menu()
    option = str(input("What is your choice? ")).upper()
    if option == "Q":
        done = True
    elif option == "A":
        if drinks_in_canteen != 0:
            thirst = 0
            drinks_in_canteen -= 1
        else:
            print("Error")
    elif option == "B":
        dis_travelled = random.randint(5, 12)
        print("The player travelled %d" % dis_travelled)
        player_dis += dis_travelled
        thirst += 1
        camel_tiredness += 1
        natives_dis += random.randint(7, 14)
        oasis_found(drinks_in_canteen)
    elif option == "C":
        dis_travelled = random.randint(10, 20)
        print("The player travelled %d" % dis_travelled)
        player_dis += dis_travelled
        thirst += 1
        camel_tiredness += random.randint(1, 3)
        natives_dis += random.randint(7, 14)
        oasis_found(drinks_in_canteen)
    elif option == "D":
        camel_tiredness = 0
        print("The Camel is happy")
        natives_dis += random.randint(7, 14)
    elif option == "E":
        status(player_dis, drinks_in_canteen, natives_dis)
    else:
        print("No existing option")

    if camel_tiredness > 8:
        print("Your camel is dead")
        done = True
    elif camel_tiredness > 5:
        print("Your camel is getting tired")

    if thirst > 6:
        print("You died of thirst!")
        done = True
    elif thirst > 4:
        print("You are thirsty")

    if player_dis <= natives_dis:
        print("Los nativo te han capturado")
        done = True
    elif player_dis - natives_dis <= 15:
        print("The natives are getting close!")

    if player_dis >= 200:
        print("\nCongrats, you won")
        done = True
    print("\n\n")

print("\nGame finished")
