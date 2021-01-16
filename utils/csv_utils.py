import csv
from pathlib import Path

import numpy


def get_list_of_dicts_from_csv_file(f_name, encoding='utf-8',
                                    newline='', delimiter=','):
    """
    Читает список словарей из CSV-файла.

    :param f_name: CSV-файл
    :param encoding: кодировка CSV-файла
    :param newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: генератор списка, содержащего словари
    """
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def save_list_of_dicts_to_csv_file(in_list, f_name, field_names,
                                   encoding='utf-8', newline='',
                                   delimiter=','):
    """
    Сохраняет список словарей в CSV-файл.

    :param in_list: список, содержащий словари
    :param f_name: CSV-файл
    :param field_names: список заголовков колонок CSV-файла
    :param encoding: кодировка CSV-файла
    :param newline: newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    """
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(f_name, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=field_names,
                                    delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(in_list)


def get_list_of_lists_from_csv_file(f_name, encoding='utf-8',
                                    newline='', delimiter=','):
    """
    Читает список списков из CSV-файла.
    Первый список - заголовки колонок CSV-файла.

    :param f_name: CSV-файл
    :param encoding: кодировка CSV-файла
    :param newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: генератор списка, содержащего списки
    """
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.reader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def save_list_of_lists_to_csv_file(in_list, f_name, encoding='utf-8',
                                   newline='', delimiter=','):
    """
    Сохраняет список списков в CSV-файл.
    Первый список - заголовки колонок CSV-файла.

    :param in_list: список, содержащий списки
    :param f_name: CSV-файл
    :param encoding: кодировка CSV-файла
    :param newline: newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    """
    Path(f_name).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(f_name), 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.writer(f_out, delimiter=delimiter)
        csv_writer.writerows(in_list)


def get_fieldnames_from_csv_file(f_name, encoding='utf-8',
                                 newline='', delimiter=','):
    """
    Возвращает список заголовков колонок CSV-файла.

    :param f_name: CSV-файл
    :param encoding: кодировка CSV-файла
    :param newline: newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: список заголовков колонок CSV-файла
    """
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        return csv.DictReader(f_in, delimiter=delimiter).fieldnames


def save_parts_csv(f_name, count_parts, encoding='utf-8',
                   newline='', delimiter=','):
    """
    Разделяет CSV-файл на примерно равные части.

    :param f_name: CSV-файл
    :param count_parts: количество частей
    :param encoding: кодировка CSV-файла
    :param newline: newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    """
    list_of_dicts = []
    with open(Path(f_name), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        field_names = list(csv_reader.fieldnames)
        for row in csv_reader:
            list_of_dicts.append(row)
    parts = numpy.array_split(list_of_dicts, count_parts)
    for count, part in enumerate(parts, 1):
        save_list_of_dicts_to_csv_file(
            part,
            f'{Path(f_name).name}_{count:03}.csv',
            field_names
        )
