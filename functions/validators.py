def parse_string(raw):
    string = raw.strip()
    if not string:
        raise ValueError("Cannot be empty")
    return " ".join(string.split()).title()


def parse_positive_int_number(raw):
    num = raw.strip()
    if not num:
        raise ValueError("Cannot be empty")
    try:
        num = int(num)
    except ValueError:
        raise ValueError("Must be an integer number")
    if num <= 0:
        raise ValueError("Must be a positive number")
    return num
    

def parse_positive_float_number(raw):
    num = raw.strip()
    if not num:
        raise ValueError("Cannot be empty")
    try:
        num = float(num)
    except ValueError:
        raise ValueError("Must be a number")
    if num <= 0:
        raise ValueError("Must be a positive number")
    return num


def parse_not_negative_int_number(raw):
    stock = raw.strip()
    if not stock:
        raise ValueError("Cannot be empty")
    try:
        stock = int(stock)
    except ValueError:
        raise ValueError("Must be an integer number")
    if stock < 0:
        raise ValueError("Must be a not negative number")
    return stock


def choice_from(options):
    def parser(raw):
        choice = raw.strip()
        try:
            int(choice)
        except ValueError:
            raise ValueError("Must be an integer number")
        else:
            if choice not in options:
                raise ValueError("Invalid choice")
            return choice
    return parser


def parse_yes_no_confirmatino(raw):
    confirm = raw.strip()
    if not confirm:
        raise ValueError("Cannot be empty")
    if confirm not in ['yes', 'y', 'Y', 'no', 'n', 'N']:
        raise ValueError("Invalid choise. Only yes (y) or no (n)")
    return confirm