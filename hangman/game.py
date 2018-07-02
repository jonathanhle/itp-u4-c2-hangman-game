from .exceptions import *
import random
from string import ascii_lowercase

# Complete with your own, just for fun :)
LIST_OF_WORDS = ['hoang', 'clare', 'dianne']


def _get_random_word(list_of_words):
    if not list_of_words:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words)

def _mask_word(word):
    if not word:
        raise InvalidWordException()
    else:
        return '*' * len(word)


def _uncover_word(answer_word, masked_word, character):
    if not answer_word or not masked_word:
        raise InvalidWordException()
    elif len(character) > 1:
        raise InvalidGuessedLetterException()
    elif len(answer_word) is not len(masked_word):
        raise InvalidWordException()
        
    answer_word_list = list(answer_word)
    masked_word_list = list(masked_word)
    new_masked_word = ""
    matching_index = []
        
    if character.lower() not in answer_word.lower():
        return masked_word
    
    for char_index,value in enumerate(answer_word_list):
        if masked_word_list[char_index].lower() in ascii_lowercase:
            new_masked_word += masked_word_list[char_index].lower()
        elif value.lower() == character.lower():
            new_masked_word += character.lower()
        else:
            new_masked_word += '*'
            
    return new_masked_word
        
        
    

def guess_letter(game, letter):
    pass
    







def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
