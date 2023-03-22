import random, os
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6
chosen_word = random.choice(word_list)
repeated_letters = []

os.system('clear')
#print(f'Pssst, the solution is {chosen_word}.')
print(logo)
# print(chosen_word)
#making an array display with "_" = len(chosen_word)
display = []
for letter in chosen_word:
    display += "_"

#function to check letters in chosen_word
def letter_checker(): 
    position = 0
   
    guess_frequency = 0
    for letter in chosen_word:
        if letter == guess:
            display[position] = guess
            guess_frequency += 1
        position += 1

    print(f"{' '.join(display)}") 
    return guess_frequency


win = False
#main loop
print(display)
while win!= True:
    guess = input("Guess a letter: ").lower()

    x = 0
    for letter in repeated_letters :
        if letter == guess:
            print("You've already gussed the word ' " + guess + "'. Please try again.")
            x += 1
            break
    repeated_letters += guess

    if x == 0:
        #checking the letter 
        if (letter_checker()) == 0:
            lives -= 1
            print("You entered " + guess + ", which is not in the word. You lost a life")
            print(stages[lives])
        else: 
            print(stages[lives])
        
        if "_" not in display:
            print("You Won")
            win = True
        elif lives == 0:
            print("You Lost")
            break 

