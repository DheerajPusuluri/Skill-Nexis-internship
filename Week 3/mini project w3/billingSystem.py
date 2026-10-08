class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total(self):
        return self.price * self.quantity


class Bill:
    def __init__(self):
        self.products = []
        self.tax_rate = 5  # 5% tax

    def add_product(self, product):
        self.products.append(product)

    def calculate_subtotal(self):
        total = 0
        for product in self.products:
            total += product.get_total()
        return total

    def calculate_tax(self):
        return self.calculate_subtotal() * self.tax_rate / 100

    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_tax()

    def display_bill(self):
        print("\n" + "=" * 60)
        print("                    FINAL BILL")
        print("=" * 60)

        print(f"{'Product':<20}{'Price':>10}{'Qty':>8}{'Total':>12}")
        print("-" * 60)

        for product in self.products:
            print(f"{product.name:<20}"
                  f"{product.price:>10.2f}"
                  f"{product.quantity:>8}"
                  f"{product.get_total():>12.2f}")

        print("-" * 60)

        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        total = self.calculate_total()

        print(f"{'Subtotal':>48} ₹{subtotal:>8.2f}")
        print(f"{'Tax (5%)':>48} ₹{tax:>8.2f}")
        print(f"{'Grand Total':>48} ₹{total:>8.2f}")

        print("=" * 60)

product1 = Product("Laptop", 50000, 1)
product2 = Product("Mouse", 800, 2)
product3 = Product("Keyboard", 1500, 1)
bill = Bill()

bill.add_product(product1)
bill.add_product(product2)
bill.add_product(product3)
bill.display_bill()