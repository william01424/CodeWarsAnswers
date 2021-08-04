'''
Reverse a string without allocating additional memory.
'''
def reverseString(list):
    # create a front and rear pointer
    # increment the pointers by one position to the middle, swapping each value
    # end when front pointer is no longer less than rear i.e. are the same or rear is in front of front pointer

    front_pointer = 0
    rear_pointer = len(list) - 1

    while front_pointer < rear_pointer:
        list[front_pointer], list[rear_pointer] = list[rear_pointer], list[front_pointer] # swaps in place without having to create a holder value.
        front_pointer += 1
        rear_pointer -= 1
