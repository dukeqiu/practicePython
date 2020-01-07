def game(word):
    print("\nWelcome to Hangme Game.")
    wrong = 0
    win = False
    reletters = list(word)
    board = ["_"] * len(word)
    stage = [" ",
    "---------------------",
    "|         |          ",
    "|         O          ",
    "|         |          ",
    "|        /|\         ",
    "|        / \         ",
    "|                    ",
    ""]
    while wrong < len(stage) - 1:
        print("\n")
        char = input("Please guess a letter: ")
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = "$"
        else:
            wrong += 1
        e = wrong + 1
        print(" ".join(board))
        print("\n".join(stage[0:e]))

        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("You lose! It was {}.".format(word))


game("test")
