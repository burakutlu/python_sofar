def payment(item_price):
    payment_type = input("Credit card or cash?: ")
    if payment_type == "credit card":
        if input(f"Payment amount is {item_price}$, do you allow it? y, n: ") == "y":
            return True
        else:
            return False
    else:
        if input(f"Will you pay {item_price}$ in cash? y, n: ") == "y":
            return True
        else:
            return False

