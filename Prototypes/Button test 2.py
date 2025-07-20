import pygame, Button_Class, time
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
BGGrey = (150,150,150)
Screen.fill((BGGrey))

fps = pygame.time.Clock()
IMG = pygame.image.load
# Maybe put ui elements image files inside another py file?
Click_Img_Def = IMG('Assets/UI/Btn_Def_Action.png').convert_alpha()
Click_Img_Prs = IMG('Assets/UI/Btn_Prs_Action.png').convert_alpha()

Exit_Img_Def = IMG('Assets/UI/Btn_Def_Exit.png').convert_alpha()
Exit_Img_Prs = IMG('Assets/UI/Btn_Prs_Exit.png').convert_alpha()

Score_Img = IMG('Assets/UI/Score.png').convert_alpha()
Chick_Img = IMG('Assets/Aseprite files/Chicken.png').convert_alpha()

Click_Btn = Button_Class.Button(36, 280, Click_Img_Def, 1)
Exit_Btn = Button_Class.Button(260, 280, Exit_Img_Def, 1)

Chicken_x = 82
Chicken_y = 84

Amount_Of_Eggs = 0
Run = True #Condition to run while loop

def Button_Logic():
    global Run, Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1
        Click_Btn.image = Click_Img_Prs
    else:
        Click_Btn.image = Click_Img_Def
        pygame.time.delay(150)

    if Exit_Btn.draw(Screen):
        Exit_Btn.image = Exit_Img_Prs
        Run = False
    else:
        Exit_Btn.image = Exit_Img_Def
        pygame.time.delay(150)

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