import random

def numberToLetter(n):
    return chr(97 + n)

def letterToNumber(l):
    return ord(l) - 97

def compare(password, query):
    if password < query:
        print("Too high! PASSWORD < " + str(query))
    else:
        print("Too low!  PASSWORD > " + str(query))

if __name__ == '__main__':
    random.seed()
    password = random.randint(0,1024)
    usr_input = input("Enter your guess: ")
    guess = int(usr_input)
    count = 1
    while(password != guess):
        compare(password, guess)
        usr_input = input("Enter your guess: ")
        guess = int(usr_input)
        count += 1
    print("That's correct, and it only took you " + str(count) + " tries!")
