from typing import NamedTuple, Dict, List
from collections import defaultdict
import pprint

with open("input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

class Bag(NamedTuple):
    color: str
    contains: Dict[str, int]

def get_bag(line: str) -> Bag:
    line = line.strip().replace("bags", "").replace("contain", "").replace(",", "").replace("bag", "").split(" ")
    line = [x for x in line if x != ""]
    color = str(line[0] + " " + line[1])
    if "no" in line:
        contains = {}
    else:
        contains = {}
        for i in range(2, len(line)-2, 3):
            quantity = int(line[i])
            subbag_color = str(line[i+1] + " " + line[i+2])
            contains[subbag_color] = quantity
    return Bag(color, contains)

def make_bags(data: List[str]) -> List[Bag]:
    return [get_bag(line) for line in data]

def parents(bags: List[Bag]) -> Dict[str, List[str]]:
    parents = defaultdict(list)
    for bag in bags:
        for child in bag.contains:
            parents[child].append(bag.color)
    return parents

def count_paths(bags: List[Bag], color: str) -> List[str]:
    parents_map = parents(bags)
    stack = [color]
    paths = set()
    while stack:
        child = stack.pop()
        for parent in parents_map.get(child, []):
            if parent not in paths:
                paths.add(parent)
                stack.append(parent)
    return list(paths)

def bags_inside(bags: List[Bag], color: str) -> int:
    bags_by_color = {bag.color: bag for bag in bags}
    n_bags = 0
    stack: List[Tuple[str, int]] = [(color, 1)]
    while stack:
        color, multiplier = stack.pop()
        bag = bags_by_color[color]
        for child, quantity in bag.contains.items():
            n_bags += multiplier * quantity
            stack.append((child, quantity * multiplier))
    return n_bags

bags = make_bags(data)
#pprint.pprint(bags)
#print(len(count_paths(bags, "shiny gold")))
print(bags_inside(bags, "shiny gold"))


        