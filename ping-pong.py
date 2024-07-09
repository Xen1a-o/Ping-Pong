#Ping Pong
from pygame import*

mw = display.set_mode((700,500))
mw.fill((255,230,255))

class GameSprite(sprite.Sprite):
    def __init__(self,pl_im,pl_x,pl_y,pl_move,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_im),(size_x,size_y))
        self.move = pl_move
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y

    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))



class Racket(GameSprite):
    def move_r(self):
        kpress = key.get_pressed()
        if kpress[K_UP] and self.rect.y <0:
            self.rect.y -=5 
        if kpress[K_DOWN] and self.rect.y>450:
            self.rect.y -=5 

    def move_l(self):
        kpress = key.get_pressed()
        if kpress[K_w] and self.rect.y <0:
            self.rect.y -=5 
        if kpress[K_s] and self.rect.y>450:
            self.rect.y -=5 

racket_l = Racket("racket.png",20,10,5,20,100)
racket_r = Racket("racket.png",670,50,5,20,100)

        
"""movex = randint(2,3) 
movey = randint(1,2)
class Ball(GameSprite):
    def update(self):
        global move
        self.rect.x +=self.movex
        self.rect.y +=self.movey

        if self.rect.x<0 or self.rect.x>700:
            pass"""



game = True 
clock = time.Clock()
FPS=60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    #mw = display.set_mode((700,500))

    racket_l.reset()
    racket_l.move_l()

    racket_r.reset()
    racket_r.move_r()

    clock.tick(FPS)
    display.update()