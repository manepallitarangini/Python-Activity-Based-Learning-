price = 30
stock = 20
qty = int(input("Idli quantity: "))
if 0 < qty <= stock:
    print("Bill:", price * qty)
    stock = stock - qty
    print("Remaining stock:", stock)
else:
    print("Invalid quantity or insufficient stock")
