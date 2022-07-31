import random
from words import word_list

class Game_Functions:
  
  def split_word_by_char(word):
    return list(word)

  
  def print_list(list):
    for x in list:
      print(x, end=" ")
    print()

  
  def was_guessed(guess, guessed_char):
    for guessed in guessed_char:
      if guess == guessed:
        print("\nYou've guessed the letter already. \nPlease choose another letter.")
        return True
    return False


  def print_missed_letter(missed_char):
    if len(missed_char) == 0:
      print("\nMissed letters: No missed letters yet." )
    else:
      print("\nMissed letters: ", end="")
      Game_Functions.print_list(missed_char)

  
  def get_random_word():
    word = random.choice(word_list)
    return word

  
  def get_dashes(word):
    dash_list = []
    for x in range(0,len(word)):
      dash_list.append('_')
    return dash_list