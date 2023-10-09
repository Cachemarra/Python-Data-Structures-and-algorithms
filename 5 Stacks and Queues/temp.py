# %%
class Stack:
    def __init__(self):
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])

    def is_empty(self):
        return len(self.stack_list) == 0

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]

    def size(self):
        return len(self.stack_list)

    def push(self, value):
        self.stack_list.append(value)

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list.pop()




##### WRITE SORT_STACK FUNCTION HERE #####
#                                        #
#  This is a separate function that is   #
#  not a method within the Stack class.  #
#                                        #
#  <- INDENT ALL THE WAY TO THE LEFT <-  #
#                                        #
##########################################
def sort_stack(input_stack):
    sorted_stack = Stack()

    if input_stack.is_empty():
        return True

    temp = input_stack.pop()

    while not input_stack.is_empty():
        if input_stack.peek() > temp:
            sorted_stack.push(temp)
            temp = input_stack.pop()

        else:
            val = input_stack.pop()
            while not sorted_stack.is_empty() and val < sorted_stack.peek():
                input_stack.push(sorted_stack.pop())
            
            sorted_stack.push(val)
            val = None
        
    sorted_stack.push(temp)
    
    while not sorted_stack.is_empty():
        input_stack.push(sorted_stack.pop())

    # while not input_stack.is_empty():
    #     temp = input_stack.pop()
        
    #     while not sorted_stack.is_empty() and sorted_stack.peek() > temp:
    #         input_stack.push(sorted_stack.pop())
    #         sorted_stack.push(temp)

    # while not sorted_stack.is_empty():
    #     input_stack.push(sorted_stack.pop())




#%%
my_stack = Stack()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()



"""
    EXPECTED OUTPUT:
    ----------------
    Stack before sort_stack():
    2
    4
    5
    1
    3

    Stack after sort_stack:
    1
    2
    3
    4
    5

"""
# %%
