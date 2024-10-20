import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, mask_card_number",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234123412341234", "1234 12** **** 1234"),
        ("5678567856785678", "5678 56** **** 5678"),
        ("1111222233334444", "1111 22** **** 4444"),
        ("5555666677778888", "5555 66** **** 8888"),
        ("1234567812345678", "1234 56** **** 5678"),
    ],
)
def test_get_mask_card_number(card_number, mask_card_number):
    assert get_mask_card_number(card_number) == mask_card_number


@pytest.mark.parametrize(
    "account_number, mask_account",
    [
        ("73654108430135874305", "**4305"),
        ("64686473678894779589", "**9589"),
        ("35383033474447895560", "**5560"),
        ("73654108430135874305", "**4305"),
    ],
)
def test_get_mask_account(account_number, mask_account):
    assert get_mask_account(account_number) == mask_account
