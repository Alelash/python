salary = 6900
veggies_sale = 0.7 #70%
kukumber = 90
TomaT = 150
LeBerry = 385 # не надо вващщещее
COOKIS = 140 + 140
# Умножение на скидку - это овощи со скидкой
buy = (kukumber * 5 + TomaT * 4) * veggies_sale + COOKIS#лепокупка
print(F"У таксиста ванэ из {salary} долларов после траты {buy} долларв осталось {salary - buy} доллров")
print(10 // 3)#целочисленное деление
print(10 % 3)#остаток оооот деления
left = salary - buy
stonks = 134.65
proezd = 36
print(f"Таксист ваня сможет купить {left // stonks} акций")
print(f"у таксиста будет {int(left % stonks)} рублей, проезд  {proezd} рублей")

numero = int(input("ЧИСЛО ПАЖАЛУСТА:"))
onenumber = numero // 100
twonumber = numero // 10 % 10
threenumber = numero % 10
print(onenumber + twonumber + threenumber)
