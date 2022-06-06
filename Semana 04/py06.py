# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with If, Else and Elif Statements

# Comparisons
# Equal: ==
# Not equal: !=
# Greater than: >
# Less than: <
# Greater or Equal: >=
# Less or Equal: <=
# Object Identify: is

# Booleans:
# and
# not
# or


language = 'Java'

if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print('Language is java')
else:
    print('No match')

user = 'Admin'
logged_in = True

# Lógica E/AND

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Lógica OU/OR
if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Lógica NOT
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1,2,3]
b = [1,2,3]

print(a == b) #verifica valores
print(a is b) #pega ID da memoria
print(id(a))
print(id(b))

# False Values:
#     False
#     None
#     Zero of any numeric type
#     Any empty sequence. For example, '',(),[]
#     Any empty mapping. For example, {}

condition = 'Teste'

if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')


