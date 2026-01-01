def pairwise(arr, target):
    indices = []
    for i, num in enumerate(arr):
        complement = target - num
        if complement in arr[i+1:]:
            indices.append(i)
            indices.append(arr.index(complement, i+1))
    return sum(indices)

if __name__ == '__main__':
    print(pairwise([2, 3, 4, 6, 8], 10))  # 9
    print(pairwise([4, 1, 5, 2, 6, 3], 7))  # 15
    print(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))  # 10
    print(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20))  # 22