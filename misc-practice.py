# Stuff for fun/practice.

# 1. Implement a function to check if a string is a palindrome. You should
# ignore whitespaces and punctuation.
def isPalindrome(s):
    if len(s) == 1:
        return True
    # Remove anything that isn't a letter
    newString = ''
    for i in range(len(s)):
        if s[i].isalpha():
            newString += s[i]
    print(newString)
    for i in range( int(len(newString)/2) ): # We only need to check half the string
        if newString[i] != newString[-i-1]:
            return False
    return True
