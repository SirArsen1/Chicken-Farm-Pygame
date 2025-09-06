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