# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 11:29:33 2020

@author: miller.caden
"""

import pygame

import blocks

pygame.init()

size = width, height = 1032, 932
step = 32
speed = [step, step]
pos = [width / 2, 16]

currentBlock = None

black = 0, 0, 0

screen = pygame.display.set_mode(size)

block = pygame.image.load("square.png")
blockrect = block.get_rect()

getTicksLastFrame = 0.0
timeCheck = (pygame.time.get_ticks()) / 1000.0

timeSinceLastMove = 0.0

while 1:
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                pos = [pos[0], speed[1] + pos[1]]
            if event.key == pygame.K_LEFT:
                pos = [pos[0] - speed[0], pos[1]]
            if event.key == pygame.K_RIGHT:
                pos = [speed[0] + pos[0], pos[1]]

        if event.type == pygame.QUIT:
            pygame.quit()

# So that the blocks auto move when one second passes
    if (t - timeSinceLastMove) / 1000.0 >= 1.0:
        timeSinceLastMove = t
        pos = [pos[0], speed[1] + pos[1]]


    print(pos)

    blockrect.center = (int(pos[0]), int(pos[1]))
    
    screen.fill(black)
    screen.blit(block, blockrect)
    pygame.display.flip()
    



