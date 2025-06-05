# function to contain the strings
def vowel_function(word):
    # list of vowels
    vowel_list = ["a", "e", "i", "o", "u"]
    # convert the vowel list to lower case to handle uppercase and lower case letters
    lower_vowel_list = [vowel.lower() for vowel in vowel_list]
    
    # convert the word to lower case
    word = word.lower()
    
    # Keep track of all the vowels in the list
    count = 0
    
    # Loop to loop through every letter in the parameter
    for i in word:
        # Condition to check if the lettter is amotng the vowels
        if i in lower_vowel_list:
            # print(i)
            count += 1
    
    # after looping return the count
    return count


print(vowel_function("Bruce Ambundo"))


