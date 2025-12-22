conversion_table = {
    "USD": 1.00,
    "EUR": 1.10,
    "GBP": 1.25,
    "JPY": 0.0070,
    "CAD": 0.75,
}

def buy_items(funds, items):
    total = 0
    total_available = float(funds[0]) * conversion_table[funds[1]]
    
    for idx, item in enumerate(items):
        total += float(item[0]) * conversion_table[item[1]]
    
        if total > total_available:
            return f"Buy the first {idx} items."
    
    return "Buy them all!"

