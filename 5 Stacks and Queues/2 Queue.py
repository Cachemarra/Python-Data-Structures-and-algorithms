# %% Node constructor
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# %% Queue constructor
class Queue():
    __INCREASE_LEN = 1
    __DECREASE_LEN = -1


    def __init__(self, value:None):
        node = Node(value)

        self.first = node
        self.last = node
        self.length = 1


    def enqueue(self, value):
        # Add someone to the line
        node = Node(value)

        if self.first is not None:
            temp = self.last
            temp.next = node
            self.last = node
        
        else:
            self.first = node
            self.last = node

        self.__changeLen(self.__INCREASE_LEN)
        return True        


    def dequeue(self):
        if self.first is not None and self.length >= 1:
            temp = self.first
            self.first = temp.next
            temp.next = None

            self.__changeLen(self.__DECREASE_LEN)

            if self.length == 0:
                self.first, self.last = None, None
                self.__changeLen(self.__INCREASE_LEN)
            return temp
        return None

    def __str__(self):
        text = ""
        temp = self.first
        while temp is not None:    
            text += f"{temp.value} → "
            temp = temp.next
        text += "None"
        return text
    
    def __changeLen(self, value):
        self.length += value


# %% Check Queue

my_queue = Queue(4)

print(my_queue)

print("".center(30, "-"))

print("Enqueue")
my_queue.enqueue(6)
my_queue.enqueue(10)
my_queue.enqueue(0)
my_queue.enqueue(2)
my_queue.enqueue(7)
print(my_queue)

print("".center(30, "-"))

print("Dequeue")
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue)
# %%
