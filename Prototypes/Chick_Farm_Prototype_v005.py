import pygame, random
from Button_Class_03 import Button_Class
from Chicken_Class_02 import Chicken_Class
from Inventory import Shop_Catalogue, Shop_Cart, Sell_Cart, Inventory

pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('ChickFarm!!!')
Screen.fill(('white'))

fps = pygame.time.Clock()
img = pygame.image.load # I'm lazy
blit = pygame.Surface.blit # I'm very lazy
Font_Name = 'VT323'  # Font used in the game

# Custom sprite class for blank windows, that work as paddings for text
class Custom_Sprite(pygame.sprite.Sprite): #should I separate all classes into separate file?
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

# Images for sprites and other graphic elements # Maybe separate those too
Exit_Img = img('Assets/UI/Btn_Def_Exit.png').convert_alpha()
Score_Img = img('Assets/UI/Score.png').convert_alpha()
Chick_Img = img('Assets/Aseprite files/Chicken.png').convert_alpha()
Add_Chick_Img = img('Assets/UI batch 02/Btn_Def_AddChick.png').convert_alpha()
Kill_Chick_Img = img('Assets/UI batch 02/Btn_Def_KillChick.png').convert_alpha()
Shop_Btn_Img = img('Assets/UI batch 02/Btn_Def_Shop.png').convert_alpha()
Shop_Window_Img = img('Assets/UI batch 02/Shop_Window_Clean.png').convert_alpha()
Add_to_cart_Btn_Img = img('Assets/UI batch 02/Add_to_cart_Btn.png').convert_alpha()
Remove_from_cart_Btn_Img = img('Assets/UI batch 02/Minus_from_cart_Btn.png').convert_alpha()
Close_Window_Btn_Img = img('Assets/UI batch 02/Close_Window_Btn.png').convert_alpha()
Buy_Btn_Img = img('Assets/UI batch 02/Buy_Btn.png').convert_alpha()
Chicken_Counter_Img = img('Assets/UI batch 02/Chicken_Counter.png').convert_alpha()
Egg_Counter_Img = img('Assets/UI batch 02/Egg_Counter.png').convert_alpha()
Money_Counter_Img = img('Assets/UI batch 02/Money_Counter.png').convert_alpha()
Market_Btn_Img = img('Assets/UI batch 02/Btn_Def_Market.png').convert_alpha()
Inventory_Btn_Img = img('Assets/UI batch 02/Btn_Def_Inventory.png').convert_alpha()
Inventory_Window_Img = img('Assets/UI batch 02/Inventory_Window_Clean.png').convert_alpha()
Close_Inv_Btn_Img = img('Assets/UI batch 02/Close_Window_Btn.png').convert_alpha()
Sell_Btn_Img = img('Assets/UI batch 02/Sell_Btn.png').convert_alpha()
Market_Window_Clean_Img = img('Assets/UI batch 02/Market_Window_Clean.png').convert_alpha()
Feed_Btn_Img = img('Assets/UI batch 02/Btn_Def_Feed.png').convert_alpha()

# Main control buttons
Exit_Btn = Button_Class(112, 270, Exit_Img, 1)
Add_Chick_Btn = Button_Class(184, 270, Add_Chick_Img, 1)
Kill_Chick_Btn = Button_Class(256, 270, Kill_Chick_Img, 1)
Shop_Btn = Button_Class(328, 270, Shop_Btn_Img, 1)
Market_Btn = Button_Class(400, 270, Market_Btn_Img, 1)
Inv_Btn = Button_Class(472, 270, Inventory_Btn_Img, 1)
Feed_Btn = Button_Class(544, 270, Feed_Btn_Img, 1)
# Shop window controls
Add_Chicken_to_cart_Btn = Button_Class(462, 120, Add_to_cart_Btn_Img, 1)
Add_Food_to_cart_Btn = Button_Class(462, 154, Add_to_cart_Btn_Img, 1)
Remove_Chicken_to_cart_Btn = Button_Class(494, 120, Remove_from_cart_Btn_Img, 1)
Remove_Food_to_cart_Btn = Button_Class(494, 154, Remove_from_cart_Btn_Img, 1)
Close_Shop_Window_Btn = Button_Class(196, 81, Close_Window_Btn_Img, 1)
Buy_Btn = Button_Class(316, 235, Buy_Btn_Img, 1)
# Market window controls
Sell_Btn = Button_Class(316, 235, Sell_Btn_Img, 1)
Add_Meat_to_Sell_Btn = Button_Class(462, 120, Add_to_cart_Btn_Img, 1)
Add_Eggs_to_Sell_Btn = Button_Class(462, 154, Add_to_cart_Btn_Img, 1)
Remove_Meat_to_Sell_Btn = Button_Class(494, 120, Remove_from_cart_Btn_Img, 1)
Remove_Eggs_to_Sell_Btn = Button_Class(494, 154, Remove_from_cart_Btn_Img, 1)
Close_Market_Window_Btn = Button_Class(196, 81, Close_Window_Btn_Img, 1)
# Inventory window controls
Close_Inv_Btn = Button_Class(196, 96, Close_Inv_Btn_Img, 1)

