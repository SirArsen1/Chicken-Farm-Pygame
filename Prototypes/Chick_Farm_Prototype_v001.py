import pygame, Button_Class
pygame.init()

Window_Width, Window_Height = 360, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

fps = pygame.time.Clock()

Click_Img = pygame.image.load('UI/ClickChick_Btn.png').convert_alpha()
Exit_Img = pygame.image.load('UI/Exit_Btn.png').convert_alpha()
Score_Img = pygame.image.load('UI/Score.png').convert_alpha()
Chick_Img = pygame.image.load('Aseprite files/Chicken.png').convert_alpha()

Click_Btn = Button_Class.Button(36, 280, Click_Img, 1)
Exit_Btn = Button_Class.Button(260, 280, Exit_Img, 1)

Amount_Of_Eggs = 0
Run = True #Condition to run while loop

def Button_Logic():
    global Run, Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

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

class Chicken():
    global Amount_Of_Eggs

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.egged = False

    def draw(self, surface):
        Screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.egged == False:
            for egg in range (2000):
                Amount_Of_Eggs += 1
        else:
            if self.egged == True:
                self.egged = False
                return
    #def Birth_Event(self):
        #Amount_Of_Eggs += 1 # in a certain amount of time

Chicken_Sprite = Chicken(84, 82, Chick_Img, 1)

def main():
    global Run, fps

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Game_Text()
        #Button_Logic()
        Chicken_Sprite.draw(Screen)

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()