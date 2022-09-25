# Python3 implementation of the approach
from sys import maxsize
from collections import deque

INT_MIN = -maxsize

# Class containing left and right
# child of current node and key value
class Node:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None

# Function to locate which level to check
# for the existence of key.
def findLevel(root: Node, data: int) -> int:
    
    # If the key is less than the root,
    # it will certainly not exist in the tree
    # because tree is level-order sorted
    if (data < root.data):
        return -1

    # If the key is equal to the root then
    # simply return 0 (zero'th level)
    if (data == root.data):
        return 0

    cur_level = 0

    while True:

        cur_level += 1
        root = root.left

        # If the key is found in any leftmost
        # element then simply return true
        # No need for any extra searching
        if (root.data == data):
            return -2

        # If key lies between the root data and
        # the left child's data OR if key is greater
        # than root data and there is no level
        # underneath it, return the current level
        if (root.data < data and 
           (root.left == None or
            root.left.data > data)):
            break

    return cur_level

# Function to traverse a binary
# encoded path and return the value
# encountered after traversal.
def traversePath(root: Node, path: list) -> int:
    
    for i in range(len(path)):
        direction = path[i]

        # Go left
        if (direction == 0):

            # Incomplete path
            if (root.left == None):
                return -1
                
            root = root.left

        # Go right
        else:

            # Incomplete path
            if (root.right == None):
                return -1
                
            root = root.right

    # Return the data at the node
    return root.data

# Function to generate gray code of
# corresponding binary number of integer i
def generateGray(n: int, x: int) -> list:
    
    # Create new arraylist to store
    # the gray code
    gray = []

    i = 0
    while (x > 0):
        gray.append(x % 2)
        x = x / 2
        i += 1

    # Reverse the encoding till here
    gray.reverse()

    # Leftmost digits are filled with 0
    for j in range(n - i):
        gray.insert(0, gray[0])

    return gray

# Function to search the key in a
# particular level of the tree.
def binarySearch(root: Node, start: int,
                  end: int, data: int,
                level: int) -> bool:

    if (end >= start):

        # Find the middle index
        mid = (start + end) / 2

        # Encode path from root to this index
        # in the form of 0s and 1s where
        # 0 means LEFT and 1 means RIGHT
        encoding = generateGray(level, mid)

        # Traverse the path in the tree
        # and check if the key is found
        element_found = traversePath(root, encoding)

        # If path is incomplete
        if (element_found == -1):

            # Check the left part of the level
            return binarySearch(root, start, 
                                mid - 1, data,
                                level)

        if (element_found == data):
            return True

        # Check the right part of the level
        if (element_found < data):
            return binarySearch(root, mid + 1, 
                                end, data, level)

        # Check the left part of the level
        else:
            return binarySearch(root, start, 
                                mid - 1, data,
                                level)

    # Key not found in that level
    return False

# Function that returns true if the
# key is found in the tree
def findKey(root: Node, data: int) -> bool:
    
    # Find the level where the key may lie
    level = findLevel(root, data)

    # If level is -1 then return false
    if (level == -1):
        return False

    # If level is -2 i.e. key was found in any
    # leftmost element then simply return true
    if (level == -2):
        return True

    # Apply binary search on the elements
    # of that level
    return binarySearch(root, 0, 
                        int(pow(2, level) - 1),
                        data, level)

# Driver code
if __name__ == "__main__":

    # Consider the following level 
    # order sorted tree
    '''
    
                5
               /  \ 
              8    10 
            /  \  /  \
           13  23 25  30
          / \  /
        32  40 50 
    '''

    root = Node(5)
    root.left = Node(8)
    root.right = Node(10)
    root.left.left = Node(13)
    root.left.right = Node(23)
    root.right.left = Node(25)
    root.right.right = Node(30)
    root.left.left.left = Node(32)
    root.left.left.right = Node(40)
    root.left.right.left = Node(50)

    # Keys to be searched
    arr = [ 5, 8, 9 ]
    n = len(arr)

    for i in range(n):
        if (findKey(root, arr[i])):
            print("Yes")
        else:
            print("No")

# This code is contributed by sanjeev2552