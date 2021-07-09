'''
Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits. For example:

12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
'''
# Algo steps:
  # 1 Base cases, check if last 2 digits can be swapped for the answer i.e. if last digit is bigger, then swap them.
  # Check order of digits for the number, to see if a bigger answer is possible.
  # 2 Parsing from the right find first the digit that is smaller than the previous digit.
  # Then find the next digit to the right of that that is the next biggest of the chosen number.
  # 3 Swap those 2 numbers, then sort digits to the right of the first chosen index.
  
def next_bigger(n):
    if n < 10:
        return -1

    digits = list(str(n))
    if int(digits[-1]) > int(digits[-2]):   # Checks if last 2 digits can be swapped to get answer
        last_pair = digits[-2:]
        return int(''.join(digits[:-2] + last_pair[::-1]))

    bigger = False
    for i in range(1, len(digits)):     # Loop checks if next bigger exists
        if int(digits[i-1]) < int(digits[i]):
            bigger = True
    if bigger == False:
        return -1

    for i in range(1, len(digits)):      # Parsing from right, finds the index of number that is smaller than number
        if digits[-i-1] < digits[-i]:   # before it.
            pivot = -i - 1      # pivot is index not value.
            break
    print('the pivot is this:', pivot)
    min_digit = 10  # start variable with number greater than 9.
    min_digit_index = 0

    for i, digit in enumerate(digits[pivot + 1:]):
        if int(digit) < min_digit and int(digit) > int(digits[pivot]):
            min_digit = int(digit)
            min_digit_index = i + 1 + len(digits[:pivot])

    print('smallest digit:', min_digit)
    print('smallest digit index:', min_digit_index)

    # need to swap locations of digits[pivot] and min_digit
    moving_num = digits[pivot]  # variable used to keep track of number so swap is carried out correctly.
    digits[pivot] = digits[min_digit_index]
    digits[min_digit_index] = moving_num

    # Sort end segment to ascending after pivot then ret
    return int(''.join(digits[:pivot + 1] + sorted(digits[pivot + 1:])))
