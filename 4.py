mark_list = {'John' : 98, 'Smith' : 87, 'joy' : 96, 'mary': 67 , 'sam': 95}
sorted_keys = sorted(mark_list, key=mark_list.get, reverse=True)
print("top 3 students")
for student in sorted_keys[:3]:
    print(student, ": ", mark_list[student])
sum = 0
for student in mark_list:
    sum += mark_list[student]
print("average marks :", sum/len(mark_list))
