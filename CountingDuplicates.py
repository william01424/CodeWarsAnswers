'''
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
'''

def duplicate_count(text):
    characters = [i.lower() for i in text]
    duplicatechars = []
    uniquechars = []
    for i in characters:
        if characters.count(i) > 1:
            duplicatechars.append(i)
    for i in duplicatechars:
        if i not in uniquechars:
            uniquechars.append(i)
    return len(uniquechars)
  
 # Using set as it doesn't include dupes to make this a little cleaner

def duplicate_count(text):
    characters = [i.lower() for i in text]
    uniquechars = set()
    for i in characters:
        if characters.count(i) > 1:
            uniquechars.add(i)
    return len(uniquechars)
  
 # See far cleaner solution 
  
 def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
