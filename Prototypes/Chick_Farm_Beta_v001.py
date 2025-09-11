import pygame, random, json, sys
from Button_Class_03 import Button_Class
from Chicken_Class_02 import Chicken_Class

pygame.init()

Window_Width, Window_Height = 720, 360
Screen = pygame.display.set_mode((Window_Width, Window_Height))
pygame.display.set_caption('ChickFarm!!!')
Screen.fill(('white'))

fps = pygame.time.Clock()
img = pygame.image.load # I'm lazy
blit = pygame.Surface.blit # I'm very lazy
Font_Name = 'VT323'  # Font used in the game

# Images for sprites and other graphic elements
## Main
Exit_Img = img('Assets/UI batch 03/Quit_Btn.png').convert_alpha()
Chick_Img = img('Assets/Aseprite files/Chicken.png').convert_alpha()
Add_Chick_Img = img('Assets/UI batch 03/Add_Btn.png').convert_alpha()
Kill_Chick_Img = img('Assets/UI batch 03/Kill_Btn.png').convert_alpha()
Shop_Btn_Img = img('Assets/UI batch 03/Shop_Btn.png').convert_alpha()
Market_Btn_Img = img('Assets/UI batch 03/Market_Btn.png').convert_alpha()
Inventory_Btn_Img = img('Assets/UI batch 03/Inventory_Btn.png').convert_alpha()
Feed_Btn_Img = img('Assets/UI batch 03/Feed_Btn.png').convert_alpha()
Main_Screen_BG_Img = img('Assets/UI batch 03/Main_BG.png').convert_alpha()
Menu_Btn_Img = img('Assets/UI batch 03/Menu_Btn.png').convert_alpha()
## Menu
Save_Btn_Img = img('Assets/UI batch 03/Save_Btn.png').convert_alpha()
Load_Btn_Img = img('Assets/UI batch 03/Load_Btn.png').convert_alpha()
Exit_Btn_Img = img('Assets/UI batch 03/Exit_Btn.png').convert_alpha()
Menu_BG_Img = img('Assets/UI batch 03/Menu_BG.png').convert_alpha()
Menu_Window_Img = img('Assets/UI batch 03/Menu_Window_Clean.png').convert_alpha()
## Shop
Shop_Window_Img = img('Assets/UI batch 03/Shop_Window_Clean.png').convert_alpha()
Buy_Btn_Img = img('Assets/UI batch 03/Buy_Btn.png').convert_alpha()
Shop_BG_Img = img('Assets/UI batch 03/Shop_BG.png').convert_alpha()
## Inventory
Inventory_Window_Img = img('Assets/UI batch 03/Inventory_Window_Clean.png').convert_alpha()
Inventory_BG_Img = img('Assets/UI batch 03/Inventory_BG.png').convert_alpha()
## Market
Market_Window_Clean_Img = img('Assets/UI batch 03/Market_Window_Clean.png').convert_alpha()
Market_BG_Img = img('Assets/UI batch 03/Market_BG.png').convert_alpha()
Sell_Btn_Img = img('Assets/UI batch 03/Sell_Btn.png').convert_alpha()
## General purpose
Close_Window_Btn_Img = img('Assets/UI batch 03/Close_Btn.png').convert_alpha()
Add_to_cart_Btn_Img = img('Assets/UI batch 03/Add_Cart_Btn.png').convert_alpha()
Remove_from_cart_Btn_Img = img('Assets/UI batch 03/Remove_Cart_Btn.png').convert_alpha()
Chick_Icon_Img = img('Assets/UI batch 03/Chick_Icon.png').convert_alpha()
Food_Icon_Img = img('Assets/UI batch 03/Food_Icon.png').convert_alpha()
Meat_Icon_Img = img('Assets/UI batch 03/Meat_Icon.png').convert_alpha()
Eggs_Icon_Img = img('Assets/UI batch 03/Eggs_Icon.png').convert_alpha()
# Custom sprites
## Custom sprite class for blank windows, that work as paddings for text
class Custom_Sprite(pygame.sprite.Sprite): #should I separate all classes into separate file?
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
## Main
Main_Screen_BG = Custom_Sprite(Main_Screen_BG_Img, 0, 0)
## Menu
Menu_Window = Custom_Sprite(Menu_Window_Img, 208, 48)
Menu_BG = Custom_Sprite(Menu_BG_Img, 0, 0)
## Shop
Shop_Window = Custom_Sprite(Shop_Window_Img, 180, 55)
Shop_BG = Custom_Sprite(Market_BG_Img, 0, 0)
Chick_Icon_Shop = Custom_Sprite(Chick_Icon_Img, 196, 116)
Food_Icon_Shop = Custom_Sprite(Food_Icon_Img, 196, 158)
## Inventory
Inventory_Window = Custom_Sprite(Inventory_Window_Img, 208, 41)
Inventory_BG = Custom_Sprite(Inventory_BG_Img, 0, 0)
Eggs_Icon_Inv = Custom_Sprite(Eggs_Icon_Img, 240, 102)
Chick_Icon_Inv = Custom_Sprite(Chick_Icon_Img, 240, 142)
Food_Icon_Inv = Custom_Sprite(Food_Icon_Img, 240, 183)
Meat_Icon_Inv = Custom_Sprite(Meat_Icon_Img, 240, 224)
## Market
Market_Window = Custom_Sprite(Market_Window_Clean_Img, 180, 55)
Market_BG = Custom_Sprite(Market_BG_Img, 0, 0)
Meat_Icon_Market = Custom_Sprite(Meat_Icon_Img, 196, 116)
Eggs_Icon_Market = Custom_Sprite(Eggs_Icon_Img, 196, 158)
# Buttons
## Main screen buttons
#Exit_Btn = Button_Class(8, 8, Exit_Img, 1)
Add_Chick_Btn = Button_Class(13, 281, Add_Chick_Img, 1)
Kill_Chick_Btn = Button_Class(185, 281, Kill_Chick_Img, 1)
Feed_Btn = Button_Class(357, 281, Feed_Btn_Img, 1)
Shop_Btn = Button_Class(529, 281, Shop_Btn_Img, 1)
Market_Btn = Button_Class(591, 281, Market_Btn_Img, 1)
Inv_Btn = Button_Class(653, 281, Inventory_Btn_Img, 1)
Menu_Btn = Button_Class(8, 8, Menu_Btn_Img, 1)
## Menu window controls
Save_Game_Btn = Button_Class(253, 124, Save_Btn_Img, 1)
Load_Game_Btn = Button_Class(253, 184, Load_Btn_Img, 1)
Exit_Game_Btn = Button_Class(253, 244, Exit_Btn_Img, 1)
Close_Menu_Window_Btn = Button_Class(224, 58, Close_Window_Btn_Img, 1)
## Shop window controls
Add_Chicken_to_cart_Btn = Button_Class(460, 115, Add_to_cart_Btn_Img, 1)
Add_Food_to_cart_Btn = Button_Class(460, 157, Add_to_cart_Btn_Img, 1)
Remove_Chicken_to_cart_Btn = Button_Class(490, 115, Remove_from_cart_Btn_Img, 1)
Remove_Food_to_cart_Btn = Button_Class(490, 157, Remove_from_cart_Btn_Img, 1)
Close_Shop_Window_Btn = Button_Class(196, 65, Close_Window_Btn_Img, 1)
Buy_Btn = Button_Class(255, 247, Buy_Btn_Img, 1)
## Market window controls
Sell_Btn = Button_Class(255, 247, Sell_Btn_Img, 1)
Add_Meat_to_Sell_Btn = Button_Class(460, 115, Add_to_cart_Btn_Img, 1)
Add_Eggs_to_Sell_Btn = Button_Class(460, 157, Add_to_cart_Btn_Img, 1)
Remove_Meat_to_Sell_Btn = Button_Class(490, 115, Remove_from_cart_Btn_Img, 1)
Remove_Eggs_to_Sell_Btn = Button_Class(490, 157, Remove_from_cart_Btn_Img, 1)
Close_Market_Window_Btn = Button_Class(196, 65, Close_Window_Btn_Img, 1)
## Inventory window controls
Close_Inv_Btn = Button_Class(224, 51, Close_Window_Btn_Img, 1)

