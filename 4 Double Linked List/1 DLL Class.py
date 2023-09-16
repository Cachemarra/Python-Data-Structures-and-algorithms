# %% Node class
class Node:
    def __init__(self, value:float):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    DECREACE_LEN = -1
    INCREASE_LEN = 1
    
    def __init__(self, value:float = None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 if value != None else 0


    def append(self, value:float):
        # Add a node to the end
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            temp = self.tail

            temp.next = new_node
            new_node.prev = temp

            self.tail = new_node

        self.__update_len(self.INCREASE_LEN)
        return True

    def prepend(self, value:float):
        new_node = Node(value)

        temp = self.head
        new_node.next = temp

        if self.length == 0:
            self.tail = new_node
        else:
            temp.prev = new_node

        self.head = new_node

        self.__update_len(self.INCREASE_LEN)
        return True
        
    def insert_manual(self, index:int, value:float):
        if index < 0 or index > self.length:
            return False
        
        node = Node(value)
        temp = self.head

        if index == 0:
            node.next = temp
            temp.prev = node
        
        elif index == self.length:
            temp = self.tail
            temp.next = node
            node.prev = temp
            
        else:
            for _ in range(index - 1):
                temp = temp.next

            follow_node = temp.next
            temp.next = node
            node.prev = temp
            node.next = follow_node
            follow_node.prev = node
        
        self.__update_len(self.INCREASE_LEN)
        return True

    def insert(self, index:int, value:float):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node = Node(value)
            
            temp = self.get_value(index-1)
            follow_node = temp.next
            
            temp.next = node
            node.prev = temp

            follow_node.prev = node
            node.next = follow_node

        self.__update_len(self.INCREASE_LEN)
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        # Storing actual tail
        temp = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None

        else:
            # Update tail
            new_tail = temp.prev
            new_tail.next = None
            self.tail = new_tail

            temp.prev = None
        
        self.__update_len(self.DECREACE_LEN)
        return temp

    def pop_first(self):
        if self.length == 0:
            return None
        
        temp = self.head
        new_head = temp.next
        new_head.prev = None
        self.head = new_head

        temp.prev = None
        self.__update_len(self.DECREACE_LEN)
        return temp
    
    def get_value(self, index:int):
        if index > self.length or index < 0:
            return False
        
        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
        
    def set_value(self, index, value):
        # Normal method
        # if index > self.length or index < 0:
        #     return False
        
        # temp = self.head
        # for _ in range(index):
        #     temp = temp.next

        # temp.value = value

        # Lazy mode
        temp = self.get_value(index)
        temp.value = value
        return True

    def remove(self, index):
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.pop_first()
            return True
        elif index == self.length:
            self.pop()
            return True
        
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next
        
        temp.next = temp.next.next
        temp = temp.next
        temp.prev = temp.prev.prev

        self.__update_len(self.DECREACE_LEN)
        return True

    def reverse(self):
        if self.length == 0:
            return None

        follow_node = self.tail.prev
        temp = self.tail
        back_node = self.tail
        temp.prev = None
        
        self.head = self.tail

        while follow_node != None:
            temp.next = follow_node
            temp.prev = back_node
            
            temp = temp.next
            back_node = temp
            follow_node = follow_node.prev
            
        temp.prev = temp.next
        temp.next = None
        self.tail = temp        
        return True

    # Dunder methods ========
    def __str__(self):
        text = "None"
        temp = self.head

        while temp != None:
            value = temp.value
            text += f" ⇆ {value}"
            temp = temp.next
        
        text += " None"
        return text

    def __update_len(self, value):
        self.length += value


# %% Test

if __name__ == "__main__":

    dLL = DoubleLinkedList(1)
    dLL.append(2)
    dLL.append(3)
    dLL.append(5)
    dLL.append(4)
    dLL.append(3)
    dLL.append(2)

    print("Append")
    print(dLL)

    print(dLL.tail.prev.value)

    # Check prepend
    print("\nPrepend")
    dLL.prepend(1)
    dLL.prepend(9)
    dLL.prepend(11)
    print(dLL)

    print(dLL.tail.prev.value)

    # Check pop
    print("\nPop")
    dLL.pop()
    dLL.pop()
    print(dLL)

    print(dLL.tail.prev.value)

    # Check pop_first
    print("\nPop first")
    dLL.pop_first()
    dLL.pop_first()
    print(dLL)

    print(dLL.tail.prev.value)

    # Check get
    print("\nGet")
    node = dLL.get_value(0)
    print(f"Value of node 0: {node.value}")
    node = dLL.get_value(3)
    print(f"Value of node 3: {node.value}")

    print(dLL.tail.prev.value)

    # Check insert
    print("\nInsert")
    dLL.insert(2, 22)
    print(f"Insert 22 in index 2")
    print(dLL)
    dLL.insert(4, 42)
    print(f"Insert 42 in index 4")
    print(dLL)
    
    print(dLL.tail.prev.value)

    # Check set
    print("\nSet")
    print(f"Set 21 in index 0")
    dLL.set_value(0, 21)
    print(dLL)
    print(f"Set 0 in index 5")
    dLL.set_value(5, 0)
    print(dLL)

    print(dLL.tail.prev.value)

    # Check remove
    print("\nRemove")
    print(f"Remove index 4")
    dLL.remove(4)
    print(dLL)    
    print(f"Remove index 2")
    dLL.remove(2)
    print(dLL)

    print(dLL.tail.prev.value)

    # Check reverse
    print("\nReverse")
    dLL.reverse()
    print(dLL)

    print(dLL.tail.prev.value)

# %%
