import random

#Creating function for random word
def choose_word():
    words = ["computer", "keyboard", "mouse", "screen", "speaker", "cord"]
    return random.choice(words)

#prompt user to guess letter 
def display_word(word, guessed_letters):
    results = ""

    for letter in word:
        if letter in guessed_letters:
            results += letter + ""
        else:
                results += "_"
                
    return results.strip()

#checking to see if word has been guessed

def check_win(word, guessed_letters):
    return all(letter in guessed_letters for letter in word)

#creating the main function of the guessing game

def play_game():
    word = choose_word()
    guessed_letters = []
    attempts = 5

    print("The Greatest Guessing Game Ever!")
    print("Guess one letter at a time.")
    print(f"You have {attempts} incorrect attempts allowed.")


    #continue until user guesses the word

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts remaining:", attempts)

        guess = input ("Enter a letter: ").lower().strip()

    #making sure the player enters a valid letter
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

    #prevent the same letter from being guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        guessed_letters.append(guess)

    #check whether the letter is in the word
        if guess in word:
            print("Correct guess!")

        else:
            attempts -= 1
            print("Incorrect guess.")

    #check whether all letters have been guessed
        if check_win(word, guessed_letters):
            print("\nCongratulations! You guess the word:", word)
            return

    #display message if runs out of attempts
    print("\nGAME OVER! The word was:", word)

    #start the game
if __name__== "__main__":
    play_game()
        
    
                        
