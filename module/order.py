from constants import *

user_piza = []
user_cost= []

def get_order(order_pizza):
    global user_piza,user_cost
    user_piza.append(PIZZA[order_pizza])
    user_cost.append(COST[order_pizza])