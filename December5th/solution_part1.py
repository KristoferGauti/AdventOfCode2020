"""
    You get on the plain and realised that you have lost your boarding pass.
    You have decided to write a program to scan the airplane for your boarding pass,
    because you cannot rememeber where your seat is located on the airplane. 
    The airplane uses binary space partitioning. A seat number might be specified like FBFBBFFRLR whereas
    F = front, B = back, R = right and L = left. The first seven characters will be either F or B. These seven
    characters specify exactly one of 128 rows in the plane. The last three characters represents one of the 8 columns
    For example decoding FBFBBFFRLR reveals the seat that is located at row 44, col 5. 
    Every seat has a unique seatID which you can get by multiplying the row number by 8 and add the column number.
"""
import os

def change_inputs_to_binary(file_stream):
    """
        To change the first 7 letters in 
        the seat instruction we must replace F with 0 and B with 1
        To change the last 3 letters we must replace R with 1 and L with 0
    """
    max_seatID = 0
    for seat_instruction in file_stream:
        seat_nr = seat_instruction.strip()
        binary_seat_number = seat_nr.replace("F","0").replace("B", "1").replace("R", "1").replace("L","0")
        row_nr = int(binary_seat_number[:7], 2)
        col_nr = int(binary_seat_number[7:10], 2)
        seatID = (row_nr << 3) + col_nr

        if seatID > max_seatID:
            max_seatID = seatID

    print(max_seatID)

def main():
    filename = os.path.join("December5th", "input.txt")
    file_obj = open(filename, "r")
    change_inputs_to_binary(file_obj.readlines())

if __name__ == "__main__":
    main()