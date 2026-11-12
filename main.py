from DATA.initial_products import initial_products
from functions.products import search_product, update_product, delete_product, product_management
from functions.printer import display_menu, display_system_title
from functions.user_input import ask
from functions.validators import choice_from


def main():
    products = initial_products

    menu = {
        "1": ("Products Management", product_management),
        "2": ("Inventory Management", ),
        "3": ("Sales Management", ),
        "4": ("Reports", ),
        "5": ("Exit", None)
    }

    while True:
        display_system_title()
        display_menu(menu)
        menu_parser = choice_from(list(menu))
        choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
        action = menu[choice][1]
        if action is None:
            print("Bye!")
            break
        
        action(products)

if __name__ == "__main__":
    main()
