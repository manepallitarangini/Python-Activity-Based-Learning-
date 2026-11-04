balance = 5000
amount = float(input("Withdraw amount: "))
if 0 < amount <= balance:
 balance = balance - amount
 print("Balance:", balance)
else:
 print("Invalid amount or insufficient balance")
