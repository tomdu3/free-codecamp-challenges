from collections import Counter

def purge_most_frequent(arr):
    counter = Counter(arr)
    most_frequent = counter.most_common()[0][0]
    return [x for x in arr if x != most_frequent]


if __name__ == "__main__":
    print(purge_most_frequent([1, 2, 2, 3]))
    print(purge_most_frequent(["a", "b", "d", "b", "c", "d", "c", "d", "c", "d"]))
    print(purge_most_frequent(["red", "blue", "green", "red", "blue", "green", "blue"]))
    print(purge_most_frequent([5, 5, 5, 5]))