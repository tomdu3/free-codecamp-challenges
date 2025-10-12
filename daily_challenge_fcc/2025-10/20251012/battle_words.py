def battle(our_team, opponent):
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    def score(word):
        score_list = []
        for l in word:
            l_pos = LETTERS.index(l.lower()) + 1
            score_list.append(l_pos if l.islower() else l_pos*2)
        return sum(score_list)
    our_team_wins, opponent_wins = 0, 0
    for our_word, opponent_word in zip(our_team.split(), opponent.split()):
        our_score = score(our_word)
        opponent_score = score(opponent_word)
        if our_score == opponent_score:
            continue
        elif our_score > opponent_score:
            our_team_wins +=1
        else:
            opponent_wins +=1
    


    if our_team_wins > opponent_wins:
        return 'We win'
    elif opponent_wins > our_team_wins:
        return 'We lose'
    else:
        return 'Draw'


# Example usage:
if __name__ == "__main__":
    print(battle("hello world", "hello word"))  # Output: "We win"
    print(battle("lorem ipsum", "kitty ipsum"))  # Output: "We lose"
    print(battle("hello world", "world hello"))  # Output: "Draw"