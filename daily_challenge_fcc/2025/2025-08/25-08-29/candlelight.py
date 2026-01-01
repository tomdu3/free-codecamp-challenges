def burn_candles(candles, leftovers_needed):
    total_burned = 0
    leftovers = 0
    
    while candles > 0:
        total_burned += candles
        leftovers += candles  # Burn current candles → get stubs
        candles = leftovers // leftovers_needed  # Make new candles
        leftovers = leftovers % leftovers_needed  # Keep leftover stubs
    
    return total_burned
