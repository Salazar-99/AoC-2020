from typing import List
import itertools

INPUT_FILE = "input.txt"

def read_file(filename: str) -> List[int]:
    """
    Read the contents of 'filename' into a list and return it.
    By default, files are read as strings so each element must be converted
    to an integer for processing.
    """
    file = open(filename, 'r')
    data_strings = file.read().split("\n")
    data_ints = [int(x) for x in data_strings]
    return data_ints

def main_1(data: List[int]) -> int:
    """
    Return the product of the two elements of the list that sum to 2020. 
    """
    diffs = {2020 - i for i in data}
    for value in data:
        if value in diffs:
            return value * (2020 - value)

def main_2(data: List[int]) -> int:
    """
    Return the product of the three elements of the list that sum to 2020.
    """
    diffs = {(2020-i-j) : (i,j) for (i,j) in itertools.product(data, data)}
    for value in data:
        if value in diffs:
            return value * diffs[value][0] * diffs[value][1]


if __name__ == "__main__":
    data = read_file(INPUT_FILE)
    result = main_2(data)
    print(result)