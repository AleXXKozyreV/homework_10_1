def get_mask_card_number(card_number: str) -> str:
    """Функция принимает номер карты в виде строки и возвращает её маску"""

    blocks_card_numbers = [card_number[:4], card_number[4:6] + "**", "****", card_number[-4:]]
    mask_card_number = " ".join(blocks_card_numbers)
    return mask_card_number


def get_mask_account(account_number: str) -> str:
    """Функция принимает номер счета в виде строки и возвращает его маску"""

    mask_account = "**" + account_number[-4:]
    return mask_account
