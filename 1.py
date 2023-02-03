def sal():
    name=input("Enter employee name: ")
    hours=int(input("Enter the number of hours worked in a week: "))
    weeks=int(input("Enter the number of weeks worked in a month: "))
    payrate=int(input("Enter payrate per hour: "))
    month_pay=hours*weeks*payrate
    print("Name of employee: ", name)
    print("Hours worked in a week: ", hours)
    print("Weeks worked in a month: ", weeks)
    print("Payrate per hour: ", payrate)
    print("Monthly pay is: ", month_pay)
sal()
