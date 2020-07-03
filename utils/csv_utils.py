import csv
from pathlib import Path

import numpy


def save_list_to_csv_file(input_list: list, out_file: str,
                          encoding='utf-8', newline='', delimiter=','):
    """
    сохраняет список списков в csv файл,
    первый список - строка заголовков

    newline '\r\r\n' -> '\r\n'
    https://docs.python.org/3/library/csv.html#id3

    delimiter - разделитель [,] or [;]

    docs -> https://docs.python.org/3/library/csv.html
    """
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.writer(f_out, delimiter=delimiter)
        csv_writer.writerows(input_list)


def get_list_of_lists_from_csv_file(input_file: str, encoding='utf-8',
                                    newline='', delimiter=',') -> list:
    """
    читает список списков из csv файла
    первый список - строка заголовков

    newline '\r\r\n' -> '\r\n'
    https://docs.python.org/3/library/csv.html#id3

    delimiter - разделитель [,] or [;]

    docs -> https://docs.python.org/3/library/csv.html
    """
    out_list = []
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.reader(f_in, delimiter=delimiter)
        for row in csv_reader:
            out_list.append(row)
    return out_list


def save_list_of_dicts_to_csv_file(input_list: list, out_file: str,
                                   field_names: list, encoding='utf-8',
                                   newline='', delimiter=','):
    """
    сохраняет список словарей в csv файл,
    у всех словарей идентичные ключи

    fieldnames - порядок ключей для записи в файл ->
    fieldnames = ['first_name', 'last_name']

    newline '\r\r\n' -> '\r\n'
    https://docs.python.org/3/library/csv.html#id3

    delimiter - разделитель [,] or [;]

    docs -> https://docs.python.org/3/library/csv.html
    """
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=field_names, delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(input_list)


def get_list_of_dicts_from_csv_file(input_file: str, encoding='utf-8',
                                    newline='', delimiter=',') -> list:
    """
    читает список словарей из csv файла

    newline='' исправляет '\r\r\n' -> '\r\n'
    https://docs.python.org/3/library/csv.html#id3

    delimiter - разделитель [,] or [;]

    docs -> https://docs.python.org/3/library/csv.html
    """
    out_list = []
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            out_list.append(row)
    return out_list


def get_fieldnames_from_csv_file(input_file: str, encoding='utf-8',
                                 newline='', delimiter=','):
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        return csv.DictReader(f_in, delimiter=delimiter).fieldnames


def save_parts_csv(input_file: str, count_parts: int, encoding='utf-8',
                   newline='', delimiter=','):
    dict_list = []
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        field_names = list(csv_reader.fieldnames)
        for row in csv_reader:
            dict_list.append(row)
    parts = numpy.array_split(dict_list, count_parts)
    for count, part in enumerate(parts, 1):
        save_list_of_dicts_to_csv_file(part, f'{input_file}_{count:03}.csv', field_names)
