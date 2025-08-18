import pygame, Button_Class_02, random, time
pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('ChickFarm!!!')
Screen.fill(('white'))

Nest_Surface_1 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_1.fill(('grey'))
Nest_Surface_1_rect = Nest_Surface_1.get_rect(topleft = (42,82))
Nest_Surface_2 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_2.fill(('grey'))
Nest_Surface_3 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_3.fill(('grey'))

Nest_Surfaces = [
    {"surface":Nest_Surface_1, "occupied":False},
    {"surface":Nest_Surface_2, "occupied":False},
    {"surface":Nest_Surface_3, "occupied":False}
]

fps = pygame.time.Clock()
img = pygame.image.load
blit = pygame.Surface.blit

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

System_Buttons = pygame.sprite.Group()
System_Buttons.add(Click_Btn, Exit_Btn, Add_Chick_Btn, Kill_Chick_Btn)

Amount_Of_Eggs = 0
Run = True

def Button_Logic():
    global Run, Amount_Of_Eggs

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        Run = False

    if Add_Chick_Btn.draw(Screen):
        for nest in Nest_Surfaces:
            if not nest["occupied"]:
                Chickens.draw(nest["surface"])
                Chick_NPC.set_idle_egg_spawn_True()
                nest["occupied"] = True
                print("chic added")
                if not Chickens:
                    Chickens.add(Chick_NPC)
                else: pass
                return

    if Kill_Chick_Btn.draw(Screen):
        for nest in Nest_Surfaces:
            if nest["occupied"]:
                Chick_NPC.kill()
                Chick_NPC.set_idle_egg_spawn_False()
                nest["occupied"] = False
                Chickens.update(nest["surface"])
                nest["surface"].fill('grey')
                Chickens.update(nest["surface"])
                pygame.display.update()
                print("chic delete")
                return

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
    def __init__(self, x, y, image, scale, egg_spawn: bool = False):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.egg_spawn = egg_spawn

    def set_idle_egg_spawn_True(self):
        self.egg_spawn = True
    def set_idle_egg_spawn_False(self):
        self.egg_spawn = False

    def idle_egg_spawn(self):
        global Amount_Of_Eggs

        Egg_Spawn_Delay = 500  # egg spawn, short for testing purpose, change later
        Get_Time = pygame.time.get_ticks()

        if not hasattr(self, "Next_Egg_Spawn_Update"):
            self.Next_Egg_Spawn_Update = 0

        if self.egg_spawn == True and (self.Next_Egg_Spawn_Update < Get_Time):
            Possible_Amount_Eggs = (1, 0, 2, 0, 3)
            Random_Amount_Eggs = random.choice(Possible_Amount_Eggs)
            Amount_Of_Eggs += Random_Amount_Eggs
            self.Next_Egg_Spawn_Update = Get_Time + Egg_Spawn_Delay

Chick_NPC = Chicken_Class(0, 0, Chick_Img, 1)

Chickens = pygame.sprite.Group()
Chickens.add(Chick_NPC)

def main():
    global Run, fps, blit, Amount_Of_Eggs

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Screen.fill(('white'))

        Chick_NPC.idle_egg_spawn()

        Game_Text()
        Button_Logic()

        pygame.Surface.blit(Screen, Nest_Surface_1, (42, 82))
        pygame.Surface.blit(Screen, Nest_Surface_2, (264, 82))
        pygame.Surface.blit(Screen, Nest_Surface_3, (486, 82))

        Chickens.update()

        System_Buttons.update()
        System_Buttons.draw(Screen)

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()