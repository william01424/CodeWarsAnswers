Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

def find_short(s):
    list = s.split(' ') # Splits the original string after every space to give list of words in str.
    l = []
    for i in list:
        l.append(len(i)) # For every word in the list, append the length of the word to a new list
    l.sort()    # Sort the list
    l = l[0]    # print the first value (lowest)
    return l
    
# This was my method at the time (very beginner level) - there are simpler methods.
    
i.e:
def find_short_faster(s):
  return min(len(x) for x in s.split(' ')) # Uses min()
    