# Sprite Groups
## Main control buttons sprite group
Main_BG = pygame.sprite.Group()
Main_BG.add(Main_Screen_BG)
Main_Screen_UI = pygame.sprite.Group()
Main_Screen_UI.add( Menu_Btn, Add_Chick_Btn, Kill_Chick_Btn, Shop_Btn, Market_Btn, Inv_Btn, Feed_Btn)
## Meny window sprite group
Menu_Window_UI = pygame.sprite.Group()
Menu_Window_UI.add(Menu_BG, Menu_Window, Save_Game_Btn, Load_Game_Btn, Exit_Game_Btn, Close_Menu_Window_Btn)
## Shop window sprite group
Shop_Window_UI = pygame.sprite.Group()
Shop_Window_UI.add(Shop_BG, Shop_Window, Add_Chicken_to_cart_Btn, Add_Food_to_cart_Btn, Remove_Chicken_to_cart_Btn, Remove_Food_to_cart_Btn, Close_Shop_Window_Btn, Buy_Btn, Chick_Icon_Shop, Food_Icon_Shop)
## Market window sprite group
Market_Window_UI = pygame.sprite.Group()
Market_Window_UI.add(Market_BG, Market_Window, Add_Eggs_to_Sell_Btn, Add_Meat_to_Sell_Btn, Remove_Meat_to_Sell_Btn, Remove_Eggs_to_Sell_Btn, Close_Market_Window_Btn, Sell_Btn, Meat_Icon_Market, Eggs_Icon_Market)
## Inventory window sprite group
Inventory_Window_UI = pygame.sprite.Group()
Inventory_Window_UI.add(Inventory_BG, Inventory_Window, Close_Inv_Btn, Eggs_Icon_Inv, Chick_Icon_Inv, Food_Icon_Inv, Meat_Icon_Inv)

