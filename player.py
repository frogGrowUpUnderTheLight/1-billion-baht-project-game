import pygame, math

class Player:
    def __init__(self, background):
        self.speed = 10
        self.x = 200
        self.y = 200
        self.angle = 90
        self.background = background
        self.image = pygame.image.load('./assets/heroes/lu-bu.png')
        self.image = pygame.transform.scale(self.image, (50, 50));

    def move(self, direction, reset):
        reset()
        if direction == 'up': self.calculateNewPosition(self.angle)
        elif direction == 'down': self.calculateNewPosition(self.angle + 180)
        elif direction == 'left': self.calculateNewPosition(self.angle + 90 )
        elif direction == 'right': self.calculateNewPosition(self.angle - 90)
        self.render()

    def turn(self, direction):
        if direction == 'right': self.angle = self.angle - 1
        elif direction == 'left': self.angle = self.angle + 1
        if self.angle >= 360: self.angle = self.angle - 360
        elif self.angle < 0: self.angle = self.angle + 360
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
        # if self.x > 1080 - 50:
        #     self.x = 1080 - 50
        # if self.x < 0:
        #     self.x = 0
        # if self.y < 0:
        #     self.y = 0
        # if self.y > 720 - 50:
        #     self.y = 720 - 50