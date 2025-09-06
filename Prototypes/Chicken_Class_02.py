import pygame, random
from Inventory import Inventory, Score

class Chicken_Class(pygame.sprite.Sprite):
    def __init__(self, x, y, image, scale, max_hp, egg_spawn: bool = False):
        pygame.sprite.Sprite.__init__(self)
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale),(height*scale)))
        self.rect = image.get_rect()
        self.rect.topleft = (x, y)
        self.max_hp = max_hp
        self.hunger_level = self.max_hp
        self.egg_spawn = egg_spawn

    # Egg spawn system
    def set_idle_egg_spawn_True(self):
        self.egg_spawn = True
    def set_idle_egg_spawn_False(self):
        self.egg_spawn = False
    def idle_egg_spawn(self):
        global Inventory, Score

        Egg_Spawn_Delay = 5000  # egg spawn, short for testing purpose, change later
        Get_Time = pygame.time.get_ticks()

        if not hasattr(self, "Next_Egg_Spawn_Update"):
            self.Next_Egg_Spawn_Update = Get_Time + 5000

        if self.egg_spawn == True and (self.Next_Egg_Spawn_Update < Get_Time):
            Possible_Amount_Eggs = (1, 0, 2, 0, 3) # zeroes added to introduce randomness into the spawn, without creating a whole random system, maybe I will make one in a future when everything else is done and I have time
            Random_Amount_Eggs = random.choice(Possible_Amount_Eggs)
            Inventory[3]['amount'] += Random_Amount_Eggs
            Score['points'] += 1
            self.Next_Egg_Spawn_Update = Get_Time + Egg_Spawn_Delay

    # Hunger system
    def hunger_meter_decrease(self):

        Hunger_Interval_Delay = 5000
        Get_Time = pygame.time.get_ticks()

        if not hasattr(self, "Next_Hunger_Point_Update"):
            self.Next_Hunger_Point_Update = Get_Time + 5000

        if self.hunger_level > 1 and (self.Next_Hunger_Point_Update < Get_Time): # it should stop at 1HP, and stop the idle egg spawn, until the chicken is fed
            self.Next_Hunger_Point_Update = Get_Time + Hunger_Interval_Delay
            self.hunger_level -= 1
            if self.hunger_level == 1:
                self.egg_spawn = False

    def hunger_meter_increase(self):
        global Inventory

        if self.hunger_level < self.max_hp: #max hunger, set to 50 for now
            self.hunger_level = self.max_hp
            return

