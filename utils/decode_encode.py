"""Меняет кодировку файлов"""


def encode_decode_file_list(file_name_list: list,
                            in_encoding='cp1252',
                            out_encoding='utf-8'):
    """Меняет кодировку файлов из списка.
    Перезаписываем исходные файлы."""
    for file_name in file_name_list:
        with open(file_name, encoding=in_encoding) as f_in:
            file_content = f_in.read()
        with open(file_name, 'w', encoding=out_encoding) as f_out:
            f_out.write(file_content)
