class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

          
    def __r_insert(self, current_node, value):
        if current_node == None: 
            return Node(value)   
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value) 
        return current_node    

    def r_insert(self, value):
        if self.root == None: 
            self.root = Node(value)
        self.__r_insert(self.root, value)  


    def min_value(self, current_node):
        while (current_node.left is not None):
            current_node = current_node.left
        return current_node.value 

    ## WRITE DELETE_NODE METHODS HERE ##
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    def __delete_node(self, node, value):
        if node is None:
            return None
        
        if node.value > value:
            node.left = self.__delete_node(node.left, value)
        if node.value < value:
            node.right = self.__delete_node(node.right, value)

        else:
            if node.left != None and node.right != None:
                # Move the min right value to the node and delete min node
                node.value = self.min_value(node.right)
                node.right = self.__delete_node(node.right, node.value)
                return node

            elif node.left != None:
                return node.left
            elif node.right != None:
                return node.right
            return None
        return node



    def delete_node(self, value):
        return self.__delete_node(self.root, value)
        




##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")


# test_delete_node_no_children
print("\n----- Test: Delete node with no children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(None, bst.root.left, "Left child of root after deleting 3:")


# test_delete_node_only_left_child
print("\n----- Test: Delete node with only left child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(1, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_node_only_right_child
print("\n----- Test: Delete node with only right child -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(8)
check(9, bst.root.right.value, "Right child of root after deleting 8:")


# test_delete_node_two_children
print("\n----- Test: Delete node with two children -----\n")
bst = BinarySearchTree()
values = [5, 3, 8, 1, 4, 7, 9]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(3)
check(4, bst.root.left.value, "Left child of root after deleting 3:")


# test_delete_root
print("\n----- Test: Delete root -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
bst.delete_node(5)
check(8, bst.root.value, "Root value after deleting 5:")


# test_delete_non_existent_node
print("\n----- Test: Attempt to delete a non-existent node -----\n")
bst = BinarySearchTree()
values = [5, 3, 8]
for v in values:
    print("Inserting value:", v)
    bst.r_insert(v)
original_root_value = bst.root.value
bst.delete_node(10)
check(original_root_value, bst.root.value, "Root value after attempting to delete 10:")
