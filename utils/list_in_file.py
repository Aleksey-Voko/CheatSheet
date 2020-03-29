import csv
import pickle
from pathlib import Path


def save_list_to_txt_file(input_list: list, out_file: str, encoding='utf-8'):
    """
    сохраняет list в текстовой файл построчно
    """
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        for line in input_list:
            f_out.write(str(line) + '\n')


def get_eval_list_from_txt_file(input_file: str, encoding='utf-8') -> list:
    """
    читает list (eval) из текстового файла построчно
    """
    out_list = []
    with open(Path(input_file), encoding=encoding) as f_in:
        for line in f_in.readlines():
            out_list.append(eval(line.strip()))
    return out_list


def get_string_list_from_txt_file(input_file: str, encoding='utf-8') -> list:
    """
    читает list из текстового файла построчно
    """
    out_list = []
    with open(Path(input_file), encoding=encoding) as f_in:
        for line in f_in.readlines():
            out_list.append(line.strip())
    return out_list


def save_object_to_bin_file(input_object, out_file_name: str):
    """
    сохраняет object в бинарный файл
    """
    with open(out_file_name, 'wb') as f_out:
        pickle.dump(input_object, f_out)


def get_object_from_bin_file(input_file: str):
    """
    читает object из бинарного файла
    """
    with open(Path(input_file), 'rb') as f_in:
        return pickle.load(f_in)


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
    with open(Path(out_file), 'w',
              encoding=encoding,
              newline=newline) as f_out:
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
                                   fieldnames: list, encoding='utf-8',
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
    with open(out_file, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=fieldnames,
                                    delimiter=delimiter)
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
