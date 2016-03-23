# These questions have to do with linked lists, so we'll use our implementation
# of a singly linked list.
from singly_linked import *

# 2.1: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP: How would you solve this problem if a temporary buffer is not
# allowed?
def removeDupes(linkList):
    if linkedList.head is None:
        return
    seen = {}       # Use a dictionary as temporary buffer to track which
                    # values we've seen. Dict has O(1) lookup time.
    prevNode = None
    currNode = linkList.head
    while currNode is not None:     # Go through list and check the value of node
        if currNode.getValue() in seen.keys():   # If we've seen it:
            prevNode.setNext(currNode.getNext())              # Set previous node's next node to the current node's next node
            currNode = currNode.getNext()
        else:
            seen[currNode.getValue()] = True    # If not, add to seen list
            prevNode = currNode
            currNode = currNode.getNext()
def removeDupes2(linkList):
    # Witout using a temp buffer means we need to do this in O(n^2) time.
    if linkedList.head is None:
        return
    prevNode = None
    currNode = linkList.head
    while currNode is not None:
        prevNode2 = currNode
        currNode2 = currNode.getNext()
        while currNode2 is not None:
            if currNode2.getValue() == currNode.getValue(): # Seen it!
                prevNode2.setNext(currNode2.getNext())
                currNode2 = currNode.getNext()
            else:
                prevNode2 = currNode2
                currNode2 = currNode2.getNext()
        prevNode = currNode
        currNode = currNode.getNext()

# 2.2: Implement an algorithm to find the kth to last element of a singly linked
# list.
def elemK(linkList, k):
    if k > linkList.getCount() or linkList.head is None:
        return "Invalid arguments. (Linked list is empty or k is too large.)"
    counter = 0
    returnNode = linkList.head
    while counter != (linkList.getCount() - k):
        counter += 1
        returnNode = returnNode.getNext()
    return returnNode.getValue()
        
def elemK2(linkList, k):
    # We can also do this without knowing how many elements are in the list.
    # Use two runners. One starts at the beginning of the list, the second
    # starts at k. When the second one hits the end of the list, the first one
    # should be at the value we return.
    if linkList.head is None:
        return "Invalid argument. Linked list is empty."
    runner1 = linkList.head
    runner2 = linkList.head
    counter = 0
    while counter < k:
        runner2 = runner2.getNext()
        if runner2 is None:
            return "Invalid argument. k is larger than the list."
        counter += 1
    # Now we have r1 at the head and r2 at k, so we can start moving both.
    while runner2 is not None:
        runner1 = runner1.getNext()
        runner2 = runner2.getNext()
    return runner1.getValue()

# 2.3: Implement an algorithm to delete a node in the middle of a singly linked
# list, given only access to that node. (So not given head of the list.)
# EXAMPLE:
#   Input: node c from the linked list a -> b -> c -> d -> e
#   Result: list should look like a -> b -> d -> e
def delMidNode(node):
    if node is None:
        return "Node is null."
    nextNode = node.getNext()
    if nextNode is None:
        return "This is the last element of the list." # Not solvable
    node.setNext(nextNode.getNext())
    node.setValue(nextNode.getValue())
    
# 2.4: Write code to partition a linked list around a value x, such that all
# nodes less than x come before all nodes greater than or equal to x.
# We assume that x can be any number, not necessarily one that's in thet list.
# We also assume that the left and right partitions don't need to be in any
# order.
def partitionList(linkList, x):
    # We do this by making two new linked lists for the right and left
    # partitions, then merging them.
    rightNodes = None       # Keep track of right node
    leftNodes = None        # Keep track of left node
    currNode = linkList.head
    while currNode is not None:
        if currNode.getValue() >= x:        # Right side, add nodes to the left
            nextNode = currNode.getNext()   # (Keep replacing the head node)
            currNode.setNext(rightNodes)
            rightNodes = currNode
            currNode = nextNode
        else:
            if leftNodes is not None:       # Left side, add nodes to the right
                leftNodes.setNext(currNode) # (Keep adding to the tail node)
            leftNodes = currNode
            currNode = currNode.getNext()
    if leftNodes is not None:               # Merge the nodes (same as doing 
        leftNodes.setNext(rightNodes)       # nothing if rightNodes are empty).
    else:                                   # If left side is empty, just set
        linkList.head = rightNodes          # the list's head to the new head.