# Custom sprites
Shop_Window = Custom_Sprite(Shop_Window_Img, 180, 65)
Egg_Counter = Custom_Sprite(Egg_Counter_Img, 108, 16)
Chicken_Counter = Custom_Sprite(Chicken_Counter_Img, 276, 16)
Money_Counter = Custom_Sprite(Money_Counter_Img, 441, 16)
Inventory_Window = Custom_Sprite(Inventory_Window_Img, 180, 80)
Market_Window = Custom_Sprite(Market_Window_Clean_Img, 180, 65)

# Main control buttons sprite group
System_Buttons = pygame.sprite.Group()
System_Buttons.add(Exit_Btn, Add_Chick_Btn, Kill_Chick_Btn, Shop_Btn,Market_Btn, Inv_Btn, Feed_Btn)
# Shop window sprite group
Shop_Window_UI = pygame.sprite.Group()
Shop_Window_UI.add(Shop_Window, Add_Chicken_to_cart_Btn, Add_Food_to_cart_Btn, Remove_Chicken_to_cart_Btn, Remove_Food_to_cart_Btn, Close_Shop_Window_Btn, Buy_Btn)
# Market window sprite group
Market_Window_UI = pygame.sprite.Group()
Market_Window_UI.add(Market_Window, Add_Eggs_to_Sell_Btn, Add_Meat_to_Sell_Btn, Remove_Meat_to_Sell_Btn, Remove_Eggs_to_Sell_Btn, Close_Market_Window_Btn, Sell_Btn)
# Main screen counters sprite group
Counters_UI = pygame.sprite.Group()
Counters_UI.add(Egg_Counter, Chicken_Counter, Money_Counter)
# Inventory window sprite group
Inventory_Window_UI = pygame.sprite.Group()
Inventory_Window_UI.add(Inventory_Window, Close_Inv_Btn)
# Nest surfaces
Nest_Surface_1 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_2 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_3 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
# Nest Surface dict with custom "flag"
Nest_Surfaces = [ # occupied is a check whether the surface is taken by chicken sprite
    {"surface":Nest_Surface_1, "occupied":False, "object":None, "visibility":False, "hp_pos":(114,79)},
    {"surface":Nest_Surface_2, "occupied":False, "object":None, "visibility":False, "hp_pos":(336,79)},
    {"surface":Nest_Surface_3, "occupied":False, "object":None, "visibility":False, "hp_pos":(558,79)}
]

# Bools for running a game
Inventory_Open = False
Shop_Open = False
Market_Open = False
HP_Text_Visibility = False
Run = True

# Window manager support functions
Current_Window = "Main"

def Buttons_State_Checker(sprite_group, class_name, window): # checks which sprites are related to button class and blocks them from being clickable
    # sprite_group = the sprite group that contains buttons we need to block,
    # class_name = just in case if there will be other classes besides button, that I want to block,
    # window = the name of the window in which buttons are supposed to work
    for sprite in sprite_group:
        if isinstance(sprite, class_name):
            sprite.locked = (Current_Window != window)

# Shop support functions
def Add_To_Cart(item_name):
    global  Shop_Catalogue, Shop_Cart
    for item in Shop_Cart:
        final_item_price = item['amount'] * item['value']
        if item['item name'] == item_name and final_item_price <= Inventory[4]['amount']:
            item['amount'] += 1
            return
    for item in Shop_Catalogue:
        if item['item name'] == item_name and final_item_price <= Inventory[4]['amount']:
            Shop_Cart.append({"item name": item["item name"], "value": item["value"], "amount": 1})
            return

