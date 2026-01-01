def pairwise(arr, target):
    indices = set()
    used_indices = set()
    
    for i, num in enumerate(arr):
        if i in used_indices:
            continue
        
        complement = target - num
        
        found = False
        for j in range(i + 1, len(arr)):
            if arr[j] == complement and j not in used_indices:
                indices.add(i)
                indices.add(j)
                used_indices.add(i)
                used_indices.add(j)
                found = True
                break
        
        if found:
            continue
    
    return sum(indices)

if __name__ == '__main__':
    print(pairwise([2, 3, 4, 6, 8], 10))  # 9
    print(pairwise([4, 1, 5, 2, 6, 3], 7))  # 15
    print(pairwise([7, 9, 13, 19, 21, 6, 3, 1, 4, 8, 12, 22], 24))  # 10
    print(pairwise([-30, -15, 5, 10, 15, -5, 20, -40], -20))  # 22