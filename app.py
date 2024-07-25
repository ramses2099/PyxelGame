import pyxel
from ship import Ship
from bullet import Bullet
from enemies import Enemy

class App:
    def __init__(self):
        pyxel.init(width=80, height=120, title="Pyxel Game")
        pyxel.load("sprites.pyxres")
        
        self.ship = Ship(35, 100, 0)
        self.enemy = Enemy(35,25, 0)
        self.group_bullets = []
        
        self.dt = 0
        pyxel.run(self.update, self.draw)
        
    def update(self):
        self.dt += 1
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.group_bullets.append(Bullet(self.ship.x, self.ship.y - 8, 0))
            
        self.ship.update(self.dt)
        
        # update bullet  
        for b in self.group_bullets:
            b.update(self.dt)
        
        self.clear_group()
    
    def draw(self):
       pyxel.cls(0) # clear windows
       self.ship.draw()
       
       self.enemy.draw()
       
       for b in self.group_bullets:
           b.draw()
       
    def clear_group(self):
        for b in self.group_bullets:
           if not b.alive:
               self.group_bullets.remove(b)


if __name__ == "__main__":
    App()