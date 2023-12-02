import random
inventory = []










def gaw():
    print("woofwoofwoofpashelnaherwoof!")



def robot_forward():
    print("robot goes fprward yes")
def robot_backward():
    print("robot goes back no ")
def robot_left():
    print("robot goes left eh ")
def robot_right():
    print("robot goes right ofc ")


def check_ineventory():
    for index, item in enumerate(inventory, start=1):
        print(F"{index}. {item}")





def craft():
    recept1 = ["rust", "knife"]#sharp rust
    recept2 = ["sharp rust", "tape", "wood"]#rusty spear
    recept3 = ["bag", 'bag', "iron bar"]#makeshift iron armor
    recept4 = ['makeshift iron armor', 'sharp rust', 'tape']#spiky makeshirt iron armor
    recept5 = ['broken cup', 'PIPE' 'low end explosive filling', 'gundpowder','cable']#pipebomb
    recept6 = ['broken cup', 'tape']#shiv
    recepts = [recept1, recept2, recept3, recept4, recept5, recept6]
    recept_names = ["sharp rust", 'rusty spear', 'makeshift iron armor', 'spiky makeshift iron armor', 'pipebomb', 'shiv']
    for index, recept in enumerate(recept_names, start=1):
        print(f"{index}. {recept}")
    choice = input("what to craft. ")
    if not choice.isdigit():
        print("only number mazafaka")
        return None
    choice = int(choice) - 1
    if choice not in range(0, len(recept_names)):
        print("wrong number mazafak")
        return None
    choice_recept = recept_names[choice]
    print(f"you chose to craft {choice_recept}")
    ingredients = recept[choice]
    print(f"items to craft with: {ingredients}")
    for item in inventory:
        if item in ingredients:
            print(F'destroyed {item}')
            inventory.remove(item)
            ingredients.remove(item)
    if not ingredients:
        inventory.append(choice_recept)
        print(f"added {choice_recept} IN INVENTORY YOU BI-")






def robot_scan():
    items = ["bottle", "stick", "bag", "rust", "wood(lame)", "broken cup", "knife","tape", "cable", "iron bar", 'seeds', 'hose','PIPE','unknown','red paint' 'low end explosive filling', "gunpowder"]
    item = random.choice(items)
    print(f"found: {item}")
    return item

def robot_pickup(item):
    global inventory
    inventory.append(item)

while True:
    key =input("enter key (wasd), or f to try find an item, e to look at your inventory.                      ")
    if key == "w":
        robot_forward()
    elif key == "a":
        robot_left()
    elif key == "s":
        robot_backward()
    elif key == "d":
        robot_right()
    elif key == "f":
        item  = robot_scan()
        robot_pickup(item)
    elif key == "e":
        print(inventory)
    elif key == 'c':
        craft()
