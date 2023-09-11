# %% Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoubleLinkedList:
    DECREACE_LEN = -1
    INCREASE_LEN = 1
    
    def __init__(self, value = None):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1 if value != None else 0


    def append(self, value):
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

    print(dLL)


# %%
