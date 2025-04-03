# Fibonacci number: A Fibonacci number, is a sequence of numbers where each number is the sum of the two preceding numbers(2 numbers before It)

# When doing Fibonacci, we always start with 0 or 1, then from there each number is obtained by adding the previous two numbers.



# In Fibonacci It is all about indexing, n is the index and the goal is to find which number will be at n

# F(n) = F(n - 1) + F(n - 1)

# At indices 0 and 1 It is always the numbers 0 and 1 taking up the positions respectively

# F(0) = 0
# F(1) = 1

# Both of these will always be 0 and 1 respectively. Let's do till index 6

# FORMULA
# F(n) = F(n - 1) + F(n - 2)

# F(0) = 0
# F(1) = 1

# Sequence 0, 1,
# Index:   0  1 

# F(2) = F(2 - 1) + F(2 - 2)
# F(2) = F(1) + F(0)
# F(2) = 1 + 0

# F(2) = 1

# Sequence: 0, 1, 1
# Index: 0, 1, 2

# F(3) = F(3 - 1) + F(3 - 2)
# F(3) = F(2) + F(1)
# F(3) = 1 + 1

# F(3) = 2

# Sequence 0, 1, 1, 2
# Index:   0, 1, 2, 3

# F(4) = F(4 - 1) + F(4 - 2)
# F(4) = F(3) + F(2)
# F(4) = 2 + 1

# F(4) = 3

# Sequence 0, 1, 1, 2, 3
# Index:   0, 1, 2, 3, 4

# F(5) = F(5 - 1) + F(5 - 2)
# F(5) = F(4) + F(3)
# F(5) = 3 + 2

# F(5) = 5

# Sequence 0, 1, 1, 2, 3, 5
# Index:   0, 1, 2, 3, 4, 5


# F(6) = F(6 - 1) + F(6 - 2)
# F(6) = F(5) + F(4)
# F(6) = 5 + 3

# F(6) = 8

# Sequence 0, 1, 1, 2, 3, 5, 8
# Index:   0, 1, 2, 3, 4, 5, 6