# Nest surfaces
Nest_Surface_1 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_2 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
Nest_Surface_3 = pygame.Surface((192, 192), flags=pygame.SRCALPHA)
# Nest Surface dict with custom flags
Nest_Surfaces = [ # occupied is a check whether the surface is taken by chicken sprite
    {"surface":Nest_Surface_1, "occupied":False, "object":None, "visibility":False, "hp_pos":(114,79)},
    {"surface":Nest_Surface_2, "occupied":False, "object":None, "visibility":False, "hp_pos":(336,79)},
    {"surface":Nest_Surface_3, "occupied":False, "object":None, "visibility":False, "hp_pos":(558,79)}
]
# Nest surface data that extracts json friendly data for save file
def Get_Nest_Data():
    Nest_Data = []

    for nest in Nest_Surfaces:
        new_dict = {}

        new_dict["occupied"] = nest["occupied"]
        if nest['object'] is not None:
            new_dict["object"] = True
        else:
            new_dict["object"] = False
        new_dict["visibility"] = nest["visibility"]

        Nest_Data.append(new_dict)

    return Nest_Data

# Chicken HPs
Chicken_HP = [
    {'chicken_hp': None},
    {'chicken_hp': None},
    {'chicken_hp': None}
]
# Shop's catalogue
Shop_Catalogue = [
    {"item name":"Food", "value":2, "amount":9999},
    {"item name":"Chicken", "value":8, "amount":9999},
]
# Shop cart, a transition state between Catalogue and Inventory
Shop_Cart = [
    {"item name":"Food", "value":2, "amount":0},
    {"item name":"Chicken", "value":8, "amount":0},
]
# Sell cart, where player puts items for sale, before selling them
Sell_Cart = [
    {"item name":"Meat", "value":5, "amount":0},
    {"item name":"Eggs", "value":1, "amount":0},
]
# Inventory
Inventory = [   # Using indexes is uncomfortable buuuut I just want to make the game playable first, maybe then I will work on readability
    {"item name":"Food", "value":2, "amount":0}, #0
    {"item name":"Chicken", "value":8, "amount":3}, #1
    {"item name":"Meat", "value":5, "amount":0}, #2
    {"item name":"Eggs", "value":1, "amount":0}, #3
    {"item name":"Money", "value":1, "amount":10}, #4
]
# Score
Score = {'points': 0}

# Bools for running a game
Menu_Open = False
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

# Save data support functions
def Chicken_HP_Tracker():
    global Chicken_HP
    for i, nest in enumerate(Nest_Surfaces):
        if nest['object'] is not None and nest['visibility']:
            Chicken_HP[i][f'chicken_hp'] = nest['object'].hunger_level
            #print(Chicken_HP)

