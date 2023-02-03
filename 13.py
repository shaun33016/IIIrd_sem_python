file_name=input("Enter filename: ")
with open(file_name,'r') as file:
    total = 0
    for line in file:
        marks = line.split()
        print(marks)
        for mark in range(0,len(marks)):
            total = total + int(marks[mark])
            Average = total / len(marks)
        print("total marks = ", total,"Average marks=%.3f " %Average)

