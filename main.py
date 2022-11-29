import sys, pygame
import os
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((1000,500))

screen.fill((110,110,5))
block = pygame.image.load(os.path.join('required', 'block.jpg'))
block_x, block_y = 100, 100     
screen.blit(block,(block_x, block_y))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_UP:
                block_y -= 40
            elif event.key == K_DOWN:
                block_y += 40
            elif event.key == K_RIGHT:
                block_x += 40
            else:
                block_x -= 40
        
        screen.fill((110,110,5))
        screen.blit(block,(block_x, block_y))
        pygame.display.flip()



