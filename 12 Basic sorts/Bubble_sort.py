def bubble_sort(list2sort):
    for i in range(len(list2sort)-1, 0, -1):
        for j in range(i): # Each iteration, the biggest number will be stored in his place
            if list2sort[j] > list2sort[j+1]:
                list2sort[j], list2sort[j+1] = list2sort[j+1], list2sort[j]
    return list2sort
    

# Test
print(bubble_sort([4, 2, 6, 5, 1, 3]))

# Result must be -> [1, 2, 3, 4, 5, 6]