import csv
from pathlib import Path


def get_list_of_dicts_from_csv_file(input_file: str, encoding='utf-8',
                                    newline='', delimiter=',') -> list:
    out_list = list()
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            out_list.append(row)
    return out_list


def save_list_of_dicts_to_csv_file(input_list: list, out_file: str,
                                   fieldnames: list, encoding='utf-8',
                                   newline='', delimiter=','):
    with open(out_file, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=fieldnames,
                                    delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(input_list)


def get_clear_digit(input_string: str) -> str:
    return ''.join([x for x in input_string if x.isdecimal()])


def get_format_phone(input_string: str) -> str:
    dig = get_clear_digit(input_string)
    if len(dig) == 6:
        phone = f'{dig[:3]}-{dig[3:]}'
    elif len(dig) == 7:
        phone = f'{dig[:3]}-{dig[3:5]}-{dig[5:]}'
    elif len(dig) == 9 and (dig[0] == '7' or dig[0] == '8'):
        phone = f'+7 {dig[1:5]} {dig[5:7]}-{dig[7:]}'
    elif len(dig) == 10:
        phone = f'+7 {dig[:3]} {dig[3:6]}-{dig[6:8]}-{dig[8:]}'
    elif len(dig) == 11:
        phone = f'+7 {dig[1:4]} {dig[4:7]}-{dig[7:9]}-{dig[9:]}'
    elif len(dig) > 11 and (dig[0] == '7' or dig[0] == '8'):
        phone = f'+7 {dig[1:4]} {dig[4:7]}-{dig[7:9]}-{dig[9:11]} ({dig[11:]})'
    else:
        phone = dig
    return phone


def main():
    list_of_dicts = get_list_of_dicts_from_csv_file('phone.csv')

    out_phone_list = []

    for phone_dict in list_of_dicts:
        for phone_src_string in phone_dict.values():
            if phone_src_string:
                for phone_string in phone_src_string.split(','):
                    format_phone = get_format_phone(phone_string)
                    out_phone_list.append({'phone': format_phone})

    save_list_of_dicts_to_csv_file(out_phone_list, 'out_phone.csv', ['phone'])


if __name__ == '__main__':
    main()
