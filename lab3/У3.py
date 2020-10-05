import pygame
from pygame.draw import *
import math as m

pygame.init()

#Небо
FPS = 30
screen = pygame.display.set_mode((500, 700))
screen.fill((0, 200, 255))

#Трава
surf1 = pygame.Surface((500, 300))
surf1.fill((0, 255, 100))
screen.blit(surf1, (0, 400))

#Забор
def Zabor(a):
    x1 = a + 0; y1 = 1.5*a + 140
    x2 = a + 700; y2 = 1.5*a + 400
    N = abs(a) // 5
    color = (0, 0, 0)
    rect(screen, color, (x1, y1 - 2, x2 - x1, y2 - y1 + 2), 2)
    h = (x2 - x1) // (N + 1)
    for i in range(N):
        rect(screen, (255, 200, 0), (x1, y1, h, y2 - y1))
        rect(screen, (0, 0, 0), (x1, y1, h, y2 - y1), 1)
        x1 += h

Zabor(-50)
Zabor(50)
Zabor(100)
Zabor(-200)

#Конура
polygon(screen, (225,200,0), ((300,425),(400,475),(400,575),(300,525)))
polygon(screen, (0,0,0), ((300,425),(400,475),(400,575),(300,525)), 2)

polygon(screen, (225,200,0), ((400,475),(450,435),(450,535),(400,575)))
polygon(screen, (0,0,0), ((400,475),(450,435),(450,535),(400,575)), 2)

polygon(screen, (225,200,0), ((300,425),(350,375),(400,475)))
polygon(screen, (0,0,0), ((300,425),(350,375),(400,475)), 2)

polygon(screen, (225,200,0), ((350,375),(410,345),(450,435), (400, 475)))
polygon(screen, (0,0,0), ((350,375),(410,345),(450,435), (400, 475)), 2)

hole = rect(screen, (225,200,0), (325, 470, 45, 60))
ellipse(screen, (0,0,0), hole)

#Цепь
ellipse(screen, (0,0,0), (340, 530, 10, 20), 1)

ellipse(screen, (0,0,0), (324, 545, 20, 10), 1)

three = rect(screen, (0,255,100), (314, 550, 20, 10), 1)
ellipse(screen, (0,0,0), three, 1)

four = rect(screen, (0,255,100), (304, 553, 20, 10), 1)
ellipse(screen, (0,0,0), four, 1)

five = rect(screen, (0,255,100), (290, 550, 20, 10), 1)
ellipse(screen, (0,0,0), five, 1)

six = rect(screen, (0,255,100), (280, 553, 20, 10), 1)
ellipse(screen, (0,0,0), six, 1)

seven = rect(screen, (0,255,100), (270, 550, 20, 10), 1)
ellipse(screen, (0,0,0), seven, 1)

eight = rect(screen, (0,255,100), (260, 548, 20, 10), 1)
ellipse(screen, (0,0,0), eight, 1)

nine = rect(screen, (0,255,100), (250, 543, 20, 10), 1)
ellipse(screen, (0,0,0), nine, 1)

#Собака
def Sabaka(b, c, d):
    ellipse(screen, (169, 169, 169), (b, c, 120*d, 60*d)) #body

    ellipse(screen, (169, 169, 169), (b + 70, c - 15, 90*d, 50*d)) #butt

    ellipse(screen, (169, 169, 169), (b - 15, c + 15, 30*d, 80*d)) #leg1

    ellipse(screen, (169, 169, 169), (b + 35, c + 30, 30*d, 80*d)) #leg2

    ellipse(screen, (169, 169, 169), (b - 30, c + 90, 40*d, 15*d)) #foot1

    ellipse(screen, (169, 169, 169), (b + 20, c + 105, 40*d, 15*d)) #foot2

    ellipse(screen, (169, 169, 169), (b + 140, c + 10, 35*d, 40*d)) #thigh2

    ellipse(screen, (169, 169, 169), (b + 75, c - 15, 35*d, 40*d)) #thigh1

    ellipse(screen, (169, 169, 169), (b + 160, c + 30, 15*d, 45*d)) #leg4

    ellipse(screen, (169, 169, 169), (b + 110, c + 20, 15*d, 45*d)) #leg3

    ellipse(screen, (169, 169, 169), (b + 90, c + 60, 35*d, 15*d)) #foot3

    ellipse(screen, (169, 169, 169), (b + 140, c + 70, 35*d, 15*d)) #foot4

    rect(screen, (169,169,169), (b - 5, c - 30, 70*d, 70*d)) #head
    rect(screen, (0,0,0), (b - 5, c - 30, 70*d, 70*d), 1)

    ellipse(screen, (169,169,169), (b - 15, c - 30, 15*d, 20*d)) #ear1
    ellipse(screen, (0,0,0), (b - 15, c - 30, 15*d, 20*d), 1)

    ellipse(screen, (169,169,169), (b + 60, c - 30, 15*d, 20*d)) #ear2
    ellipse(screen, (0,0,0), (b + 60, c - 30, 15*d, 20*d), 1)

    ellipse(screen, (255,255,255), (b + 11, c - 5, 14*d, 8*d)) #eye1
    ellipse(screen, (0,0,0), (b + 11, c - 5, 14*d, 8*d), 1)
    circle(screen, (0,0,0), (b + 18, c - 1), 2)

    ellipse(screen, (255,255,255), (b + 35, c - 5, 14*d, 8*d)) #eye2
    ellipse(screen, (0,0,0), (b + 35, c - 5, 14*d, 8*d), 1)
    circle(screen, (0,0,0), (b + 42, c - 1), 2)

    arc(screen, (0,0,0), (b + 5, c + 20, 50*d, 20*d), 0, m.pi , 1) #smile)=

Sabaka(70, 530, 1)

Sabaka(200, 400, 1)

Sabaka(300, 100, 1)

Sabaka(350, 450, 1)

Sabaka(100, 250, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
