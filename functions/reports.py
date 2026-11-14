from .printer import display_option_title
from .menu import get_action, enter_to_continue



def reports(sales:list):

    menu = {
        # "1": ("Total Sales", total_sales),
        # "2": ("Total Revenue", total_revenue),
        # "3": ("Best Selling Products", best_selling_products),
        # "4": ("Average Sale", average_sale),
        # "5": ("Category History", category_history),
        # "6": ("Category Statistics", category_statistics),
        # "7": ("Back to Main Menu", None)
    }

    while True:
        display_option_title("REPORTS")
        action = get_action(menu)
        if action is None:
            break

        try:
            action(sales)
        except ValueError as e:
            print("Error:", e)
        finally: enter_to_continue()

