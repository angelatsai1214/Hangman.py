class Player:
  
  def ask_for_a_letter():
    guess = input("\nGuess a letter for the word: ").lower()
    #only get the first letter in case the player entered a word
    guess = guess[0]
    return guess