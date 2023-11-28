## WRITE INSERTION_SORT FUNCTION HERE ##
#                                      #
#                                      #
#                                      #
#                                      #
######################################## 
def insertion_sort(unsorted):
    for i in range(1, len(unsorted)):
        current = unsorted[i]
        j = i-1
        while j >= 0 and current < unsorted[j]:

            unsorted[j+1] = unsorted[j]
            j -= 1
            
        unsorted[j+1] = current
    return unsorted



print(insertion_sort([4,2,6,5,1,3]))



"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """

