def selection_sort(list2sort):

    for i in range(len(list2sort)-1):
        min_value = i
        for j in range(i+1, len(list2sort)):
            if list2sort[j] < list2sort[min_value]:
                min_value = j
            
        if min_value != i:
            list2sort[i], list2sort[min_value] = list2sort[min_value], list2sort[i]

    return list2sort

print(selection_sort([4, 2, 6, 5, 1, 3]))
