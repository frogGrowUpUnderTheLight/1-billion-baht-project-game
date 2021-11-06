import pygame

class Button:
    def __init__(self, text, x, y):
        self.x = x
        self.y = y
        self.width = 200
        self.height = 40
        self.color = (100,100,100)
        self.color_hover = (170,170,170)
        self.enabled = True
        font = pygame.font.Font(None, 36)
        self.text_x = self.x + self.width/2 - font.size(text)[0]/2
        self.text_y = self.y + self.height/2 - font.size(text)[1]/2
        self.text = font.render(text , True , (10, 10, 10))
    # Check for clicks within the button
    def click(self, mouse, clickHandler):
        if not self.enabled:
            return
        elif self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            clickHandler()
    # Draw the button as hovered or not based on mouse position
    def hover(self, mouse, screen):
        if not self.enabled:
            pygame.draw.rect(screen,(0,50,50),[self.x,self.y, self.width, self.height])
        elif self.x <= mouse[0] <= self.x + self.width and self.y <= mouse[1] <= self.y + self.height:
            pygame.draw.rect(screen,self.color_hover,[self.x,self.y, self.width, self.height])
        else:
            pygame.draw.rect(screen,self.color,[self.x,self.y, self.width, self.height])
        screen.blit(self.text, (self.text_x, self.text_y))
    def enable(self):
        self.enabled = True
    def disable(self):
        self.enabled = False
