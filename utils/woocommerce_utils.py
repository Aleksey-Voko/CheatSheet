import csv
from pathlib import Path
from pprint import pprint


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
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=fieldnames,
                                    delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(input_list)


def get_product_card_dict_list(input_file: str, encoding='utf-8',
                               newline='', delimiter=',') -> list:
    """
    Возвращает список словарей с продуктами из файла экспорта
    """
    product_card_dict_list = []
    product_export_card_dict_list = get_list_of_dicts_from_csv_file(input_file, encoding=encoding,
                                                                    newline=newline, delimiter=delimiter)
    for product_export in product_export_card_dict_list:
        key_list = []
        value_list = []
        for product_key in list(product_export.keys())[:]:
            if product_key.startswith('Имя атрибута'):
                key_list.append(product_key)
            elif product_key.startswith('Значение(-я) аттрибута(-ов)'):
                value_list.append(product_key)

        key_list = sorted(key_list)
        key_list = [product_export[x] for x in key_list]
        value_list = sorted(value_list)
        value_list = [product_export[x] for x in value_list]

        for product_key in list(product_export.keys())[:]:
            if product_key.startswith(('Имя атрибута', 'Значение(-я) аттрибута(-ов)',
                                       'Видимость атрибута', 'Глобальный атрибут')):
                del product_export[product_key]

        product_export['Атрибуты'] = {}
        for key, value in zip(key_list, value_list):
            if key and value:
                product_export['Атрибуты'][key] = value
        product_card_dict_list.append(product_export)
    return product_card_dict_list


def get_attribute_set(input_file: str, encoding='utf-8',
                      newline='', delimiter=',') -> list:
    """
    Возвращает список атрибутов из файла экспорта
    """
    product_card_list = get_product_card_dict_list(input_file, encoding=encoding,
                                                   newline=newline, delimiter=delimiter)
    attributes_set = set()
    for product_card in product_card_list:
        attributes = product_card['Атрибуты']
        for attr in list(attributes.keys()):
            attributes_set.add(attr)
    return sorted(list(attributes_set))


def get_import_csv_product_card_list(product_card_list: list) -> list:
    """
    Возвращает список словарей с продуктами для файла импорта
    Для файла импорта понадобится ещё список field_names
    """
    product_out_dict_list = []

    # полный список возможных полей
    field_names = [
        'ID',
        'Тип',
        'Артикул',
        'Имя',
        'Опубликован',
        'рекомендуемый?',
        'Видимость в каталоге',
        'Короткое описание',
        'Описание',
        'Дата начала действия продажной цены',
        'Дата окончания действия продажной цены',
        'Статус налога',
        'Налоговый класс',
        'В наличии?',
        'Запасы',
        'Величина малых запасов',
        'Возможен ли предзаказ?',
        'Продано индивидуально?',
        'Вес (kg)',
        'Длина (cm)',
        'Ширина (cm)',
        'Высота (cm)',
        'Разрешить отзывы от клиентов?',
        'Примечание к покупке',
        'Цена распродажи',
        'Базовая цена',
        'Категории',
        'Метки',
        'Класс доставки',
        'Изображения',
        'Лимит загрузок',
        'Число дней до просроченной загрузки',
        'Родительский',
        'Сгруппированные товары',
        'Апсейл',
        'Кросселы',
        'Внешний URL',
        'Текст кнопки',
        'Позиция',
    ]

    for product_card in product_card_list:
        new_product = {}
        for field in field_names:
            field_value = product_card.get(field)
            if field_value:
                new_product[field] = field_value

        attributes_dict = {}
        for key in product_card['Атрибуты'].keys():
            attributes_dict[key] = product_card['Атрибуты'][key]

        for count, key in enumerate(attributes_dict.keys(), 1):
            if f'Имя атрибута {count}' not in field_names:
                field_names.append(f'Имя атрибута {count}')
            if f'Имя атрибута {count}' not in new_product.keys():
                new_product[f'Имя атрибута {count}'] = key

            if f'Значение(-я) аттрибута(-ов) {count}' not in field_names:
                field_names.append(f'Значение(-я) аттрибута(-ов) {count}')
            if f'Значение(-я) аттрибута(-ов) {count}' not in new_product.keys():
                new_product[f'Значение(-я) аттрибута(-ов) {count}'] = attributes_dict[key]

            if f'Видимость атрибута {count}' not in field_names:
                field_names.append(f'Видимость атрибута {count}')
            if f'Видимость атрибута {count}' not in new_product.keys():
                new_product[f'Видимость атрибута {count}'] = 1

            if f'Глобальный атрибут {count}' not in field_names:
                field_names.append(f'Глобальный атрибут {count}')
            if f'Глобальный атрибут {count}' not in new_product.keys():
                new_product[f'Глобальный атрибут {count}'] = 1

        product_out_dict_list.append(new_product)

    return product_out_dict_list


