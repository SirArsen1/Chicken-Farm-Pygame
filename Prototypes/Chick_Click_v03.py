import pygame, Button_Class
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

fps = pygame.time.Clock()

Click_Img = pygame.image.load('Assets/UI/ClickChick_Btn.png').convert_alpha()
Exit_Img = pygame.image.load('Assets/UI/Exit_Btn.png').convert_alpha()
Score_Img = pygame.image.load('Assets/UI/Score.png').convert_alpha()
Chick_Img = pygame.image.load('Assets/Aseprite files/Chicken.png').convert_alpha()

Click_Btn = Button_Class.Button(36, 280, Click_Img, 1)
Exit_Btn = Button_Class.Button(260, 280, Exit_Img, 1)

Chicken_x = 82
Chicken_y = 84

Amount_Of_Eggs = 0
Run = True #Condition to run while loop

def Button_Logic():
    global Run, Amount_Of_Eggs, Chicken_y

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1
        #Chicken_y += 5 # Attempt to animate chicken bounce after button press
    else:
        if Chicken_y > 84:
            #Chicken_y -= 5 # Attempt to animate chicken bounce after button press

    if Exit_Btn.draw(Screen):
        Run = False

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

def main():
    global Run, fps

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Game_Text()
        Screen.blit(Chick_Img, (Chicken_x, Chicken_y))
        Button_Logic()

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()