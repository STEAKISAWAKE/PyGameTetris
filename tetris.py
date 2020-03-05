# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:29:33 2020

@author: miller.caden
"""

import sys, pygame
pygame.init()

size = width, height = 1000, 900
speed = [0, 1]
pos = [0.0, 0.0]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

block = pygame.image.load("square.png");
blockrect = block.get_rect()

clock = pygame.time.Clock();
previousTime = 0
newTime = clock.get_time()

while 1:
    previousTime = newTime
    newTime = clock.get_time()

    deltatime = previousTime - newTime

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    pos = [1, int(100 * deltatime)]

    blockrect = blockrect.move(pos)

    screen.fill(black)
    screen.blit(block, blockrect)
    pygame.display.flip()
