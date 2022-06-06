# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Lists, Tuples and Sets
# Lists are mutable and tuples are not

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Chemistry' , 'Education']
courses.append('Art')
courses.insert(0, courses_2)
courses.extend((courses_2))

courses.remove('Math')
popped = courses.pop()
print(popped)

courses.reverse()

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses.index('CompSci'))
print('Math' in courses)

for index, course in enumerate(courses, start=1):
    print(index, course)

#course_str = ', '.join(courses)
#print(course_str)


#courses.sort()
#sorted_courses = sorted(courses)
#print(sorted_courses)

nums = [1, 5, 2, 3, 4]
#nums.sort(reverse=True)
print(nums)
sorted_nums = sorted(nums)
print(sorted_nums)
print(min(nums))
print(max(nums))
print(sum(nums))

#Mutable
print('/////// Listas Mutaveis ///////')
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

#Immutable
print('/////// Tuplas Imutaveis ///////')
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

#tuple_1[0] = 'Art'

#Sets
print('/////// Sets ///////')
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)
print('Math' in cs_courses)

art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


