from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()


coffee_done = True
while coffee_done:
    coffee_choice = input(f"What would you like? ({menu.get_items()}):")
    if coffee_choice == "off":
        print("Coffee machine turned OFF.")
        coffee_done = False
    elif coffee_choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

