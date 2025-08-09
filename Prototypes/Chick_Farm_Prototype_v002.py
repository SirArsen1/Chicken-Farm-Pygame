import pygame, Button_Class_02, random, time
pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

Chicken_Nest_Surface = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Empty_Color = (0, 0, 0, 0)

Draw = pygame.Surface.blit
fps = pygame.time.Clock()
img = pygame.image.load

Click_Img = img('Assets/UI/Btn_Def_Action.png').convert_alpha()
Exit_Img = img('Assets/UI/Btn_Def_Exit.png').convert_alpha()
Score_Img = img('Assets/UI/Score.png').convert_alpha()
Chick_Img = img('Assets/Aseprite files/Chicken.png').convert_alpha()
Add_Chick_Img = img('Assets/UI/Btn_Def_AddChick.png').convert_alpha()
Kill_Chick_Img = img('Assets/UI/Btn_Def_KillChick.png').convert_alpha()

Click_Btn = Button_Class_02.Button(144, 280, Click_Img, 1)
Exit_Btn = Button_Class_02.Button(368, 280, Exit_Img, 1)
Add_Chick_Btn = Button_Class_02.Button(440, 280, Add_Chick_Img, 1)
Kill_Chick_Btn = Button_Class_02.Button(512, 280, Kill_Chick_Img, 1)

Buttons = pygame.sprite.Group()
Buttons.add(Click_Btn, Exit_Btn, Add_Chick_Btn, Kill_Chick_Btn)

Amount_Of_Eggs = 0
Run = True

def Button_Logic():
    global Run, Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        Run = False

    if Add_Chick_Btn.draw(Screen): #I need to understand how to make it so it creates a chicken class and populates the designated parts of screen with them vice verse the kill button ofc
        Chickens.draw(Screen)

    #if Kill_Chick_Btn.draw(Screen):

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
    Screen.blit(Text_Pad_Surface, (216, 16))

class Chicken_Class(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)

Chick_NPC = Chicken_Class(42, 82, Chick_Img, 1)

Chickens = pygame.sprite.Group()
Chickens.add(Chick_NPC)

def main():
    global Run, fps, Draw

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Game_Text()
        Button_Logic()

        Chickens.update()

        Buttons.update()
        Buttons.draw(Screen)

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()