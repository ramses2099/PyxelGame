import pyxel
from sprite import Sprite

class Bullet(Sprite):
    def __init__(self, x: float, y: float, img: int):
        super().__init__(x, y, img, 8, 8, 8, 8, 0)
        self.speed = 6 # 5 pixel for frame 
        self.alive = True       
        
    def update(self, dt: int) -> None:
        self.y -= self.speed
        if self.y < 0:
            self.alive = False
    
    def draw(self) -> None:
        pyxel.blt(self.x, self.y, self.img, self.u, self.v, self.w, self.h, self.colkey)