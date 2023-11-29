class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # WRITE MERGE METHOD HERE #
    #                         #
    #                         #
    #                         #
    #                         #
    ###########################
    

    def merge(self, list2):

        l1_node = self.head
        l2_node = list2.head
        prev = None

        if l2_node is None:
            return
        elif l1_node is not None and l1_node.value < l2_node.value:
            prev = self.head
            l1_node = l1_node.next
        else:
            prev = list2.head
            l2_node = l2_node.next

        while l1_node is not None and l2_node is not None:
            if l1_node.value < l2_node.value:
                prev.next = Node(l1_node.value)

                l1_node = l1_node.next
                prev = prev.next
            else:
                prev.next = Node(l2_node.value)

                l2_node = l2_node.next
                prev = prev.next

        while l1_node != None:
            prev.next = Node(l1_node.value)
            
            l1_node = l1_node.next
            prev = prev.next

        while l2_node != None:
            prev.next = Node(l2_node.value)
            
            prev = prev.next
            l2_node = l2_node.next



# Testing ===================
l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""