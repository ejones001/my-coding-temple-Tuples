def process_orders(orders):
    for i, (customer, product, quantity) in enumerate(orders, 1):
        print(f"Order {i}:")
        print(f"Customer: {customer}")
        print(f"Product: {product}")
        print(f"Quantity: {quantity}")
        print()

# Sample Order Data
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

# Process and print orders
process_orders(orders)
