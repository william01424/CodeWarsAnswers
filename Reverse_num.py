'''
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

'''

class Solution:
  def reverse(self, num):
    if num == 0:
        return 0
    negative = False
    digits = [char for char in str(num)][::-1]

    if digits[-1] == '-':
        del digits[-1]
        negative = True

    ret = ''.join(digits)
    ret = ret.lstrip('0')

    if negative == True:
        ret = '-' + ret

    if -2**31 <= int(ret) <=2**31 - 1:
        return ret
    else:
        return 0
