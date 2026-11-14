from .printer import display_menu
from .validators import choice_from
from .user_input import ask

def get_action(menu):
    display_menu(menu)
    menu_parser = choice_from(list(menu))
    choice = ask(menu_parser, f"\nChoose an option [1-{len(menu)}]: ")
    action = menu[choice][1]
    return action
