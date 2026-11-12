from .user_input import ask, edit
from .validators import parse_string, parse_positive_int_number, parse_positive_float_number, parse_not_negative_int_number, choice_from, parse_yes_no_confirmatino
from .helpers import get_uniqe_id
from .printer import display_menu, display_single_product, display_option_title, display_active_products

def add_product(products:list):
    product_name = ask(parse_string, "Enter product name: ")
    product_category = ask(parse_string, "Enter product category: ")
    product_price = ask(parse_positive_float_number, "Enter product price: ")
    product_stock = ask(parse_not_negative_int_number, "Enter product stock: ")
    product_id = get_uniqe_id(products)

    new_product = {
        "id": product_id,
        "name": product_name,
        "category": product_category,
        "price": product_price,
        "stock": product_stock,
        "active": True
    }
    products.append(new_product)


def search_by_id(products):
    product_id = ask(parse_positive_int_number, "Enter product ID: ")
    for p in products:
            if p["id"] == product_id:
                return p
    return None


def search_by_name(products):
    product_name = ask(parse_string, "Enter product name: ")
    for p in products:
            if product_name in p["name"]:
                return p
    return None


def search_by_category(products):
    product_category = ask(parse_string, "Enter product category: ")
    for p in products:
            if product_category in p["category"]:
                return p
    return None


def search_product(products:list, in_stock=False):
    menu = {
        "1": ("Search by product ID", search_by_id),
        "2": ("Search by product name", search_by_name),
        "3": ("Search by category", search_by_category)
    }

    display_menu(menu)
    menu_parser = choice_from(list(menu))
    choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
    action = menu[choice][1]
    product = action(products)
    if not product or (in_stock and not product["stock"]):
        print("Product not found", in_stock * "in stock")
        return None
    display_single_product(product)
    return product


def update_product(products:list):
    product = search_product(products)
    if not product:
        return

    product["name"] = edit(parse_string, f"Enter product name", product["name"])
    product["category"] = edit(parse_string, f"Enter product category", product["category"])
    product["price"] = edit(parse_positive_float_number, f"Enter product price", product["price"])
    product["stock"] = edit(parse_not_negative_int_number, f"Enter product stock", product["stock"])


def delete_product(products:list):
    product = search_product(products)
    if not product:
        return

    user_confirmation = ask(parse_yes_no_confirmatino, "Are you sure you want to delete this product? [y/n]")
    if user_confirmation in ['yes', 'y', 'Y']:
        products.remove(product)
    

def product_management(products:list):
    while True:
        menu = {
            "1": ("Add Product", add_product),
            "2": ("Display All Products", display_active_products),
            "3": ("Search Product", search_product),
            "4": ("Update Product", update_product),
            "5": ("Delete Product", delete_product),
            "6": ("Back to Main Menu", None)
        }

        display_option_title("PRODUCTS MANAGEMENT")
        display_menu(menu)
        menu_parser = choice_from(list(menu))
        choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
        action = menu[choice][1]
        if action is None:
            break

        action(products)
