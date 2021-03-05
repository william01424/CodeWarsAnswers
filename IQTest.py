'''
Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. 
Bob observed that one number usually differs from the others in evenness. 
Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.

! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

Examples:
iq_test("2 4 7 8 10") => 3 # Third number is odd, while the rest of the numbers are even

iq_test("1 2 1 1") => 2 # Second number is even, while the rest of the numbers are odd
'''

def iq_test(numbers):
    nums = numbers.split(' ')
    num_list = [int(numb) for numb in nums]
    evens = []
    odds = []
    for num in num_list:
        if num % 2 == 0:
            evens.append(num)
        else: odds.append(num)
    if len(evens) > 1:
        for i in num_list:
            if i % 2 != 0:
                return num_list.index(i) + 1
    else:
        for i in num_list:
            if i % 2 == 0:
                return num_list.index(i) + 1
