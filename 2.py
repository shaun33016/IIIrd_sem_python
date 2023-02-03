emp=input("Enter employee name: ")
idn=int(input("Enter employee id: "))
bs=int(input("Enter basic salary: "))
al=int(input("Enter allowance: "))
gs=bs+al
if gs>20001:
    tax=gs*(30/100)
elif gs>10001 and gs<20000:
    tax=gs*(20/100)
elif gs>5001 and gs<10000:
    tax=gs*(10/100)
else:
    tax=0
net=gs-tax
print("Employe name: ", emp)
print("Employe id: ", idn)
print("Basic Salary: ", bs)
print("Allowance: ", al)
print("Gross pay: ", gs)
print("Tax to be paid: ", tax)
print("Net pay: ", net)
