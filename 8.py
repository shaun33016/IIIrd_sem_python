s1=input("Enter first string: ")
s2=input("Enter second string: ")
string=s1+s2
caps=" "
for i in string:
    if i.isupper():
        caps+=i
print(caps)
