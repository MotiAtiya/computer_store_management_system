

def display_single_product(product:dict):
    print("Product ID:", product["id"])
    print("Name:", product["name"])
    print("Category:", product["category"])
    print("Price:", product["price"])
    

def display_active_products(products:list):
    if not products:
        print("There are no products in system")
        return

    print("ID".ljust(5), "Name".ljust(40), "Category".ljust(30), "Price".ljust(10), "Stock".ljust(10))
    print()
    for p in products:
        if p["active"]:
            print(str(p["id"]).ljust(5), str(p["name"]).ljust(40), str(p["category"]).ljust(30), str(p["price"]).ljust(10), p["stock"])


def display_menu(menu):
    for index, option in menu.items():
        print(index, option[0])