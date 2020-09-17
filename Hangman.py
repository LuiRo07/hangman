#Hangman game, player has to guess word before hangman is drawn

def hangman(word):
    wrong = 0
    stages = ["",
             "______       ",
             "|            ",
             "|    |       ",
             "|    0       ",
             "|   /|\      ",
             "|   / \      ",
             "|            ",
              ]
    right_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        message = "Guess a letter"
        character = input(message)
        if character in right_letters:
            character_index = right_letters.index(character)
            letter_board[character_index] = character
            right_letters[character_index] = '$'
        else:
            wrong += 1
        print((" ".join(letter_board)))
        print("\n".join(stages[0: wrong + 1]))

        if "__" not in letter_board:
            print("You win!")
            print(" ".join(letter_board))
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! The word was {}".format(word))
        
