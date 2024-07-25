import pyxel
from sprite import Sprite


class Enemy(Sprite):
    def __init__(self, x: float, y: float, img: int):
        super().__init__(x, y, img, 16, 0, 8, 8, 0)
        self.speed = 5 # 5 pixel for frame        
              
    def update(self, dt: int) -> None:        
        self.y += self.speed       
    
    def draw(self) -> None:
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)