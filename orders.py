class Order:
    def __init__(self):
        self.items = []
        self.total_price = 0.0

    def add_item(self, item_name, item_price):
        self.items.append((item_name, item_price))
        self.total_price += item_price

    def calculate_total(self):
        return self.total_price

    def display_order(self):
        order_details = "Order Details:\n"
        for item_name, item_price in self.items:
            order_details += f"{item_name}: ${item_price:.2f}\n"
        order_details += f"Total Price: ${self.calculate_total():.2f}"
        return order_details