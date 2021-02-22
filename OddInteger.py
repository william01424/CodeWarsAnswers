'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
'''

# For this, I can import Counter from collections.

from collections import Counter

def find_it(seq):
    counted = dict(Counter(seq))    # Need to convert this to a dictionary so I can then access key provided value passes my condition.
    for key, value in counted.items():
        if value % 2 != 0:    # if value is odd return key
            return key

''' 
Note the following solution that doesn't use Counter
'''
def find_it(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i
