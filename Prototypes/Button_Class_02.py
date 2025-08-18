import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        mouse = pygame.mouse
        pos = pygame.mouse.get_pos()
        action = False

        if self.rect.collidepoint(pos):
            if mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                action = True

        if mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
