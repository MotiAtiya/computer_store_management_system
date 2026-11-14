from functions.printer import display_system_title
from functions.products import product_management
from functions.inventory import inventory_management
from functions.sales import sales_management
from functions.reports import reports
from functions.menu import get_action

from DATA.initial_products import initial_products
from DATA.initial_sales import initial_sales


def main():
    products = initial_products
    sales = initial_sales

    menu = {
        "1": ("Products Management", lambda: product_management(products)),
        "2": ("Inventory Management", lambda: inventory_management(products)),
        "3": ("Sales Management", lambda: sales_management(products, sales)),
        "4": ("Reports", lambda: reports(products, sales)),
        "5": ("Exit", None)
    }

    while True:
        display_system_title()
        _, action = get_action(menu)
        if action is None:
            print("Bye!")
            break

        action()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nBye!")
