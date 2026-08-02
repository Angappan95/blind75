'''
Merge two sorted arrays

arr1 - [1, 3, 6] arr2 - [2, 4, 10, 11]

result - [1, 2, 3, 4, 6, 10, 11]
'''

def merge_arrays(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)
    result = []

    i = j = 0

    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    if i < len1:
        remaining = arr1[i:]
        result.extend(remaining)
    if j < len2:
        remaining = arr2[j:]
        result.extend(remaining)
    return result


print(merge_arrays([1, 3, 6], [2, 4, 10, 11]))
    