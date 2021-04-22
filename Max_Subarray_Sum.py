'''
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. 
If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
'''

def max_sequence(arr):
    pointer1 = 0
    pointer2 = 0
    sum_position = 0
    max_sum = 0

    while pointer1 < len(arr):
        if pointer2 == len(arr):
            pointer1 += 1
            pointer2 = pointer1

        sum_position = sum(arr[pointer1:pointer2 + 1])
        pointer2 += 1

        if sum_position > max_sum:
            max_sum = sum_position
    return max_sum
