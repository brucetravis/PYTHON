# function to find the second larget number in a list
def second_largest_number(list):
    # Initialize max_num and second_max_num
    max_num = second_max_num = float('-inf')
    
    # Loop thorugh the numbers in the list
    for num in list:
        # If the current number in the list is greater than max_num 
        if num > max_num:
            # Update the second_max_num with the current max_num 
            second_max_num = max_num
            # Update max_num with now the latest maximum/largest value
            max_num = num
            
        # If the current number in the list is greater than the second maximum number and not the maximum number
        elif num > second_max_num and num != max_num: # This condition is only executed If there is a number larger than the seond_max_num but smaller than max_num 
            second_max_num = num # Update the current second_max_num If It's larger than the current second_max_num but smaller than max_num
            
    return second_max_num


print(second_largest_number([10, 20, 30, 40, 50]))

