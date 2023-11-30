# WRITE FIND_LONGEST_STRING FUNCTION HERE #
#                                         #
#                                         #
#                                         #
#                                         #
###########################################
def find_longest_string(string_list):
    largest_string = string_list[0]
    longest_string = len(string_list[0])

    for string in string_list:
        if len(string) > longest_string:
            longest_string = len(string)
            largest_string = string

    return largest_string




string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""