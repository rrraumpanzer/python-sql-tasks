from solution import make_cars_table, populate_cars_table, get_all_cars


def test_solution(db_transaction):
    make_cars_table(db_transaction)
    cars = get_all_cars(db_transaction)
    assert cars == []

    cars = [('lada', 'zaporozhets'), ('cherry', '9')]
    populate_cars_table(db_transaction, cars)

    assert get_all_cars(db_transaction) == [
        (2, 'cherry', '9'),
        (1, 'lada', 'zaporozhets')
    ]