def Remove_From_Cart(item_name):
    global Shop_Catalogue, Shop_Cart
    for item in Shop_Cart:
        if item['item name'] == item_name:
            item['amount'] -= 1
            return
    for item in Shop_Catalogue:
        if item['item name'] == item_name:
            Shop_Cart.pop({"item name": item["item name"], "value": item["value"], "amount": 1})
            return

def Buy_From_Cart():
    global Inventory, Shop_Cart

    for cart_item in Shop_Cart:
        final_item_price = cart_item['amount'] * cart_item['value']
        if cart_item['amount'] > 0 and final_item_price <= Inventory[4]['amount']:
                Inventory[4]['amount'] -= final_item_price

                for inventory_item in Inventory:
                    if inventory_item['item name'] == cart_item['item name']:
                        inventory_item['amount'] += cart_item ['amount']
                        cart_item ['amount'] = 0
                        break

                print('money taken')

# Market support functions
def Add_To_Sell_Cart(item_name, required_amount): # Right now it can add infinite amount of items instead of tracking the inventory
    global  Inventory, Sell_Cart
    for inv_item in Inventory:
        if inv_item['item name'] == item_name:
            if inv_item['amount'] < required_amount:
                print("no item to sell")
                return

            inv_item['amount'] -= required_amount

            for sell_item in Sell_Cart:
                if sell_item['item name'] == item_name:
                    sell_item['amount'] += required_amount
                    print ('item put to sale')
                    return

            Sell_Cart.append({"item name": item_name, "value": inv_item['value'], "amount": required_amount})

def Remove_From_Sell_Cart(item_name, required_amount):
    global Inventory, Sell_Cart
    for sell_item in Sell_Cart:
        if sell_item['item name'] == item_name:
            if sell_item['amount'] != 0:
                if sell_item['amount'] < required_amount:
                    return

                sell_item['amount'] -= required_amount

                for inv_item in Inventory:
                    if inv_item['item name'] == item_name:
                        if sell_item['amount'] > 0:
                            inv_item['amount'] += required_amount
                            print('item returned')
                            return

                        inv_item['amount'] += required_amount
                        print('item returned')

                Inventory.append({"item name": item_name, "value": inv_item['value'], "amount": required_amount})

def Sell_All_From_Sell_Cart():
    global Inventory, Sell_Cart
    for sell_item in Sell_Cart:
        Final_Price = (sell_item['amount'] * sell_item['value'])
        Inventory[4]['amount'] += Final_Price
        sell_item['amount'] = 0
        print("items sold")

# Chicken spawn logic
def Chicken_Spawn(): #Should make a unique chicken everytime used and conditions are met
    global Inventory, Nest_Surfaces

    for nest in Nest_Surfaces:
        if not nest["occupied"] and Inventory[1]["amount"] > 0:

            nest['object'] = Chicken_Class(0, 0, Chick_Img, 1, 30)
            nest['visibility'] = True
            nest['object'].set_idle_egg_spawn_True()
            nest['occupied'] = True

            Chickens.add(nest['object'])
            Chickens.draw(nest["surface"])
            pygame.display.update()

            Inventory[1]["amount"] -= 1
            print("chic added")
            return

def Chicken_Remove():
    global Inventory, Nest_Surfaces

    for nest in Nest_Surfaces:
        if nest["occupied"] and nest["object"] is not None:

            nest["object"].set_idle_egg_spawn_False()

            nest["object"] = None
            nest["visibility"] = False
            nest["occupied"] = False

            nest["surface"].fill('white')
            pygame.display.update()

            Inventory[2]['amount'] += 1
            print("chic delete")
            return

def Chicken_Class_Objects_Update():
    for chicken in Nest_Surfaces:
        if chicken['object'] != None:
            chicken['object'].idle_egg_spawn()
            chicken['object'].hunger_meter_decrease()

