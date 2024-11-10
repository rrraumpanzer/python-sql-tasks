from solution import batch_insert, get_all_products
import pytest
from decimal import Decimal


@pytest.fixture()
def products():
    return [
        {'name': 'apple', 'price': 5, 'quantity': 10},
        {'name': 'kiwi', 'price': 7, 'quantity': 12},
        {'name': 'cheese', 'price': 15, 'quantity': 20},
        {'name': 'butter', 'price': 10, 'quantity': 8}
    ]


def test_solution(db_transaction, products):
    assert get_all_products(db_transaction) == []

    batch_insert(db_transaction, products)
    selected_products = get_all_products(db_transaction)
    print(selected_products)
    assert selected_products == [
        (3, 'cheese', Decimal('15'), 20),
        (4, 'butter', Decimal('10'), 8),
        (2, 'kiwi', Decimal('7'), 12),
        (1, 'apple', Decimal('5'), 10)
    ]
