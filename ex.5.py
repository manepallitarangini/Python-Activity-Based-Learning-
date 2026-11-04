= int(input("Subject 1 marks: "))
b = int(input("Subject 2 marks: "))
c = int(input("Subject 3 marks: "))
total = a + b + c
print("Total:", total)
print("Pass" if min(a,b,c) >= 35 else "Fail") 
