def array_diff(a, b):
    for i in b:
        while i in a:
            a.remove(i)         # For every value in list b, while that value is in a, remove that value
    return a

print(array_diff([1,2,2],[1]))          # Returns [2, 2]
