# %% 
class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


# Tree
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
            return True
        else:
            return self.__compare_nodes_to_add(self.root, new_node)
            
    def __compare_nodes_to_add(self, node, new_node):
        if node.value == new_node.value:
            return False
        elif node.left == None and new_node.value < node.value:
            node.left = new_node
            return True
        elif node.right == None and new_node.value > node.value:
                node.right = new_node
                return True
        else:
            if new_node.value < node.value:
                return self.__compare_nodes_to_add(node.left, new_node)
            else:
                return self.__compare_nodes_to_add(node.right, new_node)


    def contains(self, value):
        # Check if contains a value
        node = self.root
        
        if node == None:
            return False
        
        elif value == node.value:
            return True
        
        return self.__compare_value(node, value)
    
    def __compare_value(self, node, value):
        if node == None:
            return False
        
        if node.value == value:
            return True
        
        if value < node.value:
            return self.__compare_value(node.left, value)
        else:
            return self.__compare_value(node.right, value)


    def print_tree(self):
        self.__print_node(self.root)

    def __print_node(self, node):
        if node != None:
            print(node.value)
        
            # Print left path and right
            self.__print_node(node.left)
            self.__print_node(node.right)




# %% Tests
my_tree = BinarySearchTree()

print(my_tree.root)

values = [47, 21, 18, 76, 82, 27, 52] # [5, 1, 6, 2, 7, 3, 8, 4, 9]

for i in values:
    my_tree.add_node(i)

my_tree.print_tree()

print(f"Tree contains 47? : {my_tree.contains(47)}")
print(f"Tree contains 1? : {my_tree.contains(1)}")
print(f"Tree contains 27? : {my_tree.contains(27)}")
print(f"Tree contains 92? : {my_tree.contains(92)}")


# %%
