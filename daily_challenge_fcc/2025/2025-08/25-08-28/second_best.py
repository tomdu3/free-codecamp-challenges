def get_laptop_cost(prices, budget):
    # Step 1: Remove duplicates
    unique_prices = list(set(prices))
    
    # Step 2: Sort descending
    unique_prices.sort(reverse=True)
    
    # Step 3: Filter within budget
    within_budget = [p for p in unique_prices if p <= budget]
    
    # Step 4: If none within budget
    if not within_budget:
        return 0
    
    # Step 5: Check second overall expensive
    if len(unique_prices) >= 2 and unique_prices[1] <= budget:
        return unique_prices[1]
    
    # Step 6: Otherwise return most expensive within budget
    return within_budget[0]
