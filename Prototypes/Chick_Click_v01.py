import pygame, Button_Class_01
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

Click_Img = pygame.image.load('Assets/images/ClickChick_Btn.png').convert_alpha()
Exit_Img = pygame.image.load('Assets/images/Exit_Btn.png')

Click_Btn = Button_Class_01.Button(80, 300, Click_Img, 0.7)
Exit_Btn = Button_Class_01.Button(240, 300, Exit_Img, 0.7)

Amount_Of_Eggs = 0

def Button_Logic():
    global Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        pygame.quit()

def Game_Text():
    global Amount_Of_Eggs

    Font = pygame.font.SysFont('NeueBit', 24)
    Text = Font.render(f'Amount of Eggs: {Amount_Of_Eggs}', True, ('black'))

    Pad_Width, Pad_Height = 348, 48
    Text_Pad_Surface = pygame.Surface((Pad_Width, Pad_Height))
    Text_Pad_Surface.fill(('white'))
    pygame.draw.rect(Text_Pad_Surface, 'black', (0, 0, Pad_Width, Pad_Height), 2)

    Text_Pad_Surface.blit(Text, (64, 16))
    Screen.blit(Text_Pad_Surface, (6, 6))

Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    Game_Text()

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1
    if Exit_Btn.draw(Screen):
        Run = False

    pygame.display.update()
    fps = 60

pygame.quit()