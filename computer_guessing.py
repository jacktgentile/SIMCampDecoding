import random

### password is the actual value, query is the guess
### return -1 if password < query, 1 otherwise
def compare(password, query):
    if password < query:
        print("PASSWORD < " + str(query))
        return -1
    else:
        print("PASSWORD > " + str(query))
        return 1


if __name__ == '__main__':
    random.seed()
    max = 1000000
    password = random.randint(0,max)

    count = 1
    guess = max / 2
    while(password != guess):
        count += 1
### ---------- EDIT THE CODE BELOW THIS COMMENT ---------- ###
        if password < guess:
            guess = guess - 1
        else:
            guess = guess + 1
### ---------- EDIT THE CODE ABOVE THIS COMMENT ---------- ###
    print("\n" + str(guess) + " is correct, and it only took you " + str(count) + " tries!")
