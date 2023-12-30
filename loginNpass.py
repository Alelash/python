def sign_up():
    login=input("make an logimn:")
    passwordmake = input("make an passwormd:")
    passwordtoremember=input("please input it again to make sure youe didnt forget it:")
    if passwordmake == passwordtoremember:
         write_to_file("logins.txt", login+"\n")
         write_to_file("passswords.txt", passwordmake+"\n")
         print(f"the user {login} has been registered into the chinese market now everyone nows where yu ive")
    else:
         print("the passwords dont match now i kill you")

def write_to_file(filename, text):
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)




while True:
        print("this is an OS called BobyerKorrpp, these are the options of this os;")
        print("1 - sign up")
        print("2 - exit the program(aka explode the computer or laptop because i planted 250 thousand kilos of dynomite into it and will destroy half of yo country)")
        action = input("choose. :")
        if action == "1":
            sign_up()
        if action == "2":
            print("ambatubelow *fucking evaporates your entire country*")
            break
        input("please press enter to continue")