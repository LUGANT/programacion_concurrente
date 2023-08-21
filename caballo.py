from collections.abc import Callable, Iterable, Mapping
from threading import Thread
import threading
from typing import Any
import time
import random
import curses

class CaballoThread(Thread):

    def __init__(
                ## constructor heredado
                self, group: None = None, 
                target: Callable[..., object] | None = None, name: str | None = None, args: Iterable[Any] = ..., 
                kwargs: Mapping[str, Any] | None = None, *,
                daemon: bool | None = None,
                
                ## constructor nuevo
                limite: int,
                horse_number: int,
                referee: threading.Event, #event
                
                #
                #sm: curses.window

                ) -> None:
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.limite = limite
        self.horse_number = horse_number
        self.referee = referee
        self.position: int = 0
        #self.sm = sm

    def terminarCarrera(self):
        self.referee.set()

    def esGanador(self):
        return self.position < self.limite

    def laCarreraTermino(self):
        return self.referee.is_set()

    def run(self) -> None:
        while self.esGanador():
            
            time.sleep(random.randint(0,3))
            self.position += 1

            if self.laCarreraTermino():
                break

            print("-" * (self.limite + 11) + "|")
            print(f"Caballo {self.horse_number}: {'.' * self.position}🐎 ")
            print("-" * (self.limite + 11) + "|")

            if self.position >= self.limite:
                self.terminarCarrera()
                print(f"¡Caballo {self.horse_number} es el ganador!")
                break

        return super().run()