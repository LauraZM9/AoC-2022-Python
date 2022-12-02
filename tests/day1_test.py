from days.day1 import *


def test_main():
  input = ["1000\n", "2000\n", "3000\n", "\n", "4000\n", "\n", "5000\n", "6000\n", "\n", "7000\n", "8000\n", "9000\n", "\n", "10000\n"]
  output = 24000, [24000, 11000, 6000]
  assert main(input) == output

def test_clean_data():
  input = ["1000\n", "2000\n", "3000\n", "\n", "4000\n", "\n", "5000\n", "6000\n", "\n", "7000\n", "8000\n", "9000\n", "\n", "10000\n"]
  output = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
  assert clean_data(input) == output

def test_split_calories():
  input = ["1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "", "10000"]
  output = [6000, 4000, 11000, 24000]
  assert split_calories(input) == output

def test_get_top_three():
  input = [6000, 4000, 11000, 24000]
  assert get_top_three(input) == [24000, 11000, 6000]
