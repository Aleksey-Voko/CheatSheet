from pathlib import Path

from ruamel.yaml import YAML


def add_dict_in_yaml(in_dct, out_f, encoding='utf-8', flow_style=False):
    """
    Добавляет словарь в YAML-файл.
    Если YAML-файл не существует, создаёт его.
    Если существует, дозаписывает словарь в конец файла.

    :param in_dct: словарь для добавления
    :param out_f: YAML-файл
    :param encoding: кодировка YAML-файла
    :param flow_style: True or False
    """
    yaml = YAML(pure=True)
    yaml.default_flow_style = flow_style
    sep = ''
    if Path(out_f).exists():
        mode = 'a'
        if Path(out_f).stat().st_size:
            sep = '---\n'
    else:
        mode = 'w'
    Path(out_f).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_f), mode, encoding=encoding) as f_out:
        if sep:
            f_out.write(sep)
        yaml.dump(in_dct, f_out)


def save_dicts_to_yaml(in_dicts, out_f, encoding='utf-8', flow_style=False):
    """
    Сохраняет список словарей в YAML-файл.

    :param in_dicts: список словарей
    :param out_f: YAML-файл
    :param encoding: кодировка YAML-файла
    :param flow_style: True or False
    """
    yaml = YAML(pure=True)
    yaml.default_flow_style = flow_style
    Path(out_f).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_f), 'w', encoding=encoding) as f_out:
        yaml.dump_all(in_dicts, f_out)


def get_dicts_from_yaml(in_f, encoding='utf-8'):
    """
    Читает список словарей из YAML-файл.
    :param in_f: YAML-файл
    :param encoding: кодировка YAML-файла
    :return: генератор списка, содержащего словари
    """
    yaml = YAML(pure=True)
    with open(Path(in_f), encoding=encoding) as f_in:
        for item in yaml.load_all(f_in):
            yield dict(item)
