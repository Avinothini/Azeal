b=""
a=0
print("DECIMAL    OCTAL \t\tCHARACTER")
for i in range(65533):
    try:
        a=i
        print("{:<10}{:<20}{:<10}".format(i,oct(i),chr(i)))
       
    except Exception:
        b+=" "+str(a)
        continue
print("\31")
