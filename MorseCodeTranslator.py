''' Decode the Morse code-- NOTE: This is my first iteration and is not optimal'''

def decodeMorse(morse_code):
    CODE_REVERSED = {'A': '.-', 'B': '-...', 'C': '-.-.',     # Created my own dictionary which includes 'most' morsecode characters and some punctuation
            'D': '-..', 'E': '.', 'F': '..-.',
            'G': '--.', 'H': '....', 'I': '..',
            'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',
            'S': '...', 'T': '-', 'U': '..-',
            'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', ' ':'', 'SOS':'...---...', '!':'-.-.--', '.':'.-.-.-',

            '0': '-----', '1': '.----', '2': '..---',
            '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..',
            '9': '----.'
            }

    MORSE_CODE = {value: key for key, value in CODE_REVERSED.items()}     # Had to reverse it so it was input:output rather than output:input
    morse_code = morse_code.lstrip().rstrip()     # Removing whitespace to left and right as that is nothing to translate
    morse_list = morse_code.split(' ')
    cracked_code = []

    for char in morse_list:
        cracked_code.append(MORSE_CODE[char])
        if char == '':    # This removes one of the empty characters in the list which come after every word (was 2 after every word now there is only 1)
            morse_list.remove('')
    cracked_string = ('').join(cracked_code) # Then use the remaining '' index in list as a joiner i.e. space
