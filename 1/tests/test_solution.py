from solution import add_movies, get_all_movies


def test_solution(db_transaction):
    add_movies(db_transaction)
    movies = get_all_movies(db_transaction)
    assert movies == [
        (1, 'Godfather', 1972, 175),
        (2, 'The Green Mile', 1999, 189)
    ]
