print("this is'make a wishlist'")
name = input("name,beatch?:")
wishlist = [] 






while True:
    print(f"menu:")
    print("1 - add a wish")
    print("2 - show all wish")
    print("3 - delete a wish")
    action = input(f" what do you want todo {name}? --->")
    if action == "1":
        wish = input (f"whats your wish, {name}? >>>")
        if wish not in wishlist:
            wishlist.append(wish)

    elif action =="2":
        for i, wish in enumerate(wishlist, start = 1):
            print(f"{i}.{wish}")
    elif action =="3":
        for i, wish in enumerate(wishlist, start = 1):
            print(f"{i}.{wish}")
        delete_index = input(f"{name}, enter the number of the wish to remove it|||||")
        delete_index = int(delete_index)
        if wish in wishlist:
            wishlist.remove(wish)



























        
    input("Press Enter to Continue or Write Anything you want idc tbh")
