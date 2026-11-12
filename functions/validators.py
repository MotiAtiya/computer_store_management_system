def parse_string(raw):
    string = raw.strip()
    if not string:
        raise ValueError("Cannot be empty")
    return " ".join(string.split()).title()

def parse_price(raw):
    price = raw.strip()
    if not price:
        raise ValueError("Cannot be empty")
    try:
        price = float(price)
    except ValueError:
        raise ValueError("Must be a number")
    if price <= 0:
        raise ValueError("Must be a positive number")

def parse_stock(raw):
    stock = raw.strip()
    if not stock:
        raise ValueError("Cannot be empty")
    try:
        stock = int(stock)
    except ValueError:
        raise ValueError("Must be an integer number")
    if stock < 0:
        raise ValueError("Must be a not negative number")

# def parse_menu(raw):
