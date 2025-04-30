class Checkout:
    class Discount:
        def __init__(self, num_of_items, price):
            self.num_of_items = num_of_items
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.prices:
            raise Exception("Bad Item!")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            total += self.calculateItemTotal(item, cnt)
        return total

    def addDiscount(self, item, num_of_items, price):
        discount = self.Discount(num_of_items, price)
        self.discounts[item] = discount

    def calculateItemTotal(self, item, cnt):
        total = 0
        if item in self.discounts:
            discount = self.discounts[item]
            if cnt >= discount.num_of_items:
                total += self.calculateItemDiscountedTotal(item, cnt, discount)
            else:
                total += self.prices[item] * cnt
        else:
            total += self.prices[item] * cnt

        return total

    def calculateItemDiscountedTotal(self, item, cnt, discount):
        total = 0
        num_of_discount = cnt / discount.num_of_items
        total += num_of_discount * discount.price
        remaining = cnt % discount.num_of_items
        total += remaining * self.prices[item]
        return total


checkout = Checkout()
checkout.addItemPrice("apple", 1.00)
checkout.addItemPrice("banana", 0.50)

checkout.addDiscount("apple", 3, 2.50)  # Buy 3 apples for $2.50

checkout.addItem("apple")
checkout.addItem("apple")
checkout.addItem("apple")
checkout.addItem("banana")

total = checkout.calculateTotal()
print(f"Total: ${total:.2f}")  # Output: Total: $3.00
