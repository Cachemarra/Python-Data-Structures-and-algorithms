# WRITE FIND_MAX_MIN FUNCTION HERE #
#                                  #
#                                  #
#                                  #
#                                  #
####################################
def find_max_min(my_list):
    max_value = float("-inf")
    min_value = float("inf")

    for item in my_list:
        if item > max_value:
            max_value = item
        if item < min_value:
            min_value = item

    return (max_value, min_value)



print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""