import coffee

coffee_machine = coffee.Coffee()


def add_item(menu):
    name_input = input("Enter the item's name: ").capitalize()
    price = float(input("Enter the item's price: $"))
    water_amt = int(input("Enter the required water amount: "))
    milk_amt = int(input("Enter the required milk amount: "))
    coffee_amt = int(input("Enter the required coffee amount: "))
    menu.update({name_input: {"price": price, "water": water_amt, "milk": milk_amt, "coffee": coffee_amt}})


if __name__ == "__main__":
    isRunning = True
    MenuList = {}
    while isRunning:
        usr_input = input("Commands (add, resource, machine status, buy or exit): ")
        if usr_input == "add":
            add_item(MenuList)
        elif usr_input == "machine status":
            print(coffee_machine)
        elif usr_input == "buy":
            if len(MenuList) > 0:
                coffee_machine.list(MenuList)
                cf_input = input("Enter your order: ").capitalize()
                coffee_machine.order(MenuList, cf_input)
            else:
                print("There are no items to order.")
        elif usr_input == "resource":
            water_amount = int(input("Enter the required water amount: "))
            milk_amount = int(input("Enter the required milk amount: "))
            coffee_amount = int(input("Enter the required coffee amount: "))
            coffee_machine.add_resource(water_amount, milk_amount, coffee_amount)
        elif usr_input == "exit":
            coffee_machine.quit()
            isRunning = False
        else:
            print("Invalid command.")
