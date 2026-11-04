basic = float(input("Basic salary: "))
allowance = basic * 0.20
gross = basic + allowance
deduction = gross * 0.10
print("Net salary:", gross - deduction)
