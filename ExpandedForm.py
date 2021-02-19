expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

def expanded_form(num):
    list = []
    n = (len(str(num)))   # Number of digits within num
    while n > 0:    # This loop will append each digit as a str + (n-1)*'0's UNLESS digit is '0'
        for i in str(num):
            n = n - 1
            if i != '0':
                list.append(str(i) + (n*'0'))
    String = ''.join([x + ' + ' for x in list])   # ''.join() function - joins (index + ' + ') as a string
    ExpandedForm = String[:-3]    # need to remove the final ' + ' aka final 3 characters
    return ExpandedForm
