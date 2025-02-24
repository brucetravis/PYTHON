# # functio to find the maximum number in a list
# def max_number(lst):
    
#     # Check If the list is empty
#     if not lst:
#         return None
    
#     max_num = lst[0] # Initialize the max_num with the first value
#                      # so that we have something to compare with
    
#     # Loop through all the numbers in the list
#     for num in lst:
#         # If any number in the list is greater than the initial value
#         if num > max_num:
#             # Update the max value with the lastest max_value
#             max_num = num
            
#     # return the max value
#     return max_num


# print(max_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# function to calculate the max number
def maximum_number(lst):
    # Initialize the max_number with None
    max_num = None
    
    # Loop though the list of numbers
    for num in lst:
        # If the max_num is None or the current number is greater than the maximum number
        if max_num  == None or num > max_num:
            # Update the max_num with the current value
            max_num  = num
            
    # return the maxumum value
    return max_num


print(maximum_number([1, 2, 3, 4, 5]))
    
    
    