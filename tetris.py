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

createdBlock = blocks.Parent()

createdBlock.start()

while 1:
    t = pygame.time.get_ticks()
    # deltaTime in seconds.
    deltaTime = (t - getTicksLastFrame) / 1000.0
    getTicksLastFrame = t

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                createdBlock.position = [createdBlock.position[0],  createdBlock.position[1] + createdBlock.speed]
            if event.key == pygame.K_LEFT:
                createdBlock.position = [createdBlock.position[0] - createdBlock.speed, createdBlock.position[1]]
            if event.key == pygame.K_RIGHT:
                createdBlock.position = [createdBlock.position[0] + createdBlock.speed, createdBlock.position[1]]

        if event.type == pygame.QUIT:
            pygame.quit()

    createdBlock.update(deltaTime)


    print(pos)


    
    screen.fill(black)
      
    createdBlock.draw()
    
    pygame.display.flip()
    



