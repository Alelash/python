import random 
print ("это игра угадай число")
print ("я загадаю число от 1-100000000 а ты угадай какое это число (удачи)")
attempts=10
numbwer_comp = random.randint(1, 100000000)
while attempts > 0:
    user_numbwer = int (input ("nomer pozhaluysta:") )
    print(f"ввёл {user_numbwer}")
    if user_numbwer == numbwer_comp:
        print ("да!!!")
    elif user_numbwer < numbwer_comp:
        print ("больше!")
    elif user_numbwer > numbwer_comp:
        print ("меньше!")