# Advent of Code 2021

<https://adventofcode.com/2021>

My solutions for puzzles from AoC 2021.

The code was written with Python 3.10, so this is the recommended
version to run it, even though most of it will be compatible with Python
3.7+, especially after adding `from __future__ import annotations` to
the top of each file.

Each file should be run from the repository root:

    python dayXX/partX.py

`partX.py` files include tests compatible with pytest. Pytest and other
packages required to run the code can be installed with pip (setting up
a virtual environment is advised):

    python -m pip install -r requirements.txt

Because of the file naming, pytest was configured, so the tests are
automatically detected in these files.

For a very slow test cases (due to the code that is not the most
efficient in the world), there is a special marker, and you can deselect
these tests with the following command:

    pytest -m "not slow"

It's also possible to run only the tests from a given day:

    pytest dayXX

or a given puzzle part:

    pytest dayXX/partX.py
