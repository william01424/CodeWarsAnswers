'''
Find the sum of the digits of all the numbers from 1 to N (both ends included).

Examples
# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
'''

def compute_sum(n):
    num_list = [str(i) for i in range(n+1) if i > 9]
    split_nums = []
    for num in num_list:
        for digit in num:
            split_nums.append(int(digit))
    if n > 9:
        return sum(split_nums) + 45
    else:
        return sum(range(n+1))
      
# Note this 'cleaner' solution, however run time is very similar.

def compute_sum(n):
    return sum(int(c) for i in range(1, n+1) for c in str(i))
  
