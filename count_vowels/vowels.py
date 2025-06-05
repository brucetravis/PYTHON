# # Function to count the vowels in a string
# def count_vowels(word):
#     # Vowels
#     vowels = "aeiouAEIOU"
#     # Return the sum of all vowels in a string
#     return sum(1 for char in word if char in vowels)


# # Text to check
# text = "ouija Board"
# print(count_vowels(text))



# # function to count the vowels in a string
# def count_vowels(word):
#     # Vowels to count
#     vowels = "aeiouAEIOU"
#     # Track the vowels in a string
#     count = 0
    
#     try:
#         # Loop though the users words to verify
#         for char in word:
#             # If the charcater in the word is in vowels
#             if char in vowels:
#                 count += 1
                
#     except Exception as e:
#         print(e)       

#     return count

# # Users text
# text = "OuijaBoard"
# print(count_vowels(text))


# Function to count the vowels
def count_vowels(words):
    # List of vowels 
    vowels = "aeiouAEIOU"
    return sum(1 for char in words if char in vowels)

word = "OuijaBoard"
print(count_vowels(word))
