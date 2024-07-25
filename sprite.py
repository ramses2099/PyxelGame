import pyxel
from abc import abstractmethod
from typing import Optional

class Sprite:
    def __init__(self, x: float, y: float, img: int , u: float,  v: float,  w: float,  h: float,
    colkey: Optional[int] = None) -> None:
        self.x = x
        self.y = y
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey
    
    @abstractmethod    
    def update(self, dt: int) -> None:
        pass
    
    @abstractmethod
    def draw(self) -> None:
        pass