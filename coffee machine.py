from settings import MENU, resources


def report():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}ml")
    print(f"Money: {money}$")


def check_resources(user_coffee):
    current_water = MENU[user_coffee]['ingredients']['water']
    current_milk = MENU[user_coffee]['ingredients']['milk']
    current_coffee = MENU[user_coffee]['ingredients']['coffee']
    if water - current_water >=0 and milk - current_milk >= 0 and coffee - current_coffee >=0:
        return True
    else:
        if water - current_water < 0:
            return 'water'
        elif coffee - current_coffee < 0:
            return 'coffee'
        elif milk - current_milk < 0:
            return 'milk'


def money_request(user_coffee):
    global money
    price = MENU[user_coffee]['cost']
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    user_money = pennies * 0.01 + nickles * 0.05 + dimes * 0.1 + quarters * 0.25
    if user_money > price:
        print(f"Here is ${round(user_money-price,1)} in charge.")
        money+=price
        return True
    elif user_money == price:
        money+=price
        return True
    else:
        return False


def coffee_making(user_coffee):
    global water, milk, coffee
    current_water = MENU[user_coffee]['ingredients']['water']
    current_milk = MENU[user_coffee]['ingredients']['milk']
    current_coffee = MENU[user_coffee]['ingredients']['coffee']
    water-= current_water
    milk-= current_milk
    coffee-= current_coffee


global water, milk, coffee, money
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0


run = True
while run:
    user_ask = input("What would you like? (espresso/latte/cappuccino): ")
    if user_ask == 'off':
        run = False
    elif user_ask == 'report':
        report()
    else:
        if check_resources(user_ask) == True:
            if money_request(user_ask) == True:
                coffee_making(user_ask)
                print(f"Here is your {user_ask}. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
        else:
            print("Sorry there is not enough", check_resources(user_ask))
