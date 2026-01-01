import math


def combinations(cards):
    """
    `cards` is an integer - represents how many cards to pick from the deck.
    52 cards are in the deck.
     need to find the total number of unique combinations of cards.
    """
    DECK_SIZE = 52
    # Binomial coefficients
    result = math.factorial(DECK_SIZE) / (
        math.factorial(cards) * math.factorial(DECK_SIZE - cards)
    )

    return result
