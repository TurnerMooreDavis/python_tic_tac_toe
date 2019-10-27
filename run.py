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
  while not check_board(board, i):
    print('position already taken, please choose another position')
    i = input()
  update_board(board, 'X', i)

def check_board(board, position):
  return board[position] is None

def ai_turn(board):
  i = random.randint(0,8)
  while not check_board(board, i):
    i = random.randint(0,8)
  update_board(board, 'O', i)

def game_over(board, player):
  if(all(board)):
    return True 
  if(board[0] == player and board[1] == player and board[2] == player):
    return True
  if(board[0] == player and board[3] == player and board[6] == player):
    return True
  if(board[0] == player and board[4] == player and board[8] == player):
    return True
  if(board[1] == player and board[4] == player and board[7] == player):
    return True
  if(board[2] == player and board[4] == player and board[6] == player):
    return True
  if(board[2] == player and board[5] == player and board[8] == player):
    return True
  if(board[3] == player and board[4] == player and board[5] == player):
    return True
  if(board[6] == player and board[7] == player and board[8] == player):
    return True
  return False

def play(board):
  turns = 0
  print('hello world, lets play tic tac toe')
  print_board(board)
  print('enter a coordinate to make a move')
  is_game_over = False
  while(not is_game_over):
    if(turns % 2 == 0):
      player_turn(board)
      is_game_over = game_over(board, "X")
    else:
      ai_turn(board)
      is_game_over = game_over(board, "O")
    turns += 1
  print('game over')

play(new_board)