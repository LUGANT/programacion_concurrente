import threading

n = 0
flag = False

def p():
    global n
    while not flag:
        print(n)
        n-=1

def q():
    global n
    while n == 0:
        # print(n)
        pass
    flag=True

p1 = threading.Thread(target=p)
q1 = threading.Thread(target=q)

p1.start()
q1.start()

p1.join()
q1.join()