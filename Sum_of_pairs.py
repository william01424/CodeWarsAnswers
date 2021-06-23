'''
Sum of Pairs
Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.

sum_pairs([11, 3, 7, 5],         10)
#              ^--^      3 + 7 = 10
== [3, 7]

sum_pairs([4, 3, 2, 3, 4],         6)
#          ^-----^         4 + 2 = 6, indices: 0, 2 *
#             ^-----^      3 + 3 = 6, indices: 1, 3
#                ^-----^   2 + 4 = 6, indices: 2, 4
#  * entire pair is earlier, and therefore is the correct answer
== [4, 2]

sum_pairs([0, 0, -2, 3], 2)
#  there are no pairs of values that can be added to produce 2.
== None/nil/undefined (Based on the language)

sum_pairs([10, 5, 2, 3, 7, 5],         10)
#              ^-----------^   5 + 5 = 10, indices: 1, 5
#                    ^--^      3 + 7 = 10, indices: 3, 4 *
#  * entire pair is earlier, and therefore is the correct answer
== [3, 7]
Negative numbers and duplicate numbers can and will appear.

NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.
'''

# O(n^2) Time complexity solution

def sum_pairs(ints, s):
    start_pointer = 0
    end_pointer = 1
    min_dist = [99999,99999]

    while start_pointer < len(ints):
        while end_pointer < len(ints):
            if ints[start_pointer] + ints[end_pointer] == s and end_pointer < min_dist[1]:
                min_dist = [start_pointer, end_pointer]
            elif ints[start_pointer] + ints[end_pointer] == s and end_pointer == min_dist and start_pointer < min_dist[0]:
                min_dist = [start_pointer, end_pointer]
            end_pointer += 1

        start_pointer += 1
        end_pointer = start_pointer + 1
    if min_dist == [99999,99999]:
        return None
    return [ints[min_dist[0]], ints[min_dist[1]]]
  
# O(n) Time complexity solution - this solution uses the set ds to keep track of visited values, meaning we dont need a nested loop.

def sum_pairs(ints, s):
    seen_nums = set()
    for int in ints:
        if s - int in seen_nums:
            return [s-int, int]
        else:
            seen_nums.add(int)
 
