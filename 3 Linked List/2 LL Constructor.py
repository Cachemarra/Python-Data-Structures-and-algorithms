# %% Creation of the base class Node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


# %% Creation of a class for Linked List
class LinkedList:

    DECREACE_LEN = -1
    INCREASE_LEN = 1

    def __init__(self, value=None) -> None:
        # Create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 if value != None else 0

    def append(self, value):
        # Create a new node then add to end
        new_node = Node(value)

        # Check if we don't have empty LL
        if self.length == 0: # self.head is None:
            self.head = new_node
            self.tail = new_node
        
        else:
            # Sort last nodes
            self.tail.next = new_node
            self.tail = new_node

        self._update_length(self.INCREASE_LEN)
        return True

    def prepend(self, value):
        # Create new node then add to beginning
        new_node = Node(value)

        old_head = self.head
        self.head = new_node
        self.head.next = old_head

        if self.length <= 0:
            self.tail = new_node

        self._update_length(self.INCREASE_LEN)
        return True

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        
        # Create new node and insert node in index
        if index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)

        # Insert elsewhere
        prev_node = self.get(index-1)
        node = Node(value)

        node.next = prev_node.next
        prev_node.next = node
        

        # # Grab first node and iterate through index
        # temp_node = self.head
        # for _ in range(index - 1):
        #     temp_node = temp_node.next

        #     prev_next = temp_node.next
        #     temp_node.next = new_node
        #     new_node.next = prev_next

        self._update_length(self.INCREASE_LEN)
        return True

    def pop(self):
        # Opt version
        if self.length == 0:
            return None
        
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        
        self._update_length(self.DECREACE_LEN)

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

        # # Starting point
        # temp_node = self.head

        # # Check edge cases
        # if self.length <= 1:
        #     if temp_node == None:
        #         return False
        #     else:
        #         pop_val = self.head.value
        #         self.head = None

        # else:
        #     for _ in range(self.length - 2):
        #         temp_node = temp_node.next
            
        #     pop_val = temp_node.next.value
        #     temp_node.next = None
        #     self.tail = temp_node
        # self._update_length(-1)
        # return pop_val

    def pop_first(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.tail = None
        
        pop_val = self.head
        self.head = self.head.next

        self._update_length(self.DECREACE_LEN)
        return pop_val

    def get(self, index):
        if index < 0 or index > self.length:
            return None
        
        temp = self.head

        for _ in range(index):
            temp = temp.next

        return temp

    def set(self, index, value):
        tmp = self.get(index)
        tmp.value = value
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        
        prev_node = self.get(index - 1)
        deleted_node = prev_node.next
        prev_node.next = deleted_node.next
        deleted_node.next = None
        self._update_length(self.DECREACE_LEN)

        return deleted_node

    def reverse(self):
        # Course solution
        #    Change tail and head positions
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

        # Mine solution
        # reverse = LinkedList(self.tail.value)

        # for i in range(self.length - 2, - 1, -1):
        #     reverse.append(self.get(i).value)

        # return reverse

# Interview Question.

    def find_middle_node(self):
        slow = self.head
        fast = self.head.next
        
        if slow == None or slow.next == None:
            return slow
        
        while fast != None or fast.next != None:
            fast = fast.next
            slow = slow.next
            
            if None == fast or None == fast.next:
                break
            fast = fast.next
                 
        return slow


    def has_loop(self):
        slow = self.head
        fast = self.head.next
        
        while slow != None or fast != None:
            fast = fast.next
            slow = slow.next
            
            if fast == None or fast.next == None:
                break
            if fast == slow:
                return True
            
            fast = fast.next
            
        return False
    
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

# END OF Interview Question. =============

    def _update_length(self, value):
        self.length += value

    def __str__(self):
        # Print the elements of the list
        text = ""
        temp = self.head

        while temp is not None:
            text += f" {temp.value} ->"
            temp = temp.next
        text += f" None"
        return text + f"\nLen: {self.length}"


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



# %% Functions Interview Questions
    
def find_kth_from_end(linkedList, k):
    if k <= 0:
        return None
    elif k == 1:
        temp = linkedList.tail
        temp.next = None
        return temp
    
    # Main algorithm
    slow = linkedList.head
    fast = linkedList.head

    for _ in range(k - 1):
        fast = fast.next

        if fast is None:
            return None

    while( fast.next is not None ):
        slow = slow.next
        fast = fast.next
    
    slow.next = None
    return slow
        

# %% Tests
# Linked List will be 11 -> 3 -> 23 -> 7

linked = LinkedList(3)
print(" Additions ".center(30, "-"))
print(linked)
print("Append 3")
linked.append(23)
linked.append(5)
linked.append(4)
print(linked)
print("Prepend")
linked.prepend(11)
print(linked)
print("Insert")
linked.insert(1, 7)
print(linked)

print(" Get & Set ".center(30, "-"))
print(linked.get(2).value)
print(linked.set(2, 32))
print(f"Modified linked list: {linked}")

print(" Functions ".center(30, "-"))
partitionList = linked.partition_list(12)
print(f"Partition list by value: {partitionList}")

node = find_kth_from_end(linkedList=linked, k=5)
print(f"Find kth node from end: {node.value}")
print(f"Middle Node: {linked.find_middle_node().value}")
reversed = linked.reverse()
print(f"Reversed liked list: {reversed}")

print(" Functions ".center(30, "-"))
print(f"Poped last: {linked.pop().value}")
print(linked)
print(f"Removed"); linked.remove(1)
print(linked)

print(f"Pop first: {linked.pop_first().value}")
print(linked)
print(f"Middle Node: {linked.find_middle_node().value}")

# %% 1 - 10 linked list
linked = LinkedList(1)
print(" 1 - 9 Linked List ".center(30, "-"))
print("Linked List")
for i in range(8):
    linked.append(i + 2)

linked.reverse()
print(linked)


partitionList = linked.partition_list(12)

for val in range(1, 11, 1):
    partitionList.partition_list(val)
    print(f"Partition list by value {val}: {partitionList}")
    partitionList = linked

# %%

ll = LinkedList(3)
ll.append(5)
ll.append(8)
ll.append(10)
ll.append(2)
ll.append(1)

print("LL before partition_list:")
print(ll) # Output: 3 5 8 10 2 1

ll.partition_list(5)
print("LL after partition_list:")
print(ll) # Output: 3 2 1 5 8 10
# %%
