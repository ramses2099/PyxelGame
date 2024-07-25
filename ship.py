import pyxel
from sprite import Sprite


class Ship(Sprite):
    def __init__(self, x: float, y: float, img: int):
        super().__init__(x, y, img, 8, 0, 8, 8, 0)
        self.speed = 5 # 5 pixel for frame        
      
        
    def update(self, dt: int) -> None:
        if (dt % 6 < 3):
            self.u = 8
        else:
            self.u = 0        
        
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= self.speed
        if pyxel.btn(pyxel.KEY_DOWN):
            self.y += self.speed
        if pyxel.btn(pyxel.KEY_LEFT):
            self.x -= self.speed
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += self.speed
       
    
    def draw(self) -> None:
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)