Check if a number is an Armstrong number (e.g., 153 = 1³ + 5³ + 3³)

# Arm strong number definition
- It is a number that when each digit of that number is raised to the power of the total number of digits and then those digits are added, the result is the original number.

# Example
number = 153

1 ** 3 + 5 ** 3 + 3 ** 3 = 153  


# NOTES FROM POTENTIAL ERRORS
In python I cannot Iterate through an integer. Correct?


ChatGPT said:
Yes, you cannot iterate through an integer in Python because integers are not iterable.

Why?
An iterable is an object that can return its elements one by one, like lists, tuples, strings, dictionaries, and sets.

An integer is not an iterable because it is a single value, not a collection of values.

