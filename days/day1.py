""" Day 1: Calorie Counting """

def main(cals=None):
  if not cals:
    cals = read_data()
  cals = clean_data(cals)

  total_cals = split_calories(cals)
  max_cals = max(total_cals)
  print("The maximum of calories from a reeinder: ", max_cals)

  top_3 = get_top_three(total_cals)
  print("Sum of the top three reendeer calories: ", sum(top_3))

  return max_cals, top_3


def read_data():
  with open('input/input_day1.txt') as f:
    cals = f.readlines()
  return cals


def clean_data(cals):
  return list(map(str.strip, cals))


def split_calories(cals):
  total_cals = []
  sum = 0

  for cal in cals:
    try: 
      sum += int(cal)
    except:
      total_cals.append(sum)
      sum = 0

  return total_cals


def get_top_three(total_cals):
  return sorted(total_cals, reverse=True)[:3]


if __name__ == "__main__":
    main()
    