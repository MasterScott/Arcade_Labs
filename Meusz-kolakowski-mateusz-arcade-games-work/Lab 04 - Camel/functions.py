import random


def get_started():
    print("Welcome to Camel")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")


def menu():
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")


def status(player_dist, drinks_canteen, natives_dist):
    print("Miles traveled : %d" % player_dist)
    print("Drinks in canteen: %d" % drinks_canteen)
    print("The natives are %d miles behind you" % (player_dist - natives_dist) )


def oasis_found(drinks_in_canteen):
    if random.randint(1,20) == 1:
        print("You found an oasis, the canteen drinks will be refilled")
        return 3 - drinks_in_canteen
    else:
        return 0
