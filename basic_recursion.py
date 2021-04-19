'''
Print numbers 1-100 without using any type of loop within Python.
'''
# Basic recursion example:

def numbers(number):
    number += 1
    if number <= 100:
        print(number)
    numbers(number)
    
    
