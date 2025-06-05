# # Function to reverse the string
# def reverse_string():
#     # String to reverse
#     string = "exampleString"
    
#     # Loop through each charcater of the string to print It in reverse
#     # Loop from the last chrater to the first
#     for i in range(len(string) - 1, -1, -1):
#         print(i)
        
        
# # Run the file direclty and not as an imported file
# if __name__ == "__main__":
#     reverse_string()

# Reverse the string and append to a new variable

# # Function to reverse the string
# def string_reverse():
#     # String to reverse
#     string = "exampleString"
    
#     # String to append all the reversed letters
#     reversed_string = ""
    
#     try:
#         # Loop through each character in the string to print in reverse
#         # Print from the last character
#         for i in range(len(string) - 1, -1, -1):
#             # append each character to the empty string
#             reversed_string += string[i]
        
#         # Output teh empty string containing the reversed string
#         print(reversed_string)
#     except Exception as e:
#         print(e)
        
# # Run the file direclty and not as an imported file
# if __name__ == "__main__":
#     string_reverse()
    
# # NOTE: IN LINE 31 remebsre hat you are printing integers and you can oni cocatenate strings and not integers
# # Solution: access the actual charcater instead of the index string[i]




# We can also reverse the string havinf each charcater side by side, It's index

# # Function to reverse the string
# def string_reverse():
#     # string to reverse
#     string = "exampleString"
    
#     # Loop each character in order to print the string in reverse
#     for i in range(len(string) - 1, -1, -1):
#         print(f"{string[i]}: {i}")
        
# # Run the file direclty and not as an imporetd file
# if __name__ == "__main__":
#     string_reverse()



# We can use a while loop


# # Function to reverse the string
# def string_reverse():
#     # string to reverse
#     string = "exampleString"
    
#     # Empty string to append the reversed string 
#     reversed_string = ""
    
#     # Access the last charcater of the string
#     index = len(string) - 1
    
#     # Condition to loop through the string
#     # while the index is greater than or equal to 0
#     while index >= 0:
#         # Append the last character to the reversed string variable first
#         reversed_string += string[index]
#         # decrement each index by 1
#         index -= 1
    
#     print(reversed_string)

# if __name__ == "__main__":
#     string_reverse()
    
    # 


# Using the while loop we can also add a parameter and an argument an argument

# # Function to reverse the string
# def string_reverse(s):
#     # Empty string to contain the reversed characters
#     reversed_string = ""
    
#     # Index variable to contain the last chacater that we will start from
#     # len(s) - 1 is the last index in the string
#     index = len(s) - 1
    
#     # While loop condition to loop through the indices in the string
#     while index >= 0:
#         # Append the last index charcater to the string first.
#         reversed_string += s[index]
#         # decreament the index by 1 after each Iteration in order to print the characters in reverse
#         index -= 1
    
#     # return the reversed string
#     return reversed_string
    
# print(string_reverse("exampleString"))



# We can also use recursion to reverse the string


# Function to reverse the string
# def string_reverse(s):
#     if len(s) <= 1:
#         return s
    
#     return string_reverse(s[1:]) + s[0] 

# print(string_reverse("Bruce"))

    
    