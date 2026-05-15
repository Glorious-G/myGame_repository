import random

def start_game():
    secret_number = random.randint(1,100)
    max_attempts = 10
    attempts = 0 
   
    print("I'm thinking of a number between 1 and 100.") 
    
    while attempts < max_attempts:

        guess = int(input("Enter your guess:"))

        #Validate input range
        if guess < 1 or guess > 100:
            print("Invalid number! Please enter a number between 1 and 100.")
           
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:  
            print("Too high! Try again.")  
        else:
             print(f"Congratulations! You found it in {attempts} tries.")
             break
        #Remaining guesses
        remaining = max_attempts - attempts
        print(f"You have{remaining}guesses left.")
    else:
        print("You are out of guesses!")
        print(f"The correct numberwas{secret_number}.")
        
start_game()
