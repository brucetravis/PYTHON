# Fizzbuzz function
def fizzbuzz():
    # Loop through all the numbers
    for i in range(1, 101):
        # If the number is divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            # print "FIZZBUZZ"
            print("FIZZBUZZ")
        # If the number is divisible by 5
        elif i % 5 == 0:
            # print "BUZZ"
            print("BUZZ")
        # if the number is divisible by 3
        elif i % 3 == 0:
            # print "FIZZ"
            print("FIZZ")
        else:
            # Just print the number
            print(i)
            
# Ensure that the file is being run directly and not as an imported file
if __name__ == "__main__":
    fizzbuzz()