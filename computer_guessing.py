import random


def compare(password, query):
    if password < query:
        print("PASSWORD < " + str(query))
        return -1
    else:
        print("PASSWORD > " + str(query))
        return 1

if __name__ == '__main__':
    random.seed()
    max = 100000000
    delta = max / 2
    password = random.randint(0,max)

    count = 1
    guess = delta
    while(password != guess):
        delta /= 2
        if password < guess:
            guess -= delta
        else:
            guess += delta
        count += 1
    print("\n" + str(guess) + " is correct, and it only took you " + str(count) + " tries!")