def save_import_csv_product_card_list(product_card_list: list, out_file: str,
                                      encoding='utf-8', newline='', delimiter=','):
    """
    Сохраняет файл для импорта
    """
    product_out_dict_list = []

    # полный список возможных полей
    field_names = [
        'ID',
        'Тип',
        'Артикул',
        'Имя',
        'Опубликован',
        'рекомендуемый?',
        'Видимость в каталоге',
        'Короткое описание',
        'Описание',
        'Дата начала действия продажной цены',
        'Дата окончания действия продажной цены',
        'Статус налога',
        'Налоговый класс',
        'В наличии?',
        'Запасы',
        'Величина малых запасов',
        'Возможен ли предзаказ?',
        'Продано индивидуально?',
        'Вес (kg)',
        'Длина (cm)',
        'Ширина (cm)',
        'Высота (cm)',
        'Разрешить отзывы от клиентов?',
        'Примечание к покупке',
        'Цена распродажи',
        'Базовая цена',
        'Категории',
        'Метки',
        'Класс доставки',
        'Изображения',
        'Лимит загрузок',
        'Число дней до просроченной загрузки',
        'Родительский',
        'Сгруппированные товары',
        'Апсейл',
        'Кросселы',
        'Внешний URL',
        'Текст кнопки',
        'Позиция',
    ]

    for product_card in product_card_list:
        new_product = {}
        for field in field_names:
            field_value = product_card.get(field)
            if field_value:
                new_product[field] = field_value

        attributes_dict = {}
        for key in product_card['Атрибуты'].keys():
            attributes_dict[key] = product_card['Атрибуты'][key]

        for count, key in enumerate(attributes_dict.keys(), 1):
            if f'Имя атрибута {count}' not in field_names:
                field_names.append(f'Имя атрибута {count}')
            if f'Имя атрибута {count}' not in new_product.keys():
                new_product[f'Имя атрибута {count}'] = key

            if f'Значение(-я) аттрибута(-ов) {count}' not in field_names:
                field_names.append(f'Значение(-я) аттрибута(-ов) {count}')
            if f'Значение(-я) аттрибута(-ов) {count}' not in new_product.keys():
                new_product[f'Значение(-я) аттрибута(-ов) {count}'] = attributes_dict[key]

            if f'Видимость атрибута {count}' not in field_names:
                field_names.append(f'Видимость атрибута {count}')
            if f'Видимость атрибута {count}' not in new_product.keys():
                new_product[f'Видимость атрибута {count}'] = 1

            if f'Глобальный атрибут {count}' not in field_names:
                field_names.append(f'Глобальный атрибут {count}')
            if f'Глобальный атрибут {count}' not in new_product.keys():
                new_product[f'Глобальный атрибут {count}'] = 1

        product_out_dict_list.append(new_product)

    save_list_of_dicts_to_csv_file(product_out_dict_list, out_file, field_names,
                                   encoding=encoding, newline=newline, delimiter=delimiter)
