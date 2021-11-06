import pygame
from player import Player
from background import Background
pygame.init()

size = width, height = 1080, 720
open = True
pygame.display.set_caption('LUBU HORSE WORLD!!!')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

BG_COLOR = 250,250,250
font = pygame.font.Font(None, 36)

# Rest the background to default
def resetBackground():
    background.fill(BG_COLOR)
    background.blit(text, textpos)

# Create background
background = pygame.Surface(size)
background = background.convert()
background.fill(BG_COLOR)

text = font.render("LUBU HORSE WORLD GAME", 1, (10, 10, 10))
textpos = text.get_rect(centerx=background.get_width()/2)
background.blit(text, textpos)

player = Player(background)
player.render()

while open:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: open = False

    screen.blit(background, (0, 0))

    # left, middle, right = pygame.mouse.get_pressed()

    pressed = pygame.key.get_pressed();
    if pressed[pygame.K_UP] : player.move('up', resetBackground)
    if pressed[pygame.K_DOWN] : player.move('down', resetBackground)
    if pressed[pygame.K_LEFT] : player.move('left', resetBackground)
    if pressed[pygame.K_RIGHT] : player.move('right', resetBackground)
    if pressed[pygame.K_e] : player.turn('right')
    if pressed[pygame.K_q] : player.turn('left')

    pygame.display.flip()