
import random


words = ['operator', 'overloading', 'structure', 'classes',
         'python', 'objects', 'inheritance', 'polymorphism',
         'data', 'java', 'abstract', 'float']


name = input("Enter your name? ")

while True:

  
    word = random.choice(words)

    print("Guess the characters of word")

    guesses = ''

  
    turns = 12

    while turns > 0:

   
        characters_left = 0


        print('\n')
        for char in word:

            if char in guesses:
                print(char, end=" ")

            else:
                print("_", end=" ")

                characters_left += 1

        if characters_left == 0:
           
            print("\n\nYou Win !\n")

           
            print("The word is: ", word)
            break

      
        guess = input("\n\nguess a character : ")

    
        guesses += guess

      
        if guess not in word:

            turns -= 1

          
            print("Wrong")

           
            print("You have", + turns, 'more guesses')

            if turns == 0:
                print("You Loose !")


    ch = input("Press n for New Game and q to quit : ")
    if ch == 'n':
        continue
    else:
        break
