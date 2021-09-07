import grades # Imports grades module

students = []

# Creates student01 object as an instance of class Student
student01 = grades.Student('Michael',80,70,70,True)
print('id(student01):',id(student01))
students.append(student01)

# Creates student02 object as an instance of class Student
student02 = grades.Student('Angela',60,65,75,True)
print('id(student02):',id(student02))
students.append(student02)

# Creates student03 object as an instance of class Student
student03 = grades.Student('Natalie',60,65,75,False)
print('id(student03):',id(student03))
students.append(student03)

# Print the names and marks for each of the students
print('\nStudents:\n')
# Loop through student objects' attributes
for student in students:
    print('---')
    print(f"Name: { student.name }")
    print(f"English: { student.english_mark }")
    print(f"Science: { student.science_mark }")
    print(f"Mathematics: { student.mathematics_mark }")
    print(f"Average marks: { student.ave_marks() }")
    if student.completed_assessments:
        print("Completed assessments: Yes")
    else:
        print("Completed assessments: No")
    print('---\n')