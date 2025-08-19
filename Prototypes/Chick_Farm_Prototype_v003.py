import pygame, Button_Class_02, random
pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('ChickFarm!!!')
Screen.fill(('white'))

Nest_Surface_1 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_2 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_3 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)

Nest_Surfaces = [
    {"surface":Nest_Surface_1, "occupied":False},
    {"surface":Nest_Surface_2, "occupied":False},
    {"surface":Nest_Surface_3, "occupied":False}
]

fps = pygame.time.Clock()
img = pygame.image.load
blit = pygame.Surface.blit

class Custom_Sprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

Click_Img = img('Assets/UI/Btn_Def_Action.png').convert_alpha()
Exit_Img = img('Assets/UI/Btn_Def_Exit.png').convert_alpha()
Score_Img = img('Assets/UI/Score.png').convert_alpha()
Chick_Img = img('Assets/Aseprite files/Chicken.png').convert_alpha()
Add_Chick_Img = img('Assets/UI/Btn_Def_AddChick.png').convert_alpha()
Kill_Chick_Img = img('Assets/UI/Btn_Def_KillChick.png').convert_alpha()
Shop_Btn_Img = img('Assets/UI batch 02/Btn_Def_Shop.png').convert_alpha()
Shop_Window_Img = img('Assets/UI batch 02/Shop_Window.png').convert_alpha()
Add_to_cart_Btn_Img = img('Assets/UI batch 02/Add_to_cart_Btn.png').convert_alpha()
Remove_from_cart_Btn_Img = img('Assets/UI batch 02/Minus_from_cart_Btn.png').convert_alpha()
Close_Window_Btn_Img = img('Assets/UI batch 02/Close_Window_Btn.png').convert_alpha()
Buy_Btn_Img = img('Assets/UI batch 02/Buy_Btn.png').convert_alpha()

Click_Btn = Button_Class_02.Button(108, 270, Click_Img, 1)
Exit_Btn = Button_Class_02.Button(332, 270, Exit_Img, 1)
Add_Chick_Btn = Button_Class_02.Button(404, 270, Add_Chick_Img, 1)
Kill_Chick_Btn = Button_Class_02.Button(476, 270, Kill_Chick_Img, 1)
Shop_Btn = Button_Class_02.Button(548, 270, Shop_Btn_Img, 1)
Add_Chicken_to_cart_Btn = Button_Class_02.Button(462, 117, Add_to_cart_Btn_Img, 1)
Add_Food_to_cart_Btn = Button_Class_02.Button(462, 153, Add_to_cart_Btn_Img, 1)
Remove_Chicken_to_cart_Btn = Button_Class_02.Button(494, 117, Remove_from_cart_Btn_Img, 1)
Remove_Food_to_cart_Btn = Button_Class_02.Button(494, 153, Remove_from_cart_Btn_Img, 1)
Close_Shop_Window_Btn = Button_Class_02.Button(196, 81, Close_Window_Btn_Img, 1)
Buy_Btn = Button_Class_02.Button(316, 235, Buy_Btn_Img, 1)

Shop_Window = Custom_Sprite(Shop_Window_Img, 180, 65)

System_Buttons = pygame.sprite.Group()
System_Buttons.add(Click_Btn, Exit_Btn, Add_Chick_Btn, Kill_Chick_Btn, Shop_Btn,)

Shop_Window_UI = pygame.sprite.Group()
Shop_Window_UI.add(Shop_Window, Add_Chicken_to_cart_Btn, Add_Food_to_cart_Btn, Remove_Chicken_to_cart_Btn, Remove_Food_to_cart_Btn, Close_Shop_Window_Btn, Buy_Btn)

Chicken_Stock = 3
Meat_Stock = 0
Amount_Of_Eggs = 0

# SHOP logic
Shop_Catalogue = [
    {"item name":"Food", "value":2, "amount":9999},
    {"item name": "Chicken", "value":6, "amount":9999},
]
Shop_Cart = [
    {"item name":"Food", "value":2, "amount":0},
    {"item name": "Chicken", "value":6, "amount":0},
]
Inventory = [
    {"item name":"Food", "value":2, "amount":0},
    {"item name":"Chicken", "value":6, "amount":0},
    {"item name":"Meat", "value":5, "amount":0},
    {"item name":"Eggs", "value":0.5, "amount":f'{Amount_Of_Eggs}'},
]

Shop_Open = False
Run = True

def Add_To_Cart(item_name, Shop_Catalogue, Shop_Cart):
    for item in Shop_Cart:
        if item['item name'] == item_name:
            item['amount'] += 1
            return
    for item in Shop_Catalogue:
        if item['item'] == item_name:
            Shop_Cart.append({"item name": item["item name"], "value": item["value"], "amount": 1})
            return
