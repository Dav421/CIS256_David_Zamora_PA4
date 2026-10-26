#David Zamora
#CIS256 Fall 2026
#Programming Assignment 4


from guess_the_word import choose_word, display_word, check_win

#Test 1: Verify random word is coming from list
def test_choose_word():
    words = ["computer", "keyboard", "mouse", "screen", "speaker", "cord"]
    selected_word = choose_word()
    assert selected_word in words

#Test 2: Verify correctly guessed letters are revealed
def test_correct_guess():
    word = "computer"
    guessed_letters = ["c", "o"]
    result = display_word(word, guessed_letters)
    assert result == "co______"

#Test 3: Verify incorrect guesses do not reveal letters
def test_incorrect_guess():
    word = "mouse"
    guessed_letters = ["x"]
    result = display_word(word, guessed_letters)
    assert result == "_____"

#Test 4: Verify repeated letters are revealed
def test_repeated_letters():
    word = "screen"
    guessed_letters = ["e"]
    result = display_word(word, guessed_letters)
    assert result == "___ee_"

#Test 5: Verify the player wins after they guess all letters
def test_check_win():
    word = "mouse"
    guessed_letters = ["m", "o", "u", "s", "e"]
    assert check_win(word, guessed_letters) is True

#Test 6: Verify incomplete guesses do not win
def test_check_not_win():
    word = "mouse"
    guessed_letters = ["m", "o"]
    assert check_win(word, guessed_letters) is False
    

            
    
