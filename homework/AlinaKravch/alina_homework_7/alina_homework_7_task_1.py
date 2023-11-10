# Guess the program number
program_number = 5
user_number = int(input("Enter a number between 1 and 10:"))

while program_number != user_number:
    print("Try again!")
    user_number = int(input("Enter a number between 1 and 10:"))

print("Congrats! You've guessed the number!")
