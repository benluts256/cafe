class Menu:
    def __init__(self):
        self.items = {}

    def add_item(self, name, price):
        self.items[name] = price

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]

    def display_menu(self):
        if not self.items:
            print("Menu is empty.")
        else:
            print("Menu:")
            for name, price in self.items.items():
                print(f"{name}: ${price:.2f}")