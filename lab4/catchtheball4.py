import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 5
screen = pygame.display.set_mode((600, 600))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

ochki = 0  #счетчик очков
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)

x = []
y = []
r = []
color = []

a = []
b = []
c = []
color1 = []

global n
n = 10                                      #количество шаров и кубиков

for i in range(n):
    x.append(randint(100, 500))
for i in range(n):
    y.append(randint(100, 500))              #создаём списки координат, радиусов и цветов для шариков; дальше всё берём отсюда
for i in range(n):
    r.append(randint(30, 40))                   
for i in range(n):
    color.append(COLORS[randint(0, 5)])
for i in range(n):
    a.append(randint(10, 50))

for i in range(n):                          #b, c - координаты угла кубика, а - сторона
    a.append(randint(10, 20))
for i in range(n):
    b.append(randint(100, 500))
for i in range(n):
    c.append(randint(100, 500))
for i in range(n):
    color1.append(COLORS[randint(0, 5)])
    

def ball(x, y, color, r):
    circle(screen, color, (x, y), r)           #Шар
def square(a, b, c, color):
    rect(screen, color, (b, c, a, a))          #Кубик
    

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            file = open('raiting.txt', 'a')
            file.write('player ' + str(ochki) + '\n')
            file.close()
            finished = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            e_x = event.pos[0]  
            e_y = event.pos[1]
            for i in range(n):
                if (e_x - int(x[i]))**2 + (e_y - int(y[i]))**2 <= (int(r[i]))**2:   #проверка попадания в шарик
                    ochki +=1
                    r[i] = 0              #исчезание шарика
                    color[i] = BLACK
                else:
                    ochki +=0
            for i in range(n):
                if int(b[i]) <= e_x <= int(b[i])+int(a[i]):   #проверка попадания в кубик
                    if int(c[i]) <= e_y <= int(c[i])+int(a[i]):
                        ochki +=5
                        a[i] = 0              #исчезание кубика
                        color1[i] = BLACK
                    else:
                        ochki +=0
                else:
                    ochki +=0        
                    
    textsurface = myfont.render(str(ochki), False, (255,255,255))   #счётчик очков выводится на экран
    screen.blit(textsurface, (250,0))

    for i in range(n):                        
        ball(x[i], y[i], color[i], r[i])
        if 100 < y[i] < 500:
            if 100 < x[i] < 500:                              #тут шарики двигаются
                x[i] += randint(-30, 30)
                y[i] += randint(-30, 30)
            if x[i] >= 500:
                x[i] -= 50
                y[i] += randint(-30, 30)
            if x[i] <= 100:
                x[i] += 50
                y[i] += randint(-30, 30)
        if y[i] >= 500:
            if 100 < x[i] < 500:
                x[i] += randint(-30, 30)
                y[i] -= 50
            if x[i] >= 500:
                x[i] -= 50
                y[i] -= 50
            if x[i] <= 100:
                x[i] += 50
                y[i] -= 50
        if y[i] <= 100:
            if 100 < x[i] < 500:
                x[i] += randint(-30, 30)
                y[i] += 50
            if x[i] >= 500:
                x[i] -= 50
                y[i] += 50
            if x[i] <= 100:
                x[i] += 50
                y[i] += 50
        
    for i in range(n):                        
        square(a[i], b[i], c[i], color1[i])
        if 100 < c[i] < 500:
            if 100 < b[i] < 500:                              #тут двигаются кубики
                b[i] += randint(-50, 50)
                c[i] += randint(-50, 50)
            if b[i] >= 500:
                b[i] -= 50
                c[i] +=randint(-50, 50)
            if b[i] <= 100:
                b[i] += 50
                c[i] += randint(-50, 50)
        if c[i] >= 500:
            if 100 < b[i] < 500:
                b[i] += randint(-50, 50)
                c[i] -= 50
            if b[i] >= 500:
                b[i] -= 50
                c[i] -= 50
            if b[i] <= 100:
                b[i] += 50
                c[i] -= 50
        if c[i] <= 100:
            if 100 < b[i] < 500:
                b[i] += randint(-50, 50)
                c[i] += 50
            if b[i] >= 500:
                b[i] -= 50
                c[i] += 50
            if b[i] <= 100:
                b[i] += 50
                c[i] += 50  
    
    pygame.display.update()
    screen.fill(BLACK)


pygame.quit()                 #ну и всё

