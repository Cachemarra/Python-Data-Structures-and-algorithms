# %% Node constructor
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


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
        temp = self.top
        if self.height >= 1 and temp is not None:
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

    def is_empty(self):
        return len(self.stack_list) == 0


def is_balanced_parentheses(string:str=None):
    stack = Stack()
    opening_brac = {")": "(", "]": "[", "}": "{"}

    if len(string) == 0:
        return True
    
    if string[0] in opening_brac.keys():
        return False
        
    stack.push(string[0])    
    
    for i in string[1:]:
        if i in opening_brac.values(): # ( [ {
            stack.push(i)
        else: # ) ] }
            prev = stack.pop()
            if prev != opening_brac[i]:
                return False
                
    return True if stack.is_empty() else False


def reverse_string(string):
    stack = Stack()
    result = ""
    
    if len(string) == 0:
        return result

    for i in string:
        stack.push(i)

    for _ in range(stack.size()):
        result += stack.pop()

    return result


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

print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print(f"Node value: {my_stack.pop()}")
print("Final stack")
print(my_stack)

# %%
