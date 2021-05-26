'''
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

This is the first kata in series:
'''

def find_uniq(arr):
    non_dupe_values = list(set(arr))  # Cannot index into a set therefore used list after set applied.
    if arr.count(non_dupe_values[0]) > 1:
        return non_dupe_values[1]
    else:
        return non_dupe_values[0]
      
# See more condensed version:

def find_uniq(arr):
    a, b = set(arr) # Only ever 2 values therefore a, b = set(arr) assigns variable names effectively.
    return a if arr.count(a) == 1 else b
