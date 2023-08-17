import threading
m = threading.Lock()
dinero = 0

def deposit(n):
    m.acquire()
    global dinero
    dinero += n
    m.release()

def extract(n):
    m.acquire()
    global dinero
    dinero -= n
    m.release()

def add_profit():
    for i in range(10000):
        deposit(10)

def get_profit():
    for i in range(10000):
        extract(10)

client1 = threading.Thread(target=add_profit)
client2 = threading.Thread(target=get_profit)

client2.start()
client1.start()
print(dinero)
client1.join()
client2.join()



