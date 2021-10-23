import random

"""
Guess the number game. Program chooses the random number in range 1-100 and user has to guess.
When the entered value is too small or too big, the user gets the corresponding message.

After giving a letter instead of number, the warning is showed. 
:param comp_picked_number: number chosen randomly by the computer
:param user_picked_number: consecutive guesses by the user


"""
comp_picked_number = random.randint(1,100)
while True:
    try:
        user_picked_number = int((input("Guess the number: ")))
        if (user_picked_number > 100) or (user_picked_number < 0):
            print("Number out of range")
        else:
            if user_picked_number < comp_picked_number:
                print("Too small")
            elif user_picked_number > comp_picked_number:
                print("Too big")
            elif user_picked_number == comp_picked_number:
                print("You win!")
                break
    except ValueError:
        print("It's not a number!")


