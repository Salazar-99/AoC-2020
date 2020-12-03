from typing import List

INPUT_FILE = "input.txt"
TREE = "#"
OPEN = "."

with open(INPUT_FILE) as f:
    data = f.readlines()
    data = [line.strip("\n") for line in data]

def traverse_path(data: List[str], slope_x: int, slope_y:int) -> int:
    counter = 0
    N = len(data[0])
    row = 0
    i = 0
    while row < len(data):
        index = (slope_x*i) % N
        if data[row][index] == "#":
            counter += 1
        row += slope_y
        i += 1
    return counter

x_slopes = [1,3,5,7,1]
y_slopes = [1,1,1,1,2]

product = 1
for x_slope, y_slope in zip(x_slopes, y_slopes):
    product *= traverse_path(data, x_slope, y_slope)

print(product)