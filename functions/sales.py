from .printer import display_option_title, display_sale_summary, display_continue_msg
from .user_input import ask
from .validators import parse_positive_int_number, choice_from, parse_percentage
from .products import search_by_id, get_product_by_id
from .helpers import get_next_id
from .menu import get_action
from .inventory import update_stock


def add_item_to_cart(products:list, cart:dict):
    product = search_by_id(products)
    if not product:
        raise ValueError("Product not found")
    if not product["active"]:
        raise ValueError("Product not active")
    product_id = product["id"]
    quantitiy = ask(parse_positive_int_number, "Enter quantity: ")
    if quantitiy > product["stock"]:
        raise ValueError("Not enough quantity in stock")
    if product_id in cart and quantitiy + cart[product_id] > product["stock"]:
        raise ValueError("Not enough quantity in stock")

    if product_id in cart:
        cart[product_id] += quantitiy
    else:
        cart[product_id] = quantitiy


def update_quantity(products:list, cart:dict):
    product = search_by_id(products)
    if not product:
        raise ValueError("Product not found")
    if product["id"] not in cart.keys():
        raise ValueError("Product not in cart")
    quantitiy = ask(parse_positive_int_number, "Enter quantity: ")
    if quantitiy > product["stock"]:
            raise ValueError("Not enough quantity in stock")
    cart[product["id"]] = quantitiy


def remove_item(products:list, cart:dict):
    product = search_by_id(products)
    if not product:
        raise ValueError("Product not found")
    if product["id"] not in cart.keys():
        raise ValueError("Product not in cart")
    del cart[product["id"]]


def complete_sale(products:list, cart:dict, salses:list):
    if not cart:
        raise ValueError("The cart is empty")

    discount = ask(parse_percentage, "Enter discount [0-100]: ")

    
    items = []
    for product_id, quantity in cart.items():
        product = get_product_by_id(products, product_id)
        update_stock(product, -quantity)
        items.append({
            "product_id": product_id,
            "name": product["name"],                # type: ignore
            "quantity": quantity,
            "unit_price": product["price"],         # type: ignore
            "total": product["price"] * quantity    # type: ignore
        })

    sale_id = get_next_id(salses)
    subtotal = sum(item["total"] for item in items)
    total = subtotal - subtotal * discount / 100

    sale = {
        "id": sale_id,
        "items": items,
        "subtotal": subtotal,
        "discount": discount,
        "total": total
    }

    display_sale_summary(sale)
    salses.append(sale)
    

def new_sell(products:list, sales:list):
    display_option_title("NEW SALE")

    cart = {}

    if not cart:
        print("Cart is empty")

    num_of_sales = len(sales)

    continue_sell = True

    while continue_sell:
        menu = {
            "1": ("Add Item", lambda: add_item_to_cart(products, cart)),
            "2": ("Update Quantity", lambda: update_quantity(products, cart)),
            "3": ("Remove Item", lambda: remove_item(products, cart)),
            "4": ("Complete Sale", lambda: complete_sale(products, cart, sales)),
            "5": ("Cancel Sale", None)
        }

        action = get_action(menu)
        if action is None:
            break

        try:
            action()
        except ValueError as e:
            print("Error:", e)
        finally:
            display_continue_msg()

        if len(sales) > num_of_sales:
            break
        
