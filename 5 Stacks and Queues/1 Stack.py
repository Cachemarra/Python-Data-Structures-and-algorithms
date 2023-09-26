# %% Node constructor
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


# %% Stack constructor
class Stack:
    __INCREASE_HEIGHT = 1
    __DECREASE_HEIGHT = -1

    def __init__(self, value=None):
        node = Node(value)

        self.top = node
        self.height = 1


    def push(self, value):
        node = Node(value)

        temp = self.top
        if temp.value is None and self.height == 1:
            self.top = node
            return True
        else:
            node.next = temp
            self.top = node

            self.__updateHeight__(self.__INCREASE_HEIGHT)
            return True
        

    def pop(self):
        
        if self.height >= 1:
            temp = self.top
            self.top = temp.next
            temp.next = None

            self.__updateHeight__(self.__DECREASE_HEIGHT)
            return temp
        return None


    def __str__(self):
        text = ""
        
        temp = self.top
        while temp is not None:
            value = temp.value
            text += f"{value}\n↓\n"
            temp = temp.next

        text += "None"
        return text

    def __updateHeight__(self, value):
        self.height += value


# %% Check

my_stack = Stack(4)
print(my_stack)

print("".center(30, "-"))

my_stack.push(11)
my_stack.push(5)
my_stack.push(0)
my_stack.push(1)
my_stack.push(3)
print(my_stack)

print("".center(30, "-"))

print(f"Node value: {my_stack.pop().value}")
print(f"Node value: {my_stack.pop().value}")
print("Final stack")
print(my_stack)

# %%
