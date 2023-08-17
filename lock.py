import threading

m = threading.Lock()

m.acquire() 

#seccion critica

m.release()