def validate_input(prompt, valid_options):
    while True:
        user_input = input(prompt)
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please choose from {valid_options}.")

def format_price(price):
    return f"${price:.2f}"

def display_message(message):
    print(message)