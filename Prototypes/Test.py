import pygame

pygame.init()
Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
Screen.fill((255, 255, 255))
pygame.display.set_caption("Pet the Pigeon")

Text = pygame.font.SysFont(None, 24)
Text_Line1 = Text.render(("Pet the pigeon"), True, (0, 0, 255))

Side_Menu_Surface = pygame.Surface((280, 720))
Side_Menu_Surface.fill((128, 128, 128))

Chicken_Art = pygame.Surface((360, 360), pygame.SRCALPHA)

Chicken_Nose_Outline = pygame.draw.polygon(Chicken_Art, (0,0,0), ((165, 126),(170, 149),(146, 140)), 5)
Chicken_Circle_Lower_Body_Outline = pygame.draw.circle(Chicken_Art, (0,0,0), (180, 180), 36, 5)
Chicken_Circle_Upper_Body_Outline = pygame.draw.circle(Chicken_Art, (0,0,0), (180, 140), 28, 5)
Chicken_Circle_Lower_Body = pygame.draw.circle(Chicken_Art, ("grey"), (180, 180), 32, 0)
Chicken_Circle_Upper_Body = pygame.draw.circle(Chicken_Art, ("grey"), (180, 140), 24, 0)
Chicken_Circle_Lower_Body = pygame.draw.circle(Chicken_Art, (0,0,0), (180, 135), 5, 0)
Chicken_Nose = pygame.draw.polygon(Chicken_Art, ("yellow"), ((165, 130),(170, 145),(150, 140)))

#pygame.draw.circle(Screen, (255, 255, 255), (180, 180), 100)

Run = True

while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    Screen.blit(Screen, (0, 0))
    Screen.blit(Text_Line1, (48, 32))
    #Screen.blit(Side_Menu_Surface, (1000, 0))
    Screen.blit(Chicken_Art, (0, 0))

    fps = 60
    pygame.display.flip()

pygame.quit()

