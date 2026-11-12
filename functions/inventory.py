from .printer import display_in_stock_products, display_option_title, display_menu, display_out_of_stock_products, display_low_stock_products
from .validators import choice_from, parse_not_negative_int_number, parse_positive_int_number
from .user_input import ask
from .products import search_product

def search_product_in_stock(products:list):
     search_product(products, True)


def add_to_stock(products:list):
    product = search_product(products)
    if not product:
        return
    
    quantity = ask(parse_not_negative_int_number, "Enter quantity to add to inventory: ")
    product["stock"] = quantity


def remove_from_stock(products:list):
    product = search_product(products)
    if not product:
        return

    quantity = ask(parse_not_negative_int_number, "Enter quantity to remove from the inventory: ")
    if quantity > product["stock"]:
        print("Not enough in stock")
        return
    
    product["stock"] -= quantity

def low_stock_products(products:list):
    low_threshold = ask(parse_positive_int_number, "Define Low Inventory Threshold: ")
    display_low_stock_products(products, low_threshold)

def inventory_management(products:list):
    while True:
        menu = {
            "1": ("Display In-Stock Products", display_in_stock_products),
            "2": ("Search Product In Stock", search_product_in_stock),
            "3": ("Add Quantity to Stock", add_to_stock),
            "4": ("Remove Quantity from Stock", remove_from_stock),
            "5": ("Display Out of Stock Product", display_out_of_stock_products),
            "6": ("Display Low Stock Product", low_stock_products),
            "7": ("Back to Main Menu", None)
        }

        display_option_title("INVENTORY MANAGEMENT")
        display_menu(menu)
        menu_parser = choice_from(list(menu))
        choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
        action = menu[choice][1]
        if action is None:
            break

        action(products)

