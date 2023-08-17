from collections.abc import Callable, Iterable, Mapping
from threading import Thread
from typing import Any
import time
import random

class CaballoThread(Thread):

    def __init__(
                ## constructor heredado
                self, group: None = None, 
                target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., 
                kwargs: Mapping[str, Any] | None = None, *,
                daemon: bool | None = None,
                ## constructor nuevo
                limite: int,
                horse_number: int
                ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.limite = limite
        self.horse_number = horse_number
        self.position: int = 0

    def run(self) -> None:
        
        print("Caballo: ",end=" ")

        for i in range(self.limite):
            
            self.position += 1
            print(f"{self.horse_number}", end="",flush=True)
            time.sleep(random.randint(0,10))
        
        print(f"\nEl caballo {self.horse_number} llego a la meta")
        return super().run()

class PosicionThread(Thread):

    def __init__(self, 
                 group: None = None, 
                 target: Callable[..., object] | None = None, 
                 name: str | None = None, 
                 args: Iterable[Any] = ..., 
                 kwargs: Mapping[str, Any] | None = None, *, 
                 daemon: bool | None = None) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

class CaballoConThread():

    position: int = 0
    __thr_correr: Thread = None
    __thr_checkear: Thread = None

    def __init__(self, limite: int) -> None:
        self.limite = limite

    def empezarCarrera(self) -> None:
        self.__inicializar_threads()
        self.__terminar_threads()
        
    
    def __inicializar_threads(self):
        self.__thr_correr = Thread(target=self.__avanzar())
        self.__thr_correr.start()

    def __terminar_threads(self):
        self.__thr_correr.join()
        self.__thr_checkear.join()

    ## thread correr
    def __avanzar(self):
        self.__thr_checkear = Thread(target=self.__llegueALaMeta())
        self.__thr_checkear.start()
        
        self.position += 1
        
    ## thread checkear
    def __llegueALaMeta(self):
        while True:
            print(self.position, end="")
            if(self.position == self.limite):
                print("termine!")
                break