# 🛒 Checkout System with Discounts (Python)
This homework implements a simple yet flexible checkout system in Python. It allows you to scan items, apply pricing, define item-specific bulk discounts, and compute the total price dynamically.
<br />

🎯 Features:

  * Add items and their base prices
  * Support for quantity-based discounts
  * Calculate total cost of all items in cart
  * Error handling for unpriced items
<br />

🧱 Class Overview:

  🧮 Checkout Class:

  * The main class that handles item scanning, pricing, and total calculation.
  
  📉 Discount Inner Class:
  
  * Handles the data structure for quantity-based discounts.
<br />

📌 Methods:

  Method	Description:

  * addItemPrice(item, price):	Sets the price for a given item
  * addItem(item):	Adds an item to the checkout (raises an exception if the item has no price)
  * addDiscount(item, num_of_items, price):	Adds a bulk discount for an item
  * calculateTotal():	Returns the total cost of all scanned items
  * calculateItemTotal(item, count):	Calculates the total for a specific item considering discounts
  * calculateItemDiscountedTotal(item, count, discount):	Applies the discount logic for a discounted item
<br />

