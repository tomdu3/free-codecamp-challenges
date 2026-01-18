def gets_free_shipping(cart, minimum):
    items = {
        "shirt": 34.25,
        "jeans": 48.50,
        "shoes": 75.00,
        "hat": 19.95,
        "socks": 15.00,
        "jacket": 109.95,
    }

    return sum(items[item] for item in cart) >= minimum