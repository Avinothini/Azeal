i=int(input("enter a number:"))
for a in range(i):
 for b in range(a,i):
  print(" ",end='')
 for c in range(a):
  print(" *",end='')
 print()   
for a in range(i):
 for b in range(a):
  print(" ",end='')
 for c in range(a,i):
  print(" *",end='')
 print()
  
