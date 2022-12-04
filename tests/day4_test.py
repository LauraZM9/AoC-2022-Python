from days.day4 import *

INPUT = [
  "2-4,6-8",
  "2-3,4-5",
  "5-7,7-9",
  "2-8,3-7",
  "6-6,4-6",
  "2-6,4-8"
  ]

def test_main():
  assert main(INPUT) == 2

def test_get_fully_contained_section():
  assert get_fully_contained_sections(INPUT) == 2
# 2-8 fully contains 3-7
# 6-6 is fully contained by 4-6

def test_get_ends():
  input = "2-4,6-8"
  i1, i2 = input.split(",")
  assert get_ends(i1) == (2,4)
  assert get_ends(i2) == (6,8)

def test_get_no_overlapping_pais():
  assert get_no_overlapping_sections(INPUT) == 4