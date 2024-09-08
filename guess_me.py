import random

#Number of times Player can guess
counter = 3
#Number of times Player Guessed
guess_counter = 0
#In Buit Range of the game is betwwen 0 to 100
program_num = random.randrange(0, 100)

# List of surprise messages
surprise_messages = [
    "You're a genius! 🌟",
    "Wow, you must have a lucky streak! 🎉",
    "Fantastic job! 🚀",
    "Impressive! You nailed it! 💪",
    "You're on fire! 🔥"
]

# Introduction message
print("Welcome to the Guessing Game! 🎉")
print("I'm thinking of a number between 0 and 99.")
print(f"You have {counter} tries to guess it. Good luck!")

#Logic 
while guess_counter < counter:
    guess_counter += 1
    #Number Player guessed
    player_num = int(input("Enter your guess: "))

    if player_num == program_num:
        surprise_message = random.choice(surprise_messages)
        print(f"WOW!! (⊙_◎) You guessed the correct number {player_num} in your {guess_counter} try!")
        break
    elif guess_counter >= counter and program_num != player_num:
        print(f"You exhuasted all of your tries. The correct number is {program_num}. ╯︿╰ Better Luck Next Time.")
    elif program_num > player_num:
        print("Try again! It's a bit higher （￣︶￣）↗　")
    elif program_num < player_num:
        print("Try again! It's a bit lower （￣︶￣）↗　")