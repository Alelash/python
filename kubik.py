import random
def betting(shmackaroonies):
    print(f"you currently have {shmackaroonies}. the rules are simple. you choose from 1-6 and win or loose. if you win you get x2 the money. if you dont... you know what happens")
    TheBet = input("input how much shmackaroonies you want to bet:")
    TheBet = int(TheBet)
    if TheBet > shmackaroonies or TheBet <= 0:
        print("")
        return None
    Choice = input("choose1-6:")
    Choice = int(Choice)
    if Choice > 6 or Choice <= 0:
        print("wrong number")
        return None
    
    if kubik == Choice:
        print(f"congrats! you got x2 {TheBet}")

        return shmackaroonies + TheBet
    else:
        print("you didnt get the number right.")
        return shmackaroonies - TheBet
        
        












kubik = random.randint(1,6)
name = input ("Hello, hello my dear player! welcome to 'Kubik'! in here you bet for the right number with your REAL money!!!!@!@!@ and yes you currently have 1000 shmackaroonies. please tell me your name, dear player:")

shmackaroonies = 1000
shmackaroonies = int(shmackaroonies)
bankrupt = False
while shmackaroonies >= 0:
    if not bankrupt: 
        print("alright,welcome to the game.please choose what you would like to do")
        print("1 - Bet for the dice")
        print("2 - exit the game")
        print("3 - go outside and ask for shmackaroonies")
        action = input("choose. :")
        shmackaroonies = betting(shmackaroonies)

