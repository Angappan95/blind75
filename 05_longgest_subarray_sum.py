"""
Find the contiguous subarray with the largest sum and return that sum.

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output: 6
# Subarray: [4, -1, 2, 1]
"""

def brute_force(nums):
    l = len(nums)
    start = 0
    max_sum = 0
    

    for start in range(l):
        for end in range(start, l):
            current_sum = sum(nums[start:end+1])
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


def running_sum(nums):
    l = len(nums)
    start = 0
    max_sum = 0
    

    for start in range(l):
        current_sum = 0
        for end in range(start, l):
            current_sum = current_sum + nums[end]
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum


def kadanes_algo(nums):
    max_sum = float('-inf')
    current_sum = 0

    for num in nums:
        current_sum += num
        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0
    return max_sum


def kadanes_algo_opt(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(current_sum + num, num)
        max_sum = max(current_sum, max_sum)
    return max_sum


print(kadanes_algo_opt([-2, 1, -3, 4, -1, 2, 1, -5, 4]))