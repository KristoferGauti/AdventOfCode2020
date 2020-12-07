"""
    You board the plane and the plane is completely full, so your seat is going to be easily found
    There is a catch which is that some of the seats at the very front and back do not exist. Those
    seats will be missing from your list of seats. Your seat was not in the very front and back though
    the seats with ids +1 and -1 from yours will be on your list
    What is the ID of your seat?
"""
import os
from solution_part1 import *

SEAT_QUANTITY = 2**10
SEAT_NOT_TAKEN = "O"
SEAT_TAKEN = "X"
AVAILABLE_SEATS = [SEAT_NOT_TAKEN for _ in range(SEAT_QUANTITY - 1)]

def board_the_plane(seat_instructions):
    for instruction in seat_instructions:
        binary_seat_number = instruction.replace("F","0").replace("B", "1").replace("R", "1").replace("L","0")
        decimal_seat_number = int(binary_seat_number, 2)
        AVAILABLE_SEATS[decimal_seat_number] = SEAT_TAKEN

def find_your_seat():
    for seatID, i in enumerate(AVAILABLE_SEATS):
        if 69 < seatID < 861: #your seat is not at the very front or back
            if i == SEAT_NOT_TAKEN:
                print(seatID) #The last number in this sequence is your seatID

def main():
    filename = os.path.join("December5th", "input.txt")
    file_obj = open(filename, "r")
    board_the_plane(file_obj.readlines())
    find_your_seat()

if __name__ == "__main__":
    main()