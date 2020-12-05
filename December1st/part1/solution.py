"""
    We have an expense report (input.txt) Find two entries 
    that sum up to 2020 and then multiply those two numbers together
"""
import os

def brute_force_solution(expense_report):
    """
        Time complexity ~n^2/2 or O(n^2) because we have 2 independent for loops
        That means to take the sum_{i=0}^{n} (i^2) = n^2/2 where n is 
        the length of the list
    """
    for i in range(0, len(expense_report)):
        for j in range(1, len(expense_report)):
            if (expense_report[i] + expense_report[j] == 2020):
                return (expense_report[i] * expense_report[j])

def main():
    file_path = os.path.join("December1st", "input.txt")
    file_object = open(file_path, "r")
    int_stream = lambda x : map(int, x)
    answer = brute_force_solution(list(int_stream(file_object)))
    print(answer)

if __name__ == "__main__":
    main()

