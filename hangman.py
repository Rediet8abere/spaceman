import random
import time


hangman = (

"""
   _________
    |/
    |
    |
    |
    |
    |
    |___
    """,

"""
   _________
    |/   |
    |
    |
    |
    |
    |
    |___
    H""",

"""
   _________
    |/   |
    |   (_)
    |
    |
    |
    |
    |___
    HA""",

"""
   ________
    |/   |
    |   (_)
    |    |
    |    |
    |
    |
    |___
    HAN""",


"""
   _________
    |/   |
    |   (_)
    |   /|
    |    |
    |
    |
    |___
    HANG""",


"""
   _________
    |/   |
    |   (_)
    |   /|\
    |    |
    |
    |
    |___
    HANGM""",



"""
   ________
    |/   |
    |   (_)
    |   /|\
    |    |
    |   /
    |
    |___
    HANGMA""",


"""
   ________
    |/   |
    |   (_)
    |   /|\
    |    |
    |   / \
    |
    |___
    HANGMAN""")

wrong = 0
used = []
password = "python".upper()

words = open("words.txt", "r").read().split()

words = str(random.choice(words).upper())


print(" ")
print("-----Welcome to HANGMAN, You get seven chances to guess the mystery word-----")
print(" ")

max_wrong = len(hangman) - 1



so_far = "*" * len(words)
print("You need to guess", len(words), "letters word")
while wrong < max_wrong and so_far != words:


    print(hangman[wrong])

    print("\nYou've used the following letters:\n", used)
    print("\nSo far, the word is:\n", so_far)

    inp = input("Pick a letter----->").upper()

    if inp == password:
        print(" ")
        print("please wait...")
        time.sleep(3)
        print("cheat-code activated")
        print(" ")
        print("Correct word is", words)
        exit()

    if inp.isdigit() is True:
        print("Invalid Input")
        continue

    if len(inp) > 1:
        print("Invalid Input")
        continue
    while inp in used:
        print("You've already guessed the letter:", inp)
        inp = input("Pick a letter----->").upper()


        if inp.isalpha() is False:
            print("Invalid Input")
            continue

        if len(inp) > 1:
            print("Invalid Input")
            continue

    used.append(inp)

    if inp in words:
        print("Yes,", inp, "is in the word!")
        new = ""
        for i in range(len(words)):
            if inp == words[i]:
                new += inp
            else:
                new += so_far[i]
        so_far = new

    else:
        print("Sorry,", inp, "isn't in the word.")
        wrong += 1

if (wrong == max_wrong):
    print( hangman[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")

print("\nThe word was", words)
