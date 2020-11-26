class Food:
    pass
class Drink:
    pass
def newFood(name,price,quantity,weight):
    food = Food()
    food.name      = name
    food.price     = price
    food.quantity  = quantity
    food.weight    = weight
    return food
def newDrink(name,price,quantity,volume):
    drink = Drink()
    drink.name      = name
    drink.price     = price
    drink.quantity  = quantity
    drink.volume    = volume
    return drink
def printFood(food):
    print(f"{food.name:28}|{food.price:7}|{food.quantity:7}|{food.weight:7}|")
def printDrink(drink):
    print(f"{drink.name:28}|{drink.price:7}|{drink.quantity:7}|{drink.volume:7}|")

###############################################

f1 = newFood("Salata Vegetariana","71 Lei",20,"450 gr")
f2 = newFood("Cheesecake","55 Lei",15,"160 gr")

d1 = newDrink("Cappuccino","53 Lei",30,"340 ml")
d2 = newDrink("Cacao","41 Lei",40,"340 ml") 
#######################
printFood(f1)
printFood(f2)

printDrink(d1)
printDrink(d2)
