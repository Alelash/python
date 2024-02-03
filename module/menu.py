from constants import *
from order import  *



def choice_pizza():
    print('hi welcome to pizzadreamthingidk chooose pizza or die')
    print('pizzariea pizza choice:') 
    for i, pizza in enumerate(PIZZA):
        print(f"{i+1}.{pizza} - {COST[i]} shmackaroonies")
    while True:      
        order = int(input('choose: ')) - 1
        get_order(order_pizza=order)

        print("added into ca- zzzzzzzzzzzzzz")
        flag = input("any more 'izzaas??")
        if flag.upper() == 'FUCK YOU':
            print("ok :(")
            break
        