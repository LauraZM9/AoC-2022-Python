from days.day5 import *

INPUT = [
  '    [D]    \n',
  '[N] [C]    \n',
  '[Z] [M] [P]\n',
  ' 1   2   3 \n',
  '\n',
  'move 1 from 2 to 1\n',
  'move 3 from 1 to 3\n',
  'move 2 from 2 to 1\n',
  'move 1 from 1 to 2\n'
  ]

# def test_main():
  # assert main(INPUT) == (['[C]','[M]','[Z]'],['[M]','[C]','[D]'])
  # assert main(INPUT) == (0,['[M]','[C]','[D]'])  

def test_extract_numbers():
  input = 'move 1 from 2 to 1'
  assert extract_numbers(input) == ["1", "2", "1"]

def test_apply_move():
  board_dict = {
    1: ['[Z]', '[N]'],
    2: ['[M]', '[C]', '[D]'],
    3: ['[P]']
  }
  move = [1, 2, 1]
  output = {
    1: ['[Z]', '[N]', '[D]'],
    2: ['[M]', '[C]', ],
    3: ['[P]']
  }
  assert apply_move(board_dict, move) == output

def test_apply_move_multiple_single_crate():
  board_dict = {
    1: ['[Z]', '[N]'],
    2: ['[M]', '[C]', '[D]'],
    3: ['[P]']
  }
  move = [1, 2, 1]
  output = {
    1: ['[Z]', '[N]', '[D]'],
    2: ['[M]', '[C]'],
    3: ['[P]']
  }
  assert apply_move_multiple(board_dict, move) == output

def test_apply_move_multiple_three_crates():
  board_dict = {
    1: ['[Z]', '[N]', '[D]'],
    2: ['[M]', '[C]'],
    3: ['[P]']
  }
  move = [3, 1, 3]
  output = {
    1: [],
    2: ['[M]', '[C]'],
    3: ['[P]', '[Z]', '[N]', '[D]']
  }
  assert apply_move_multiple(board_dict, move) == output

def test_apply_move_multiple_three_crates():
  board_dict = {
    1: [],
    2: ['[M]', '[C]'],
    3: ['[P]', '[Z]', '[N]', '[D]']
  }
  move = [2, 2, 1]
  output = {
    1: ['[M]', '[C]'],
    2: [],
    3: ['[P]', '[Z]', '[N]', '[D]']
  }
  assert apply_move_multiple(board_dict, move) == output

def test_apply_move_multiple_three_crates():
  board_dict = {
    1: ['[M]', '[C]'],
    2: [],
    3: ['[P]', '[Z]', '[N]', '[D]']
  }
  move = [1, 1, 2]
  output = {
    1: ['[M]'],
    2: ['[C]'],
    3: ['[P]', '[Z]', '[N]', '[D]']
  }
  assert apply_move_multiple(board_dict, move) == output

def test_apply_move_multiple_three_crates():
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
  move = [7, 6, 8]
  output = {
    1: ["[N]","[C]","[R]","[T]","[M]","[Z]","[P]"],
    2: ["[D]","[N]","[T]","[S]","[B]","[Z]"],
    3: ["[M]","[H]","[Q]","[R]","[F]","[C]","[T]","[G]"],
    4: ["[G]","[R]","[Z]"],
    5: ["[Z]","[N]","[R]","[H]"],
    6: ["[F]"],
    7: ["[W]","[D]","[Z]","[R]","[C]","[G]","[M]"],
    8: ["[S]","[J]","[F]","[L]","[H]","[W]","[Z]","[Q]","[H]","[S]","[W]","[P]","[Z]","[L]","[D]"],
    9: ["[S]","[Q]","[P]","[W]","[N]"]
  }
  assert apply_move_multiple(board_dict, move) == output


def test_apply_move_multiple_three_crates():
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
  move = [7, 6, 8]
  output = {
    1: ["[N]","[C]","[R]","[T]","[M]","[Z]","[P]"],
    2: ["[D]","[N]","[T]","[S]","[B]","[Z]"],
    3: ["[M]","[H]","[Q]","[R]","[F]","[C]","[T]","[G]"],
    4: ["[G]","[R]","[Z]"],
    5: ["[Z]","[N]","[R]","[H]"],
    6: ["[F]"],
    7: ["[W]","[D]","[Z]","[R]","[C]","[G]","[M]"],
    8: ["[S]","[J]","[F]","[L]","[H]","[W]","[Z]","[Q]","[H]","[S]","[W]","[P]","[Z]","[L]","[D]"],
    9: ["[S]","[Q]","[P]","[W]","[N]"]
  }
  assert apply_move_multiple(board_dict, move) == output

def test_get_part_two_result():
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
  moves = [
    "move 7 from 6 to 8\n",
    "move 5 from 2 to 6\n",
    "move 2 from 4 to 1\n",
    "move 1 from 4 to 5\n",
    "move 5 from 7 to 6\n",
    "move 7 from 6 to 3\n",
    "move 5 from 9 to 2\n",
    "move 6 from 2 to 3\n",
    "move 2 from 7 to 9\n",
    "move 20 from 3 to 1\n"
  ]
  output = {
    1: ["[N]",
    "[C]","[R]","[T]","[M]",
    "[Z]","[P]","[R]","[Z]",
    "[H]","[Q]","[R]","[F]",
    "[C]","[T]","[G]","[B]",
    "[Z]","[Z]","[R]","[C]",
    "[G]","[M]","[D]","[S]",
    "[Q]","[P]","[W]","[N]"
    ],
    2: [],
    3: ["[M]"],
    4: [],
    5: ["[Z]","[N]","[R]","[H]","[G]"],
    6: ["[F]","[N]","[T]","[S]",],
    7: [],
    8: ["[S]","[J]","[F]","[L]","[H]","[W]","[Z]","[Q]", "[H]","[S]","[W]","[P]","[Z]","[L]","[D]"],
    9: ["[W]","[D]",]
  }
  assert get_part_two_result(board_dict, moves) == output