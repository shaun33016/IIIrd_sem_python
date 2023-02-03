string=input("Enter string: ")
vow=0
for i in string:
    if(i=='a' or i=='A' or i=='e' or i=='E' or i=='i' or i=='I' or i=='o' or i=='O' or i=='u' or i=='U'):
        vow+=1
print("Number of vowels in string is ", vow)        
