import random
new_board= [None] * 9
# print('...\n...\n...')
# i1 = input()
# print(i1)


def print_board(board):
  print('\n')
  print_string = ""
  for i, character in enumerate(board):
    if i == 3 or i == 6:
      print_string += '\n'
    if character is None: 
      print_string += '. '
    else:
      print_string += character + ' ' 
  print(print_string)

def update_board(board, player, position):
  board[position] = player
  print_board(board)

def player_turn(board):
  i = input()
  update_board(board, 'X', i)

def ai_turn(board):
  i = random.randint(0,8)
  while board[i] is not None:
    i = random.randint(0,8)
  update_board(board, 'O', i)

def play(board):
  turns = 0
  print('hello world, lets play tic tac toe')
  print_board(board)
  print('enter a coordinate to make a move')
  while(not all(board)):
    if(turns % 2 == 0):
      player_turn(board)
    else:
      ai_turn(board)
    turns += 1
  print('game over')

play(new_board)