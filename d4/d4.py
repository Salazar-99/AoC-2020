from typing import List, Dict 
 
INPUT_FILE = "input.txt"
REQUIRED_FIELDS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

with open(INPUT_FILE) as f:
    data = f.read()

Passport = Dict[str, str]

def make_passport(data: str) -> Passport:
    lines = data.strip().split("\n")
    lines = [line.strip() for line in lines if line.strip()]

    passport = {}

    for line in lines:
        for chunk in line.split(" "):
            field, value = chunk.split(":")
            passport[field] = value
    
    return passport

def extract_passports(data: str) -> List[Passport]:
    chunks = data.split("\n\n")
    return [make_passport(chunk) for chunk in chunks if chunk.strip()]

def validate_passport(passport: Passport, required_fields: List[str] = REQUIRED_FIELDS) -> bool:
    return all(field in passport for field in required_fields)

PASSPORTS = extract_passports(data)

print(sum(validate_passport(passport) for passport in PASSPORTS))