# # function to find the maximum number in a list
# def max_num(list):
#     # variable holding the initial maximum number which is none
#     max_num = list[0]
    
#     # Loop through the list to find the maximum number
#     for num in list:
#         # Condition determine the maximum number
#         if num > max_num:
#             # Update max_num with the max_num value
#             max_num = num
            
#     return max_num

# # Call the function and print the result
# print(max_num([10, 20, 30, 40, 50]))

# Output: 50

# Returning all unmbers greater that the Initial value to be compared with
# Function to find the maximum number
def max_num(list):
    # Initial value to compare with
    max_num = list[0]
    
    # return the max number
    return [num for num in list if num > max_num]

print(max_num([10, 20, 30, 40, 50]))

# Output: [20, 30, 40, 50]