string=input("Enter string: ")
pos=1
count=0
for i in string:
    if i.isupper():
        count=count+1
        print(i,"found in ", pos," position")
    pos+=1
print("The number of uppercase characters is: ", count)
