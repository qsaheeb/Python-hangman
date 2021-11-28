stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]

import random
def hangman():
  words_list=["Arab","Kuwait","Japan","Russia","China"]
  word=words_list[random.randint(0,4)]
  word_list=list(word)
  board=["__"]*len(word)
  print(" ".join(board))
  str="Guess word?  "
  win=False
  wrong=0
  while wrong < len(stages) - 1:
    print("\n")
    char = input(str)
    if char in word_list:
      inx=word_list.index(char)
      board[inx]=word_list[inx]
      word_list[inx]='$'
    else:
      wrong+=1
    print(" ".join(board))
    print(("\n".join(stages[:wrong+1])))

    if "__" not in board:
      print("You Won!\n")
      win=True
      break
  if win!=True:
    print("You lose the game!. It was {}.".format(word))

hangman()
