# file = open("text.txt", mode="r", encoding="utf-8")
# file.write("christmas! just a week away!\n")
# file.close()
with open("text.txt", mode="r", encoding="utf-8") as file:
   text =  file.readline("")
   print(text)