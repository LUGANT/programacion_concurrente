import threading
from caballo import CaballoThread

caballo1 = CaballoThread(limite=10,horse_number=1)
caballo2 = CaballoThread(limite=10,horse_number=2)
caballo3 = CaballoThread(limite=10,horse_number=3)
caballo4 = CaballoThread(limite=10,horse_number=4)
caballo5 = CaballoThread(limite=10,horse_number=5)

caballo1.start()
print()
caballo2.start()
print()
caballo3.start()
print()
caballo4.start()
print()
caballo5.start()
print()

caballo1.join()
caballo2.join()
caballo3.join()
caballo4.join()
caballo5.join()