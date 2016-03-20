# 1.1
# Implement an algorithm to determine if a string has all unique characters.
def uniqueChars(s):
    if len(s) > 26: # There are only 26 letters!
        return False
    seenChars = set() # The set data structure has O(1) membership test time compared to an array
    for letter in s:
        if letter in seenChars:
            return False
        seenChars.add(letter);
    return True
# This has time complexity O(n) * O(1) = O(n)

# 1.2
# Implement a function void reverse(char* str) in C or C++ which reverses a null-terminated string.


# 1.3
# Given two strings, write a method to decide if one is a permutation of the other.
def isPermutation(s1, s2):
    if len(s1) != len(s2):
        return False
    if sorted(s1) != sorted(s2): # If they're permutations, they'll have the same letter seq when sorted.
        return False
    return True
# This has time complexity O(n log n) * 2 = O(n log n). (Python's sorting algorithm is Timsort which takes O(n log n) time.)

# Alternatively, we could do by counting the occurences of each letter.
def isPermutation2(s1, s2):
    if len(s1) != len(s2):
        return False
    letterCounts = {} # Key:Value is letter:occurences
    for letter in s1:
        letterCounts[letter] = letterCounts.get(letter, 0) + 1 # Return 0 if there is no entry
    for letter in s2:
        if (letterCounts.get(letter, 0) - 1) < 0: # A negative number would mean a letter appeared in s2 that doesn't appear in s1
            return False
    return True
# This has time complexity O(n) + O(n) = O(n).

# 1.4
# Write a method to replace all spaces in a string with "%20".
def changeSpaces(s):
    returnString = ''
    prior = 0
    for i, letter in list(enumerate(s)):
        if letter == ' ':
            returnString += s[prior:i] # The part before the space
            returnString += "%20" # The replacement
            prior = i + 1
    returnString += s[prior:] # Add stuff after the last space, if there's anything.
    return returnString
# This has time complexity O(n) since we go through the string once.

# 1.5
# Implement a method to perform basic string compression using the counts of repeated characters.
# For example, string 'aabbcd' would become 'a2b2c1d1'. If the "compressed" string would not become smaller
# than the original string, return the original string.
def stringCompression(s):
    returnString = ''
    count = 1
    for i in range(len(s)):
        if (i + 1) < len(s):
            if s[i] == s[i+1]: # Same as next character
                count += 1
            else:
                returnString += s[i] + str(count)
                count = 1
        else: # Handle the last character
            returnString += s[i] + str(count)
    if len(returnString) >= len(s):
        return s
    return returnString
# This one feels kind of ugly. The time complexity is O(n) since we have one for loop through range(len(s)).

# 1.6
# Given an image represented by a NxN matrix, where each pixel in the image is 4 bytes, write a method to
# rotate the image by 90 degrees. Can you do this in place?


# 1.7
# Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.


# 1.8
# Assume you have a method isSubstring which checks if one word is a substring of another. Given two strings,
# s1 and s2, write code to check if s2 is a rotation of s1 using only one call to isSubstring.
# def checkRotate(s1, s2):
#    if len(s1) != len(s2):
#        return False
#    return isSubstring(s1+s1, s2)

# I had to look at the solutions for this one. Important thing to notice is that if s1 = xy and s2 = yx,
# yx will always be a subset of xyxy. 






    
