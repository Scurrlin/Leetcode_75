# Merge Intervals

def merge(intervals: List[List[int]]) -> List[List[int]]:

# This line defines a function named `merge` that takes a list of lists (each
# containing two integers) as an argument and returns a list of lists.

    intervals.sort(key=lambda x: x[0])

# This line sorts the `intervals` list in ascending order based on the first
# element of each sublist. The `key` parameter of the `sort` function is a
# function that defines how to sort the elements. Here, it's a lambda function
# that takes an element `x` (a sublist in this case) and returns its first
# element (`x[0]`).

    merged = []

# This line initializes an empty list named `merged` that will store the merged
# intervals.

    for interval in intervals:

# This line starts a for loop that iterates over each sublist (`interval`) in
# the sorted `intervals` list.

        if not merged or merged[-1][1] < interval[0]:

# This line checks if `merged` is empty (`not merged`) or if the second element
# of the last sublist in `merged` is less than the first element of the current
# `interval`. This condition is true when there is no overlap between the last
# merged interval and the current interval.

            merged.append(interval)

# If the condition is true, the current `interval` is appended to the `merged`
# list.

        else:

# This line starts the else block, which is executed if the if condition is
# false, i.e., there is an overlap between the last merged interval and the
# current interval.

            merged[-1][1] = max(merged[-1][1], interval[1])

# If there is an overlap, the second element of the last sublist in `merged` is
# updated to be the maximum of its current value and the second element of the
# current `interval`. This effectively extends the last merged interval to
# include the current interval.

    return merged

# Finally, the function returns the `merged` list, which contains the merged
# intervals.