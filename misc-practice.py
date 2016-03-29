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

# 2. Implement a function to check if a string is an anagram of another string.
# Here, s1 is the original string and s2 is the anagram string.
def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    s2_list = list(s2)
    for char in s1:
        if char in s2_list:
            s2_list.remove(char)
        else:
            return False
    if len(s2_list) == 0:
        return True

# 3. You want to buy bus tickets for the next month. You know exactly which days
# you will be travelling. The month has 30 days and there are 3 types of
# tickets you can buy.
#       1-day ticket: costs 2, valid for one day
#       7-day ticket: costs 7, valid for seven consecutive days
#       30-day ticket: costs 25, valid for all 30 days.
# You want to pay as little as possible. You are given a sorted (in increasing
# order array of dates you will be travelling. Write a function that will
# return the minimum amount of money you have to spend on tickets.
def minTickets(travelDays):
    priceOne = 2
    priceSeven = 7
    priceThirty = 25
    if len(travelDays) >= 25:
        # (7 x 3) + (2 x 2) = 21 + 4 = 25. That means if we have 23 days of
        # travel and at least 21 of them are consecutive, then it's the same
        # to buy the 30-day tickets as to buy 3x 7-day and 2x 1-day. 
        return(priceThirty)
    elif len(travelDays) < 4:
        # If there are less than 7 travel days, we might think it would be
        # cheapest to buy all one-day tickets. But what if those days are all
        # within one week? i.e. travel 6 consecutive days, but not the seventh.
        # Then, it would be cheaper to buy the seven-day ticket.
        # If we have 1, 2, 3 travel days, it's cheaper to buy one-day tickets
        # since 2 x 3 = 6 max cost. If we have four days that happen to be
        # within the same week, it's cheaper to buy the seven-day ticket since
        # 7 < (2 x 4).
        return(len(travelDays) * priceOne)
    # First, since the array is sorted, it shouldn't be hard to figure out
    # consecutive days. The difference between each number and the next will
    # just be one.
    # We can go through the list and find the runs of consecutive days.
    # Actually, we just want to find cases where there are 4 or more days that
    # lie within a 7-day period. (See above explanation.) 
    consecutiveDays = []
    discardedDays = []
    consecutivePeriods = 0
    singleDays = 0
    minSum = 0
    for i, day in enumerate(travelDays):
        if len(consecutiveDays) == 0:
            consecutiveDays.append(day)
        else:
            if day <= (consecutiveDays[0] + 6): # Within the consecutive period
                consecutiveDays.append(day)
            else:   # Outside the consecutive period
                if day <= (consecutiveDays[1] + 6): # See Note below.
                    discardedDays.append(consecutiveDays[0])
                    consecutiveDays.remove(consecutiveDays[0])
                    consecutiveDays.append(day)
                elif len(consecutiveDays) >= 4: 
                    consecutivePeriods += 1
                    consecutiveDays = [day]
                else:
                    singleDays += len(consecutiveDays)
                    consecutiveDays = [day]
    if len(consecutiveDays) >= 4:
        consecutivePeriods += 1
    else:
        singleDays += len(consecutiveDays)
    if len(discardedDays) >= 4:
        minSum += minTickets(discardedDays)
    else:
        singleDays += len(discardedDays)
    return (singleDays * 2 + consecutivePeriods * 7 + minSum) 
        
    # Note:
    # We need this if statement because otherwise in some cases we won't
    # actually get the minimum ticket price!
    # What if we have [1, 6, 7, 8, 9, 28]? The best case here is to buy
    # a 7-day period ticket and use it on days 6, 7, 8, 9. Then buy 1-day
    # tickets for day 1 and 28, for a total cost of 11. But we will get a result
    # of 12 for 6 individual days. 
    # We should add an if-statement to check:
    #   If we find a date larger than consecutiveDays[0] + 6, check if it is 
    #   less than consecutiveDays[1] + 6. If so, then move thet list up by one.
    #   That is, discard consecutiveDays[0] and add the new date to the list. 

    # But wait! What if we run into a sequence of 14 consescutive days? Using
    # this code, we will end up with one consecutive period and 7 single days.
    # The best thing I came up with was making another list, discardedDays, and
    # recursively calling this function on it in case there was another sequence
    # of consecutive days in it. This makes the runtime O(n^2) though, I think.

# 4. Given an array of numbers, find the longest alternating subsequence.
# That is, a subsequence [a1, a2, a3, ..., ak] where a1 > a2, a2 < a3, a3 > a4,
# a1    a3    ...       or       a2    a4
#    a2    a4                 a1    a3    ...
def altSequence(nums):
    if len(nums) < 2:
        return nums
    # Create a subsequence array. We'll put tuples in this of the form
    # (index, up/down/either). This is the index of the number in the nums
    # array and then a value of 1 (expect next number to be bigger), -1 (expect
    # next number to be smaller) or 0 (can be either).
    # Keep track of lastNum. This is the last number we added to the array.
    subsequence = []
    subsequence.append((nums[0], 0))
    longest = []
    
    # Go through the list of numbers and for each one, check the last value of
    # subsequence and see if the current number follows the expectation in the
    # tuple. If yes, then append the index and update lastNum. If no, then
    # see if the length of subsequence is longer than the length of the longest
    # subsequence we've seen so far. If yes, then replace it. Unfortunately,
    # this means we have to keep track of two lists, giving us O(2n) space.
    for i in range(1, len(nums)):
        expectation = subsequence[len(subsequence) - 1]
        if nums[i] > expectation[0] and expectation[1] == 1:
            subsequence.append((nums[i], -1))
        elif nums[i] < expectation[0] and expectation[1] == -1:
            subsequence.append((nums[i], 1))
        elif expectation[1] == 0:
            if nums[i] > expectation[0]:
                subsequence.append((nums[i], -1))
            else:
                subsequence.append((nums[i], 1))
        else:
            if len(subsequence) > len(longest):
                longest = subsequence
            subsequence = [(nums[i], 0)]
    if len(subsequence) > len(longest):
        longest = subsequence
    subsequence = [x[0] for x in longest]
    return subsequence