def Remove_From_Cart(item_name, Shop_Catalogue, Shop_Cart):
    for item in Shop_Cart:
        if item['item name'] == item_name:
            item['amount'] -= 1
            return
    for item in Shop_Catalogue:
        if item['item'] == item_name:
            Shop_Cart.pop({"item name": item["item name"], "value": item["value"], "amount": 1})
            return

def Button_Logic():
    global Run, Amount_Of_Eggs, Chicken_Stock, Meat_Stock, Shop_Open

    if Click_Btn.draw(Screen):
        Amount_Of_Eggs += 1

    if Exit_Btn.draw(Screen):
        Run = False

    if Add_Chick_Btn.draw(Screen):
        for nest in Nest_Surfaces:
            if not nest["occupied"] and Chicken_Stock > 0:
                Chickens.draw(nest["surface"])
                Chick_NPC.set_idle_egg_spawn_True()
                if not Chickens:
                    Chickens.add(Chick_NPC)
                    Chickens.draw(nest["surface"])
                    Chick_NPC.set_idle_egg_spawn_True()
                nest["occupied"] = True
                pygame.display.update()
                Chicken_Stock -= 1
                print("chic added")
                return

    if Kill_Chick_Btn.draw(Screen):
        for nest in Nest_Surfaces:
            if nest["occupied"]:
                Chick_NPC.kill()
                Chick_NPC.set_idle_egg_spawn_False()
                nest["occupied"] = False
                Chickens.update(nest["surface"])
                nest["surface"].fill('white')
                Chickens.update(nest["surface"])
                pygame.display.update()
                print("chic delete")
                return

    if Shop_Btn.draw(Screen):
        Shop_Open = True
        print("Shop opened")

    if Close_Shop_Window_Btn.draw(Screen):
        Shop_Open = False
        print("Shop closed")

    if Add_Chicken_to_cart_Btn.draw(Screen):
        Add_To_Cart("Chicken", Shop_Catalogue, Shop_Cart)
        print("Added Chicken")
    if Remove_Chicken_to_cart_Btn.draw(Screen) and Shop_Cart[1]['amount'] > 0:
        Remove_From_Cart("Chicken", Shop_Catalogue, Shop_Cart)
        print("Removed Chicken")
    if Add_Food_to_cart_Btn.draw(Screen):
        Add_To_Cart("Food", Shop_Catalogue, Shop_Cart)
        print("Added Food")
    if Remove_Food_to_cart_Btn.draw(Screen) and Shop_Cart[0]['amount'] > 0:
        Remove_From_Cart("Food", Shop_Catalogue, Shop_Cart)
        print("Removed Food")

    if Buy_Btn.draw(Screen):
        # supposed to take all amount of items from cart to inventory and take the money from wallet
        pass

def Main_Screen_Text():
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

def Shop_Window_Text():
    global Shop_Catalogue, Shop_Cart

    Font_Name = 'NeueBit' #Ask teacher about this problem, python fails to identify bold version of installed font
    Body_Font_Size = 32
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    Body_Line1_Value_Chicken = Body_Font.render(f'{Shop_Cart[1]["value"]}$', True, ('black'))
    Body_Line1_Amount_Chicken = Body_Font.render(f'{Shop_Cart[1]["amount"]}x', True, ('black'))
    Body_Line2_Value_Food = Body_Font.render(f'{Shop_Cart[0]["value"]}$', True, ('black'))
    Body_Line2_Amount_Food = Body_Font.render(f'{Shop_Cart[0]["amount"]}x', True, ('black'))
    Body_Final_Price = Body_Font.render(f'{((Shop_Cart[1]["amount"])*(Shop_Cart[1]["value"])+(Shop_Cart[0]["amount"])*(Shop_Cart[0]["value"]))}$', True, ('black'))

    Screen.blit(Body_Line1_Value_Chicken, (356, 122))
    Screen.blit(Body_Line1_Amount_Chicken, (404, 123))
    Screen.blit(Body_Line2_Value_Food, (356, 158))
    Screen.blit(Body_Line2_Amount_Food, (404, 159))
    Screen.blit(Body_Final_Price, (391, 205))

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
    global Run, fps, blit, Amount_Of_Eggs, Shop_Open

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Screen.fill(('white'))

        Chick_NPC.idle_egg_spawn()

        Main_Screen_Text()
        Button_Logic()

        pygame.Surface.blit(Screen, Nest_Surface_1, (42, 82))
        pygame.Surface.blit(Screen, Nest_Surface_2, (264, 82))
        pygame.Surface.blit(Screen, Nest_Surface_3, (486, 82))

        Chickens.update()

        System_Buttons.update()
        System_Buttons.draw(Screen)

        Shop_Window_UI.update()
        if Shop_Open:
            Shop_Window_UI.update()
            Shop_Window_UI.draw(Screen)
            Shop_Window_Text()

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()