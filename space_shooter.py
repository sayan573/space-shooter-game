import pygame
import random
import math
from pygame import mixer

mixer.init()
pygame.init()

screen=pygame.display.set_mode((960,641))
pygame.display.set_caption("Space Shooter Game")
icon=pygame.image.load("space_logo.png")
pygame.display.set_icon(icon)
background=pygame.image.load("bg.jpg")
spaceshipimg=pygame.image.load("rocket.png")

alienimg=[]
alienX=[]
alienY=[]
alienspeedX=[]
alienspeedY=[]

no_of_aliens=8

for i in range(no_of_aliens):
    alienimg.append(pygame.image.load("alien_ship.png"))
    alienX.append(random.randint(0,896))
    alienY.append(random.randint(10,300))
    alienspeedX.append(0.8)
    alienspeedY.append(60)

score=0
bulletimg=pygame.image.load("bullet.png")
check=False
bulletX=447
bulletY=534

spaceshipX=432
spaceshipY=560
changeX=0

running=True

font=pygame.font.SysFont("Arial",32)
def score_text():
    img=font.render(f"Score: {score}",True,"white")
    screen.blit(img,(10,10))

font_gameover=pygame.font.SysFont("Arial",64,"bold")

def gameover():
    over=mixer.Sound("game_over.mp3")
    over.set_volume(0.3)
    over.play()
    img_gameover=font_gameover.render("GAME OVER",True,"white")
    screen.blit(img_gameover,(300,250))
    font=pygame.font.SysFont("Calibri",32,"bold")
    img=font.render(f"Total Score: {score}",True,"white")
    screen.blit(img,(365,350))

while running:
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                changeX=-1.2
            if event.key==pygame.K_RIGHT:
                changeX=1.2
            if event.key==pygame.K_SPACE:
                if check is False:
                    check=True
                    bulletX=spaceshipX+19.5
        if event.type==pygame.KEYUP:
            changeX=0
    spaceshipX+=changeX
    if spaceshipX<=0:
        spaceshipX=0
    elif spaceshipX>=896:
        spaceshipX=896
    for i in range(no_of_aliens):
        if alienY[i]>510:
            for j in range(no_of_aliens):
                alienY[j]=2000
            gameover()
            break
        alienX[i]+=alienspeedX[i]
        if alienX[i]<=0:
            alienspeedX[i]=0.8
            alienY[i]+=alienspeedY[i]
        elif alienX[i]>=898:
            alienspeedX[i]=-0.8
            alienY[i]+=alienspeedY[i]
        distance=math.sqrt(math.pow(bulletX-alienX[i],2)+math.pow(bulletY-alienY[i],2))
        if distance<27:
            explosion=mixer.Sound("death.mp3")
            explosion.set_volume(0.3)
            explosion.play()
            bulletY=590
            check=False
            alienX[i]=random.randint(0,896)
            alienY[i]=random.randint(5,220)
            score=score+5
        screen.blit(alienimg[i],(alienX[i],alienY[i]))
        if bulletY<=0:
            bulletY=534
            check=False
        if check:
            screen.blit(bulletimg,(bulletX,bulletY))
            bulletY-=2
        screen.blit(spaceshipimg,(spaceshipX,spaceshipY))
        score_text()

    pygame.display.update()