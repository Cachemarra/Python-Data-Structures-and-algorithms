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

    def add_node(self, value):
        new_node = Node(value)

        if self.root == None:
            self.root = new_node

        else:
            self.__compare_nodes(self.root, new_node)
            
    def __compare_nodes(self, node, new_node):
        if node.left == None and new_node.value < node.value:
            node.left = new_node
        elif node.right == None and new_node.value > node.value:
                node.right = new_node
            
        else:
            if new_node.value < node.value:
                self.__compare_nodes(node.left, new_node)
            else:
                self.__compare_nodes(node.right, new_node)


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


# %%
