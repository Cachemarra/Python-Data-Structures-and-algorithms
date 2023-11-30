# WRITE ROTATE FUNCTION HERE #
#                            #
#                            #
#                            #
#                            #
##############################
def rotate(nums, k):
    for _ in range(k):
        element = nums.pop()
        nums.insert(0, element)
 
# Other Solution
# def rotate(nums, k):
#     k = k % len(nums)
#     nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)

"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

    Explanation: The list has been rotated to the right by 3 steps:


    1.- [7, 1, 2, 3, 4, 5, 6]
    2.- [6, 7, 1, 2, 3, 4, 5]
    3.- [5, 6, 7, 1, 2, 3, 4]
"""