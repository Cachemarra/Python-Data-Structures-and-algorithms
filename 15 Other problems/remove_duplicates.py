# WRITE REMOVE_DUPLICATES FUNCTION HERE #
#                                       #
#                                       #
#                                       #
#                                       #
#########################################
def remove_duplicates(my_list):

    prev = None
    index = 0

    for _ in range(len(my_list)):
        if prev == my_list[index]:
            my_list.pop(index)
        else:
            prev = my_list[index]
            index += 1

    return len(my_list)


# Test case 1: Empty list
test1 = []
print(f"Test 1 Before: {test1}")
result1 = remove_duplicates(test1)
print(f"Test 1 After: {test1[:result1]}")
print(f"New Length: {result1}")
print("------")

# Test case 2: List with all duplicates
test2 = [1, 1, 1, 1, 1]
print(f"Test 2 Before: {test2}")
result2 = remove_duplicates(test2)
print(f"Test 2 After: {test2[:result2]}")
print(f"New Length: {result2}")
print("------")

# Test case 3: List with no duplicates
test3 = [1, 2, 3, 4, 5]
print(f"Test 3 Before: {test3}")
result3 = remove_duplicates(test3)
print(f"Test 3 After: {test3[:result3]}")
print(f"New Length: {result3}")
print("------")

# Test case 4: List with some duplicates
test4 = [1, 1, 2, 2, 3, 4, 5, 5]
print(f"Test 4 Before: {test4}")
result4 = remove_duplicates(test4)
print(f"Test 4 After: {test4[:result4]}")
print(f"New Length: {result4}")
print("------")


