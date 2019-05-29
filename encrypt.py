def numberToLetter(num):
    return chr(97 + num)

def letterToNumber(letter):
    return ord(letter) - 97


def encryptLetter(letter, key):
    num = letterToNumber(letter)
    num = (num + key) % 26
    return numberToLetter(num)


if __name__ == '__main__':
    message = input("Enter your message:  ").lower()
    key = int(input("Enter your key:  "))
    secret_message = ""
    for c in message:
        if c.isalpha():
            secret_message += encryptLetter(c, key)
        else:
            secret_message += c
    print("Encrypted message is\n" + secret_message)
