import random 
print ("это игра угадай число")
print ("я загадаю число от 1-100 а ты угадай какое это число")
name = input("Whats your name, pardner?")
gamer_round_wombocombo = 0
while gamer_round_wombocombo < 3:
    gamer_round_wombocombo+=1
    print(f"raund nomer {gamer_round_wombocombo}")
    attempts=10
    numbwer_comp = random.randint(1, 100)
    while attempts > 0:
        print(f"{name},ya got youself an {attempts} amount of tries, pardner.")
        user_numbwer = input ("nomer pozhaluysta:") 
        if not user_numbwer.isdigit():
            print(f"{name}, это не число, дурaшенька ;)")
            continue
        attempts -= 1
        print(f"ввёл {user_numbwer}")
        user_numbwer = int(user_numbwer)
        if user_numbwer == numbwer_comp:
            print (f"молодец,{name}, ты угадал, молорик.")
        elif user_numbwer < numbwer_comp:
            print (f"больше, {name}")
        elif user_numbwer > numbwer_comp:
            print (f"меньше, {name}.")
        if attempts == 10:
            print("vse, кончились попыткас, вот уж такс")
            break
