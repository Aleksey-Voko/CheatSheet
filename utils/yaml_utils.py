"""
For product card list
"""

from pathlib import Path

from ruamel.yaml import YAML


def add_dict_in_yaml(in_dct: dict, out_file: str, encoding='utf-8', flow_style=True):
    yaml = YAML(pure=True)
    yaml.default_flow_style = flow_style
    sep = ''
    if Path(out_file).exists():
        mode = 'a'
        if Path(out_file).stat().st_size:
            sep = '---\n'
    else:
        mode = 'w'
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), mode, encoding=encoding) as f_out:
        if sep:
            f_out.write(sep)
        yaml.dump(in_dct, f_out)


def save_dicts_to_yaml(in_dicts, out_file: str, encoding='utf-8', flow_style=True):
    yaml = YAML(pure=True)
    yaml.default_flow_style = flow_style
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(Path(out_file), 'w', encoding=encoding) as f_out:
        yaml.dump_all(in_dicts, f_out)


def get_dicts_from_yaml(input_file: str, encoding='utf-8'):
    yaml = YAML(pure=True)
    with open(Path(input_file), encoding=encoding) as f_in:
        for item in yaml.load_all(f_in):
            yield dict(item)


if __name__ == '__main__':
    # product_card_list = get_eval_list_from_file('product_card_list.txt')
    # save_dicts_to_yaml(product_card_list, 'product_card_list_flow.yml', flow_style=True)

    product_card_list = get_dicts_from_yaml('product_card_list_flow.yml')
    save_dicts_to_yaml(product_card_list, 'out_flow_tmp.yaml', flow_style=False)

    # for product_card in product_card_list:
    #     add_dict_in_yaml(product_card, 'out_flow_tmp.yaml', flow_style=False)
