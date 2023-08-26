# %% Creation of the base class Node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        pass



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
        if self.head is None:
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

        if self.length <= 1:
            self.tail = new_node

        self._update_length(self.INCREASE_LEN)
        return True

    def insert(self, index, value):
        # Create new node and insert node in index
        new_node = Node(value)

        if index == 1:
            _ = self.prepend(value)
        elif index == self.length:
            _ = self.append(value)

        else:
            # Grab first node and iterate through index
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next

                prev_next = temp_node.next
                temp_node.next = new_node
                new_node.next = prev_next

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
        prev_node = self.get(index - 1)

        deleted_node = prev_node.next
        prev_node.next = deleted_node.next

        return True

    def reverse(self):
        reverse = LinkedList(self.tail.value)

        for i in range(self.length - 2, - 1, -1):
            reverse.append(self.get(i).value)

        return reverse

    def _update_length(self, value):
        self.length += value

    def __str__(self):
        # Print the elements of the list
        text = ""
        temp = self.head

        while temp is not None:
            text += f" {temp.value} ->"
            temp = temp.next

        return text + f"\nLen: {self.length}"


# %% Tests
# Linked List will be 11 -> 3 -> 23 -> 7

linked = LinkedList(3)
print(linked)
linked.append(23)
print(linked)
linked.prepend(11)
print(linked)
linked.insert(3, 7)
print(linked)

# print(linked.reverse())
print(linked.get(2).value)
print(linked.set(2, 32))
print(f"Modified linked list: {linked}")
reversed = linked.reverse()
print(f"Reversed liked list: {reversed}")
print(f"Poped last: {linked.pop().value}")
print(linked)
print(f"Removed"); linked.remove(1)
print(linked)

print(f"Pop first: {linked.pop_first().value}")
print(linked)

# %%