# Shop support functions
def Add_To_Cart(item_name):
    global  Shop_Catalogue, Shop_Cart
    total = sum(item["amount"] * item['value'] for item in Shop_Cart)
    for cart_item in Shop_Cart:
        if cart_item['item name'] == item_name:
            final_total = total + cart_item['value']
            if final_total <= Inventory[4]['amount']:
                cart_item['amount'] += 1
            return
    for shop_item in Shop_Catalogue:
        if shop_item['item name'] == item_name:
            if shop_item['value'] <= Inventory[4]['amount']:
                Shop_Cart.append({"item name": shop_item["item name"], "value": shop_item["value"], "amount": 1})
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
    global Inventory, Shop_Cart, Score

    for cart_item in Shop_Cart:
        final_item_price = cart_item['amount'] * cart_item['value']
        if cart_item['amount'] > 0 and final_item_price <= Inventory[4]['amount']:
                Inventory[4]['amount'] -= final_item_price
                Score['points'] += 1

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
    global Inventory, Sell_Cart, Score
    for sell_item in Sell_Cart:
        Final_Price = (sell_item['amount'] * sell_item['value'])
        Inventory[4]['amount'] += Final_Price
        sell_item['amount'] = 0
        Score['points'] += Final_Price // 4
        print("items sold")

# Chicken logic
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
    global Run, Inventory, Shop_Open, Inventory_Open, Market_Open, Menu_Open, Current_Window, HP_Text_Visibility, Score, Nest_Surfaces_Data, Chicken_HP, Chicken_Class
    # Main screen menu buttons
    #if Exit_Btn.draw(Screen):
    if Add_Chick_Btn.draw(Screen):
        Chicken_Spawn()
    if Kill_Chick_Btn.draw(Screen):
        Chicken_Remove()
        Score['points'] += 1
    if Feed_Btn.draw(Screen):
        if Inventory[0]['amount'] > 0:
            Inventory[0]['amount'] -= 1
            for chicken in Nest_Surfaces:
                if chicken['object'] != None:
                    chicken['object'].hunger_meter_increase()
                    Score['points'] += 1
            print('chicken being fed')
            return

    # Menu
    if Menu_Btn.draw(Screen):
        Menu_Open = True
        Current_Window = "Menu"
        print(Current_Window)
        print("Menu opened")
    if Save_Game_Btn.draw(Screen):
        Save_Data = [
            {'inventory_data': Inventory},
            {'score_data': Score},
            {'chicken_hp_data': Chicken_HP},
            {'nests_data': Get_Nest_Data()}
        ]

        with open('Chick_Farm_Save_Data.txt', 'w') as data_file:
            json.dump(Save_Data, data_file, indent=4)
            print(Save_Data)
            print('saved')

    if Load_Game_Btn.draw(Screen):
        try:
            with open('Chick_Farm_Save_Data.txt') as data_file:
                loaded_data = json.load(data_file)
                print('loaded')

            Inventory = loaded_data[0]['inventory_data']
            Score = loaded_data[1]['score_data']
            Chicken_HP = loaded_data[2]['chicken_hp_data']

            nest_data = loaded_data[3]['nests_data']

            if nest_data:
                for i, nest in enumerate(Nest_Surfaces):
                    nest['occupied'] = nest_data[i]['occupied']
                    nest['visibility'] = nest_data[i]['visibility']

                    if nest_data[i]['object']:
                        nest['object'] = Chicken_Class(0, 0, Chick_Img, 1, 30)
                        nest['object'].set_idle_egg_spawn_True()

                        print(nest['object'].hunger_level)

                        for data in Chicken_HP: # IT DOESNT WORK BUT THE DEADLINE IS CLOSE AND I NEED TO WRITE A PAPER, SO will fix it later
                            if nest['object'] is not None and data['chicken_hp'] is not None:
                                nest['object'].hunger_level = data['chicken_hp']

                                Chickens.add(nest['object'])
                                Chickens.draw(nest["surface"])

                                print(nest['object'].hunger_level)

                    else:
                        nest['object'] = None

        except FileNotFoundError:
            print('No file created yet')

    if Exit_Game_Btn.draw(Screen):
        Run = False
    if Close_Menu_Window_Btn.draw(Screen):
        Menu_Open = False
        Current_Window = "Main"

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

