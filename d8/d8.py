from typing import NamedTuple, List
import pprint

with open("input.txt") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

class Instruction(NamedTuple):
    type: str
    value: int

def parse_line(line: str) -> Instruction:
    line = line.split(" ")
    return Instruction(type=line[0], value=int(line[1]))

def run_program(instructions: List[Instruction]) -> int:
    accumulator = 0
    visited = set()
    index = 0
    while index not in visited:
        visited.add(index)
        instruction = instructions[index]
        if instruction.type == 'nop':
            index += 1
        elif instruction.type == 'acc':
            accumulator += instruction.value
            index += 1
        elif instruction.type == 'jmp':
            index += instruction.value
    return accumulator

instructions = [parse_line(line) for line in data]
#pprint.pprint(instructions)
print(run_program(instructions))
