# Транзакции

В этом упражнении уже создано соединение с базой данных и следующие таблицы:

`posts`, которая содержит информацию о постах:

- `id` — id поста, первичный ключ, генерируется базой данных автоматически
- `title` — название поста
- `content` — содержание поста
- `author_id` — id автора
- `created_at` – дата создания поста, генерируется автоматически

`comments`, которая содержит информацию о комментариях:

- `id` – id комментария, первичный ключ, генерируется базой данных автоматически
- `post_id` – id поста, к которому оставлен комментарий
- `author_id` – id автора
- `content` – содержание комментария
- `created_at` – дата создания комментария, генерируется автоматически

## src/solution.py

Реализуйте следующие функции:

- `create_post()` – принимает соединение с базой данных и словарь с данными поста. Словарь должен содержать ключи: `title`, `content`, `author_id`. Функция должна создать новый пост и вернуть его `id`.

- `add_comment()` – принимает соединение с базой данных и словарь с данными комментария. Словарь должен содержать ключи: `post_id`, `author_id`, `content`. Функция должна добавить новый комментарий и вернуть его `id`.

- `get_latest_posts()` – принимает соединение с базой данных и количество постов. Возвращает список n последних постов с их комментариями. Каждый элемент списка должен быть словарем с ключами: `id`, `title`, `content`, `author_id`, `created_at`, `comments`. `comments` – это список словарей с ключами: `id`, `author_id`, `content`, `created_at`.


```python
conn = psycopg2.connect('..')

get_latest_posts(conn, 1)
# []

post = {'title': 'My Super Post', 'content': 'text', 'author_id': 42}
create_post(conn, post) # 1

comment = {'post_id': 1, 'author_id': 42, 'content': 'wow such post'}
add_comment(conn, comment) # 1

get_latest_posts(conn, 1)
# [{
# 'id': 1,
# 'title': 'My Super Post',
# 'content': 'text',
# 'author_id': 42,
# 'created_at': datetime.datetime(2022, 7, 19, 14, 32, 37, 123857),
# 'comments': [
#  {
#   'id': 1,
#   'author_id': 42,
#   'content': 'wow such post',
#   'created_at': datetime.datetime(2022, 8, 19, 14, 32, 37, 135319)
#   }
#  ]}]
```