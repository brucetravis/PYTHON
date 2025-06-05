2️⃣ Student Grade Manager
Concept:

Store student names and their grades in a list.
Allow the user to add students, remove students, and view all grades.
Features:
✅ Add student and grade
✅ Remove a student
✅ Calculate the class average

# .title() capitalizes the first letter of each word and ensures the rest are in lowercase.

# This ensures proper formatting even if the user enters the name in all caps or lowercase.


any() in Python
any() is a built-in function that returns True if at least one element in an iterable is True; otherwise, it returns False

# Syntax:
any(iterable)


iterable – Can be a list, tuple, set, dictionary, etc.
Returns:
True if at least one element is truthy.
False if all elements are falsy.

numbers = [0, 0, 0, 5]  
print(any(numbers))  # Output: True (because 5 is truthy)



# A loop to check If a student exists in python(inefficient way)

# # Loop through the list checking If the student exists in each Iteration
    # for student in students:
    #     # Check by the name to confirm If the student already exists
    #     if student["name"] == name:
    #         print("Student already exists! exists.")
    #         # Exit the loop
    #         return



# IDEA: We can Include the position of a student
