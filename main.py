from functions.printer import display_system_title
from functions.products import product_management
from functions.inventory import inventory_management
from functions.sales import new_sell
from functions.menu import get_action

from DATA.initial_products import initial_products
from DATA.initial_sales import initial_sales


def main():
    products = initial_products
    sales = initial_sales

    menu = {
        "1": ("Products Management", lambda: product_management(products)),
        "2": ("Inventory Management", lambda: inventory_management(products)),
        "3": ("Sales Management", lambda: new_sell(products, sales)),
        "4": ("Reports", ),
        "5": ("Exit", None)
    }

    while True:
        display_system_title()
        action = get_action(menu)
        if action is None:
            print("Bye!")
            break

        action()

if __name__ == "__main__":
    main()
