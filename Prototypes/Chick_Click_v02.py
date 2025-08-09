import pygame, Button_Class_01
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

Click_Img = pygame.image.load('UI/ClickChick_Btn.png').convert_alpha()
Exit_Img = pygame.image.load('UI/Exit_Btn.png').convert_alpha()
Score_Img = pygame.image.load('UI/Score.png').convert_alpha()
Chick_Img = pygame.image.load('UI/Chicken.png').convert_alpha()

Click_Btn = Button_Class_01.Button(36, 280, Click_Img, 1)
Exit_Btn = Button_Class_01.Button(260, 280, Exit_Img, 1)

Amount_Of_Eggs = 0

def Button_Logic():
    global Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        pygame.quit()

def Game_Text():
    global Amount_Of_Eggs
    Font_Name = 'NeueBit' #Ask teacher about this problem, python fails to identify bold version of installed font
    Font_Size = 40
    Font = pygame.font.SysFont(Font_Name, Font_Size)
    Text = Font.render(f'{Amount_Of_Eggs}', True, ('black'))

    Pad_Width, Pad_Height = 288, 64
    Text_Pad_Surface = pygame.Surface((Pad_Width, Pad_Height), pygame.SRCALPHA)

    Text_Pad_Surface.blit(Score_Img, (0, 0))
    Text_Pad_Surface.blit(Text, (223, 22))
    Screen.blit(Text_Pad_Surface, (36, 16))

Run = True
while Run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    Game_Text()
    Screen.blit(Chick_Img, (90, 92))
    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1
    if Exit_Btn.draw(Screen):
        Run = False

    pygame.display.update()
    fps = 60

pygame.quit()