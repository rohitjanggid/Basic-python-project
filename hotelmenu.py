def hotelmenu():
    menu = {
        "pizza":150,
        "pasta":80,
        "tea":20,
        "salad":50,
        "coffee":60,
        "momos":60,
    }

    print("Welcome to our restaurant")
    print("Here is the menu")
    for item, price in menu.items():
        print(f"{item.capitalize()}:{price}INR")

    order_total = 0
    
    while True:
        item = input("Enter the name of the item you want to order:").lower()
        if item in menu:
            try:
                quantity = int(input(f"how many {item}s you want to order ?"))
                item_cost = menu[item] * quantity
                order_total += item_cost
                print(f"{quantity} x {item} added. subtatal : {item_cost} INR")
            except ValueError:
                print("please enter a vaild number for quantity")
        else:
            print(f"Sorry, '{item}' is not available.")

        another = input("Do you want to add another item? (yes/no):").strip().lower()
        if another != "yes":
            break
    
    print(f"\nYour total amount to pay is {order_total} INR.")

hotelmenu()
    