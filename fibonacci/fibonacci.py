# Function to generate a fibonacci number
def fibonacci(n):
    # Starting numbers
    sequence = [0, 1]

    # Loop through the numbers
    for i in range(2, n): #start from index 2
        next_number = sequence[i - 1] + sequence[i - 2] # Formula: F(n) = F(n - 1) + F(n - 2)
        sequence.append(next_number) #Add to sequence
        
    return sequence[:n]  # Return only the first n terms


# Example: Generate Fibonacci sequence up to n terms
n = int(input("Enter the number of terms: "))  # Get input from user
print(f"Fibonacci sequence up to {n} terms:", fibonacci(n))  # Display result

