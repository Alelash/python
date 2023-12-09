def plus(a,b):
    return a+b
def umnozhsnie(a,b):
    return a*b
def minus(a,b):
    return a-b
def deleniye(a,b):
    return a/b

def input_num(input_phrase):
    x=input(input_phrase)
    if not x.isdigit():
        print("notnumber")
        return input_num(input_phrase)
    return int(x)











n1 = input("number 1:")
n1 = int(n1)
n2= input("number 2:")
n2 = int(n2)
umnozheniye = n2 * n1
deleniye = n1 / n2
plus = n1 + n2
minus = n1 - n1
print (F"умножение = {umnozheniye}, деление = {deleniye}, плюс = {plus} минус = {minus}")