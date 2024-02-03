from cost import *
import random

def pay():
    money=random.choice(["ja", "nu-uh"])
    if money == "ja":
        print("you decide to pay... and you do it succesfully! you even manage to do something... wel... you know.")
    else:
        print("you decide to pay, but you forogot your wallet. result? .... you have been thrown out for being poor")