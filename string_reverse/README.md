Reverse a string – Without using [::-1] or .reverse().


# PLAN
1. Loop through each character in word
2. Get the last index
3. Decrease from the last index in order to print It in reverse

# NOTES
If we never include the step in range(start, stop), Python assumes the default step is +1 (moving forward).

Example Without Step
python
Copy
Edit
for i in range(5, 0):  
    print(i)
🔴 This will NOT work! It won’t print anything.

Why?

range(5, 0) means:
Start at 5
Stop before 0
Default step = +1 (which means counting up, not down).
But starting at 5 and increasing will never reach 0—so the loop does nothing. ❌
Fixing It: Using -1 Step
If we want to count backward, we must specify -1 as the step:

python
Copy
Edit
for i in range(5, 0, -1):
    print(i)
✅ Output:

Copy
Edit
5
4
3
2
1
Starts at 5
Stops before 0
Step -1 moves backward
Final Rule
If you don’t specify the step, Python assumes +1.
If you want to count backward, you must specify -1.