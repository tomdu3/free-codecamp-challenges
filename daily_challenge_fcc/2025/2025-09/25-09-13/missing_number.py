def find_missing_numbers(nums):
    nums = list(sorted(set(nums)))
    missing = []
    for i in range(1, max(nums)):
        if i not in nums:
            missing.append(i)
    return missing
    