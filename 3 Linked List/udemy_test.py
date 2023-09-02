# %%
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next  
            
    def print_all(self):
        if self.length == 0:
            print("Head: None")
        else:
            print("Head: ", self.head.value)
        print("Length: ", self.length)
        print("\nLinked List:")
        if self.length == 0:
            print("empty")
        else:
            self.print_list()

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.length += 1


    # WRITE REMOVE_DUPLICATES METHOD HERE #
    #                                     #
    #                                     #
    #                                     #
    #                                     #
    #######################################
    def remove_duplicates(self):
        if self.length == 0:
            return None
        
        # Extract all node values
        temp = self.head
        node_values = []
        while temp != None:
            node_values.append(temp.value)
            temp = temp.next
        
        node_values = set(node_values)
        node_values.remove(self.head.value)
        temp = self.head
        next_temp = self.head.next

        while next_temp != None:
            if next_temp.value in node_values:
                node_values.remove(next_temp.value)

                temp.next = next_temp
                temp = temp.next

            next_temp = next_temp.next
                



# %%
my_linked_list = LinkedList(1)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(3)
my_linked_list.append(2)
my_linked_list.append(4)
my_linked_list.remove_duplicates()

my_linked_list.print_all()




"""
    EXPECTED OUTPUT:
    ----------------
    Head:  1
    Length:  4
    Linked List:
    1
    2
    3
    4
    
"""

# %%
