import random
from word_list import your_word


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


#Set random word
chosen_word = random.choice(your_word)
word_length = len(chosen_word)
#print(chosen_word)
#print(word_length)

#Set 'lives', chance for fill a letter 6 times
lives = 6


#Creating an empty list from chosen word, call empty display
empty_display =[]
for _ in range(word_length):
    empty_display += "_"
#print(empty_display)
#Making loop question
end_of_game = False
while not end_of_game:
    #Ask player to guess a word
    player_guess = input("Guess a letter: ").lower()

    if player_guess in empty_display:
        print(f"You already guessed {empty_display}")


    #Check guess letter match with chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == player_guess:
            empty_display[position] = letter
    #print(empty_display)

    if player_guess not in chosen_word:
        print(f"You guessed {player_guess}, is not in the word. You are lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("YOU LOSE")

    if "_" not in empty_display:
        end_of_game = True
        print("YOU WIN")
    print(stages[lives])




