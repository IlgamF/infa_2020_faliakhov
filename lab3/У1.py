
import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 700))
screen.fill((255, 255, 255))

circle(screen, (0,0,0), (350, 350), 205, 5 )
circle(screen, (255, 255, 0), (350, 350), 200)

circle(screen, (0, 0, 0), (275, 300), 32, 1)
circle(screen, (255, 200, 255), (275, 300), 30)

circle(screen, (0, 0, 0), (425, 300), 26, 1)
circle(screen, (255, 200, 255), (425, 300), 24)

circle(screen, (0, 0, 0), (275, 300), 15, 1)
circle(screen, (0, 0, 0), (425, 300), 15, 1)

circle(screen, (255, 0, 0), (275, 300), 13)
circle(screen, (255, 0, 0), (425, 300), 13)

rect(screen, (0, 0, 0), (225, 400, 250, 30))

polygon(screen, (0, 0, 0), ((210,215), (335, 265), (310,290), (185, 240)))
polygon(screen, (0, 0, 0), ((375,265), (470, 240), (495, 265), (400, 290)))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
