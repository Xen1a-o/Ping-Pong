
#Ping Pong
from pygame import*
from typing import*

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

font.init()
pl1 = font.Font(None,50).render("Player 1 lost",False,(0,0,0))
pl2 = font.Font(None,50).render("Player 2 lost",False,(0,0,0))


racket_l = Racket("racket.png",20,10,20,100)
racket_r = Racket("racket.png",670,50,20,100)
ball = GameSprite("Ball.png",350,250,50,50)
        



game = True 
clock = time.Clock()
FPS=60

dx = 2
dy = 2

finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    
    
    ball.rect.x += dx
    ball.rect.y += dy

    if ball.rect.y > 450:
        dy = dy*(-1)
    if ball.rect.y < 0:
        dy = dy*(-1)

    if sprite.collide_rect(racket_l,ball) or sprite.collide_rect(racket_r,ball):
        dx = dx*(-1)

    if ball.rect.x > 700:
        mw.blit(pl2,(350,250))
        finish = True

    if ball.rect.x < 0:
        mw.blit(pl1,(350,250))
        finish = True
         


    if not finish:
        mw.fill((255,230,255))
        ball.reset()
        racket_l.reset()
        racket_l.move_l()
        racket_r.reset()
        racket_r.move_r()
    
    display.update()
    clock.tick(FPS)
    
