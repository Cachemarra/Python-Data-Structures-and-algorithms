def swap(list2swap, index1, index2):
    list2swap[index1], list2swap[index2] = list2swap[index2], list2swap[index1]


def pivot(unsorted, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if unsorted[i] < unsorted[pivot_index]:
            swap_index += 1
            swap(unsorted, swap_index, i)

    swap(unsorted, pivot_index, swap_index)

    return swap_index


def quick_sort_helper(unsorted, left, right):
    if left < right: # Base case
        pivot_index = pivot(unsorted, left, right)

        quick_sort_helper(unsorted, left, pivot_index-1)
        quick_sort_helper(unsorted, pivot_index+1, right)

    return unsorted

def quick_sort(unsorted):
    return quick_sort_helper(unsorted, 0, len(unsorted)-1)

my_list = [4, 6, 1, 7, 3, 2, 5]


print(quick_sort(my_list))