# Text functions
def Counters_Text():
    global Font_Name, Inventory

    Font_Size = 24
    Body_Font = pygame.font.SysFont(Font_Name, Font_Size)
    # Names of counters
    Egg_Counter_Title_Text = Body_Font.render('Eggs:', True, ('black'))
    Chicken_Counter_Title_Text = Body_Font.render('Chix:', True, ('black'))
    Bank_Counter_Title_Text = Body_Font.render('Bank:', True, ('black'))
    Score_Counter_Title = Body_Font.render('Score:', True, ('black'))
    # Data of counters
    Egg_Counter_Text = Body_Font.render(f'{Inventory[3]["amount"]}', True, ('black'))
    Chicken_Counter_Text = Body_Font.render(f'{Inventory[1]["amount"]}', True, ('black'))
    Bank_Wallet_Counter_Text = Body_Font.render(f'{Inventory[4]["amount"]}$', True, ('black'))
    Score_Counter_Text = Body_Font.render(f'{Score["points"]}', True, ('black'))

    Screen.blit(Egg_Counter_Title_Text, (99, 20))
    Screen.blit(Chicken_Counter_Title_Text, (234, 20))
    Screen.blit(Bank_Counter_Title_Text, (360, 20))
    Screen.blit(Score_Counter_Title, (506, 20))

    Screen.blit(Egg_Counter_Text, (156, 20))
    Screen.blit(Chicken_Counter_Text, (291, 20))
    Screen.blit(Bank_Wallet_Counter_Text, (418, 20))
    Screen.blit(Score_Counter_Text, (573, 20))

def Menu_Window_Text():
    global Font_Name

    H1_Font_Size = 44
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Menu_Window_Tile = H1_Font.render(f'MENU', True, ('black'))

    Screen.blit(Menu_Window_Tile, (325, 52))

def Shop_Window_Text():
    global Shop_Catalogue, Shop_Cart, Font_Name

    Body_Font_Size = 32
    H1_Font_Size = 44
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Shop_Window_Tile = H1_Font.render(f'SHOP', True, ('black'))
    # Name
    Body_Line1_Name_Chicken = Body_Font.render(f'Chick', True, ('black'))
    Body_Line2_Name_Food = Body_Font.render(f'Food', True, ('black'))
    Body_Final_Name_Money = Body_Font.render(f'Total:', True, ('black'))
    # Price
    Body_Line1_Value_Chicken = Body_Font.render(f'{Shop_Cart[1]["value"]}$', True, ('black'))
    Body_Line2_Value_Food = Body_Font.render(f'{Shop_Cart[0]["value"]}$', True, ('black'))
    # Amount
    Body_Line1_Amount_Chicken = Body_Font.render(f'{Shop_Cart[1]["amount"]}x', True, ('black'))
    Body_Line2_Amount_Food = Body_Font.render(f'{Shop_Cart[0]["amount"]}x', True, ('black'))
    # Final price
    Body_Final_Price = Body_Font.render(f'{((Shop_Cart[1]["amount"])*(Shop_Cart[1]["value"])+(Shop_Cart[0]["amount"])*(Shop_Cart[0]["value"]))}$', True, ('black'))

    Screen.blit(Shop_Window_Tile, (325, 59))
    Screen.blit(Body_Line1_Name_Chicken, (240, 116))
    Screen.blit(Body_Line2_Name_Food, (240, 157))
    Screen.blit(Body_Line1_Value_Chicken, (346, 116))
    Screen.blit(Body_Line1_Amount_Chicken, (410, 116))
    Screen.blit(Body_Line2_Value_Food, (346, 157))
    Screen.blit(Body_Line2_Amount_Food, (410, 157))
    Screen.blit(Body_Final_Name_Money, (291, 207))
    Screen.blit(Body_Final_Price, (377, 207))

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
    Body_Final_Name_Money = Body_Font.render(f'Total:', True, ('black'))
    # Price
    Body_Line1_Value_Meat = Body_Font.render(f'{Sell_Cart[0]["value"]}$', True, ('black'))
    Body_Line2_Value_Eggs = Body_Font.render(f'{Sell_Cart[1]["value"]}$', True, ('black'))
    # Amount
    Body_Line1_Amount_Meat = Body_Font.render(f'{Sell_Cart[0]["amount"]}x', True, ('black'))
    Body_Line2_Amount_Eggs = Body_Font.render(f'{Sell_Cart[1]["amount"]}x', True, ('black'))
    # Final price
    Body_Final_Price = Body_Font.render(f'{((Sell_Cart[1]["amount"])*(Sell_Cart[1]["value"])+(Sell_Cart[0]["amount"])*(Sell_Cart[0]["value"]))}$', True, ('black'))

    Screen.blit(Shop_Window_Tile, (308, 59))
    Screen.blit(Body_Line1_Name_Meat, (240, 116))
    Screen.blit(Body_Line2_Name_Eggs, (240, 158))
    Screen.blit(Body_Line1_Value_Meat, (346, 116))
    Screen.blit(Body_Line1_Amount_Meat, (410, 116))
    Screen.blit(Body_Line2_Value_Eggs, (346, 158))
    Screen.blit(Body_Line2_Amount_Eggs, (410, 158))
    Screen.blit(Body_Final_Name_Money, (290, 207))
    Screen.blit(Body_Final_Price, (377, 207))

