grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_value = []
sorted_students = sorted(students)

for i in grades:
    average_ = sum(i) / len(i)
    average_value.append(average_)

average_grades = zip(students,average_value)
print(dict(average_grades))
