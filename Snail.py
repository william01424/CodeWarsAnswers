'''
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
'''

def snail(snail_map):
    snail_trail = []
    size = len(snail_map[0])**2

    while len(snail_trail) < size:

        if len(snail_map[0]) == 2:
            snail_trail += snail_map[0]
            snail_trail += snail_map[-1][::-1]
            return snail_trail
        if len(snail_map[0]) == 1:
            snail_trail += snail_map[0]
            return snail_trail

        n = len(snail_map[0])
        # top
        snail_trail += snail_map[0]

        # mid_right (n-2 squares)
        mid_right = []
        cs = 1
        while len(mid_right) < n - 2:
            mid_right.append(snail_map[cs][-1])
            cs += 1
        snail_trail += mid_right

        # bottom
        snail_trail += snail_map[-1][::-1]

        # mid_left (n-2 squares)
        mid_left = []
        cs = -2
        while len(mid_left) < n - 2:
            mid_left.append(snail_map[cs][0])
            cs -= 1
        snail_trail += mid_left

        # Deleting visited values
        del snail_map[0]
        del snail_map[-1]
        counter = 0
        while counter < n - 2:
            del snail_map[counter][0]
            del snail_map[counter][-1]
            counter += 1

    return snail_trail
