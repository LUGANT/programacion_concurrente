import curses
from threading import Thread, Event
from caballo import CaballoThread

def start_threads(thread_list:list[Thread]):
    for thread in thread_list:
        thread.start()    

def join_threads(thread_list:list[Thread]):
    for thread in thread_list:
        thread.join()    

num_caballos = int(input("Ingrese la cantidad de caballos a participar: "))

referee = Event()
meta = 10
caballos: list[Thread] = []

for i in range(num_caballos):
    caballos.append(CaballoThread(limite=meta, horse_number=i+1, referee=referee))

start_threads(caballos)

join_threads(caballos)