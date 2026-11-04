marks = [int(input("Exam mark: "))
         for i in range(3)]
print("Average:", sum(marks) / 3)
for i in range(1, 3):
    if marks[i] > marks[i-1]:
     print("Improved")
    elif marks[i] < marks[i-1]:
      print("Declined")
    else:
     print("No change")
