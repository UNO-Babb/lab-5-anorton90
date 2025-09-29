#LetterFrequency.py
#Name:Alyssia Norton
#Date:9-28-25
#Assignment:lab 5

#This program will create a CSV file of frequencies based on a text file.
#Use Excel or similar spreadsheet software to visualize the frequencies of the CSV file.

import os

def countLetters(message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    message = message.upper()

    freq = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    #loop through each letter
    #Find the position in the alphabet
    #Increase the frequency at that position. If position was 5, then frequencies[5] = frequencies[5] + 1

    for letter in message:
        spot = alpha.find(letter)
        if spot >= 0:
            freq[spot] = freq[spot] + 1

    output = ""
    for i in range(26):
        print (alpha[i], ":", freq[i])
        line = alpha[i] + "," + str(freq[i]) + "\n"
        output = output + line

    writeToFile(output)


def writeToFile(fileText):
    # This setup is typically for online environments like repl.it or specific local setups
    # It ensures the file is saved in the correct directory.
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.chdir(dir_path)

    freqFile = open("frq.csv", 'w')
    freqFile.write(fileText)

    freqFile.close()
    print("\nFrequencies saved to 'frq.csv'. Open this file to create your chart!")


def main():
    msg = input("Enter a message: ")
    countLetters(msg)


if __name__ == '__main__':
  main()
