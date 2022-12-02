""" Day 2: Rock Paper Scissors """

from utils.utils import *

def main(game=None):
  if not game:
    game = read_data('input/input_day2.txt')
  game = clean_data(game)

  # when second column is my move
  total_score = 0
  for round in game:
    total_score += move_score(round) + game_score(round)
  print("Total score when second column is my move: ", total_score)

  # when second column is the output of the game
  total_score_v2 = 0
  for round in game:
    total_score_v2 += game_score_v2(round)
  print("The score when the second column is the output of the game: ", total_score_v2)
  
  return total_score, total_score_v2


# measure the score for your move
def move_score(round):
  my_move = round[-1]
  score = 0

  if my_move == 'X':
    score = 1
  elif my_move == 'Y':
    score = 2
  else:
    score = 3

  return score


# measure the score for the game
def game_score(round):
  loses = ['B X', 'C Y', 'A Z']
  draw = ['A X', 'B Y', 'C Z']
  wins = ['C X', 'A Y', 'B Z']

  score = 0
  if round in loses:
    score = 0
  elif round in draw:
    score = 3
  elif round in wins:
    score = 6

  return score


# column two is the game score
def game_score_v2(round):
  loses = ['B X', 'C Y', 'A Z']
  draw = ['A X', 'B Y', 'C Z']
  wins = ['C X', 'A Y', 'B Z']

  output = round[-1]
  if output == 'X':
    for element in loses:
      if element[0] == round[0]:
        score = move_score(element[-1])
  elif output == 'Y':
    for element in draw:
      if element[0] == round[0]:
        score = move_score(element[-1]) + 3
  elif output == 'Z':
    for element in wins:
      if element[0] == round[0]:
        score = move_score(element[-1]) + 6
  return score


if __name__ == "__main__":
  main()