import math
a=int(input("Enter the coefficient of x^2: "))
b=int(input("Enter the coefficient of x: "))
c=int(input("Enter the coefficient of constant: "))
if a*b*c==0:
    print("No roots.")
    exit(0)
d=(b*b)-(4*a*c)
if d==0:
    printf("Equal and real roots")
    x1=x2=-b/(2*a)
    print("Roots are: ",x1, x2)
elif d>0:
    print("Real and distinct roots")
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print("Roots are: ",x1, x2)
else:
    print("Imaginary roots")
    x1=-b/(2*a)
    x2=math.sqrt(math.sqrt(math.fabs(d)))/(2*a)
    print("Roots are: ",x1,"+i",x2," and ",x1,"-i",x2)
