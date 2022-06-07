# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 06/06/2022 - Semestre 2021-2

# Use Underlying Operating System Functionalit

import os
from datetime import datetime

os.chdir('C:/Users/rafam/Desktop/SEII-RafaelMarquesBorgesPacheco/') # change directory

print((os.getcwd())) #get currently directory
# os.removedirs('OS-DEMO-2/SubDir1')

# os.mkdir('OS-DEMO-1')
os.makedirs('OS-DEMO-2/SubDir1')

# os.rmdir('OS-DEMO-1')
os.removedirs('OS-DEMO-2/SubDir1')

# os.rename('OS-DEMO-1', 'OS-DEMO-121')
mod_time = os.stat('OS-DEMO-121').st_mtime #mt = modifided time
print(datetime.fromtimestamp(mod_time))
# print(os.stat('OS-DEMO-121')) #.parametro

# for dirpath, dirnames, filenames in os.walk('C:/Users/rafam/Desktop/SEII-RafaelMarquesBorgesPacheco/'):
#     print('Current Path:', dirpath)
#     print('Directiories', dirnames)
#     print('Files:', filenames)
#     print()

print(os.environ.get('C:'))

# print(os.listdir())


