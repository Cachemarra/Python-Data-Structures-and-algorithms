# %% Constructor
class MaxHeap:
    def __init__(self):
        self.heap = []


    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2
    
    def _parent(self, index):
        return (index - 1) // 2
    
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
        return True
            

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        # Replace the head with the last value to keep the tree completed
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return max_value
        

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if (left_index < len(self.heap)) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if (right_index < len(self.heap)) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return
        # Function to move a value to his true location.
        # while True:
        #     if self.heap[self._left_child(index)] is None or self.heap[self._right_child(index)] is None:
        #         break
        #     if self.heap[index] < self.heap[self._left_child(index)]:
        #         index_ = self._left_child(index)
        #         self._swap(index, index_)
        #         index = index_
            
        #     if self.heap[index] < self.heap[self._right_child(index)]:
        #         index_ = self._right_child(index)
        #         self._swap(index, index_) 
        #         index = index_


# %%

myheap = MaxHeap()
myheap.insert(99)
myheap.insert(72)
myheap.insert(61)
myheap.insert(58)

print(myheap.heap)

# Insert new vale that must go on top
myheap.insert(100)
print(f"Updated heap:\n{myheap.heap}")

# Add new value
myheap.insert(75)
print("Adding 75")
print(myheap.heap)

print("\nNew Heap")
myheap = MaxHeap()
myheap.insert(95)
myheap.insert(75)
myheap.insert(80)
myheap.insert(55)
myheap.insert(60)
myheap.insert(50)
myheap.insert(65)
print(myheap.heap)

# Remove top
print("Removing top (99)")
myheap.remove()
print(myheap.heap)
print("Removing (80)")
myheap.remove()
print(myheap.heap)
# %%
