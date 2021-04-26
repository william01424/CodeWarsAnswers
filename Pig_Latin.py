'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
'''

def pig_it(text):
    list_of_words = text.split(' ')
    pig_latin = []
    for word in list_of_words:
        if word.isalpha() == False:
            pig_latin.append(word)
        else:
            start_char = word[0]
            pig_latin.append(word[1:] + start_char + 'ay')

    return ' '.join(pig_latin)
