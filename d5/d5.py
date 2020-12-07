from typing import List, NamedTuple

INPUT_FILE = "input.txt"

with open(INPUT_FILE) as f:
    data = f.readlines()
    data = [line.strip() for line in data]

class Seat(NamedTuple):
    row: int
    col: int

    @property
    def seat_id(self) -> int:
        return (self.row * 8) + self.col

def get_seat(boarding_pass: str) -> Seat:
    row_data = boarding_pass[:-3]
    column_data = boarding_pass[7:]
    row_bottom = 0
    row_top = 127
    for letter in row_data:
        if letter == "F":
            row_top -= (row_top - row_bottom) // 2 + 1
        elif letter == "B":
            row_bottom += (row_top - row_bottom) // 2 + 1
    col_bottom = 0
    col_top = 7
    for letter in column_data:
        if letter == "R":
            col_bottom += (col_top - col_bottom) // 2 + 1
        elif letter == "L":
            col_top -= (col_top - col_bottom) // 2 + 1
    return Seat(row=row_bottom, col=col_bottom)

def find_max_id(seats: List[Seat]) -> int:
    max_id = 0
    for seat in seats:
        if seat.seat_id > max_id:
            max_id = seat.seat_id
    return max_id

seats = [get_seat(boarding_pass) for boarding_pass in data]
print(find_max_id(seats))
 
seat_ids = sorted([seat.seat_id for seat in seats])
for i in range(len(seat_ids)-1):
    if seat_ids[i+1] - seat_ids[i] > 1:
        print(seat_ids[i] + 1)