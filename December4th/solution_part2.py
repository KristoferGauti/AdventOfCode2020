"""
    The line at the airport is getting quicker since you just broke the
    system by removing the country ID to validate the North Pole passport.
    The security is here so you got to be careful.You need to add some data
    validation quick. You can continue ignooring th cid field but the other fields
    have strict rules for automatic validation of the passports.
    they are as follows:
    byr -> four digits, at least 1920 and at most 2002
    iyr -> four digits, at least 2010 and at most 2020
    eyr -> four digits; at least 2020 and at most 2030
    hgt -> a number followed by either cm or in: 
           If cm, the number must be at least 150 and at most 193
           If in, the number must be at least 59 and at most 76
    hcl -> a # followed by exactly six characters 0-9 or a-f
    ecl -> exactly one of: amb blu brn gry grn hzl oth
    pid -> a nine-digit number, including leading zeroes
    cid -> ignored, missing or not
"""
from solution_part1 import *
import os
import re

def count_valid_passport(passports):
    passport_valid_counter = 0
    for passport_dict in passports:
        if (len(passport_dict) == 8) or ("cid" not in passport_dict and len(passport_dict) == 7):
            if (1920 <= int(passport_dict["byr"]) <= 2002):
                if (2010 <= int(passport_dict["iyr"]) <= 2020):
                    if (2020 <= int(passport_dict["eyr"]) <= 2030):
                        if (passport_dict["hgt"][-2:] == "cm") and (150 <= int(passport_dict['hgt'][:-2]) <= 193) or \
                            (passport_dict['hgt'][-2:] == 'in') and (59 <= int(passport_dict['hgt'][:-2]) <= 76):
                            if (re.search("#[0-9a-f]{6}", passport_dict["hcl"])):
                                if (passport_dict["ecl"] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                                    if (passport_dict["pid"].isdigit() and len(passport_dict["pid"]) == 9):
                                        passport_valid_counter += 1
    return passport_valid_counter
                    
def main():
    filename = os.path.join("December4th", "input.txt")
    file_obj = open(filename, "r")
    paragraph_list = file_obj.read().split("\n\n")
    passports = clean_data(paragraph_list)
    print(count_valid_passport(passports))
    
if __name__ == "__main__":
    main()