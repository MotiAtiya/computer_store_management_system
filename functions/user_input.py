def ask(parse_input, prompt_input):
    while True:
        try:
            return parse_input(input(prompt_input))
        except ValueError as e:
            print("Error:", e)

