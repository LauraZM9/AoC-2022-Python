def read_data(file):
  with open(file) as f:
    cals = f.readlines()
  return cals


def clean_data(cals):
  return list(map(str.strip, cals))