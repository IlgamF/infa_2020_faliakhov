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
x1 = 0; y1 = 140
x2 = 700; y2 = 400
N = 20
color = (0, 0, 0)
rect(screen, color, (x1, y1 - 2, x2 - x1, y2 - y1 + 4), 2)
h = (x2 - x1) // (N + 1)
for i in range(N):
    rect(screen, (255, 200, 0), (x1, y1, h-2, y2 - y1))
    rect(screen, (255, 200, 0), (x1, y1, h-2, y2 - y1), 2)
    x1 += h

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
ellipse(screen, (169, 169, 169), (70, 530, 120, 60)) #body

ellipse(screen, (169, 169, 169), (140, 515, 90, 50)) #butt

ellipse(screen, (169, 169, 169), (55, 545, 30, 80)) #leg1

ellipse(screen, (169, 169, 169), (105, 560, 30, 80)) #leg2

ellipse(screen, (169, 169, 169), (40, 620, 40, 15)) #foot1

ellipse(screen, (169, 169, 169), (90, 635, 40, 15)) #foot2

ellipse(screen, (169, 169, 169), (210, 540, 35, 40)) #thigh2

ellipse(screen, (169, 169, 169), (145, 515, 35, 40)) #thigh1

ellipse(screen, (169, 169, 169), (230, 560, 15, 45)) #leg4

ellipse(screen, (169, 169, 169), (180, 550, 15, 45)) #leg3

ellipse(screen, (169, 169, 169), (160, 590, 35, 15)) #foot3

ellipse(screen, (169, 169, 169), (210, 600, 35, 15)) #foot4

rect(screen, (169,169,169), (65, 500, 70, 70)) #head
rect(screen, (0,0,0), (65, 500, 70, 70), 1)

ellipse(screen, (169,169,169), (55, 500, 15, 20)) #ear1
ellipse(screen, (0,0,0), (55, 500, 15, 20), 1)

ellipse(screen, (169,169,169), (130, 500, 15, 20)) #ear2
ellipse(screen, (0,0,0), (130, 500, 15, 20), 1)

ellipse(screen, (255,255,255), (81, 525, 14, 8)) #eye1
ellipse(screen, (0,0,0), (81, 525, 14, 8), 1)
circle(screen, (0,0,0), (88, 529), 2)

ellipse(screen, (255,255,255), (105, 525, 14, 8)) #eye2
ellipse(screen, (0,0,0), (105, 525, 14, 8), 1)
circle(screen, (0,0,0), (112, 529), 2)

arc(screen, (0,0,0), (75, 550, 50, 20), 0, m.pi , 1) #smile)=


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
