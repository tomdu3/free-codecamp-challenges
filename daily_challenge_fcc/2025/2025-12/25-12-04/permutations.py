from collections import Counter
import math
def count_permutations(s):
    counter = Counter(s)
    total_permutations = math.factorial(len(s))
    for count in counter.values():
        total_permutations //=math.factorial(count)
    return total_permutations