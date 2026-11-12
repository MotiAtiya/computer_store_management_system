from DATA.initial_products import initial_products
from functions.products import search_product, update_product


def main():
    products = initial_products
    # search_product(products)
    update_product(products)
    
if __name__ == "__main__":
    main()
