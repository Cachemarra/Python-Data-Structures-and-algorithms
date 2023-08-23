# %% Creation of the base class Node
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        pass



# %% Creation of a class for Linked List
class LinkedList:
    def __init__(self, value) -> None:
        # Create a new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


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

        self._update_length(1)
        return True

    def prepend(self, value):
        # Create new node then add to beginning
        new_node = Node(value)

        old_head = self.head
        self.head = new_node
        self.head.next = old_head

        self._update_length(1)
        return True


    def insert(self, index, value):
        # Create new node and insert node in index
        new_node = Node(value)

        # Grab first node and iterate through index
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next

        prev_next = temp_node.next
        temp_node.next = new_node
        new_node.next = prev_next

        self._update_length(1)
        return True

    def pop(self, index=None):
        pass


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


