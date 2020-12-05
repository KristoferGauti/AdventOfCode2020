"""
    For a given grid in input.txt start on the top leftmost dot (.) and traverse 
    3 right and 1 down. If you stop at an tree (#) count the tree.
    Count how many trees you encounter by traversing the map all 
    the way to the right bottommost row. the pattern in every row can repeat itself many times
"""
import os

def get_paths_to_1D_list(a_list):
    """
        Gets all the paths and puts it into
        a 1 dimentional list
    """
    the_path_list = []
    for path in a_list:
        the_path_list.append(path.strip())

    return the_path_list

def expand_the_paths(a_list):
    """The pattern in each row can repeat itself many times"""
    for i in range(len(a_list)):
        a_list[i] = a_list[i] * 10000
    
def count_trees_when_traversing(the_path_list, right, down):
    """
        counts the trees (#) by traversing all the map to 
        the bottom (the while loops brakes if the index is out of bounds)
    """

    x, y = 0, 0
    tree_counter = 0

    while right <= (len(the_path_list) - 1):
        x += right
        y += down
        try:
            if the_path_list[y][x] == "#":
                tree_counter += 1
        except IndexError:
            break

    return tree_counter

def main():
    filename = os.path.join("December3rd", "input.txt")
    file_object = open(filename, "r")
    the_path_list = get_paths_to_1D_list(file_object)
    expand_the_paths(the_path_list)
    answer = count_trees_when_traversing(the_path_list, 3, 1)
    print(answer)
    

if __name__ == "__main__":
    main()