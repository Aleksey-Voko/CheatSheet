def get_clear_digit(input_string: str) -> str:
    return ''.join([x for x in input_string if x.isdecimal()])


def get_format_phone(input_string: str) -> str:
    dig = get_clear_digit(input_string)
    phone = f'phone: +{dig[0]} {dig[1:4]} {dig[4:6]}-{dig[6:8]}-{dig[8:]}'
    phone = phone.replace('+8', '+7')
    return phone


if __name__ == '__main__':
    print(get_format_phone('телефон - (8)555 446-677'))
