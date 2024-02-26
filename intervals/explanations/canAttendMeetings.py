# Meeting Rooms (Leetcode Premium)

def canAttendMeetings(intervals: List[List[int]]) -> bool:

# This line defines a function named `canAttendMeetings` that takes a list of lists (each containing two integers) as an argument and returns a boolean.

    intervals.sort(key=lambda x: x[0])

# This line sorts the `intervals` list in ascending order based on the first element of each sublist. The `key` parameter of the `sort` function is a function that defines how to sort the elements. Here, it's a lambda function that takes an element `x` (a sublist in this case) and returns its first element (`x[0]`).

    for i in range(1, len(intervals)):

# This line starts a for loop that iterates over the indices of the `intervals` list, starting from the second index.

        if intervals[i][0] < intervals[i-1][1]:

# This line checks if the first element of the current interval is less than the second element of the previous interval. This condition is true when the current interval starts before the previous interval ends, which means the meetings overlap.

            return False

# If the condition is true, the function returns `False`, indicating that it's not possible to attend all meetings without any overlaps.

    return True

# If the function has not returned `False` after checking all intervals, it returns `True`, indicating that it's possible to attend all meetings without any overlaps.