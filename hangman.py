import random

# List of words for the game
words = ['python', 'java', 'hangman', 'programming', 'developer', 'code', 'algorithm']

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word with guessed letters
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Function to play the Hangman game
def play_hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit on incorrect guesses
    
    print("Welcome to Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Enter a letter to guess: ").lower()
        
        # Ensure the input is a valid single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! {guess} is not in the word.")
        
        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break
    else:
        print(f"\nGame over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
