# Write a function called sumIntervals/sum_intervals() that accepts an array of intervals, and returns the sum of all the interval lengths. 
# Overlapping intervals should only be counted once.

# Intervals are represented by a pair of integers in the form of an array. The first value of the interval will always be less than the second value. 
# Interval example: [1, 5] is an interval from 1 to 5. The length of this interval is 4.

# sum_of_intervals([(1,4),(7,10),(3,5)]) = 7

def sum_of_intervals(intervals):
    list = []
    for i in intervals:   # For each index(list) in given list(intervals), I set a start and stop for range = to first and last value in indet(list)
        start = i[0]
        stop = i[-1]
        list.extend(range(start, stop))   # List extend is best here as we are printing a full range (always increment by 1 in this case [1 is default])
    RangeNums= []   # Ran into issues with appending when list[i] == list[i + 1] as we are removing the original list so it iterates out of range.
    for i in list:    # Easier to move unique numbers from 1 list to another
        if i not in RangeNums:
            RangeNums.append(i)
    return len(RangeNums)   # Return the length of the RangeNums list to get final answer


# NOTE: you can set start stop from the layout of the index itself (See below):

def sum_of_intervals(intervals):
    list = []
    for start, stop in intervals:       # Becuase index is in form [x1, x2] - we can say for x1, x2 in intervals do this i.e. we can assign values in the for loop statement
        list.extend(range(start, stop)) # rather than after. This makes the code 'cleaner'. In this case we assign start, stop as th
    RangeNums = []                      # range() >> range(start,stop,increment[set to 1 by default])
    for i in list:
        if i not in RangeNums:
            RangeNums.append(i)
    return len(RangeNums)
