money = 25
shopping_catalogue = [
    {'item':'chicken', 'value':6, 'amount':6},
    {'item':'food', 'value':2, 'amount':12},
]
shopping_cart = []

if input == f"add {shopping_catalogue['item']}":
    shopping_catalogue.append(shopping_catalogue[0])