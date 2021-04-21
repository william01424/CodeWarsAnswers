'''
Complete the method/function so that it converts dash/underscore delimited words into camel casing. 
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
'''

def to_camel_case(text):

    text = text.replace('-', ' ')
    text = text.replace('_',' ')

    split_words = text.split(' ')

    camel_case = [] + [split_words[0]]
    for word in split_words[1:]:
        camel_case.append(word.title())

    return ''.join(camel_case)
  
  ## NOTE - you can apply multiple actions to a single varialbe i.e. text.replace().replace().split()
  
  def to_camel_case(text):

    split_words = text.replace('-', ' ').replace('_',' ').split(' ')
    
    camel_case = [] + [split_words[0]]
    for word in split_words[1:]:
        camel_case.append(word.title())

    return ''.join(camel_case)
  
