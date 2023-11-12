class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else: 
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
        
    ## WRITE R_CONTAINS METHODS HERE ##
    #                                 #
    #                                 #
    #                                 #
    #                                 #
    ###################################
    def __contains(self, node, value):
        if node == None:
            return False
        
        elif node.value == value:
            return True
        
        if node.value > value:
            return self.__contains(node.left, value)
        else:
            return self.__contains(node.right, value)
        
        return False
        
        
    
    def r_contains(self, value):
        if self.root is None:
            return False
        else:
            return self.__contains(self.root, value)


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.r_contains(27))

print('\nBST Contains 17:')
print(my_tree.r_contains(17))
                


"""
    EXPECTED OUTPUT:
    ----------------
    BST Contains 27:
    True

    BST Contains 17:
    False

"""

