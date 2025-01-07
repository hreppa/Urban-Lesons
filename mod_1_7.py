"""отсортировать список струдентов, создать библиотеку
 и присвоить в качестве значения средний бал"""

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_sort = sorted(students)

print()

students_grades = {}

for unit in range(len(students)):
    print(f'{students_sort[unit]: <10}: {grades[unit]}')
    each_elem = grades[unit]
    students_grades[students_sort[unit]] = (sum(each_elem)/len(each_elem))

print()
print(students_grades)
