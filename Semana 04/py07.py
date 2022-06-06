# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Working with Loops and Iterations - For/While

nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found')
        continue #break
    print(num)

# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

for i in range(1, 11):
    print(i)

x = 0

while x <= 10: #Control C para sair de um loop infinito
    if x == 5:
        break
    print(x)
    x += 1