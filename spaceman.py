import random
rocket = (
"""
   ________
    |/  /
    |  /(_)
    |  |/| |
    |  | | |
    |  |/  |
    |  |___|
    |  `````
    |___
    spaceman""",

    """
       ________
        |/   /
        |   /(_)
        |   |/| |
        |   | | |
        |   |/  |
        |   |   |
        |___
        spacema""",

      """
     _________
      |/   /
      |   /(_)
      |   |/| |
      |   | | |
      |   |   |
      |   |   |
      |___
      spacem""",
      """
     _________
      |/   /
      |   /(_)
      |   |/| |
      |   | | |
      |   |   |
      |
      |___
      space""",
      """
     ________
      |/  /
      |  /(_)
      |  | | |
      |  | | |
      |
      |
      |___
      spa""",
   """
      _________
       |/  /
       |  /(_)
       |
       |
       |
       |
       |___
       sp""",
    """
      _________
       |/   /
       |
       |
       |
       |
       |
       |___
       s""",
       """
      _________
       |/
       |
       |
       |
       |
       |
       |___
       """
)

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.
    Returns:
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    #print(words_list[0])
    #print(words_list)
    secret_word = random.choice(words_list)
    #print(secret_word)
    return secret_word, words_list

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    for letters in secret_word:
        if letters in letters_guessed:
            continue
        else:
            return False

    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.
    Returns:
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    ##print(letters_guessed)
    word_sofar = ""
    for letter in secret_word:
        if letter in letters_guessed:
            word_sofar += letter
        else:
            word_sofar += "_ "
    return word_sofar


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word
    for letter in secret_word:
        if letter == guess:
            return True
    return False
def mystery(secret_word, words_list):
    print(secret_word)
    #print(words_list)
    print(len(secret_word))
    print(len(words_list))
    start = 0
    end = len(words_list)
    mid = (start+end)//2
    print(words_list[mid])
    print(mid)
    while start <= end:
        mid = (start+end)//2
        print(words_list[mid])
        if len(words_list[mid]) == len(secret_word):
            return True
        elif len(words_list[mid]) > len(secret_word):
            end = mid - 1
        else:
            start = mid + 1
    return False



def spaceman(secret_word, words_list):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''
    #TODO: show the player information about the game according to the project spec
    print("Welcome to Spaceman!")
    print(secret_word)
    print("The secret word contains: {} letters".format(len(secret_word)))
    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    incorrect_guess = 7
    letters_guessed = list()
    incorrect_letter = list()
    word_is_guessed = False
    while incorrect_guess > 0:
        print("You have {} incorrect guesses, please enter one letter per round". format(incorrect_guess))
        print("___________________________________________")
        player_guess = input("Enter a letter: ")
        while len(player_guess) > 1:
            print("Please only enter one letter at a time")
            player_guess = input("Enter a letter: ")
        if is_guess_in_word(player_guess, secret_word) == False:
            if player_guess in incorrect_letter:
                print("already guessed, Please try guessing another word")
            else:
                incorrect_letter.append(player_guess)
                print(incorrect_letter)
                print(incorrect_guess)
                print(rocket[incorrect_guess])
                incorrect_guess-=1
                print("Your guess is incorrect")
                if incorrect_guess == 0:
                    print(rocket[incorrect_guess])
                    print("Game lost")
                    print(secret_word)
        else:
            if player_guess in letters_guessed:
                print("already guessed, Please try guessing another word")
            else:
                print("Your guess appears in the word: ")
                mystery(secret_word, words_list)
                letters_guessed.append(player_guess)
                print("words guessed so far:  ", get_guessed_word(secret_word, letters_guessed))
                if is_word_guessed(secret_word, letters_guessed):
                    print("Game Won")
                    incorrect_guess = 0
                    player = input("Do you wanna play again?")
                    if player.lower() == "yes":
                        secret_word = load_word()
                        print(secret_word)
                        incorrect_guess = len(secret_word)


    #TODO: Check if the guessed letter is in the secret or not and give the player feedback


        #TODO: show the guessed word so far
        #TODO: check if the game has been won or lost


#These function calls that will start the game
secret_word, words_list = load_word()
spaceman(secret_word, words_list)
