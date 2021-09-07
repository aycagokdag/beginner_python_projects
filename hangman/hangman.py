import random
from words import words
import string

def get_word():
    # chooses a word from the words file imported above
    word = random.choice(words) 
    while '-' in word or ' ' in word:
        word = random.choice(words) 
        
    return word.upper()

def hangman():
    word = get_word()
    word_letters = set(word) # keeps letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # guesses of user
    
    lives = 6
    
    while len(word_letters) > 0 and lives > 0:
        # join returns a list into a string ' '.join(['a','b','cd']) --> 'abcd'
        print('You have used these letters:', ' '.join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Your word: ', ' '.join(word_list))
        
        user_letter = input('Guess a letter:').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1;
                print('Letter is not in the word.')
                print('You have lives', lives, 'left')
        
        elif user_letter in used_letters:
            print('You have already tried that letter. Please try again.')
        
        else:
            print('Invalid character. Please try again.')
    
    if lives == 0:
        print('You lost! The word is', word)
    else:
        print('Congratulations!')

hangman()