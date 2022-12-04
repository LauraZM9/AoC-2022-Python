""" Day 4: Camp Cleanup """

from utils.utils import *

def main(section_pairs=None):
  if not section_pairs:
    section_pairs = read_data('input/input_day4.txt')
  section_pairs = clean_data(section_pairs)

  # part 1
  number_of_fully_contained_sections = get_fully_contained_sections(section_pairs)
  print("This is how many sections are fully contained:", number_of_fully_contained_sections)

  # part 2
  print(get_no_overlapping_sections(section_pairs))
  return number_of_fully_contained_sections


def get_fully_contained_sections(section_pairs):
  count = 0
  for section in section_pairs:
    p1, p2 = section.split(",")
    p1_lower, p1_upper = get_ends(p1)
    p2_lower, p2_upper = get_ends(p2)
    if (p1_lower <= p2_lower) and (p2_upper <= p1_upper):
      count += 1
    elif (p2_lower <= p1_lower) and (p1_upper <= p2_upper):
      count += 1
  return count
      

def get_ends(interval):
    interval = interval.split("-")
    return int(interval[0]), int(interval[1])


def get_no_overlapping_sections(section_pairs):
  count = 0
  for section in section_pairs:
    p1, p2 = section.split(",")
    p1_lower, p1_upper = get_ends(p1)
    p2_lower, p2_upper = get_ends(p2)
    p1_range = range(p1_lower, p1_upper+1)
    p2_range = range(p2_lower, p2_upper+1)
    intersection = [i for i in p1_range if i in p2_range]
    print(intersection)
    if intersection:
      count += 1
  return count


if __name__ == "__main__":
  main()