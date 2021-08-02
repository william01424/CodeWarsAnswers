'''
Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return true if the string is valid, and false if it's invalid.

This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea!

All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.

What is considered Valid?
A string of braces is considered valid if all braces are matched with the correct brace.

Examples
"(){}[]"   =>  True
"([{}])"   =>  True
"(}"       =>  False
"[(])"     =>  False
"[({})](]" =>  False
'''

from collections import deque
def validBraces(string):
    stack = deque()
    for char in string:
        if len(stack) == 0 and (char == ')' or char == ']' or char == '}'):
            print('test')
            return False
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        if char == ')' and stack[-1] == '(':
            stack.pop()
        if char == ']' and stack[-1] == '[':
            stack.pop()
        if char == '}' and stack[-1] == '{':
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False
