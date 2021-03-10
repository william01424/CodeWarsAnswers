'''
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" (as a string)
'''

def alphabet_position(text):
    from string import ascii_lowercase
    text = text.lower()   # Convert all text to lower case (upper case has different ascii code)

    Characters = {character : str(index) for index, character in enumerate(ascii_lowercase, start = 1)}   
    # Creates dict from ascii lowercase and uses enum to assign values from 1
    
    nums = [Characters[character] for character in text if character in Characters]   # List comp - Characters[character] == value
    return ' '.join(nums)   # Rejoin list to str
  
  # See this far simpler method:
  
  def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())    # Using ord() and isalpha() [to ignore ' ' and '.' etc] 
