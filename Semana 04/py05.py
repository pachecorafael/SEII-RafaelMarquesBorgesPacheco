# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with Key-value pairs

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])

#student['phone'] = '555-5555'
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student.get('phone', 'Not Found'))
#del student['age']
#age = student.pop('age')
#print(age)
print(student)
print(student.keys())
print(student.values())
print(student.items())
for keys,value in student.items():
    print(keys, value)