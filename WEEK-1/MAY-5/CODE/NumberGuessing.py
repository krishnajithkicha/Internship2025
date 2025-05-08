import random
def numberguessing():
    print("*****NUMBER GUESSING GAME*******")
    print("You have to think of a number between the given range")
    print("I will try to guess the number you are thinking of")
    print("You have to give me hints whether my guess is too high or too low")
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    print("Please think of a number between", lower_bound, "and", upper_bound)
    attempts = 0
    while True:
        guess=random.randint(lower_bound, upper_bound)
        attempts += 1
        print("Is your number", guess, "?")
        answer=input("Enter 'h' if my guess is too high, 'l' if it's too low, or 'c' if I guessed it right: ")
        if answer=="h":
            upper_bound = guess - 1
        elif answer=='l':
            lower_bound = guess + 1
        elif answer=='c':
            print("Yay! I guessed your number in", attempts, "attempts.")
            break
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")
numberguessing()
