"""In this part you will need to find all the trees that were bumped if 
the character goes with these coordinates: 
1 to the right and 1 down, 3 to the right and 1 down, 5 to the right and 1 down,
7 to the right and 1 down, 1 to the right and 2 down,"""

import os
from solution_part1 import *

def main():
    filename = os.path.join("December3rd", "input.txt")
    file_object = open(filename, "r")
    the_path_list = get_paths_to_1D_list(file_object)
    expand_the_paths(the_path_list)
    
    coords = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    answer = 1
    for coord in coords:
        answer *= count_trees_when_traversing(the_path_list, coord[0], coord[1])

    print(answer)

if __name__ == "__main__":
    main()