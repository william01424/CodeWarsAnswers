'''
Write a function filter_long_words that takes a string sentence and an integer n.

Return a list of all words that are longer than n.

Example:

filter_long_words("The quick brown fox jumps over the lazy dog", 4) = ['quick', 'brown', 'jumps']
'''

def filter_words(sentence, n):
    list = sentence.split(' ')
    return [word for word in list if len(word) > n]
  
  
# Also note, this could be improved into one line if you add tthe split into the list comp (see here):

def filter_words(sentence, n):
    return [word for word in sentence.split() if len(word) > n]   # split() will default split on space
  
  
  
