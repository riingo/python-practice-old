# Practice with binary trees.

# Implementation of a general binary tree. If we wanted to just do a generic
# n-ary tree, we'd need to keep a list of the children, rather than having
# just right and left children. We'd also probably want a functioni for adding
# and removing child nodes. But for now, let's stick with binary trees.
class Tree():
    def __init__(self, value=None):
        self.value = value
        self.right = None
        self.left = None

# Import our implementation of stacks/queues.
from stacks_queues import *

# Depth first search implementation
def DFS(root, value):
    # DFS uses a stack to keep track of the nodes we've been to.
    # 1. Push the root node onto the stack. 
    # 2. Push the root node's children onto the stack.
    # 3. Pop the first element. Push its children onto the stack.
    # 4. Repeat until all nodes have been visited or we find the value.
    # Note: If this were a graph with possibly connected nodes, we'd need
    # an additional variable to keep track of which nodes we've been to. Since
    # this is a tree, we won't be going back to any previously visited nodes so
    # we don't need to worry about that. 
    toVisit = Stack(root)
    while toVisit.peek() is not None:
        root = toVisit.pop()
        if root.value.value == value:
            return True
        if root.value.right is not None:
            toVisit.push(root.value.right)
        if root.value.left is not None:
            toVisit.push(root.value.left)
    return False

# Depth first search recursive implementation
def DFS_recursive(root, value):
    if root.value == value:
        return True
    findLeft = False
    findRight = False
    if root.left is not None:
        findLeft = DFS_recursive(root.left, value)
    if root.right is not None:
        findRight = DFS_recursive(root.right, value)
    return (findLeft or findRight)

# Breadth first search implementation
def BFS(root, value):
    # In a BFS, we search each of the nodes on a level before proceeding to
    # the next level of children nodes. We'll use a queue to keep track of
    # the nodes.
    #   1. Push the root node onto the queue.
    #   2. Push the children nodes onto the queue.
    #   3. Pop the first element. Push its children onto the queue.
    #   4. Continue until we find the value or have seen all of the tree.
    toVisit = Queue(root)
    while toVisit.first.value is not None:
        root = toVisit.dequeue()
        if root.value.value == value:
            return True
        if root.value.right is not None:
            toVisit.enqueue(root.value.right)
        if root.value.left is not None:
            toVisit.enqueue(root.value.left)
    return False

# Breadth first search recursive implementation
def BFS_recursive(root, value):
    if root.value == value:
        return True
    findLeft = False
    findRight = False
    if root.left is not None:
        findLeft = BFS_recursive(root.left, value)
    if root.right is not None:
        findRight = BFS_recursive(root.right, value)
    return (findLeft or findRight)


# Test case.
##    p1 = Tree('A')
##    p2 = Tree('B')
##    p3 = Tree('C')
##    p4 = Tree('D')
##    p5 = Tree('E')
##    p6 = Tree('F')
##    p4.right = p6
##    p3.left = p4
##    p1.right = p3
##    p1.left = p2
##    p4.left = p5
#      A
#    B   C
#         D
#        E F
