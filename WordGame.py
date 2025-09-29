#Word Game is a knock-off version of a popular online word-guessing game.

import random

def inWord(letter, word):
    """Returns boolean if letter is anywhere in the given word"""
    # The 'in' operator checks if a substring (letter) exists in a string (word).
    return letter in word

def inSpot(letter, word, spot):
    """Returns boolean response if letter is in the given spot in the word."""
    # Check if the character at the specified index (spot) of the word matches the letter.
    # Note: spot should be a 0-indexed integer (0 for the first letter, 4 for the last).
    return word[spot] == letter

def rateGuess(myGuess, word):
    """Rates your guess and returns a word with the following features.
    - Capital letter if the letter is in the right spot
    - Lower case letter if the letter is in the word but in the wrong spot
    - * if the letter is not in the word at all"""

    # Ensure both are uppercase for consistent comparison
    myGuess = myGuess.upper()
    word = word.upper()
    
    feedback = ""

    # Iterate through each letter of the 5-letter guess
    for i in range(5):
        letter = myGuess[i]

        # 1. Check for a perfect match (in the right spot)
        if inSpot(letter, word, i):
            feedback += letter.upper()  # Capital letter for correct spot
        
        # 2. Check if the letter is in the word, but not in this spot
        elif inWord(letter, word):
            # The letter is in the word (inWord is True), but not at the current spot (inSpot was False)
            feedback += letter.lower()  # Lowercase letter for correct letter, wrong spot
        
        # 3. The letter is not in the word at all
        else:
            feedback += "*"  # Asterisk for a completely wrong letter

    return feedback

def main():
    # Pick a random word from the list of all words
    # NOTE: You must have a 'words.txt' file containing a list of 5-letter words, one per line.
    try:
        with open("words.txt", 'r') as wordFile:
            content = wordFile.read()
            wordList = [w.strip().upper() for w in content.split("\n") if len(w.strip()) == 5]
    except FileNotFoundError:
        print("Error: 'words.txt' file not found. Using a placeholder word.")
        wordList = ["GREAT", "PLANT", "CRANE", "TRAIN", "HOUSE"]

    if not wordList:
        print("Error: No 5-letter words found in the list. Exiting.")
        return

    todayWord = random.choice(wordList)
    
    # Optional: For testing/debugging, you can uncomment this line:
    # print(f"DEBUG: The word is {todayWord}")

    MAX_TRIES = 6
    guess_count = 0
    solved = False

    print("\nWelcome to Word Game! Guess the 5-letter word.")
    
    # User should get 6 guesses
    while guess_count < MAX_TRIES and not solved:
        guess_count += 1
        
        # --- Get Valid Guess from User ---
        while True:
            myGuess = input(f"Guess {guess_count}/{MAX_TRIES}: ").strip().upper()
            if len(myGuess) == 5 and myGuess.isalpha():
                break
            else:
                print("Invalid input. Please enter a 5-letter word.")

        # --- Check Guess and Provide Feedback ---
        if myGuess == todayWord:
            solved = True
            print(f"\n***** {myGuess.upper()} *****")
        else:
            feedback = rateGuess(myGuess, todayWord)
            print(f"Feedback: {feedback}") # e.g., "Feedback: sW*EE"

    # --- Game End Condition ---
    if solved:
        print(f"\n🎉 CONGRATULATIONS! You guessed the word '{todayWord}' in {guess_count} tries!")
    else:
        print(f"\n😭 OUT OF TRIES. The word was '{todayWord}'. Better luck next time!")


if __name__ == '__main__':
    main()