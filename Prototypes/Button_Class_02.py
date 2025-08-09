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
        #surface.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()
        Action = False

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and self.clicked == False:
                self.clicked = True
                Action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return Action
