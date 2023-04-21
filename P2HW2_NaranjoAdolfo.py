#CTI-110
#P2HW2 - List
#Adolfo Naranjo
#04-21-2023

grade_module1 = float(input('Enter grade for Module 1: '))
grade_module2 = float(input('Enter grade for Module 2: '))
grade_module3 = float(input('Enter grade for Module 3: '))
grade_module4 = float(input('Enter grade for Module 4: '))
grade_module5 = float(input('Enter grade for Module 5: '))
grade_module6 = float(input('Enter grade for Module 6: '))

grades = [65.5, 88, 78.5, 90, 61, 92]
average_grade = sum(grades) / len(grades)



print('------------Results-----------')
print(f'Lowest Grade: {min(grades)}')
print(f'Highest Grade: {max(grades)}')
print(f'Sum of Grades: {sum(grades)}')
print(f'Average Grade: {average_grade}')     

