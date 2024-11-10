from solution import get_order_sum


def test_solution(db_transaction):
    customers_stats = get_order_sum(db_transaction, 2)
    assert customers_stats.split('\n') == [
        'Покупатель John Smith совершил покупок на сумму 240',
        'Покупатель Michael Brown совершил покупок на сумму 800',
    ]
