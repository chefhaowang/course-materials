def calculate_total(prices, quantities):
    total = 0
    for i in range(prices):
        total += prices[i] * quantities[i]

    if total > 500:
        discount = total * 0.20
        total -= discount
    elif total > 200:
        discount = total * 0.15
        total -= discount
    elif total > 100:
        discount = total * 0.10
        total -= discount

    if total < 100:
        tax = total * 0.05
    elif total < 500:
        tax = total * 0.10
    else:
        tax = total * 0.15

    total += tax

    return total


# Sample shopping cart
prices = [999.99, 25.50, 45.00]  # Prices of items
quantities = [1, 2, 1]  # Quantities of items
print(f"Total price: ${calculate_total(prices, quantities)}")

# Additional test case for an empty cart
empty_prices = []
empty_quantities = []
print(f"Total price for an empty cart: ${
      calculate_total(empty_prices, empty_quantities):.2f}")

# Additional test case for mismatched cart
mismatched_prices = [10, 20]
mismatched_quantities = [1]
print(f"Total price for mismatched cart: ${
      calculate_total(mismatched_prices, mismatched_quantities):.2f}")

# Additional test cases for various price ranges
prices1 = [50, 50, 50]  # Total 150
quantities1 = [1, 1, 1]
print(f"Total price: ${calculate_total(prices1, quantities1):.2f}")

prices2 = [300, 300]  # Total 600
quantities2 = [1, 1]
print(f"Total price: ${calculate_total(prices2, quantities2):.2f}")

prices3 = [50, 50]  # Total 100
quantities3 = [1, 1]
print(f"Total price: ${calculate_total(prices3, quantities3):.2f}")
