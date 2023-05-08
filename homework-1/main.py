"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

import csv

# with psycopg2.connect(
#     host="localhost",
#     database="north",
#     user="postgres",
#     password="1987Satyam"
# ) as conn:
#
#     with conn.cursor() as cur:
#
#         with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
#             data = csv.reader(file)
#             next(data)
#             for row in data:
#                 cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)
#
# with psycopg2.connect(
#         host="localhost",
#         database="north",
#         user="postgres",
#         password="1987Satyam"
# ) as conn:
#
#     with conn.cursor() as cur:
#         with open('north_data/customers_data.csv', 'r', encoding='utf-8') as file:
#             data = csv.reader(file)
#             next(data)
#             for row in data:
#                 cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="1987Satyam"
) as conn:

    with conn.cursor() as cur:
        with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
            data = csv.reader(file)
            next(data)
            for row in data:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)

conn.close()
