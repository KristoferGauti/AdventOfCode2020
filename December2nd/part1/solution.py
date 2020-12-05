import os

"""
    The text file input.txt contains password policies. For example 1-3 b: abs is a valid password 
    The numbers 1-3 describes how many of the letter b the password must have.
    A password is valid if it has at least 1-3 of that particular letter in itself.
    Find how many valid passwords there are and print the quantity
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

def count_valid_password(password_policy_list):
    """
        Time complexity: ~n or O(n) where n is the length of the list
        Iterate through the password policy list line by line and
        checks if the password is valid, 
        if so increase the valid_password_counter
    """
    valid_password_counter = 0
    for qty, letter, password in password_policy_list:
        qty_list = list(map(int, qty.split("-")))
        min_qty = qty_list[0]
        max_qty = qty_list[1]
        the_letter = letter[:-1]
    
        if (min_qty <= password.count(the_letter) <= max_qty):
            valid_password_counter += 1

    return valid_password_counter

def main():
    """Total time complexity: ~2n or O(n)"""
    filename = os.path.join("December2nd", "input.txt")
    password_stream = open(filename, "r")
    striped_password_stream = [password.strip() for password in password_stream]
    password_policies_list = get_password_policies_list(striped_password_stream)

    print(count_valid_password(password_policies_list))

main()