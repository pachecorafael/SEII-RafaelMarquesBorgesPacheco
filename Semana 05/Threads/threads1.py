# Rafael Pacheco - Sistemas Embarcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 12/06/2022 - Semestre 2021-2

#Working with Threding Module

#import threading
import concurrent.futures
import time

#Uso manual de threads
#


# start = time.perf_counter()
#
# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...') #f string pra imprimir uma variavel
#     time.sleep(seconds)
#     print('Done Sleeping...')
#
# # #Criação da primeira thread
# # t1 = threading.Thread(target=do_something) #nao colocar () pq nao queremos executar a função
# # t2 = threading.Thread(target=do_something)
# #
# # #Threads devem ser iniciadas
# # t1.start()
# # t2.start()
# #
# # #Garante que as threads sejam completadas antes de seguir o resto do script
# # t1.join()
# # t2.join()
#
# #Lista de threads
# threads = []
# for _ in range(10): #_ -> nao precisa da variavel i
#     t = threading.Thread(target=do_something, args=[1.5])
#     t.start()
#     threads.append(t)
#
# for thread in threads:
#     thread.join()
#
# finish = time.perf_counter()
#
# print(f'Finished in {round(finish-start, 2)} second(s)')

start = time.perf_counter()

def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...') #f string pra imprimir uma variavel
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

with concurrent.futures.ThreadPoolExecutor() as executor:
    # f1 = executor.submit(do_something,1)
    # f2 = executor.submit(do_something, 1)
    secs = [5,4,3,2,1]
    results = executor.map(do_something, secs) #função map vai rodar a funça do something com todos os valores da lista

    # for result in results:
    #     print(result) #para printar os resultados quando todos acabarem, printando na ordem que comecou


    # results = [executor.submit(do_something,sec) for sec in secs] #pesquisar sobre!
    #
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())
    # print(f1.result())
    # print(f2.result())

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
