from .user_input import ask, edit
from .validators import parse_string, parse_id, parse_price, parse_stock, choice_from
from .helpers import get_uniqe_id
from .printer import display_menu, display_single_product

def add_product(products:list):
    product_name = ask(parse_string, "Enter product name: ")
    product_category = ask(parse_string, "Enter product category: ")
    product_price = ask(parse_price, "Enter product price: ")
    product_stock = ask(parse_stock, "Enter product stock: ")
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
    product_id = ask(parse_id, "Enter product ID: ")
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


def search_product(products:list):
    menu = {
        "1": ("Search by product ID", search_by_id),
        "2": ("Search by product name", search_by_name),
        "3": ("Search by category", search_by_category)
    }

    display_menu(menu)
    menu_parser = choice_from(list(menu))
    choice = ask(menu_parser, "Enter your choice [1-3]: ")
    product = menu[choice][1](products)
    if product:
         display_single_product(product)
         return product
    else:
         print("Product not found")
         return None


def update_product(products:list):
    product = search_product(products)
    if not product:
        return

    product["name"] = edit(parse_string, f"Enter product name", product["name"])
    product["category"] = edit(parse_string, f"Enter product category", product["category"])
    product["price"] = edit(parse_price, f"Enter product price", product["price"])
    product["stock"] = edit(parse_stock, f"Enter product stock", product["stock"])