# Buttons functions
def Button_Logic():
    global Run, Inventory, Shop_Open, Inventory_Open, Market_Open, Current_Window, HP_Text_Visibility
    # Main screen menu buttons
    if Exit_Btn.draw(Screen):
        Run = False
    if Add_Chick_Btn.draw(Screen):
        Chicken_Spawn()
    if Kill_Chick_Btn.draw(Screen):
        Chicken_Remove()
    # Shop
    if Shop_Btn.draw(Screen):
        Shop_Open = True
        Current_Window = "Shop"
        print(Current_Window)
        print("Shop opened")
    if Close_Shop_Window_Btn.draw(Screen):
        Shop_Open = False
        Current_Window = "Main"
        print(Current_Window)
        print("Shop closed")
    if Add_Chicken_to_cart_Btn.draw(Screen):
        Add_To_Cart("Chicken")
        print("Added Chicken")
    if Remove_Chicken_to_cart_Btn.draw(Screen) and Shop_Cart[1]['amount'] > 0:
        Remove_From_Cart("Chicken")
        print("Removed Chicken")
    if Add_Food_to_cart_Btn.draw(Screen):
        Add_To_Cart("Food")
        print("Added Food")
    if Remove_Food_to_cart_Btn.draw(Screen) and Shop_Cart[0]['amount'] > 0:
        Remove_From_Cart("Food")
        print("Removed Food")
    if Buy_Btn.draw(Screen):
        Buy_From_Cart()
        print("Item bought")
        pass
    # Inventory
    if Inv_Btn.draw(Screen):
        Inventory_Open = True
        Current_Window = "Inventory"
        print ("Inventory opened")
    if Close_Inv_Btn.draw(Screen):
        Inventory_Open = False
        Current_Window = "Main"
        print("Inventory closed")
    # Market
    if Market_Btn.draw(Screen):
        Market_Open = True
        Current_Window = "Market"
        print("Market opened")
    if Close_Market_Window_Btn.draw(Screen):
        Market_Open = False
        Current_Window = "Main"
        print("Market closed")
    if Add_Meat_to_Sell_Btn.draw(Screen):
        Add_To_Sell_Cart("Meat", 1)
        #print("Put to sell Chicken")
    if Remove_Meat_to_Sell_Btn.draw(Screen):
        Remove_From_Sell_Cart("Meat", 1)
        #print("Removed Chicken")
    if Add_Eggs_to_Sell_Btn.draw(Screen):
        Add_To_Sell_Cart("Eggs", 6)
        #print("Put to sell Food")
    if Remove_Eggs_to_Sell_Btn.draw(Screen):
        Remove_From_Sell_Cart("Eggs", 6)
        #print("Removed Food")
    if Sell_Btn.draw(Screen):
        Sell_All_From_Sell_Cart()

    if Feed_Btn.draw(Screen):
        if Inventory[0]['amount'] > 0:
            Inventory[0]['amount'] -= 1
            for chicken in Nest_Surfaces:
                if chicken['object'] != None:
                    chicken['object'].hunger_meter_increase()
            print('chicken being fed')
            return

# Text functions
def Counters_Text():
    global Font_Name, Inventory

    Font_Size = 32 # new font size for counters
    Body_Font = pygame.font.SysFont(Font_Name, Font_Size)
    # Names of counters
    Egg_Counter_Title_Text = Body_Font.render('Eggs:', True, ('black'))
    Chicken_Counter_Title_Text = Body_Font.render('Chix:', True, ('black'))
    Bank_Counter_Title_Text = Body_Font.render('Bank:', True, ('black'))
    # Data of counters
    Egg_Counter_Text = Body_Font.render(f'{Inventory[3]["amount"]}', True, ('black'))
    Chicken_Counter_Text = Body_Font.render(f'{Inventory[1]["amount"]}', True, ('black'))
    Bank_Wallet_Counter_Text = Body_Font.render(f'{Inventory[4]["amount"]}$', True, ('black'))

    Screen.blit(Egg_Counter_Title_Text, (124, 28))
    Screen.blit(Chicken_Counter_Title_Text, (294, 28))
    Screen.blit(Bank_Counter_Title_Text, (457, 28))

    Screen.blit(Egg_Counter_Text, (190, 28))
    Screen.blit(Chicken_Counter_Text, (355, 28))
    Screen.blit(Bank_Wallet_Counter_Text, (525, 28))

