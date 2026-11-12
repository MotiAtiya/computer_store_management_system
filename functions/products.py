from .user_input import ask
from .validators import parse_string, parse_price, parse_stock
from .helpers import get_uniqe_id


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

