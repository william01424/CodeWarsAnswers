'''
Task
You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.

Examples
[7, 1]  =>  [1, 7]
[5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
'''

def sort_array(source_array):
    sorted_odd_nums = sorted([num for num in source_array if num % 2 == 1])
    
    index = 0
    final = []
    for num in source_array:
        if num % 2 == 1:
            final.append(sorted_odd_nums[index])
            index += 1
        else:
            final.append(num)
    return final
