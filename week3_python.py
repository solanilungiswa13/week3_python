def calculate_discount(price, discount_percent): 
    """Calculates the final price after applying a discount. 
    Args: price: The original price of the item. discount_percent: The discount percentage. 
    Returns: The final price after applying the discount, or the original price if the discount is less than 20%. 
    """ 
    if discount_percent >= 20: 
        discount_amount = price * (discount_percent / 100) 
        final_price = price - discount_amount 
        return final_price 
    else: 
        return price 
    # Prompt the user to enter the original price and discount percentage. 
original_price = float(input("Enter the original price of the item: ")) 
discount_percentage = float(input("Enter the discount percentage: ")) 
# Calculate the final price using the calculate_discount function. 
final_price = calculate_discount(original_price, discount_percentage) 
# Print the final price. 
print("The final price is:", final_price)