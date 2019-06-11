import random


if __name__ == '__main__':
    # This stuff happens once at the beginning of the program
    random.seed()
    max = 10000
    password = random.randint(0, max)

    # Change the code below
    # Here are your initial values
    count = 1
    guess = 0
    delta = 1
    while(abs(password-guess) > 0.5):
        # This stuff happens everytime our guess is wrong
        count = count + 1
        delta = 1
        if password < guess:
            guess = guess - delta
        else:
            guess = guess + delta
    # Don't change this line
    print("\n" + str(password) + " is correct, and it only took you " + str(count) + " tries!")
