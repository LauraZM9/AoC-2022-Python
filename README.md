# Advent of Code 2022 in Python

[Advent of Code](https://adventofcode.com/)

To run the files:
```
python days/day1.py
```

To run the tests:
```
python -m pytest tests/day1_test.py
```

## Troubleshooting

When getting error for relative imports like:

`ModuleNotFoundError or ImportNotFound`

Use this article [How to Fix ModuleNotFoundError and ImportError](https://medium.com/towards-data-science/how-to-fix-modulenotfounderror-and-importerror-248ce5b69b1c)

Specifically:
```
export PYTHONPATH="${PYTHONPATH}:/Users/laura.zaharia/Personal/AoC-2022-Python"
```

Some useful references:
- [How to implement a sliding window](https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7) -> adapted for day 6 solution