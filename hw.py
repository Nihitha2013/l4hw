import pygame 
import random
from pygame import mixer
mixer.init()
pygame.init()

color="indigo"
class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,h,w):
        super().__init__()
        self.image=pygame.Surface([w,h])
        
        pygame.draw.rect(self.image,color,pygame.Rect(0,0,w,h))
        self.rect=self.image.get_rect()

    def moveRight(self,pix):
        self.rect.x +=pix
    def moveLeft(self,pix):
        self.rect.x -=pix
    def moveForward(self,speed):
        self.rect.y-=speed*speed/10
    def moveBackward(self,speed):
        self.rect.y+=speed*speed/10

bg=pygame.image.load("bg.jpeg")
bg=pygame.transform.scale(bg,(500,500))

pygame.init()
screen=pygame.display.set_mode((500,400))
pygame.display.set_caption("Add Sprite n collision")

all_sprite_list=pygame.sprite.Group()
rad=20
sp1=Sprite(color,50,50)
sp1.rect.x=random.randint(0,450)
sp1.rect.y=random.randint(0,450)
all_sprite_list.add(sp1)

sp2=Sprite("orange",50,50)
sp2.rect.x=random.randint(0,450)
sp2.rect.y=random.randint(0,450)
all_sprite_list.add(sp2)

exit=True
clock=pygame.time.Clock()
while exit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit=False
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_x:
                exit=False


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sp1.moveLeft(5)
    if keys[pygame.K_RIGHT]:
        sp1.moveRight(5)
    if keys[pygame.K_UP]:
        sp1.moveForward(5)
    if keys[pygame.K_DOWN]:
        sp1.moveBackward(5)


    all_sprite_list.update()

    screen.blit(bg,(0,0))
    all_sprite_list.draw(screen)
    pygame.display.flip()

    if sp1.rect.colliderect(sp2.rect):
        all_sprite_list.remove(sp2)
        text="YOU WON"
        font=pygame.font.SysFont("Times New Roman",50)
        text=font.render(text,True,"blue")
        screen.blit(text,(200,200))
        mixer.music.load("goodresult-82807 (2).mp3")
        mixer.music.set_volume(0.5)
        mixer.music.play()


    pygame.display.update()
    clock.tick(10)

pygame.quit()