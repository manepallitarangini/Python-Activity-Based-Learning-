attended = int(input("Classes attended: "))
total = int(input("Total classes: "))
percentage = attended / total * 100
print("Attendance:", percentage, "%")
print("Eligible" if percentage >= 75 else "Not eligible")
