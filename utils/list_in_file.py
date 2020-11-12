import pickle
from pathlib import Path


def save_list_to_file(input_list: list, out_file: str, encoding='utf-8'):
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        for line in input_list:
            f_out.write(str(line) + '\n')


def get_eval_list_from_file(input_file: str, encoding='utf-8'):
    with open(Path(input_file), encoding=encoding) as f_in:
        for line in f_in:
            yield eval(line.rstrip())


def get_string_list_from_file(input_file: str, encoding='utf-8'):
    with open(Path(input_file), encoding=encoding) as f_in:
        for line in f_in:
            yield line.rstrip()


def save_object_to_file(in_obj, out_file: str):
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'wb') as f_out:
        pickle.dump(in_obj, f_out)


def get_object_from_file(input_file: str):
    with open(Path(input_file), 'rb') as f_in:
        return pickle.load(f_in)
