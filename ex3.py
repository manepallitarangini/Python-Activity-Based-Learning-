km = float(input("Distance in km: "))
age = int(input("Age: "))
fare = km * 2
if age >= 60:
 fare = fare * 0.8
print("Final fare:", fare + 30)
