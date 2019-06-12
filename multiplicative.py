# DECLARE ANY EXTRA FUNCTIONS HERE



def encryptLetter(letter, key):
    if not letter.isalpha():
        return letter
    num = ord(letter)-97
    num = (num * key) % 26
    return chr(num+97)


### ---------- DO NOT TOUCH THIS CODE ---------- ###
if __name__ == '__main__':
    message = input("Enter your message:  ").lower()
    key = int(input("Enter your key:  "))
    secret_message = ""
    for c in message:
        secret_message += encryptLetter(c, key)
    print("Encrypted message is\n" + secret_message)
