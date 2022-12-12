from days.day7 import *

INPUT = [
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

def test_main():
  assert main(INPUT) == None

def test_populated_dict():
  output_dict = {
    "/" : {
      "type": "dir",
      "a": {
        "type": "dir",
        "e":{
          "type": "dir",
          "i":{
            "type": "file",
            "size": 584
          }
        },
        "f":{
          "type": "file",
          "size": 29116
        },
        "g":{
          "type": "file", 
          "size": 2557
        },
        "h.lst":{
          "type": "file",
          "size": 62596
        }
      },
      "b.txt":{
        "type": "file",
        "size": 14848514
      },
      "c.dat":{
        "type": "file",
        "size": 8504156
      },
      "d":{
        "type": "dir",
        "j": {
          "type": "file",
          "size": 4060174
        },
        "d.log":{
          "type": "file",
          "size": 8033020
        },
        "d.ext":{
          "type": "file",
          "size": 5626152
        },
        "k":{
          "type": "file",
          "size": 7214296
        }
      }
    }
  }
  assert populate_dict() == output_dict

def test_find_parent():
  assert find_parent()