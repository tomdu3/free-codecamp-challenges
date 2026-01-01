def calculate_tips(meal_price, custom_tip):
    """
    Given the price of your meal and a custom tip percent,
    return an array with three tip values; 15%, 20%, and the custom amount.

    Args:
        meal_price (str): The total price of the meal, in format: "$N.NN".
        custom_tip (str): The custom tip percentage (e.g., 15 for 15%), in format: "N%".
    Returns:
        amounts (list): An array of strings representing the tip amounts for 15%, 20%, and the custom tip percentage, each in format: "$N.NN".
    """

    # Remove the dollar sign and convert to float
    price = float(meal_price.replace("$", ""))
    # Remove the percent sign and convert to float
    custom_percentage = float(custom_tip.replace("%", ""))/100
    # Calculate tip amounts
    tip_15 = price * 0.15
    tip_20 = price * 0.20
    tip_custom = price * custom_percentage
    # Format amounts to two decimal places with dollar sign
    amounts = [f"${tip_15:.2f}", f"${tip_20:.2f}", f"${tip_custom:.2f}"]

    return amounts