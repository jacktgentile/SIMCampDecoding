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
    password = random.randint(0,1024)
    count = 1
    delta = 512

    guess = delta
    while(password != guess):
        delta /= 2
        if password < guess:
            guess -= delta
        else:
            guess += delta
        count += 1
    print(str(guess) + " is correct, and it only took you " + str(count) + " tries!")
