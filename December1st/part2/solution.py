"""
    We have an expense report (input.txt) Find two entries 
    that sum up to 2020 and then multiply those two numbers together
"""
import os

def brute_force_solution(expense_report):
    """
        Time complexity ~n^3/3 or O(n^3) because we have 3 independent for loops
        That means to take the sum_{i=0}^{n} (i^3) = n^3/3 where n is 
        the length of the list
    """
    for i in range(0, len(expense_report)):
        for j in range(1, len(expense_report)):
            for k in range(2, len(expense_report)):
                if (expense_report[i] + expense_report[j] + expense_report[k] == 2020):
                    return (expense_report[i] * expense_report[j] * expense_report[k])

def main():
    filepath = os.path.join("December1st", "input.txt")
    file_object = open(filepath, "r")
    int_stream = [int(num) for num in file_object]
    answer = brute_force_solution(int_stream)
    print(answer)

if __name__ == "__main__":
    main()