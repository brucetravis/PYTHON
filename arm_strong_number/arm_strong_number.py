# Ineffficient approach

# # Function to check if a number is an armstrong number
# def arm_strong_number(number):
#     # Convert the number into a string so that we can count the digits
#     num_string = str(number)
#     # Count the digits in the string
#     num_len = len(num_string)
    
#     # Empty List to store integers
#     sum_list = []
    
#     # Loop thorugh all the digits raising them up to the power of the number of digits
#     for digit in num_string:
#         # Convert each digit into an integer again
#         integer_digit = int(digit)
#         # raise each integer_digit to the power of the length of the number
#         raised_digit = integer_digit ** num_len
#         # store each digit into the new list
#         sum_list.append(raised_digit)
        
#     # Add the numbers in the list
#     total = sum(sum_list)
    
#     # compare if the numbers match
#     return total == number

# print(arm_strong_number(153))       


# Efficient approach

# # function to determine If a number is an armstrong number
# def arm_strong_number(number):
#     # Convert the number into a string so that we can be able to loop and count the number of digits
#     num_str = str(number)
#     # Find the length of the digits in the number
#     num_len = len(num_str)
    
#     # Sum total of the number
#     total = sum(int(digit) ** num_len for digit in num_str)
    
#     # compare to see If the match
#     return total == number
    
# print(arm_strong_number(153))



# check for Armstrong numbers in a given range?

# function to determine If a numer is an arm strong number
def is_arm_strong_number(number):
    # convert the nmebr to a string to enable counting
    number_str = str(number)
    # Find the length of the number
    number_len = len(number_str)
    
    # sum total of the number
    total = sum(int(digit) ** number_len for digit in number_str)
    
    # Compare the sum total with the original number
    return total == number


# function to check the arm strong numbers in a given range
def find_arm_strong(start, end):
    # Loop to find arm strong numbers in a range
    arm_strong_numbers = [num for num in range(start, end + 1) if is_arm_strong_number(num)]
    # return the arm strong numbers
    return arm_strong_numbers


# starting range
starting_range = int(input("Enter a starting number: "))
# Ending range
ending_range = int(input("Enter an ending number: "))

# arm_strong list of numbers
arm_strong_list = find_arm_strong(starting_range, ending_range)

# Pring out the numbers
print(f"Arm strong numbers between {starting_range} and {ending_range}: {arm_strong_list}")
