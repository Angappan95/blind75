'''
Given a string, find the length of the longest substring without repeating characters.

s = "abcdabcbb"

# Output: 3
# Longest substring: "abc"
'''

def brute_force(string):
    length = len(string)
    unique_str = ''
    for left in range(length):
        for right in range(left+1, length):
            substring = string[left:right]

            # use set to check if all the chars are unique
            if len(set(substring)) == len(substring):
                if len(substring) > len(unique_str):
                    unique_str = substring
    return (unique_str, len(unique_str))

def sliding_window(string):
    # Expand from current position
    left = 0
    max_length = 0
    seen = set()

    for right, ch in enumerate(string):
        while ch in seen:
            seen.remove(ch)
            left += 1

        seen.add(ch)
        max_length = max(max_length, right - left + 1)
        
    return max_length
    


print(sliding_window('abcabcdefb'))
print(sliding_window('abbba'))