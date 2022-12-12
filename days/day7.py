""" Day 7: No Space Left On Device """

from utils.utils import *


class TreeNode:
  def __init__(self, value, type, size=None):
    print("Initializing...")
    self.value = value
    self.children = []
    self.type = type
    self.size = size

  def add_child(self, child_node):
    print("Adding child node: " + child_node.value)
    if child_node not in self.children:
      self.children.append(child_node)

  def remove_node(self, child_node):
    print("Removing node: " + child_node.value)
    new_children = []
    for child in self.children:
      if child != child_node:
        new_children.append(child)
    self.children = new_children

  def traverse(self):
    print("Traverse tree...")
    all_nodes = []
    node_to_visit = [self]
    while len(node_to_visit) > 0:
      current_node = node_to_visit.pop()
      # print(current_node.value)
      all_nodes.append(current_node.value)
      node_to_visit += current_node.children
    return all_nodes


def main(cmd=None):
  if not cmd:
    cmd = read_data('input/input_day7.txt')
  cmd = clean_data(cmd)
  cme = [
    "$ cd /\n",
    "$ ls\n",
    "dir a\n",
    "14848514 b.txt\n",
    "8504156 c.dat\n",
    "dir d\n",
    "$ cd a\n",
    "$ ls\n",
    "dir e\n",
    "29116 f\n",
    "2557 g\n",
    "62596 h.lst\n",
    "$ cd e\n",
    "$ ls\n",
    "584 i\n",
    "$ cd ..\n",
    "$ cd ..\n",
    "$ cd d\n",
    "$ ls\n",
    "4060174 j\n",
    "8033020 d.log\n",
    "5626152 d.ext\n",
    "7214296 k\n"
    ]

  cme = clean_data(cme)
  tree = populate_tree(cme)
  printTree(tree)

  return None

def populate_tree(cmd):
  root = TreeNode("/", "dir")
  current_dir = root
  all_nodes = [root]
  for line in cmd:
    line = line.split(" ")
    print(line)
    print("current", current_dir.value)

    # when it's a command
    if line[0] == "$":

      # when ls to see the content
      if line[1] == 'ls':
        continue

      # when cd in a dir
      if line[1] == 'cd':
        if current_dir.value == line[2]:
          continue

        if line[2] == '..':
          parent_dir_value = get_parent_dir(root, current_dir)
          print("aici", parent_dir_value)
          current_dir = get_obj_by_value(all_nodes, parent_dir_value)
          print("current dir obj?", current_dir)

        else:
          values = []
          for node in all_nodes:
            values.append(node.value)

          if line[2] in values:
            current_dir = get_obj_by_value(all_nodes, line[2])

          else:
            new_dir = TreeNode(line[2], "dir")
            all_nodes.append(new_dir)
            current_dir.add_child(new_dir)
            current_dir = new_dir


    # when it's an output
    else:

      # when it's a file
      if line[0].isnumeric():
        new_file = TreeNode(line[1], "file", line[0])
        all_nodes.append(new_file)
        current_dir.add_child(new_file)
      
      # when it's a directory
      if line[0] == 'dir':
        new_dir = TreeNode(line[1], "dir")
        all_nodes.append(new_dir)
        current_dir.add_child(new_dir)

  return root


def get_parent_dir(root, curr):
  node_to_visit = [root]
  while len(node_to_visit) > 0:
    current_node = node_to_visit.pop()
    if curr in current_node.children:
      return current_node.value
    node_to_visit += current_node.children


def printTree(root, markerStr="+- ", levelMarkers=[]):
    emptyStr = " "*len(markerStr)
    connectionStr = "|" + emptyStr[:-1]
    level = len(levelMarkers)
    mapper = lambda draw: connectionStr if draw else emptyStr
    markers = "".join(map(mapper, levelMarkers[:-1]))
    markers += markerStr if level > 0 else ""
    print(f"{markers}{root.value}")
    for i, child in enumerate(root.children):
        isLast = i == len(root.children) - 1
        printTree(child, markerStr, [*levelMarkers, not isLast])


def get_obj_by_value(all_nodes, value):
  print("here are all the nodes", len(all_nodes))
  for node in all_nodes:
    print(node.value, value)
    if node.value == value:
      return node


if __name__ == "__main__":
  main()