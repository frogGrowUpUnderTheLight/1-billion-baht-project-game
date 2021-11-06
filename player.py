import pygame, math

class Player:
    def __init__(self, screen, background):
        self.speed = 10
        self.center_pos = (350, 250)
        self.map_location = (0, 0)
        self.angle = 0
        self.background = background
        self.screen = screen
        self.image = pygame.image.load('./assets/heroes/lu-bu.png')
        self.image = pygame.transform.scale(self.image, (100, 100));

    def move(self, direction):
        if direction == 'down': heading = self.angle
        elif direction == 'up': heading = self.angle + 180
        elif direction == 'right': heading = self.angle + 90
        elif direction == 'left': heading = self.angle - 90
        self.map_location = self.background.calculateNewPosition(heading, self.speed)

    def turn(self, direction):
        if direction == 'right': self.angle = self.angle - 1
        elif direction == 'left': self.angle = self.angle + 1
        if self.angle >= 360: self.angle = self.angle - 360
        elif self.angle < 0: self.angle = self.angle + 360

    def render(self):
        # Ref https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        # offset from pivot to center
        pos = (400, 300)
        originPos = (50, 50)
        image_rect = self.image.get_rect(topleft = (pos[0] - originPos[0], pos[1]-originPos[1]))
        offset_center_to_pivot = pygame.math.Vector2(pos) - image_rect.center

        # roatated offset from pivot to center
        rotated_offset = offset_center_to_pivot.rotate(-self.angle)

        # roatetd image center
        rotated_image_center = (pos[0] - rotated_offset.x, pos[1] - rotated_offset.y)

        # get a rotated image
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        rotated_image_rect = rotated_image.get_rect(center = rotated_image_center)

        # rotate and blit the image
        self.screen.blit(rotated_image, rotated_image_rect)
