import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transaction):
    transaction_filter = filter_by_currency(transaction, "USD")
    assert next(transaction_filter)["id"] == 939719570
    assert next(transaction_filter)["id"] == 142264268
    assert next(transaction_filter)["id"] == 895315941


@pytest.mark.parametrize('index, expected', [
    (0, "Перевод организации"),
    (1, "Перевод со счета на счет"),
    (2, "Перевод со счета на счет"),
    (3, "Перевод с карты на карту"),
    (4, "Перевод организации")
])
def test_transaction_descriptions(index, expected):
    transactions = [
        {'description': "Перевод организации"},
        {'description': "Перевод со счета на счет"},
        {'description': "Перевод со счета на счет"},
        {'description': "Перевод с карты на карту"},
        {'description': "Перевод организации"}
    ]
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


@pytest.mark.parametrize('start, stop, result', [
    (1, 4, ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003", "0000 0000 0000 0004"]),
    (11223344, 11223345, ['0000 0000 1122 3344', '0000 0000 1122 3345']),
    (1111222233334444, 1111222233334445, ['1111 2222 3333 4444', '1111 2222 3333 4445'])
])
def test_card_number_generator(start: int, stop: int, result: list) -> None:
    generator = list(card_number_generator(start, stop))
    assert generator == result
