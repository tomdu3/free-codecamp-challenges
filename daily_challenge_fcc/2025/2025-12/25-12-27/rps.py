def rock_paper_scissors(player1, player2):
    CHOICES = ["Rock", "Paper", "Scissors"]
    
    player1_position = CHOICES.index(player1)
    player2_position = CHOICES.index(player2)
    
    if player1_position == player2_position:
        return "Tie"
    elif (player1_position + 1) % 3 == player2_position:
        return "Player 2 wins"
    else:
        return "Player 1 wins"

