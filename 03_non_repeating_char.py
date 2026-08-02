'''
Given a string, return the index of its first non-repeating character. Return -1 when every character repeats.

s = "leetcode"

# Output: 0
s = "loveleetcode"
'''

def non_repeating_char_brute_force(string):
    length = len(string)

    for i in range(length):
        for j in range(length):
            if i != j and string[i] == string[j]:
                break
        else:
            return i
    return -1


def non_repeating_char_counter(string):
    counter = {}
    for ch in string:
        counter[ch] = counter.get(ch, 0) + 1
    for i, ch in enumerate(string):
        if counter[ch] == 1:
            return i
    return -1



print(non_repeating_char_counter('leetcode'))
print(non_repeating_char_counter('loveleetcodev'))
print(non_repeating_char_counter('maddam'))