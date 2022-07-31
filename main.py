#import
from function import Game_Functions
from player import Player

#Constant
HANGMAN = [
    '''  
       +---+
       |   |
           |
           |
           |
           |
           |
    ==========''',
  '''  
       +---+
       |   |
       o   |
           |
           |
           |
           |
    ==========''',
  '''  
       +---+
       |   |
       o   |
       |   |
           |
           |
           |
    ==========''',
  '''  
       +---+
       |   |
       o   |
       |   |
       |   |
           |
           |
    ==========''',
  '''  
       +---+
       |   |
       o   |
      /|   |
       |   |
           |
           |
    ==========''',
  '''  
       +---+
       |   |
       o   |
      /|\  |
       |   |
           |
           |
    ==========''',
    '''  
       +---+
       |   |
       o   |
      /|\  |
       |   |
      /    |
           |
    ==========''',
    '''  
       +---+
       |   |
       o   |
      /|\  |
       |   |
      / \  |
           |
    =========='''
]
  
# Main
print("Welcome to Hangman!")

hangman_index = 0
missed_char = set()
guessed_char = set()
was_guessed = False
word = Game_Functions.get_random_word()
dash_list = Game_Functions.get_dashes(word)
can_add = True

while True:

  #print hangman
  print(HANGMAN[hangman_index])

  #print missed letters
  Game_Functions.print_missed_letter(missed_char)

  #print the dash lines
  print()
  Game_Functions.print_list(dash_list)
  word_char_list = Game_Functions.split_word_by_char(word)

  #check end game conditions
  #winning condition
  if dash_list == word_char_list:
    print("\nCongratulations, you got the word!")
    break
  #losing condition
  if hangman_index == 7:
    print("\nGameover, you lost")
    print("The word was: " + word)
    break

  #ask player for a letter
  guess = Player.ask_for_a_letter()

  #check if the player repeated their guesses
  was_guessed = Game_Functions.was_guessed(guess, guessed_char)

  #continue only if player didn't repeat guesses
  if was_guessed == False:
    guessed_char.add(guess)
    index = -1
    correct = False
    #replace dash line with guess if the letters match
    for c in word_char_list:
      index+=1
      if guess == c:
        correct = True
        dash_list[index] = word_char_list[index]

    #update missed_char and hangman_index if the guess wasn't a letter in the word
    if correct == False:
      for missed in missed_char:
        if guess == missed:
          can_add = False
          break
        else:
          can_add = True
      if can_add:
        missed_char.add(guess)
        hangman_index += 1

