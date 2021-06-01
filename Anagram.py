'''
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
Note for Go
For Go: Empty string slice is expected when there are no anagrams found.
'''

def anagrams(base_word, words):
    list = [word for word in words if len(base_word) == len(word)]
    sorted_words = []
    sorted_base_word = ' '.join(sorted(base_word))

    for word in list:
        a = ' '.join(sorted(word))
        sorted_words.append(a)

    index_counter = 0
    final_list = []
    for word in sorted_words:
        if sorted_base_word == word:
            final_list.append(list[index_counter])
        index_counter += 1
        if index_counter > len(list) - 1:
            break
    return final_list
  
  # Note much faster solution:
  
  def anagrams(word, words):
    match = sorted(word)
    return [w for w in words if match == sorted(w)]
