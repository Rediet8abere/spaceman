from spaceman import *


def test_is_word_guessed():
    assert is_word_guessed('happy', ['h', 'a', 'y', 'p']) == True
    assert is_word_guessed('dehydrator', ['a', 'd', 'h', 't', 'e', 'r', 'o']) == False
    # assert my_sum_function([3, 5]) == 8

def test_is_guess_in_word():
    assert is_guess_in_word('l', 'apple') == True
    assert is_guess_in_word('k', 'apple') == False
    assert is_guess_in_word(5, 'apple') == False

def test_get_guessed_word():
    assert get_guessed_word('flowery', ['l','y']) == '_ l_ _ _ _ y'
    assert get_guessed_word('workingman', []) == '_ _ _ _ _ _ _ _ _ _ '
    assert get_guessed_word('unstrained', ['f', 't', 'a', 'd', 'k']) == '_ _ _ t_ a_ _ _ d'
