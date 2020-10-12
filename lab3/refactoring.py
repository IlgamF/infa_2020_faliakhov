import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((666, 941))


'''
numbers in comments go from left to right
'''
#grey sky
rect(screen, (102, 102, 102), (0, 0, 666, 393))

#moon
circle(screen, (230, 230, 230), (550, 81), 57)

#clouds
ellipse(screen, (51, 51, 51), (32, 88, 521, 63))   #left
ellipse(screen, (77, 77, 77), (292, 56, 376, 67))  #right1
ellipse(screen, (77, 77, 77), (394, 132, 412, 59)) #right2
ellipse(screen, (26, 26, 26), (325, 203, 418, 60)) #right3

def House():
#house carcass
    rect(screen, (40, 34, 11), (34, 205, 347, 480))

#roof
    polygon(screen, (0, 0, 0), ([53, 168], [0, 206],
            [415, 206],[354, 168], [53, 168]))     #roof
    rect(screen, (26, 26, 26), (83, 133, 11, 55))  #tube1
    rect(screen, (26, 26, 26), (102, 84, 23, 107)) #tube2
    rect(screen, (26, 26, 26), (241, 142, 11, 34)) #tube3
    rect(screen, (26, 26, 26), (327, 121, 12, 70)) #tube4

#up windows
    rect(screen, (72, 62, 55), (57, 207, 37, 170)) #window1
    rect(screen, (72, 62, 55), (126, 207, 37, 170))#window2
    rect(screen, (72, 62, 55), (215, 207, 37, 170))#window3
    rect(screen, (72, 62, 55), (302, 207, 37, 170))#window4

#down windows
    rect(screen, (43, 17, 0), (71, 545, 66, 83))   #window1
    rect(screen, (43, 17, 0), (176, 545, 66, 83))  #window2
    rect(screen, (212, 170, 0), (276, 545, 66, 83))#window3

#balcony
    rect(screen, (26, 26, 26), (0, 393, 420, 48))  #floor
    rect(screen, (26, 26, 26), (7, 351, 11, 43))   #railing
    rect(screen, (26, 26, 26), (18, 329, 380, 22)) #bar1
    rect(screen, (26, 26, 26), (51, 351, 22, 43))  #bar2
    rect(screen, (26, 26, 26), (115, 351, 18, 43)) #bar3
    rect(screen, (26, 26, 26), (183, 351, 17, 43)) #bar4  
    rect(screen, (26, 26, 26), (257, 351, 19, 43)) #bar5
    rect(screen, (26, 26, 26), (332, 351, 20, 43)) #bar6
    rect(screen, (26, 26, 26), (397, 351, 8, 43))  #bar7

House()

#ghost
surf = pygame.Surface((200, 200))
surf.fill((0, 0, 0))

surf.set_alpha(150)

polygon(surf, (179, 179, 179), ([103, 30], [109, 30], [147, 59],
                                  [163, 74], [185, 93], [188, 118],
                                  [181, 124], [170, 126], [159, 135],
                                  [156, 147], [149, 161], [129, 161],
                                  [116, 159], [59, 167], [83, 182],
                                  [70, 183], [53, 163], [33, 152],
                                  [0, 157], [13, 135], [16, 125],
                                  [35, 98], [35, 90], [43, 76],
                                  [48, 52], [103, 30])) #body

circle(surf, (179, 179, 179), (75, 37), 30)             #head
circle(surf, (135, 205, 222), (60, 39), 8)              #eye1   
circle(surf, (135, 205, 222), (87, 34), 8)              #eye2
circle(surf, (0, 0, 0), (57, 38), 3)                    #pupil1
circle(surf, (0, 0, 0), (85, 33), 3)                    #pupil2
line(surf, (255, 255, 255), [65, 33], [59, 36], 2)      #flare1
line(surf, (255, 255, 255), [91, 28], [86, 32], 2)      #flare2

surf = pygame.transform.rotate(surf, 0)

surf = pygame.transform.scale(surf, (200, 200))

screen.blit(surf, (452, 593))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            pygame.quit()
