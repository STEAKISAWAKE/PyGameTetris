import pygame

pygame.init()

screen = pygame.display.set_mode((800, 700))

blue = (0,0,255)
red = (255,0,0)
light_blue = (0,147,255)
green = (0,255,0)
yellow = (255,255,0)
orange = (255,165,0)

block = pygame.image.load("square.png")


class Parent:

    position = [0.0, 0.0]
    speed = 32.0
    color = (1.0, 0.0, 0.0)

    blocks = []
    rects = []

    timeSinceLastMove = 0.0

    def __init__(self):
        self.position = [0.0, 0.0]
        self.speed = 32
        self.color = (1.0, 0.0, 0.0)

        self.blocks = []
        self.rects = []

        self.timeSinceLastMove = 0.0

    def draw(self):
        for x in range(3):
            pygame.draw.rect(screen, self.color, self.rects[x])
        
    def update(self, deltaTime):
        if (pygame.time.get_ticks() - self.timeSinceLastMove) / 1000.0 >= 1.0:
            self.timeSinceLastMove = pygame.time.get_ticks()
            self.position = [self.position[0], self.speed[1] + self.position[1]]
    
    def start(self):
        for x in range(3):
            self.blocks[x] = block
            self.rects[x] = block.get_rect()

    def end(self):
        pass


class BlockBase(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self, deltaTime, timeSinceLastMove, t):
       if (t - timeSinceLastMove) / 1000.0 >= 1.0:
           self.position = [self.pos[0], self.speed[1] + self.pos[1]]
       
        
class Square(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self, deltaTime, timeSinceLastMove, t):
        if (t - timeSinceLastMove) / 1000.0 >= 1.0:
            self.position = [self.pos[0], self.speed[1] + self.pos[1]]
            
        
class Line(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class ZBlockR(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class ZBlockL(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class TBlock(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class LBlockL(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass


class LBlockR(Parent):
    def blocks(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass