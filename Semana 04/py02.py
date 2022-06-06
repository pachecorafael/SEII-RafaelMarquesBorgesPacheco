# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with the Textual Data
print('Hello World')

message = 'Hello World'
print(message)

message_PT = 'Olá mundo'
print(message_PT)

mes = "Bobbys's World"
print(mes)

print(len(message))
print(message[0])
print(message[0:5])
print(message[6:])

print(message.lower())
print(message.upper())
print(message.count('l'))
print(message.find('World'))

message_U = message.replace('World','Universe')
print(message_U)

greeting = 'Hello'
name = 'Rafael'

mes1 = greeting + ', ' + name + '. Welcome!'
print(mes1)

mes2 = '{}, {}. Welcome!'.format(greeting,name)
print(mes2)

mes3 = f'{greeting}, {name.upper()}. Welcome!'
print(mes3)

print(dir(name))
print(help(str))


