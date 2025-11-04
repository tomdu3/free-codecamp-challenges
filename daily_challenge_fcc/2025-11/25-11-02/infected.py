import math
def infected(days):
    reduction_rate = .20
    currently_infected = 1
    if days == 0:
        return currently_infected

    for day in range(1, days+1):
        currently_infected *=2 
        if  day % 3 == 0:
            print(currently_infected,  math.ceil(currently_infected * reduction_rate))
            currently_infected -= math.ceil(currently_infected * reduction_rate)
        
    
    return currently_infected