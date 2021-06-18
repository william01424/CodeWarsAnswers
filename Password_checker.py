'''
You need to write a function that will validate a password to make sure it meets the following criteria:

At least six characters long
contains a lowercase letter
contains an uppercase letter
contains a number
Valid passwords will only be alphanumeric characters.
'''
# Note original kata wanted some sort of regex, but I just wrote a function variant as I was unsure in answer format it was looking for...

def password_check(str):
    if len(str) < 6:
        return False

    lower_count = 0
    upper_count = 0
    number_count = 0

    for char in str:
        if char.islower() == True:
            lower_count += 1
        if char.isupper() == True:
            upper_count += 1
        if char.isnumeric() == True:
            number_count += 1
        if char.isalnum() == False:
            return False
    if lower_count > 0 and upper_count > 0 and number_count > 0:
        return True
    else:
        return False
