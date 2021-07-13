'''
A format for expressing an ordered list of integers is to use a comma separated list of either

individual integers
or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string in the range format.

Example:

solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-6,-3-1,3-5,7-11,14,15,17-20"
'''

def solution(args):
    range_extracted = []
    range_counter = 0
    i = 1

    while i < len(args):
        if args[i-1] == args[i] + 1 or args[i-1] == args[i] - 1:
            while args[i - 1 + range_counter] - args[i + range_counter] == -1:
                range_counter += 1
                if i + range_counter >= len(args):
                    break
            if args[i-1] + 1 == args[i-1 + range_counter]:
                range_extracted.append(str(args[i - 1]))
                range_extracted.append(str(args[i - 1 + range_counter]))
            else:
                range_extracted.append(f"{args[i-1]}-{args[i-1 + range_counter]}")
            i += range_counter
            range_counter = 0
        else:
            range_extracted.append(str(args[i-1]))
        i += 1
        
    # This section below cleans up an issue with missing the last index. If we loop 1 more time through the while loop,
    # we get out of index error due to poor initial loop construction...
    
    range_extracted.append(str(args[-1]))
    if range_extracted[-1] == range_extracted[-2]:
        del range_extracted[-1]
    elif str(range_extracted[-1]) in range_extracted[-2]:
        del range_extracted[-1]

    return ','.join(range_extracted)
