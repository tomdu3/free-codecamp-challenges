def launch_fuel(payload):
    prev_fuel = 0
    
    while True:

        total_mass = payload + prev_fuel
        needed_fuel = total_mass / 5
        
        if needed_fuel - prev_fuel < 1:
            return round(needed_fuel, 1)
        
        prev_fuel = needed_fuel
