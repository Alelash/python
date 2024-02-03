from menu import choice_pizza
# from order import show_order
from cost import show_cost
from pay import pay
# from check import give_check
import time
def start():
    choice_pizza()
    time.sleep(10)
    show_cost()
    time.sleep(12)
    pay()


start()