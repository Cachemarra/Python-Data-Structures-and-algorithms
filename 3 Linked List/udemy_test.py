class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.length += 1 
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next    
            
    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    # WRITE PARTITION_LIST METHOD HERE #
    #                                  #
    #                                  #
    #                                  #
    #                                  #
    ####################################
    
    def partition_list(self, x):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head
        
        # Creation of two LL
        equalGreat = LinkedList(None)
        less = LinkedList(None)

        temp = self.head
        while temp != None:
            if temp.value >= x:
                equalGreat.append(temp.value)
            else:
                less.append(temp.value)
            temp = temp.next

        self.make_empty()
        
        self.head = less.head
        temp = self.head
        lessNext = less.head
        
        while lessNext.next != None:
            temp.next = lessNext.next
            temp = temp.next
            lessNext = lessNext.next
            
        # Merge LinkedList
        tempGreat = equalGreat.head

        while tempGreat != None:
            if tempGreat.value == None: break
            temp.next = tempGreat
            temp = temp.next
            tempGreat = tempGreat.next
        
        return less
    

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
ll.print_list() # Output: 3 5 8 10 2 1

ll.partition_list(5)

print("LL after partition_list:")
ll.print_list() # Output: 3 2 1 5 8 10


"""
    EXPECTED OUTPUT:
    ----------------
    LL before partition_list:
    3
    5
    8
    10
    2
    1
    LL after partition_list:
    3
    2
    1
    5
    8
    10
    
"""
