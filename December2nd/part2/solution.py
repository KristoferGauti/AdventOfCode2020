import os

"""
    The text file input.txt contains password policies. For example 1-3 b: abs or  
    1-3 b babft are invalid passwords, where the numbers 1-3 describes that the 
    letter b must be in the first place of the word or the third place, 
    it cannot be in both first place and the third place. Example of a valid passwords: 1-3 a: asvge
"""

def get_password_policies_list(passwords):
    """
        Time complexity: ~n or O(n) where n is the length of the list
        Gets the password policy lines from the file input.txt
    """
    column_list = []
    for password in passwords:
        column_list.append(password.split(" "))
        
    return column_list

def count_valid_passwords(password_policy_list):
    """
        Time complexity: ~n or O(n) where n is the length of the list
        counts a valid password if the password's index contains exactly 
        one of the given letter. Other occurenses of the given letter are 
        irrelevant passwords, that is why the if statement has an XOR check.    
    """
    valid_password_counter = 0
    for not_a_computer_index, letter, password in password_policy_list:
        qty_list = list(map(int, not_a_computer_index.split("-")))
        low_index = qty_list[0] - 1
        high_index = qty_list[1] - 1
        the_letter = letter[:-1]

        if (password[low_index] == the_letter) ^ (password[high_index] == the_letter):
            valid_password_counter += 1

    print(valid_password_counter)


def main():
    """Total time complexity: """
    filename = os.path.join("December2nd", "input.txt")
    password_stream = open(filename, "r")
    striped_password_stream = [password.strip() for password in password_stream]
    password_policies_list = get_password_policies_list(striped_password_stream)

    count_valid_passwords(password_policies_list)

main()