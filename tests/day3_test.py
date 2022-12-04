from days.day3 import *

def test_main():
  input = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg",
  "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
  "ttgJtRGJQctTZtZT",
  "CrZsJsPPZsGzwwsLwLmpwMDw"]
  assert main(input) == 157

def test_get_compartment_content_first():
  input = "vJrwpWtwJgWrhcsFMMfFFhFp"
  output = "vJrwpWtwJgWr", "hcsFMMfFFhFp"
  assert get_compartment_content(input) == output

def test_get_compartment_content_second():
  input = "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL"
  output = "jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL"
  assert get_compartment_content(input) == output

def test_get_compartment_content_second():
  input = "PmmdzqPrVvPwwTWBwg"
  output = "PmmdzqPrV", "vPwwTWBwg"
  assert get_compartment_content(input) == output

def test_get_similarities_first():
  input = "vJrwpWtwJgWr", "hcsFMMfFFhFp"
  output = "p"
  assert get_similarities(input) == output

def test_get_priority_score():
  assert get_priority_score("p") == 16
  assert get_priority_score("L") == 38

def test_get_badge_code():
  input = [
  "vJrwpWtwJgWrhcsFMMfFFhFp",
  "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
  "PmmdzqPrVvPwwTWBwg"
  ]
  output = "r"
  assert get_badge_code(input) == output