price = float(input("Price: "))
qty = int(input("Quantity: "))
total = price * qty
if total >= 1000: total = total * 0.90
print("Final bill:", total)
