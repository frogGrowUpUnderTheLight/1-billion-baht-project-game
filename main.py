import pygame
from player import Player
from background import Background
from button import Button
pygame.init()

size = width, height = 800, 600
open = True
pygame.display.set_caption('LUBU HORSE WORLD!!!')
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
state = 'start'

BG_COLOR = 250,250,250
font = pygame.font.Font(None, 36)


# Create title
# text = font.render("LUBU HORSE WORLD GAME", 1, (10, 10, 10))
# textpos = text.get_rect(centerx=size[0]/2)
# window.blit(text, textpos)

def startGame():
    global state
    state = 'game'
    player.render()

def quitGame():
    global open
    open = False

background = Background(screen)
background.render()
player = Player(screen, background)
startButton = Button('Start', 300, 200)
exitButton = Button('Quit', 300, 250)
disabled = Button('Disabled', 300, 300)
disabled.disable()


while open:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: quitGame()

    # left, middle, right = pygame.mouse.get_pressed()
    if state == 'game':
        pressed = pygame.key.get_pressed();
        if pressed[pygame.K_UP] : player.move('up')
        if pressed[pygame.K_DOWN] : player.move('down')
        if pressed[pygame.K_LEFT] : player.move('left')
        if pressed[pygame.K_RIGHT] : player.move('right')
        if pressed[pygame.K_e] : player.turn('right')
        if pressed[pygame.K_q] : player.turn('left')
        background.render()
        player.render()

    if state == 'start':
        if event.type == pygame.MOUSEBUTTONDOWN:
            startButton.click(mouse, startGame)
            exitButton.click(mouse, quitGame)
            disabled.click(mouse, quitGame)

        mouse = pygame.mouse.get_pos()
        startButton.hover(mouse, screen)
        exitButton.hover(mouse, screen)
        disabled.hover(mouse, screen)

    pygame.display.flip()
