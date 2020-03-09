# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:29:33 2020

@author: miller.caden
"""

import pygame
pygame.init()

size = width, height = 1000, 900
step = 32
speed = [step, step]
pos = [100, 0]
black = 0, 0, 0


screen = pygame.display.set_mode(size)

block = pygame.image.load("square.png")
blockrect = block.get_rect()

getTicksLastFrame = 0.0
timeCheck = (pygame.time.get_ticks()) / 1000.0

while 1:
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()




    speed[0] = 1 + speed[0] * (deltaTime * deltaTime)

    pos = [pos[0], speed[1] * deltaTime + pos[1]]



    print(pos)

    blockrect.center = (int(pos[0]), int(pos[1]))
    
    screen.fill(black)
    screen.blit(block, blockrect)
    pygame.display.flip()
    



