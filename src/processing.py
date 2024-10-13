def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    """Функцию принимает список словарей и опционально значение для ключа state, затем возвращает новый
    список словарей, содержащий только те словари, у которых ключ state соответствует значению 'EXECUTED'."""

    filtered_list_of_dictionaries = []
    for key_list_of_dic in list_of_dictionaries:
        if key_list_of_dic.get("state") == state:
            filtered_list_of_dictionaries.append(key_list_of_dic)
    return filtered_list_of_dictionaries


def sort_by_date(list_of_dictionaries: list, sort_order: bool = True) -> list:
    """Функцию принимает список словарей и необязательный параметр, задающий
    порядок сортировки, затем возвращает новый список, отсортированный по дате."""

    if sort_order:
        sorted_list = sorted(list_of_dictionaries, key=lambda x: x['date'])
    else:
        sorted_list = sorted(list_of_dictionaries, key=lambda x: x['date'], reverse=True)
    return sorted_list
