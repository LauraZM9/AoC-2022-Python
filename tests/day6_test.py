from days.day6 import *

def test_main():
  input = ["mjqjpqmgbljsphdztnvjfqwrcgsmlb\n"]
  assert main(input) == (7, 19)

sol_dict ={
  "bvwbjplbgvbhsrlpgdmjqwftvncz": 5,
  "nppdvjthqldpwncqszvftbrmjlhg": 6,
  "mjqjpqmgbljsphdztnvjfqwrcgsmlb": 7,
  "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 10,
  "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 11
}

for key,value in sol_dict.items():
  def test_get_subroutine():
    assert get_subroutine(key, 4) == value

def test_are_all_letters_different():
  assert are_all_letters_different('mjqj') == False
  assert are_all_letters_different('abcd') == True

sol_dict_part_2 ={
"mjqjpqmgbljsphdztnvjfqwrcgsmlb": 19,
"bvwbjplbgvbhsrlpgdmjqwftvncz": 23,
"nppdvjthqldpwncqszvftbrmjlhg": 23,
"nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg": 29,
"zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw": 26
}

for key,value in sol_dict_part_2.items():
  def test_get_subroutine():
    assert get_subroutine(key, 14) == value