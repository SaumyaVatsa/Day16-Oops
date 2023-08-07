# Imports
from menu import Menu, MenuItem
from Coffee_maker import Coffee_maker
from money_machine import MoneyMachine

# Objects
money_machine = MoneyMachine()
coffee_maker = Coffee_maker()
menu = Menu()
is_on = True

# Main Program
while is_on:
    options = menu.get_items()
    choice = input(f"what would you like to have? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
