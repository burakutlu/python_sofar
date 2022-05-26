import coffee

coffee_machine = coffee.Coffee()


def add_item(listItems):
    name_input = input("Enter the item's name: ").capitalize()
    new_item = coffee.MenuItem(name_input)
    listItems.append(new_item)


if __name__ == "__main__":
    item_list = []
    isRunning = True
    while isRunning:
        usr_input = input("Commands (add, item status, machine status, buy): ")
        if usr_input == "add":
            add_item(item_list)
        elif usr_input == "machine status":
            print(coffee_machine)
        elif usr_input == "buy":
            if len(item_list) > 0:
                coffee_machine.list(item_list)
                item = eval(input("Enter the name of the item: ").capitalize())
                print(type(item))
            else:
                print("There are no items to order.")
