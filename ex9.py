p = input("Password: ")
ok = len(p) >= 8 and any(c.isupper() for c in p) and any(c.islower() for c in p)
ok = ok and any(c.isdigit() for c in p) and any(not c.isalnum() for c in p)
print("Valid" if ok else "Invalid") 
