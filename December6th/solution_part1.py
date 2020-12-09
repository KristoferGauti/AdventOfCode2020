"""
    You need to switch planes when you land at your destination. The other plane is 
    much larger which means that custom declaration forms are distributed to the passengers.
    The form asks a series of 26 yes or no questions marked a - z. In the input.txt are all of 
    the answers - yes which were answered by all of the passengers. for example a b c x a b c y a b c z.
    In that example, 6 questions were answered as yes (a, b, c, x, y, z). Count the number of yes answers
    in each paragraph (do not count the duplicate letters). What is the sum of these counts?
"""
import os

def _remove_duplicate_letters(group_answers_lists):
    for i in range(len(group_answers_lists)):
        group_answers_lists[i] = {letter for answers in group_answers_lists[i] for letter in answers}

def clean_data(data):
    group_question_list = []
    line_list = []
    for line in data:
        answers = line.strip().split("\n")
        if answers == [""]:
            group_question_list.append(line_list)
            line_list = []
        else:
            line_list.extend(answers)
    group_question_list.append(line_list)
        
    #remove duplicate letters
    _remove_duplicate_letters(group_question_list)
    return group_question_list
      
def count_yes_answers(answers_list):
    answers_quantity = 0
    for answers in answers_list:
        answers_quantity += len(answers)
    print(answers_quantity)

def main():
    filename = os.path.join("December6th", "input.txt")
    file_obj = open(filename, "r")
    unique_answers_list = clean_data(file_obj.readlines())
    count_yes_answers(unique_answers_list)

if __name__ == "__main__":
    main()