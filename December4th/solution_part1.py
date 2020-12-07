"""
    You forgot your passport and you are at the airport. You have the North Pole 
    passport with you which is similar to a regular passport, the only difference is that
    the North Pole passport does not have a cid (country ID). Each passports are represented by key: value pairs
    with the fields byr (birth year), iyr (issue year), eyr (expiration year), hgt (height), hcl (hair color), ecl (eye color), pid (passportID), cid (countryID)
    A passport is valid if it has all the required fields or if it has all the required fields except cid.
    Count the number of valid passwords in input.txt file.
"""
import os

def clean_data(data_list):
    clean_data_list = []
    passport_dict = dict()
    for paragraph in data_list:
        clean_paragraph = paragraph.replace("\n", " ")
        clean_data_list.append(clean_paragraph.split(" "))

    #clear duplicate passports
    for i in range(len(clean_data_list)):
        clean_data_list[i] = {clean_data_list[i][j][:3] : clean_data_list[i][j][4:] for j in range(len(clean_data_list[i]))}

    return clean_data_list

def count_valid_passports(data):
    valid_password_counter = 0
    for passport_fields in data:
        if (len(passport_fields) == 8) or ("cid" not in passport_fields and len(passport_fields) == 7):
            valid_password_counter += 1    
       
    return valid_password_counter

def main():
    filename = os.path.join("December4th", "input.txt")
    file_obj = open(filename, "r")
    paragraph_list = file_obj.read().split("\n\n")
    passports = clean_data(paragraph_list)
    print(count_valid_passports(passports))

if __name__ == "__main__":
    main()

