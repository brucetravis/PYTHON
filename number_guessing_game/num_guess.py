# Import random to enable choosing of a random number
import random

def guess_num():
    # List of numbers to choose from
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # Keeping tracks of the counts of times they choose
    count = 1
    # keepinf track of the guesses
    guesses = 5
    
    # Output the numbers for the user to see
    print(numbers)
    
    try:
        # Choose a random number
        random_number = random.choice(numbers)
        # Loop so that the code keeps on asking the user to guess
        while True:
            # Prompt the user to choose a number
            user_guess = int(input("Guess the Number: "))
            # If statement to validate if the user has chosen the right number
            if user_guess == random_number:
                count += 1
                print(f"Count: {count}")
                print(f"EURIKA!!!😃😃😃, The number was {random_number}")
                break

            elif user_guess < random_number:
                print(f"You guessed low. Try again")
                print(f"Guesses: {guesses}")
                print(f"Counts: {count}")


            elif user_guess > random_number:
                print(f"You guessed High, Try again")
                print(f"Guesses: {guesses}")
                print(f"Count: {count}")


            count += 1
            guesses -= 1            

            if guesses == 0:
                print(f"😭😭😭😭 0 CHANCES LEFT\nThe number was {random_number}")

    except Exception as e:
        print(f"There was an error: {e}")

if __name__ == "__main__":
    guess_num()

