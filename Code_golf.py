'''
Re-write the initial function below so that it is 31 characters or less:

def f(iterable, integer):
    length = len(iterable)
    if length > integer:
        return length
    else:
        return 0
This simple function takes an input iterable and an integer. 
If the length of the iterable is larger than the integer it returns that length. Otherwise it returns zero. 
All inputs will be valid and and all iterables will have a defined length.
'''

# Anonymous functions in python to drop character count down. Replace if else with [][] notation. Use := to assign variable mid function.
# Remove all spaces.

# Attempt 1 (too long..):
def f(l,i):
 return[0,x:=len(l)][x>i]


# Attempt 2 (after googling code golf basics)

f=lambda x,l,i:[0,x:=len(l)][x>i]
