"""
    You misread the instruction. The instructions were that you needed to identify the questions 
    that everyone answered yes not count every yes answered question. For example, abc in one paragraph 
    counts as 3 whereas every 1 person answered yes to the questions a, b, c. col(a, b, c) here there is no
    question that every 1 person answered yes. col(a, b) col(a, c) here every one answered yes to only 1 question, a.
    For each group (paragraph), count the number of question in which everyone answered yes, and sum up the counts.
"""
import os

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
    return group_question_list

def count_all_yeses(answers):
    counter = 0
    for answer in answers:
        set_answer = map(set, answer)
        intersection = set.intersection(*set_answer)
        counter += len(intersection)
        
    return counter

def main():
    filename = os.path.join("December6th", "input.txt")
    file_obj = open(filename, "r")
    question_answers = clean_data(file_obj.readlines())
    print(count_all_yeses(question_answers))

if __name__ == "__main__":
    main()