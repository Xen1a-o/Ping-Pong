<<<<<<< HEAD
#Ping Pong
from pygame import*

mw = display.set_mode((700,500))
mw.fill((255,230,255))

class GameSprite(sprite.Sprite):
    def __init__(self,pl_im,pl_x,pl_y,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_im),(size_x,size_y))
        #self.move = pl_move
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y

    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))



class Racket(GameSprite):
    def move_r(self):
        kpress = key.get_pressed()
        if kpress[K_UP] and self.rect.y >0:
            self.rect.y -=5 
        if kpress[K_DOWN] and self.rect.y<400:
            self.rect.y +=5 

    def move_l(self):
        kpress = key.get_pressed()
        if kpress[K_w] and self.rect.y >0:
            self.rect.y -=5 
        if kpress[K_s] and self.rect.y<400:
            self.rect.y +=5 

racket_l = Racket("racket.png",20,10,20,100)
racket_r = Racket("racket.png",670,50,20,100)
ball = GameSprite("Ball.png",350,250,50,50)
        



game = True 
clock = time.Clock()
FPS=60

dx = 2
dy = 2


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    mw.fill((255,230,255))
    
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y > 450:
        dy = dy*(-1)
    if ball.rect.y < 0:
        dy = dy*(-1)

    if sprite.collide_rect(racket_l,ball) or sprite.collide_rect(racket_r,ball):
        dx = dx*(-1)

    ball.reset()

    racket_l.reset()
    racket_l.move_l()

    racket_r.reset()
    racket_r.move_r()
    
    display.update()
    clock.tick(FPS)
    
=======
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
>>>>>>> 62f488ba733cd6f840674cf6e9a2f5e5a39dc669