def Shop_Window_Text():
    global Shop_Catalogue, Shop_Cart, Font_Name

    Body_Font_Size = 32
    H1_Font_Size = 44
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Shop_Window_Tile = H1_Font.render(f'SHOP', True, ('black'))
    # Name
    Body_Line1_Name_Chicken = Body_Font.render(f'Chicken', True, ('black'))
    Body_Line2_Name_Food = Body_Font.render(f'Chick food', True, ('black'))
    Body_Final_Name_Money = Body_Font.render(f'Final price:', True, ('black'))
    # Price
    Body_Line1_Value_Chicken = Body_Font.render(f'{Shop_Cart[1]["value"]}$', True, ('black'))
    Body_Line2_Value_Food = Body_Font.render(f'{Shop_Cart[0]["value"]}$', True, ('black'))
    # Amount
    Body_Line1_Amount_Chicken = Body_Font.render(f'{Shop_Cart[1]["amount"]}x', True, ('black'))
    Body_Line2_Amount_Food = Body_Font.render(f'{Shop_Cart[0]["amount"]}x', True, ('black'))
    # Final price
    Body_Final_Price = Body_Font.render(f'{((Shop_Cart[1]["amount"])*(Shop_Cart[1]["value"])+(Shop_Cart[0]["amount"])*(Shop_Cart[0]["value"]))}$', True, ('black'))

    Screen.blit(Shop_Window_Tile, (323, 72))
    Screen.blit(Body_Line1_Name_Chicken, (196, 118))
    Screen.blit(Body_Line2_Name_Food, (196, 152))
    Screen.blit(Body_Line1_Value_Chicken, (356, 118))
    Screen.blit(Body_Line1_Amount_Chicken, (404, 118))
    Screen.blit(Body_Line2_Value_Food, (356, 152))
    Screen.blit(Body_Line2_Amount_Food, (404, 152))
    Screen.blit(Body_Final_Name_Money, (232, 200))
    Screen.blit(Body_Final_Price, (391, 200))

def Market_Window_Text():
    global Shop_Catalogue, Shop_Cart, Font_Name

    Body_Font_Size = 32
    H1_Font_Size = 44
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Shop_Window_Tile = H1_Font.render(f'MARKET', True, ('black'))
    # Name
    Body_Line1_Name_Meat = Body_Font.render(f'Meat', True, ('black'))
    Body_Line2_Name_Eggs = Body_Font.render(f'6 eggs', True, ('black'))
    Body_Final_Name_Money = Body_Font.render(f'Final price:', True, ('black'))
    # Price
    Body_Line1_Value_Meat = Body_Font.render(f'{Sell_Cart[0]["value"]}$', True, ('black'))
    Body_Line2_Value_Eggs = Body_Font.render(f'{Sell_Cart[1]["value"]}$', True, ('black'))
    # Amount
    Body_Line1_Amount_Meat = Body_Font.render(f'{Sell_Cart[0]["amount"]}x', True, ('black'))
    Body_Line2_Amount_Eggs = Body_Font.render(f'{Sell_Cart[1]["amount"]}x', True, ('black'))
    # Final price
    Body_Final_Price = Body_Font.render(f'{((Sell_Cart[1]["amount"])*(Sell_Cart[1]["value"])+(Sell_Cart[0]["amount"])*(Sell_Cart[0]["value"]))}$', True, ('black'))

    Screen.blit(Shop_Window_Tile, (323, 72))
    Screen.blit(Body_Line1_Name_Meat, (196, 118))
    Screen.blit(Body_Line2_Name_Eggs, (196, 152))
    Screen.blit(Body_Line1_Value_Meat, (320, 118))
    Screen.blit(Body_Line1_Amount_Meat, (404, 118))
    Screen.blit(Body_Line2_Value_Eggs, (320, 152))
    Screen.blit(Body_Line2_Amount_Eggs, (404, 152))
    Screen.blit(Body_Final_Name_Money, (232, 200))
    Screen.blit(Body_Final_Price, (391, 200))

