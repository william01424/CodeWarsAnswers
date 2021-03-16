'''
In this kata you have to create all permutations of an input string and remove duplicates, if present. 
This means, you have to shuffle all letters from the input in all possible orders.

Examples:

permutations('a'); # ['a']
permutations('ab'); # ['ab', 'ba']
permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
'''

# Hard part of this kata is knowing the itertools library.

def permutations(string):
  from itertools import permutations    # Very useful - remember difference betweeen product, permutations and combinations.
  All_results = list(map(''.join, permutations(string)))    # map() -- applies a function to an iterable, in this case ''.join to the permutations tuple.

  no_duplicates = set(All_results)    # Sets have no duplicates! Useful quality of sets.
  result = []
  for i in no_duplicates:   # Final result is wanted in list format.
    result.append(i)
  return result


# See this 'best practises' code for cleaner solution

import itertools

def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))
