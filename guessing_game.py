import random
import sys

my_guess = random.randint(0, 100)

def guess_number(user_guess):
    if (user_guess > my_guess):
        return (False, """sorry, lower\n""")
    if (user_guess < my_guess):
        return (False, """sorry, higher\n""")
    return (True, """Right, good guess!\n""")

def main():
    print "Welcome to my guessing game!"
    guess_result = None
    message = "Please guess a number between 1 and 100\n"
    while (guess_result is None or not guess_result):
        (guess_result, message) = guess_number(input(message))
    print(message)

main()