def Inventory_Window_Text():
    global Font_Name, Inventory

    Body_Font_Size = 24
    H1_Font_Size = 44
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Inventory_Window_Title = H1_Font.render(f'INVENTORY', True, ('black'))
    # Name
    Body_Name_Eggs = Body_Font.render('Eggs', True, ('black'))
    Body_Name_Chicken = Body_Font.render('Chicken', True, ('black'))
    Body_Name_Food = Body_Font.render('Chick food', True, ('black'))
    Body_Name_Meat = Body_Font.render('Meat Stock', True, ('black'))
    Body_Name_Money = Body_Font.render('Money:',True, ('black'))
    # Amounts
    Body_Line1_Eggs = Body_Font.render(f'{Inventory[3]["amount"]}x', True, ('black'))
    Body_Line2_Chicken = Body_Font.render(f'{Inventory[1]["amount"]}x', True, ('black'))
    Body_Line3_Food = Body_Font.render(f"{Inventory[0]['amount']}x", True, ('black'))
    Body_Line4_Meat = Body_Font.render(f'{Inventory[2]["amount"]}x', True, ('black'))
    # Price
    Body_Line1_Eggs_Value = Body_Font.render(f'{Inventory[3]["value"]}$', True, ('black'))
    Body_Line2_Chicken_Value = Body_Font.render(f'{Inventory[1]["value"]}$', True, ('black'))
    Body_Line3_Food_Value = Body_Font.render(f'{Inventory[0]["value"]}$', True, ('black'))
    Body_Line4_Meat_Value = Body_Font.render(f'{Inventory[2]["value"]}$', True, ('black'))
    # Money
    Body_Line5_Money = Body_Font.render(f'{Inventory[4]["amount"]}$',True, ('black'))

    Screen.blit(Inventory_Window_Title, (282, 84))
    Screen.blit(Body_Name_Eggs, (196, 132))
    Screen.blit(Body_Name_Chicken, (196, 156))
    Screen.blit(Body_Name_Food, (196, 180))
    Screen.blit(Body_Name_Meat, (196, 204))
    Screen.blit(Body_Line1_Eggs, (499, 132))
    Screen.blit(Body_Line2_Chicken, (499, 156))
    Screen.blit(Body_Line3_Food, (499, 180))
    Screen.blit(Body_Line4_Meat, (499, 204))
    Screen.blit(Body_Line1_Eggs_Value, (390, 132))
    Screen.blit(Body_Line2_Chicken_Value, (390, 156))
    Screen.blit(Body_Line3_Food_Value, (390, 180))
    Screen.blit(Body_Line4_Meat_Value, (390, 204))
    Screen.blit(Body_Name_Money, (308, 240))
    Screen.blit(Body_Line5_Money, (368, 240))

def Hunger_Points_Counter_Text():
    global Chicken_Class, Nest_Surfaces

    Font_Size = 32
    Body_Font = pygame.font.SysFont(Font_Name, Font_Size)

    for nest in Nest_Surfaces:
        if nest['object'] is not None and nest['visibility']:
            Max_HP = nest['object'].max_hp
            Current_HP = nest['object'].hunger_level
            Chicken_HP_Meter = Body_Font.render(f"{Current_HP}/{Max_HP}", True, 'black')
            Screen.blit(Chicken_HP_Meter, nest['hp_pos'])
            #print('HP')

# Chicken class
Chick_NPC = Chicken_Class(0,0, Chick_Img, 1, 50)

Chickens = pygame.sprite.Group()
Chickens.add(Chick_NPC)

# Main loop
def main():
    global Run, fps, blit, Shop_Open, Inventory_Open, Current_Window

    while Run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Run = False

        Screen.fill(('white'))

        #Counters_UI.update()
        #Counters_UI.draw(Screen)
        Counters_Text()

        Button_Logic()

        pygame.Surface.blit(Screen, Nest_Surface_1, (42, 82))
        pygame.Surface.blit(Screen, Nest_Surface_2, (264, 82))
        pygame.Surface.blit(Screen, Nest_Surface_3, (486, 82))

        Chickens.update()
        Chicken_Class_Objects_Update()
        Hunger_Points_Counter_Text()

        System_Buttons.update()
        System_Buttons.draw(Screen)
        Buttons_State_Checker(System_Buttons, Button_Class, "Main")

        if Shop_Open:
            Shop_Window_UI.update()
            Shop_Window_UI.draw(Screen)
            Shop_Window_Text()
        Buttons_State_Checker(Shop_Window_UI, Button_Class, "Shop")

        if Inventory_Open:
            Inventory_Window_UI.update()
            Inventory_Window_UI.draw(Screen)
            Inventory_Window_Text()
        Buttons_State_Checker(Inventory_Window_UI, Button_Class, "Inventory")

        if Market_Open:
            Market_Window_UI.update()
            Market_Window_UI.draw(Screen)
            Market_Window_Text()
        Buttons_State_Checker(Market_Window_UI, Button_Class, "Market")

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()