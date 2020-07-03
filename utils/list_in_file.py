import pickle
from pathlib import Path


def save_list_to_txt_file(input_list: list, out_file: str, encoding='utf-8'):
    """
    сохраняет list в текстовой файл
    """
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        for line in input_list:
            f_out.write(str(line) + '\n')


def get_eval_list_from_txt_file(input_file: str, encoding='utf-8') -> list:
    """
    читает list (eval) из текстового файла
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


def save_object_to_bin_file(input_object, out_file: str):
    """
    сохраняет object в бинарный файл
    """
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'wb') as f_out:
        pickle.dump(input_object, f_out)


def get_object_from_bin_file(input_file: str):
    """
    читает object из бинарного файла
    """
    with open(Path(input_file), 'rb') as f_in:
        return pickle.load(f_in)
