"""
Given a list of intervals, merge all overlapping intervals.

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

# Output: [[1, 6], [8, 10], [15, 18]]
"""

def merge_intervals(intervals):
    if len(intervals) <= 0:
        return []

    intervals.sort(key = lambda interval: interval[0])
    
    merged_intervals = []
    merged_intervals.append(intervals[0])

    for interval in intervals[1:]:
        last_merged_interval = merged_intervals[-1]
        
        if last_merged_interval[1] > interval[0]:
            last_merged_interval[1] = max(last_merged_interval[1], interval[1])
        else:
            merged_intervals.append(interval)
        
    
    return merged_intervals


print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))