# 1. Write a function to swap a number in place.
def swapNums(a, b):
##    0 --------- a ---- b
##                  diff
##    0 ---- b -- a   # set b = diff
##      diff
##
##    0 ---- b --(a)---- a # a = a + diff
##      diff        diff
##
##    0 --------- b ---- a # b = a - diff
##
##    # This is the case where a < b to start with tho.
    if a < b:
        b = (b - a)
        a += b
        b = a - b
    elif a > b:
        a = (a - b)
        b += a
        a = b - a
    return (a, b)
