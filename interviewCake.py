# Solutions for the questions on interviewcake.com.
# I don't have access to the full solutions, so I'm not always able to check
# that my answer is correct.

# 1. Suppose we could access yesterday's stock prices as a list where:
#       - The indicies are time in minutes past trade opening time, which was 9:30am
#       - The values are the prices in dollars of Apple stock at that time.
#       Ex. stock_prices_yesterday[60] = 500 represents a stock cost of $500 at 10:30am.
# Write an efficient function that takes stock_prices_yesterday and returns the best
# profit I could have made with one purchase and one sale of one stock. No shorting -- you
# must buy before you sell. You may not buy and sell at the same time either.

def get_max_profit(stock_prices_yesterday):
    # Keep track of the smallest value and the profit we've made. For each value, if the
    # profit is better, replace the profit. If we find a smaller value, replace the smallest
    # value.
    # Because we could have a negative profit (i.e. prices keep going down all day) or a
    # zero profit, we set maxProfit to a really large small number instead of zero.
    if len(stock_prices_yesterday) < 2:
        raise IndexError("We requires at least 2 prices.")
    maxProfit = -1000000
    lowestValue = stock_prices_yesterday[0]

    for i in range(1, len(stock_prices_yesterday)):     # Skip first index
        profit = stock_prices_yesterday[i] - lowestValue
        if profit > maxProfit:
            maxProfit = profit
        if stock_prices_yesterday[i] < lowestValue:
            lowestValue = stock_prices_yesterday[i]
    return maxProfit

# Test cases:
# get_max_profit([10, 7, 5, 8, 11, 9])    # Should return 6
# get_max_profit([10, 9, 8, 7, 6, 5])     # Should return -1
# get_max_profit([25, 75, 1, 2])          # Should return 25
# get_max_profit([10, 10, 10, 10, 10])    # Should return 0


# **** I don't think this is most optimal solution... 
# 2. You have a list of integers, and for each index, you want to find the product of
# every integer except the integer at that index. Write a function
# get_products_of_all_ints_except_at_index() that takes a list of integers and returns a
# list of products. 
#   Ex. Given [1, 7, 3, 4], return [84, 12, 28, 21] by calculating [7*3*4, 1*3*4, 1*7*4, 1*7*3]
# Do not use division in your solution. (That would be too easy! We could just calculate
# the product of every integer, then return that value/integer at each index.)

def get_products_of_all_ints_except_at_index(integerList):
    if len(integerList) <= 1:
        raise IndexError("We require at least 2 integers.")
    returnList = [1] * len(integerList)
    for i, value in enumerate(integerList):
        counter = 0
        while counter < len(integerList):
            if counter != i:
                returnList[counter] *= value
            counter += 1
    return returnList

# Test cases:
# get_products_of_all_ints_except_at_index([1, 7, 3, 4])    # [84, 12, 28, 21]
# get_products_of_all_ints_except_at_index([0, 0, 0])       # [0, 0, 0]


# 3. Given a list of ints, find the highest_product you can get from three of the ints.
# Assume the input will always have at least three integers.

def highest_product(integerList):
    # We can just grab the three largest integers and return their product.
    max1 = max2 = max3 = -100000
    min1 = min2 = 100000

    for value in integerList:
        if value >= max1:
            max3 = max2
            max2 = max1
            max1 = value
        elif value >= max2:
            max3 = max2
            max2 = value
        elif value > max3:
            max3 = value
        if value <= min1:
            min2 = min1
            min1 = value
        elif value < min2:
            min2 = value
    return max(max1 * max2 * max3, max1 * min1 * min2)

# Test cases:
# highest_product([-10, -10, 5, 9, 300])    # 30000
# highest_product([0, 0, 0])                # 0
# highest_product([1, 10, -20, 3])          # 30
# highest_product([5, 5, 3, 5])             # 125






# 43. Merge two sorted arrays into one sorted array.
# This assumes that if we have duplicates, we only want to count one. This is
# the merge part of mergesort!

def mergeSortedArrays(arr1, arr2):
    returnArray = []
    while len(arr1) > 0 and len(arr2) > 0:
        if arr1[0] > arr2[0]:
            minimum = arr2[0]
            del arr2[0]
        elif arr1[0] < arr2[0]:
            minimum = arr1[0]
            del arr1[0]
        else:
            minimum = arr1[0]
            del arr1[0]
            del arr2[0]
        returnArray.append(minimum)
    if len(arr1) > 0:
        returnArray += arr1
    elif len(arr2) > 0:
        returnArray += arr2
    return returnArray
