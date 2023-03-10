from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
profit = 0
menu = Menu()
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()


while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        user_input = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(user_input) and money_machine.make_payment(user_input.cost):
            coffee_maker.make_coffee(user_input)
