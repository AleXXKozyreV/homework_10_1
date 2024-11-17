import json


def transaction_amount(file_path: str) -> float:
    """Функция, которая выводит сумму транзакции"""

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            repository = json.load(file)
        if isinstance(repository, list):
            return repository
        else:
            return []

    except Exception as error:
        print(f"Ошибка {error}")
        return []
