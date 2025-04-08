from data import MENU
from data import resources

# from art import logo
# print(logo)
make_new_coffee = True
while make_new_coffee:
    def menu_input():
        """Gathers an input value from the user just like on a normal coffee machine a user would press a button to decide
        what operation to commence."""
        menu_prompt = input("What would you like? (espresso/latte/cappuccino)\n").lower()
        return menu_prompt
        # Hidden Input OFF for turning fo the machine


    def resources_show():
        """Shows the representation of current resources available in the coffe machine"""
        for res in resources:
            print(f"{res} : {resources[res]}")


    def is_resource_sufficient(coffee_type, order_ingredients):

        for item in order_ingredients:
            if order_ingredients[item] >= resources[item]:
                print(f"Sorry there is not enough {item}")
                return False
        return True


    def coin_prompt(coffee_type):
        print(f"Please insert coins (pennies/nickles/dimes or quarters) to buy {coffee_type}")
        pennies_input = (int(input("How many pennies will you put in?\n")) * 0.01)
        nickles_input = (int(input("How many nickles will you put in?\n")) * 0.05)
        dimes_input = (int(input("How many dimes will you put in?\n")) * 0.10)
        quarters_input = (int(input("How many quarters will you put in?\n")) * 0.25)
        total_sum = pennies_input + nickles_input + dimes_input + quarters_input
        return round(total_sum, 2)


    def coin_check(coffee_type, total_coin):
        # print("gets in")
        if total_coin > MENU[coffee_type]["cost"]:
            resources["money"] += total_coin
            change = resources["money"] - MENU[coffee_type]["cost"]
            return f"Here is your {coffee_type}. Enjoy!. Here is ${round(change, 2)} in change."
        elif total_coin < MENU[coffee_type]["cost"]:
            return f"Sorry, {total_coin} is not enough money. Money refunded."
        elif total_coin == MENU[coffee_type]["cost"]:
            resources["money"] += total_coin
            return f"Here is your {coffee_type}. Enjoy!"


    def deducting_resources(coffe_type):
        for res in resources:
            if res in MENU[coffe_type]["ingredients"]:
                resources[res] = resources[res] - MENU[coffe_type]["ingredients"][res]


    def maintenance_prompt(hidden_command):
        if hidden_command == "off":
            print("coffe machine turned OFF.")

        elif hidden_command == "report":
            resources_show()


    def menu_input_check(user_input):
        """Main checking(and probably operating/time will show) function"""

        if (user_input == "espresso") or (user_input == "latte") or (user_input == "cappuccino"):
            drink = MENU[user_input]
            print(f"Cost of {user_input} is {MENU[user_input]['cost']}.")
            res = is_resource_sufficient(user_input, drink["ingredients"])
            if res:
                total_coins = coin_prompt(user_input)
                coin_checker = coin_check(user_input, total_coins)
                deducting_resources(user_input)
                print(coin_checker)

            elif not res:
                return res
        elif user_input == "report":
            maintenance_prompt(user_input)
        elif user_input == "off":
            maintenance_prompt(user_input)


    # add clear console here and there and we are FIRE!!✅
    menu_input_check(menu_input())
