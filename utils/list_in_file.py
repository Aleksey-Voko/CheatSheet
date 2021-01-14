import pickle
from pathlib import Path


def get_str_list_from_file(in_f, encoding='utf-8'):
    with open(Path(in_f), encoding=encoding) as f_in:
        for line in f_in:
            yield line.rstrip()


def get_eval_list_from_file(in_f, encoding='utf-8'):
    with open(Path(in_f), encoding=encoding) as f_in:
        for line in f_in:
            yield eval(line.rstrip())


def save_str_list_to_file(in_list, out_f, encoding='utf-8'):
    Path(out_f).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_f), 'w', encoding=encoding) as f_out:
        for line in in_list:
            f_out.write(str(line) + '\n')


def save_obj_to_file(in_obj, out_f):
    Path(out_f).parent.mkdir(parents=True, exist_ok=True)
    with open(out_f, 'wb') as f_out:
        pickle.dump(in_obj, f_out)


def get_obj_from_file(in_f):
    with open(Path(in_f), 'rb') as f_in:
        return pickle.load(f_in)
