from days.day2 import *

def test_main():
  input = ['A Y\n', "B X\n", "C Z\n"]
  output = 15, 12
  assert main(input) == output

def test_move_score():
  assert move_score('A X') == 1
  assert move_score('B Y') == 2
  assert move_score('A Z') == 3

def test_game_score_lose():
  assert game_score('B X') == 0
  assert game_score('C Y') == 0
  assert game_score('A Z') == 0

def test_game_score_draw():
  assert game_score('A X') == 3
  assert game_score('B Y') == 3
  assert game_score('C Z') == 3

def test_game_score_lose():
  assert game_score('C X') == 6
  assert game_score('A Y') == 6
  assert game_score('B Z') == 6

def test_game_score_v2():
  assert game_score_v2('A Y') == 4
  assert game_score_v2('B X') == 1
  assert game_score_v2('C Z') == 7
