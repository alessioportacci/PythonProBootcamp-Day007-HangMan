import random
import words
import ascii_art

print(ascii_art.logo)

chosen_word = random.choice(words.word_list)
print(chosen_word)

ended = False
lives = 6
display = []
guessed_letters = []

for letter in chosen_word:
  display.append("_")
  
while not ended:
  user_letter = input("Choose a letter ").lower()

  if user_letter not in guessed_letters:
    #Save the letter
    guessed_letters.append(user_letter)
    #Update guess letters
    for i in range(len(chosen_word)):
      if chosen_word[i] == user_letter:
        display[i] = user_letter
    #If wrong guess
    if user_letter not in chosen_word:
      lives -= 1
      print(f"You guessed {user_letter}, that's not in the word. You lose a life.")

    #Check if player has lost
    if lives == 0:
      endend = True
      print("You lost")
    #Check if player has won
    elif "_" not in display:
      ended = True
      print("You win")
      
  else:
    print(f"You've already guessed {user_letter}")

  #Print hangman
  if not ended:
    print(ascii_art.stages[lives])
    print (display)

