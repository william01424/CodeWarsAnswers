'''
In this simple exercise, you will create a program that will take two lists of integers, a and b. Each list will consist of 3 positive integers above 0, 
representing the dimensions of cuboids a and b. You must find the difference of the cuboids' volumes regardless of which is bigger.

For example, if the parameters passed are ([2, 2, 3], [5, 4, 1]), the volume of a is 12 and the volume of b is 20. Therefore, the function should return 8.

Your function will be tested with pre-made examples as well as random ones.

If you can, try writing it in one line of code.
'''

def find_difference(a, b):
    volume_a = 1
    volume_b = 1
    for i in a:
        volume_a *= i
    for i in b:
        volume_b *= i
    return abs(volume_a - volume_b)

# See top answer makes use of mumpy prod to reduce this to one line

from numpy import prod

def find_difference(a, b):
    return abs(prod(a) - prod(b))

  
# Alternatively this method also works in this scenario, however for multiplying larger lists, it causes issues.

def find_difference(a, b):
    return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])
