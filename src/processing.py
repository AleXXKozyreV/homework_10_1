def filter_by_state(list_of_dictionaries: list, state: str = 'EXECUTED') -> list:
    """Функцию принимает список словарей и опционально значение для ключа state, затем возвращает новый список словарей,
    содержащий только те словари, у которых ключ state соответствует значению 'EXECUTED'."""

    filtered_list_of_dictionaries = []
    for key_list_of_dic in list_of_dictionaries:
        if key_list_of_dic.get("state") == state:
            filtered_list_of_dictionaries.append(key_list_of_dic)
    return filtered_list_of_dictionaries

