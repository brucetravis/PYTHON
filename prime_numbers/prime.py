# Function to check If a number is prime
def prime_number(n):
    # Check If n is prime
    
    # If n is less than 1 num is not prime
    if n < 1:
        print(f"{n}: is NOT  a prime number.") 
        return
    
    # Loop through all the numbers i a range of numbers
    for i in range(2, n):
        # If n is divided by any number in the range and the remainder is 0
        if n % i == 0:
            # Print out a message
            print(f"{n}: is NOT a prime number.")
            return
        
    print(f"{n}: is a prime number.")
        
prime_number(50)
