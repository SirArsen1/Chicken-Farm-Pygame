import pygame, Button_Class_01, random, time
pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('Chick-Click')
Screen.fill(('white'))

Chicken_Nest_Surface = pygame.Surface((192, 192), flags=pygame.SRCALPHA) # surface in which chick spawn button spawns chicken, supposedely there is supposed to be three of them, and program should check if they are empty before populating it
Empty_Color = (0, 0, 0, 0)

fps = pygame.time.Clock()
img = pygame.image.load

Click_Img = img('Assets/UI/Btn_Def_Action.png').convert_alpha()
Exit_Img = img('Assets/UI/Btn_Def_Exit.png').convert_alpha()
Score_Img = img('Assets/UI/Score.png').convert_alpha()
Chick_Img = img('Assets/Aseprite files/Chicken.png').convert_alpha()
Add_Chick_Img = img('Assets/UI/Btn_Def_AddChick.png').convert_alpha()
Kill_Chick_Img = img('Assets/UI/Btn_Def_KillChick.png').convert_alpha()

Click_Btn = Button_Class_01.Button(144, 280, Click_Img, 1)
Exit_Btn = Button_Class_01.Button(368, 280, Exit_Img, 1)
Add_Chick_Btn = Button_Class_01.Button(440, 280, Add_Chick_Img, 1)
Kill_Chick_Btn = Button_Class_01.Button(512, 280, Kill_Chick_Img, 1)

Amount_Of_Eggs = 0
Run = True #Condition to run while loop

def Button_Logic():
    global Run, Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        Run = False

    if Add_Chick_Btn.draw(Screen): #I need to understand how to make it so it creates a chicken class and populates the designated parts of screen with them vice verse the kill button ofc
        Chick_NPC_1.visibility_on()
        Chick_NPC_1.draw(Chicken_Nest_Surface) # it does add chick to the sprite
        #pygame.Surface.lock(Chicken_Nest_Surface)

    if Kill_Chick_Btn.draw(Screen):
        Chick_NPC_1.visibility_off()
        Chicken_Nest_Surface.fill(("red")) #nope, doesnt help, it covers the chicken, but prevents adding chicken back

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

class Chicken_Class():
    global Amount_Of_Eggs

    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.visibility = True
        self.idle_egg_spawn = self.visibility

    def visibility_on(self):
        self.visibility = True
        if self.visibility == True:
            pass

    def visibility_off(self):
        self.visibility = False
        if self.visibility == False:
            pass

    def draw(self, surface):
        global Amount_Of_Eggs

        Chicken_Class.visibility_on(self)

        Egg_Spawn_Delay = 100 # eggs spawn with chicken, should fix that
        Get_Time = pygame.time.get_ticks()

        if not hasattr(self, "Next_Egg_Spawn_Update"):
            self.Next_Egg_Spawn_Update = 0

        while self.idle_egg_spawn == True and (self.Next_Egg_Spawn_Update < Get_Time):
            Possible_Amount_Eggs = (1, 2, 3)
            Random_Amount_Eggs = random.choice(Possible_Amount_Eggs)
            Amount_Of_Eggs += Random_Amount_Eggs
            self.Next_Egg_Spawn_Update = Get_Time + Egg_Spawn_Delay

        Screen.blit(self.image, (self.rect.x, self.rect.y))
Chick_NPC_1 = Chicken_Class(42, 82, Chick_Img, 1)

#Chicken_Sprite_1 = Chicken_Class(42, 82, Chick_Img, 1)
#Chicken_Sprite_2 = Chicken_Class(264, 82, Chick_Img, 1)
#Chicken_Sprite_3 = Chicken_Class(486, 82, Chick_Img, 1)

def main():
    global Run, fps

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Game_Text()
        Button_Logic()
        #Chicken_Sprite_1.draw(Screen)
        #Chicken_Sprite_2.draw(Screen)
        #Chicken_Sprite_3.draw(Screen)
        pygame.Surface.blit(Screen, Chicken_Nest_Surface, (42,82))

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()