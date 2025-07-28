
class CafeApp:
    def __init__(self):
        self.menu = Menu()
        self.orders = []

    def display_menu(self):
        print("Welcome to the Mini Cafe!")
        print("Here is our menu:")
        self.menu.display_items()

    def take_order(self):
        order_items = input("Please enter the items you want to order (comma-separated): ")
        order = Order(order_items.split(","))
        self.orders.append(order)
        print(f"Order created: {order.display_order()}")

    def run(self):
        self.display_menu()
        while True:
            self.take_order()
            another = input("Would you like to place another order? (yes/no): ")
            if another.lower() != 'yes':
                break
        print("Thank you for visiting the Mini Cafe!")

if __name__ == "__main__":
    app = CafeApp()
    app.run()