'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
'''
def generate_hashtag(s):
    if len(s) > 140 or s == '': return False    # Initial constraints
    s = s.title()   # Caps every word
    s = s.replace(" ","")   # Replaces spaces with nothing.
    hash = '#' + s    # Add '#' to s and return hash (the final answer)
    return hash


# Please see this cleaner response:
'''
This solution combines the string actions together s.action1().action2().
It also has both conditions into one inequality i.e. 0<len(s)<=140
All code is condensed to one line.
'''
def generate_hashtag(s): return '#' +s.title().replace(' ','') if 0<len(s)<=140 else False

