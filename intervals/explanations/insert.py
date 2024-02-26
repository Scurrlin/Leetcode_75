# Insert Interval

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

# This line defines a function named `insert` that takes two arguments: `intervals`, a list of lists of integers, and `newInterval`, a list of integers. The function returns a list of lists of integers.

    left, right = [], []

# This line initializes two empty lists, `left` and `right`.

    start, end = newInterval[0], newInterval[1]

# This line assigns the first and second elements of `newInterval` to `start` and `end` respectively.

    for interval in intervals:

# This line starts a loop that iterates over each `interval` in `intervals`.

        if interval[1] < start:

# This line checks if the second element of the current `interval` is less than `start`.

            left.append(interval)

# If the condition is true, the current `interval` is appended to the `left` list.

        elif interval[0] > end:

# If the first condition is not met, this line checks if the first element of the current `interval` is greater than `end`.

            right.append(interval)

# If the second condition is true, the current `interval` is appended to the `right` list.

        else:

# If neither of the first two conditions is met, the code enters this else block.

            start = min(start, interval[0])

# This line updates `start` to be the minimum of the current `start` and the first element of the current `interval`.

            end = max(end, interval[1])

# This line updates `end` to be the maximum of the current `end` and the second element of the current `interval`.

    return left + [[start, end]] + right

# This line returns the concatenation of the `left` list, a list containing `start` and `end`, and the `right` list. This effectively inserts the new interval into the correct position in the sorted list of intervals.