from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_or_acc_num: str) -> str:
    """Функция принимает тип и номер карты или счета в виде строки и возвращает строку с замаскированным номером"""

    if len(card_or_acc_num.split()[-1]) == 16:
        mask_card_number_ = get_mask_card_number(card_or_acc_num.split()[-1])
        result = f"{card_or_acc_num[:-16]}{mask_card_number_}"

    elif len(card_or_acc_num.split()[-1]) == 20:
        mask_account_ = get_mask_account(card_or_acc_num.split()[-1])
        result = f"{card_or_acc_num[:-20]}{mask_account_}"

    return result


def get_date(old_data: str) -> str:
    """Функция принимает строку с датой и форматирует её"""

    data_slice = old_data[0:10].split("-")
    result = ".".join(data_slice[::-1])

    return result
