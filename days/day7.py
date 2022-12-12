""" Day 7: No Space Left On Device """

from utils.utils import *

def main(cmd=None):
  if not cmd:
    cmd = read_data('input/input_day7.txt')
  cmd = clean_data(cmd)
  print(cmd)
  return None

def populate_dict(cmd):
  dir_structure = {}
  current_dir = "/"
  nested_levels = []
  for line in cmd:
    line = line.split(" ")

# if it's cd -> get current dir and add to structure if not there yet
    if line[0] == "$" and line[1] == 'cd':
      if not line[2] in recursive_items(cmd):
        cmd[current_dir]
      current_dir = line[2]
    elif line[0] == "$" and line[1] == 'ls':
      continue

    else:
      if line[0] == "dir":
        dir_structure[current_dir] = line[1]
        dir_structure[current_dir][line[1]]["type"] = "dir"


def recursive_items(dictionary):
  keys = []
  for key, value in dictionary.items():
      if type(value) is dict:
          yield from recursive_items(value)
      else:
          keys.append(key)
  return keys

def get_directory():
  pass

if __name__ == "__main__":
  main()