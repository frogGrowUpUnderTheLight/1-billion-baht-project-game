import pygame, math

class Background:
    def __init__(self, screen):
        self.x = 0
        self.y = 0
        self.screen = screen
        self.image = pygame.image.load('./assets/maps/test_background.png')

        # Get screen broundaries
        image_rect = self.image.get_rect();
        screen_rect = screen.get_rect();
        self.boundaries = tuple(map(lambda i, j: (i - j) * -1, image_rect, screen_rect))

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def calculateNewPosition(self, heading, speed):
        if heading >= 360: heading = heading - 360
        elif heading < 0: heading = heading + 360
        radians = math.radians(heading)
        self.x = self.x + speed * math.cos(radians)
        self.y = self.y - speed * math.sin(radians)

        # Make sure the background does not go off screen
        if (self.x > self.boundaries[0]): self.x = self.boundaries[0]
        if (self.x < self.boundaries[2]): self.x = self.boundaries[2]
        if (self.y > self.boundaries[1]): self.y = self.boundaries[1]
        if (self.y < self.boundaries[3]): self.y = self.boundaries[3]

        return (self.x, self.y)
