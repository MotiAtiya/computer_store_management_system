from .printer import display_option_title, display_active_products, display_function_title
from .validators import parse_not_negative_int_number, parse_positive_int_number
from .user_input import ask
from .products import search_product
from .menu import get_action, enter_to_continue

def search_product_in_stock(products:list):
     search_product(products, True)


def update_stock(product, quantity):
    product['stock'] += quantity

def add_to_stock(products:list):
    product = search_product(products)
    quantity = ask(parse_positive_int_number, "Enter quantity to add to inventory: ")
    update_stock(product, quantity)
    print(f"\n{quantity} units of {product['name']} added successfuly!")


def remove_from_stock(products:list):
    product = search_product(products, True)
    quantity = ask(parse_positive_int_number, "Enter quantity to remove from the inventory: ")
    if quantity > product['stock']:
        raise ValueError("Not enough in stock")
    
    update_stock(product, -quantity)
    print(f"\n{quantity} units of {product['name']} removed successfuly!")


def in_stock_products(products:list):
    in_stock = list(filter(lambda p: p['stock'] > 0 ,products))
    if not in_stock:
        raise ValueError("The stock is empty")

    display_active_products(in_stock)


def out_of_stock_products(products:list):
    out_of_stock = list(filter(lambda p: p['stock'] == 0 ,products))
    if not out_of_stock:
        raise ValueError("There are no out of stock products in system")

    display_active_products(out_of_stock)


def low_stock_products(products:list):
    low_threshold = ask(parse_positive_int_number, "Define Low Inventory Threshold: ")
    low_stock = list(filter(lambda p: p['stock'] <= low_threshold ,products))
    if not low_stock:
        raise ValueError("There are no los stock pruduct in system")
    
    display_active_products(low_stock)


def inventory_management(products:list):
    menu = {
        "1": ("Display In-Stock Products", in_stock_products),
        "2": ("Search Product In Stock", search_product_in_stock),
        "3": ("Add Quantity to Stock", add_to_stock),
        "4": ("Remove Quantity from Stock", remove_from_stock),
        "5": ("Display Out of Stock Product", out_of_stock_products),
        "6": ("Display Low Stock Product", low_stock_products),
        "7": ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Inventory Management")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action(products)
        except ValueError as e:
            print("Error:", e)
        finally:
            enter_to_continue()

