def battle(my_army, opposing_army):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def check_strength(char):
        strength = 0
        if char in alpha:
            strength += alpha.index(char) + 1
        elif char.isdigit():
            strength += int(char)
        return strength
    
    if len(my_army) < len(opposing_army):
        return "We retreated"
    elif len(my_army) > len(opposing_army):
        return "Opponent retreated"
    
    my_wins = 0
    opposing_wins = 0
    
    for i in range(len(my_army)):
        if check_strength(my_army[i]) > check_strength(opposing_army[i]):
            my_wins += 1
        elif check_strength(my_army[i]) < check_strength(opposing_army[i]):
            opposing_wins += 1
    
    if my_wins > opposing_wins:
        return "We won"
    elif my_wins < opposing_wins:
        return "We lost"
    else:
        return "It was a tie"