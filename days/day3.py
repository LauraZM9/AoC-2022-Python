""" Day 3: Rucksack Reorganization """

from utils.utils import *

def main(items=None):
  if not items:
    items = read_data('input/input_day3.txt')
  items = clean_data(items)

  # part 1
  sum = 0
  for item in items:
    compartments = get_compartment_content(item)
    content = get_similarities(compartments)
    sum += get_priority_score(content)
  print("This is the sum of the misplaced items: ", sum)

  # part 2
  sum_badge_score = 0
  elves = [items[i:i+3] for i in range(0, len(items), 3)]
  for group in elves:
    badge = get_badge_code(group)
    sum_badge_score += get_priority_score(badge)
  print("This is the sum of all the badges' score: ", sum_badge_score)
  return sum, sum_badge_score


def get_compartment_content(rucksack_items):
  half = int(len(rucksack_items)/2)
  return rucksack_items[:half], rucksack_items[half:]


def get_similarities(compartments):
  return ''.join(set(compartments[0]).intersection(compartments[1]))


def get_priority_score(element):
  if element.isupper():
    score = ord(element) - ord("A") + 27
  else:
    score = ord(element) - ord("a") + 1
  return score 


def get_badge_code(group):
  common = get_similarities((group[0], group[1]))
  return get_similarities((common, group[2]))

if __name__ == "__main__":
  main()