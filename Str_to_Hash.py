'''
Please write a function that will take a string as input and return a hash. The string will be formatted as such. 
The key will always be a symbol and the value will always be an integer.

"a=1, b=2, c=3, d=4"
This string should return a hash that looks like

{ 'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''

def str_to_hash(str):
    if str == '':
        return {}
    list = str.split(', ')
    kv_pairs = []
    for element in list:
        a = [element.split('=')]
        kv_pairs += a
    hash = {}
    for kv_pair in kv_pairs:
        hash[kv_pair[0]] = int(kv_pair[1])
    return hash
