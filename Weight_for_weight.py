'''
My friend John and I are members of the "Fat to Fit Club (FFC)". 
John is worried because each month a list with the weights of members is published and each month he is the last on the list which means he is the heaviest.

I am the one who establishes the list so I told him: "Don't worry any more, I will modify the order of the list". It was decided to attribute a "weight" to numbers. 
The weight of a number will be from now on the sum of its digits.

For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list 100 will come before 99.

Given a string with the weights of FFC members in normal order can you give this string ordered by "weights" of these numbers?

Example:
"56 65 74 100 99 68 86 180 90" ordered by numbers weights becomes: 

"100 180 90 56 65 74 68 86 99"
When two numbers have the same "weight", let us class them as if they were strings (alphabetical ordering) and not numbers:

180 is before 90 since, having the same "weight" (9), it comes before as a string.

All numbers in the list are positive numbers and the list can be empty.

Notes
it may happen that the input string have leading, trailing whitespaces and more than a unique whitespace between two consecutive numbers
For C: The result is freed.
'''
def order_weight(strng):
  # Split string into list and remove all possible whitespace
    original_list = [num for num in strng.split(' ')]
    new_list = [num for num in original_list if num.isnumeric() == True]
  # Split nums into their digits, convert to ints for sum() - creating list of sums for ordering
    digits = [list(num) for num in new_list]
    for num in digits:
        for i in range(0, len(num)):
            num[i] = int(num[i])
    sum_list = [sum(num) for num in digits]
    
    # Zipping two lists then sorting based on sum_list. Then using .join() function to return string with correct weight orders!

    return ' '.join([x for _,x in sorted(zip(sum_list, new_list))])
  
# See best solution:

def order_weight(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))    # Need to find out what this lambda does!!
