# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with Import Modules and Exploring the standart library
import sys
sys.path.append('Users\\rafam\\Desktop\\SEII-RafaelMarquesBorgesPacheco\\Semana04')

from py09_mymodule import find_index, test #*


courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print(sys.path)