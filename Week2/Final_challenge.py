def update_stock(current_stock, new_books):
    # Variable to hold the updated stock
    updated_stock = current_stock + new_books
    
    # Print the update message
    print(f"Added {new_books} new books. Total stock is now {updated_stock} books.")
    
    # Return the updated stock
    return updated_stock

# Example usage:
current_stock = 50
new_books = 20
updated_stock = update_stock(current_stock, new_books)
print(f"Updated stock: {updated_stock}")