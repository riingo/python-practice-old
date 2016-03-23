# Implement a singly-linked list.
class Node:
    'Implements a node of a singly-linked list.'
    def __init__(self, value=None, nextNode=None):
        self.value = value
        self.next = nextNode
    def getNext(self):
        return self.next
    def getValue(self):
        return self.value
    def setNext(self, nextNode):
        self.next = nextNode
    def setValue(self, value):
        self.value = value

class LinkedList:
    'Implements a singly-linked list.'
    def __init__(self):
        self.head = None # Head node is the first node
    def addNode(self, data): # Insertion and deletion for linked list has O(1) time!
        newNode = Node(data)
        if self.head is None:           # This is the first node
            self.head = newNode
        else:                           # Move along list until we get last node
            currNode = self.head
            nextNode = self.head.getNext()
            while nextNode is not None:
                currNode = nextNode
                nextNode = currNode.getNext()
            currNode.setNext(newNode)
    def delNode(self, data):
        prevNode = None
        currNode = self.head
        while currNode is not None:
            if currNode.getValue() == data:
                prevNode.setNext(currNode.getNext())
                break
            prevNode = currNode
            currNode = currNode.getNext()
        if currNode is None:        # We made it through the whole list
            return "Data not found."            
        return
    def findNode(self, data):
        # This is really similar to deleting a node.
        prevNode = None
        currNode = self.head
        while currNode is not None:
            if currNode.getValue() == data:
                return currNode
            prevNode = currNode
            currNode = currNode.getNext()
        return "Data not found."
    def getCount(self):             # Count the number of nodes in the list
        counter = 0
        currNode = self.head
        while currNode is not None:
            counter += 1
            currNode = currNode.getNext()
        return counter
    def getValues(self):            # Print out the contents of the linked list
        values = []
        currNode = self.head
        while currNode is not None:
            values.append(currNode.getValue())
            currNode = currNode.getNext()
        return values
    def reverse(self):              # Reverse the linked list iteratively
        oldNode = None
        currNode = self.head
        while currNode is not None:
            nextNode = currNode.getNext()
            currNode.setNext(oldNode)
            oldNode = currNode
            currNode = nextNode
        self.head = oldNode
    def reverse2(self, currNode, oldNode):  # Reverse the linked list recursively
        if currNode is None:
            # Base case where there is an empty list
            self.head = oldNode
            return
        nextNode = currNode.getNext()
        currNode.setNext(oldNode)
        oldNode = currNode
        return self.reverse2(nextNode, oldNode)
