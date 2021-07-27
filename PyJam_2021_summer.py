from sys import exit
from random import randint,choice
import pygame, easygui
print('Install easygui and pygame if you have not already')
while True:
    option = easygui.buttonbox(msg='Choose an option', choices=['PLAY','HELP','INFO','CHEATS','RESET'], default_choice = 'PLAY',cancel_choice='PLAY')
    if option == 'PLAY':
        break
    elif option == 'HELP':
        easygui.msgbox(msg='The goal of the game is to not hit the red squares for as long as possible.\nTo move, use the left and right arrow keys.\nIf you see a yellow like square and hit it you will get a couple extra points.\nThe farther along you go the faster it will get.\nIf you see a blue triangle and hit it you will have a shield and get an extra life.\nThe checkered squares will delete all the red squares.\nThe sides will teleport you to the other side.\nThe other squares are the background.\nPress space to pause/unpause.\nA yellow flash means that you have beat your highscore.\nYour game is saved, if you would like to reset this press RESET')
        continue
    elif option == 'INFO':
        easygui.msgbox(msg='This game was created by Zachary Summers as part of the summer 2021 pyjam game jam.')
        continue
    elif option == 'RESET':
        file = open('Highscore.txt','w')
        file.write('0')
        file.close()
        file = open('coin_rects.txt','w')
        file.write('[]')
        file.close()
        file = open('shield_rects.txt','w')
        file.write('[]')
        file.close()
        file = open('background_rects.txt','w')
        file.write('[]')
        file.close()
        file = open('die_rects.txt','w')
        file.write('[]')
        file.close
        file = open('power_rects.txt','w')
        file.write('[]')
        file.close
        file = open('score.txt','w')
        file.write('0')
        file.close()
        file = open('shields.txt','w')
        file.write('0')
        file.close()
        file = open('time.txt','w')
        file.write('0')
        file.close()
        continue
    elif option == 'CHEATS':
        easygui.msgbox(msg='Press 1 to get a shield\nPress 2 to remove all red squares') 
        continue
pygame.init()
pygame.mixer.music.load('song.wav')
pygame.display.set_caption('Falling Forever')
pygame.mixer.music.play(-1)
size = (900,800)
screen = pygame.display.set_mode(size)
x = 450
y = 150
w = 50
h = 50
file = open('power_rects.txt')
exec('power_rects =' + file.read())
file.close()
file = open('shield_rects.txt')
exec('shield_rects =' + file.read())
file.close()
file = open('shields.txt')
shield = int(file.read())
file.close()
x_change = 0
file = open('die_rects.txt')
exec('die_rects =' + file.read())
file.close()
file = open('background_rects.txt')
exec('background_rects =' + file.read())
file.close()
file = open('coin_rects.txt')
exec('coin_rects =' + file.read())
file.close()
speed = 2
file = open('time.txt')
time1 = int(file.read())
file = open('score.txt')
score =  int(file.read())
file.close()
font=pygame.font.SysFont("comicsansms",50)
s = 1
coinPic = pygame.image.load('cookie.jpg')
powerPic = pygame.image.load('power.jpg')
shieldPic=pygame.image.load('shield.jpg')
coinPic = pygame.transform.scale(coinPic, (24,24))
file= open('Highscore.txt','r')
highscore=int(file.read())
file.close()
highscoreHitTimeRemaining=0
highscoreHitTimeRemainingBool=False
img = pygame.image.load('img.jpg')
img = pygame.transform.scale(img, (w,h))
pause=False
if time1//2000 >= 2:
    speed = time1//2000
