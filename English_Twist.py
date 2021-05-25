'''
You will be given a list of strings, a transcript of an English Shiritori match. 
Your task is to find out if the game ended early, and return a list that contains every valid string until the mistake. If a list is empty return an empty list. 
If one of the elements is an empty string, that is invalid and should be handled.

Examples:
All elements valid:
The array {"dog","goose","elephant","tiger","rhino","orc","cat"}

should return {"dog","goose","elephant","tiger","rhino","orc","cat"}

An invalid element at index 2:
The array {"dog","goose","tiger","cat", "elephant","rhino","orc"}

should return ("dog","goose") since goose ends in 'e' and tiger starts with 't'
'''

def game(words):
    index_counter = 0
    if words.count('') >= 1:
        return words[:words.index('')]

    while index_counter < len(words) - 1:
        if words[index_counter][-1] == words[index_counter + 1][0]:
            index_counter += 1
        else:
            break
    return words[:index_counter + 1]
