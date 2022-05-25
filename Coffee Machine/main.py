import coffee

coffee_machine = coffee.Coffee()


def add_item(listItems):
    name_input = input("Enter the item's name: ").capitalize()
    x = coffee.MenuItem(name_input)
    listItems.append(x.name)


if __name__ == "__main__":
    item_list = []
    isRunning = True
    while isRunning:
        usr_input = input("Commands (add, item status, machine status, buy): ")
        if usr_input == "add":
            add_item(item_list)
        elif usr_input == "item status":
            for item in item_list:
                print(item)
        elif usr_input == "machine status":
            print(coffee_machine)
        elif usr_input == "buy":
            if len(item_list) > 0:
                coffee_machine.list(item_list)
                item = input("Enter the name of the item: ").capitalize()
                coffee_machine.order(item_list[item])
            else:
                print("There are no items to order.")
