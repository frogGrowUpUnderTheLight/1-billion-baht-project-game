import pygame, math

class Background:
    def __init__(self, background):
        self.speed = 10
        self.x = 0
        self.y = 0
        self.angle = 90
        self.background = background
        self.image = pygame.image.load('./assets/maps/stage0.jpg')
        self.image = pygame.transform.scale(self.image, (1080, 720));

    def move(self, direction, reset):
        reset()
        if direction == 'up': self.calculateNewPosition(self.angle + 180)
        elif direction == 'down': self.calculateNewPosition(self.angle)
        elif direction == 'left': self.calculateNewPosition(self.angle - 90 )
        elif direction == 'right': self.calculateNewPosition(self.angle + 90)
        self.render()

    def render(self):
        image = pygame.transform.rotate(self.image, self.angle - 90)
        self.background.blit(image, (self.x, self.y))


    def calculateNewPosition(self, heading):
        if heading >= 360: heading = heading - 360
        elif heading < 0: heading = heading + 360
        radians = math.radians(heading)
        self.x = self.x + self.speed * math.cos(radians)
        self.y = self.y - self.speed * math.sin(radians)