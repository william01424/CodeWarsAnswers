'''
A list S will be given. You need to generate a list T from it by following the given process:

Remove the first and last element from the list S and add them to the list T.
Reverse the list S
Repeat the process until list S gets emptied.
Example
S = [1,2,3,4,5,6]
T = []

S = [2,3,4,5] => [5,4,3,2]
T = [1,6]

S = [4,3] => [3,4]
T = [1,6,5,2]

S = []
T = [1,6,5,2,3,4]

DO NOT CHANGE INPUT.
'''
# First solution was a lot cleaner but the run time was far too high for large lists.

def arrange(s):
    T = []
    front_pointer = 0
    rear_pointer = -1
    reverse = 0

    while len(T) < len(s):
        if len(T) + 1 == len(s):
            T += [s[len(s)//2]]
            return T

        append = [s[front_pointer], s[rear_pointer]]
        if reverse == 0:
            T += append
            reverse = 1
        elif reverse == 1:
            T += append[::-1]
            reverse = 0
        front_pointer += 1
        rear_pointer -= 1
    return T
