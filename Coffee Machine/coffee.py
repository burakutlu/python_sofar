import datetime
import payment


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
            print(f'Item: {item}, price: ${item_list[item]["price"]}')

    def order(self, item_list, item):
        if payment.payment(item_list[item]["price"]):
            self.order_no += 1
            self.log.write(f'Order {self.order_no}: {item}, ${item_list[item]["price"]},'
                           f' transaction time: {datetime.datetime.now()}\n')
            print(f"Enjoy your {item}!")
            self.log.flush()
            self.water -= item_list[item]["water"]
            self.milk -= item_list[item]["milk"]
            self.coffee -= item_list[item]["coffee"]
        else:
            print("Transaction failed.")

    def add_resource(self, water_amount, milk_amount, coffee_amount):
        if water_amount > 0 and milk_amount > 0 and coffee_amount > 0:
            self.water += water_amount
            self.milk += milk_amount
            self.coffee += coffee_amount
        else:
            print("Invalid input.")

    def quit(self):
        self.log.close()