def Inventory_Window_Text():
    global Font_Name, Inventory

    Body_Font_Size = 32
    H1_Font_Size = 44
    Body_Font = pygame.font.SysFont(Font_Name, Body_Font_Size)
    H1_Font = pygame.font.SysFont(Font_Name, H1_Font_Size)

    # Window title
    Inventory_Window_Title = H1_Font.render(f'INVENTORY', True, ('black'))
    # Name
    Body_Name_Eggs = Body_Font.render('Eggs', True, ('black'))
    Body_Name_Chicken = Body_Font.render('Chick', True, ('black'))
    Body_Name_Food = Body_Font.render('Food', True, ('black'))
    Body_Name_Meat = Body_Font.render('Meat', True, ('black'))
    Body_Name_Money = Body_Font.render('Money:',True, ('black'))
    # Amounts
    Body_Amount_Eggs = Body_Font.render(f'{Inventory[3]["amount"]}x', True, ('black'))
    Body_Amount_Chicken = Body_Font.render(f'{Inventory[1]["amount"]}x', True, ('black'))
    Body_Amount_Food = Body_Font.render(f"{Inventory[0]['amount']}x", True, ('black'))
    Body_Amount_Meat = Body_Font.render(f'{Inventory[2]["amount"]}x', True, ('black'))
    # Price
    Body_Value_Eggs = Body_Font.render(f'{Inventory[3]["value"]}$', True, ('black'))
    Body_Value_Chicken = Body_Font.render(f'{Inventory[1]["value"]}$', True, ('black'))
    Body_Value_Food = Body_Font.render(f'{Inventory[0]["value"]}$', True, ('black'))
    Body_Value_Meat = Body_Font.render(f'{Inventory[2]["value"]}$', True, ('black'))
    # Money
    Body_Line5_Money = Body_Font.render(f'{Inventory[4]["amount"]}$',True, ('black'))

    Screen.blit(Inventory_Window_Title, (283, 45))
    Screen.blit(Body_Name_Eggs, (284, 101))
    Screen.blit(Body_Name_Chicken, (284, 142))
    Screen.blit(Body_Name_Food, (284, 182))
    Screen.blit(Body_Name_Meat, (284, 223))

    Screen.blit(Body_Value_Eggs, (390, 101))
    Screen.blit(Body_Value_Chicken, (390, 142))
    Screen.blit(Body_Value_Food, (390, 182))
    Screen.blit(Body_Value_Meat, (390, 223))

    Screen.blit(Body_Amount_Eggs, (453, 101))
    Screen.blit(Body_Amount_Chicken, (453, 142))
    Screen.blit(Body_Amount_Food, (453, 182))
    Screen.blit(Body_Amount_Meat, (453, 223))

    Screen.blit(Body_Name_Money, (285, 272))
    Screen.blit(Body_Line5_Money, (371, 272))

def Hunger_Points_Counter_Text(): #HP do not appear when loading chicken from save data
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

        Button_Logic()

        pygame.Surface.blit(Screen, Nest_Surface_1, (42, 82))
        pygame.Surface.blit(Screen, Nest_Surface_2, (264, 82))
        pygame.Surface.blit(Screen, Nest_Surface_3, (486, 82))

        Chickens.update()
        Chicken_HP_Tracker()
        Chicken_Class_Objects_Update()
        Hunger_Points_Counter_Text()

        Main_BG.update()
        Main_BG.draw(Screen)
        Main_Screen_UI.update()
        Main_Screen_UI.draw(Screen)
        Counters_Text()
        Buttons_State_Checker(Main_Screen_UI, Button_Class, "Main")

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

        if Menu_Open:
            Menu_Window_UI.update()
            Menu_Window_UI.draw(Screen)
            Menu_Window_Text()
        Buttons_State_Checker(Menu_Window_UI, Button_Class, "Menu")

        pygame.display.update()
        fps = 60

    pygame.quit()

if __name__ == '__main__':
    main()