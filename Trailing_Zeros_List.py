'''
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''

def move_zeros(array):
    for number in array:
        if number == 0:
            array.remove(number)
            array.append(0)
    return array

# This felt like more of a 7 Kyu problem - many other people in the comments thought the same way.
