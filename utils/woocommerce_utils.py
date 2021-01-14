import csv
from collections import OrderedDict
from pathlib import Path

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


def get_dicts_from_csv_file(in_f, encoding='utf-8',
                            newline='', delimiter=','):
    """
    Читает список словарей из CSV-файла.

    :param in_f: CSV-файл
    :param encoding: кодировка CSV-файла
    :param newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: генератор списка, содержащего словари
    """
    with open(Path(in_f), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            yield row


def save_dicts_to_csv_file(in_list, out_f, field_names,
                           encoding='utf-8', newline='', delimiter=','):
    """
    Сохраняет список словарей в CSV-файл.

    :param in_list: список, содержащий словари
    :param out_f: CSV-файл
    :param field_names: список заголовков колонок CSV-файла
    :param encoding: кодировка CSV-файла
    :param newline: newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    """
    Path(out_f).parent.mkdir(parents=True, exist_ok=True)
    with open(out_f, 'w', encoding=encoding, newline=newline) as f_out:
        csv_writer = csv.DictWriter(f_out, fieldnames=field_names,
                                    delimiter=delimiter)
        csv_writer.writeheader()
        csv_writer.writerows(in_list)


def get_product_card_dicts(in_f, encoding='utf-8',
                           newline='', delimiter=','):
    """
    Читает словари с продуктами из файла экспорта.

    :param in_f: CSV-файл экспорта
    :param encoding: кодировка CSV-файла
    :param newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: генератор списка, содержащего словари с продуктами
    """
    product_card_dicts = get_dicts_from_csv_file(in_f, encoding=encoding,
                                                 newline=newline,
                                                 delimiter=delimiter)
    for product in product_card_dicts:
        key_list = []
        value_list = []
        for product_key in list(product.keys())[:]:
            if product_key.startswith('Имя атрибута'):
                key_list.append(product_key)
            elif product_key.startswith('Значение(-я) аттрибута(-ов)'):
                value_list.append(product_key)

        key_list = [product[x] for x in key_list]
        value_list = [product[x] for x in value_list]

        for product_key in list(product.keys())[:]:
            if product_key.startswith((
                    'Имя атрибута', 'Значение(-я) аттрибута(-ов)',
                    'Видимость атрибута', 'Глобальный атрибут')):
                del product[product_key]

        # noinspection PyTypeChecker
        product['Атрибуты'] = OrderedDict()
        for key, value in zip(key_list, value_list):
            if key and value:
                # noinspection PyUnresolvedReferences
                product['Атрибуты'][key] = value

        yield product


def get_attribute_set(in_f, encoding='utf-8',
                      newline='', delimiter=','):
    """
    Читает список возможных атрибутов из файла экспорта.

    :param in_f: CSV-файл экспорта
    :param encoding: кодировка CSV-файла
    :param newline: newline='' исправляет '\r\r\n' -> '\r\n'
        https://docs.python.org/3/library/csv.html#id3
    :param delimiter: разделитель [,] or [;]
    :return: сортированный список атрибутов продукта
    """
    product_card_dicts = get_product_card_dicts(in_f, encoding=encoding,
                                                newline=newline,
                                                delimiter=delimiter)
    attributes_set = set()
    for product_card in product_card_dicts:
        # noinspection PyUnresolvedReferences
        for attr in list(product_card['Атрибуты'].keys()):
            attributes_set.add(attr)
    return sorted(list(attributes_set))


def get_import_product_card_dicts(product_cards):
    """
    Возвращает словари с продуктами для файла импорта.
    Распределяет атрибуты по колонкам.

    :param product_cards: список словарей, содержащих продукты
    :return: генератор списка словарей, содержащих продукты для импорта.
    """
    for product_card in product_cards:
        new_product = OrderedDict()
        for field_key in product_card:
            if field_key != 'Атрибуты':
                new_product[field_key] = product_card[field_key]

        attributes_dict = OrderedDict()
        for attr_key in product_card['Атрибуты'].keys():
            attributes_dict[attr_key] = product_card['Атрибуты'][attr_key]

        for count, attr_key in enumerate(attributes_dict.keys(), 1):
            new_product[f'Имя атрибута {count}'] = attr_key
            new_product[
                f'Значение(-я) аттрибута(-ов) {count}'
            ] = attributes_dict[attr_key]
            new_product[f'Видимость атрибута {count}'] = 1
            new_product[f'Глобальный атрибут {count}'] = 1

        yield new_product
