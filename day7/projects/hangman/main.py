from asciis import title, stages
from word_generator.random_word import get_random_word

print(title)
print('''
Welcome to hangman!
You have a total of 5 life to find out what the word is.
The rules are simple:
    - Only guess one letter at a time, not complying will make you loose the game.
    - Each time you guess a incorrect letter a life is taken away from you, run out of life and you loose.
    - Each time you guess a correct, the letter will be shown in each place it is valid.
    - Guess the right word one letter at a time to win the game. 
''')

hanging_stages = stages.stages
word_to_guess = list(get_random_word())
cripted_word = []
wrong_guess = []
lifes = 5
word_to_guess_range = range(len(word_to_guess))

for letter in word_to_guess_range:
    cripted_word.append("_")

def has_guessed_all():
    return not "_" in cripted_word

def replace_with_letter(index, letter):
    cripted_word[index] = letter

def print_crypted_word():
    return "".join(cripted_word)

def print_results():
    print(print_crypted_word())
    print(f"The word was {"".join(word_to_guess)}")

while not has_guessed_all():
    choosen_letter = input("Choose a letter: ").lower()
    print(f"You choose: {choosen_letter}\n\n")
    if len(choosen_letter) > 1:
        print("You tried to guess to many characters at once, too bad...")
        lifes = 0
    elif lifes == 0:
        print("You have lost the game")
        print_results()
    elif choosen_letter in cripted_word:
        print(f"You already successfully guessed {choosen_letter}")
    elif choosen_letter in wrong_guess:
        print(f"You already unsuccessfully guessed {choosen_letter}")
    elif choosen_letter in word_to_guess:
        for letter_index in word_to_guess_range:
            if choosen_letter == word_to_guess[letter_index]:
                replace_with_letter(letter_index, choosen_letter)
        print(f"Good guess!\nWord to guess: {print_crypted_word()}\n\n")
    else:
        lifes -= 1
        print(f"letter {choosen_letter} isn't in the word.\n")
        print(f"{hanging_stages[lifes]}")
        print(f"Word to guess: {print_crypted_word()}\n\n")

print("You won the game, congrats!")