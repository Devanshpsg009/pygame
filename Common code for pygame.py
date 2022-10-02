#Common code for pygame
import pygame, sys
pygame.init()

Width = 600
Height = 600
Bg_color = (0,0,0) #R,G,B respectively


Screen = pygame.display.set_mode((Width,Height))
pygame.display.set_caption('Your title here')
Screen.fill(Bg_color)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()