def parse_string(raw):
    string = raw.strip()
    if not string:
        raise ValueError("Cannot be empty")
    return " ".join(string.split()).title()


def parse_id(raw):
    product_id = raw.strip()
    if not product_id:
        raise ValueError("Cannot be empty")
    try:
        product_id = int(product_id)
        if product_id <= 0:
            raise ValueError("Must be a positive number")
        return product_id
    except ValueError:
        raise ValueError("Must be an integer number")
    

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


def choice_from(options):
    def parser(raw):
        choice = raw.strip()
        if choice not in options:
            raise ValueError(f"Invalid choise")
        return choice
    return parser


def parse_yes_no_confirmatino(raw):
    confirm = raw.strip()
    if not confirm:
        raise ValueError("Cannot be empty")
    if confirm not in ['yes', 'y', 'Y', 'no', 'n', 'N']:
        raise ValueError("Invalid choise. Only yes (y) or no (n)")
    return confirm