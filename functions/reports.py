from .printer import display_option_title, display_function_title, display_sale_summary
from .menu import get_action, enter_to_continue
from .products import get_product_by_id

def total_sales(sales:list):
    print(len(sales), "sales in total")


def total_revenue(sales:list):
    total = sum(sale['total'] for sale in sales)
    print(total)


def best_selling_products(products:list, sales:list):
    if not sales:
        raise ValueError("No sales in system")
    
    selling_products = {}
    for sale in sales:
        for item in sale['items']:
            product_id = item['product_id']
            selling_products[product_id] = selling_products.get(product_id, 0) + item['quantity']


    best_5 = sorted(selling_products, key=lambda k: selling_products[k], reverse=True)[:5]

    for product_id in best_5:
        product = get_product_by_id(products, product_id)
        print(f"{str(f"{product['name']}:").ljust(25)} {selling_products[product_id]} units") # type: ignore


def average_sale(sales:list):
    if not sales:
        raise ValueError("No sales in system")

    total = sum(sale['total'] for sale in sales)
    average = round(total / len(sales), 2)
    print(average)


def sales_history(sales:list):
    if not sales:
        raise ValueError("No sales in system")

    for sale in sales:
        print("Sale ID:", sale['id'])
        display_sale_summary(sale)
        print()


def category_statistics(products:list, sales:list):
    if not sales:
        raise ValueError("No sales in system")
    
    categories = {}
    for sale in sales:
        for item in sale['items']:
            product = get_product_by_id(products, item['product_id'])
            category = product['category'] # type: ignore
            if category in categories:
                categories[category] += item['quantity']
            else:
                categories[category] = item['quantity']


    for category in categories:
        print(f"{str(f"{category}:").ljust(20)} {categories[category]} units") # type: ignore



def reports(products:list, sales:list):

    menu = {
        "1": ("Total Sales", lambda: total_sales(sales)),
        "2": ("Total Revenue", lambda: total_revenue(sales)),
        "3": ("Best Selling Products", lambda: best_selling_products(products, sales)),
        "4": ("Average Sale", lambda: average_sale(sales)),
        "5": ("Sales History", lambda: sales_history(sales)),
        "6": ("Category Statistics", lambda: category_statistics(products, sales)),
        "7": ("Back to Main Menu", None)
    }

    while True:
        display_option_title("Reports")
        title, action = get_action(menu)
        if action is None:
            break

        try:
            display_function_title(title)
            action()
        except ValueError as e:
            print("Error:", e)
        finally: enter_to_continue()

