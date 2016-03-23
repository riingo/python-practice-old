# Implements a stack data structure. We could implement this as a linked
# list that prevents the user from "peeking" past the top node. :)
from singly_linked import *

class Stack:
    def __init__(self, data=None):
        self.top = Node(data)
    def push(self, data):
        # New top node should point to the old top node
        newTop = Node(data)
        newTop.setNext(self.top)
        self.top = newTop
    def pop(self):
        returnVal = self.top
        if returnVal is not None:
            # Change the top node to whatever comes after the top node 
            self.top = returnVal.getNext()
        return returnVal
    def peek(self):
        # Return the top node's value
        return self.top

# Implements a queue data structure. Same idea, except it's FIFO.
class Queue:
    def __init__(self, data=None):
        self.first = Node(data)
        self.last = self.first
        self.last.setNext(self.first)
    def enqueue(self, data):
        # If this is the first thing we're adding, the first and last are the same
        if self.first.getValue() is None:
            self.first = Node(data)
            self.last = self.first
            self.last.setNext(self.first)
        # Otherwise, we set the new item to be last and point it at the old last.
        else:
            newLast = Node(data)
            newLast.setNext(self.last)
            self.last = newLast
    def dequeue(self):
        returnVal = self.first
        currNode = self.last
        if currNode == returnVal: # There's only one value on the list
            self.first = Node(None)
            self.last = self.first
            self.last.setNext(self.first)
            return returnVal
        # We need to go all the way through the list to find the node that is
        # pointing at the first node, that is, the node that is second in line.
        while currNode.getNext() is not returnVal:
            currNode = currNode.getNext()
        self.first = currNode
        self.first.setNext(None)
        return returnVal
