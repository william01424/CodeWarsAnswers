# Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

def make_readable(seconds):
    HH = seconds // 3600    # Hours as whole number
    MM = int((seconds / 60) - (HH*60))    # total minutes - hours as minutes = remaining minutes
    SS = seconds - ((MM*60)+(HH*3600))    # total seconds - minutes as seconds + hours as seconds = remaining seconds
    return f"{HH:02d}:{MM:02d}:{SS:02d}"    # formatted to 00:00:00 form using f insertion {:02d} -- (Don't need the d?)
