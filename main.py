from caballo import CaballoConThread, CaballoThread

import time
import threading


def print_welcome():
  for i in range(5):
    time.sleep(0.4)
  print("Welcome")

def print_bye():
  for i in range(5):
    time.sleep(0.6)
  print("Bye")

time1 = threading.Thread(target=print_welcome)
time2 = threading.Thread(target=print_bye)

def main():
    caballo = CaballoConThread(limite=100)
    caballo.empezarCarrera()


if __name__ == "__main__":
    main()