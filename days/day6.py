""" Day 6: Tuning Trouble """

from utils.utils import *

def main(signal=None):
  if not signal:
    signal = read_data('input/input_day6.txt')
  signal = clean_data(signal)[0]

  # Part 1
  subroutine = get_subroutine(signal, 4)
  print(subroutine)

  # Part 2
  subroutine_p2 = get_subroutine(signal, 14)
  print(subroutine_p2)
  
  return subroutine, subroutine_p2
  
def get_subroutine(signal, marker_length):
  left_window = 0

  # to store counts of characters; constant time
  counts = {}

  for right_window in range(len(signal)):
    if not signal[right_window] in counts.keys():
      counts[signal[right_window]] = 1

    counts[signal[right_window]] += 1

    for value in counts.values():
      if value > 1:
        counts[signal[right_window]] -= 1
        right_window += 1

    right_window += 1
    if right_window > marker_length - 1:
      if are_all_letters_different(signal[left_window:right_window]):
          break
      left_window += 1

  return right_window


def are_all_letters_different(four_letter_word):
  return len(set(four_letter_word)) == len(four_letter_word)

if __name__ == "__main__":
  main()