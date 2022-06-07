# Rafael Pacheco - Sistemas Embarcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with matplotlib (Seções 1 a 6)
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]

plt.scatter(x,y) #x/y

x1 = np.arange(0,1000,1)
# print(x1)
plt.plot(x1, x1**2)

plt.show()