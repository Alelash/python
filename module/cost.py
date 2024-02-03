from constants import *
from order import *
def show_cost():
    global user_pizza, user_cost
    print(f"yu order these piza:")
    for number, pizza in enumerate(user_piza):
        print(f"{number+1}. {pizza} - {user_cost[number]}")

    print("your total is")
    summa = 0 
    for cost in user_cost:
        summa += cost
    print(summa)
    return summa