while True:
    if score > highscore:
        highscore = score
        if highscoreHitTimeRemainingBool==True:
            highscoreHitTimeRemaining=10
            highscoreHitTimeRemainingBool=False
    if not pause:
        time1 += 1
    if time1% 100 == 0:
        score += 1 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            file.close()
            file = open('coin_rects.txt','w')
            file.write(str(coin_rects))
            file.close()
            file = open('shield_rects.txt','w')
            file.write(str(coin_rects))
            file.close()
            file = open('background_rects.txt','w')
            file.write(str(background_rects))
            file.close()
            file = open('die_rects.txt','w')
            file.write(str(die_rects))
            file.close
            file = open('power_rects.txt','w')
            file.write(str(power_rects))
            file.close
            file = open('score.txt','w')
            file.write(str(score))
            file.close()
            file = open('shields.txt','w')
            file.write(str(shield))
            file.close()
            file = open('time.txt','w')
            file.write(str(time1))
            file.close()
            pygame.quit()
            file=open('Highscore.txt','w')
            file.write(str(highscore))
            file.close()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                x_change = 2
            elif event.key == pygame.K_LEFT:
                x_change = -2
            if event.key == pygame.K_SPACE:
                pause = not pause
            if event.key == pygame.K_1:
                shield+=1
            if event.key == pygame.K_2:
                die_rects=[]
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                x_change = 0
    if time1%2000==0:
        speed += 1 
    if x + 25 >= 900:
        x = 51
    if x - 25 <= 0:
        x = 849
    if randint(0,5000//speed) == 5:
        power_rects.append([randint(-60,900),800,24,24])
    if randint(0,7500//speed) == 5:
        shield_rects.append([randint(-60,900),800,24,24])
    if randint(0,2500//speed)==5:
        coin_rects.append([randint(-60,900),800,24,24])
    if choice([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]):
        for i in range(0,speed- 1 ):
            die_rects.append([randint(-60,900),900,randint(20,70),randint(20,70)])
    if choice([1,0,1,0,1,0,0,0,0,0,0,0]):
        for i in range(0,speed-1):
            background_rects.append([randint(-60,900),800,randint(20,70),randint(20,70),choice([(0,255,0),(255,0,255),(0,0,255),(0,0,0)])])
    for i in shield_rects:
        if pygame.Rect((i[0],i[1],i[2],i[3])).colliderect(pygame.draw.rect(screen,(100,100,100),pygame.Rect((x-25,y-25,w,h)))):
            i[1] = -100
            shield += 1
    for i in power_rects:
        if pygame.Rect((i[0],i[1],i[2],i[3])).colliderect(pygame.draw.rect(screen,(100,100,100),pygame.Rect((x-25,y-25,w,h)))):
            die_rects = []
            power_rects = []
    for i in coin_rects:
        if pygame.Rect((i[0],i[1],i[2],i[3])).colliderect(pygame.draw.rect(screen,(100,100,100),pygame.Rect((x-25,y-25,w,h)))):
            add = randint(int(score/5),score*3)
            score += add
            i[1] = -100
    for i in die_rects:
        if not pause:
            i[1] -= speed
        if pygame.Rect((i[0],i[1],i[2],i[3])).colliderect(pygame.draw.rect(screen,(100,100,100),pygame.Rect((x-25,y-25,w,h)))):
            if shield == 0:
                die_rects = []
                speed = 2
                time1 = 0
                x = 400
                score = 0
                power_rects = []
                background_rects = []
                coin_rects = []
                highscoreHitTimeRemainingBool=True
                shield_rects = []
                break
            else:
                shield -= 1
                die_rects = []
    if not pause:
        x += x_change
    if highscoreHitTimeRemaining>0:
        screen.fill((255,255,0))
        highscoreHitTimeRemaining-=1
    else:
        screen.fill((0,0,0))
    for j in reversed(range(len(background_rects))):
        i=background_rects[j]
        if not pause:
            i[1] -= speed - 1
        pygame.draw.rect(screen,i[4],pygame.Rect((i[0],i[1],i[2],i[3])))
        if i[1] <= -100:
            background_rects.remove(i)
    for i in coin_rects:
        screen.blit(coinPic,pygame.Rect((i[0],i[1],i[2],i[3])))
        if not pause:
            i[1]-=speed
    for i in shield_rects:
        screen.blit(shieldPic,pygame.Rect((i[0],i[1],i[2],i[3])))
        if not pause:
            i[1]-=speed
    for i in power_rects:
        if not pause:
            i[1] -= speed
        screen.blit(powerPic,pygame.Rect((i[0],i[1],i[2],i[3])))
    for i in die_rects:
        pygame.draw.rect(screen,(255,0,0),pygame.Rect((i[0],i[1],i[2],i[3])))
    scoreText = font.render(''.join(["Current Score: ",str(score)]),True,(255,255,255))
    scoreText_rect  = scoreText.get_rect(topleft = (20,0))
    highscoreText = font.render(("Highscore: "+str(highscore)),True,(255,255,255))
    highscoreText_rect = highscoreText.get_rect(topleft = (20,50))
    rect = img.get_rect()
    rect.center = (x,y)
    screen.blit(img, rect)
    screen.blit(scoreText,scoreText_rect)
    screen.blit(highscoreText,highscoreText_rect)
    pygame.display.update()
