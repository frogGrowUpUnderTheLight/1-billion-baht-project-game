import pygame, math

def loadScale(file, scale):
    image = pygame.image.load(file)
    return pygame.transform.smoothscale(image, scale)

class Player:
    def __init__(self, screen, background):
        self.speed = 10
        self.baseHeightJump = 100
        self.maxHeigtJump = 0
        self.speedJump = (self.baseHeightJump + 100)/20
        self.center_pos = (350, 250)
        self.screen_center_pos = (400, 300)
        self.map_location = (0, 0)
        self.angle = 0
        self.background = background
        self.screen = screen
        self.image = pygame.image.load('./assets/heroes/arrow.png')
        self.n_image = loadScale('./assets/heroes/char_base_N.png', (100,100))
        self.s_image = loadScale('./assets/heroes/char_base_S.png', (100,100))
        self.w_image = loadScale('./assets/heroes/char_base_W.png', (100,100))
        self.e_image = loadScale('./assets/heroes/char_base_E.png', (100,100))
        self.ne_image = loadScale('./assets/heroes/char_base_NE.png', (100,100))
        self.se_image = loadScale('./assets/heroes/char_base_SE.png', (100,100))
        self.nw_image = loadScale('./assets/heroes/char_base_NW.png', (100,100))
        self.sw_image = loadScale('./assets/heroes/char_base_SW.png', (100,100))
        self.jumping = False
        self.jumpTimes = 0
        self.gConstant = 0.5
        self.jumpDir = 1
        self.z = 0

    def reset(self):
        self.angle = 0
        self.center_pos = (400, 300)

    def move(self, direction):
        if direction == 'left': heading = self.angle
        elif direction == 'right': heading = self.angle + 180
        elif direction == 'down': heading = self.angle + 90
        elif direction == 'up': heading = self.angle - 90
        self.map_location = self.background.calculateNewPosition(heading, self.speed)

    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jumpTimes = 1
            self.jumpDir = 1
            self.gConstant = self.gConstant*-1
            self.z = 0
        else:
            self.jumpTimes += 1
            self.jumpDir = 1
            if self.gConstant > 0: self.gConstant = self.gConstant*-1
        self.vi = self.speedJump
        self.vt = self.vi
        self.maxHeigtJump = self.z + self.baseHeightJump
        self.vo = 2*self.gConstant*self.maxHeigtJump
        if self.vo < 0: self.vo = math.sqrt(self.vo*-1)

    def updateJump(self):
        if not self.jumping:
            return

        self.vi = self.vt
        self.vt += self.gConstant
        self.executeJump((self.vt*self.vt - self.vi*self.vi)/(self.gConstant*2)*self.jumpDir)
        if self.vt == 0:
            self.jumpDir = -1
            if self.gConstant < 0:
                self.gConstant = self.gConstant*-1
        if self.vt >= self.vo:
            self.jumpDir = 1
            self.jumping = False
            self.jumpTimes = 0
            self.z = 0
            self.center_pos = (400, 300)

    def executeJump(self, change):
        self.z += change
        self.center_pos = tuple(map(lambda i, j: i - j, self.center_pos, (0,change)))

    def turn(self, direction):
        if direction == 'right': self.angle = self.angle - 1
        elif direction == 'left': self.angle = self.angle + 1
        if self.angle >= 360: self.angle = self.angle - 360
        elif self.angle < 0: self.angle = self.angle + 360

    def render(self):
        self.updateJump()

        # Ref https://stackoverflow.com/questions/4183208/how-do-i-rotate-an-image-around-its-center-using-pygame
        # offset from pivot to center
        pos = self.screen_center_pos
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

        if 22 < self.angle <= 67: image = self.nw_image
        elif 67 < self.angle <= 112: image = self.w_image
        elif 112 < self.angle <= 157: image = self.sw_image
        elif 157 < self.angle <= 202: image = self.s_image
        elif 202 < self.angle <= 247: image = self.se_image
        elif 247 < self.angle <= 292: image = self.e_image
        elif 292 < self.angle <= 337: image = self.ne_image
        else: image = self.n_image
        self.screen.blit(image, self.center_pos)
