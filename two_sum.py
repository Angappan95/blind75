'''
Given an integer array nums and an integer target, return the indices of two numbers whose sum equals target.

nums = [2, 7, 11, 15]
target = 17

# Output: [0, 1]
'''
def get_pairs_brute_force(nums, target):
    length = len(nums)
    for i in range(length):
        for j in range(i+1, length):
            if nums[i]+nums[j] == target:
                return [i, j]
    return [-1, -1]


def get_pairs_pointer(nums, target):
    # assuming the nums array is always sorted ascendingly
    left = 0
    right = len(nums)-1
    while left < right:
        if nums[left]+ nums[right] == target:
            return [left, right]
        elif nums[left]+ nums[right] > target:
            right -= 1
        else:
            left += 1
    return [-1, -1]

def get_paris_hash(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [i, seen[complement]]
        seen[num] = i
    return [-1, -1]


print(get_paris_hash([2, 7, 11, 15], 18))

