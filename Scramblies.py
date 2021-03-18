'''
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
Input strings s1 and s2 are null terminated.

Examples

scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
'''

# Had a couple of tries doing this, both were just over the 12000 ms limit. Wasn't sure how to optimise, and checked solutions.

# Attemot 1:

def scramble(s1, s2):
    position = 0
    while position + 1 < len(s2):
        if s2[position] in s1:
            position += 1
        else: return False
    if position + 1 == len(s2):
        return True

# Attempt 2:

def scramble(s1, s2):
    complete = 0
    for character in s2:
        if s1.count(character) >= s2.count(character):
            complete += 1
    if complete == len(s2):
        return True
    else: return False
    
# Solution - was close as both solutions did function correctly. Issues with performance. 

def scramble(s1,s2):
    for c in set(s2):
        if s1.count(c) < s2.count(c):
            return False
    return True