# 2.5: You have two numbers represented by a linked list, where each node
# contains a single digit. The digits are stored in reverse order, such that
# the 1s digit is the head of the list. Write a function that adds the two
# numbers and returns the sum as a linked list.
# EX:
#   Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is, 617+295
#   Output: (2 -> 1 -> 9). That is, 912.
def backwardDigitAddition(list1, list2):
    # When we normally add, we start with the 1s place and move upwards.
    # So this is actually the easier direction to add.
    if list1 is None and list2 is None:
        return None
    node1 = list1.head
    node2 = list2.head
    sumList = linkedList()  # linked list for the sum
    carryOver = 0

    while node1 is not None or node2 is not None:
        if node1 is not None:
            digit1 = node1.getValue()
        else:
            digit1 = 0
        if node2 is not None:
            digit2 = node2.getValue()
        else:
            digit2 = 0

        sumValue = carryOver + digit1 + digit2
        sumList.addNode(sumValue % 10)  # Remainder goes into current digit's place in answer
        carryOver = sumValue // 10      # Carry over

        if node1 is not None:
            node1 = node1.getNext()
        if node2 is not None:
            node2 = node2.getNext()
    return sumList
# I think the above is pretty ugly with all the if/else parts. It would be nice if we could use Python's
# ternary condition expression: (falseValue, trueValue)[test]. But this doesn't have short circuit
# behavior, meaning that both falseValue and trueValue will be evaluated regardless of the result of "test".
# This causes a problem if we want to do something like digit = (node.getValue(), 0)[node is None].
# Oh well. :/

# Suppose the digits are stored in forward order. Repeat the problem.
# EX:
#   Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617+295
#   Output: (9 -> 1 -> 2). That is, 912.

def forwardDigitAddition(list1, list2):
    # Similar to the above, but it's a bit tricky handling carryover values. We need to check every time
    # we add stuff together to see if it would have created a carryover value. If so, we need to go back
    # to the relevant node and add the carryover.
    if list1 is None and list2 is None:
        return None
    node1 = list1.head
    node2 = list2.head
    sumList = linkedList()      # linked list for the sum
    sumListPrev = None
    carryOver = 0

    while node1 is not None or node2 is not None:
        if node1 is not None:
            digit1 = node1.getValue()
        else:
            digit1 = 0
        if node2 is not None:
            digit2 = node2.getValue()
        else:
            digit2 = 0

        sumValue = carryOver + digit1 + digit2
        carryOver = sumValue // 10

        if carryOver > 0:                       # Go back and add to previous node
            if sumList is None:                 # Add new digit
                sumList.addNode(carryOver)
                sumListPrev = sumList.head      # Keep track of previous value
            else:                               # Existing number there
                sumListPrev.setValue(sumListPrev.getValue() + carryOver)
            carryOver = 0
        sumList.addNode(sumValue % 10)
        if sumListPrev is None:         # If this was the first node we added
            sumListPrev = sumList.head
        else:
            sumListPrev = sumListPrev.getNext()

        if node1 is not None:
            node1 = node1.getNext()
        if node2 is not None:
            node2 = node2.getNext()
    return sumList
        
# This code looks so ugly. ;_; Looking in CTCI, we can do everything for this question recursively which
# would probably make it nicer. 

# 2.6: Given a circular linked list, implement an algorithm which returns the node at the
# beginning of the loop.
# EX:
#   Input: A -> B -> C -> D -> E -> C (the same C as earlier)
#   Output: C
def circularList(lst):
    # The first thing we could do is keep a list of the nodes we've seen and if we go back to one,
    # then that node must be the beginning of the circular loop. If we put this list of seen nodes
    # in a hash table (or dictionary), then it only has O(1) lookup. 
    seen = {}
    currNode = lst.head
    while currNode is not None:
        if currNode in seen.keys():
            return currNode
        seen[currNode] = True
        currNode = currNode.getNext()
    return "Non-circular linked list."

# Another solution uses the "runner" technique.
# We'll use two "runners", one moving at 1 node at a time and the other moving at 2. Eventually
# they will meet each other if there is a loop in the list (otherwise one will hit the end).
# TODO

# 2.7: Implement a function to check if a linked list is a palindrome. 







    
