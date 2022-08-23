# its a 15-puzzle game project
from tabnanny import check
import numpy as np
import pygame as pg
import time
from pygame.locals import *
from array import *
pg.init()

WIDTH, HEIGHT = 800, 800
size = (HEIGHT//4)/1.1
color = [(0,0,0), (255,48,48), (255,255,255), (0, 255, 0)] #BLACK, RED, WHITE, GREEN

xlist = [(size*0.05), ((HEIGHT/4) + size*0.05), ((HEIGHT/2) + size*0.05), ((HEIGHT/4)*3 + size*0.05)]
ylist = [(size*0.05), ((HEIGHT/4) + size*0.05), ((HEIGHT/2) + size*0.05), ((HEIGHT/4)*3 + size*0.05)]
a = 0 
gameOn = True
result1 = False
result2 = False
result3 = False

ax = np.array([[(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])],
               [(xlist[0]), (xlist[1]), (xlist[2]), (xlist[3])]])
ay = np.array([[(ylist[0]), (ylist[0]), (ylist[0]), (ylist[0])],
               [(ylist[1]), (ylist[1]), (ylist[1]), (ylist[1])],
               [(ylist[2]), (ylist[2]), (ylist[2]), (ylist[2])],
               [(ylist[3]), (ylist[3]), (ylist[3]), (ylist[3])]])


screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("15PUZZLE by Pablo") 
my_font = pg.font.SysFont('Comic Sans MS', 50)

def rarray(): # Random 1-15 numbers array
    global num
    num = np.random.choice(16, size=(4, 4), replace=False)

def check():
    global wCheck, result1, result2
    wCheck = np.arange(1,17).reshape(4, 4)
    wCheck[3, 3] = 0
    result1 = np.allclose(wCheck, num)
    #result2 = np.array_equal(wCheck, num)
    print(result1)


check
rarray()
while gameOn:  #Main Game loop
    screen.fill((color[0]))
    for x in range(4):
        for y in range(4):    
            if num[x, y] != 0 and result3 == False:
                pg.draw.rect(screen, (color[2]),((ax[x ,y]), (ay[x ,y]), size, size), 5, 10,)
                screen.blit(my_font.render(str(num[x, y]), True, (color[2])), ((ax[x ,y]+70), (ay[x ,y]+60)))

            elif num[x, y] == 0:
                pg.draw.rect(screen, (color[1]), ((ax[x ,y]), (ay[x ,y]), size, size), 5, 10)
                for event in pg.event.get():
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_UP:
                            if x != 0:
                                a = num[x-1, y] 
                                num[x-1, y] = 0
                                num[x, y] = a
                            else:
                                continue
                        if event.key == pg.K_DOWN:
                            if x != 3:
                                a = num[x+1, y]
                                num[x+1, y] = 0
                                num[x, y] = a
                            else:
                                continue
                        if event.key == pg.K_RIGHT:
                            if y != 3:
                                a = num[x, y+1] 
                                num[x, y+1] = 0
                                num[x, y] = a
                            else:
                                continue
                        if event.key == pg.K_LEFT:
                            if y != 0:
                                a = num[x, y-1] 
                                num[x, y-1] = 0
                                num[x, y] = a
                            else:
                                continue
                        if event.key == QUIT or event.key == pg.K_ESCAPE:
                            gameOn = False 
                        elif event.key == pg.K_BACKSPACE:
                            check()
                            if result1 == True:
                                result3 = True
                                screen.fill((color[0]))   
                                screen.blit(my_font.render(("WIN!"), True, (color[2])), ((ax[x ,y]+70), (ay[x ,y]+60)))
    
    pg.display.update()
print(num)
print(wCheck)