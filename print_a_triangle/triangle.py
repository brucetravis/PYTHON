# # Function to print a right angled triangle
# def triangle(n):
#     # Loop through a range of numbers in which, 
#     # in the range, you will have to add n to 1 since n is your input
#     for i in range(1, n + 1):
#         # Print the right angled tringle of asterix
#         print("*" * i)
        
# # Call the function providing an argument for the parameter n
# triangle(10)


# We can modify the code further to increase each line of asterix



# Function to print a right angled triangle
def triangle(n):
    # Loop through the range values
    # For this we add a step
    for i in range(1, n + 1, 2):
        # Print out the values
        print("*" * i)
        
# Call the function providing an argument
triangle(50)
        
