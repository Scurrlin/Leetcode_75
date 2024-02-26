# Non-overlapping Intervals

def eraseOverlapIntervals(intervals: List[List[int]]) -> int:

# This line defines a function named `eraseOverlapIntervals` that takes a list of lists (each containing two integers) as an argument and returns an integer.

    if not intervals:
        return 0

# This block checks if the `intervals` list is empty. If it is, the function returns 0 because there are no intervals to erase.

    intervals.sort(key=lambda x: x[1])

# This line sorts the `intervals` list in ascending order based on the second element of each sublist. The `key` parameter of the `sort` function is a function that defines how to sort the elements. Here, it's a lambda function that takes an element `x` (a sublist in this case) and returns its second element (`x[1]`).

    end = intervals[0][1]

# This line initializes a variable `end` with the value of the second element of the first sublist in the sorted `intervals` list.

    count = 1

# This line initializes a variable `count` with the value 1. This variable keeps track of the number of non-overlapping intervals.

    for interval in intervals[1:]:

# This line starts a for loop that iterates over each sublist (`interval`) in the `intervals` list, starting from the second sublist.

        if interval[0] >= end:

# This line checks if the first element of the current `interval` is greater than or equal to `end`. This condition is true when the current interval does not overlap with the previous non-overlapping interval.

            end = interval[1]

# If the condition is true, `end` is updated to the value of the second element of the current `interval`.

            count += 1

# Also, if the condition is true, `count` is incremented by 1.

    return len(intervals) - count

# Finally, the function returns the difference between the total number of intervals and the number of non-overlapping intervals. This is the minimum number of intervals that need to be erased to eliminate all overlaps.