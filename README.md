# PYTHON
Coding with Lumi

Find the second largest number in a list


# What is "Negative Infinity"?
Negative infinity is a concept from mathematics that represents an infinitely small number (i.e., a number that is smaller than any real number, no matter how negative).

In Python, float('-inf') is a special value that represents negative infinity.

When you initialize variables with negative infinity, it ensures that any number you compare will be larger than that initial value.

# Why do we use negative infinity here?
In the case of finding the largest and second-largest numbers, we want to ensure that:

The first number in the list will automatically be treated as the largest number when you start the loop.

We want to have a "small" starting value for max_num and second_max_num, so when you compare the first element, it gets assigned as the first largest number.

How does float('-inf') help in this case?
When you initialize max_num and second_max_num with float('-inf'), it ensures that no matter what values are in your list, the first comparison will make the first element in the list the new max_num, since all elements in the list will be greater than negative infinity.

As you continue the loop, if you find a number greater than the current max_num, that number becomes the new max_num, and the old max_num becomes the second_max_num.


max_num = second_max_num = float('-inf')

max_num = float('-inf'): The max_num starts with negative infinity, so the very first number in the list will automatically be greater than this and get assigned to max_num.

second_max_num = float('-inf'): Similarly, the second_max_num starts at negative infinity, so any number larger than second_max_num (and smaller than max_num) will be considered as the second largest.


Step-by-Step Explanation
Initial Setup:

max_num = -∞ (negative infinity)

second_max_num = -∞ (negative infinity)

For the first number (10):

max_num = -∞, second_max_num = -∞

Since 10 > max_num, we update second_max_num = max_num (which is -∞), and then max_num = 10.

So now:

max_num = 10

second_max_num = -∞

For the next number (20):

max_num = 10, second_max_num = -∞

Since 20 > max_num, we update second_max_num = max_num (which is 10), and then max_num = 20.

So now:

max_num = 20

second_max_num = 10

For a number smaller than max_num but larger than second_max_num (e.g., 15):

max_num = 20, second_max_num = 10

Since 15 > second_max_num and 15 != max_num, the condition elif num > second_max_num and num != max_num: becomes True.

We then update second_max_num = 15, keeping max_num = 20.

So now:

max_num = 20

second_max_num = 15

Why use elif num > second_max_num and num != max_num:?
The condition elif num > second_max_num and num != max_num: ensures that:

num > second_max_num: We only update second_max_num if the current number is larger than the current second largest number.

num != max_num: We make sure that we don't mistakenly set second_max_num to the value of max_num (which would happen if num were equal to max_num). This avoids having both max_num and second_max_num hold the same value.

Full Example with Numbers:
Let's go through an example:

Initial State:


max_num = -float('inf')  # Represents negative infinity
second_max_num = -float('inf')  # Represents negative infinity
Processing numbers:

num = 10:


if num > max_num:  # 10 > -inf
    second_max_num = max_num  # second_max_num = -inf
    max_num = 10  # max_num = 10
After processing 10:

max_num = 10

second_max_num = -inf

num = 20:


if num > max_num:  # 20 > 10
    second_max_num = max_num  # second_max_num = 10
    max_num = 20  # max_num = 20
After processing 20:

max_num = 20

second_max_num = 10

num = 15:


elif num > second_max_num and num != max_num:  # 15 > 10 and 15 != 20
    second_max_num = 15  # second_max_num = 15
After processing 15:

max_num = 20

second_max_num = 15

Final Result:

max_num = 20

second_max_num = 15

