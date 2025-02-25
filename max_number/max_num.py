# function to find the maximum number in a list
def maximum_num(list):
    # If the list if empty return None
    if not list: # If lst is empty 'not lst' is True but If lst not empty, not lst becomes true
        return None
    
    # Initialize the max number with the first value so that we can compare with the first value
    max_num = list[0]
    
    # Loop through all the numbers in the list
    for num in list:
        if num > max_num:
            # Update the max_num with the lates max_num value
            max_num = num
            
    # After Iteration, return the max_value
    return max_num

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print(maximum_num(numbers))

# None means no value

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


# function using the max method
def maximum_number(lst):
    return max(lst) if lst else None # Return the max value If the list is not empty, otherwise return None

print(maximum_number([1, 2, 3, 4, 5]))
print(maximum_number([])) # Output: None (for an empty list)

    