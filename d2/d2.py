from typing import Tuple, List
import re

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    data = f.readlines()
    data = [line.strip("\n") for line in data]

def parse_password_reqs(password_reqs: str) -> Tuple[int, int, str, str]:
    parts = password_reqs.split(" ")
    bounds = parts[0].split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])
    letter = list(parts[1])[0]
    password = parts[2]
    return lower, upper, letter, password

def validate_password(lower, upper, letter, password: str) -> bool:
    counter = 0
    for char in password:
        if char == letter:
            counter += 1
        if counter > upper:
            return False
    if counter < lower:
        return False
    return True

def validate_password_2(lower, upper, letter, password: str) -> bool:
    if (password[lower-1] == letter) ^ (password[upper-1] == letter):
        return True
    return False

def count_valid_passwords(data: List[str]) -> int:
    counter = 0
    for password_reqs in data:
        lower, upper, letter, password = parse_password_reqs(password_reqs)
        counter += validate_password(lower, upper, letter, password)
    return counter

def count_valid_passwords_2(data: List[str]) -> int:
    counter = 0
    for password_reqs in data:
        lower, upper, letter, password = parse_password_reqs(password_reqs)
        counter += validate_password_2(lower, upper, letter, password)
    return counter

print(count_valid_passwords_2(data))