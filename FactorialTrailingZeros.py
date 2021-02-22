"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 * ... * N

Be careful 1000! has 2568 digits...
"""
# At first I solved using this method, however this causes runtime issues with large numbers, so a mathmatical method for calculating trailing 0s was required.

def factorial(n):   # Function to calculate the factorial value
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial * i
    return factorial

def zeros(n):   # Converts number to a string, then reverse counts the '0's until it hits a character other than '0'
    Zeros = 0
    if factorial(n) != 0:
        for x in reversed(str(factorial(n))):
            if x == '0':
                Zeros = Zeros + 1
            else: break
        return Zeros
    else: return 0

# See the following link for the maths behind this code: https://www.purplemath.com/modules/factzero.htm
 
def zeros(n):
    i = 5
    zeros = 0
    while n>= i:
        zeros = zeros + n // i
        i = i * 5
    return zeros
