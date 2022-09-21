[![Python](https://img.shields.io/badge/Python-%33.6-blue.svg)](https://www.python.org/downloads/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Prerequisites

* Python 3.6.15

## Usage

This script iterates a list of up to 10,000 integers
to find all pairs with the given sum in it.

If you want to process more, it is possible to overload the ram memory.

run ```python main.py --help``` for more info.

### example

```python main.py --target 12 --numbers 1 9 5 0 20 -4 12 16 7```

This exetution should be return ```{(5, 7), (0, 12), (-4, 16)}```