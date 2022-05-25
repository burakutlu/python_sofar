import datetime
import payment


class MenuItem:
    def __init__(self, name):
        self.name = name
        self.price = float(input("Enter the item's price: "))
        self.water = int(input("Enter the required water amount: "))
        self.milk = int(input("Enter the required milk amount: "))
        self.coffee = int(input("Enter the required coffee amount: "))

    def __repr__(self):
        return f"{self.name}, {self.price}$, Required: {self.water}ml water, {self.milk}ml milk and {self.coffee}g " \
               f"coffee.\n"


class Coffee:
    def __init__(self):
        self.water = 5000  # ml
        self.milk = 5000
        self.coffee = 2500  # g
        self.order_no = 0
        self.log = open("log.txt", "a")

    def __repr__(self):
        return f"Water: {self.water}ml, Milk: {self.milk}ml, Coffee: {self.coffee}g\n"

    def list(self, item_list):
        for item in item_list:
            print(f"{item.name}, {item.price}$\n")

    def order(self, item):
        if payment.payment(item.price):
            self.order_no += 1
            self.log.write(f"Order {self.order_no}: {item.name}, {datetime.datetime.now()}")
            print(f"Enjoy your {item.name}!")
        else:
            print("Transaction failed.")

    def add_resource(self, water_amount, milk_amount, coffee_amount):
        if water_amount and milk_amount and coffee_amount > 0:
            self.water += water_amount
            self.milk += milk_amount
            self.coffee += coffee_amount
        else:
            print("Invalid input.")
