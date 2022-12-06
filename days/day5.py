""" Day 5: Supply Stacks """

from utils.utils import *
import re


def main(structure=None):
  if not structure:
    structure = read_data('input/input_day5.txt')
    
  board_structure, moves = split_board_and_moves(structure)

  # board_dict = convert_to_dict(board_structure)
  board_dict = {
    1: ["[N]","[C]","[R]","[T]","[M]","[Z]","[P]"],
    2: ["[D]","[N]","[T]","[S]","[B]","[Z]"],
    3: ["[M]","[H]","[Q]","[R]","[F]","[C]","[T]","[G]"],
    4: ["[G]","[R]","[Z]"],
    5: ["[Z]","[N]","[R]","[H]"],
    6: ["[F]","[H]","[S]","[W]","[P]","[Z]","[L]","[D]"],
    7: ["[W]","[D]","[Z]","[R]","[C]","[G]","[M]"],
    8: ["[S]","[J]","[F]","[L]","[H]","[W]","[Z]","[Q]"],
    9: ["[S]","[Q]","[P]","[W]","[N]"]
  }
  # board_dict = {
  #   1: ['[Z]', '[N]'],
  #   2: ['[M]', '[C]', '[D]'],
  #   3: ['[P]'] 
  # }

  # Part 1
  # top_crates = get_part_one_result(board_dict, moves)
  # print("First part result board", top_crates)

  # Part 2
  board = get_part_two_result(board_dict, moves)
  print("Second part result board", board)

  return None
  

def get_part_one_result(board_dict, moves):
  for move in moves:
    numbers = extract_numbers(move)
    apply_move(board_dict, numbers)

  top_crates = []
  for value in board_dict.values():
    top_crates.append(value[-1])
  return top_crates


def get_part_two_result(board_dict, moves):
  for move in moves:
    num = extract_numbers(move)
    apply_move_multiple(board_dict, num)
  return board_dict


def split_board_and_moves(structure):
  for line in structure:
      if line == '\n':
        board_structure = structure[:structure.index(line)]
        moves = clean_data(structure[structure.index(line) + 1:])
  return board_structure, moves


def extract_numbers(instruction):
  return re.findall(r'\d+', instruction)


def convert_to_dict(board_structure):
  board_dict = {}
  columns = extract_numbers(board_structure[-1])
  for line in board_structure[:-1]:
    li = []
    for column in columns:
      if line[board_structure[-1].index(column)].strip():
        li.append(line[board_structure[-1].index(column)].strip())
    board_dict[column] = li
  return board_dict
  

def apply_move(board_dict, move):
  move = [int(i) for i in move]
  for _ in range(move[0]):
    to_move = board_dict[move[1]].pop()
    board_dict[move[2]].append(to_move)
  return board_dict


def apply_move_multiple(board_dict, move):
  move = [int(i) for i in move]
  initial_list = board_dict[move[1]]
  to_move = []
  for _ in range(move[0]):
    to_move.append(initial_list.pop())
  to_move.reverse()
  board_dict[move[2]] += to_move
  return board_dict


if __name__ == "__main__":
  main()