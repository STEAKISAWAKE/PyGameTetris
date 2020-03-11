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
    
    t = timeSinceLastMove = 0.0
    color = [blue, yellow, red, light_blue, green, orange]
    filename = ["", "", "", ""]
    blockrects = []
    blocks = []

    def __init__(self):
        self.position = [0.0]
        self.speed = 32
        self.color = (1.0, 0.0, 0.0)

        self.blocks = []
        self.rects = []

    def draw(self):
        pygame.draw.rect(screen, self.color, self.blockrect)
        
    def update(self, deltaTime, timeSinceLastMove, t):
        if (t - timeSinceLastMove) / 1000.0 >= 1.0:
            self.position = [self.position[0], self.speed[1] + self.position[1]]
    
    def start(self, filename, blocks, blockrects):
        for x in range(3):
            blocks[x] = block
            rects[x] = block.get_rect()

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