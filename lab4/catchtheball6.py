import pygame
from pygame.draw import *
from pygame.locals import *
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

pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
newfont = pygame.font.SysFont('Comic Sans MS', 20)

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
    r.append(randint(20, 30))                   
for i in range(n):
    color.append(COLORS[randint(0, 5)])

for i in range(n):                          #b, c - координаты угла кубика, а - сторона
    a.append(randint(20, 50))
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

def openscreen():
    rules1 = newfont.render('Щёлкай по фигурам и получай очки', False, (255,255,255))
    rules2 = newfont.render('Чем меньше фигура - тем больше очков', False, (255,255,255))
    rules3 = newfont.render('У тебя будет 30 секунд', False, (255,255,255))
    rules4 = newfont.render('Введи своё имя и нажми пробел, чтобы начать', False, (255,255,255))#
    screen.blit(rules1, (120,60))
    screen.blit(rules2, (100,110))
    screen.blit(rules3, (170,160))
    screen.blit(rules4, (70,210))
    global player
    player = ''
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(BLACK)
                    finished = True
                if event.unicode == '\b':
                    player = player[:-1]
                    name = myfont.render(player, False, (255,255,0))
                    screen.fill(BLACK)
                    screen.blit(name, (200, 20))
                    screen.blit(rules1, (120,60))
                    screen.blit(rules2, (100,110))
                    screen.blit(rules3, (170,160))
                    screen.blit(rules4, (70,210))
                    pygame.display.update()
                else:
                    if len(player) <= 11:
                        player += event.unicode
                        name = myfont.render(player, False, (255,255,0))
                        screen.fill(BLACK)
                        screen.blit(name, (200, 20))
                        screen.blit(rules1, (120,60))
                        screen.blit(rules2, (100,110))
                        screen.blit(rules3, (170,160))
                        screen.blit(rules4, (70,210))
                        pygame.display.update()
                    
def game():
    screen.fill(BLACK)
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    ochki = 0                                                                       #счетчик очков
    pygame.time.set_timer(pygame.QUIT, 30000)
    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open('raiting6.txt', 'a')
                file.write(str(ochki) + ' ' + player + '\n')
                file.close()

                file = open('raiting6.txt', 'r')
                lines = [line.rstrip('\n') for line in file]
                j = []
                for i in range(len(lines)):
                    l = lines[i].split()
                    l[0] = int(l[0])
                    j.append(l)
                j.sort(reverse = True)
                file.close()

                file = open('raiting6.txt', 'w')
                for i in range(len(j)):
                    file.write(str(j[i][0]) + ' ' + j[i][1] + '\n')
                file.close()

                finished = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                e_x = event.pos[0]  
                e_y = event.pos[1]
                for i in range(n):
                    if (e_x - int(x[i]))**2 + (e_y - int(y[i]))**2 <= (int(r[i]))**2:   #проверка попадания в шарик
                        ochki +=3
                        r[i] = 0                                       #исчезание шарика
                        color[i] = BLACK
                    else:
                        ochki +=0
                for i in range(n):
                    if int(b[i]) <= e_x <= int(b[i])+int(a[i]):                  #проверка попадания в кубик
                        if int(c[i]) <= e_y <= int(c[i])+int(a[i]):
                            ochki += (60 - int(a[i]))
                            a[i] = 0                                         #исчезание кубика
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
                if 100 < x[i] < 500:                                     #тут шарики двигаются
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
        

openscreen()
game()

pygame.quit()                 #ну и всё
