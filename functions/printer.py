

def display_single_product(product:dict):
    print("Product ID:", product["id"])
    print("Name:", product["name"])
    print("Category:", product["category"])
    print("Price:", product["price"])


def display_products(products:list):
    print("ID".ljust(5), "Name".ljust(40), "Category".ljust(30), "Price".ljust(10), "Stock".ljust(10))
    print()
    for p in products:
        if p["active"]:
            print(str(p["id"]).ljust(5), str(p["name"]).ljust(40), str(p["category"]).ljust(30), str(p["price"]).ljust(10), p["stock"])


def display_active_products(products:list):
    if not products:
        print("There are no products in system")
        return

    display_products(list(filter(lambda p: p["active"] == True ,products)))


def display_in_stock_products(products:list):
    if not products:
        print("The stock is empty")
        return

    display_products(list(filter(lambda p: p["stock"] > 0 ,products)))


def display_out_of_stock_products(products:list):
    if not products:
        print("There are no products in system")
        return

    display_products(list(filter(lambda p: p["stock"] == 0 ,products)))

    
def display_low_stock_products(products:list, low_threshold):
    if not products:
        print("There are no products in system")
        return

    display_products(list(filter(lambda p: p["stock"] <= low_threshold ,products)))

    
def display_menu(menu):
    for index, option in menu.items():
        print(f"{index}. {option[0]}")


def display_system_title():
    print("""
=================================
       COMPUTER STORE SYSTEM
=================================
    """)


def display_option_title(option_title):
    print(f"\n--------- {option_title} ---------\n")

