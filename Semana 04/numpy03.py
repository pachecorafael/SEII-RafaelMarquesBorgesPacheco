# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with numpy () - Indexing and Slicing (1 Dimension)
import numpy as np
import matplotlib.pyplot as plt

#Seção 1
# a1 = np.array([3,5,7])
# print(a1)
# a2 = np.zeros(10)
# print(a2)
# a3 = np.ones(10)
# print(a3)
# a4 = np.random.random(10)
# print(a4)
# a5 = np.random.randn(10) #normal distribution
# print(a5)
# a6 = np.linspace(0, 10, 100) #vai de zero a 10, 100 numeros igualmente espaçados
# print(a6)
# a7 = np.arange(0, 10, 0.02)
# print(a7)

#Seção 2
# A8 = 2*a1
# A9 = 1/a1 + 2
# A10 = a1>4 #False or true

# x = np.linspace(0,10,100)
# y = x**2
# plt.plot(x,y)

# plt.hist(a4)

# def f(x):
#     return x**2 * np.sin(x)/np.exp(-x)
#
# y2 = f(x)
# plt.plot(x,y2)

#Seção 3
a1 = np.array([2,4,6,8,10])
print(a1[2])
print(a1[2:])
print(a1[:-2])
print(a1[1:-2])
print(a1[a1>3])

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])
print(names)
first_letter_J = np.vectorize(lambda s: s[0])(names)=='J'
# lambda s: s[0] Pega s e retorna seu primeito elemento
'''Give me a string and I'll give you the first character of the string'''
# vectorize -> cria um loop for e vai em todos os elementos
# de 'names' sequencialmente aplicando a função lambda

print(first_letter_J)
teste = names[first_letter_J]
print(teste)


# plt.grid(True)
# plt.show()