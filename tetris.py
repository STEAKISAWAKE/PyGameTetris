# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:29:33 2020

@author: miller.caden
"""

import sys, pygame
pygame.init()

size = width, height = 1000, 900
speed = [1, 1]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

block = pygame.image.load("");
blockrect = block.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()