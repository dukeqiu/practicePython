import random

def game(word):
    wrong = 0
    win = False
    print("Welcome to Hangman game.")
    reletters = list(word)
    board = ["_"] * len(word)
    stage = [" ",
    "---------------",
    "|       |      ",
    "|       O      ",
    "|       |      ",
    "|      /|\     ",
    "|      / \     ",
    "|              ",
    "|              "
    ]
    while wrong < len(stage) - 1:
        char = input("\nPlease guess a letter: ")
        if char in word:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = "$"
        else:
            wrong += 1
        e = wrong + 1
        print(" ".join(board))
        print("\n".join(stage[0:e]))
        if "_" not in board:
            win = True
            print("You win!")
            print(" ".join(board))
            break
    if not win:
        print("You lose. It was {}.".format(word))

i = random.randint(0,9)
word_list = [
"hello",
"mary",
"duke",
"and",
"alibaba",
"alipay",
"room",
"love",
"happy",
"money"
]

game(word_list[i])
