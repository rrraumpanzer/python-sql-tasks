# Запросы

## src/solution.py

Создайте функцию `batch_insert()`, которая принимает соединение, и список товаров и массово добавляет их в базу. Каждый товар представлен словарем с ключами `name`, `price`, и `quantity`. Для безопасной и быстрой работы с базой данных используйте плейсхолдеры.

Так же создайте функцию `get_all_products()`, которая принимает соединение, и возвращает весь список товаров, отсортированый по цене товара `DESC`.

```python
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price NUMERIC NOT NULL,
    quantity INT NOT NULL
);
conn = psycopg2.connect('..')

products = [
    {'name': 'milk', 'price': 12, 'quantity': 20},
    {'name': 'bread', 'price': 3, 'quantity': 10},
    {'name': 'orange', 'price': 6, 'quantity': 5}
]
get_all_products(conn) # []

batch_insert(conn, products)
get_all_products(conn)
# [(1, 'milk', 12, 20),
#  (3, 'orange', 6, 5),
#  (2, 'bread', 3, 10)]
```

## Подсказки

Для массовой вставки в БД используется функция [execute_values](https://www.psycopg.org/docs/extras.html#psycopg2.extras.execute_values).