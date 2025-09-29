#Caesar Cipher
#The Caesar cipher moves each letter forward in the alphabet by
#the key.  The resulting message has all the letters advanced by 'key'
#letters.
#To run the code, run the main() function

def encode(message, key):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    secret = ""

    for letter in message:
        if (alpha.find(letter) >= 0): #check to see if the letter is actually a letter
            spot = (alpha.find(letter) + key) % 26
            secret = secret + alpha[spot]
        else: # letter must have been a number, symbol, or punctuation.
            secret = secret + letter

    return secret

def decode(message, key):
    """
    Decodes a Caesar Cipher message by shifting each letter back by the key.
    Shifting back is the same as encoding with a negative key.
    """
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()
    plaintext = ""

    # The decoding process is the same as encoding, but the key is subtracted
    # from the spot. Python's % operator handles negative numbers correctly
    # for 'wrap-around' logic. For example, (-3) % 26 is 23 (W).
    for letter in message:
        if (alpha.find(letter) >= 0): # Check if the letter is in the alphabet
            # Subtract the key to go backward in the alphabet
            spot = (alpha.find(letter) - key) % 26
            plaintext = plaintext + alpha[spot]
        else: # Preserve non-alphabetic characters
            plaintext = plaintext + letter

    return plaintext

def main():
    message = input("Enter a message: ")
    # Ensure the key is an integer for the math to work
    try:
        key = int(input("Enter a key: "))
    except ValueError:
        print("Invalid key. Please enter an integer.")
        return

    secret = encode(message, key)
    print ("Encrypted:", secret)
    plaintext = decode(secret, key)
    print ("Decrypted:", plaintext)

#def decode(message, key):
    #We will want to decode the message here.

def main():
    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    secret = encode(message, key)
    print ("Encrypted:", secret)
    plaintext = decode(secret, key)
    print ("Decrypted:", plaintext)


if __name__ == '__main__':
  main()
