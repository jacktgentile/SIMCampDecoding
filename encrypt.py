### DECLARE ANY EXTRA FUNCTIONS HERE ###




def encryptLetter(letter, key):
    ### YOUR CODE GOES HERE ###
    return 'x'


### ---------- DO NOT TOUCH THIS CODE ---------- ###
if __name__ == '__main__':
    message = input("Enter your message:  ").lower()
    key = int(input("Enter your key:  "))
    secret_message = ""
    for c in message:
        secret_message += encryptLetter(c, key)
    print("Encrypted message is\n" + secret_message)
